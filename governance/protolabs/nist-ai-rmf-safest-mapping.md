# SAFEST to NIST AI RMF Crosswalk

> **Purpose:** Mapping between the DNB SAFEST methodology (retained as internal governance rubric) and the NIST AI RMF Four Functions and Seven Characteristics. Enables organizations using SAFEST to demonstrate NIST AI RMF alignment and vice versa.

**Version:** 1.0  
**Last Updated:** 2026-04-23  
**Owner:** ProtoLabs AI Governance Office  
**Review Cycle:** Quarterly

---

## Executive Summary

This document provides a bidirectional mapping between two AI governance methodologies:

| Methodology | Origin | Structure | Use Case |
|-------------|--------|-----------|----------|
| **SAFEST** | De Nederlandsche Bank (DNB) | Six Pillars (Soundness, Accountability, Fairness, Ethics, Skills, Transparency) | Internal governance rubric, supervisory reporting |
| **NIST AI RMF** | US National Institute of Standards and Technology | Four Functions (Govern, Map, Measure, Manage) + Seven Characteristics | Risk management framework, international standard |

**Key Insight:** SAFEST and NIST AI RMF are complementary. SAFEST provides a organizational maturity lens; NIST AI RMF provides a risk management lifecycle. Together they provide comprehensive coverage.

---

## SAFEST → NIST AI RMF Mapping

### SAFEST Pillar S — Soundness

> *"Technically sound, validated, resilient"*

| SAFEST Element | NIST AI RMF Mapping | Coverage |
|----------------|---------------------|----------|
| Technical validation | MEASURE Function (MS-1, MS-2) | 🟢 Full |
| Model accuracy | Characteristic: Valid and Reliable | 🟢 Full |
| Resilience testing | Characteristic: Secure and Resilient | 🟢 Full |
| Performance monitoring | MEASURE Function (MS-3) | 🟢 Full |
| Drift detection | MANAGE Function (MG-3) | 🟢 Full |

**NIST AI RMF Coverage:** Soundness maps primarily to the **MEASURE** function and the **Valid and Reliable** + **Secure and Resilient** characteristics.

---

### SAFEST Pillar A — Accountability

> *"Clear ownership, roles, escalation"*

| SAFEST Element | NIST AI RMF Mapping | Coverage |
|----------------|---------------------|----------|
| Clear ownership | GOVERN Function (GV-1.2) | 🟢 Full |
| Defined roles | GOVERN Function (GV-1.2) | 🟢 Full |
| Escalation procedures | MANAGE Function (MG-2) | 🟢 Full |
| Audit trails | GOVERN Function (GV-7.1) | 🟢 Full |
| Decision rights | GOVERN Function (GV-4) | 🟢 Full |

**NIST AI RMF Coverage:** Accountability maps primarily to the **GOVERN** function and the **Accountable and Transparent** characteristic.

---

### SAFEST Pillar F — Fairness

> *"No discrimination; bias identified and mitigated"*

| SAFEST Element | NIST AI RMF Mapping | Coverage |
|----------------|---------------------|----------|
| Bias identification | MAP Function (MP-3) | 🟢 Full |
| Bias mitigation | MANAGE Function (MG-1) | 🟢 Full |
| Fairness testing | MEASURE Function (MS-2) | 🟢 Full |
| Demographic parity | Characteristic: Fair with Harmful Bias Managed | 🟢 Full |
| Disparate impact analysis | Characteristic: Fair with Harmful Bias Managed | 🟢 Full |

**NIST AI RMF Coverage:** Fairness maps primarily to the **MAP** and **MEASURE** functions and the **Fair with Harmful Bias Managed** characteristic.

---

### SAFEST Pillar E — Ethics

> *"Aligned with values & societal norms"*

| SAFEST Element | NIST AI RMF Mapping | Coverage |
|----------------|---------------------|----------|
| Ethical guidelines | GOVERN Function (GV-1) | 🟡 Partial |
| Value alignment | MAP Function (MP-3.4) — Societal impacts | 🟡 Partial |
| Ethical review | GOVERN Function (GV-2) | 🟡 Partial |
| Stakeholder consultation | GOVERN Function (GV-3) | 🟢 Full |

**NIST AI RMF Coverage:** Ethics is distributed across **GOVERN** and **MAP** functions. NIST AI RMF treats ethics as a cross-cutting concern rather than a standalone pillar.

**Gap Note:** Organizations may want to supplement NIST AI RMF with explicit ethical review processes (see `../01-discovery-governance/templates/ethical-use-policy.md`).

---

### SAFEST Pillar S — Skills

> *"Sufficient AI literacy"*

