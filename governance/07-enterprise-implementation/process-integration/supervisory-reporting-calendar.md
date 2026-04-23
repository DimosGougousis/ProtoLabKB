# Supervisory Reporting Calendar

## Purpose

Provide a consolidated calendar of all regulatory reporting deadlines and supervisory submission requirements related to AI governance for Dutch FinTechs supervised by DNB and ECB. Missing a reporting deadline is a compliance failure that can trigger supervisory action. This document ensures the CAIO, Compliance Officer, and governance teams know exactly what is due, when, and to whom -- eliminating the risk of forgotten obligations.

## When to Use

- During annual governance planning to build the reporting calendar into the project schedule
- At the start of each quarter to confirm upcoming deadlines
- When onboarding a new CAIO or Compliance Officer
- During DORA compliance program setup to identify AI-relevant reporting obligations
- When preparing for SREP (Supervisory Review and Evaluation Process) engagements

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **Compliance Officer** | **Responsible** -- tracks deadlines, coordinates submissions, ensures completeness |
| **CAIO** | **Accountable** -- owns AI-specific reporting content, reviews before submission |
| **Board** | **Informed** -- receives copies of all regulatory submissions relating to AI |
| **Internal Audit** | **Consulted** -- validates reporting accuracy before submission |
| **Model Owners** | **Consulted** -- provide system-specific data for inventory and incident reports |

## Regulatory Basis

- **DORA Article 19** -- reporting of major ICT-related incidents to competent authorities
- **DORA Article 28** -- outsourcing register for ICT third-party service providers (includes AI/ML services)
- **DORA Article 26(11)** -- annual report on ICT third-party arrangements
- **DNB Good Practice for AI** -- expectation of proactive supervisory engagement and self-assessment
- **EU AI Act Article 72** -- post-market monitoring and reporting obligations for high-risk AI
- **EU AI Act Article 62** -- reporting of serious incidents involving high-risk AI
- **Wft Section 3:17** -- sound and controlled business operations with adequate reporting
- **GDPR Article 33** -- breach notification to supervisory authority within 72 hours (where AI processes personal data)
- **PSD2 (Payment Services Directive)** -- incident reporting for payment service providers

---

## 1. Annual SREP Cycle

The Supervisory Review and Evaluation Process (SREP) is DNB's primary mechanism for assessing the soundness of supervised institutions. For FinTechs with AI systems, SREP increasingly includes AI governance as a review topic.

### 1.1 SREP Timeline (Typical Annual Cycle)

| Phase | Period | AI Governance Activities |
|-------|--------|------------------------|
| **Pre-SREP preparation** | Q1 | Update AI system inventory; refresh risk assessments; compile governance evidence package |
| **SREP questionnaire / data request** | Q1-Q2 | Respond to DNB data requests with AI governance documentation; provide model inventory |
| **On-site engagement** | Q2-Q3 | DNB interviews with CAIO, Board members, Model Owners; demonstrate governance in practice |
| **SREP outcome and findings** | Q3-Q4 | Receive SREP letter; address findings; implement remediation plan |
| **Remediation follow-up** | Q4-Q1 | Report on remediation progress; close findings before next cycle |

### 1.2 SREP Evidence Package for AI Governance

Prepare this evidence package annually, regardless of whether DNB specifically requests it.

| Evidence Category | Documents to Prepare | SAFEST Ref |
|------------------|---------------------|-----------|
| **Governance structure** | CoE charter, AI Governance Committee charter, CAIO mandate, org chart | A-01, A-04 |
| **AI system inventory** | Complete inventory with risk tiers, model owners, deployment dates | S-01 |
| **Risk management** | AI risk register, risk appetite statement, risk assessment methodology | A-03, S-02 |
| **Model documentation** | Model cards for all high-risk systems, data sheets, technical documentation | T-12 |
| **Evaluation evidence** | Eval suite results for all high and limited-risk systems, bias test reports | S-03, F-03 |
| **Monitoring evidence** | Monitoring dashboards, alert history, drift detection reports | S-12, T-17 |
| **Incident history** | AI incident reports, root cause analyses, remediation actions | A-15 |
| **Training records** | AI literacy training completion records for board, management, and staff | K-09 |
| **Third-party AI** | AI vendor assessments, contract provisions, outsourcing register entries | S-18 |

