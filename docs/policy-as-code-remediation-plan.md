# Policy-as-Code Remediation Plan — 6 Real Gaps

> **Purpose:** Actionable remediation plan for the 6 genuine gaps identified in the Policy-as-Code state assessment. Each gap is mapped to existing architecture that partially addresses it, the specific shortfall, and a sprint-level implementation plan.
>
> **Version:** 1.0
> **Date:** 2026-04-28
> **Owner:** Chief AI Officer
> **Approved By:** AI Governance Council

---

## Executive Summary

A comprehensive review of the ProtoLabs governance framework against state-of-the-art Policy-as-Code research identified **6 genuine gaps** (not 10 — 4 of the original 10 were already addressed by existing architecture). These gaps fall into three categories:

| Category | Gaps | Impact |
|----------|------|--------|
| **Architecture exists, needs implementation** | Gap 1 (Executable Checklists) | Blocks automated enforcement |
| **Architecture exists, needs extension** | Gap 5 (Policy Tree), Gap 7 (Adversarial Testing) | Limits cross-framework coherence |
| **No architecture exists** | Gap 3 (Formal Verification), Gap 4 (Multi-Modal CAD), Gap 10 (Control Tax) | Requires new design |

### What Already Exists (Correcting the Record)

The original external evaluation claimed 10 gaps. Review of actual governance artifacts revealed that 4 "gaps" were already designed:

| Claimed Gap | Actual State |
|-------------|-------------|
| Gap 2: No Policy Engine | **7-Layer Governance Enforcement Pipeline** with OPA/Cedar integration, fail-closed design, <25ms latency budget |
| Gap 6: No Runtime Compliance | **Safety Agent Architecture** + continuous compliance checks in Layer 1 of the enforcement pipeline |
| Gap 8: No Client-Specific Enforcement | **Multi-Tenant Isolation** (6-layer model) + per-tenant budgets + RBAC + compliance keyword routing |
| Gap 9: No Provenance Chain | **Layer 6 Audit Log** with SHA-256 integrity chain, policy decision recording, delegation chain linking |

---

## Gap 1: Checklists Are Not Executable

### Current State

| Aspect | Detail |
|--------|--------|
| **Existing Architecture** | 7-Layer Governance Enforcement Pipeline (`governance/03-runtime-governance/agentic-workflows/governance-enforcement-pipeline.md`) |
| **What Works** | Pipeline specifies OPA/Cedar policy engine, fail-closed execution, compliance check layer |
| **What's Missing** | The YAML checklists (`pre-deployment-gate.yaml`, `model-card-completeness-checklist.yaml`, etc.) are documentation artifacts — they are not compiled into OPA Rego or Cedar policies that execute in CI/CD |
| **Evidence** | `pre-deployment-gate.yaml` has `evidence_ref` fields for human review, not machine-evaluable conditions |

### Gap Detail

The 7-layer pipeline is fully specified with OPA Rego and Cedar code examples, but the actual governance checklists that define *what* should be enforced remain as human-readable YAML. The bridge between "policy document" and "policy engine" is missing.

### Remediation Plan

| Sprint | Task | Deliverable | Effort |
|--------|------|-------------|--------|
| **S1** | Audit all checklists and extract machine-evaluable conditions | `policy-conditions-inventory.yaml` — maps each checklist item to evaluable type (boolean, threshold, evidence-exists, api-check) | 1 sprint |
| **S1** | Define OPA Rego package structure | `policies/` directory with `compliance/`, `budget/`, `rbac/`, `safety/` sub-packages | 0.5 sprint |
| **S2** | Compile `pre-deployment-gate.yaml` into Rego policies | `policies/compliance/pre-deployment.rego` — 20 critical checks as executable rules | 1 sprint |
| **S2** | Compile `model-card-completeness-checklist.yaml` into Rego | `policies/compliance/model-card.rego` — completeness validation | 0.5 sprint |
| **S3** | Integrate OPA into CI/CD pipeline | GitHub Actions workflow that evaluates Rego policies against agent deployment manifests | 1 sprint |
| **S3** | Build evidence collection adapters | Scripts that populate OPA input from actual artifacts (eval results, model cards, audit logs) | 1 sprint |
| **S4** | Add remaining checklists (bias-testing, data-quality, model-validation) | Rego policies for all 5 development governance checklists | 1 sprint |
| **S4** | Dashboard for policy compliance status | Real-time view of which agents pass/fail which policies | 0.5 sprint |

