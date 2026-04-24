# ISO/IEC 42001:2023 Gap Analysis & Certification Roadmap

> **Purpose:** Maps every clause of ISO/IEC 42001 (AI Management System) to existing ProtoLabs governance artifacts, identifies gaps, and provides a certification readiness roadmap for aerospace/medical client procurement requirements.

**Version:** 1.0  
**Last Updated:** 2026-04-24  
**Owner:** ProtoLabs AI Governance Office  
**Target Certification Date:** Q1 2027  
**Certification Body:** TÜV SÜD or BSI (recommended for manufacturing AI)  

---

## Executive Summary

ISO/IEC 42001 is the **only certifiable standard** in ProtoLabs' governance stack. While NIST AI RMF provides risk management guidance and Singapore MGF provides principles, ISO 42001 provides the **management system structure** that external auditors can certify.

### Certification Business Case

| Driver | Impact |
|--------|--------|
| **Aerospace clients (AS9100D)** | ISO 42001 certification becoming procurement gate for AI-powered suppliers |
| **Medical device clients (ISO 13485)** | FDA/MDR expecting AIMS for AI-enabled manufacturing partners |
| **Automotive (IATF 16949)** | OEMs requiring AI management system evidence in PPAP submissions |
| **EU AI Act compliance** | ISO 42001 recognized as "state of the art" for Article 9 risk management |
| **Competitive differentiation** | First-mover advantage in certified AI manufacturing governance |

### Current State Assessment

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ISO 42001 READINESS SCORECARD                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Clause 4 — Context of the Organisation        ████████████░░░░  80%       │
│  Clause 5 — Leadership                         ██████████░░░░░░░░  60%       │
│  Clause 6 — Planning                           ██████████████░░░░  85%       │
│  Clause 7 — Support                            ████████░░░░░░░░░░  50%       │
│  Clause 8 — Operation                          ████████████░░░░░░  70%       │
│  Clause 9 — Performance Evaluation             ██████████░░░░░░░░  60%       │
│  Clause 10 — Improvement                       ████████░░░░░░░░░░  50%       │
│  Annex A — AI Controls                         ████████████░░░░░░  70%       │
│  Annex B — Implementation Guidance             ██████████░░░░░░░░  60%       │
│                                                                              │
│  OVERALL READINESS                             ███████████░░░░░░░  65%       │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Clause-by-Clause Gap Analysis

### Clause 4: Context of the Organisation

> **Requirement:** Understand internal and external issues, determine the scope of the AIMS, and establish the AI management system.

#### 4.1 Understanding the Organisation and its Context

| Requirement | Existing Artifact | Gap | Action | Priority |
|-------------|-------------------|-----|--------|----------|
| Document internal issues (business objectives, capabilities) | `governance-charter.md` | Minor | Add AI-specific business context section | Medium |
| Document external issues (regulatory, market, tech) | `regulatory-reference-index.md` | None | Already comprehensive | — |
| Identify interested parties and their needs | `stakeholder-value-map.md` | Minor | Add client procurement requirements explicitly | Medium |

**Evidence Status:** ✅ **STRONG** — `ml-lifecycle-canvas.md` and `regulatory-reference-index.md` provide comprehensive context.

#### 4.2 Understanding the Needs and Expectations of Interested Parties

| Interested Party | Needs Documented? | Evidence | Gap |
|------------------|-------------------|----------|-----|
| Aerospace clients (AS9100D) | Partial | `vertical-aerospace.agent.md` | Need explicit procurement requirements mapping |
| Medical device clients (ISO 13485) | Partial | `vertical-medical.agent.md` | Need FDA/MDR AI supplier expectations |
| Automotive OEMs (IATF 16949) | Partial | `vertical-automotive-ev.agent.md` | Need PPAP AI governance requirements |
| Regulators (EU AI Act, NIST) | Yes | `regulatory-reference-index.md` | None |
| Internal stakeholders | Yes | `governance-roles-raci.md` | None |

**Gap:** Missing explicit **client procurement requirement mapping** for ISO 42001 certification as a supplier qualification.

**Action:** Create `client-procurement-requirements-mapping.md` linking AS9100D, ISO 13485, IATF 16949 AI clauses to ProtoLabs AIMS.

