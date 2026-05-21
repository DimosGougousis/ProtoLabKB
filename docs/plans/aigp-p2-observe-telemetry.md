# AIGP Plan 2: Observe Plane — SDK + Telemetry Foundation

> **Status:** ready (after P1) · **Duration:** ~4 weeks · **Depends on:** Plan 1 · **Master plan:** [critically-review-and-recommend-starry-creek.md](./critically-review-and-recommend-starry-creek.md)

## Context

The Observe plane is the **spine** of the harness. It captures, normalizes, and stores agent telemetry across 7 layers (inputs, reasoning, actions, coordination, outputs, state drift, human/org). Without it, the other 4 planes have nothing to evaluate, prove, control, or learn from.

This plan implements the SDK that agent runtimes call into, the OTel collector that processes events, the receivers that ingest from non-OTel sources, and the storage layer (TimescaleDB hot, MinIO cold, Apache AGE for lineage).

## Goal

By the end of this plan:
- Any agent runtime (LangChain, LangGraph, CrewAI, Autogen) can emit OTel-compliant events with 2 lines of integration code
- All 7 telemetry layers have validated Zod schemas in `packages/shared/src/telemetry/`
- 10k synthetic events/sec ingestion sustained
- Layer-4 (coordination) lineage queryable in Apache AGE
- Schema versioning infrastructure in place — events carry `schema_version`, replay can pin

## Dependencies

- Plan 1 complete (CI, license, tests, docs)
- Decision needed: OTel GenAI semconv version pin (current draft as of plan kickoff)

## Deliverables

### 1. Universal envelope + 7 layer schemas

`packages/shared/src/telemetry/`:
- `envelope.ts` — universal envelope (event_id, run_id, agent_id, principal_id, workflow_id, risk_tier, cluster_tag, pattern_tag, layer, ts, schema_version, required_l_level)
- `layer1-input.ts` — InputEvent schema
- `layer2-reasoning.ts` — ReasoningStep schema
- `layer3-action.ts` — ToolCall schema
- `layer4-coordination.ts` — coord events (spawn/message/handoff/terminate/role/authority)
- `layer5-output.ts` — OutputEvent schema
- `layer6-drift.ts` — StateWrite + DriftSnapshot schemas
- `layer7-human.ts` — Human event schemas (approval/escalation/override/dispute/incident)
- `index.ts` — re-exports + ZodSchema discriminated union
- All schemas versioned via package version + `schema_version` field

Test coverage: each schema has roundtrip tests (encode → JSON → decode → equal); known-bad inputs reject with helpful errors.

### 2. OTel GenAI semconv mapping

- Pin OTel GenAI semconv version (record in ADR-006)
- `packages/shared/src/telemetry/otel-mapping.ts` — converts internal events to OTel spans/metrics
- Custom `aigp.*` namespace registered for non-semconv fields
- Span name conventions documented

### 3. TypeScript SDK `@aigp/sdk-ts`

`packages/sdk-ts/`:
- Auto-instrumentation for `@anthropic-ai/sdk`, `openai`, `@aws-sdk/client-bedrock-runtime`
- Manual instrumentation API: `governance.startRun()`, `governance.recordToolCall()`, etc.
- OTel trace + metric exporters
- Configuration: `AIGP_API_URL`, `AIGP_API_KEY`, `AIGP_PRINCIPAL_ID` env vars
- Adapter wrappers as separate sub-packages:
  - `@aigp/sdk-langchain`
  - `@aigp/sdk-langgraph`
  - `@aigp/sdk-crewai`
  - `@aigp/sdk-autogen`
- Each adapter: 2-line integration in user code; tested against framework's example apps

### 4. OTel Collector with custom processor

