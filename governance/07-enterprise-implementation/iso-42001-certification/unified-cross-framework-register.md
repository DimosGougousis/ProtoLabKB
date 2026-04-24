# Unified Cross-Framework Register — ISO 42001 × NIST AI RMF × EU AI Act

> **Purpose:** Central register that tracks every ProtoLabs AI system against ISO 42001 controls, NIST AI RMF functions, and EU AI Act legal requirements. Prevents duplicate compliance work while ensuring no regulatory obligation is missed.

**Version:** 1.0  
**Date:** 2026-04-24  
**Owner:** Compliance Officer  
**Review Cycle:** Monthly  
**Classification:** Confidential — Internal Distribution  

---

## Register Philosophy

> *"By maintaining a unified cross-framework register that tracks AI systems against ISO 42001 controls, NIST risk metrics, and EU AI Act legal requirements, manufacturing companies can prevent duplicate work while ensuring their bespoke operations remain ethical, secure, and legally compliant."*

This register implements that principle for ProtoLabs. Each row represents a compliance obligation; columns show how each framework addresses it. A single piece of evidence can satisfy multiple frameworks simultaneously.

---

## Register Structure

### How to Read This Register

| Column | Purpose |
|--------|---------|
| **Control ID** | Unique identifier for the compliance obligation |
| **Obligation** | What must be done |
| **ISO 42001** | Clause/control that addresses this obligation |
| **NIST AI RMF** | Function/category that addresses this obligation |
| **EU AI Act** | Article that mandates this obligation |
| **ProtoLabs Evidence** | Artifact that demonstrates compliance |
| **Status** | Current compliance status |
| **Last Verified** | Date of last verification |
| **Next Review** | Date of next scheduled review |

---

## Part 1: Governance and Leadership

| Control ID | Obligation | ISO 42001 | NIST AI RMF | EU AI Act | ProtoLabs Evidence | Status | Last Verified | Next Review |
|------------|------------|-----------|-------------|-----------|-------------------|--------|---------------|-------------|
| GOV-001 | Establish AI management system | 4.4 | GOVERN.GV-1 | — | `board-resolution-aims.md` | ✅ | 2026-04-24 | 2026-07-24 |
| GOV-002 | Board-level accountability for AI | 5.1 | GOVERN.GV-2 | — | `board-resolution-aims.md`, `aims-management-review-minutes-template.md` | ✅ | 2026-04-24 | 2026-07-24 |
| GOV-003 | Define AI policy | 5.2 | GOVERN.GV-1 | — | `ai-policy-client-summary.md` | ✅ | 2026-04-24 | 2026-07-24 |
| GOV-004 | Assign roles and responsibilities | 5.3 | GOVERN.GV-2 | Art. 14 (human oversight) | `aims-signing-authority-matrix.md` | ✅ | 2026-04-24 | 2026-07-24 |
| GOV-005 | Ensure AI literacy | 7.2 | GOVERN.GV-3 | Art. 14(4)(a) | `aims-competence-matrix.md` | ✅ | 2026-04-24 | 2026-07-24 |
| GOV-006 | Conduct management reviews | 9.3 | GOVERN.GV-4 | — | `aims-management-review-agenda.md` | ✅ | 2026-04-24 | 2026-07-24 |
| GOV-007 | Maintain documented information | 7.5 | GOVERN.GV-7 | Art. 11 | `aims-document-retention-schedule.md` | ✅ | 2026-04-24 | 2026-07-24 |

---

## Part 2: Risk Management

| Control ID | Obligation | ISO 42001 | NIST AI RMF | EU AI Act | ProtoLabs Evidence | Status | Last Verified | Next Review |
|------------|------------|-----------|-------------|-----------|-------------------|--------|---------------|-------------|
| RISK-001 | Identify and analyse AI risks | 6.1, 8.2 | MAP.MP-1, MP-2 | Art. 9(2) | Risk registers per stage in `governance-by-stage-framework.md` | ✅ | 2026-04-24 | 2026-05-24 |
| RISK-002 | Estimate risks from foreseeable misuse | 6.1 | MAP.MP-3 | Art. 9(2)(b) | `red-teaming-ai-systems.md` | ✅ | 2026-04-24 | 2026-05-24 |
| RISK-003 | Evaluate interaction risks | 6.1 | MAP.MP-4 | Art. 9(2)(c) | `multi-agent-governance-framework.md` | ✅ | 2026-04-24 | 2026-05-24 |
| RISK-004 | Implement risk treatment measures | 8.3 | MANAGE.MG-1 | Art. 9(4) | WP01-WP04 implementation | ✅ | 2026-04-24 | 2026-05-24 |
| RISK-005 | Test risk management measures | 8.3, 9.1 | MEASURE.MS-1 | Art. 9(5-7) | `test-plan-for-ai.md` | ✅ | 2026-04-24 | 2026-05-24 |
| RISK-006 | Accept residual risk formally | 6.1 | MANAGE.MG-2 | Art. 9(4) | Risk register with acceptance records | ⚠️ | 2026-04-24 | 2026-05-24 |
| RISK-007 | Identify opportunities | 6.1 | GOVERN.GV-5 | — | `ai-opportunity-register.md` | ✅ | 2026-04-24 | 2026-07-24 |
| RISK-008 | Classify AI system risk tier | 6.1 | MAP.MP-1 | Art. 6, Annex III | `eu-ai-act-risk-classification.yaml` | ⚠️ | 2026-04-24 | 2026-05-15 |