#### 4.3 Determining the Scope of the AI Management System

| Requirement | Status | Evidence |
|-------------|--------|----------|
| Scope boundaries defined | ✅ | `agent-tier-classification.yaml` defines all agents in scope |
| Scope includes AI system lifecycle | ✅ | `product-development-lifecycle.md` covers 7 gates |
| Scope exclusions justified | ⚠️ | Need explicit statement: "Excluded: third-party AI tools not integrated into ProtoLabs agent fleet" |

**Gap:** No explicit scope exclusion statement for non-integrated third-party AI.

**Action:** Add scope statement to `governance-charter.md`.

#### 4.4 AI Management System

| Requirement | Status | Evidence |
|-------------|--------|----------|
| Establish, implement, maintain, and continually improve AIMS | ✅ | Full governance framework operational |
| Processes and their interactions defined | ✅ | `product-development-lifecycle.md` + `governance-by-stage-framework.md` |

**Evidence Status:** ✅ **STRONG**

---

### Clause 5: Leadership

> **Requirement:** Top management must demonstrate leadership and commitment to the AIMS.

#### 5.1 Leadership and Commitment

| Requirement | Status | Evidence | Gap |
|-------------|--------|----------|-----|
| Board-level AI policy | ✅ | `governance-charter.md` | None |
| AI policy aligned with business strategy | ⚠️ | `ai-risk-appetite-framework.md` | Need explicit board resolution linking AI governance to business objectives |
| Resource allocation for AIMS | ❌ | None | Need budget line item for AIMS operations |
| Management review meetings | ⚠️ | `quarterly-governance-report.md` | Need explicit ISO 42001 management review agenda |

**Gap:** No explicit **board resolution** or **dedicated AIMS budget**.

**Action:** 
1. Create `board-resolution-aims.md` — formal board resolution adopting ISO 42001
2. Add AIMS budget line to `quarterly-governance-report.md` Section 10

#### 5.2 AI Policy

| Requirement | Status | Evidence |
|-------------|--------|----------|
| Policy established | ✅ | `governance-charter.md` |
| Policy communicated | ⚠️ | Internal only | Need client-facing policy summary |
| Policy available as documented information | ✅ | `governance-charter.md` version-controlled |

**Gap:** No **client-facing AI policy summary** for procurement questionnaires.

**Action:** Create `ai-policy-client-summary.md` — one-page summary for RFP responses.

#### 5.3 Organizational Roles, Responsibilities, and Authorities

| Requirement | Status | Evidence | Gap |
|-------------|--------|----------|-----|
| Roles defined | ✅ | `governance-roles-raci.md` | None |
| Responsibilities assigned | ✅ | `raci-by-ai-lifecycle-stage.md` | None |
| Authorities defined | ⚠️ | Partial | Need explicit signing authority for AIMS decisions |

**Gap:** No explicit **signing authority matrix** for AIMS decisions (e.g., who can approve Tier 3 agent deployment?).

**Action:** Create `aims-signing-authority-matrix.md`.

---

### Clause 6: Planning

> **Requirement:** Plan actions to address risks and opportunities, establish AI objectives, and plan changes.

#### 6.1 Actions to Address Risks and Opportunities

| Requirement | Status | Evidence | Gap |
|-------------|--------|----------|-----|
| Risk assessment methodology | ✅ | `risk-management-plan.md` | None |
| Risk register maintained | ✅ | Risk registers per stage in `governance-by-stage-framework.md` | None |
| Opportunities identified | ⚠️ | Partial | Need explicit "AI opportunity register" |
| Risk treatment plans | ✅ | `risk-mitigation-plan.md` | None |

**Gap:** No explicit **AI opportunity register** (ISO 42001 requires opportunities, not just risks).

**Action:** Create `ai-opportunity-register.md` — business value, competitive advantage, innovation potential.

#### 6.2 AI Objectives and Planning to Achieve Them

| Requirement | Status | Evidence | Gap |
|-------------|--------|----------|-----|
| AI objectives established | ⚠️ | Implicit in eval metrics | Need explicit SMART objectives for AIMS |
| Objectives measurable | ⚠️ | Partial | Need KPIs specifically for AIMS effectiveness |
| Monitoring plan for objectives | ❌ | None | Need AIMS KPI dashboard |

