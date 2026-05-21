# AIGP Plan 3: G8 Meta-Governance — Audit + Policy + HITL + Eval

> **Status:** ready (after P1, P2) · **Duration:** ~6 weeks · **Depends on:** P1, P2 · **Master plan:** [critically-review-and-recommend-starry-creek.md](./critically-review-and-recommend-starry-creek.md)

## Context

G8 is the **harness's self-portrait**. The five G8 patterns map almost one-to-one to the five planes:

| G8 pattern | Plane it materializes |
|---|---|
| 28 Audit trail | PROVE |
| 25 Guardrails | EVALUATE (realtime) |
| 27 Continuous eval | EVALUATE (offline) + LEARN |
| 26 HITL escalation | CONTROL |
| 6 Constraint-driven planning | All five (cross-cutting) |

Building G8 = building the planes themselves to a credible standard. **Without G8 working, every other cluster's claims are unfalsifiable.** This is the keystone of the entire harness.

## Goal

By the end of this plan:
- Audit chain operational (L2 tamper-evident) with hourly verification + freeze-on-break
- Policy engine running OPA + YAML→Rego compiler with 6 G8 policies enforced
- Eval harness skeleton: replay engine, golden-set manager, regression runner
- HITL queue with appeals workflow + executive-override path
- "Harness Self-Attestation" evidence pack generates and verifies offline
- Risk-tier model fully operational: registration → Rego policy → tier assignment → audit-chained lifecycle

## Dependencies

- P1 (foundation) and P2 (observe plane with telemetry events flowing) complete
- Decision: OPA installation (standalone binary vs `@open-policy-agent/opa-wasm` embedded)

## Deliverables

**Internal sequencing within G8: 28 → 25 → 27 → 26 → 6.** Audit chain is the substrate; guardrails write to it; eval reads it; HITL needs eval signals; constraint-driven planning needs all of the above.

### 1. Audit chain (Pattern 28; Plane: PROVE)

