# EU AI Act Conformity Assessment Procedure — Article 43

> **Purpose:** Defines the formal conformity assessment process for ProtoLabs AI systems under the EU AI Act (Regulation (EU) 2024/1689), ensuring high-risk AI systems meet essential requirements before placement on the EU market.

**Version:** 1.0  
**Date:** 2026-04-24  
**Owner:** Compliance Officer  
**Classification:** Confidential — Internal Distribution  
**Regulatory Basis:** EU AI Act Articles 43, 48, Annexes IV-VII  

---

## 1. Scope

This procedure applies to all ProtoLabs AI systems classified as **high-risk** under the EU AI Act (Articles 6, Annex III, and Annex I), including:
- DFM evaluation agents used for critical manufacturing decisions
- Quality control vision systems making pass/fail decisions
- Predictive maintenance systems for safety-critical equipment
- Any AI system embedded in machinery, vehicles, or medical devices (Annex I)

---

## 2. Conformity Assessment Routes

### Route A: Internal Production Control (Article 43.1)

Applicable for Annex III high-risk AI systems where ProtoLabs is the **provider**.

| Step | Activity | Evidence Required | Owner |
|------|----------|-------------------|-------|
| 1 | Verify risk classification | Risk classification per `eu-ai-act-risk-classification.yaml` | Compliance Officer |
| 2 | Ensure technical documentation complete | Annex IV technical documentation | Model Owner |
| 3 | Implement quality management system | ISO 42001 AIMS operational | CAIO |
| 4 | Conduct internal testing | Test reports per `test-plan-for-ai.md` | ML Engineer |
| 5 | Prepare EU Declaration of Conformity | Signed DoC template | Compliance Officer |
| 6 | Affix CE marking | Physical/digital CE mark | Compliance Officer |
| 7 | Register in EU database | Registration per `eu-database-registration-procedure.md` | Compliance Officer |

### Route B: EU-Type Examination (Article 43.2)

Applicable for:
- Annex I high-risk AI systems (safety components in machinery, vehicles, medical devices)
- Systems where harmonised standards are not fully applied
- Systems requiring Notified Body involvement

| Step | Activity | Evidence Required | Owner |
|------|----------|-------------------|-------|
| 1 | Select Notified Body | Notified Body with AI scope (e.g., TÜV SÜD, BSI, DEKRA) | Compliance Officer |
| 2 | Submit EU-type examination application | Application + technical documentation | Compliance Officer |
| 3 | Notified Body examines design | Design review, testing, documentation audit | Notified Body |
| 4 | Receive EU-type examination certificate | Certificate of conformity | Notified Body |
| 5 | Implement production quality assurance | ISO 42001 + production controls | CAIO |
| 6 | Prepare EU Declaration of Conformity | Signed DoC referencing type examination | Compliance Officer |
| 7 | Affix CE marking | Physical/digital CE mark | Compliance Officer |

### Route C: Full Quality Assurance (Article 43.3)

Applicable for high-volume production of Annex I AI systems.

[Detailed steps for full QA route — to be expanded when applicable]

---

## 3. Conformity Assessment Checklist

### Pre-Assessment Preparation

| Check | Requirement | Evidence | Status |
|-------|-------------|----------|--------|
| 3.1 | Risk classification completed and documented | `eu-ai-act-risk-classification.yaml` | ☐ |
| 3.2 | Technical documentation per Annex IV complete | `model-card.md`, `data-sheet.md`, `test-plan-for-ai.md` | ☐ |
| 3.3 | Risk management system implemented | `risk-management-plan.md`, risk register | ☐ |
| 3.4 | Data governance practices established | `data-governance-plan.md`, `data-sheet.md` | ☐ |
| 3.5 | Human oversight measures implemented | `human-in-the-loop-patterns.md` | ☐ |
| 3.6 | Accuracy, robustness, cybersecurity tested | `dfm-accuracy-eval-suite.yaml`, `red-teaming-ai-systems.md` | ☐ |
| 3.7 | Quality management system (ISO 42001) operational | AIMS certification or implementation evidence | ☐ |
| 3.8 | Post-market monitoring system established | `periodic-revalidation-schedule.yaml` | ☐ |
| 3.9 | Incident reporting procedure established | `eu-ai-act-incident-reporting-procedure.md` | ☐ |
| 3.10 | Registration procedure established | `eu-database-registration-procedure.md` | ☐ |