**Gap:** No explicit **AIMS objectives** or **AIMS-specific KPIs**.

**Action:** Create `aims-objectives-and-kpis.md` with targets like:
- "Achieve ISO 42001 certification by Q1 2027"
- "Maintain >95% DFM accuracy across all specialist agents"
- "Zero safety incidents from Tier 2/3 agent actions"
- "100% audit trail completeness for all agent decisions"

#### 6.3 Planning of Changes

| Requirement | Status | Evidence | Gap |
|-------------|--------|----------|-----|
| Change management process | ✅ | `change-management-for-ai.md` | None |
| Changes planned systematically | ✅ | `governance-in-cicd.md` | None |
| Impact assessment for changes | ⚠️ | Partial | Need explicit AIMS impact assessment template |

**Gap:** No **AIMS-specific change impact assessment** (e.g., "Does this model update affect certification scope?").

**Action:** Add AIMS impact section to `change-management-for-ai.md`.

---

### Clause 7: Support

> **Requirement:** Provide resources, competence, awareness, communication, and documented information.

#### 7.1 Resources

| Requirement | Status | Evidence | Gap |
|-------------|--------|----------|-----|
| Personnel resources | ✅ | `governance-roles-raci.md` | None |
| Infrastructure (compute, tools) | ⚠️ | Partial | Need explicit AIMS infrastructure inventory |
| Financial resources | ❌ | None | Need AIMS budget |

**Gap:** No **AIMS infrastructure inventory** or **dedicated budget**.

**Action:** 
1. Create `aims-infrastructure-inventory.md` — tools, platforms, environments
2. Add AIMS budget to annual planning

#### 7.2 Competence

| Requirement | Status | Evidence | Gap |
|-------------|--------|----------|-----|
| Competence requirements defined | ⚠️ | Partial | `test-plan-for-ai.md` references competence | Need explicit competence matrix |
| Training delivered | ⚠️ | Partial | `training-and-awareness-plan.md` exists | Need completion tracking |
| Competence records maintained | ❌ | None | Need training records per role |

**Gap:** No **competence matrix** or **training completion tracking**.

**Action:** Create `aims-competence-matrix.md` mapping roles to required skills, certifications, and training status.

#### 7.3 Awareness

| Requirement | Status | Evidence | Gap |
|-------------|--------|----------|-----|
| AI policy awareness | ⚠️ | Partial | Need awareness campaign evidence |
| Role-specific awareness | ⚠️ | Partial | Need role-specific awareness materials |
| Consequences of non-conformance | ❌ | None | Need explicit consequences documentation |

**Gap:** No evidence of **awareness campaigns** or **consequences of non-conformance**.

**Action:** 
1. Create awareness campaign plan with dates, attendance, materials
2. Document consequences in `governance-charter.md`

#### 7.4 Communication

| Requirement | Status | Evidence | Gap |
|-------------|--------|----------|-----|
| Internal communication plan | ⚠️ | Partial | `quarterly-governance-report.md` | Need explicit communication plan |
| External communication plan | ❌ | None | Need client/regulator communication plan |

**Gap:** No **external communication plan** for AI governance (e.g., how do we communicate incidents to clients?).

**Action:** Create `aims-communication-plan.md` — internal and external communication protocols.

#### 7.5 Documented Information

| Requirement | Status | Evidence | Gap |
|-------------|--------|----------|-----|
| Document control | ✅ | Version control on all artifacts | None |
| Records retention | ⚠️ | Partial | `audit-record-schema.yaml` | Need explicit retention schedule for AIMS records |
| Documented information available | ✅ | All artifacts in `governance/` | None |

**Gap:** No **explicit retention schedule** for AIMS records (ISO 42001 requires defined retention periods).

**Action:** Create `aims-document-retention-schedule.md`.

---

### Clause 8: Operation

> **Requirement:** Plan, implement, and control the processes needed to meet AI system requirements.

#### 8.1 Operational Planning and Control