**Total Effort:** 6.5 sprints
**Dependencies:** None (can start immediately)
**Blocks:** All automated governance enforcement

### Success Criteria

- [ ] 100% of critical checklist items (marked `critical: true`) have corresponding Rego policies
- [ ] CI/CD pipeline blocks deployment if any critical policy fails
- [ ] Policy compliance dashboard shows real-time status per agent
- [ ] Evidence collection is automated (no manual `evidence_ref` population)

---

## Gap 3: No Formal Verification for Safety-Critical Outputs

### Current State

| Aspect | Detail |
|--------|--------|
| **Existing Architecture** | Safety Agent Architecture (`safety-agent-architecture.md`) — runtime monitoring, kill-switch, fail-closed |
| **What Works** | Runtime interception, output gating, independent monitoring |
| **What's Missing** | All verification is probabilistic (eval suites with accuracy thresholds). No formal guarantees that a Tier 3 agent's output satisfies regulatory constraints. |
| **Why It Matters** | When PL-LMM prices a flight-critical aerospace part or generates a DFM recommendation for a medical implant, "95% accuracy" is insufficient for regulators and clients. |

### Gap Detail

The Safety Agent monitors and intercepts, but it cannot *prove* that an output is correct — it can only check that it *looks* correct based on heuristics. For Tier 3 agents operating on safety-critical parts, this is inadequate.

### Remediation Plan

| Sprint | Task | Deliverable | Effort |
|--------|------|-------------|--------|
| **S1-S2** | Research & scoping: Identify which Tier 3 outputs are candidates for formal verification | `formal-verification-candidate-analysis.md` — maps each Tier 3 output type to verification feasibility | 2 sprints |
| **S2** | Define formal specification language for DFM constraints | `specs/dfm-constraints.lean` — Lean 4 definitions of manufacturing constraints (min wall thickness, max aspect ratio, etc.) | 1 sprint |
| **S3-S4** | Build constraint checker that translates DFM rules into Lean 4 theorems | `tools/formal-dfm-checker/` — takes extracted features + rules, produces proof obligations | 2 sprints |
| **S5-S6** | Implement proof kernel integration | Lean 4 kernel embedded as a service; agent outputs are submitted as conjectures, kernel returns proved/refuted | 2 sprints |
| **S7** | Integrate formal verification into Safety Agent output gate | Layer 7 (Execution Wrapper) extended with formal proof check for Tier 3 outputs | 1 sprint |
| **S8** | Build audit trail for formal proofs | Each verified output includes the Lean 4 proof object as evidence | 0.5 sprint |

**Total Effort:** 10.5 sprints
**Dependencies:** Gap 1 (executable checklists) for policy specification
**Blocks:** Tier 3 agent deployment for safety-critical applications

### Scope Limitation

Formal verification is only feasible for **deterministic, rule-based outputs** (DFM constraint checking, tolerance validation). It is NOT feasible for:
- VLM-based visual assessments (probabilistic)
- Natural language explanations (generative)
- Cost estimation (model-based)

**Strategy:** Apply formal verification to the *constraint satisfaction* layer, not the *reasoning* layer. The Safety Agent handles probabilistic checks; the formal verifier handles deterministic guarantees.

### Success Criteria

- [ ] 100% of Tier 3 DFM constraint outputs have formal proofs or explicit "unverifiable" flags
- [ ] Formal verification latency <500ms per output
- [ ] Audit trail includes Lean 4 proof objects for all verified outputs
- [ ] Regulators can inspect proof objects independently

---

## Gap 4: No Multi-Modal CAD Guardrails

### Current State

| Aspect | Detail |
|--------|--------|
| **Existing Architecture** | WP01 Input Sanitization (text-focused) + CAD Features Catalogue (parsing/analysis, no guardrails) |
| **What Works** | Text input sanitization, CAD file parsing (STEP, STL, OBJ), feature recognition, VLM analysis |
| **What's Missing** | No guardrail layer between "CAD file uploaded" and "CAD file parsed/analyzed." A malicious or corrupted CAD file could exploit the feature recognition model. |

### Gap Detail

