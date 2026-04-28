# AIMS Internal Audit Plan

> **Document Type:** Operational Governance — ISO 42001 Compliance
> **Version:** 1.0
> **Effective Date:** 2026-04-28
> **Owner:** Head of Internal Audit
> **Approved By:** AI Governance Council
> **Review Cycle:** Annual
> **Next Review:** 2027-04-28

---

## Purpose

This plan establishes the internal audit program for ProtoLabs' AI Management System (AIMS) as required by ISO/IEC 42001 Clause 9.2. Internal audits verify that the AIMS conforms to ISO 42001 requirements, ProtoLabs' own governance policies, and applicable regulations. Without this plan, ProtoLabs cannot achieve or maintain ISO 42001 certification.

## When to Use

- When scheduling annual audit activities
- When preparing for external ISO 42001 certification audit
- When investigating governance non-conformities
- When the Governance Council requests assurance on specific controls

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **Head of Internal Audit** | **Accountable** — owns the audit program, schedules audits, reports findings |
| **Internal Auditors** | **Responsible** — conduct audits per this plan |
| **CAIO** | **Approver** — approves audit scope and findings |
| **Governance Council** | **Recipient** — receives audit reports and approves corrective actions |
| **Process Owners** | **Cooperative** — provide evidence and implement corrective actions |

## Regulatory Basis

- **ISO/IEC 42001 Clause 9.2** — Internal audit requirements
- **ISO/IEC 42001 Clause 9.2.2** — Internal audit program
- **ISO/IEC 42001 Clause 10.1** — Nonconformity and corrective action
- **NIST AI RMF GV-5.1** — Ongoing monitoring and review

---

## 1. Audit Program Overview

### 1.1 Audit Frequency

| Audit Type | Frequency | Scope |
|-----------|-----------|-------|
| **Full AIMS Audit** | Annual | All ISO 42001 clauses + Annex A controls |
| **Pillar Audit** | Semi-annual (rotating) | One governance pillar per cycle |
| **Agent-Specific Audit** | Per deployment + annual | Individual agent compliance |
| **Triggered Audit** | As needed | Post-incident, regulatory change, or Council directive |

### 1.2 Annual Audit Calendar (2026-2027)

| Quarter | Audit Focus | ISO 42001 Clauses | Lead Auditor |
|---------|------------|-------------------|-------------|
| **Q2 2026** | Full AIMS baseline audit (pre-certification) | Clauses 4-10, Annex A | [Name] |
| **Q3 2026** | Pillar audit: Discovery + Development Governance | Clauses 6.1, 8.1, 8.4 | [Name] |
| **Q4 2026** | Pillar audit: Runtime + Operational Governance | Clauses 8.1, 9.1, 10.1 | [Name] |
| **Q1 2027** | Pre-certification readiness audit | All clauses (gap closure verification) | [Name] |
| **Q2 2027** | Post-certification surveillance audit | Focus on findings from Q2 2026 | [Name] |

---

## 2. Audit Scope and Criteria

### 2.1 Full AIMS Audit Scope

| ISO 42001 Clause | Audit Criteria | Key Evidence |
|------------------|---------------|-------------|
| **4.1** Context of the Organisation | Internal/external issues documented | `ml-lifecycle-canvas.md`, `regulatory-reference-index.md` |
| **4.2** Interested Parties | Stakeholder needs identified | `stakeholder-value-map.md` |
| **4.3** AIMS Scope | Scope boundaries defined | `agent-tier-classification.yaml` |
| **5.1** Leadership | Board-level AI policy exists | `governance-charter.md`, `ai-governance-policy.md` |
| **5.2** AI Policy | Policy established and communicated | `ai-governance-policy.md` |
| **5.3** Roles and Responsibilities | Roles defined and assigned | `governance-roles-raci.md`, `ai-governance-council-charter.md` |
| **6.1** Risk Assessment | Risk methodology and register maintained | `risk-management-plan.md`, `ai-risk-appetite-framework.md` |
| **6.2** AI Objectives | SMART objectives established | `aims-objectives-and-kpis.md` |
| **7.1** Resources | Personnel, infrastructure, budget allocated | `governance-roles-raci.md` |
| **7.2** Competence | Competence requirements defined and met | `aims-competence-matrix.md` |
| **7.3** Awareness | Awareness campaigns conducted | Evidence of training delivery |
| **7.4** Communication | Internal/external communication plans | `aims-communication-plan.md` |
| **7.5** Documented Information | Document control in place | Version-controlled artifacts |
| **8.1** Operational Control | Development/deployment processes defined | `product-development-lifecycle.md`, `pre-deployment-gate.yaml` |
| **8.2** Risk Assessment (per system) | Per-agent risk assessments complete | Per-agent risk registers |
| **8.4** Lifecycle Processes | Requirements → design → eval → deploy → monitor | `eval-driven-development.md`, `model-card.md` |
| **9.1** Monitoring | Monitoring plan and KPIs defined | `continuous-monitoring-plan.md` |
| **9.2** Internal Audit | This plan exists and is executed | This document |
| **9.3** Management Review | Management review conducted | `aims-management-review-agenda.md` |
| **10.1** Nonconformity | Corrective action process defined | `aims-corrective-action-template.md` |
| **10.2** Continual Improvement | Improvement register maintained | `aims-improvement-register.md` |

