# AIGP Plan 5: G1 + G3 + G4 Clusters + MCP Governance Server

> **Status:** ready (after P1, P2, P3) · **Duration:** ~4 weeks · **Depends on:** P1, P2, P3; G4 needs P4 lineage · **Runs in parallel with:** P4 · **Master plan:** [critically-review-and-recommend-starry-creek.md](./critically-review-and-recommend-starry-creek.md)

## Context

This plan ships three clusters and the integration surface external agents use to call governance:

- **G1 Single-agent reasoning** (patterns 1, 2, 4) — highest production volume, lowest-risk first deliverable
- **G3 Routing & specialization** (patterns 9, 10, 11, 12) — routing decisions touch every other cluster
- **G4 Linear pipelines** (patterns 5, 13, 20) — uses lineage from P4
- **MCP Governance Server** — enables external agent runtimes to call governance via MCP protocol

By shipping G1 + G3 + G4, the harness covers ~12 of the 30 patterns and enters credible MVP territory.

## Goal

By the end of this plan:
- G1 detection, scoring, and policy enforcement operational with all 6 G1 policies (G1-P01 through G1-P06) including the rubber-stamping honesty check
- G3 routing decisions captured and policies enforced with low-confidence fallback handler
- G4 pipeline lineage queryable in AGE; lineage breaks detected and pipelines halted
- MCP Governance Server live with 4 tools; external LangGraph agent can call the gate end-to-end
- All three cluster evidence packs cross-reference G8 self-attestation

## Dependencies

- P1 (foundation), P2 (observe plane), P3 (audit + policy + eval + HITL)
- P4 in progress — G4 lineage queries depend on AGE schema being established
- Coordinate with P4 team on shared AGE node/edge types

## Deliverables

### 1. G1 ReAct loop tracker

`packages/api/src/governance/g1/react-tracker/`:
- Computes `loop_index`, `last_observation_used`, `goal_drift_score`, `max_loops_threshold(tier)`
- Goal drift detection: embedding similarity between current step's task description and original goal
- Threshold config-driven per tier: R1=5, R2=10, R3=15, R4=25 (defaults; Rego-overridable)

### 2. G1 Reflexion convergence detector + honesty check

`packages/api/src/governance/g1/reflexion-monitor/`:
- Tracks `iteration_index`, `criteria_id`, `score_before`, `score_after`, `improvement_rate`, `gave_up`
- Convergence detector: if `improvement_rate < 0.05` for 2+ iterations, auto-stop with quality flag
- Infinite-iteration guard: hard stop at iteration_index = 5 (configurable per tier)
- **Honesty check (G1-P06):** flags when self-critique pattern is constant (e.g., always 0.95 → 0.99 regardless of input). Computed via variance analysis on score_before/score_after across runs

### 3. G1 Self-RAG efficiency monitor

`packages/api/src/governance/g1/selfrag-monitor/`:
- Tracks `retrieved_count`, `relevance_decision`, `retrieval_iterations`, `context_efficiency`
- Context efficiency = retrieved-and-used / retrieved-total
- Alerts on `context_efficiency < 0.2` at R3+

### 4. G1 policies (G1-P01 through G1-P06)

In `policies/g1/`, YAML compiled to Rego:

| ID | Trigger | Severity | Action | Tier |
|---|---|---|---|---|
| **G1-P01 Loop budget** | `loop_index > max_loops_threshold(tier)` | high | Suspend loop, escalate, audit | All |
| **G1-P02 Goal drift** | `goal_drift_score > 0.5` for 2+ steps | medium | HITL review queue | R2+ |
| **G1-P03 Reflexion non-convergence** | `improvement_rate < 0.05` for 2+ iterations | medium | Auto-stop, return best version with quality flag | All |
| **G1-P04 Infinite refinement** | `iteration_index > 5` | high | Hard stop, audit | All |
| **G1-P05 Retrieval irrelevance** | `context_efficiency < 0.2` | low | Alert, propose retrieval policy review | R3+ |
| **G1-P06 Self-critique honesty** | constant-pattern self-scores | medium | Flag for adversarial test set | R2+ |

Each with golden cases (see master plan §B.G1).

### 5. G1 SDK auto-instrumentation