The CAD pipeline (CAD-001 through VLM-008) is an *analysis* pipeline, not a *guarded* pipeline. It assumes inputs are benign. The existing WP01 covers text prompts but has no geometry-level checks.

### Attack Vectors

| Vector | Description | Impact |
|--------|-------------|--------|
| **Adversarial geometry** | Crafted mesh/STEP files that cause feature recognition to misidentify features | Incorrect DFM assessment, wrong pricing |
| **Malformed file exploitation** | Specially crafted file headers or structures that exploit parser vulnerabilities | Code execution, denial of service |
| **Metadata injection** | Malicious metadata embedded in CAD files (STEP AP242 allows arbitrary text) | Prompt injection via file metadata |
| **Dimensional spoofing** | Files that appear valid but contain contradictory dimensional data | Conflicting DFM recommendations |

### Remediation Plan

| Sprint | Task | Deliverable | Effort |
|--------|------|-------------|--------|
| **S1** | Define CAD file threat model | `threat-model-cad-inputs.md` — comprehensive attack surface analysis | 0.5 sprint |
| **S1** | Build file format validator | `tools/cad-guardrails/format-validator/` — validates STEP/STL/OBJ/3MF structural integrity before parsing | 1 sprint |
| **S2** | Implement geometry sanity checks | `tools/cad-guardrails/geometry-sanity/` — bounding box limits, vertex count limits, degenerate face detection | 1 sprint |
| **S2** | Build metadata sanitizer | `tools/cad-guardrails/metadata-sanitizer/` — strips or validates non-essential metadata from STEP/3MF | 0.5 sprint |
| **S3** | Implement adversarial geometry detection | `tools/cad-guardrails/adversarial-detector/` — statistical analysis of mesh properties to detect crafted inputs | 1.5 sprints |
| **S3** | Build dimensional consistency checker | `tools/cad-guardrails/consistency-checker/` — cross-validates extracted features against file metadata | 0.5 sprint |
| **S4** | Integrate CAD guardrails into pipeline as pre-parse layer | Pipeline modification: guardrails execute before CAD-001 parser | 0.5 sprint |
| **S4** | Add CAD guardrail metrics to monitoring | Dashboard: file rejection rate, adversarial detection rate, format validation pass rate | 0.5 sprint |

**Total Effort:** 6 sprints
**Dependencies:** Gap 1 (for policy specification of guardrail thresholds)
**Blocks:** Production deployment of CAD evaluation system

### Success Criteria

- [ ] 100% of uploaded CAD files pass through guardrail layer before parsing
- [ ] Adversarial geometry detection catches >95% of known attack patterns
- [ ] File format validation rejects malformed files before parser execution
- [ ] Metadata injection vectors eliminated (no raw metadata reaches VLM)
- [ ] Guardrail latency <2 seconds per file

---

## Gap 5: No Policy Tree with Inheritance

### Current State

| Aspect | Detail |
|--------|--------|
| **Existing Architecture** | Flat checklists per lifecycle stage (`01-discovery-governance/checklists/`, `02-development-governance/checklists/`, etc.) + compliance keyword routing in CLAUDE.md |
| **What Works** | Per-stage checklists, framework mapping (NIST ↔ EU AI Act ↔ ISO 42001 ↔ Singapore MGF), compliance keyword detection |
| **What's Missing** | No hierarchical relationship between policies. When EU AI Act "explainability" requirements conflict with ITAR "no technical data disclosure" requirements, there's no mechanism to resolve the conflict programmatically. |

### Gap Detail

The current governance stack has:
- **Horizontal coverage:** Checklists for each lifecycle stage
- **Framework mapping:** Cross-references between NIST, EU AI Act, ISO 42001, Singapore MGF
- **But no vertical hierarchy:** No parent-child policy relationships, no inheritance, no conflict resolution

### Remediation Plan

