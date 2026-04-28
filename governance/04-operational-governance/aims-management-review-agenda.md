# AIMS Management Review Agenda

> **Document Type:** Operational Governance — ISO 42001 Compliance
> **Version:** 1.0
> **Effective Date:** 2026-04-28
> **Owner:** Chief AI Officer (CAIO)
> **Approved By:** AI Governance Council
> **Review Cycle:** Quarterly (aligned with governance report)

---

## Purpose

This document defines the agenda for ISO 42001 Clause 9.3 management reviews. Management reviews are the mechanism by which top management evaluates AIMS suitability, adequacy, and effectiveness. Without a structured agenda, management reviews become ad-hoc discussions rather than evidence-based evaluations.

## Regulatory Basis

- **ISO/IEC 42001 Clause 9.3** — Management review (inputs, outputs, frequency)
- **NIST AI RMF GV-5.1** — Ongoing monitoring and review

---

## Meeting Metadata

| Field | Value |
|-------|-------|
| **Meeting Title** | AIMS Management Review |
| **Date** | [FILL IN] |
| **Attendees** | CAIO, Head of Engineering, DPO, Legal Counsel, Head of Internal Audit, Safety Officer |
| **Facilitator** | CAIO |
| **Duration** | 120 minutes |

---

## Standing Agenda

### Part 1: Inputs (ISO 42001 Cl. 9.3.2) — 75 minutes

| # | Agenda Item | ISO Clause | Presenter | Duration | Input Document |
|---|------------|-----------|-----------|----------|----------------|
| 1 | Status of actions from previous management reviews | 9.3.2(a) | CAIO | 10 min | Previous meeting minutes |
| 2 | Changes in external/internal issues affecting AIMS | 9.3.2(b) | Legal Counsel | 10 min | `regulatory-change-monitor.md` |
| 3 | AIMS performance and effectiveness | 9.3.2(c) | CAIO | 15 min | `aims-objectives-and-kpis.md` |
| 3a | — KPI dashboard review | | | | Quarterly governance report |
| 3b | — Nonconformity and corrective action status | | | | `aims-corrective-action-template.md` |
| 3c | — Monitoring and measurement results | | | | Eval results, drift detection reports |
| 3d | — Audit results (internal) | | | | `aims-internal-audit-plan.md` |
| 4 | Adequacy of resources | 9.3.2(d) | Head of Engineering | 10 min | Resource allocation report |
| 5 | Effectiveness of actions to address risks and opportunities | 9.3.2(e) | Safety Officer | 10 min | Risk register, opportunity register |
| 6 | Opportunities for improvement | 9.3.2(f) | Head of Internal Audit | 10 min | `aims-improvement-register.md` |
| 7 | Stakeholder feedback and complaints | 9.3.2(g) | VP Product | 10 min | Client feedback summary |

### Part 2: Outputs (ISO 42001 Cl. 9.3.3) — 45 minutes

| # | Output Decision | Owner | Deadline |
|---|----------------|-------|----------|
| 1 | Decisions on AIMS improvement opportunities | CAIO | Per improvement register |
| 2 | Decisions on resource needs | CAIO | Next budget cycle |
| 3 | Decisions on AIMS changes (if any) | Council | Per change impact |

---

## Meeting Minutes Template

```yaml
management_review:
  review_id: "MR-2026-Q2"
  date: "YYYY-MM-DD"
  attendees:
    - name: "[Name]"
      role: "CAIO"
      present: true
    # ... additional attendees

  inputs_reviewed:
    - item: "Previous action items"
      status: "[X/Y completed]"
      notes: "[Summary]"
    - item: "KPI dashboard"
      overall_health: "green | amber | red"
      notes: "[Summary]"
    - item: "Nonconformities"
      open_count: 0
      notes: "[Summary]"
    - item: "Audit results"
      major_findings: 0
      minor_findings: 0
      notes: "[Summary]"

  outputs:
    decisions:
      - "[Decision 1]"
      - "[Decision 2]"
    resource_requests:
      - "[Resource request 1]"
    improvement_actions:
      - action: "[Action]"
        owner: "[Name]"
        deadline: "YYYY-MM-DD"

  next_review_date: "YYYY-MM-DD"
```

---

## Cross-References

| Document | Relationship |
|----------|-------------|
| [AIMS Objectives and KPIs](../06-executive/aims-objectives-and-kpis.md) | KPI inputs to review |
| [AIMS Internal Audit Plan](aims-internal-audit-plan.md) | Audit results input to review |
| [AIMS Corrective Action Template](aims-corrective-action-template.md) | Nonconformity status input |
| [AIMS Improvement Register](aims-improvement-register.md) | Improvement opportunities input |
| [Quarterly Governance Report](../06-executive/quarterly-governance-report.md) | Report informed by review outputs |

---

*This document is version-controlled and auditable.*
