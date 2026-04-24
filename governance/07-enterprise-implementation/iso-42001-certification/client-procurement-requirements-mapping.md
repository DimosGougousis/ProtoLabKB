# Client Procurement Requirements Mapping — ISO/IEC 42001 Certification

> **Purpose:** Maps ProtoLabs' ISO/IEC 42001 AIMS capabilities to common client procurement requirements, enabling rapid RFP response and demonstrating certifiable AI governance to aerospace, medical, and automotive clients.

**Version:** 1.0  
**Last Updated:** 2026-04-24  
**Owner:** Chief AI Officer / Sales Engineering  
**Review Cycle:** Quarterly  
**Classification:** Confidential — Internal Use (Client-Facing Derivatives Approved)  

---

## Executive Summary

ProtoLabs' ISO/IEC 42001:2023 certification provides a **certifiable, independently audited** AI Management System that directly addresses the AI governance requirements increasingly specified in RFPs from regulated industries. This document maps our AIMS artifacts to typical procurement requirements, enabling rapid, evidence-based RFP responses.

**Key Value Propositions:**
- ✅ **Certifiable Standard:** ISO 42001 is the only internationally recognized certifiable AI management system standard
- ✅ **Independent Verification:** Third-party audit by accredited certification body (TÜV SÜD or BSI)
- ✅ **Regulatory Alignment:** Maps to EU AI Act, NIST AI RMF, Singapore MGF, and emerging regulations
- ✅ **Industry-Specific:** Aerospace (AS9100), Medical (ISO 13485), Automotive (IATF 16949) compatible
- ✅ **Continuous Improvement:** PDCA cycle ensures ongoing enhancement, not one-time compliance

---

## Common Procurement Requirements Mapping

### Category 1: AI Governance and Management System

| Client Requirement | ProtoLabs AIMS Response | Evidence Artifact | ISO 42001 Clause |
|-------------------|------------------------|-------------------|------------------|
| "Demonstrate an AI management system" | ProtoLabs operates a certified ISO/IEC 42001:2023 AIMS | `board-resolution-aims.md`, certification certificate | 4.4 |
| "Board-level accountability for AI" | Board resolution establishing AIMS, quarterly management review | `board-resolution-aims.md`, `aims-management-review-minutes-template.md` | 5.1, 9.3 |
| "Defined AI policy" | Comprehensive AI policy with client-facing summary | `ai-policy-client-summary.md` | 5.2 |
| "Clear roles and responsibilities" | RACI matrix with named AIMS owner, policy owner, technical owner, safety officer | `aims-signing-authority-matrix.md` | 5.3 |

### Category 2: Risk Management

| Client Requirement | ProtoLabs AIMS Response | Evidence Artifact | ISO 42001 Clause |
|-------------------|------------------------|-------------------|------------------|
| "AI risk assessment process" | Systematic AI risk assessment for all agents, covering safety, security, fairness, privacy | Risk assessment reports per agent | 6.1, 8.2 |
| "Risk treatment and mitigation" | Documented risk treatment plans, WP01-WP04 implementation | `work-package-01-input-sanitization.md` through `work-package-04-audit-compliance.md` | 8.3 |
| "Residual risk acceptance" | Formal residual risk acceptance process with appropriate authority levels | Risk register with acceptance records | 6.1 |
| "Third-party and supply chain risk" | Vendor risk assessments, dependency management | `aims-infrastructure-inventory.md` | 8.3 |

### Category 3: Safety and Reliability

| Client Requirement | ProtoLabs AIMS Response | Evidence Artifact | ISO 42001 Clause |
|-------------------|------------------------|-------------------|------------------|
| "Safety-critical AI controls" | Tier 2/3 safety architecture with kill switches (30s/5s), guardrails, human-in-the-loop | `agent-tier-classification.yaml`, safety architecture docs | 8.3, 8.4 |
| "Accuracy and performance validation" | DFM accuracy evaluation suite, continuous monitoring, quarterly accuracy reports | `dfm-accuracy-eval-suite.yaml`, accuracy dashboards | 9.1 |
| "Fail-safe mechanisms" | Kill switches, circuit breakers, graceful degradation, rollback capability | Safety agent configuration, runbooks | 8.3 |
| "Human oversight" | Meaningful human accountability, HITL for Tier 2/3, override capabilities | `aims-signing-authority-matrix.md` | 5.3, 8.4 |