### Essential Requirements Verification (Annex IV)

| Annex IV Section | Requirement | Evidence | Status |
|-----------------|-------------|----------|--------|
| 1 | General description of AI system | `model-card.md` — system description | ☐ |
| 2 | Description of design choices | Architecture documentation | ☐ |
| 3 | Description of training data | `data-sheet.md` | ☐ |
| 4 | Description of validation and testing | `test-plan-for-ai.md`, test results | ☐ |
| 5 | Description of risk management | `risk-management-plan.md` | ☐ |
| 6 | Description of human oversight | `human-in-the-loop-patterns.md` | ☐ |
| 7 | Description of accuracy and performance | `dfm-accuracy-eval-suite.yaml` | ☐ |
| 8 | Description of changes and updates | Change log, version control | ☐ |

---

## 4. EU Declaration of Conformity Template

```
EU DECLARATION OF CONFORMITY

No.: [Unique identifier]

1. AI System Identification:
   Name: [System name]
   Version: [Version number]
   Serial/Model Number: [If applicable]

2. Provider Identification:
   Name: ProtoLabs [Entity name]
   Address: [Registered address]
   Contact: [Email/Phone]

3. This declaration of conformity is issued under the sole responsibility of the provider.

4. Object of the Declaration:
   AI system: [Name and description]
   Risk classification: High-risk per EU AI Act Article 6 [Annex III/Annex I]

5. The object of the declaration described above is in conformity with:
   - Regulation (EU) 2024/1689 (EU AI Act)
   - [Harmonised standards applied, if any]
   - [Common specifications applied, if any]

6. Conformity Assessment Procedure:
   - Route: [Internal Production Control / EU-Type Examination / Full QA]
   - Notified Body: [Name, ID number] (if applicable)
   - Certificate: [Reference] (if applicable)

7. The technical documentation is kept at:
   [Address where documentation is maintained]

8. Signed for and on behalf of:
   [Place], [Date]
   [Name], [Position]
   [Signature]
```

---

## 5. Roles and Responsibilities

| Role | Responsibility |
|------|---------------|
| **Compliance Officer** | Coordinates conformity assessment, maintains checklist, prepares DoC |
| **CAIO** | Accountable for overall conformity; signs DoC |
| **Model Owner** | Provides technical documentation, ensures system meets requirements |
| **ML Engineer** | Conducts testing, provides test evidence |
| **Legal Counsel** | Reviews DoC, advises on regulatory interpretation |
| **Notified Body** | (If Route B/C) Conducts independent examination |

---

## 6. Timeline

| Activity | Duration | Dependencies |
|----------|----------|--------------|
| Pre-assessment preparation | 2-4 weeks | Technical documentation complete |
| Internal review | 1-2 weeks | Pre-assessment complete |
| Notified Body examination (Route B) | 4-8 weeks | Application submitted |
| DoC preparation and signing | 1 week | Assessment complete |
| CE marking | Immediate | DoC signed |
| EU database registration | 1-2 weeks | CE marking applied |
| **Total (Route A)** | **4-8 weeks** | |
| **Total (Route B)** | **8-16 weeks** | |

---

## 7. Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-24 | ProtoLabs AI Governance Office | Initial conformity assessment procedure |

---

## See Also

- `ce-marking-procedure.md` — CE marking process
- `eu-database-registration-procedure.md` — EU database registration
- `eu-ai-act-incident-reporting-procedure.md` — Incident reporting
- `governance/04-operational-governance/regulatory/eu-ai-act-compliance-mapping.md` — Article-by-article mapping