- Postgres migration: `audit_chain` table with INSERT-only triggers (UPDATE/DELETE rejected at DB level)
- Schema: `event_id`, `event_payload_sha256`, `prev_hash` (32B), `this_hash` (32B), `inserted_ts`, `signing_key_id`, `chain_position`, `hash_algo` (default `sha256`)
- Append service in `packages/api/src/governance/g8/audit-chain/`
- Hash function: SHA-256 over canonical JSON ([RFC 8785 / JCS](https://datatracker.ietf.org/doc/html/rfc8785))
- Hourly verifier walks chain, raises G8-P01 on break
- Periodic root commit to MinIO; opt-in [Sigsum](https://www.sigsum.org/) anchor for R0/R1 events
- Fault injection tests: tampered row, missing row, out-of-order row, duplicate row — all detected within 1 cycle

### 2. Policy engine (Pattern 25; Plane: EVALUATE realtime)

- Embed OPA via Go binary or `@open-policy-agent/opa-wasm` for in-process eval
- YAML→Rego compiler in `packages/api/src/governance/g8/policy-engine/yaml-rego.ts`
- Policy registry:
  - Stored in `policies/` directory (git-tracked, signed via git-signed commits)
  - Hot copy in Redis for low-latency eval
  - Versioned via git tag
- Realtime evaluator service `apps/evaluate-svc`:
  - Subscribes `observe.>` from NATS
  - Evaluates against active policy bundle
  - Emits `evaluate.violation.<severity>` and `evaluate.pass`

#### 6 G8 policies (P01–P06)

Each in YAML, compiled to Rego, with golden cases:

| ID | Trigger | Severity | Action | Tier |
|---|---|---|---|---|
| **G8-P01 Chain integrity** | `prove.chain.verify` result=broken | critical | Alert auditors, freeze appends, open incident | All |
| **G8-P02 Guardrail bypass** | `observe.tool.call` preflight=deny AND tool executed | critical | Suspend agent, MI9→4, audit | R2+ |
| **G8-P03 HITL SLA breach** | `observe.human.escalation` `time_to_decision_ms > sla(tier)` | high | Escalate to backup, page on-call | R1+ |
| **G8-P04 Drift breach** | `evaluate.drift.alert` `drift_score > threshold(tier)` | drift-scaled | Open incident, propose policy/eval review | R2+ |
| **G8-P05 Constraint disclosure** | `observe.output.produced` to external destination | medium | Require disclosure annotation; emit if missing | R2+ (Art. 13) |
| **G8-P06 Regulator notification** | `observe.human.incident` severity≥high for R1 | critical | Open regulator notification workflow + auto evidence pack | R1 |

### 3. Eval harness (Pattern 27; Plane: EVALUATE offline + LEARN)

- `apps/eval-harness/` service
- Replay engine: load `(event_set, policy_version, scoring_fn_version)` → re-run → expect identical result for deterministic functions
- Golden-set manager: versioned in MinIO, indexed in Postgres
- Regression runner: triggered on policy/scoring change, blocks merge if regression
- Drift detector: TimescaleDB continuous aggregates per agent × cluster × tier
- Rollback engine: when accuracy degrades, rollback policy + alert team

### 4. HITL queue (Pattern 26; Plane: CONTROL)

- Postgres queue table `hitl_review` with role-based assignment
- WebSocket/SSE notifications via Fastify+Redis pub/sub
- HITL UI in Next.js dashboards (T3 Team, T4 Runtime)
- **Appeals workflow:**
  - Multi-stakeholder review (compliance + legal + business + executive)
  - Slow path (days), audit-chained, regulator-disclosable
- **Executive override:**
  - Single named executive, fast path (minutes)
  - Audit-chained with justification
  - Auto-flagged for regulator disclosure if R0 override
- Both paths feed Learn plane (proposals, golden-set adds)

### 5. Constraint-driven planning (Pattern 6)

- Cross-cutting: integrates audit + policy + HITL + eval
- Telemetry: `aigp.g8.constraint.consulted`, `aigp.g8.constraint.violated_path`, `aigp.g8.constraint.escalation_threshold`
- Implementation: a "constraint context" that policies consult during planning; violations emit events; escalation threshold triggers HITL

### 6. Evidence pack — "Harness Self-Attestation"

`packages/api/src/governance/g8/evidence-pack/`:
- Template generator with 7 sections (chain integrity, policy summary, drift summary, HITL summary, eval summary, cross-cluster references, signatures)
- Signed with platform key (separate Ed25519 key, rotated quarterly)
- Optional auditor co-sign
- Generated weekly + on-demand via API
- **Cascade rule:** if G8-P01 fires, all subsequent packs flagged `PENDING_REVERIFICATION`

### 7. G8 dashboard widgets

`packages/web/src/dashboards/g8/`:
- T1 Board: chain integrity boolean + last-verify-ts; R1 incidents/month; regulator notifications sent/outstanding
- T2 CAIO: policy version diff history; drift heatmap R1/R2; HITL queue depth + SLA per tier
- T3 Team: per-agent guardrail fire rate (top 10); per-policy fire rate; team incidents
- T4 Runtime: realtime guardrail stream; HITL queue with assignee; chain append rate

### 8. Risk-tier model

- Rego policy bundle in `policies/risk-tier/default.rego` (customer-overridable)
- Six dimensions (A–F) captured at agent registration
- Tier assignment lifecycle: declared at registration → continuous validation → auto-promote (never auto-demote) → scheduled review
- Audit-chained tier changes
- 5 tiers (R0 Prohibited, R1 Critical, R2 Elevated, R3 Standard, R4 Minimal) with defense-in-depth R0 enforcement (MCP gate + evaluate plane + observe ingestion)

## Implementation tasks

(Sequenced — each ~1-3 days)

**Week 1: Audit chain**
1. Postgres migration `audit_chain` table + INSERT-only triggers
2. Append service with SHA-256 over JCS
3. Verifier service (hourly cron + on-demand)
4. Fault injection test suite
5. Sigsum anchor integration (opt-in for R1)

**Week 2: Policy engine**
6. OPA embedded in evaluate-svc
7. YAML→Rego compiler
8. Policy registry with git-signed loading
9. Realtime evaluator subscribing to NATS
10–15. G8-P01 through G8-P06 implemented + golden cases (one policy per task)

**Week 3: Eval harness**
16. Replay engine skeleton
17. Golden-set manager (MinIO + Postgres index)
18. Regression runner
19. Drift detector with continuous aggregates
20. Rollback engine

**Week 4: HITL**
21. `hitl_review` table + queue logic
22. WebSocket/SSE notifications
23. HITL UI in T4 Runtime dashboard
24. HITL UI in T3 Team dashboard
25. Appeals workflow
26. Executive override workflow

**Week 5: Constraint planning + Evidence pack**
27. Constraint context + telemetry
28. Pattern-6 escalation logic
29. Evidence pack generator
30. Signing + auditor co-sign
31. Cascade rule on chain break

**Week 6: Risk-tier + dashboards + integration**
32. Risk-tier Rego bundle (default policies)
33. Agent registration flow with 6 dimensions
34. Auto-promote logic (drift-triggered)
35. T1 Board widgets
36. T2 CAIO widgets
37. T3 Team widgets
38. T4 Runtime widgets
39. End-to-end test: synthetic R1 incident → guardrail fire → HITL escalation → evidence pack generation

## Risk

**High.** This is the keystone plan. Risks:

- **Merkle chain bugs are catastrophic** — any logic error makes the entire audit story unreliable. Mitigation: extensive fault-injection testing; security review of chain code; consider third-party crypto audit before production.
- **OPA performance** — if policy eval becomes a hot path, latency could degrade ingestion. Mitigation: benchmark early, cache compiled policies, batch eval.
- **HITL UX** — bad UX = reviewers ignore queue → SLA breaches → cascading G8-P03 fires. Mitigation: usability test with at least 2 prospective reviewers; iterate before MVP.
- **Tier formula complexity** — Rego formulas need to be correct AND understandable to compliance officers. Mitigation: ship default formulas with extensive comments; offer YAML→Rego compiler as authoring surface.

## Acceptance criteria

- [ ] Audit chain verified hourly; breaks detected within 1 cycle under fault injection
- [ ] Broken chain freezes new appends until restored
- [ ] All 6 G8 policies enforce in realtime with golden-case test pass rate 100%
- [ ] Replay engine produces bit-identical output for deterministic scoring functions
- [ ] HITL queue with SLA tracking; appeals + override paths both audit-chained
- [ ] Drift detector raises alert within target window for synthetic drift injection
- [ ] Evidence pack generates on demand; verifies offline with platform key
- [ ] Cascade rule: when chain breaks, all subsequent packs flagged `PENDING_REVERIFICATION`
- [ ] Self-attestation pack auto-generates weekly
- [ ] Risk-tier registration flow operational; auto-promote tested with synthetic drift agent
- [ ] All 4 dashboard tiers populated with G8 widgets
- [ ] End-to-end: synthetic R1 incident flows through full G8 path

## Verification commands

```bash
# Chain integrity under fault injection
pnpm --filter g8-audit-chain test:fault-injection

# Policy regression
pnpm --filter g8-policy-engine test:regression

# Eval replay
pnpm --filter eval-harness replay --event-set golden-001 --policy-version v1.0.0

# HITL UX flow
pnpm --filter web test:e2e -- --grep "HITL queue"

# Evidence pack offline verification
pnpm --filter evidence-pack verify -- attestation-2026-W18.pack

# Risk-tier auto-promote
pnpm test:integration -- --grep "auto-promote"
```

## Notes

- This plan is the highest-stakes work in the project. Budget for slowdowns. Don't compromise audit chain correctness for speed.
- The 6 G8 policies established here become templates for cluster-specific policies in plans 4–6.
- Sigsum integration is opt-in — recommend implementing the integration but defaulting to off for v1; turn on for first R1-tier customer.
- **Consider commissioning a third-party crypto audit of the audit chain implementation before any production deployment.**