### Category 4: Security and Adversarial Defense

| Client Requirement | ProtoLabs AIMS Response | Evidence Artifact | ISO 42001 Clause |
|-------------------|------------------------|-------------------|------------------|
| "Adversarial robustness" | WP02 adversarial defense system, red team testing, prompt injection defense | `work-package-02-adversarial-defense.md` | 8.3 |
| "Input validation and sanitization" | WP01 multi-layer input sanitization, schema validation, content filtering | `work-package-01-input-sanitization.md` | 8.3 |
| "Security monitoring" | WP03 runtime monitoring, anomaly detection, SIEM integration | `work-package-03-runtime-monitoring.md` | 9.1 |
| "Incident response" | Documented incident response procedures, escalation paths, forensic capability | Incident response plan | 10.1 |

### Category 5: Explainability and Transparency

| Client Requirement | ProtoLabs AIMS Response | Evidence Artifact | ISO 42001 Clause |
|-------------------|------------------------|-------------------|------------------|
| "Explainable AI" | Every DFM recommendation includes reasoning, source citations, confidence scores | Agent output templates | 8.4 |
| "Audit trail" | Complete audit logging, immutable logs, chain of custody | `aims-document-retention-schedule.md`, audit logs | 7.5, 9.1 |
| "Model documentation" | Model cards, training data documentation, performance benchmarks | Model registry | 8.4 |
| "Decision traceability" | End-to-end traceability from input to output, version control | MLOps pipeline documentation | 8.4 |

### Category 6: Privacy and Data Protection

| Client Requirement | ProtoLabs AIMS Response | Evidence Artifact | ISO 42001 Clause |
|-------------------|------------------------|-------------------|------------------|
| "Data protection compliance" | GDPR/CCPA compliance, data minimization, purpose limitation | Privacy impact assessments | 6.1, 8.3 |
| "Data subject rights" | Process for access, rectification, erasure, portability requests | DPO procedures | 6.1 |
| "Data retention and disposal" | Documented retention schedule, secure disposal procedures | `aims-document-retention-schedule.md` | 7.5 |
| "Cross-border data transfers" | Transfer impact assessments, Standard Contractual Clauses | Legal documentation | 6.1 |

### Category 7: Fairness and Bias

| Client Requirement | ProtoLabs AIMS Response | Evidence Artifact | ISO 42001 Clause |
|-------------------|------------------------|-------------------|------------------|
| "Bias testing and mitigation" | Regular bias audits, demographic parity testing, mitigation strategies | Bias audit reports | 6.1, 8.3 |
| "Fairness metrics" | Documented fairness KPIs, monitoring dashboards | `aims-objectives-and-kpis.md` | 9.1 |
| "Inclusive design" | Diverse training data, accessibility considerations | Data documentation | 8.4 |

### Category 8: Compliance and Certification

| Client Requirement | ProtoLabs AIMS Response | Evidence Artifact | ISO 42001 Clause |
|-------------------|------------------------|-------------------|------------------|
| "ISO 42001 certification" | Certified by accredited body (TÜV SÜD or BSI), certificate valid | Certification certificate | All |
| "Internal audit program" | Annual internal audit program, clause-by-clause checklist, findings tracked to closure | `aims-internal-audit-plan.md`, `aims-internal-audit-checklist.md` | 9.2 |
| "Management review" | Quarterly management review with board-level oversight | `aims-management-review-agenda.md`, minutes | 9.3 |
| "Corrective action process" | Documented CAR process, root cause analysis, effectiveness verification | `aims-corrective-action-template.md`, tracker | 10.1 |
| "Continuous improvement" | Improvement register, opportunity register, innovation pipeline | `aims-improvement-register.md`, `ai-opportunity-register.md` | 10.2 |

---

## Industry-Specific Procurement Requirements

### Aerospace (AS9100, AS9102, FAR 25)