### 2.2 Annex A Controls Audit

| Control Category | Key Controls | Evidence |
|-----------------|-------------|----------|
| **A.2 AI Risk Assessment** | Risk classification, treatment plans | `agent-tier-classification.yaml`, risk registers |
| **A.3 AI System Impact Assessment** | Impact assessment per agent | `ai-ethics-impact-assessment.md` |
| **A.4 AI System Lifecycle** | Development, deployment, monitoring, retirement | `product-development-lifecycle.md` |
| **A.5 Data for AI Systems** | Data quality, provenance, governance | `source-grounding-data-contract.yaml` |
| **A.6 Information for Interested Parties** | Transparency, documentation | `model-card.md`, `transparency-controls.md` |
| **A.7 Human Oversight** | Oversight mechanisms, kill switches | `human-in-the-loop-patterns.md` |
| **A.8 Third-Party AI** | Vendor controls, DPAs | `third-party-ai-vendor-controls.md` |

---

## 3. Audit Process

### 3.1 Audit Lifecycle

```
PLAN → PREPARE → EXECUTE → REPORT → FOLLOW-UP → CLOSE
  │        │         │         │          │         │
  v        v         v         v          v         v
Scope   Evidence  Interviews  Findings  Corrective  Verify
& plan  review    & testing   & gaps    actions     effectiveness
```

### 3.2 Audit Steps

| Step | Activity | Duration | Output |
|------|----------|----------|--------|
| 1 | Define scope and criteria | 1 week | Audit plan |
| 2 | Request evidence from process owners | 2 weeks | Evidence package |
| 3 | Review evidence against criteria | 1 week | Preliminary findings |
| 4 | Conduct interviews and walkthroughs | 1 week | Interview notes |
| 5 | Draft audit report with findings | 1 week | Draft report |
| 6 | Review findings with process owners | 1 week | Agreed findings |
| 7 | Finalize audit report | 3 days | Final report |
| 8 | Present to Governance Council | Next meeting | Council decision |
| 9 | Track corrective actions | Ongoing | Corrective action tracker |
| 10 | Verify corrective action effectiveness | Per SLA | Closure evidence |

---

## 4. Audit Findings Classification

| Finding Type | Definition | Required Action | SLA |
|-------------|-----------|-----------------|-----|
| **Major Nonconformity** | Systematic failure or absence of required control | Immediate corrective action; may block certification | 30 days |
| **Minor Nonconformity** | Isolated failure or incomplete implementation | Corrective action required | 60 days |
| **Observation** | Opportunity for improvement (not a nonconformity) | Recommended action | 90 days |
| **Positive Finding** | Exemplary practice worth highlighting | Document and share | N/A |

---

## 5. Auditor Competence Requirements

| Requirement | Detail |
|-------------|--------|
| **Independence** | Auditors must not audit their own work or processes they manage |
| **ISO 42001 knowledge** | Lead auditors must have completed ISO 42001 awareness training |
| **AI domain knowledge** | At least one auditor must understand AI/ML systems |
| **Audit methodology** | Lead auditors trained in ISO 19011 (auditing management systems) |

---

## 6. Audit Reporting

### 6.1 Audit Report Contents

Every audit report must include:
1. Audit scope, criteria, and dates
2. Audit team composition
3. Summary of findings (major, minor, observations)
4. Detailed findings with evidence references
5. Positive findings
6. Recommendations
7. Corrective action requirements with deadlines

### 6.2 Distribution

| Recipient | Report Type |
|-----------|------------|
| Governance Council | Full report |
| CAIO | Full report |
| Board of Directors | Executive summary (major findings only) |
| Process Owners | Findings relevant to their area |
| External auditor (during certification) | Full report on request |

---

## 7. Pre-Certification Readiness Checklist

Before external ISO 42001 certification audit:

| Item | Status | Evidence |
|------|--------|----------|
| All major nonconformities from internal audits closed | | |
| AIMS documented and accessible | | |
| Management review conducted at least once | | |
| Internal audit conducted at least once (full scope) | | |
| Corrective action process operational | | |
| Improvement register maintained | | |
| All required documented information available | | |

---

## Cross-References

| Document | Relationship |
|----------|-------------|
| [ISO 42001 Gap Analysis](../../docs/iso-42001-gap-analysis.md) | Gap analysis identifies audit focus areas |
| [AIMS Corrective Action Template](aims-corrective-action-template.md) | Template for audit finding corrective actions |
| [AIMS Management Review Agenda](aims-management-review-agenda.md) | Audit results feed into management review |
| [Governance by Stage Framework](../../docs/governance-by-stage-framework.md) | Stage-specific governance evidence |
| [AI Governance Policy](../ai-governance-policy.md) | Parent policy |

---

*This plan is version-controlled and auditable. Unauthorized modifications void governance compliance claims.*