| Requirement | Status | Evidence | Gap |
|-------------|--------|----------|-----|
| AI system development processes | ✅ | `product-development-lifecycle.md` | None |
| AI system deployment processes | ✅ | `pre-deployment-gate.yaml` | None |
| Process controls defined | ✅ | `governance-enforcement-pipeline.md` | None |

**Evidence Status:** ✅ **STRONG**

#### 8.2 AI Risk Assessment

| Requirement | Status | Evidence | Gap |
|-------------|--------|----------|-----|
| Risk assessment for each AI system | ✅ | `risk-management-plan.md` + per-agent risk registers | None |
| Risk treatment implemented | ✅ | `risk-mitigation-plan.md` | None |
| Residual risk accepted | ⚠️ | Partial | Need explicit risk acceptance signatures |

**Gap:** No **explicit risk acceptance signatures** at board level for residual risks.

**Action:** Add risk acceptance signature block to `risk-management-plan.md`.

#### 8.3 AI Risk Treatment

| Requirement | Status | Evidence | Gap |
|-------------|--------|----------|-----|
| Treatment measures implemented | ✅ | WP01-WP04 implementation | None |
| Treatment effectiveness evaluated | ⚠️ | Partial | Need periodic treatment effectiveness review |

**Gap:** No **periodic treatment effectiveness review** (e.g., "Is WP01 still effective against new injection techniques?").

**Action:** Add treatment effectiveness review to quarterly governance report agenda.

#### 8.4 AI System Lifecycle Processes

| Requirement | Status | Evidence | Gap |
|-------------|--------|----------|-----|
| Requirements specification | ✅ | `responsible-product-brief.md` | None |
| Design and development | ✅ | `eval-driven-development.md` | None |
| Verification and validation | ✅ | `test-plan-for-ai.md` | None |
| Deployment | ✅ | `pre-deployment-gate.yaml` | None |
| Monitoring | ✅ | `continuous-monitoring-plan.md` | None |
| Retirement | ⚠️ | Partial | `model-retirement-procedure.md` missing |

**Gap:** No **model retirement procedure** (ISO 42001 requires planned decommissioning).

**Action:** Create `model-retirement-procedure.md` — data archival, knowledge transfer, client notification.

---

### Clause 9: Performance Evaluation

> **Requirement:** Monitor, measure, analyze, and evaluate the AIMS.

#### 9.1 Monitoring, Measurement, Analysis, and Evaluation

| Requirement | Status | Evidence | Gap |
|-------------|--------|----------|-----|
| Monitoring plan | ✅ | `continuous-monitoring-plan.md` | None |
| Performance indicators | ⚠️ | Partial | `ai-quality-metrics-catalog.md` | Need AIMS-specific KPIs |
| Evaluation methods | ✅ | `eval-driven-development.md` | None |
| Evaluation results documented | ⚠️ | Partial | Need centralized AIMS evaluation repository |

**Gap:** No **centralized AIMS evaluation repository** or **AIMS-specific KPIs**.

**Action:** 
1. Create `aims-evaluation-repository.md` — index of all eval results
2. Define AIMS KPIs in `aims-objectives-and-kpis.md`

#### 9.2 Internal Audit

| Requirement | Status | Evidence | Gap |
|-------------|--------|----------|-----|
| Internal audit program | ❌ | None | Need ISO 42001 internal audit plan |
| Audit criteria defined | ❌ | None | Need audit checklist against ISO 42001 clauses |
| Audit results reported to management | ❌ | None | Need audit report template |

**Gap:** No **internal audit program** for ISO 42001.

**Action:** 
1. Create `aims-internal-audit-plan.md` — annual audit schedule
2. Create `aims-internal-audit-checklist.md` — clause-by-clause audit criteria
3. Create `aims-internal-audit-report-template.md`

#### 9.3 Management Review

| Requirement | Status | Evidence | Gap |
|-------------|--------|----------|-----|
| Management review inputs defined | ⚠️ | Partial | `quarterly-governance-report.md` | Need ISO 42001-specific review agenda |
| Management review outputs documented | ⚠️ | Partial | Need explicit management review minutes |
| Review frequency defined | ✅ | Quarterly | None |

**Gap:** No **ISO 42001-specific management review agenda** or **formal minutes**.

