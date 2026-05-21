# AIGP Plan 4: G7 Long-Memory + Lineage

> **Status:** ready (after P1, P2, P3) · **Duration:** ~3 weeks · **Depends on:** P1, P2, P3 · **Runs in parallel with:** P5 · **Master plan:** [critically-review-and-recommend-starry-creek.md](./critically-review-and-recommend-starry-creek.md)

## Context

G7 covers patterns 7 (RAISE), 29 (Knowledge graph), 30 (Continuous adaptation). The **core governance question:** has behavior drifted from prior commitments?

This plan brings Apache AGE / lineage online — and other clusters depend on it for traceability and topology queries:
- **G4 (linear pipelines)** needs AGE for handoff/lineage queries
- **G5 (parallel orchestration)** needs AGE for topology and message graph
- **G7 itself** needs AGE for memory provenance and commitment tracking

Without G7, drift detection across long horizons is a slogan, not a capability.

## Goal

By the end of this plan:
- KG schema operational in Apache AGE with multi-hop queries fast enough for runtime use
- Drift detection per `(agent × cluster × tier)` running on TimescaleDB continuous aggregates
- Commitment drift detected on synthetic contradiction agent
- KG poisoning rollback verified under adversarial test
- Causation chain (memory → reasoning → KG → decision) captured at L2 for all R1+ runs

## Dependencies

- P1 (foundation), P2 (observe plane with state.write + kb.update events flowing), P3 (audit chain + policy engine + eval harness)
- AGE installed in P2; this plan extends the schema with G7-specific node/edge types

## Deliverables

### 1. KG schema in Apache AGE

Extends the base AGE schema from P2:

**Nodes:**
- `Agent` (already in P2)
- `Workflow` (already)
- `Memory` — agent's persistent state, scoped by `(agent_id, scope)`
- `KGNode` — entity in the org-wide knowledge graph
- `Commitment` — first-class node for "agent said it would do X" / "agent decided Y"
- `Artifact` — outputs that downstream agents consume

**Edges:**
- `WROTE_TO` (Agent → Memory) — memory write event
- `READ_FROM` (Agent → Memory) — memory read event
- `KG_QUERIED` (Agent → KGNode) — KG read at decision time
- `KG_WROTE` (Agent → KGNode) — KG mutation
- `COMMITTED_TO` (Agent → Commitment) — agent made a commitment
- `CONTRADICTS` (Decision → Commitment) — current decision contradicts prior commitment (computed)
- `CAUSED` (Memory → Decision) — causation edge for explainability

### 2. Memory-write event handler

Consumes layer-6 `state.write` events, writes to AGE as `Agent → WROTE_TO → Memory` with `value_sha256`, `causation_event_id`, `scope`, `key`, `timestamp`. Diff stored at R2+.

### 3. KB-update event handler with diff

Consumes layer-6 `kb.update` events, writes to AGE as `Agent → KG_WROTE → KGNode` with full diff (R2+) or sha256-only (R3, R4). Diff stored in MinIO; AGE has the reference.

### 4. Drift detector with continuous aggregates

`apps/drift-detector/`:
- TimescaleDB continuous aggregates over layer-2 (reasoning), layer-3 (actions), layer-5 (outputs)
- Computes per `(agent_id, cluster_tag, risk_tier, window)`:
  - `hallucination_rate`, `escalation_rate`, `tool_misuse_rate`, `cost_per_run`, `avg_latency_ms`, `policy_violation_rate`, `refusal_rate`, `user_satisfaction`
- Window cadence per tier: R1 continuous, R2 hourly, R3 daily, R4 weekly
- Drift score: cosine distance between current window and rolling baseline
- Threshold per tier
- Alert on threshold breach via NATS `evaluate.drift.alert`

### 5. Drift baselines computed weekly per cohort

- Baseline ID = `(cohort, time_anchor, version)`
- Cohort = agents in same `(cluster_tag, risk_tier)`
- Baseline metrics stored in TimescaleDB; refreshed weekly with bake-in period to avoid noise
- `evaluate.drift.alert` events reference `baseline_id`

### 6. Adversarial test harness

`apps/adversarial-tester/`:
- Maintains golden adversarial sets per pattern (1-30) + per cluster (G1-G8)
- Cases include: prompt injection, contradictory memory writes, fake KG mutations, role drift simulation
- Runs nightly against all R1+ agents (mandatory) and on-demand
- Results captured as `aigp.g7.adversarial_test_result` (drift snapshot extension)
- Failure rate threshold per agent — exceeding triggers G7-P02 or G8-P02 escalation

### 7. G7 telemetry overlay

Already defined in P2 schemas; this plan implements the producers:
- `aigp.g7.memory_writes[]`
- `aigp.g7.kg_query`
- `aigp.g7.kg_subgraph_returned` (refs at low tier; full at R1)
- `aigp.g7.kg_writes[]`
- `aigp.g7.commitment_id`
- `aigp.g7.commitment_drift_score`

### 8. G7-P01 Commitment drift policy

Trigger: current decision contradicts prior commitment captured in memory.

Implementation:
1. On `observe.output.produced` for an agent, query AGE for `Agent → COMMITTED_TO → Commitment` nodes within trailing window
2. Compare current decision semantics (text + structured fields) to commitments via embedding similarity + structured-field mismatch detection
3. If contradiction score > threshold(tier), emit `evaluate.violation.high` with prior-commitment evidence attached

