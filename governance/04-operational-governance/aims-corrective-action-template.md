# AIMS Corrective Action Template (8D)

> **Document Type:** Operational Governance — Nonconformity Management
> **Version:** 1.0
> **Effective Date:** 2026-04-28
> **Owner:** Head of Internal Audit
> **Approved By:** AI Governance Council
> **Review Cycle:** Annual

---

## Purpose

This template provides a structured root cause analysis and corrective action format for AIMS nonconformities, audit findings, and Sev1/Sev2 incidents. The 8D (Eight Disciplines) methodology ensures that corrective actions address root causes, not symptoms.

## Regulatory Basis

- **ISO/IEC 42001 Clause 10.1** — Nonconformity and corrective action
- **NIST AI RMF MG-2.1** — Incident response

---

## Corrective Action Record

```yaml
corrective_action:
  ca_id: "CA-2026-001"
  title: "[FILL IN: Brief description]"
  source: "internal_audit | incident | regulatory | management_review"
  source_ref: "[FILL IN: Audit report ID, incident ID, or finding reference]"
  severity: "major_nonconformity | minor_nonconformity | observation"
  opened_date: "YYYY-MM-DD"
  owner: "[FILL IN: Name, Role]"
  due_date: "YYYY-MM-DD"
  status: "open | in_progress | verified | closed"

  # D1: Team
  team:
    - name: "[Name]"
      role: "[Role]"
    - name: "[Name]"
      role: "[Role]"

  # D2: Problem Description
  problem_description: >
    [FILL IN: What happened? When? Where? What was the impact?
    Be specific — include evidence references.]

  # D3: Interim Containment
  interim_containment:
    actions:
      - "[FILL IN: What immediate action was taken to contain the problem?]"
    effectiveness: "[FILL IN: Did containment work? Evidence.]"
    implemented_date: "YYYY-MM-DD"

  # D4: Root Cause Analysis
  root_cause_analysis:
    method: "5-why | fishbone | fault_tree | other"
    root_causes:
      - cause: "[FILL IN: Root cause 1]"
        evidence: "[FILL IN: Evidence supporting this cause]"
      - cause: "[FILL IN: Root cause 2]"
        evidence: "[FILL IN: Evidence supporting this cause]"

  # D5: Permanent Corrective Actions
  corrective_actions:
    - action: "[FILL IN: What will permanently fix the root cause?]"
      owner: "[Name]"
      deadline: "YYYY-MM-DD"
      status: "planned | in_progress | complete"
    - action: "[FILL IN: Additional corrective action if needed]"
      owner: "[Name]"
      deadline: "YYYY-MM-DD"
      status: "planned | in_progress | complete"

  # D6: Implementation and Validation
  validation:
    method: "[FILL IN: How will you verify the fix works?]"
    evidence: "[FILL IN: Evidence of effectiveness]"
    validated_date: "YYYY-MM-DD"
    validated_by: "[Name]"

  # D7: Prevention of Recurrence
  systemic_improvements:
    - "[FILL IN: What process change prevents this from happening again?]"
    - "[FILL IN: What monitoring was added?]"

  # D8: Closure
  closure:
    closed_date: "YYYY-MM-DD"
    closed_by: "[Name]"
    lessons_learned: "[FILL IN: What did we learn?]"
    framework_updates:
      - "[FILL IN: Any governance framework changes made as a result]"
```

---

## Effectiveness Verification

After corrective action closure, verify effectiveness:

| Verification Timing | Activity | Owner |
|--------------------|----------|-------|
| 30 days post-closure | Check that nonconformity has not recurred | Internal Audit |
| 90 days post-closure | Verify systemic improvements are operating | Internal Audit |
| Next internal audit | Include in audit scope | Lead Auditor |

---

## Cross-References

| Document | Relationship |
|----------|-------------|
| [AIMS Internal Audit Plan](aims-internal-audit-plan.md) | Audit findings use this template |
| [Incident Severity Classification](incident-severity-classification.md) | Sev1/Sev2 incidents use this template |
| [AIMS Improvement Register](aims-improvement-register.md) | Systemic improvements tracked here |
| [Governance Framework Changelog](../05-cross-cutting/governance-framework-changelog.md) | Framework updates logged here |

---

*This template is version-controlled and auditable.*