| Sprint | Task | Deliverable | Effort |
|--------|------|-------------|--------|
| **S1** | Design policy tree schema | `policy-tree-schema.yaml` — defines nodes (policies), edges (inheritance/conflict), and resolution rules | 1 sprint |
| **S1** | Map existing checklists to tree nodes | Each checklist item becomes a leaf node with parent references | 0.5 sprint |
| **S2** | Define inheritance rules | `policy-inheritance-rules.md` — how child policies inherit from parents, override semantics | 0.5 sprint |
| **S2** | Build conflict detection engine | `tools/policy-tree/conflict-detector/` — analyzes policy tree for logical conflicts (e.g., "must explain" vs "must not disclose") | 1 sprint |
| **S3** | Implement conflict resolution strategies | `policy-conflict-resolution.yaml` — priority ordering (regulatory > contractual > internal), jurisdiction-specific overrides | 1 sprint |
| **S3** | Build policy tree compiler | Compiles the hierarchical tree into flat OPA Rego policies with conflict resolution applied | 1 sprint |
| **S4** | Integrate with Gap 1 executable checklists | Policy tree feeds directly into OPA policy engine | 0.5 sprint |
| **S4** | Add provenance tracking (links to Gap 9 architecture) | Each compiled policy traces back to its source regulation and tree position | 0.5 sprint |

**Total Effort:** 6 sprints
**Dependencies:** Gap 1 (executable checklists) — policy tree compiles into Rego
**Blocks:** Cross-framework compliance for regulated clients

### Policy Tree Structure (Proposed)

```
ROOT: ProtoLabs AI Governance Policy
├── REGULATORY: EU AI Act
│   ├── Art. 9: Risk Management
│   │   ├── [inherits to] Tier 1 Controls
│   │   ├── [inherits to] Tier 2 Controls
│   │   └── [inherits to] Tier 3 Controls
│   ├── Art. 14: Human Oversight
│   │   └── [conflict with] ITAR: No Technical Data Disclosure
│   │       └── [resolution] Jurisdiction override: ITAR takes precedence
│   └── Art. 50: Transparency
│       └── [inherits to] Client-Facing Agent Disclosure
├── REGULATORY: ITAR/EAR
│   ├── Technical Data Controls
│   │   └── [overrides] EU AI Act Art. 14 explainability when ITAR applies
│   └── Export Control Screening
├── SECTOR: AS9100D (Aerospace)
│   └── [inherits to] Aerospace Vertical Agent Controls
├── SECTOR: ISO 13485 (Medical)
│   └── [inherits to] Medical Vertical Agent Controls
├── INTERNAL: ProtoLabs Standards
│   ├── DFM Accuracy Requirements
│   └── Client Data Handling
└── CONTRACTUAL: Per-Client Overrides
    └── [compiled per order] Client-Specific Guardrails
```

### Success Criteria

- [ ] All existing checklists mapped to policy tree nodes
- [ ] Conflict detection identifies all known regulatory conflicts (minimum: EU AI Act vs ITAR)
- [ ] Conflict resolution produces deterministic, auditable decisions
- [ ] Compiled Rego policies reflect resolved policy tree
- [ ] Policy tree is version-controlled and auditable

---

## Gap 7: No Adversarial Testing Framework

### Current State

| Aspect | Detail |
|--------|--------|
| **Existing Architecture** | WP02 Adversarial Defense (mentioned in `GOVERNANCE-FRAMEWORK-MAPPING.md`), eval suites per agent |
| **What Works** | Eval-driven development, golden dataset testing, performance benchmarks |
| **What's Missing** | No systematic adversarial testing covering OWASP LLM Top 10 (2025) or agentic-specific attack taxonomy. Red-team exercises are mentioned but not codified into CI/CD. |

### Gap Detail

Current testing is **functional** (does the agent produce correct outputs?) but not **adversarial** (can the agent be manipulated into producing harmful outputs?). The eval suites test for accuracy, not for security.

### Remediation Plan

