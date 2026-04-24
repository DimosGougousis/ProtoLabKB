# AIMS Management Review Agenda — ISO/IEC 42001 Clause 9.3

> **Purpose:** Defines the quarterly management review agenda for the ProtoLabs AI Management System, ensuring ISO/IEC 42001 Clause 9.3 compliance and effective governance oversight.

**Version:** 1.0  
**Last Updated:** 2026-04-24  
**Owner:** Chief AI Officer (AIMS Owner)  
**Review Cycle:** Quarterly  
**Next Review:** 2026-07-24  

---

## Meeting Logistics

| Attribute | Value |
|-----------|-------|
| **Frequency** | Quarterly (last Friday of quarter) |
| **Duration** | 3 hours |
| **Chair** | Chief AI Officer (AIMS Owner) |
| **Required Attendees** | Policy Owner, Technical Owner, Safety Officer, Compliance Officer, DPO |
| **Optional Attendees** | Operational Owners, ML Lead, MLOps Lead, Internal Audit |
| **Location** | Boardroom / Virtual |
| **Minutes** | Governance Office |

---

## Standard Agenda

### Opening (15 minutes)

| Item | Description | Owner |
|------|-------------|-------|
| 1.1 | Roll call and attendance | Governance Office |
| 1.2 | Review and approve previous minutes | Chair |
| 1.3 | Review action items from previous meeting | Governance Office |
| 1.4 | Agenda confirmation | Chair |

### Part 1: AIMS Performance (45 minutes)

| Item | Description | Evidence | Owner |
|------|-------------|----------|-------|
| 1.1 | Certification progress review | Gap closure %, audit readiness | CAIO |
| 1.2 | AI objectives and KPIs status | `aims-objectives-and-kpis.md` dashboard | CAIO |
| 1.3 | DFM agent accuracy trends | `dfm-accuracy-eval-suite.yaml` quarterly results | Technical Owner |
| 1.4 | Safety performance | Incident count, kill switch tests, guardrail violations | Safety Officer |
| 1.5 | Security posture | Adversarial test results, vulnerability status | Security Engineer |
| 1.6 | Client feedback summary | NPS, CSAT, complaints, compliments | Policy Owner |

### Part 2: Risk and Opportunity Review (30 minutes)

| Item | Description | Evidence | Owner |
|------|-------------|----------|-------|
| 2.1 | Risk register review | Open risks, new risks, closed risks | Compliance Officer |
| 2.2 | Risk treatment effectiveness | WP01-WP04 performance metrics | Technical Owner |
| 2.3 | Residual risk acceptance | Risks requiring acceptance decisions | Policy Owner |
| 2.4 | Opportunity register review | `ai-opportunity-register.md` | CAIO |
| 2.5 | Emerging risks | New technologies, regulations, threats | Compliance Officer |

### Part 3: Audit and Compliance (30 minutes)

| Item | Description | Evidence | Owner |
|------|-------------|----------|-------|
| 3.1 | Internal audit results | `aims-internal-audit-report-template.md` | Internal Audit |
| 3.2 | Corrective action status | `aims-corrective-action-tracker.md` | Process Owners |
| 3.3 | Certification body interactions | Stage 1/2 audit status, findings | CAIO |
| 3.4 | Regulatory updates | EU AI Act, NIST updates, state laws | Compliance Officer |
| 3.5 | Compliance metrics | Framework alignment scores | Compliance Officer |

### Part 4: Operational Review (30 minutes)

| Item | Description | Evidence | Owner |
|------|-------------|----------|-------|
| 4.1 | Agent deployment/retirement status | Agent registry updates | Technical Owner |
| 4.2 | Tier classification changes | `agent-tier-classification.yaml` changes | Safety Officer |
| 4.3 | Infrastructure and resource status | `aims-infrastructure-inventory.md` | Technical Owner |
| 4.4 | Training and competence status | `aims-competence-matrix.md` | HR / CAIO |
| 4.5 | Vendor and third-party status | Vendor risk assessments | Procurement |

### Part 5: Improvement and Strategic (20 minutes)

| Item | Description | Evidence | Owner |
|------|-------------|----------|-------|
| 5.1 | Improvement register review | `aims-improvement-register.md` | CAIO |
| 5.2 | Nonconformity trends | Incident patterns, root cause themes | Safety Officer |
| 5.3 | Best practices and innovations | Industry trends, new tools, techniques | CAIO |
| 5.4 | Strategic initiatives | New agent proposals, capability expansion | Policy Owner |
| 5.5 | Budget and resource needs | AIMS budget status, resource gaps | CAIO |

### Closing (10 minutes)

| Item | Description | Owner |
|------|-------------|-------|
| 6.1 | New action items assignment | Chair |
| 6.2 | Next meeting scheduling | Governance Office |
| 6.3 | Any other business | All |
| 6.4 | Meeting close | Chair |

---

## Required Inputs

The following documents must be distributed to attendees at least 5 business days before the meeting:

| Input | Source | Due Date |
|-------|--------|----------|
| Previous meeting minutes | Governance Office | D-5 |
| Action item status | Governance Office | D-5 |
| AIMS KPI dashboard | MLOps | D-5 |
| Risk register update | Compliance Officer | D-5 |
| Internal audit report (if applicable) | Internal Audit | D-5 |
| Incident summary | Safety Officer | D-5 |
| Budget status | Finance | D-5 |

---

## Required Outputs

The following must be produced within 5 business days after the meeting:

| Output | Owner | Due Date |
|--------|-------|----------|
| Management review minutes | Governance Office | D+5 |
| Updated action item tracker | Governance Office | D+5 |
| Updated risk register (if changed) | Compliance Officer | D+5 |
| Updated improvement register (if changed) | CAIO | D+5 |
| Board summary (if required) | CAIO | D+5 |

---

## Special Agenda Items

### Pre-Certification Review (Q2-Q3 2026)

Additional agenda items for reviews leading to certification:

| Item | Description | Evidence |
|------|-------------|----------|
| Gap closure verification | Review all gaps from `docs/iso-42001-gap-analysis.md` | Gap tracker |
| Internal audit readiness | Confirm internal audit completed, findings closed | Audit report |
| Certification body selection | Review TÜV SÜD / BSI proposals | Procurement evaluation |
| Stage 1 audit preparation | Review documentation package | Document checklist |
| Stage 2 audit preparation | Review evidence readiness | Evidence tracker |

### Post-Certification Review (Q1 2027 onwards)

| Item | Description | Evidence |
|------|-------------|----------|
| Certification maintenance | Surveillance audit schedule, preparation | Certification records |
| Continuous improvement focus | Post-certification improvement priorities | Improvement register |
| Market differentiation | Client feedback on certification value | Sales feedback |

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-24 | ProtoLabs AI Governance Office | Initial management review agenda |

---

## See Also

- `governance/07-enterprise-implementation/iso-42001-certification/aims-management-review-minutes-template.md` — Minutes template
- `governance/06-executive/quarterly-governance-report.md` — Quarterly board report
- `docs/iso-42001-gap-analysis.md` — Gap analysis (Clause 9.3)