`packages/sdk-ts/src/auto-instrument/g1-pattern-detection.ts`:
- Detects ReAct/Reflexion/Self-RAG pattern from semconv signals (e.g., presence of `cot_text` + `loop_count` field → ReAct)
- Auto-tags `pattern_tag` and `cluster_tag` on outgoing events
- Reduces integration burden: agent code doesn't have to declare pattern explicitly

### 6. G1 dashboards + evidence pack

`packages/web/src/dashboards/g1/`:
- T1 Board: G1 agent count · avg iterations per task · goal drift incidents per month
- T2 CAIO: loop budget breach trends · Reflexion convergence rate · retrieval efficiency trend
- T3 Team: top-10 longest-running G1 agents · Reflexion non-convergence by criteria_id · retrieval miss patterns
- T4 Runtime: live loop counters · current iterations across active runs · Self-RAG cache hit rates

Evidence pack — "G1 Reasoning-Loop Behavior Attestation": per-agent loop stats, Reflexion convergence stats, Self-RAG efficiency, goal-drift incidents/resolutions. Cross-references G8 pack.

### 7. G3 routing classifier instrumentation

`packages/api/src/governance/g3/`:
- Captures `classifier_id`, `classifier_version`, `confidence`, `routing_destination_chosen`, `routing_destination_candidates[]` (with scores), `routing_features_used[]`
- Records every routing decision (every layer-3 tool.call where the tool itself was a router)

### 8. G3 low-confidence fallback handler

- When `confidence < 0.6` at R2+, route to fallback handler instead of confidently-but-wrongly chosen handler
- Fallback handler emits HITL flag for the original request

### 9. G3 policies (G3-P01, G3-P02)

In `policies/g3/`:

| ID | Trigger | Severity | Action | Tier |
|---|---|---|---|---|
| **G3-P01 Low-confidence routing** | `confidence < 0.6` | medium | Route to fallback + HITL flag | R2+ |
| **G3-P02 Risk-incorrect routing** | risk-features matching R1+ routed to R3-classified handler | high | Rollback + escalate to safety review | R2+ |

### 10. G3 dashboards + evidence pack

- T2 CAIO: routing decision distribution by classifier
- T3 Team: low-confidence routings + drift
- Evidence: classifier version + features-at-decision-time captured for every routed request (L1 baseline; L2 for R2+).

### 11. G4 pipeline lineage capture (uses AGE from P4)

`packages/api/src/governance/g4/`:
- Captures `pipeline_id`, `stage_index`, `stage_name`, `input_artifact_id`, `output_artifact_id`, `handoff_validation`
- Lineage edges in AGE: `Stage → CONSUMED → Artifact`, `Stage → PRODUCED → Artifact`, `Stage_N → HANDED_OFF_TO → Stage_N+1`
- Coordinates with P4 on shared schema

### 12. G4 policies (G4-P01, G4-P02)

In `policies/g4/`:

| ID | Trigger | Severity | Action | Tier |
|---|---|---|---|---|
| **G4-P01 Unvalidated handoff** | stage consumes prior output without schema validation | high | Pause at next stage + HITL | R2+ |
| **G4-P02 Lineage break** | stage N output_artifact_id ≠ stage N+1 input_artifact_id | critical | Pipeline halt + audit incident | All |

### 13. G4 dashboards + evidence pack

- T2 CAIO: per-stage error rates + handoff-validation pass rate
- T3 Team: pipeline lineage DAG visualization
- Evidence: lineage subgraph for any pipeline run, queryable from AGE; L2 for R2+.

### 14. MCP Governance Server `apps/mcp-governance`

The integration surface external agent runtimes use to call governance.

Implements 4 MCP tools:
- **`governance.check(action, context)`** → `{ decision: 'allow' | 'hold' | 'deny', reason, policy_id, policy_version }`. Synchronous policy check before agent acts.
- **`governance.requestApproval(action, justification)`** → opens HITL review, returns `{ decision, approver_id, time_to_decision_ms }` when human decides (with timeout). Async with timeout.
- **`governance.escalate(reason, level)`** → raises MI9 level for the calling agent. Used when agent self-detects a problem.
- **`governance.report(event)`** → agent-initiated self-disclosure (e.g., "I just used a deprecated tool"). Becomes an audit event.