| Sprint | Task | Deliverable | Effort |
|--------|------|-------------|--------|
| **S1** | Codify OWASP LLM Top 10 (2025) as test cases | `tests/adversarial/owasp-llm-top10/` — 10 test suites covering each OWASP category | 1 sprint |
| **S1** | Define agentic attack taxonomy | `agentic-attack-taxonomy.md` — tool misuse, delegation chain abuse, memory poisoning, context manipulation | 0.5 sprint |
| **S2** | Build adversarial test harness | `tools/adversarial-test-harness/` — automated framework for running attack scenarios against agents | 1 sprint |
| **S2** | Implement prompt injection test suite | `tests/adversarial/prompt-injection/` — 50+ injection patterns targeting ProtoLabs-specific contexts | 1 sprint |
| **S3** | Build tool misuse test suite | `tests/adversarial/tool-misuse/` — tests that attempt to invoke tools outside agent permissions | 1 sprint |
| **S3** | Implement delegation chain attack tests | `tests/adversarial/delegation-attacks/` — tests for privilege escalation through agent delegation | 0.5 sprint |
| **S4** | Integrate adversarial tests into CI/CD | GitHub Actions workflow: adversarial tests run on every agent change, block deployment on failure | 0.5 sprint |
| **S4** | Build red-team exercise automation | `tools/red-team-automation/` — LLM-based red-team agent that generates novel attack patterns | 1 sprint |
| **S4** | Add adversarial metrics to governance dashboard | Attack success rate, coverage by OWASP category, trend analysis | 0.5 sprint |

**Total Effort:** 7.5 sprints
**Dependencies:** Gap 1 (for policy-as-code integration)
**Blocks:** Production deployment of Tier 2+ agents

### OWASP LLM Top 10 (2025) Coverage

| # | Category | Test Approach | Priority |
|---|----------|--------------|----------|
| LLM01 | Prompt Injection | 50+ injection patterns, context manipulation | P0 |
| LLM02 | Sensitive Information Disclosure | Tests for ITAR/PII leakage through agent outputs | P0 |
| LLM03 | Supply Chain Vulnerabilities | Third-party model/vendor integrity checks | P1 |
| LLM04 | Data and Model Poisoning | Training data integrity, RAG poisoning detection | P1 |
| LLM05 | Improper Output Handling | Output validation, XSS/injection in generated content | P0 |
| LLM06 | Excessive Agency | Tool invocation beyond permissions, privilege escalation | P0 |
| LLM07 | System Prompt Leakage | Tests for system prompt extraction | P1 |
| LLM08 | Vector and Embedding Weaknesses | RAG manipulation, embedding poisoning | P1 |
| LLM09 | Misinformation | Grounding verification, hallucination detection | P1 |
| LLM10 | Unbounded Consumption | Resource exhaustion, cost amplification attacks | P2 |

### Success Criteria

- [ ] 100% of OWASP LLM Top 10 categories have automated test coverage
- [ ] Agentic attack taxonomy covers tool misuse, delegation, memory poisoning
- [ ] Adversarial tests run in CI/CD and block deployment on failure
- [ ] Attack success rate tracked per agent per quarter
- [ ] Red-team exercise generates novel attacks quarterly

---

## Gap 10: No Control Tax Analysis

### Current State

| Aspect | Detail |
|--------|--------|
| **Existing Architecture** | None — controls are treated equally with no cost/benefit analysis |
| **What Works** | Comprehensive control catalog (52+ controls across lifecycle stages) |
| **What's Missing** | No quantification of the operational and financial cost per control. No way to answer: "Is this control worth its latency/cost overhead?" |

### Gap Detail

The governance framework defines *what* controls exist and *when* they apply, but not *how much they cost* or *whether the cost is justified*. This makes it impossible to optimize the control portfolio.

### Remediation Plan

| Sprint | Task | Deliverable | Effort |
|--------|------|-------------|--------|
| **S1** | Define control cost model | `control-cost-model.md` — categories: compute cost, latency overhead, human review time, tooling cost, maintenance burden | 0.5 sprint |
| **S1** | Inventory all controls and assign cost categories | `control-tax-inventory.yaml` — every control tagged with cost type and estimated cost | 0.5 sprint |
| **S2** | Instrument control execution with cost tracking | Each control in the 7-layer pipeline emits cost metrics (latency, compute, tokens) | 1 sprint |
| **S2** | Define risk mitigation value model | `risk-mitigation-value-model.md` — maps each control to the risk(s) it mitigates and the expected loss reduction | 0.5 sprint |
| **S3** | Build control tax dashboard | Real-time dashboard: cost per control, cost per agent, cost per order, ROI per control | 1 sprint |
| **S3** | Implement optimization recommendations | `tools/control-tax-optimizer/` — analyzes cost vs. risk reduction, recommends control adjustments | 1 sprint |
| **S4** | Integrate with policy tree (Gap 5) | Control tax data feeds into policy conflict resolution (cheaper control wins when equivalent) | 0.5 sprint |
| **S4** | Add control tax to quarterly governance report | Board-level view: total governance cost, cost per risk category, optimization opportunities | 0.5 sprint |

