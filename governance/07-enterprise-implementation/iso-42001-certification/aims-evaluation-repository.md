# AIMS Evaluation Repository — ISO/IEC 42001 Evidence Collection

> **Purpose:** Central repository index for all evaluation evidence supporting the ProtoLabs AI Management System, enabling efficient demonstration of conformity during internal audits, certification audits, and client assessments.

**Version:** 1.0  
**Last Updated:** 2026-04-24  
**Owner:** Chief AI Officer / Compliance Officer  
**Review Cycle:** Quarterly  
**Classification:** Confidential — Internal Distribution  

---

## Repository Structure

```
governance/07-enterprise-implementation/iso-42001-certification/
├── 01-context-and-leadership/          # Clause 4-5 evidence
├── 02-planning/                        # Clause 6 evidence
├── 03-support/                         # Clause 7 evidence
├── 04-operations/                      # Clause 8 evidence
├── 05-performance-evaluation/          # Clause 9 evidence
├── 06-improvement/                     # Clause 10 evidence
├── 99-certification-body/              # External audit evidence
└── INDEX.md                            # This file
```

---

## Clause 4: Context of the Organisation

### 4.1 Understanding the Organisation and its Context

| Evidence ID | Description | Location | Owner | Last Updated |
|-------------|-------------|----------|-------|--------------|
| E-4.1-001 | Organisational context analysis | `governance/00-getting-started/` | CAIO | 2026-04-24 |
| E-4.1-002 | External issues register (regulatory, market, technology) | `governance/01-discovery-governance/` | Compliance Officer | 2026-04-24 |
| E-4.1-003 | Internal issues register (capabilities, culture, resources) | `governance/00-getting-started/` | CAIO | 2026-04-24 |

### 4.2 Understanding the Needs and Expectations of Interested Parties

| Evidence ID | Description | Location | Owner | Last Updated |
|-------------|-------------|----------|-------|--------------|
| E-4.2-001 | Interested parties register | `governance/01-discovery-governance/` | Policy Owner | 2026-04-24 |
| E-4.2-002 | Client requirements mapping | `client-procurement-requirements-mapping.md` | Sales Engineering | 2026-04-24 |
| E-4.2-003 | Regulatory requirements tracker | `governance/01-discovery-governance/` | Compliance Officer | 2026-04-24 |

### 4.3 Determining the Scope of the AIMS

| Evidence ID | Description | Location | Owner | Last Updated |
|-------------|-------------|----------|-------|--------------|
| E-4.3-001 | AIMS scope statement | `board-resolution-aims.md` | CAIO | 2026-04-24 |
| E-4.3-002 | Scope boundaries diagram | `docs/governance-by-stage-framework.md` | CAIO | 2026-04-24 |
| E-4.3-003 | Exclusions justification (if any) | `board-resolution-aims.md` | CAIO | 2026-04-24 |

### 4.4 AI Management System

| Evidence ID | Description | Location | Owner | Last Updated |
|-------------|-------------|----------|-------|--------------|
| E-4.4-001 | AIMS process map | `docs/governance-by-stage-framework.md` | CAIO | 2026-04-24 |
| E-4.4-002 | Process interaction matrix | `governance/02-development-governance/` | Technical Owner | 2026-04-24 |
| E-4.4-003 | AIMS documentation structure | `governance/` (all folders) | Governance Office | 2026-04-24 |

---

## Clause 5: Leadership

### 5.1 Leadership and Commitment

| Evidence ID | Description | Location | Owner | Last Updated |
|-------------|-------------|----------|-------|--------------|
| E-5.1-001 | Board resolution for AIMS | `board-resolution-aims.md` | Board Secretary | 2026-04-24 |
| E-5.1-002 | Management review minutes | `aims-management-review-minutes-template.md` | Governance Office | 2026-04-24 |
| E-5.1-003 | Resource allocation records | Finance records | CFO | 2026-04-24 |

### 5.2 AI Policy

