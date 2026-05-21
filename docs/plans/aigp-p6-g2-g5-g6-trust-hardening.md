# AIGP Plan 6: G2 + G5 + G6 + §C Trust Levels + Hardening

> **Status:** ready (after P1–P5) · **Duration:** ~6 weeks · **Depends on:** P1, P2, P3, P4, P5 · **Master plan:** [critically-review-and-recommend-starry-creek.md](./critically-review-and-recommend-starry-creek.md)

## Context

The final plan closes pattern coverage and locks down the trust-level enforcement that makes the harness's claims defensible.

- **G2 Branch exploration** (patterns 3, 8) — detect faked breadth and cherry-picked decisions
- **G5 Parallel orchestration** (patterns 14, 15, 17, 18, 19) — answer "who actually decided this?" in multi-agent runs
- **G6 Deliberative / adversarial** (pattern 16) — detect dissent suppression
- **§C Trust-level enforcement** — `required_l_level` propagation + L3 replay engine + L4 scope documentation
- **ARI/MI9 reimplementation** as versioned scoring functions in eval harness (closes locked fork #2 from master plan)
- **Performance hardening** + multi-tenancy preparation

After this plan, the harness has end-to-end coverage of all 30 patterns and credible trust claims at all 5 levels (L0 through L3, with L4 scope documented).

## Goal

By the end of this plan:
- G2, G5, G6 cluster coverage shipped with policies, dashboards, evidence packs
- `required_l_level` computed and enforced for every event; mismatches fire `evaluate.trust.violation`
- L3 replay engine produces bit-identical results for canonical scoring functions
- L4 scope documented (R0 enforcement, chain insert, tier promotion) — explicitly deferred
- ARI/MI9 reimplemented as versioned, replayable scoring functions
- Ingestion sustains 1k events/sec/agent without backpressure
- Multi-tenancy preparation in place: RLS in Postgres, per-tenant Redis namespacing
- Customer-facing policy authoring UI scaffolded

## Dependencies

- All prior plans (P1–P5) complete
- AGE schema stable (P4)
- MCP server live (P5)
- Decision: WASM vs Rego for L3 scoring functions (recommend: support both; small WASM kernels for compute-heavy, Rego for declarative)

## Deliverables

### G2 Branch exploration

#### 1. G2 branch tree capture

`packages/api/src/governance/g2/`:
- Telemetry overlay producers for `aigp.g2.branches[]` (id, score, abandoned, depth, reasoning)
- Captures `chosen_branch_id`, `score_gap_to_runner_up`, `exploration_depth_max`, `branches_total`

#### 2. G2 decisiveness metric

- `decisiveness_score = score_gap_to_runner_up / max_branch_score`
- Low decisiveness = suspicious choice; surfaces in dashboards

#### 3. G2 faked-breadth detector

- Detects when declared ToT/LATS pattern emits only 1 branch (no real exploration)
- Detects when branches are too similar to be genuine alternatives (embedding similarity)

#### 4. G2 policies (G2-P01, G2-P02)

| ID | Trigger | Severity | Action | Tier |
|---|---|---|---|---|
| **G2-P01 Faked breadth** | `branches_total < 2` for declared ToT/LATS pattern | medium | Flag for review; suspend if recurring | All |
| **G2-P02 Cherry-picked decision** | chose non-highest-scoring branch without `chosen_override_reason` | medium | HITL review | R2+ |

#### 5. G2 dashboards + evidence pack

- T3 Team: branch-count distribution + low-decisiveness runs
- T4 Runtime: branch-tree drilldown per run
- Evidence: branch trees audit-chained at L2 for R2+

### G5 Parallel orchestration

#### 6. G5 topology snapshot capture

`packages/api/src/governance/g5/`:
- Captures `aigp.g5.topology_snapshot` at every coord event: agents alive, roles, parent/child links
- Time-series of topology changes per workflow

#### 7. G5 message graph in AGE

- Materializes layer-4 coordination events as graph: `Agent → SENT → Agent` with message_type, role_at_time, trust_level
- Multi-hop queries: "all messages that contributed to this final synthesis"

#### 8. G5 role drift detection

- Each agent has assigned role manifest at registration (extends agent registry from P3)
- Role manifest specifies authorized tools + responsibilities
- Role drift = agent calls a tool not in manifest (e.g., "research" agent calls `send-email`)
- Computed at every layer-3 tool.call

#### 9. G5 policies (G5-P01, G5-P02)

| ID | Trigger | Severity | Action | Tier |
|---|---|---|---|---|
| **G5-P01 Phantom decider** | synthesis event has no clear coordinator | high | HITL accountability assignment | R2+ |
| **G5-P02 Role drift** | agent action doesn't match assigned role | medium | Containment: revoke tool authorizations for that role | R2+ |

#### 10. G5 dashboards + evidence pack

- T3 Team: coordinator-attribution rate + role-drift incidents
- T4 Runtime: topology graph viz per run
- Evidence: full topology + message graph for R2+ runs at L2

### G6 Deliberative / adversarial

#### 11. G6 dissent event capture

`packages/api/src/governance/g6/`:
- Captures `aigp.g6.dissent_events[]` (proposer, content sha, was_considered flag) at every debate-style coordination
- Distinguishes from regular `agent.message` via `message_type='dissent'`

#### 12. G6 arbiter decision records

- Captures `aigp.g6.arbiter_decision_record` (final choice + reasoning + which dissents addressed)
- For every debate, the arbiter must explicitly mark each dissent's `was_considered` and explain rejection if applicable

#### 13. G6 policies (G6-P01, G6-P02)

| ID | Trigger | Severity | Action | Tier |
|---|---|---|---|---|
| **G6-P01 Dissent suppression** | dissent_events with was_considered=false AND arbiter chose non-dissent option | high | HITL review of arbiter decision | R2+ |
| **G6-P02 Single-perspective debate** | only one proposer_id (debate of one) | medium | Flag for adversarial test set | All |

#### 14. G6 dashboards + evidence pack

- T2 CAIO: dissent-considered rate + arbiter override rate
- T3 Team: suppressed-dissent incidents
- Evidence: full proposer/arbiter/dissent log for R2+ debates at L2; arbiter decision records always L2

### §C Trust-level enforcement

#### 15. `required_l_level` computation

In `packages/api/src/governance/trust-levels/`:
- Function `computeRequiredLevel(event) → 'L0'|'L1'|'L2'|'L3'|'L4'`
- Stacks rules: max of `byTier(R)`, `byEventType(t)`, `byCluster(c)`
- Documented rule set in code with rationale per rule
- Tested against full coverage matrix (7 layers × 8 clusters × 5 tiers)

#### 16. `required_l_level` propagation

- Every event carries `required_l_level` field (added by normalizer in P2; enforced here)
- Audit chain entries reference required level
- Evidence packs declare achieved level per event

#### 17. Trust-level mismatch detection

- New event type: `evaluate.trust.violation` (high severity)
- Fires when actual delivered level < required level
- Action: incident + policy/eval review

### L3 replay engine

#### 18. WASM/Rego scoring functions

`packages/api/src/governance/eval/scoring-fn/`:
- Scoring function interface: `(events: Event[], policy: Policy) → Score` 
- WASM modules for compute-heavy (e.g., embedding-based drift)
- Rego policies for declarative (e.g., threshold checks)
- Both content-addressed in MinIO (sha256 → blob), version-tagged in git
- Replay engine loads pinned `(scoring_fn_version, policy_version, event_set_id)`, executes, expects bit-identical output

#### 19. Stochastic function handling

- For functions using randomness (e.g., adversarial test generation), capture seed in event
- Replay re-executes with captured seed → deterministic re-execution
- Bounded-distance equivalence for inherently stochastic outputs (with tolerance config)

### L4 scope documentation

#### 20. L4 scope identification

- Identified L4 paths (deferred to post-MVP):
  - **R0 enforcement logic** — must reject 100% of R0 actions; formal verification protects against logic errors that could let prohibited actions through
  - **Audit chain insertion logic** — formal verification of chain integrity invariants under concurrent inserts
  - **Tier promotion logic** — formal verification of "auto-promote, never auto-demote" invariant
- Tools considered: TLA+ (protocol-level), Lean/Coq (code-level), [OPA Regorus](https://github.com/microsoft/regorus) (policy verification)
- Document scope in ADR-008; defer implementation to post-MVP

### ARI/MI9 reimplementation (closes locked fork #2)

#### 21. ARI as versioned scoring function

- Move `packages/api/src/routes/governance.ts` ARI logic to `packages/api/src/governance/eval/scoring-fn/ari/`
- Express as Rego policy (or WASM if compute-heavy)
- Version-tagged; old ARI scores carry their version
- Re-evaluation creates new score record (non-destructive)

#### 22. MI9 as versioned scoring function

- Same treatment for MI9 containment level computation
- Now reproducible: any historic MI9 level can be recomputed from same inputs

### Performance hardening

#### 23. Ingestion throughput target

- Sustain 1k events/sec/agent without backpressure (10k events/sec/cluster)
- Audit chain insert latency p99 < 10ms
- AGE query latency p95 < 100ms for typical lineage queries

#### 24. AGE query optimization

- Index analysis on AGE-backing tables
- Query pattern review: cache common subgraphs

### Multi-tenancy preparation

#### 25. Postgres RLS

- Row-level security on all tables: `tenant_id` column + RLS policies
- Migration to add `tenant_id` to existing tables (default tenant `default-tenant`)

#### 26. Per-tenant Redis namespacing

- Redis keys prefixed with `tenant:<id>:`
- Multi-tenant rate limiting

### Customer-facing policy authoring UI

#### 27. Policy authoring UI scaffolding

`packages/web/src/dashboards/policy-authoring/`:
- YAML editor with policy template library
- Preview: dry-run policy against last 7 days of events
- Diff view vs current production policy
- Submit-for-review workflow (creates git PR)
- Targeted at compliance officers, not engineers

## Implementation tasks

**Week 1: G2**
1. G2 branch tree capture
2. G2 decisiveness metric
3. G2 faked-breadth detector
4. G2-P01 + G2-P02 policies
5. G2 dashboards + evidence pack

**Week 2: G5 part 1**
6. G5 topology snapshot capture
7. G5 message graph materialization in AGE
8. Role manifest in agent registry
9. G5 role drift detection

**Week 3: G5 part 2 + G6**
10. G5-P01 + G5-P02 policies
11. G5 dashboards + evidence pack
12. G6 dissent event capture
13. G6 arbiter decision records
14. G6-P01 + G6-P02 policies
15. G6 dashboards + evidence pack

**Week 4: §C trust levels**
16. `computeRequiredLevel()` with full coverage matrix tests
17. `required_l_level` propagation through pipeline
18. `evaluate.trust.violation` event + policy
19. WASM/Rego scoring function infrastructure
20. L3 replay with bit-identical assertion
21. Stochastic function handling (seed capture)
22. ADR-008: L4 scope and deferral rationale

**Week 5: ARI/MI9 + performance**
23. ARI reimplementation as versioned scoring fn
24. MI9 reimplementation as versioned scoring fn
25. Performance hardening: ingestion throughput
26. Performance hardening: audit chain insert latency
27. Performance hardening: AGE query optimization

**Week 6: Multi-tenancy + policy authoring UI**
28. Postgres RLS migration
29. Per-tenant Redis namespacing
30. Multi-tenant rate limiting
31. Policy authoring UI scaffolding
32. Policy preview / dry-run feature
33. Submit-for-review (git PR) workflow
34. End-to-end MVP demo: full harness with all clusters live, multi-tenant, evidence packs across all 8 clusters

## Risk

**Medium-high.** Risks:

- **Performance unknowns** — actual throughput at 1k events/sec/agent may not hold under production load mix. Mitigation: load test continuously throughout the plan; have escape hatches (sharding, read replicas, NATS partitioning).
- **Multi-tenancy scope creep** — full multi-tenancy (RBAC across tenants, billing, isolation guarantees) is a separate product. This plan does *preparation* only. Mitigation: explicit non-goals — no billing, no inter-tenant features, no SLA guarantees.
- **L3 replay bit-identical assertion is fragile** — any non-determinism (timestamps, random IDs, FP rounding) breaks the assertion. Mitigation: canonical event normalization for replay; explicit allow-list of "allowed non-determinism" with bounded equivalence.
- **G6 dissent capture requires runtime cooperation** — debate runtimes must emit dissent events. Mitigation: SDK adapters do this automatically; document for manual instrumentation.

## Acceptance criteria

- [ ] All G2/G5/G6 cluster acceptance criteria met (master plan §B sketches)
- [ ] `required_l_level` computed correctly for full 7×8×5 matrix
- [ ] `evaluate.trust.violation` fires on synthetic mismatch
- [ ] L3 replay produces bit-identical output for deterministic scoring functions
- [ ] L3 replay produces bounded-distance output for stochastic functions with seed capture
- [ ] L4 scope documented in ADR-008; explicitly deferred to post-MVP
- [ ] ARI/MI9 scores reproducible bit-identically across replays
- [ ] Old ARI/MI9 scores readable with their original version
- [ ] Ingestion sustains 1k events/sec/agent for 10 min without backpressure
- [ ] Audit chain insert p99 latency < 10ms
- [ ] AGE query p95 latency < 100ms
- [ ] Postgres RLS active; cross-tenant access prohibited in tests
- [ ] Policy authoring UI: compliance officer can author + preview + submit policy
- [ ] **End-to-end MVP demo**: all 8 clusters with policies firing, evidence packs generating, multi-tenant deployment working

## Verification commands

```bash
# G2 / G5 / G6 golden cases
pnpm --filter g2-policies test:golden
pnpm --filter g5-policies test:golden
pnpm --filter g6-policies test:golden

# Trust-level matrix
pnpm --filter trust-levels test:coverage-matrix

# L3 replay bit-identical
pnpm --filter eval-harness test:replay-deterministic

# Performance
pnpm --filter observe-svc test:load -- --rate 1000 --per-agent --duration 600

# Multi-tenant isolation
pnpm test:integration -- --grep "multi-tenant isolation"

# End-to-end MVP demo
pnpm demo:mvp
```

## Notes

- This plan caps the MVP. Post-MVP work (L4 formal verification, full multi-tenancy product, customer-facing policy IDE) is explicitly out of scope.
- The policy authoring UI is *scaffolding* only — a full IDE-grade authoring experience is post-MVP work.
- Performance targets are MVP-grade — production scale will need further work post-MVP.
- After this plan: the harness covers all 30 patterns (8 in full design from G1+G8, 6 in compact-sketch implementation from G2/G3/G4/G5/G6/G7), supports 5 trust levels (L0–L3 + L4 documented), enforces 5 risk tiers (R0–R4), and operates the full 5-plane architecture.