---

## 2. Model Inventory Submission

### 2.1 Submission Requirements

DNB expects supervised institutions to maintain and be able to produce a complete AI/ML model inventory at any time. While there is no fixed annual submission date, the inventory must be current and available upon request.

| Requirement | Specification | Frequency |
|------------|--------------|-----------|
| Inventory completeness | 100% of production AI/ML systems | Continuous |
| Inventory update after deployment | Within 5 business days of new deployment or retirement | Per change |
| Inventory format | Structured (spreadsheet or database), not narrative | Always |
| Inventory available for supervisory request | Within 2 business days of request | On demand |
| Annual inventory reconciliation | Full reconciliation of inventory against production systems | Annual (Q4) |

---

## 3. Incident Reporting Timelines

### 3.1 AI Incident Reporting Obligations

| Regulation | What to Report | To Whom | Timeline | Form |
|-----------|---------------|---------|----------|------|
| **DORA Art. 19** | Major ICT-related incidents (including AI system failures affecting critical functions) | DNB / ECB | Initial notification: within 4 hours of classification; Intermediate report: within 72 hours; Final report: within 1 month | DORA incident reporting template |
| **EU AI Act Art. 62** | Serious incidents involving high-risk AI systems (death, serious health damage, serious property damage, fundamental rights breach) | National market surveillance authority | Without undue delay, no later than 15 days after becoming aware | EU AI Act serious incident form |
| **GDPR Art. 33** | Personal data breaches involving AI processing | Autoriteit Persoonsgegevens (AP) | Within 72 hours of becoming aware | AP breach notification form |
| **PSD2** | Major operational or security incidents affecting payment services | DNB | Within 4 hours (initial); detailed report within 3 business days | EBA incident reporting template |

### 3.2 Internal Escalation to Reporting Triggers

| AI Incident Severity | Internal Response | External Reporting Triggered? |
|---------------------|------------------|------------------------------|
| **Severity 1** -- Critical (system failure, harmful outputs at scale, data breach) | CEO + Board notified within 1 hour; CAIO activates response | DORA: likely yes; GDPR: if personal data involved; EU AI Act: if serious incident |
| **Severity 2** -- Major (significant performance degradation, fairness violation, security breach) | CAIO notified within 2 hours; AI Governance Committee notified | DORA: assess; GDPR: assess; EU AI Act: assess |
| **Severity 3** -- Moderate (minor performance issue, contained fairness concern) | Model Owner resolves; CAIO notified within 24 hours | Generally no, unless escalated |
| **Severity 4** -- Minor (cosmetic issue, non-material anomaly) | Model Owner resolves; logged in incident register | No |

---

## 4. Outsourcing Register Updates

### 4.1 AI-Relevant Third-Party Services

Under DORA, FinTechs must maintain a register of all ICT third-party service providers. AI/ML services must be included.

| Third-Party AI Service Type | Example | Register Entry Required |
|----------------------------|---------|----------------------|
| LLM API providers | OpenAI, Anthropic, Google AI | Yes -- ICT third-party service |
| Cloud ML platforms | AWS SageMaker, Azure ML, GCP Vertex AI | Yes -- ICT third-party service |
| AI-specific SaaS | Fraud detection APIs, KYC verification services, credit scoring APIs | Yes -- critical or important function if used for regulated activities |
| Data providers for AI training | Alternative data vendors, credit bureau data | Yes -- if ICT service dependency |
| AI monitoring and observability | MLflow, Weights & Biases, Datadog ML monitoring | Yes -- ICT third-party service |

### 4.2 Outsourcing Register Update Schedule