**Action:** 
1. Create `aims-management-review-agenda.md` — ISO 42001 clause review checklist
2. Create `aims-management-review-minutes-template.md`

---

### Clause 10: Improvement

> **Requirement:** Continually improve the suitability, adequacy, and effectiveness of the AIMS.

#### 10.1 Nonconformity and Corrective Action

| Requirement | Status | Evidence | Gap |
|-------------|--------|----------|-----|
| Nonconformity identification | ✅ | `ai-incident-report.md` | None |
| Root cause analysis | ⚠️ | Partial | Need structured RCA template |
| Corrective action implementation | ⚠️ | Partial | Need corrective action tracking |
| Effectiveness of corrective action | ❌ | None | Need effectiveness verification |

**Gap:** No **structured RCA template**, **corrective action tracking**, or **effectiveness verification**.

**Action:** 
1. Create `aims-corrective-action-template.md` — 8D or similar structured RCA
2. Create `aims-corrective-action-tracker.md` — open/closed status, effectiveness review dates

#### 10.2 Continual Improvement

| Requirement | Status | Evidence | Gap |
|-------------|--------|----------|-----|
| Improvement opportunities identified | ⚠️ | Partial | `governance-maturity-roadmap.md` | Need explicit improvement register |
| Improvement actions implemented | ⚠️ | Partial | Need tracking mechanism |
| Improvement results evaluated | ❌ | None | Need effectiveness measurement |

**Gap:** No **improvement register** or **effectiveness measurement**.

**Action:** 
1. Create `aims-improvement-register.md` — opportunity, action, owner, target date, result
2. Link to `aims-objectives-and-kpis.md` for effectiveness measurement

---

## Annex A: AI Controls Gap Analysis

### A.1 AI Policy (Control 5.2)

| Control | Status | Evidence | Gap |
|---------|--------|----------|-----|
| Policy covers AI system purpose | ✅ | `governance-charter.md` | None |
| Policy covers ethical principles | ✅ | `ai-ethics-impact-assessment.md` | None |
| Policy covers regulatory compliance | ✅ | `regulatory-reference-index.md` | None |
| Policy reviewed annually | ⚠️ | Quarterly review cadence | Need annual policy review evidence |

### A.2 Internal Organization (Control 5.3)

| Control | Status | Evidence | Gap |
|---------|--------|----------|-----|
| Roles for AI system lifecycle | ✅ | `governance-roles-raci.md` | None |
| Independence of oversight | ⚠️ | Partial | Need explicit independence statement for Safety Officer |

### A.3 Resources for AI Systems (Control 7.1)

| Control | Status | Evidence | Gap |
|---------|--------|----------|-----|
| Data resources | ✅ | `data-governance-plan.md` | None |
| Compute resources | ⚠️ | Partial | Need infrastructure inventory |
| Human resources | ✅ | `governance-roles-raci.md` | None |

### A.4 Assessing and Treating AI Risks (Controls 6.1, 8.2, 8.3)

| Control | Status | Evidence | Gap |
|---------|--------|----------|-----|
| Risk assessment | ✅ | `risk-management-plan.md` | None |
| Risk treatment | ✅ | `risk-mitigation-plan.md` | None |
| Residual risk acceptance | ⚠️ | Partial | Need explicit acceptance |

### A.5 AI System Impact Assessment (Control 8.2)

| Control | Status | Evidence | Gap |
|---------|--------|----------|-----|
| Impact assessment for each system | ✅ | `ml-lifecycle-canvas.md` | None |
| Re-assessment on significant change | ⚠️ | Partial | Need change-triggered re-assessment procedure |

### A.6 AI System Objectives (Control 6.2)

| Control | Status | Evidence | Gap |
|---------|--------|----------|-----|
| Objectives established | ⚠️ | Partial | Need explicit AIMS objectives |
| Objectives monitored | ❌ | None | Need AIMS KPI dashboard |

### A.7 AI System Design and Development (Control 8.4)

| Control | Status | Evidence | Gap |
|---------|--------|----------|-----|
| Requirements specification | ✅ | `responsible-product-brief.md` | None |
| Design documentation | ✅ | `model-card.md` | None |
| Testing and validation | ✅ | `test-plan-for-ai.md` | None |
| Version control | ✅ | Git-based | None |