Auth: agents authenticate via JWT (already in repo) + agent_id in token. MCP server validates and routes.

Tested with external LangGraph agent via the `@aigp/sdk-langgraph` adapter (from P2).

## Implementation tasks

(Sequenced — each ~1-3 days)

**Week 1: G1**
1. ReAct loop tracker
2. Goal drift detector with embedding similarity
3. Reflexion convergence detector
4. Reflexion infinite-iteration guard
5. Reflexion honesty check (variance analysis)
6. Self-RAG efficiency monitor
7. G1-P01 through G1-P06 policies (one per task) with golden cases

**Week 2: G1 SDK + dashboards + evidence**
8. G1 SDK auto-instrumentation (pattern detection)
9. G1 T1/T2/T3/T4 dashboard widgets (one tier per task)
10. G1 evidence pack template
11. G1 end-to-end test

**Week 3: G3 + G4**
12. G3 routing classifier instrumentation
13. G3 low-confidence fallback handler
14. G3-P01 + G3-P02 policies
15. G3 dashboards + evidence pack
16. G4 pipeline lineage capture (uses AGE)
17. G4-P01 + G4-P02 policies
18. G4 dashboards + evidence pack

**Week 4: MCP Governance Server**
19. MCP server scaffolding in `apps/mcp-governance`
20. `governance.check` tool implementation
21. `governance.requestApproval` tool with HITL integration
22. `governance.escalate` tool
23. `governance.report` tool
24. JWT auth integration
25. End-to-end test: external LangGraph agent calls all 4 tools successfully

## Risk

**Medium.** Risks:

- **G1-P06 honesty check is novel** — needs golden-set tuning. False positives could flag legitimate Reflexion runs. Mitigation: start with high variance threshold (low FPR), iterate based on runtime data.
- **MCP server auth is new attack surface** — bad auth = anyone can suspend any agent. Mitigation: security review before MCP exposes any sensitive operations; rate-limit per agent_id.
- **G4 depends on P4 AGE schema** — if P4 slips, G4 ships partial. Mitigation: define AGE contract early between P4/P5 leads; G4 can ship without lineage queries (just events) and add queries when P4 lands.
- **Goal drift embedding compute cost** — every step needs embedding comparison. Mitigation: cache embeddings per task; use small model for drift detection.

## Acceptance criteria

- [ ] All 6 G1 policies fire correctly on golden cases (P01–P06)
- [ ] G1-P06 honesty check detects rubber-stamping in synthetic Reflexion agent
- [ ] G1 SDK auto-instrumentation detects pattern from runtime signals
- [ ] G1 dashboards populated in all 4 tiers
- [ ] G1 evidence pack generates and cross-references G8
- [ ] G3 low-confidence routings route to fallback handler
- [ ] G3 risk-incorrect routings rollback and escalate
- [ ] G3 dashboards populated; evidence pack generates
- [ ] G4 lineage edges materialize in AGE for every pipeline run
- [ ] G4 lineage break halts pipeline at next stage + audit
- [ ] G4 dashboards populated; evidence pack generates
- [ ] MCP Governance Server responds to all 4 tools
- [ ] External LangGraph test agent calls all 4 MCP tools end-to-end

## Verification commands

```bash
# G1 policy golden cases
pnpm --filter g1-policies test:golden

# G1 honesty check on synthetic rubber-stamper
pnpm --filter g1-reflexion test:integration -- --grep "honesty check"

# G3 routing
pnpm --filter g3-policies test:golden

# G4 lineage
psql -c "SELECT * FROM cypher('aigp', \$\$ MATCH (s1:Stage)-[:HANDED_OFF_TO]->(s2:Stage) RETURN s1.name, s2.name LIMIT 10 \$\$) AS (s1 TEXT, s2 TEXT);"

# MCP server end-to-end
pnpm --filter mcp-governance test:e2e -- --client langgraph
```

## Notes

- This plan runs in parallel with P4. Coordinate on AGE schema changes via shared ADR.
- G1 is the highest-volume cluster — its dashboards and evidence packs become the model for the other clusters' UX.
- MCP server is the **public-facing** surface other teams' agents will integrate against. Treat it like a product API: stable, documented, versioned.
- Consider publishing the MCP server as an open-source reference implementation alongside the SDKs from P2.