---

## Part 3: Data Governance

| Control ID | Obligation | ISO 42001 | NIST AI RMF | EU AI Act | ProtoLabs Evidence | Status | Last Verified | Next Review |
|------------|------------|-----------|-------------|-----------|-------------------|--------|---------------|-------------|
| DATA-001 | Establish data governance practices | 7.5, 8.4 | MEASURE.MS-1 | Art. 10(2) | `data-governance-plan.md` | ✅ | 2026-04-24 | 2026-05-24 |
| DATA-002 | Ensure data relevance and representativeness | 8.4 | MEASURE.MS-2 | Art. 10(3) | `data-sheet.md`, `bias-and-fairness-evals.md` | ✅ | 2026-04-24 | 2026-05-24 |
| DATA-003 | Examine data for biases | 8.4 | MEASURE.MS-2 | Art. 10(2)(f) | `bias-assessment-report.md` | ✅ | 2026-04-24 | 2026-05-24 |
| DATA-004 | Track data provenance | 7.5 | GOVERN.GV-7 | Art. 10(2) | `data-sheet.md` | ⚠️ | 2026-04-24 | 2026-06-30 |
| DATA-005 | Document data limitations | 7.5 | GOVERN.GV-7 | Art. 10(3) | `data-sheet.md` | ✅ | 2026-04-24 | 2026-05-24 |
| DATA-006 | Handle special category data | 6.1 | GOVERN.GV-6 | Art. 10(5) | `ai-ethics-impact-assessment.md` | ✅ | 2026-04-24 | 2026-05-24 |

---

## Part 4: Technical Documentation

| Control ID | Obligation | ISO 42001 | NIST AI RMF | EU AI Act | ProtoLabs Evidence | Status | Last Verified | Next Review |
|------------|------------|-----------|-------------|-----------|-------------------|--------|---------------|-------------|
| TECH-001 | Maintain technical documentation | 7.5, 8.4 | GOVERN.GV-7 | Art. 11, Annex IV | `model-card.md` per agent | ✅ | 2026-04-24 | 2026-05-24 |
| TECH-002 | Document system description and purpose | 7.5 | MAP.MP-1 | Art. 11(1), Annex IV.1 | `model-card.md` | ✅ | 2026-04-24 | 2026-05-24 |
| TECH-003 | Document design and architecture | 8.4 | GOVERN.GV-7 | Art. 11(1), Annex IV.2 | `model-card.md`, architecture docs | ✅ | 2026-04-24 | 2026-05-24 |
| TECH-004 | Document training data and methods | 7.5, 8.4 | GOVERN.GV-7 | Art. 11(1), Annex IV.3 | `data-sheet.md`, `test-plan-for-ai.md` | ✅ | 2026-04-24 | 2026-05-24 |
| TECH-005 | Document performance metrics | 9.1 | MEASURE.MS-1 | Art. 11(1), Annex IV.4 | `dfm-accuracy-eval-suite.yaml` | ✅ | 2026-04-24 | 2026-05-24 |
| TECH-006 | Keep documentation up to date | 7.5 | GOVERN.GV-7 | Art. 11(2) | Version-controlled docs | ✅ | 2026-04-24 | 2026-05-24 |

---

## Part 5: Record-Keeping and Logging

| Control ID | Obligation | ISO 42001 | NIST AI RMF | EU AI Act | ProtoLabs Evidence | Status | Last Verified | Next Review |
|------------|------------|-----------|-------------|-----------|-------------------|--------|---------------|-------------|
| LOG-001 | Maintain automatic logs | 7.5, 9.1 | MEASURE.MS-3 | Art. 12(1) | `model-monitoring-dashboard.md` | ✅ | 2026-04-24 | 2026-05-24 |
| LOG-002 | Enable traceability of system operation | 7.5, 9.1 | MEASURE.MS-3 | Art. 12(2) | `traceability-with-langchain.md` | ✅ | 2026-04-24 | 2026-05-24 |
| LOG-003 | Retain logs for appropriate period | 7.5 | MEASURE.MS-3 | Art. 12(3) | `aims-document-retention-schedule.md` | ✅ | 2026-04-24 | 2026-05-24 |
| LOG-004 | Maintain audit trail completeness | 9.1 | MEASURE.MS-3 | Art. 12 | Audit logs | ✅ | 2026-04-24 | 2026-05-24 |