| Event | Action | Timeline |
|-------|--------|----------|
| New AI third-party service onboarded | Add to outsourcing register | Before contract execution |
| Contract renewal or material amendment | Update register entry | Within 5 business days |
| Service terminated | Mark as terminated in register with date | Within 5 business days |
| Annual register review | Full reconciliation of register against active services | Annually (Q4) |
| DNB/ECB request for register | Submit current register | Within 2 business days |

---

## 5. DORA Reporting Obligations

### 5.1 Annual DORA Reports

| Report | Content | Submission To | Deadline | Owner |
|--------|---------|--------------|----------|-------|
| **ICT third-party register** | Complete register of all ICT third-party arrangements including AI services | DNB / ECB | Annually (date set by supervisor) | Compliance Officer |
| **ICT risk management review** | Annual review of ICT risk management framework, including AI risk management | Board (internal) | Q4 annually | CTO + CAIO |
| **Digital operational resilience testing** | Results of resilience testing for critical AI systems | DNB (if requested) | As scheduled by supervisor | CTO |

### 5.2 Event-Triggered DORA Reports

| Trigger Event | Report Required | Timeline | Owner |
|--------------|----------------|----------|-------|
| Major ICT incident involving AI | Incident notification (initial + intermediate + final) | 4h / 72h / 1 month | CAIO + Compliance |
| Significant cyber threat involving AI | Voluntary notification | As soon as practical | CISO + CAIO |
| Contract with critical AI third-party provider | Notification of critical arrangement | Before contract execution | Compliance Officer |
| Material change to AI risk management | Update risk management documentation | Before change implementation | CAIO |

---

## 6. Self-Assessment Deadlines

### 6.1 Internal Governance Self-Assessments

| Assessment | Scope | Frequency | Owner | Output |
|-----------|-------|-----------|-------|--------|
| **SAFEST self-assessment** | All 6 SAFEST pillars for all AI systems | Annually (Q1) | CAIO | SAFEST scorecard with evidence references |
| **AI risk appetite review** | Verify risk appetite is appropriate for current AI portfolio | Annually (Q1) or after material change | CAIO + CRO | Updated risk appetite statement |
| **AI governance maturity** | Assess maturity level using [Governance Maturity Roadmap](../risk-based-adoption/governance-maturity-roadmap.md) | Semi-annually (Q1, Q3) | CAIO | Maturity scorecard |
| **3LoD effectiveness** | Verify three lines of defense operating correctly for AI | Annually (Q2) | Internal Audit | 3LoD assessment report |
| **AI ethics review** | Review ethical risk for all high-risk and customer-facing AI | Annually (Q2) | AI Ethics Board | Ethics review outcomes |
| **Training needs analysis** | Assess AI competency gaps across the organization | Annually (Q3) | CAIO + HR | Training plan for next year |
| **Business continuity for AI** | Test fallback and rollback procedures for critical AI systems | Semi-annually (Q2, Q4) | CTO + CAIO | BC test results |

---

## 7. Month-by-Month Calendar Template

### 7.1 Annual Reporting Calendar

| Month | Internal Activities | External Submissions | Key Deadlines |
|-------|-------------------|---------------------|---------------|
| **January** | Kick off SAFEST self-assessment; AI risk appetite review; Q4 governance report finalization | -- | SAFEST self-assessment begins |
| **February** | Complete SAFEST self-assessment; begin SREP preparation; AI inventory reconciliation | -- | SAFEST self-assessment due |
| **March** | SREP evidence package preparation; Q1 quarterly governance report | Submit AI risk appetite statement to Board | Q1 board report due |
| **April** | 3LoD effectiveness assessment begins; ethics review for high-risk AI; respond to SREP data requests | DORA ICT third-party register (if annual deadline set by supervisor) | Outsourcing register submission |
| **May** | Complete 3LoD assessment; SREP on-site preparation; governance maturity mid-year check | -- | 3LoD assessment due |
| **June** | Q2 quarterly governance report; ethics review completion; mid-year governance review | Submit Q2 board report | Q2 board report due |
| **July** | Training needs analysis; address SREP findings (if received); BC test planning | -- | Training needs analysis begins |
| **August** | Business continuity test for critical AI; SREP remediation (if applicable) | -- | BC test (1st of 2) |
| **September** | Q3 quarterly governance report; governance maturity assessment; SREP remediation status | Submit Q3 board report; SREP remediation status report (if applicable) | Q3 board report due |
| **October** | Annual AI inventory reconciliation; outsourcing register review; next-year governance budget planning | -- | Inventory reconciliation begins |
| **November** | Complete inventory reconciliation; complete outsourcing register update; BC test (2nd) | -- | BC test (2nd of 2) |
| **December** | Q4 quarterly governance report; annual governance effectiveness review; next-year plan finalization | Submit Q4 board report; annual governance report to Board | Q4 board report due; annual report |