| SAFEST Element | NIST AI RMF Mapping | Coverage |
|----------------|---------------------|----------|
| AI literacy | GOVERN Function (GV-2.1) | 🟢 Full |
| Training programs | GOVERN Function (GV-2.1) | 🟢 Full |
| Competency frameworks | GOVERN Function (GV-2) | 🟢 Full |
| Continuous learning | GOVERN Function (GV-5) | 🟢 Full |

**NIST AI RMF Coverage:** Skills maps primarily to the **GOVERN** function (GV-2: "Risk Management Culture" and GV-3: "Workforce Diversity & Inclusion").

---

### SAFEST Pillar T — Transparency

> *"Explainable, auditable"*

| SAFEST Element | NIST AI RMF Mapping | Coverage |
|----------------|---------------------|----------|
| Explainability | Characteristic: Explainable and Interpretable | 🟢 Full |
| Auditability | GOVERN Function (GV-7.1) | 🟢 Full |
| Documentation | GOVERN Function (GV-7) | 🟢 Full |
| Disclosure to users | Characteristic: Accountable and Transparent | 🟢 Full |
| Model cards | GOVERN Function (GV-7.1) | 🟢 Full |

**NIST AI RMF Coverage:** Transparency maps to the **GOVERN** function and the **Accountable and Transparent** + **Explainable and Interpretable** characteristics.

---

## NIST AI RMF → SAFEST Mapping

### NIST AI RMF GOVERN Function → SAFEST

| NIST AI RMF Sub-Category | SAFEST Pillar(s) | Coverage |
|-------------------------|------------------|----------|
| GV-1: Policies & Procedures | A (Accountability), T (Transparency) | 🟢 Full |
| GV-2: Risk Management Culture | S (Skills), E (Ethics) | 🟢 Full |
| GV-3: Workforce Diversity | S (Skills), E (Ethics) | 🟢 Full |
| GV-4: Risk Tolerance | A (Accountability) | 🟢 Full |
| GV-5: Monitoring & Review | S (Soundness), T (Transparency) | 🟢 Full |
| GV-6: Third-Party Risk | A (Accountability) | 🟢 Full |
| GV-7: Documentation | T (Transparency) | 🟢 Full |

---

### NIST AI RMF MAP Function → SAFEST

| NIST AI RMF Sub-Category | SAFEST Pillar(s) | Coverage |
|-------------------------|------------------|----------|
| MP-1: Context of Use | E (Ethics) | 🟡 Partial |
| MP-2: Categorization | S (Soundness) | 🟢 Full |
| MP-3: Impacts | E (Ethics), F (Fairness) | 🟢 Full |
| MP-4: Likelihood & Severity | S (Soundness) | 🟢 Full |
| MP-5: Risk Tracking | A (Accountability) | 🟢 Full |

---

### NIST AI RMF MEASURE Function → SAFEST

| NIST AI RMF Sub-Category | SAFEST Pillar(s) | Coverage |
|-------------------------|------------------|----------|
| MS-1: Methods & Metrics | S (Soundness) | 🟢 Full |
| MS-2: Evaluation | S (Soundness), F (Fairness) | 🟢 Full |
| MS-3: Tracking | S (Soundness) | 🟢 Full |
| MS-4: Feedback | T (Transparency) | 🟢 Full |
| MS-5: Assurance | A (Accountability), T (Transparency) | 🟢 Full |

---

### NIST AI RMF MANAGE Function → SAFEST

| NIST AI RMF Sub-Category | SAFEST Pillar(s) | Coverage |
|-------------------------|------------------|----------|
| MG-1: Risk Response | A (Accountability), F (Fairness) | 🟢 Full |
| MG-2: Incident Response | A (Accountability), S (Soundness) | 🟢 Full |
| MG-3: Review & Update | S (Soundness), T (Transparency) | 🟢 Full |
| MG-4: Communication | T (Transparency), A (Accountability) | 🟢 Full |

---

## Seven Characteristics → SAFEST Mapping

| NIST AI RMF Characteristic | Primary SAFEST Pillar(s) | Secondary SAFEST Pillar(s) |
|---------------------------|---------------------------|---------------------------|
| **Valid and Reliable** | S — Soundness | T — Transparency |
| **Safe** | S — Soundness | A — Accountability |
| **Secure and Resilient** | S — Soundness | A — Accountability |
| **Accountable and Transparent** | A — Accountability, T — Transparency | E — Ethics |
| **Explainable and Interpretable** | T — Transparency | S — Soundness |
| **Privacy-Enhanced** | E — Ethics | A — Accountability |
| **Fair with Harmful Bias Managed** | F — Fairness | E — Ethics |

---

## Combined Coverage Matrix