Action: HITL with prior-commitment evidence attached. Policy in `policies/g7/p01-commitment-drift.yaml`.

Golden cases:
- (a) Agent committed "no Q3 launches", later schedules Q3 launch → fires
- (b) Agent committed "use vendor X", later picks vendor Y for unrelated reason → fires
- (c) Agent committed "respond within 2 days", consistently does so → no fire
- (d) Apparent contradiction explained by intervening event → no fire (with intervening_event_id)

### 9. G7-P02 KG poisoning policy

Trigger: adversarial-detected change to KG with high impact score and no human approval.

Implementation:
1. After every `kg.update` for R2+ agents, run adversarial scoring on the diff
2. If `adversarial_impact_score > threshold`, check for human approval in same workflow
3. No approval → emit `evaluate.violation.critical` and rollback the KG mutation

Action: rollback KG mutation, freeze writes for that agent, open incident. Policy in `policies/g7/p02-kg-poisoning.yaml`.

### 10. Causation chain capture

For any R1+ decision, capture:
- All memory reads (Agent → READ_FROM → Memory)
- All KG queries (Agent → KG_QUERIED → KGNode)
- All reasoning steps (layer-2 events)
- The decision (layer-5 event)

Stored as a subgraph in AGE; queryable via Cypher; included in evidence packs.

### 11. G7 dashboard widgets

`packages/web/src/dashboards/g7/`:
- T2 CAIO: KG mutation rate by agent · commitment drift heatmap (agent × time)
- T3 Team: memory-write provenance browser (per-agent timeline of state changes)
- T4 Runtime: live KG query/write stream

### 12. G7 evidence pack template

For any decision involving long-memory, captures the causation chain, memory reads, KG queries, and the decision. References G8 self-attestation pack (keystone). L2 by default; L3 (replayable) for R1.

## Implementation tasks

(Sequenced — each ~1-3 days)

**Week 1: AGE schema + event handlers**
1. Extend AGE schema with G7 node types (Memory, KGNode, Commitment)
2. Extend AGE schema with G7 edge types (WROTE_TO, READ_FROM, KG_QUERIED, KG_WROTE, COMMITTED_TO, CONTRADICTS, CAUSED)
3. Memory-write event handler in `apps/observe-svc`
4. KB-update event handler with diff
5. Causation chain capture logic

**Week 2: Drift + adversarial**
6. Drift detector skeleton with continuous aggregates
7. Per-tier drift cadence (R1 continuous, R2 hourly, ...)
8. Drift score computation (cosine distance)
9. Threshold-per-tier alerting
10. Drift baselines computed weekly per cohort
11. Adversarial test harness skeleton
12. Golden adversarial sets (initial seed for G1, G7)
13. Nightly test runner for R1+ agents

**Week 3: Policies + dashboards + integration**
14. G7-P01 commitment drift policy + golden cases
15. G7-P02 KG poisoning policy + golden cases
16. T2 CAIO dashboard widgets
17. T3 Team dashboard widgets
18. T4 Runtime dashboard widgets
19. G7 evidence pack template
20. End-to-end test: synthetic contradiction agent → G7-P01 fires → HITL with evidence
21. End-to-end test: KG poisoning → G7-P02 fires → rollback verified

## Risk

**Medium.** Risks:
- **Graph query performance at scale untested.** Mitigation: load test at week 2; if AGE buckles, evaluate Neo4j as escape hatch (additive, not destructive — keep AGE for the simple cases).
- **Commitment drift false positives.** Semantic comparison is fuzzy; threshold tuning will take iterations. Mitigation: start with high threshold (low FPR), lower as signal/noise improves.
- **Adversarial test maintenance.** Golden adversarial sets need ongoing curation. Mitigation: budget 10% of plan duration for golden-set work; document the curation process.

## Acceptance criteria

- [ ] AGE schema includes all G7 node and edge types
- [ ] Memory-write and KB-update events materialize correctly in AGE
- [ ] Drift detection running per tier with documented cadence
- [ ] Drift baselines refreshed weekly
- [ ] Adversarial test harness running nightly for R1+ agents
- [ ] G7-P01 detects commitment drift on synthetic contradiction agent
- [ ] G7-P02 detects KG poisoning + rolls back the mutation
- [ ] Causation chain queryable for any R1+ decision
- [ ] All 3 dashboard tiers populated with G7 widgets
- [ ] G7 evidence pack generates and references G8 self-attestation pack

## Verification commands

```bash
# AGE schema test
psql -c "SELECT * FROM cypher('aigp', \$\$ MATCH (a:Agent)-[:COMMITTED_TO]->(c:Commitment) RETURN a, c LIMIT 10 \$\$) AS (a TEXT, c TEXT);"

# Drift detector test
pnpm --filter drift-detector test:integration

# Adversarial test runner
pnpm --filter adversarial-tester run --tier R1 --pattern 7

# G7-P01 golden cases
pnpm --filter g7-policies test:golden -- --policy g7-p01

# G7-P02 + rollback
pnpm test:integration -- --grep "kg poisoning rollback"
```

## Notes

- AGE schema extensions should be additive — don't break the schema P2 established.
- Commitment drift threshold needs tuning per cluster; start with conservative defaults, expose as Rego config so customers can override.
- This plan and Plan 5 run in parallel — coordinate on shared touchpoints (AGE schema, MCP server interactions).
- The adversarial test harness becomes a long-term asset; budget for ongoing golden-set curation in operations.