### 7.2 Event-Driven Reporting (Any Month)

These obligations are not calendar-based but triggered by events:

| Event | Obligation | Timeline | Owner |
|-------|-----------|----------|-------|
| AI incident (Severity 1-2) | Assess DORA / EU AI Act / GDPR reporting thresholds | Within 4 hours of incident | CAIO + Compliance |
| New high-risk AI deployment | Notify AI Governance Committee; update inventory | Before deployment | CAIO |
| New AI third-party contract | Update outsourcing register; assess criticality | Before contract | Compliance |
| Regulatory guidance published | Assess impact on AI governance framework | Within 30 days | CAIO + Compliance |
| Material change to AI system | Assess re-assessment / re-notification obligations | Before change | Model Owner |

---

## 8. Reporting Preparation Checklist

Use this checklist 30 days before any major submission deadline.

| # | Item | Done? | Owner |
|---|------|-------|-------|
| 1 | AI system inventory is current and complete | [ ] | CAIO |
| 2 | All model cards for high-risk systems are up to date | [ ] | Model Owners |
| 3 | Evaluation results for the current period are compiled | [ ] | ML Engineers |
| 4 | AI risk register is current with accurate trending | [ ] | AI Risk Analyst |
| 5 | Incident reports for the period are finalized with root causes | [ ] | CAIO |
| 6 | Training completion records are current | [ ] | Governance Coordinator |
| 7 | Outsourcing register reflects current AI third-party arrangements | [ ] | Compliance Officer |
| 8 | Board has received and acknowledged the quarterly governance report | [ ] | CAIO |
| 9 | Internal Audit has reviewed submission materials (for annual submissions) | [ ] | Internal Audit |
| 10 | Submission format matches regulator requirements | [ ] | Compliance Officer |

---

## Cross-References

- **Governance in Quarterly Planning:** [governance-in-quarterly-planning.md](governance-in-quarterly-planning.md) -- quarterly cadence that produces inputs for supervisory reporting
- **AI Incident Report Template:** [../../04-operational-governance/templates/ai-incident-report.md](../../04-operational-governance/templates/ai-incident-report.md) -- incident documentation that feeds DORA reporting
- **SAFEST Checklist:** [../../04-operational-governance/regulatory/safest-checklist-detailed.md](../../04-operational-governance/regulatory/safest-checklist-detailed.md) -- self-assessment basis
- **Board-Level AI Accountability:** [../organizational-model/board-level-ai-accountability.md](../organizational-model/board-level-ai-accountability.md) -- board reporting obligations
- **Regulatory Reference Index:** [../../05-cross-cutting/regulatory-reference-index.md](../../05-cross-cutting/regulatory-reference-index.md) -- detailed regulatory citations
- **Three Lines of Defense:** [../organizational-model/three-lines-of-defense-for-ai.md](../organizational-model/three-lines-of-defense-for-ai.md) -- 3LoD assessment referenced in calendar
- **Governance Maturity Roadmap:** [../risk-based-adoption/governance-maturity-roadmap.md](../risk-based-adoption/governance-maturity-roadmap.md) -- maturity assessment referenced in calendar

---

*Last updated: 2026-03-01*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