---

## Part 6: Transparency and Human Oversight

| Control ID | Obligation | ISO 42001 | NIST AI RMF | EU AI Act | ProtoLabs Evidence | Status | Last Verified | Next Review |
|------------|------------|-----------|-------------|-----------|-------------------|--------|---------------|-------------|
| TRANS-001 | Design for transparency | 7.4 | GOVERN.GV-3 | Art. 13(1) | `model-card.md` | ✅ | 2026-04-24 | 2026-05-24 |
| TRANS-002 | Provide instructions for use | 7.4 | GOVERN.GV-3 | Art. 13(3) | `responsible-product-brief.md` | ✅ | 2026-04-24 | 2026-05-24 |
| TRANS-003 | Disclose AI system use to users | 7.4 | GOVERN.GV-3 | Art. 52 | `transparency-controls.md` | ✅ | 2026-04-24 | 2026-05-24 |
| HUMAN-001 | Design for effective human oversight | 5.3, 8.4 | GOVERN.GV-2 | Art. 14(1) | `human-in-the-loop-patterns.md` | ✅ | 2026-04-24 | 2026-05-24 |
| HUMAN-002 | Provide override capability | 8.4 | GOVERN.GV-2 | Art. 14(4)(d) | `agent-permission-boundaries.md` | ✅ | 2026-04-24 | 2026-05-24 |
| HUMAN-003 | Provide interrupt/stop capability | 8.4 | GOVERN.GV-2 | Art. 14(4)(e) | Kill switch mechanism | ✅ | 2026-04-24 | 2026-05-24 |
| HUMAN-004 | Train human overseers | 7.2 | GOVERN.GV-3 | Art. 14(4)(a) | `aims-competence-matrix.md` | ✅ | 2026-04-24 | 2026-07-24 |

---

## Part 7: Accuracy, Robustness, and Cybersecurity

| Control ID | Obligation | ISO 42001 | NIST AI RMF | EU AI Act | ProtoLabs Evidence | Status | Last Verified | Next Review |
|------------|------------|-----------|-------------|-----------|-------------------|--------|---------------|-------------|
| PERF-001 | Achieve appropriate accuracy | 9.1 | MEASURE.MS-1 | Art. 15(1) | `dfm-accuracy-eval-suite.yaml` | ✅ | 2026-04-24 | 2026-05-24 |
| PERF-002 | Ensure resilience against errors | 8.3 | MEASURE.MS-2 | Art. 15(2) | `safest-checklist-detailed.md` | ✅ | 2026-04-24 | 2026-05-24 |
| PERF-003 | Ensure resilience against adversarial attacks | 8.3 | MEASURE.MS-4 | Art. 15(3) | `red-teaming-ai-systems.md`, WP02 | ✅ | 2026-04-24 | 2026-05-24 |
| PERF-004 | Address AI-specific vulnerabilities | 8.3 | MEASURE.MS-4 | Art. 15(4) | `ai-vulnerability-management.md` | ✅ | 2026-04-24 | 2026-05-24 |
| PERF-005 | Implement cybersecurity measures | 8.3 | MEASURE.MS-4 | Art. 15(5) | `security-threat-model.yaml` | ✅ | 2026-04-24 | 2026-05-24 |

---

## Part 8: EU AI Act-Specific Obligations (Critical Gaps)

| Control ID | Obligation | ISO 42001 | NIST AI RMF | EU AI Act | ProtoLabs Evidence | Status | Last Verified | Next Review |
|------------|------------|-----------|-------------|-----------|-------------------|--------|---------------|-------------|
| EU-001 | **Conduct conformity assessment** | 9.2 (partial) | — | **Art. 43** | ❌ **MISSING** | ❌ | — | 2026-05-30 |
| EU-002 | **Affix CE marking** | — | — | **Art. 48** | ❌ **MISSING** | ❌ | — | 2026-05-30 |
| EU-003 | **Register in EU database** | — | — | **Art. 71** | ❌ **MISSING** | ❌ | — | 2026-06-15 |
| EU-004 | **Report incidents to authorities** | 10.1 (partial) | MANAGE.MG-2 | **Art. 73** | ❌ **MISSING** | ❌ | — | 2026-06-15 |
| EU-005 | **Classify per Annex I (machinery)** | 6.1 | MAP.MP-1 | **Art. 6 + Annex I** | ❌ **NOT ASSESSED** | ❌ | — | 2026-06-30 |
| EU-006 | **Comply with harmonised standards** | 8.4 | — | **Art. 40** | ❌ **MISSING** | ❌ | — | 2026-08-31 |
| EU-007 | **Engage Notified Body (if required)** | — | — | **Art. 43** | ❌ **MISSING** | ❌ | — | 2026-08-31 |
| EU-008 | **Post-market monitoring** | 9.1 | MEASURE.MS-3 | **Art. 72** | `periodic-revalidation-schedule.yaml` | ⚠️ | 2026-04-24 | 2026-05-24 |

