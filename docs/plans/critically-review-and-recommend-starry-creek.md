# Critically Review & Recommend: AI Governance Platform — Agentic Harness

> **Status:** brainstorm in progress. This document captures locked decisions; sections marked _in design_ will be filled as the brainstorm closes. Final spec lands at `docs/superpowers/specs/<date>-ai-governance-platform-harness-design.md` once approved.

## Context

The user owns [github.com/DimosGougousis/ai-governance-platform](https://github.com/DimosGougousis/ai-governance-platform) — a self-hosted observability/governance plane for AI agents owned elsewhere. Solo-author prototype.

- **Stack:** Next.js 14 + Fastify 4 + Postgres 16 / TimescaleDB + Redis 7 + NATS JetStream, all TypeScript, pnpm/Turborepo
- **Built-in primitives:** agent registry, OTLP/webhook/bulk ingestion, 7 Zod data contracts (C1–C7), ARI scoring, MI9 containment levels (0–4), SAFEST (112 items), EU AI Act Art. 11 / DORA / IAMA, 8 RBAC roles, 4 dashboard tiers
- **Critical gaps:** 5 commits / ~2 months stale, no license, no CI, no tests, audit-as-schema-only, no policy DSL (hardcoded TS in `packages/api/src/routes/governance.ts`), no eval harness (scoring unfalsifiable), no HITL workflow, no platform self-observability, no lineage / knowledge graph, no MCP / tool adapters

The user wants the platform extended to govern 30 multi-agent execution patterns (ReAct, ToT, swarms, debate, MetaGPT, KG, etc.). This plan addresses the GitHub repo as the authoritative target. A divergent local workspace at `C:\Users\dimos\AIGovernance` exists but is **not** a clone of that repo (different focus, auth/RBAC oriented) — out of scope for this review.

## Lens (locked)

**A. Govern the patterns.** Extend platform contracts, scoring, audit, policy DSL, and evals so it can detect, score, and enforce policy on each of the 30 patterns when used by external agents. Stays inside current product scope. ~6–10 focused weeks for core; longer for full pattern coverage.

Lenses considered and deferred: B (execute the patterns — major scope expansion), C (apply patterns internally — engineering quality, can fold in later), D (mixed phasing).

## Harness mental model — 5 jobs, 5 planes

Every governance harness does five things: **observe, evaluate, prove, control, learn**.

| Plane | Job | Components | Storage |
|---|---|---|---|
| **OBSERVE** | Capture and normalize agent telemetry | SDK (TS/Py), OTel collector with custom processor, OTLP/webhook/bulk receivers, normalizer service, lineage materializer | TimescaleDB hypertable, MinIO/S3 cold (Parquet, content-addressed), Apache AGE on Postgres for lineage, Redis hot lookup |
| **EVALUATE** | Decide whether observed behavior was OK | Policy DSL (YAML→Rego on OPA), realtime evaluator service, eval harness with replay, drift detector, golden-dataset registry | Policies in git + Redis hot, eval results in TimescaleDB, golden sets in MinIO indexed in Postgres |
| **PROVE** | Make events tamper-evident, exportable, regulator-ready | Append-only audit chain (Postgres + Merkle hashes), evidence-pack generator (Art. 11/12, DORA, SOC2, GDPR DSAR templates), signed-export, optional Sigsum anchor | Postgres append-only with INSERT-only triggers; MinIO immutable evidence packs |
| **CONTROL** | Intervene before/during/after agent behavior | MCP Governance Server (`check`/`requestApproval`/`escalate`/`report`), HITL review queue, containment engine, break-glass | Queue in Postgres + Redis, containment policies versioned, break-glass events in audit chain |
| **LEARN** | Close the loop — feedback → policy/eval updates | Feedback capture, incident workflow, proposal pipeline (PR-style), drift→action | Postgres + git + MinIO |

Inter-plane spine: **NATS JetStream** (already in stack). Each plane is a Fastify service / module sharing one Zod schema registry. **Solo-dev shape: modular monolith now, extract services as load profiles diverge.**

## Cross-cutting tech decisions

| Decision | Choice | Rationale |
|---|---|---|
| Inter-plane bus | NATS JetStream | Already in stack; durable; replayable |
| Schema registry | Zod + central package | Already your pattern; extend |
| Lineage graph | Apache AGE on Postgres | Avoid Neo4j until queries demand it |
| Policy engine | OPA + YAML→Rego compiler | Mature, regulator-aware, replayable |
| Audit chain | Postgres append-only + optional Sigsum anchor | No new DB; external anchor for L2 |
| Control surface | MCP server | Standard protocol for agent runtimes to call governance |
| Object store | MinIO local / S3 prod | Standard, fits Docker Compose |
| Identity | Existing JWT/RBAC + AGE principal graph | Builds on auth |
| Service shape | Modular monolith now | Solo dev; extract when load diverges |

## 7 telemetry layers — what gets monitored

| # | Layer | Examples | Regulatory tie-in |
|---|---|---|---|
| 1 | Inputs | prompt, principal, attached context, PII, injection attempts | GDPR data minimization; AI Act Art. 15 cybersecurity |
| 2 | Reasoning | model+version, tokens, latency, CoT, branches, confidence | AI Act Art. 13 transparency; SOC2 availability |
| 3 | Actions | tool calls, parameters, return values, side effects, $, rate | AI Act Art. 12 logging; DORA operational resilience |
| 4 | Coordination | agent topology, message graph, role assignments, authority delegation | AI Act Art. 14 oversight (multi-agent edition) |
| 5 | Outputs | content, action outcomes, sensitivity, factuality, hallucinations | AI Act Art. 13; brand & legal exposure |
| 6 | State drift | memory writes, KB updates, behavior trend, adversarial robustness | NIST AI RMF Manage; ISO 42001 monitoring |
| 7 | Human/org | approvals, escalations, overrides, disputes, incidents | AI Act Art. 14; DORA incident reporting |

Repo today partially instruments layer 3 (ingestion) and layer 7 (RBAC). Layers 1, 2, 4, 5, 6 not structurally instrumented. Detailed schemas captured in **§A** (in design).

## 8 governance archetype clusters — collapse 30 patterns to 8

Patterns within a cluster share telemetry, policy templates, dashboard widgets. Build 8 archetypes; cover all 30.

| Cluster | Patterns | Shared telemetry primitive | Hardest governance question |
|---|---|---|---|
| **G1 Single-agent reasoning** | 1, 2, 4 | reason→act→observe trace + self-critique log | When does a loop become runaway? |
| **G2 Branch exploration** | 3, 8 | branch tree with scores + abandoned paths | Did the agent honestly explore, or fake breadth? |
| **G3 Routing & specialization** | 9–12 | classification log + downstream-handler audit | Why did this go *here* and not elsewhere? |
| **G4 Linear pipelines** | 5, 13, 20 | document lineage / handoff DAG | Where did bad data enter, what downstream is poisoned? |
| **G5 Parallel orchestration** | 14, 15, 17, 18, 19 | agent topology + message graph + role events | Who actually decided this? Who is responsible? |
| **G6 Deliberative / adversarial** | 16 | proposer–arbiter–dissent log | Was dissent surfaced or suppressed? |
| **G7 Long-memory / lineage** | 7, 29, 30 | state-change events + KG deltas + drift metrics | Has behavior drifted from prior commitments? |
| **G8 Constraint & meta-governance** | 6, 25, 26, 27, 28 | policy-eval log + escalation log + hash-chained audit | Is the harness *itself* trustworthy? |

Per-cluster designs in **§B** (in design).

## 5 trust verification levels — evidence depth

- **L0 Self-asserted** — agent claims X
- **L1 Logged** — telemetry confirms X *(most "AI observability" stops here)*
- **L2 Tamper-evident** — hash-chained audit proves order + integrity
- **L3 Replayable** — eval harness re-runs same inputs, gets equivalent outputs
- **L4 Formally verified** — property holds across all permitted inputs

EU AI Act high-risk realistically needs L2+L3. DORA incidents need L2. Internal low-risk use can live at L1. Repo today: **L1 for ingested events, L0 for ARI/MI9 scoring** (no replay).

Per-pattern × event evidence depth — **§C** (in design).

## Risk-tier model (locked)

Multi-dimensional, single-tier-rollup. Single tier preserves UX simplicity; dimensions explain *why* and *what to change*.

### Six dimensions

| Code | Dimension | Levels |
|---|---|---|
| A | Regulatory class | A0 out-of-scope · A1 minimal · A2 limited · A3 high (Annex III) · A4 unacceptable (Art. 5) |
| B | Blast radius | B0 sandbox · B1 single-user advisory · B2 single-user action · B3 team · B4 org/customer · B5 public/systemic |
| C | Reversibility | C0 fully · C1 reversible-with-effort · C2 bounded-window · C3 irreversible |
| D | Data sensitivity | D0 public · D1 internal · D2 internal-sensitive · D3 PII · D4 special category |
| E | Autonomy | E0 suggestion · E1 approval-gated · E2 time-bounded · E3 fully autonomous · E4 self-modifying |
| F | Velocity | F0 async · F1 same-day batch · F2 near-RT · F3 RT · F4 safety-critical |

### Five tiers (composite, Rego-defined, customer-overridable)

| Tier | Code | Default formula (illustrative) |
|---|---|---|
| Prohibited | R0 | A4, OR (A3 ∧ C3 ∧ E3+) without override |
| Critical | R1 | A3, OR B5, OR (D4 ∧ C2+), OR E4, OR F4 |
| Elevated | R2 | (B3-B4), OR (D2-D3), OR (E2-E3 ∧ C2+), OR (F3 ∧ B2+) |
| Standard | R3 | A2, OR (B2 ∧ E1), OR (D2 ∧ E1) |
| Minimal | R4 | else |

### Tier-to-governance gate table

| Plane | R4 Minimal | R3 Standard | R2 Elevated | R1 Critical | R0 Prohibited |
|---|---|---|---|---|---|
| **Observe** | L1 logged, 10% sampled, 30d retention | L1 logged, 100%, 1y retention | **L2** tamper-evident, 100%, 3y retention | **L2** + lineage graph, 100%, 7y retention | Blocked event chained |
| **Evaluate** | Realtime advisory, weekly drift | Realtime enforced, daily drift, weekly replay | Realtime enforced, hourly drift, daily replay, golden-set required | Realtime enforced, continuous drift, per-run replay, golden + adversarial set | n/a |
| **Prove** | Logged only | Logged + retention | Hash-chain + on-demand evidence pack | Hash-chain + auto evidence pack per run + external anchor | Block reason chained |
| **Control** | Optional MCP gate | MCP gate required for irreversible (C2+) tools | MCP gate required all tools, HITL on first violation, containment armed | MCP gate required all tools, HITL on every action, break-glass armed | All blocked at MCP gate |
| **Learn** | Aggregated feedback only | Per-violation feedback | Per-event feedback, incident workflow on violation | Per-event feedback, incident per deviation, quarterly tier review | Block-cause review |

### Tier assignment lifecycle

- **At registration:** owner declares A/D/E; platform infers B/C from tool manifest; F measured at runtime; Rego policy computes initial tier; tier change audit-chained.
- **Continuous validation:** observed behavior drives drift detector; observed > declared → auto-promote; promotion audit-chained, owner notified.
- **Auto-promote, never auto-demote.** Demotion requires explicit owner request + review.
- **Scheduled review:** R1 quarterly · R2 semi-annual · R3 annual · R4 on change · R0 by exception.

### Multi-agent workflow tier

- Workflow tier = **max(participating agents' tiers)** — containment, not averaging.
- Cross-tier delegations flagged. Downward delegation (high→low) requires explicit policy permission + audit.

### Integration with existing repo concepts

| Existing | What it really is | Clean role |
|---|---|---|
| Dashboard tiers (T1–T4) | Audience tiers (who sees what) | Stay as audience surface; rename in docs to avoid collision |
| ARI score | Scalar risk *signal* | One input among many to drift detection; **not** the canonical tier |
| MI9 levels (0–4) | Automated *response* level when something goes wrong | Reactive level triggered by violations; **not** baseline classification |

```
Risk tier R0–R4   →  what governance applies (proactive baseline)
       ↓
Behavior signals  →  ARI, hallucination rate, escalation rate, ...
       ↓
Violation         →  policy hit
       ↓
MI9 level 0–4     →  what response triggers (reactive)
       ↓
Audience          →  which dashboard tier surfaces it (T1–T4)
```

### Locked forks (risk-tier model)

1. **Tier formula** = Rego policy bundle, customer/industry-overridable; default bundle shipped.
2. **R0 override** = dual path. **Executive-override-with-audit** (fast, single named exec, regulator-disclosed) AND **appeals workflow** (slow, multi-stakeholder review). Both audit-chained, both feed Learn.
3. **Custom dimensions** = 6 platform-fixed for MVP (cross-customer benchmarking); customers add *score modifiers* in Rego, not new dimensions.
4. **Naming** = ship both — `R0-R4` codes in API/DB; named labels (Prohibited/Critical/Elevated/Standard/Minimal) in UI/reports.
5. **R0 enforcement** = all three (MCP gate, evaluate plane, observe ingestion) — defense-in-depth.

## Locked forks (formerly open)

1. **Control surface.** **MCP server primary, SDK fallback** for runtimes that don't speak MCP. The SDK is a thin shim that calls the same MCP endpoints internally for consistency — one authority surface, two ingress paths.
2. **ARI/MI9 scoring location.** Move from hardcoded TS in `packages/api/src/routes/governance.ts` to **versioned scoring functions in the eval harness**. Each score is reproducible from `(event_set_id, policy_version, scoring_fn_version)`. Old scores carry their version; re-evaluation is non-destructive (creates new score record, never mutates).
3. **Audit chain anchor.** **Internal Postgres-append-only + optional Sigsum anchor for R1** (and R0 block events). R2/R3 internal-only by default; opt-in to external anchor for high-stakes customers.

## Sequencing

### Brainstorm sequence (used for this design)

**F → A → B (per cluster) → C in parallel.** Risk tier gates everything; layers say what's emitted; clusters say what's pattern-specific; trust levels say how strong evidence has to be. *Closed.*

### Implementation: 6-plan breakdown (~25 weeks total)

Each plan in its own file under `C:\Users\dimos\.claude\plans\` (created post-approval). Plans 4 and 5 run in parallel; everything else sequential.

| # | File (target) | Title | Duration | Depends on |
|---|---|---|---|---|
| 1 | `aigp-p1-foundation.md` | Foundation & Repo Hygiene | ~2 wk | — |
| 2 | `aigp-p2-observe-telemetry.md` | Observe Plane: SDK + Telemetry | ~4 wk | P1 |
| 3 | `aigp-p3-g8-meta-governance.md` | G8 Meta-Governance: Audit + Policy + HITL + Eval | ~6 wk | P1, P2 |
| 4 | `aigp-p4-g7-lineage.md` | G7 Long-Memory + Lineage *(parallel with P5)* | ~3 wk | P1, P2, P3 |
| 5 | `aigp-p5-g1-g3-g4-mcp.md` | G1 + G3 + G4 + MCP Governance Server *(parallel with P4)* | ~4 wk | P1, P2, P3; G4 needs P4 |
| 6 | `aigp-p6-g2-g5-g6-trust-hardening.md` | G2 + G5 + G6 + §C Trust + Hardening | ~6 wk | P1–P5 |

#### Plan 1 — Foundation & Repo Hygiene
**Why first.** No license, no CI, no tests = no engineer can credibly contribute. Unblocks everything.
**Deliverables:** License (Apache-2.0 or AGPL-3.0 — pick at plan start) · GitHub Actions CI (typecheck, lint, test, build, docker-build) · Vitest with coverage gates (>70% on changed files) · ESLint + Prettier CI-enforced · ADR directory + template · README rewrite reflecting v3 architecture honestly · CONTRIBUTING / CODE_OF_CONDUCT / SECURITY · Docker Compose dev validated end-to-end · Existing schema audit (dead code, unused tables).
**Risk:** low. **Acceptance:** CI green on trivial PR; clone-to-dev-server <10 min for new contributor.

#### Plan 2 — Observe Plane: SDK + Telemetry Foundation
**Why next.** Nothing else works without telemetry. This is the spine.
**Deliverables:** Universal envelope + 7 layer schemas (Zod) in `packages/shared/src/telemetry/` · OTel GenAI semconv pinned version; `aigp.*` namespace defined · TypeScript SDK `@aigp/sdk-ts` with auto-instrumentation · Adapter wrappers (LangChain, LangGraph, CrewAI, Autogen) · OTel collector with enrichment processor (principal, tier, cluster_tag, pattern_tag) · Receivers (OTLP gRPC/HTTP, webhook, bulk batch) · Normalizer service `apps/observe-svc` with Zod + NATS publish · TimescaleDB schema migration (extend events; add 7-layer tables) · MinIO content-addressed payload store · Apache AGE installation + lineage materializer · Schema versioning infrastructure.
**Risk:** medium (OTel semconv still evolving; vendor changes can break wrappers). **Acceptance:** 10k synthetic events through full pipeline; layer-4 lineage queryable; SDK demos with all 4 frameworks emitting valid events.

#### Plan 3 — G8 Meta-Governance: Audit + Policy + HITL + Eval
**Why next.** G8 is the harness's self-portrait. Without G8 working, every other cluster's claims are unfalsifiable.
**Deliverables:** Append-only `audit_chain` Postgres table + INSERT-only triggers · Merkle hash chain (SHA-256 over RFC 8785 canonical JSON) · Hourly chain verifier + freeze-on-break (G8-P01) · Optional Sigsum anchor (R0/R1) · OPA + YAML→Rego compiler · Policy registry (versioned, signed, git, Redis hot) · Realtime evaluator service `apps/evaluate-svc` · Eval harness skeleton (replay engine, golden-set manager, regression runner) · HITL queue (Postgres + Redis + SSE) · HITL UI in Next.js (T3 + T4 dashboards) · Appeals workflow + executive-override path (both audit-chained) · 6 G8 policies (P01–P06) with golden cases · "Harness Self-Attestation" evidence pack generator · G8 dashboard widgets (T1/T2/T3/T4) · Risk-tier Rego bundle + agent registration flow + lifecycle + auto-promote.
**Risk:** high (Merkle chain bugs are catastrophic; demands fault-injection testing). **Acceptance:** all G8 acceptance criteria; chain break detected within 1 cycle under fault injection; evidence pack offline-verifiable.

#### Plan 4 — G7 Long-Memory + Lineage *(parallel with P5)*
**Why now.** Brings Apache AGE / lineage online — G4 and G5 depend on it for traceability and topology queries.
**Deliverables:** KG schema in AGE (entities, relationships, commitments) · Memory-write + KB-update event handlers · Drift detector (TimescaleDB continuous aggregates) · Drift baselines per agent × cluster × tier · Adversarial test harness + golden adversarial sets · G7 telemetry overlay · G7 policies (G7-P01 commitment drift, G7-P02 KG poisoning) · Causation chain capture (memory → reasoning → KG → decision) · G7 dashboard widgets (T2/T3/T4) · G7 evidence pack template.
**Risk:** medium (graph query performance at scale untested). **Acceptance:** all G7 acceptance criteria; commitment drift detected on synthetic contradiction agent; KG poisoning rollback verified.

#### Plan 5 — G1 + G3 + G4 + MCP Governance Server *(parallel with P4)*
**Why now.** G1 is highest production volume; G3 routes everything; G4 unblocks pipelines. MCP server enables external agent runtimes to call governance.
**Deliverables:** G1: ReAct loop tracker, Reflexion convergence detector with honesty check, Self-RAG efficiency monitor · G1 policies G1-P01 through G1-P06 · G1 SDK auto-instrumentation · G1 dashboards + evidence pack · G3: routing classifier instrumentation, low-confidence fallback handler · G3 policies G3-P01, G3-P02 · G3 dashboards + evidence · G4: pipeline lineage capture (uses AGE from P4) · G4 policies G4-P01, G4-P02 · G4 dashboards + evidence · MCP Governance Server `apps/mcp-governance` exposing 4 tools: `check`, `requestApproval`, `escalate`, `report`.
**Risk:** medium (rubber-stamping detection G1-P06 is novel; needs golden-set tuning). **Acceptance:** all G1/G3/G4 criteria; MCP server responds to all 4 tools; external LangGraph test agent successfully calls the gate end-to-end.

#### Plan 6 — G2 + G5 + G6 + §C Trust Levels + Hardening
**Why last.** Sophisticated patterns + cross-cutting trust levels + ops hardening. Closes coverage and prepares for production.
**Deliverables:** G2: branch tree capture + decisiveness metric + faked-breadth detector + policies + dashboards + evidence · G5: topology snapshot + message graph in AGE + role-drift detection + policies + dashboards + evidence · G6: dissent event capture + arbiter decision records + policies + dashboards + evidence · §C trust-level enforcement: `required_l_level` computation + propagation + mismatch detector · L3 replay engine: WASM/Rego scoring functions, content-addressed storage · L4 scope documented (R0 enforcement, chain insert, tier promotion) — deferred to post-MVP · ARI/MI9 reimplemented as versioned scoring functions in eval harness (closes locked fork #2) · Performance hardening (ingestion throughput, audit chain insert latency, AGE query optimization) · Multi-tenancy preparation · Customer-facing policy authoring UI scaffolding.
**Risk:** medium-high (performance unknowns; multi-tenant scope can creep). **Acceptance:** all G2/G5/G6 acceptance criteria; trust-level mismatches fire `evaluate.trust.violation`; ARI/MI9 reproducible bit-identically across replays; ingestion sustains 1k events/sec/agent without backpressure.

## Verification (to be detailed after design closes)

- Replay 10 representative agent runs through harness, validate L1+L2+L3 evidence produced
- Run policy regression suite against 90 days of synthetic events
- Generate AI Act Art. 11 evidence pack for a sample R1 workflow; review against actual regulator template
- Drift detector: inject synthetic drift, verify detection within target window per tier
- Tier auto-promotion: register agent at R3, induce R2 behavior, verify promotion + audit chain entry
- MCP gate: from external agent, request denied action, verify all three enforcement points fired

## §A — Layer-by-layer telemetry design (locked)

### Universal envelope

```ts
// every event carries this
{
  event_id, run_id, parent_event_id?, agent_id, principal_id, workflow_id,
  risk_tier: 'R0..R4', cluster_tag: 'G1..G8', pattern_tag: 1..30,
  layer: 1..7, ts, schema_version, required_l_level
}
```

Full Zod schemas live in `packages/shared/src/telemetry/` (canonical home; reference brainstorm conversation for inline schemas).

### Per-layer summary

| Layer | Event(s) | OTel mapping | Cluster overlays |
|---|---|---|---|
| **1 Inputs** | `observe.input.received` | extends `gen_ai.prompt`, `gen_ai.request.*`; custom `aigp.injection.*`, `aigp.pii.*`, `aigp.principal.*` | G1 loop_invocation_index · G3 intent_inferred · G7 memory_keys_loaded |
| **2 Reasoning** | `observe.reasoning.step` | `gen_ai.system`, `gen_ai.usage.*`, `gen_ai.response.finish_reasons`; custom `aigp.cot.*`, `aigp.branches.*`, `aigp.self_critique.*` | G1 loop_count + self_critique R3+ · G2 branches mandatory + companion event · G6 dissent capture |
| **3 Actions** | `observe.tool.call` | `gen_ai.tool.*`; custom `aigp.tool.side_effect.*`, `aigp.tool.preflight.*` | G3 routing_classifier_version · G7 kg_query, kg_subgraph_hash |
| **4 Coordination** | `observe.coordination.{spawn,message,handoff,terminate,role,authority}` | no semconv; custom `aigp.coordination.*` + OTel span links | G5 topology + message graph mandatory R3+ · G6 dissent type R2+ · G7 authority chain R2+ |
| **5 Outputs** | `observe.output.produced` | extends `gen_ai.completion`; custom `aigp.output.classification.*` | G2 chosen_vs_alternatives_diff · G6 arbiter_decision_record |
| **6 State drift** | `observe.{state.write,kb.update,drift.snapshot}` | drift metrics as OTel instruments `aigp.drift.*` | G7 kb.update + diff R2+ · G8 harness self-drift |
| **7 Human/org** | `observe.human.{approval,escalation,override,dispute,incident}` | no semconv; custom `aigp.human.*` | G8 approval chain + regulator notification R1 |

### Tier-graded mandatory fields (principle)

- **R4 minimal** — sha256 only for content, no payload, no auxiliary signals; 10% stratified sampling
- **R3 standard** — redacted payload + auxiliary signals (PII, classification)
- **R2 elevated** — full payload + delegation chains + factuality signals + preflight checks for all tools
- **R1 critical** — everything R2 + adversarial signals + ground-truth comparisons + multi-approver chains + confidence
- **R0 prohibited** — block event chained, attempt audit-trailed, no payload

Per-layer per-tier matrices captured inline during brainstorm; canonical Zod schemas in `packages/shared/src/telemetry/`.

### Cross-layer notes

- **Cost roll-up.** `cost_usd` appears in layers 2/3/5/6; aggregator emits `aigp.cost.run_total` per `run_id`.
- **Content addressing.** Every payload has full + sha256; audit chain references sha256 only; payload retrieval via MinIO content store. Reconciles data minimization (low tier) with full evidence (high tier).
- **Forbidden, not optional.** Blank cells in tier matrices = forbidden by data minimization. R4 must NOT capture `prompt_text`. Protects GDPR posture.
- **Schema versioning.** Every event carries `schema_version`. Replay must pin schema + scoring fn version to reproduce.
- **R4 sampling.** Stratified by `cluster_tag` and `pattern_tag` so all clusters/patterns retain visibility at low retention.

## §B — Cluster-by-cluster pattern coverage

_Locked: G8 first. Other clusters in design._

### §B.G8 — Constraint & Meta-Governance (locked)

**Patterns covered:** 6 (Constraint-driven planning), 25 (Guardrails & policy enforcement), 26 (HITL with escalation), 27 (Continuous eval & monitoring), 28 (Audit trail).

**Why first.** G8 patterns *are* the harness. Hardens audit, policy, eval, HITL before any other cluster makes claims that depend on them. Without G8, claims about G1–G7 are unfalsifiable. The five G8 patterns map almost one-to-one to the five planes:

| G8 pattern | Plane it materializes |
|---|---|
| 28 Audit trail | PROVE |
| 25 Guardrails | EVALUATE (realtime) |
| 27 Continuous eval | EVALUATE (offline) + LEARN |
| 26 HITL escalation | CONTROL |
| 6 Constraint-driven planning | All five (cross-cutting) |

**Internal sequencing within G8:** **28 → 25 → 27 → 26 → 6**. Audit chain is the substrate; guardrails write to it; eval reads it; HITL needs eval signals; constraint-driven planning needs all of the above.

#### Telemetry overlay (extends universal layers)

| Pattern | Extra fields / events on top of universal |
|---|---|
| **6 Constraint-driven** | `aigp.g8.constraint.consulted`, `aigp.g8.constraint.violated_path`, `aigp.g8.constraint.escalation_threshold` |
| **25 Guardrails** | `evaluate.guardrail.{input,tool_param,output}.fired` carrying `guardrail_id`, `version`, `decision`, `reason`, `downstream_action` |
| **26 HITL** | `aigp.g8.hitl.queue_age_ms`, `aigp.g8.hitl.checkpoint_id`, `aigp.g8.hitl.complexity_score`, `aigp.g8.hitl.appeals_status` |
| **27 Continuous eval** | `evaluate.replay.run`, `evaluate.drift.alert`, `evaluate.regression.detected`, `evaluate.rollback.triggered` |
| **28 Audit trail** | `prove.chain.append`, `prove.chain.verify`, `prove.evidence_pack.generate`, `prove.export.signed` |

#### Policy templates (6 representative)

| ID | Trigger | Severity | Action | Tier scope |
|---|---|---|---|---|
| **G8-P01 Chain integrity** | `prove.chain.verify` result=broken | critical | Alert auditors, freeze new appends, open incident | All |
| **G8-P02 Guardrail bypass** | `observe.tool.call` preflight=deny AND tool executed | critical | Suspend agent, MI9→4, audit | R2+ |
| **G8-P03 HITL SLA breach** | `observe.human.escalation` `time_to_decision_ms > sla(tier)` | high | Escalate to backup, page on-call | R1+ |
| **G8-P04 Drift breach** | `evaluate.drift.alert` `drift_score > threshold(tier)` | drift-scaled | Open incident, propose policy/eval review | R2+ |
| **G8-P05 Constraint disclosure** | `observe.output.produced` to external destination | medium | Require disclosure annotation; emit if missing | R2+ (Art. 13) |
| **G8-P06 Regulator notification** | `observe.human.incident` severity≥high for R1 | critical | Open regulator notification workflow + auto evidence pack | R1 |

Each policy carries `policy_id`, `policy_version`, `golden_set_id`, `regulation_refs`, `applicable_clusters`.

#### Eval scenarios (golden cases per policy)

| Policy | Golden case kinds |
|---|---|
| **G8-P01** | (a) 1000 events, 1 tampered → expect detect ≤1 cycle; (b) clean replay → identical hashes; (c) anchor mismatch → alert |
| **G8-P02** | (a) denied tool called 10× → 10 fires; (b) allowed tool / denied params → fire; (c) nested call chain bypassing gate → fire |
| **G8-P03** | (a) R1 escalation, SLA timeout → fire + backup; (b) R3 same → no fire (scope); (c) handoff → chain captured |
| **G8-P04** | (a) +5% hallucination_rate → alert in window; (b) drift below threshold → no fire; (c) sustained drift → escalation |
| **G8-P05** | (a) external output, no disclosure → fire; (b) external output with disclosure → pass; (c) audit-only output → no fire |
| **G8-P06** | (a) high-severity R1 incident → notification + pack; (b) R3 same severity → no notification |

Golden sets versioned in MinIO, indexed in Postgres, regression-tested on every policy / scoring-fn change.

#### Dashboard widgets

| Dashboard tier | G8 widgets |
|---|---|
| **T1 Board** | Audit chain integrity (boolean + last-verify-ts) · Critical incidents (R1) by month · Regulator notifications sent / outstanding |
| **T2 CAIO** | Policy version diff history · Drift heatmap across R1/R2 agents · HITL queue depth + SLA per tier |
| **T3 Team** | Per-agent guardrail fire rate (top 10) · Per-policy fire rate over time · Open incidents owned by team |
| **T4 Runtime** | Realtime guardrail fire stream · HITL queue (time-in-queue + assignee) · Audit chain append rate |

#### Evidence pack — "Harness Self-Attestation"

Generated weekly + on-demand. Scope: time range, agents/tiers covered.

1. Audit chain integrity: events count, verifications passed, chain proofs
2. Policy enforcement summary: fires by policy, decisions, overrides
3. Drift detection summary: alerts, resolutions, MTTD/MTTR
4. HITL summary: approvals, time-to-decide, SLA breaches
5. Continuous eval summary: replays run, regressions caught, regressions deployed (with rollbacks)
6. Cross-cluster references: every other cluster's evidence pack references this one — **G8 is the keystone**
7. Signed by platform key (+ optional external auditor co-sign)

**Cascade rule.** If G8-P01 chain integrity fails, all evidence packs generated *after* the break point are flagged `PENDING_REVERIFICATION` until chain is restored. This makes G8 trust load-bearing for the whole product.

#### Implementation footprint

```
packages/api/src/governance/g8/
├── audit-chain/        # Merkle chain, verifier, anchor service (Sigsum opt-in)
├── policy-engine/      # OPA wrapper, YAML→Rego compiler, policy registry
├── eval-harness/       # replay engine, regression runner, golden-set manager
├── hitl/               # queue, assignment, decision capture, appeals workflow
├── evidence-pack/      # generator, signer, exporter
└── shared/             # G8 telemetry overlays, constants
packages/api/migrations/
└── 0xx_audit_chain.sql # append-only table, INSERT-only triggers
packages/web/src/dashboards/g8/
└── widgets per T1/T2/T3/T4
```

#### G8 done — acceptance criteria

- Audit chain verified hourly; breaks detected within 1 cycle; broken chain freezes new appends
- All policy fires logged to audit chain, queryable, replayable, regression-tested
- HITL queue with SLA tracking; escalations and overrides audit-chained; appeals workflow operational
- Drift detector running; alerts open incidents; incidents close via Learn workflow
- Evidence packs generated on demand for any time range; signed; verifiable offline
- Self-attestation pack generated weekly; cascading `PENDING_REVERIFICATION` works under fault injection

### §B.G1 — Single-agent reasoning loops (locked)

**Patterns covered:** 1 (ReAct), 2 (Reflexion), 4 (Self-RAG).

**Core governance question:** When does a reasoning loop become runaway?

**Why this cluster next:** highest production volume; lowest-risk first deliverable for end users; fastest visible value; covers a large slice of typical agent traffic.

#### Telemetry overlay

| Pattern | Extra fields / events |
|---|---|
| **1 ReAct** | `aigp.g1.react.loop_index`, `last_observation_used`, `goal_drift_score`, `max_loops_threshold` |
| **2 Reflexion** | `aigp.g1.reflexion.iteration_index`, `criteria_id`, `score_before`, `score_after`, `improvement_rate`, `gave_up` |
| **4 Self-RAG** | `aigp.g1.selfrag.retrieved_count`, `relevance_decision`, `retrieval_iterations`, `context_efficiency` |

#### Policy templates (6 representative)

| ID | Trigger | Severity | Action | Tier |
|---|---|---|---|---|
| **G1-P01 Loop budget** | `loop_index > max_loops_threshold(tier)` | high | Suspend loop, escalate, audit | All |
| **G1-P02 Goal drift** | `goal_drift_score > 0.5` for 2+ consecutive steps | medium | Surface to HITL review queue | R2+ |
| **G1-P03 Reflexion non-convergence** | `improvement_rate < 0.05` for 2+ iterations AND not at threshold | medium | Auto-stop, return best version with quality flag | All |
| **G1-P04 Infinite refinement** | `iteration_index > 5` | high | Hard stop, audit | All |
| **G1-P05 Retrieval irrelevance** | `context_efficiency < 0.2` | low | Alert, propose retrieval policy review | R3+ |
| **G1-P06 Self-critique honesty** | inconsistent before/after pattern (rubber-stamping detection) | medium | Flag for adversarial test set | R2+ |

**G1-P06 is the subtle one** — detects when Reflexion's self-critique is rubber-stamping (always reports "improved" with the same delta regardless of input). A common failure mode that defeats the entire pattern.

#### Eval scenarios

| Policy | Golden case kinds |
|---|---|
| G1-P01 | (a) unsolvable task → expect fires at threshold; (b) solvable within budget → no fire |
| G1-P02 | (a) deflected goal → fires; (b) consistent goal → pass |
| G1-P03 | (a) 5 iterations, <5% improvement each → fires + auto-stop; (b) converges in 3 → pass |
| G1-P04 | (a) iteration cap removed → expect hard-stop at 5; (b) iteration ≤5 → pass |
| G1-P05 | (a) 50 retrieved, 1 used → fires; (b) 5 retrieved, 4 used → pass |
| G1-P06 | (a) constant-pattern self-scores → fires; (b) varied legitimate self-scoring → pass |

#### Dashboard widgets

| Dashboard | G1 widgets |
|---|---|
| **T1 Board** | G1 agent count · avg iterations per task · goal drift incidents per month |
| **T2 CAIO** | Loop budget breach trends · Reflexion convergence rate · retrieval efficiency trend |
| **T3 Team** | Top-10 longest-running G1 agents · Reflexion non-convergence by criteria_id · retrieval miss patterns |
| **T4 Runtime** | Live loop counters · current iterations across active runs · Self-RAG cache hit rates |

#### Evidence pack — "G1 Reasoning-Loop Behavior Attestation"

Per agent: total runs, average loops, max loops observed, budget breaches, Reflexion convergence stats (mean iterations to threshold, % gave up, % hit infinite-cap), Self-RAG efficiency, goal-drift incidents/resolutions. Cross-references G8 pack for harness integrity.

#### Implementation footprint

```
packages/api/src/governance/g1/
├── react-tracker/      # loop counter, goal drift detector
├── reflexion-monitor/  # convergence detector, infinite-iteration guard, honesty check
├── selfrag-monitor/    # retrieval efficiency tracker
├── policies/           # G1-P01 through G1-P06 (Rego)
└── shared/
packages/api/src/sdk/auto-instrument/
└── g1-pattern-detection.ts  # detect ReAct/Reflexion/Self-RAG from semconv signals
```

#### G1 done — acceptance criteria

- Loop budget enforcement per tier (config-driven thresholds)
- Goal drift detection with measurable false-positive/negative rates from golden set
- Reflexion convergence detection + infinite-iteration guard operational
- Self-RAG efficiency tracked, reported, alertable
- Self-critique honesty check (G1-P06) operational at R2+
- All 4 dashboard tiers populated with G1 widgets
- G1 evidence pack generates and cross-references G8

### §B.G2 — Branch exploration (compact)

**Patterns:** 3 (Tree-of-Thought), 8 (LATS).
**Governance question:** Did the agent honestly explore alternatives, or fake breadth?

**Telemetry:** `aigp.g2.branches[]` (id, score, abandoned, depth, reasoning), `aigp.g2.chosen_branch_id`, `aigp.g2.score_gap_to_runner_up`, `aigp.g2.exploration_depth_max`, `aigp.g2.branches_total`.

**Policies:**
- **G2-P01 Faked breadth** — `branches_total < 2` for declared ToT/LATS pattern. Severity medium. Flag for review; suspend if recurring.
- **G2-P02 Cherry-picked decision** — chose non-highest-scoring branch without documented `chosen_override_reason`. Severity medium. HITL review.

**Dashboard:** branch-tree drilldown per run (T4); branch-count distribution + low-decisiveness runs (T3).
**Evidence:** branch trees audit-chained at L2 for R2+.

---

### §B.G3 — Routing & specialization (compact)

**Patterns:** 9 (Skill router), 10 (Intent classification), 11 (Load-based), 12 (Risk-based).
**Governance question:** Why did this request go *here* and not elsewhere?

**Telemetry:** `aigp.g3.classifier_id`, `aigp.g3.classifier_version`, `aigp.g3.confidence`, `aigp.g3.routing_destination_chosen`, `aigp.g3.routing_destination_candidates[]` (with scores), `aigp.g3.routing_features_used[]`.

**Policies:**
- **G3-P01 Low-confidence routing** — `confidence < 0.6` at R2+. Severity medium. Route to fallback handler + HITL flag.
- **G3-P02 Risk-incorrect routing** — request with risk-features matching R1+ routed to a R3-classified handler. Severity high. Rollback + escalate to safety review.

**Dashboard:** routing decision distribution by classifier (T2); low-confidence routings + drift (T3).
**Evidence:** classifier version + features-at-decision-time captured for every routed request (L1 baseline; L2 for R2+).

---

### §B.G4 — Linear pipelines (compact)

**Patterns:** 5 (Hierarchical decomposition), 13 (Sequential pipeline), 20 (MetaGPT structured outputs).
**Governance question:** Where did bad data enter, and what downstream is poisoned?

**Telemetry:** `aigp.g4.pipeline_id`, `aigp.g4.stage_index`, `aigp.g4.stage_name`, `aigp.g4.input_artifact_id`, `aigp.g4.output_artifact_id` (lineage edges in AGE graph), `aigp.g4.handoff_validation` (pass/fail/skipped).

**Policies:**
- **G4-P01 Unvalidated handoff** — stage consumes prior output without validating against schema. Severity high. Pause at next stage + HITL.
- **G4-P02 Lineage break** — stage N's `output_artifact_id` doesn't match stage N+1's `input_artifact_id` (lost provenance). Severity critical. Pipeline halt + audit incident.

**Dashboard:** pipeline lineage DAG visualization (T3); per-stage error rates + handoff-validation pass rate (T2).
**Evidence:** lineage subgraph for any pipeline run, queryable from AGE; L2 for R2+.

---

### §B.G5 — Parallel orchestration (compact)

**Patterns:** 14 (Fan-out/fan-in), 15 (Specialist swarm), 17 (Lead-supporting), 18 (DyLAN), 19 (Agentverse).
**Governance question:** Who actually decided this? Who is responsible?

**Telemetry:** `aigp.g5.topology_snapshot` (agents alive, roles, parent/child links), `aigp.g5.coordinator_id`, `aigp.g5.synthesis_event_id`, `aigp.g5.contributing_agents[]` (with influence weight on final), `aigp.g5.role_drift` (boolean per actor).

**Policies:**
- **G5-P01 Phantom decider** — synthesis event has no clear coordinator (no agent claimed authorship of the final output). Severity high. Surface for HITL accountability assignment.
- **G5-P02 Role drift** — agent's actions don't match its assigned role (e.g., a "research" agent calls a "send-email" tool). Severity medium. Containment: revoke tool authorizations for that role until reviewed.

**Dashboard:** topology graph viz per run (T4); coordinator-attribution rate + role-drift incidents (T3).
**Evidence:** full topology + message graph for R2+ runs, captured to AGE; coordinator attribution mandatory at L2.

---

### §B.G6 — Deliberative / adversarial (compact)

**Patterns:** 16 (Debate / deliberation with arbiter).
**Governance question:** Was dissent surfaced or suppressed?

**Telemetry:** `aigp.g6.debate_id`, `aigp.g6.proposer_ids[]`, `aigp.g6.arbiter_id`, `aigp.g6.dissent_events[]` (proposer, content sha, was_considered flag), `aigp.g6.arbiter_decision_record` (final choice + reasoning + which dissents addressed).

**Policies:**
- **G6-P01 Dissent suppression** — `dissent_events` has entries with `was_considered=false` AND arbiter chose a non-dissent option. Severity high. HITL review of arbiter decision.
- **G6-P02 Single-perspective debate** — only one `proposer_id` (debate of one is no debate). Severity medium. Flag for adversarial test set inclusion.

**Dashboard:** dissent-considered rate + arbiter override rate (T2); suppressed-dissent incidents (T3).
**Evidence:** full proposer/arbiter/dissent log for R2+ debates at L2; arbiter decision records always L2.

---

### §B.G7 — Long-memory / lineage (compact)

**Patterns:** 7 (RAISE), 29 (Knowledge graph), 30 (Continuous adaptation).
**Governance question:** Has behavior drifted from prior commitments?

**Telemetry:** `aigp.g7.memory_writes[]` (scope, key, value sha, causation event), `aigp.g7.kg_query`, `aigp.g7.kg_subgraph_returned` (refs at low tier; full at R1), `aigp.g7.kg_writes[]` (node/edge diff), `aigp.g7.commitment_id`, `aigp.g7.commitment_drift_score`.

**Policies:**
- **G7-P01 Commitment drift** — current decision contradicts prior commitment captured in memory (e.g., agent earlier said "no Q3 launches", now scheduling one). Severity high. HITL with prior-commitment evidence attached.
- **G7-P02 KG poisoning** — adversarial-test-detected change to KG with high impact score and no human approval. Severity critical. Rollback KG mutation, freeze writes, open incident.

**Dashboard:** KG mutation rate + commitment-drift heatmap (T2); memory-write provenance browser (T3); live KG query/write stream (T4).
**Evidence:** for any decision involving long-memory, capture causation chain (memory load → reasoning → KG query → decision) at L2; KG mutations always L2; for R1, add adversarial-test pass record.

---

### Cluster coverage summary

| Cluster | Patterns | Status |
|---|---|---|
| **G1 Single-agent reasoning** | 1, 2, 4 | **Full design** |
| **G2 Branch exploration** | 3, 8 | Compact sketch |
| **G3 Routing & specialization** | 9, 10, 11, 12 | Compact sketch |
| **G4 Linear pipelines** | 5, 13, 20 | Compact sketch |
| **G5 Parallel orchestration** | 14, 15, 17, 18, 19 | Compact sketch |
| **G6 Deliberative / adversarial** | 16 | Compact sketch |
| **G7 Long-memory / lineage** | 7, 29, 30 | Compact sketch |
| **G8 Constraint & meta-governance** | 6, 25, 26, 27, 28 | **Full design** |

**All 30 patterns addressed.** G1 + G8 establish the design template (telemetry overlay → policies → eval → dashboards → evidence pack → footprint → done criteria); the 6 sketches confirm the framework holds for every cluster and surface cluster-specific signals worth detecting. Engineers fill the sketches into full designs at implementation time, following the G1/G8 template.

## §C — Trust-level architecture (locked)

### Default trust-level rules

**By tier (baseline):**

| Tier | Default L | Notes |
|---|---|---|
| R0 | L2 | Block events must prove block happened correctly + when |
| R1 | L2 + L3 | Replayable required for scoring, policy fires, classifications, drift snapshots |
| R2 | L2 for prove plane events; L1 elsewhere | Hash chain over audit-relevant events |
| R3 | L1 + retention | Logged with 1y retention |
| R4 | L1 sampled | 10% sampling, 30d retention |

**By event type (escalations regardless of tier):**

- `prove.chain.*` → always L2 (it *is* the chain)
- `evaluate.violation.critical` → L2 + L3
- `observe.human.approval` for R1 → L2 (immutable record of who approved what)
- `observe.tool.call` with `side_effect_class ∈ {send, spend, delete, deploy}` → L2 (irreversible side-effects need integrity)
- `evaluate.replay.run` → L3 (replay results must themselves be replayable)

**By cluster overlay:**

- G6 dissent events → L2 (suppression detection requires immutable record)
- G7 kb.update events → L2 (lineage demands integrity)
- G8 all events → L2 (meta-governance, by definition)

### Implementation primitives

#### L1 — Logged

Existing TimescaleDB events table. No additional infra.

#### L2 — Tamper-evident (hash chain)

- Append-only `audit_chain` Postgres table; INSERT-only triggers (UPDATE/DELETE rejected at DB level)
- Each row: `event_id`, `event_payload_sha256`, `prev_hash` (32B), `this_hash` (32B), `inserted_ts`, `signing_key_id`, `chain_position`
- Hash: SHA-256 over canonical JSON ([RFC 8785 / JCS](https://datatracker.ietf.org/doc/html/rfc8785)) for deterministic results
- Hourly verifier walks chain; raises G8-P01 on break; broken chain freezes new appends
- Periodic root commit to MinIO + opt-in [Sigsum](https://www.sigsum.org/) anchor for R1 (and R0 events)
- Future-proof for SHA-3 by storing `hash_algo` field

#### L3 — Replayable

- Decision events store `(event_set_id, scoring_fn_version, policy_version, output)`
- Eval harness re-runs: load same `event_set` + same policy bundle + same scoring fn → expect same output
- Replay equivalence:
  - **Bit-identical** for deterministic functions (most policies, most scoring)
  - **Bounded-distance + seed capture** for stochastic functions (rare; flagged explicitly)
- Scoring functions stored as WASM modules or Rego policies; **content-addressed in MinIO**, **version-tagged in git**
- Replay results in TimescaleDB; replay events themselves are L3 (turtles all the way)

#### L4 — Formally verified

- **Out of MVP scope.** Reserved for narrow safety-critical paths.
- Identified scope: R0 enforcement logic; audit chain insertion logic; tier-promotion logic.
- Future tools: TLA+ (protocol-level properties), Lean/Coq (code-level), OPA regorus (policy verification).
- Defer until post-MVP; document scope now so it's not lost.

### Enforcement

At ingest, the normalizer service:
1. Computes event's `required_l_level` from `(tier, event_type, cluster)`
2. If L2: writes to audit chain in same transaction as event store
3. If L3: captures `(event_set_id, scoring_fn_version, policy_version)` at decision time
4. If L4 (post-MVP): validates against pre-verified module signature

Every event carries `required_l_level` metadata. Failures to meet level emit `evaluate.trust.violation` (high severity).

### §C done — acceptance criteria

- Trust-level matrix defined for all 7 layers × 8 clusters × 5 tiers (table at `docs/specs/trust-level-matrix.csv`)
- Audit chain (L2) operational: append, verify, anchor (Sigsum opt-in for R1/R0)
- Replay engine (L3) operational: bit-identical replay verified for canonical scoring functions; stochastic functions handled with seed capture
- L4 scope explicitly identified (R0 enforcement, chain insertion, tier promotion) and deferred to post-MVP
- Trust-level metadata propagated through all events; mismatches fire `evaluate.trust.violation`