| Evidence ID | Description | Location | Owner | Last Updated |
|-------------|-------------|----------|-------|--------------|
| E-5.2-001 | AI policy (internal) | `governance/01-discovery-governance/ai-policy.md` | Policy Owner | 2026-04-24 |
| E-5.2-002 | AI policy (client summary) | `ai-policy-client-summary.md` | Policy Owner | 2026-04-24 |
| E-5.2-003 | Policy communication records | Email/Intranet records | Governance Office | 2026-04-24 |

### 5.3 Organisational Roles, Responsibilities and Authorities

| Evidence ID | Description | Location | Owner | Last Updated |
|-------------|-------------|----------|-------|--------------|
| E-5.3-001 | AIMS roles and responsibilities | `aims-signing-authority-matrix.md` | CAIO | 2026-04-24 |
| E-5.3-002 | RACI matrix | `governance/00-getting-started/` | Governance Office | 2026-04-24 |
| E-5.3-003 | Job descriptions (AI-related roles) | HR records | HR | 2026-04-24 |

---

## Clause 6: Planning

### 6.1 Actions to Address Risks and Opportunities

| Evidence ID | Description | Location | Owner | Last Updated |
|-------------|-------------|----------|-------|--------------|
| E-6.1-001 | Risk and opportunity assessment methodology | `governance/02-development-governance/` | Compliance Officer | 2026-04-24 |
| E-6.1-002 | AI risk register | `governance/03-runtime-governance/` | Safety Officer | 2026-04-24 |
| E-6.1-003 | Opportunity register | `ai-opportunity-register.md` | CAIO | 2026-04-24 |
| E-6.1-004 | Risk treatment plans | `work-package-01` through `work-package-04` | Technical Owner | 2026-04-24 |

### 6.2 AI Objectives and Planning to Achieve Them

| Evidence ID | Description | Location | Owner | Last Updated |
|-------------|-------------|----------|-------|--------------|
| E-6.2-001 | AI objectives and KPIs | `aims-objectives-and-kpis.md` | CAIO | 2026-04-24 |
| E-6.2-002 | Objective monitoring dashboard | MLOps dashboard | MLOps Lead | 2026-04-24 |
| E-6.2-003 | Objective achievement reports | Quarterly reports | Governance Office | 2026-04-24 |

### 6.3 Planning of Changes

| Evidence ID | Description | Location | Owner | Last Updated |
|-------------|-------------|----------|-------|--------------|
| E-6.3-001 | Change management procedure | `governance/02-development-governance/` | Technical Owner | 2026-04-24 |
| E-6.3-002 | Change request records | Change log | MLOps Lead | 2026-04-24 |
| E-6.3-003 | Impact assessment records | Change records | Safety Officer | 2026-04-24 |

---

## Clause 7: Support

### 7.1 Resources

| Evidence ID | Description | Location | Owner | Last Updated |
|-------------|-------------|----------|-------|--------------|
| E-7.1-001 | Resource inventory | `aims-infrastructure-inventory.md` | Technical Owner | 2026-04-24 |
| E-7.1-002 | Budget and resource plans | Finance records | CFO | 2026-04-24 |
| E-7.1-003 | Resource adequacy assessments | Management review records | CAIO | 2026-04-24 |

### 7.2 Competence

| Evidence ID | Description | Location | Owner | Last Updated |
|-------------|-------------|----------|-------|--------------|
| E-7.2-001 | Competence matrix | `aims-competence-matrix.md` | HR / CAIO | 2026-04-24 |
| E-7.2-002 | Training records | HR/LMS records | HR | 2026-04-24 |
| E-7.2-003 | Competence gap analysis | `aims-competence-matrix.md` | HR / CAIO | 2026-04-24 |

### 7.3 Awareness

| Evidence ID | Description | Location | Owner | Last Updated |
|-------------|-------------|----------|-------|--------------|
| E-7.3-001 | Awareness training materials | Training repository | HR | 2026-04-24 |
| E-7.3-002 | Training attendance records | LMS records | HR | 2026-04-24 |
| E-7.3-003 | Communication records | Email/Intranet | Governance Office | 2026-04-24 |

### 7.4 Communication