| Requirement | ProtoLabs Response | Evidence |
|-------------|-------------------|----------|
| Configuration management | AIMS document control, version management, change control | `aims-document-retention-schedule.md` |
| Traceability | End-to-end traceability from requirements to outputs | MLOps pipeline |
| Supplier quality | Vendor qualification, ongoing monitoring, audit rights | `aims-infrastructure-inventory.md` |
| Risk management (AS9100 8.1.1) | AI risk assessment integrated with aerospace risk management | Risk register |

### Medical (ISO 13485, FDA 21 CFR Part 820, EU MDR)

| Requirement | ProtoLabs Response | Evidence |
|-------------|-------------------|----------|
| Design controls | AI system lifecycle with design reviews, verification, validation | `work-package-cad-ai-evaluation.md` |
| Software validation | IQ/OQ/PQ for AI systems, validation protocols | Validation reports |
| Post-market surveillance | Continuous monitoring, adverse event reporting, periodic safety updates | WP03 monitoring |
| Clinical evaluation | Performance validation against clinical requirements | Accuracy evaluations |

### Automotive (IATF 16949, ASPICE, ISO 26262)

| Requirement | ProtoLabs Response | Evidence |
|-------------|-------------------|----------|
| Functional safety (ISO 26262) | Safety agent architecture, ASIL-aligned controls | Safety architecture docs |
| Cybersecurity (ISO/SAE 21434) | WP02 adversarial defense, threat analysis, security monitoring | Security assessments |
| PPAP readiness | Documented process capability, control plans, MSA | Process documentation |
| Traceability | Requirements traceability matrix, bidirectional tracing | Traceability matrix |

---

## RFP Response Templates

### Quick Response (One-Page)

> ProtoLabs operates a **certified ISO/IEC 42001:2023 AI Management System** (Certificate #[XXX], [Certification Body], valid [Date]). Our AIMS covers all AI agents used in DFM evaluation, material selection, and production scheduling, with independent third-party verification of our governance, risk management, safety controls, and continuous improvement processes. We provide full transparency through audit trails, explainable recommendations, and documented risk treatment. Our certification is maintained through annual surveillance audits and quarterly management reviews with board oversight.

### Detailed Response (Three-Page)

[Expand with specific evidence references, metrics, and client-relevant examples]

---

## Evidence Package for Client Audit

When clients request to audit our AI governance:

| Document | Purpose | Shareable? |
|----------|---------|------------|
| ISO 42001 Certificate | Proof of certification | ✅ Yes (public) |
| `ai-policy-client-summary.md` | High-level policy overview | ✅ Yes (public) |
| `aims-objectives-and-kpis.md` | Performance commitments | ✅ Yes (with NDA) |
| Internal audit summary | Evidence of ongoing compliance | ✅ Yes (with NDA) |
| Management review minutes | Board-level oversight evidence | ✅ Yes (with NDA, redacted) |
| Risk register (summary) | Risk management evidence | ✅ Yes (with NDA, sanitized) |
| Detailed procedures | Operational evidence | ❌ No (internal only) |
| Full audit reports | Detailed findings | ❌ No (internal only) |

---

## Competitive Differentiation

| Competitor Claim | ProtoLabs Advantage |
|-----------------|---------------------|
| "We follow AI principles" | **Certified** management system, independently audited |
| "We do risk assessments" | **Systematic** risk assessment with treatment tracking, integrated into AIMS |
| "We have safety controls" | **Tiered** safety architecture with kill switches, guardrails, HITL |
| "We're transparent" | **Explainable** outputs with source citations, full audit trails |
| "We comply with regulations" | **Proactive** compliance with EU AI Act, NIST, Singapore MGF via ISO 42001 |

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-24 | ProtoLabs AI Governance Office | Initial procurement requirements mapping |

---

## See Also

- `governance/07-enterprise-implementation/iso-42001-certification/ai-policy-client-summary.md` — Client-facing policy
- `governance/07-enterprise-implementation/iso-42001-certification/aims-evaluation-repository.md` — Evaluation evidence
- `docs/iso-42001-gap-analysis.md` — Gap analysis