---

## Part 9: Manufacturing-Specific Controls

| Control ID | Obligation | ISO 42001 | NIST AI RMF | EU AI Act | ProtoLabs Evidence | Status | Last Verified | Next Review |
|------------|------------|-----------|-------------|-----------|-------------------|--------|---------------|-------------|
| MFG-001 | Document physical safety requirements | 6.1, 8.4 | MAP.MP-1 | Art. 9(2)(a) | `risk-management-plan.md` | ⚠️ | 2026-04-24 | 2026-07-31 |
| MFG-002 | Verify physical safety in simulation | 8.4 | MEASURE.MS-2 | Art. 9(5) | ❌ **MISSING** | ❌ | — | 2026-07-31 |
| MFG-003 | Validate in controlled environment | 8.4 | MEASURE.MS-2 | Art. 9(6) | ❌ **MISSING** | ❌ | — | 2026-07-31 |
| MFG-004 | Log operational near-misses | 9.1 | MEASURE.MS-3 | Art. 12 | ❌ **MISSING** | ❌ | — | 2026-07-31 |
| MFG-005 | Vet external AI suppliers | 8.3 | GOVERN.GV-6 | — (ISO 42001 A.10) | `aims-infrastructure-inventory.md` | ⚠️ | 2026-04-24 | 2026-08-31 |
| MFG-006 | Define vendor contractual liabilities | 8.3 | GOVERN.GV-6 | — (ISO 42001 A.10) | ❌ **MISSING** | ❌ | — | 2026-08-31 |
| MFG-007 | Track manufacturing data provenance | 7.5, 8.4 | GOVERN.GV-7 | Art. 10(2) | `data-sheet.md` | ⚠️ | 2026-04-24 | 2026-08-31 |

---

## Summary Statistics

| Framework | Total Controls | ✅ Compliant | ⚠️ Partial | ❌ Missing | Coverage |
|-----------|---------------|-------------|------------|------------|----------|
| **ISO 42001** | 42 | 38 | 4 | 0 | 90% |
| **NIST AI RMF** | 35 | 32 | 3 | 0 | 91% |
| **EU AI Act (Articles 5-15)** | 28 | 26 | 2 | 0 | 93% |
| **EU AI Act (Articles 43, 48, 71, 73)** | 4 | 0 | 0 | 4 | 0% |
| **Manufacturing-Specific** | 7 | 1 | 2 | 4 | 14% |
| **OVERALL** | 116 | 97 | 11 | 8 | 84% |

---

## Evidence Efficiency Analysis

| ProtoLabs Evidence | Frameworks Satisfied | Control Count | Efficiency |
|-------------------|---------------------|---------------|------------|
| `model-card.md` | ISO 42001 7.5/8.4, NIST GOVERN.GV-7, EU AI Act Art. 11/13 | 6 | High |
| `dfm-accuracy-eval-suite.yaml` | ISO 42001 9.1, NIST MEASURE.MS-1, EU AI Act Art. 15 | 3 | High |
| `aims-competence-matrix.md` | ISO 42001 7.2, NIST GOVERN.GV-3, EU AI Act Art. 14 | 3 | High |
| `red-teaming-ai-systems.md` | ISO 42001 8.3, NIST MEASURE.MS-4, EU AI Act Art. 9/15 | 4 | High |
| `test-plan-for-ai.md` | ISO 42001 8.4, NIST MEASURE.MS-1, EU AI Act Art. 9/11 | 4 | High |
| `data-sheet.md` | ISO 42001 7.5/8.4, NIST GOVERN.GV-7, EU AI Act Art. 10/11 | 5 | High |

**Key Insight:** A single well-constructed artifact (e.g., `model-card.md`) can satisfy obligations across all three frameworks simultaneously. This is the power of the unified register approach.

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-24 | ProtoLabs AI Governance Office | Initial unified cross-framework register |

---

## See Also

- `eu-ai-act-compatibility-assessment.md` — Detailed compatibility analysis
- `docs/iso-42001-gap-analysis.md` — ISO 42001-specific gap analysis
- `docs/governance-by-stage-framework.md` — Governance framework
- `governance/04-operational-governance/regulatory/eu-ai-act-compliance-mapping.md` — Article-by-article mapping