### A.8 AI System Deployment (Control 8.4)

| Control | Status | Evidence | Gap |
|---------|--------|----------|-----|
| Deployment procedures | ✅ | `pre-deployment-gate.yaml` | None |
| Rollback procedures | ⚠️ | Partial | Need explicit rollback plan |
| Post-deployment monitoring | ✅ | `continuous-monitoring-plan.md` | None |

### A.9 AI System Monitoring (Control 9.1)

| Control | Status | Evidence | Gap |
|---------|--------|----------|-----|
| Performance monitoring | ✅ | `model-monitoring-dashboard.md` | None |
| Drift detection | ✅ | `drift-detection-evals.md` | None |
| Incident detection | ✅ | `ai-incident-report.md` | None |

### A.10 AI System Documentation (Control 7.5)

| Control | Status | Evidence | Gap |
|---------|--------|----------|-----|
| Model documentation | ✅ | `model-card.md` | None |
| System documentation | ✅ | `agent-registry-entry.yaml` | None |
| Operational documentation | ✅ | `runbook-*.md` | None |

---

## Certification Roadmap

### Phase 1: Gap Closure (Q2-Q3 2026)

| Week | Activity | Deliverable | Owner |
|------|----------|-------------|-------|
| 1-2 | Create missing artifacts (board resolution, AIMS objectives, competence matrix) | 12 new documents | AI Governance Office |
| 3-4 | Implement internal audit program | Audit plan + checklist | Internal Audit |
| 5-6 | Conduct first internal audit | Audit report with findings | Internal Audit |
| 7-8 | Close internal audit findings | Corrective actions closed | Process Owners |
| 9-10 | Management review of AIMS readiness | Management review minutes | CAIO |
| 11-12 | Select certification body (TÜV SÜD or BSI) | Certification contract | Procurement |

### Phase 2: Pre-Certification (Q4 2026)

| Week | Activity | Deliverable | Owner |
|------|----------|-------------|-------|
| 13-16 | Stage 1 audit (documentation review) | Stage 1 report | Certification Body |
| 17-20 | Close Stage 1 findings | Corrective evidence | Process Owners |
| 21-24 | Stage 2 audit (on-site/remote assessment) | Stage 2 report | Certification Body |
| 25-26 | Close Stage 2 nonconformities | Corrective actions | Process Owners |

### Phase 3: Certification (Q1 2027)

| Week | Activity | Deliverable | Owner |
|------|----------|-------------|-------|
| 27-28 | Certification decision | ISO 42001 certificate | Certification Body |
| 29-30 | Communicate certification to clients | Press release, RFP updates | Marketing |
| 31-52 | Surveillance audit preparation | Continuous compliance | AI Governance Office |

---

## Resource Requirements

| Resource | Internal | External | Cost Estimate |
|----------|----------|----------|---------------|
| AI Governance Office (0.5 FTE) | ✅ | — | $75K |
| Internal Audit (0.25 FTE) | ✅ | — | $35K |
| Certification body fees | — | ✅ | $25K |
| Consultant (gap closure support) | — | ✅ | $40K |
| Training (ISO 42001 lead auditor) | — | ✅ | $5K |
| **Total** | | | **~$180K** |

---

## Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Gap closure rate | 100% by Q3 2026 | Artifact completion tracker |
| Internal audit findings | <5 major, 0 critical | Audit report |
| Certification audit findings | 0 critical, <3 minor | Stage 2 report |
| Time to certification | Q1 2027 | Certificate date |
| Client procurement wins attributed to certification | 2+ by Q2 2027 | CRM tracking |

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-24 | ProtoLabs AI Governance Office | Initial gap analysis and certification roadmap |

---

## See Also

- `governance/05-cross-cutting/nist-ai-rmf-compliance-mapping.md` — Multi-framework cross-mapping
- `governance/05-cross-cutting/regulatory-reference-index.md` — Regulatory reference index
- `governance/06-executive/quarterly-governance-report.md` — Quarterly governance report template
- `docs/governance-by-stage-framework.md` — Stage-by-stage governance mapping