- Deploy [OTel Collector Contrib](https://github.com/open-telemetry/opentelemetry-collector-contrib)
- Custom processor `aigp_enricher` (Go):
  - Looks up principal_id from auth header → enriches event
  - Looks up agent_id in registry → enriches `risk_tier`, `cluster_tag`, `pattern_tag`
  - Validates schema_version compatibility
  - Drops malformed events with metric
- Configuration in `infrastructure/otel-collector/config.yaml`
- Health endpoint, metrics endpoint

### 5. Receivers

- **OTLP gRPC receiver** — port 4317 (standard)
- **OTLP HTTP receiver** — port 4318 (standard)
- **Webhook receiver** — `POST /v1/events/webhook` for non-OTel sources (Lindy, n8n, Zapier)
- **Bulk batch receiver** — `POST /v1/events/bulk` accepts Parquet for backfill / migration
- All receivers feed into the same NATS subject `observe.raw`

### 6. Normalizer service `apps/observe-svc`

- Subscribes `observe.raw` from NATS
- Validates against Zod schema registry
- Enriches (if not already enriched by collector)
- Routes to NATS subjects: `observe.layer.{1..7}.{event_subtype}`
- Drops malformed events; emits metrics on drop rate
- Writes content-addressed payloads to MinIO; references in event store

### 7. TimescaleDB schema migration

- Extend existing `events` hypertable to support all 7 layers
- One hypertable per layer (or one shared with `layer` column + indexes — decide based on query patterns)
- Continuous aggregates for drift baselines (consumed by Plan 4)
- Retention policies per `risk_tier`:
  - R4: 30d hot, 0 cold
  - R3: 1y hot, 0 cold
  - R2: 3y hot + cold archive
  - R1: 7y hot + cold archive

### 8. MinIO content-addressed payload store

- Deploy MinIO (already in Docker Compose from P1)
- Bucket structure: `aigp-payloads/<sha256-prefix>/<sha256>` (Parquet for batches, raw for individual)
- Lifecycle policies aligned to retention
- Integrated with Postgres event store: events reference payload by SHA-256 only

### 9. Apache AGE installation + lineage materializer

- Install AGE Postgres extension
- Schema: nodes (`Agent`, `Workflow`, `Artifact`, `Memory`, `KGNode`), edges (`SPAWNED`, `SENT`, `PRODUCED`, `CONSUMED`, `WROTE_TO`, `DERIVED_FROM`)
- `apps/observe-svc/src/lineage-materializer.ts` consumes layer-4 + layer-6 events, writes graph
- Cypher query helpers for downstream consumers (G4, G5, G7 plans)

### 10. Schema versioning infrastructure

- Schema package versioned via semver
- Events carry `schema_version` (from package version)
- Replay engine (Plan 3) pins schema_version + scoring_fn_version
- Compatibility matrix documented; breaking changes require migration script

## Implementation tasks

Each task ~30-90 min; commit after each.

**Week 1: Schemas**
1. Create `packages/shared/src/telemetry/envelope.ts` with Zod schema + tests
2. Layer 1 schema + tests (input event)
3. Layer 2 schema + tests
4. Layer 3 schema + tests
5. Layer 4 schemas + tests (6 sub-events)
6. Layer 5 schema + tests
7. Layer 6 schemas + tests (state.write, kb.update, drift.snapshot)
8. Layer 7 schemas + tests (5 human events)
9. ZodSchema discriminated union + index.ts
10. ADR-006: OTel GenAI semconv version pin
11. `packages/shared/src/telemetry/otel-mapping.ts` + tests

**Week 2: SDK + adapters**
12. Skeleton `packages/sdk-ts/` with config loading
13. Anthropic SDK auto-instrumentation
14. OpenAI SDK auto-instrumentation
15. Bedrock auto-instrumentation
16. Manual API: `governance.startRun()` + tests
17. `governance.recordToolCall()` + tests
18. Other manual APIs
19. `@aigp/sdk-langchain` adapter + integration test
20. `@aigp/sdk-langgraph` adapter + integration test
21. `@aigp/sdk-crewai` adapter + integration test
22. `@aigp/sdk-autogen` adapter + integration test

**Week 3: Collector + receivers + normalizer**
23. OTel Collector deployment in Docker Compose
24. Custom `aigp_enricher` processor (Go, in `infrastructure/otel-collector/processor/`)
25. OTLP gRPC + HTTP receivers wired
26. Webhook receiver in `apps/observe-svc`
27. Bulk batch receiver
28. Normalizer service main loop
29. NATS subject routing
30. MinIO integration + content-addressed write

**Week 4: Storage + lineage + load test**
31. Postgres migration: extend events hypertable
32. Continuous aggregates for drift baselines
33. Retention policies per tier
34. Install Apache AGE
35. Define KG schema
36. Lineage materializer service
37. Cypher query helpers
38. Load test: 10k events/sec sustained
39. ADR-007: Schema versioning policy
40. End-to-end demo: LangGraph agent emits → flows through full pipeline → queryable in AGE

## Risk

**Medium.** Main risks:
- OTel GenAI semconv is still evolving — pin version + plan migration policy in ADR-006
- Adapter wrappers may break on upstream framework changes — pin tested versions, add CI integration tests against locked versions
- AGE performance at scale untested — Plan 4 will pressure-test; raise to plan now if early load tests show problems

## Acceptance criteria

- [ ] All 7 layer schemas implemented + tested with roundtrip and rejection cases
- [ ] OTel mapping tested with real OTel collector
- [ ] SDK demos with all 4 frameworks emitting valid events end-to-end
- [ ] 10k synthetic events/sec sustained through full pipeline
- [ ] Layer-4 lineage queryable in AGE (Cypher: `MATCH (a:Agent)-[:SPAWNED]->(b:Agent) RETURN a, b`)
- [ ] Retention policies operational per tier
- [ ] Schema versioning documented in ADR-007

## Verification commands

```bash
# Schema test
pnpm --filter @aigp/shared test

# SDK adapter integration tests
pnpm --filter @aigp/sdk-langchain test:integration
pnpm --filter @aigp/sdk-langgraph test:integration
pnpm --filter @aigp/sdk-crewai test:integration
pnpm --filter @aigp/sdk-autogen test:integration

# Load test
pnpm --filter observe-svc test:load -- --rate 10000 --duration 60

# AGE query
psql -c "SELECT * FROM cypher('aigp', \$\$ MATCH (a:Agent)-[:SPAWNED]->(b:Agent) RETURN a.name, b.name LIMIT 10 \$\$) AS (a TEXT, b TEXT);"

# End-to-end demo
pnpm demo:langgraph
```

## Notes

- The four adapter sub-packages can be parallelized if you have multiple devs.
- AGE is a Postgres extension — no new deployment infrastructure needed beyond `CREATE EXTENSION age;` in migrations.
- Custom OTel processor is Go (collector is Go); first time the repo will have non-TS code — set up basic Go toolchain in P1's CI.
- Bulk batch receiver Parquet decoding may need `apache-arrow` or similar — add as dep.