```
                    ┌─────────────────────────────────────────────────────────┐
                    │              NIST AI RMF FUNCTIONS                       │
                    ├─────────────┬─────────────┬─────────────┬─────────────────┤
                    │   GOVERN    │    MAP      │   MEASURE   │     MANAGE      │
┌───────────────────┼─────────────┼─────────────┼─────────────┼─────────────────┤
│ S — Soundness     │      🟡     │      🟡     │      🟢     │       🟢        │
│ A — Accountability│     🟢     │      🟢     │      🟡     │       🟢        │
│ F — Fairness      │      🟡     │      🟢     │      🟢     │       🟢        │
│ E — Ethics        │      🟢     │      🟢     │      🟡     │       🟡        │
│ S — Skills        │      🟢     │      🟡     │      🟡     │       🟡        │
│ T — Transparency  │      🟢     │      🟡     │      🟢     │       🟢        │
└───────────────────┴─────────────┴─────────────┴─────────────┴─────────────────┘

Legend: 🟢 Full Coverage  🟡 Partial Coverage
```

---

## Implementation Guidance

### For Organizations Using SAFEST (Adding NIST AI RMF)

1. **Leverage existing SAFEST assessments** — Most SAFEST evidence can be reused for NIST AI RMF
2. **Focus on gaps** — Ethics in MAP function, Skills in MEASURE function
3. **Add Seven Characteristics assessment** — This is new in NIST AI RMF
4. **Update documentation** — Reference both frameworks in model cards and governance artifacts

### For Organizations Using NIST AI RMF (Adding SAFEST)

1. **Use SAFEST as maturity model** — SAFEST provides more granular organizational maturity criteria
2. **Leverage SAFEST for supervisory reporting** — If reporting to DNB or similar regulators
3. **Add explicit ethical review** — SAFEST's Ethics pillar provides more structure than NIST AI RMF
4. **Implement skills tracking** — SAFEST's Skills pillar provides detailed competency frameworks

---

## Artifact Mapping

| ProtoLabs Artifact | SAFEST Coverage | NIST AI RMF Coverage |
|-------------------|-----------------|---------------------|
| `dfm-accuracy-eval-suite.yaml` | S — Soundness | MEASURE Function, Valid and Reliable |
| `bias-and-fairness-evals.md` | F — Fairness | MEASURE Function, Fair with Harmful Bias Managed |
| `governance-roles-raci.md` | A — Accountability | GOVERN Function, Accountable and Transparent |
| `ethical-use-policy.md` | E — Ethics | GOVERN Function |
| `training-and-awareness-plan.md` | S — Skills | GOVERN Function |
| `transparency-controls.md` | T — Transparency | GOVERN Function, Accountable and Transparent |
| `red-teaming-ai-systems.md` | S — Soundness | MEASURE/MANAGE Functions, Safe, Secure and Resilient |
| `source-grounding-data-contract.yaml` | T — Transparency | GOVERN Function, Accountable and Transparent |
| `kill-switch-specification.md` | S — Soundness, A — Accountability | MANAGE Function, Safe |
| `audit-record-schema.yaml` | A — Accountability, T — Transparency | GOVERN Function, Accountable and Transparent |

---

## Summary: When to Use Which Framework

| Scenario | Recommended Framework | Rationale |
|----------|----------------------|-----------|
| US market entry | NIST AI RMF | US regulatory expectation |
| EU market entry | SAFEST + EU AI Act | DNB alignment, supervisory ready |
| International deployment | Both | Comprehensive coverage |
| Board reporting | SAFEST | Six-pillar structure resonates |
| Technical risk assessment | NIST AI RMF | Four-function lifecycle |
| Regulatory audit preparation | Both | Demonstrate maturity |
| Incident response | NIST AI RMF | MANAGE function structure |
| Training and skills development | SAFEST | Skills pillar detail |

---

## Cross-References

- [NIST AI RMF Reference Guide](../05-cross-cutting/nist-ai-rmf-reference-guide.md) — Complete NIST AI RMF guidance
- [NIST AI RMF Assessment Checklist](../01-discovery-governance/checklists/nist-ai-rmf-assessment.yaml) — Machine-readable checklist
- [ML Lifecycle Canvas (NIST Edition)](../00-getting-started/ml-lifecycle-canvas-nist-edition.md) — Updated canvas
- [SAFEST Coverage Matrix](./safest-coverage-matrix.md) — ProtoLabs-specific SAFEST coverage
- [Regulatory Reference Index](../05-cross-cutting/regulatory-reference-index.md) — Complete regulatory mapping

---

*Last updated: 2026-04-23 / Version: 1.0 / Classification: Internal*