**Total Effort:** 5.5 sprints
**Dependencies:** Gap 1 (executable checklists for cost instrumentation), Gap 5 (policy tree for optimization)
**Blocks:** Governance cost optimization, board-level ROI reporting

### Control Tax Categories

| Category | Cost Drivers | Measurement |
|----------|-------------|-------------|
| **Compute** | GPU/CPU time for guardrails, evals, monitoring | $/execution |
| **Latency** | Added latency to agent response time | ms/execution |
| **Human Review** | Engineer/compliance officer time for approvals | hours/quarter |
| **Tooling** | License costs for OPA, monitoring, audit tools | $/month |
| **Maintenance** | Engineering time to update policies, fix false positives | hours/quarter |
| **Opportunity Cost** | Delayed deployments due to governance gates | days/feature |

### Success Criteria

- [ ] Every control has a quantified cost estimate
- [ ] Control tax dashboard shows real-time cost per control per agent
- [ ] Optimization recommendations generated quarterly
- [ ] Board report includes governance cost breakdown
- [ ] At least 2 controls optimized based on cost/benefit analysis in first quarter

---

## Implementation Summary

### Effort by Gap

| Gap | Sprints | Priority | Dependencies |
|-----|---------|----------|--------------|
| Gap 1: Executable Checklists | 6.5 | **P0** — blocks everything | None |
| Gap 3: Formal Verification | 10.5 | **P2** — blocks Tier 3 safety-critical | Gap 1 |
| Gap 4: Multi-Modal CAD Guardrails | 6 | **P1** — blocks CAD system deployment | Gap 1 |
| Gap 5: Policy Tree with Inheritance | 6 | **P1** — blocks cross-framework compliance | Gap 1 |
| Gap 7: Adversarial Testing | 7.5 | **P1** — blocks Tier 2+ deployment | Gap 1 |
| Gap 10: Control Tax | 5.5 | **P2** — enables optimization | Gap 1, Gap 5 |
| **TOTAL** | **42 sprints** | | |

### Recommended Sequencing

```
PHASE 1 (Sprints 1-6): Foundation
├── Gap 1: Executable Checklists (S1-S4)
├── Gap 5: Policy Tree (S1-S4, parallel with Gap 1)
└── Gap 7: Adversarial Testing (S1-S2, start after Gap 1 S2)

PHASE 2 (Sprints 7-12): Production Readiness
├── Gap 4: Multi-Modal CAD Guardrails (S1-S4)
├── Gap 7: Adversarial Testing (S3-S4, complete)
└── Gap 10: Control Tax (S1-S4)

PHASE 3 (Sprints 13-18): Advanced Capabilities
├── Gap 3: Formal Verification (S1-S8)
└── Gap 10: Control Tax optimization (ongoing)
```

### Budget Estimate

| Phase | Sprints | Team | Estimated Cost |
|-------|---------|------|----------------|
| Phase 1 | 6 | 3 engineers | $180K |
| Phase 2 | 6 | 4 engineers | $240K |
| Phase 3 | 6 | 3 engineers | $180K |
| **TOTAL** | **18** | **Avg 3.3 engineers** | **$600K** |

---

## Cross-References

| Document | Relationship |
|----------|-------------|
| [7-Layer Governance Enforcement Pipeline](../governance/03-runtime-governance/agentic-workflows/governance-enforcement-pipeline.md) | Existing architecture that Gap 1 implements |
| [Safety Agent Architecture](../governance/03-runtime-governance/agentic-workflows/safety-agent-architecture.md) | Existing architecture extended by Gap 3 |
| [Multi-Tenant Isolation](../governance/03-runtime-governance/agentic-workflows/multi-tenant-isolation.md) | Existing architecture referenced by Gap 4 |
| [AI Governance Policy](../governance/ai-governance-policy.md) | Parent policy |
| [ISO 42001 Gap Analysis](../docs/iso-42001-gap-analysis.md) | Certification readiness affected by these gaps |
| [Governance Framework Architecture](../docs/governance-framework-architecture.md) | Updated architecture document |

---

*This document is version-controlled and auditable. It should be reviewed quarterly alongside the ISO 42001 gap analysis.*