| Evidence ID | Description | Location | Owner | Last Updated |
|-------------|-------------|----------|-------|--------------|
| E-7.4-001 | Communication plan | `aims-communication-plan.md` | Governance Office | 2026-04-24 |
| E-7.4-002 | Internal communication records | Email/Intranet | Governance Office | 2026-04-24 |
| E-7.4-003 | External communication records | CRM/Email | Policy Owner | 2026-04-24 |

### 7.5 Documented Information

| Evidence ID | Description | Location | Owner | Last Updated |
|-------------|-------------|----------|-------|--------------|
| E-7.5-001 | Document control procedure | `governance/00-getting-started/` | Governance Office | 2026-04-24 |
| E-7.5-002 | Master document list | Document registry | Governance Office | 2026-04-24 |
| E-7.5-003 | Document retention schedule | `aims-document-retention-schedule.md` | Governance Office | 2026-04-24 |
| E-7.5-004 | Version control records | Git/Document management | Governance Office | 2026-04-24 |

---

## Clause 8: Operation

### 8.1 Operational Planning and Control

| Evidence ID | Description | Location | Owner | Last Updated |
|-------------|-------------|----------|-------|--------------|
| E-8.1-001 | Operational procedures | `governance/02-development-governance/` | Technical Owner | 2026-04-24 |
| E-8.1-002 | Process control records | MLOps logs | MLOps Lead | 2026-04-24 |
| E-8.1-003 | Criteria for processes | Agent specifications | Technical Owner | 2026-04-24 |

### 8.2 AI Risk Assessment

| Evidence ID | Description | Location | Owner | Last Updated |
|-------------|-------------|----------|-------|--------------|
| E-8.2-001 | AI risk assessment methodology | `governance/02-development-governance/` | Safety Officer | 2026-04-24 |
| E-8.2-002 | Agent risk assessments | Per-agent risk assessments | Safety Officer | 2026-04-24 |
| E-8.2-003 | Risk assessment review records | Review meeting minutes | Safety Officer | 2026-04-24 |

### 8.3 AI Risk Treatment

| Evidence ID | Description | Location | Owner | Last Updated |
|-------------|-------------|----------|-------|--------------|
| E-8.3-001 | Risk treatment plans | `work-package-01` through `work-package-04` | Technical Owner | 2026-04-24 |
| E-8.3-002 | Safety agent configuration | Safety architecture docs | Safety Officer | 2026-04-24 |
| E-8.3-003 | Guardrail implementation records | Configuration management | MLOps Lead | 2026-04-24 |
| E-8.3-004 | Kill switch test records | Test logs | Safety Officer | 2026-04-24 |

### 8.4 AI System Lifecycle

| Evidence ID | Description | Location | Owner | Last Updated |
|-------------|-------------|----------|-------|--------------|
| E-8.4-001 | AI system lifecycle procedure | `governance/02-development-governance/` | Technical Owner | 2026-04-24 |
| E-8.4-002 | Design and development records | Per-agent design docs | Technical Owner | 2026-04-24 |
| E-8.4-003 | Verification and validation records | Test reports | QA Lead | 2026-04-24 |
| E-8.4-004 | Deployment records | MLOps deployment logs | MLOps Lead | 2026-04-24 |
| E-8.4-005 | Model retirement records | `model-retirement-procedure.md` | Technical Owner | 2026-04-24 |

---

## Clause 9: Performance Evaluation

### 9.1 Monitoring, Measurement, Analysis and Evaluation

| Evidence ID | Description | Location | Owner | Last Updated |
|-------------|-------------|----------|-------|--------------|
| E-9.1-001 | Monitoring and measurement plan | `governance/03-runtime-governance/` | MLOps Lead | 2026-04-24 |
| E-9.1-002 | KPI monitoring dashboards | MLOps dashboard | MLOps Lead | 2026-04-24 |
| E-9.1-003 | Analysis and evaluation records | Quarterly reports | Governance Office | 2026-04-24 |
| E-9.1-004 | DFM accuracy evaluation results | `dfm-accuracy-eval-suite.yaml` | Technical Owner | 2026-04-24 |

