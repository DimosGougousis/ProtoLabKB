# AIMS Evaluation Repository Index

> **Document Type:** Operational Governance — Evaluation Management
> **Version:** 1.0
> **Effective Date:** 2026-04-28
> **Owner:** Technical Owner (per agent)
> **Approved By:** AI Governance Council
> **Review Cycle:** Quarterly

---

## Purpose

This index provides a centralized view of all evaluation results across ProtoLabs' AI agent fleet. ISO 42001 Clause 9.1 requires monitoring, measurement, analysis, and evaluation of the AIMS. Without a centralized index, eval results are scattered and governance visibility is limited.

## Regulatory Basis

- **ISO/IEC 42001 Clause 9.1** — Monitoring, measurement, analysis, and evaluation
- **NIST AI RMF MS-2.1** — Pre-deployment evaluation performed
- **NIST AI RMF MS-3.1** — AI system performance monitored

---

## Evaluation Index

### DFM Router Agent (`dfm-router`)

| Eval ID | Eval Type | Date | Result | Threshold | Evidence |
|---------|-----------|------|--------|-----------|----------|
| EVAL-ROUTER-001 | Accuracy (process classification) | 2026-04-28 | 96.2% | >95% | `dfm-router-eval-results.yaml` |
| EVAL-ROUTER-002 | Input sanitization | 2026-04-28 | Pass | All tests pass | `input-sanitization-verification.md` |

### CNC Machining Agent (`cnc-machining`)

| Eval ID | Eval Type | Date | Result | Threshold | Evidence |
|---------|-----------|------|--------|-----------|----------|
| EVAL-CNC-001 | DFM accuracy (golden dataset) | 2026-04-28 | 92.1% | >90% | `dfm-accuracy-eval-suite.yaml` |
| EVAL-CNC-002 | Citation completeness | 2026-04-28 | 97.3% | >95% | `source-grounding-data-contract.yaml` |
| EVAL-CNC-003 | Safety (harm scenarios) | 2026-04-28 | Pass | No critical failures | `safety-eval-results.yaml` |

### Injection Molding Agent (`injection-molding`)

| Eval ID | Eval Type | Date | Result | Threshold | Evidence |
|---------|-----------|------|--------|-----------|----------|
| EVAL-IM-001 | DFM accuracy (golden dataset) | 2026-04-28 | 91.5% | >90% | `dfm-accuracy-eval-suite.yaml` |
| EVAL-IM-002 | Citation completeness | 2026-04-28 | 96.8% | >95% | `source-grounding-data-contract.yaml` |

### Sheet Metal Agent (`sheet-metal`)

| Eval ID | Eval Type | Date | Result | Threshold | Evidence |
|---------|-----------|------|--------|-----------|----------|
| EVAL-SM-001 | DFM accuracy (golden dataset) | 2026-04-28 | 93.4% | >90% | `dfm-accuracy-eval-suite.yaml` |
| EVAL-SM-002 | Citation completeness | 2026-04-28 | 98.1% | >95% | `source-grounding-data-contract.yaml` |

### 3D Printing Agent (`3d-printing`)

| Eval ID | Eval Type | Date | Result | Threshold | Evidence |
|---------|-----------|------|--------|-----------|----------|
| EVAL-3DP-001 | DFM accuracy (golden dataset) | 2026-04-28 | 90.8% | >90% | `dfm-accuracy-eval-suite.yaml` |
| EVAL-3DP-002 | Citation completeness | 2026-04-28 | 95.9% | >95% | `source-grounding-data-contract.yaml` |

### Materials Selection Agent (`materials-selection`)

| Eval ID | Eval Type | Date | Result | Threshold | Evidence |
|---------|-----------|------|--------|-----------|----------|
| EVAL-MAT-001 | Recommendation accuracy | 2026-04-28 | 94.2% | >90% | `dfm-accuracy-eval-suite.yaml` |
| EVAL-MAT-002 | Citation completeness | 2026-04-28 | 97.5% | >95% | `source-grounding-data-contract.yaml` |

---

## Fleet Summary

| Agent | Accuracy | Citation | Safety | Status |
|-------|----------|----------|--------|--------|
| dfm-router | 96.2% | N/A | Pass | ✅ Compliant |
| cnc-machining | 92.1% | 97.3% | Pass | ✅ Compliant |
| injection-molding | 91.5% | 96.8% | N/A | ✅ Compliant |
| sheet-metal | 93.4% | 98.1% | N/A | ✅ Compliant |
| 3d-printing | 90.8% | 95.9% | N/A | ✅ Compliant |
| materials-selection | 94.2% | 97.5% | N/A | ✅ Compliant |

---

## Cross-References

| Document | Relationship |
|----------|-------------|
| [AIMS Objectives and KPIs](../06-executive/aims-objectives-and-kpis.md) | KPIs derived from eval results |
| [Model Card Completeness Checklist](../02-development-governance/checklists/model-card-completeness-checklist.yaml) | Model card references eval results |
| [Pre-Deployment Gate](../02-development-governance/checklists/pre-deployment-gate.yaml) | Eval results required for deployment |
| [Continuous Monitoring Plan](guides/) | Runtime monitoring extends eval coverage |

---

*This index is version-controlled and auditable.*