### 9.2 Internal Audit

| Evidence ID | Description | Location | Owner | Last Updated |
|-------------|-------------|----------|-------|--------------|
| E-9.2-001 | Internal audit program | `aims-internal-audit-plan.md` | Internal Audit | 2026-04-24 |
| E-9.2-002 | Audit checklists | `aims-internal-audit-checklist.md` | Internal Audit | 2026-04-24 |
| E-9.2-003 | Audit reports | `aims-internal-audit-report-template.md` | Internal Audit | 2026-04-24 |
| E-9.2-004 | Auditor competence records | HR records | HR | 2026-04-24 |

### 9.3 Management Review

| Evidence ID | Description | Location | Owner | Last Updated |
|-------------|-------------|----------|-------|--------------|
| E-9.3-001 | Management review agenda | `aims-management-review-agenda.md` | Governance Office | 2026-04-24 |
| E-9.3-002 | Management review minutes | `aims-management-review-minutes-template.md` | Governance Office | 2026-04-24 |
| E-9.3-003 | Action item tracking | Action tracker | Governance Office | 2026-04-24 |

---

## Clause 10: Improvement

### 10.1 Nonconformity and Corrective Action

| Evidence ID | Description | Location | Owner | Last Updated |
|-------------|-------------|----------|-------|--------------|
| E-10.1-001 | Corrective action procedure | `aims-corrective-action-template.md` | Compliance Officer | 2026-04-24 |
| E-10.1-002 | Corrective action tracker | `aims-corrective-action-tracker.md` | Compliance Officer | 2026-04-24 |
| E-10.1-003 | Root cause analysis records | CAR files | Process Owners | 2026-04-24 |
| E-10.1-004 | Effectiveness verification records | CAR files | Internal Audit | 2026-04-24 |

### 10.2 Continual Improvement

| Evidence ID | Description | Location | Owner | Last Updated |
|-------------|-------------|----------|-------|--------------|
| E-10.2-001 | Improvement register | `aims-improvement-register.md` | CAIO | 2026-04-24 |
| E-10.2-002 | Improvement implementation records | Project records | CAIO | 2026-04-24 |
| E-10.2-003 | Innovation pipeline | `ai-opportunity-register.md` | CAIO | 2026-04-24 |

---

## Certification Body Audit Evidence

### Stage 1 Audit (Documentation Review)

| Evidence Package | Contents | Prepared By | Status |
|-----------------|----------|-------------|--------|
| Stage 1 — AIMS Documentation | All policies, procedures, plans | Governance Office | ☐ Ready |
| Stage 1 — Context and Scope | Scope statement, context analysis | CAIO | ☐ Ready |
| Stage 1 — Risk Assessment | Risk register, treatment plans | Safety Officer | ☐ Ready |

### Stage 2 Audit (Implementation Evidence)

| Evidence Package | Contents | Prepared By | Status |
|-----------------|----------|-------------|--------|
| Stage 2 — Operational Evidence | Deployment logs, monitoring records, test results | MLOps Lead | ☐ Ready |
| Stage 2 — Interview Schedule | Staff interviews by role | Governance Office | ☐ Ready |
| Stage 2 — Live Demonstration | Agent operation, safety features, audit trails | Technical Owner | ☐ Ready |

---

## Evidence Maintenance

| Activity | Frequency | Owner |
|----------|-----------|-------|
| Evidence inventory update | Monthly | Governance Office |
| Evidence completeness check | Quarterly (pre-management review) | Compliance Officer |
| Evidence accessibility audit | Annually (pre-certification audit) | Internal Audit |
| Evidence retention verification | Annually | Governance Office |

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-24 | ProtoLabs AI Governance Office | Initial evaluation repository index |

---

## See Also

- `governance/07-enterprise-implementation/iso-42001-certification/aims-internal-audit-checklist.md` — Audit checklist with evidence requirements
- `docs/iso-42001-gap-analysis.md` — Gap analysis
- `docs/governance-by-stage-framework.md` — Governance framework
