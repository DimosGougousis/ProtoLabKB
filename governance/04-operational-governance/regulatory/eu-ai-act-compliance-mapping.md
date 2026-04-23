# EU AI Act Compliance Mapping

## Purpose

This document provides an article-by-article compliance mapping of the EU AI Act (Regulation (EU) 2024/1689) to the Master AI Governance Framework. For each relevant article, it specifies: what the regulation requires, what compliance evidence is needed, which role is responsible, and which framework artifacts address the requirement. This is the authoritative reference for demonstrating that the organization's AI governance practices satisfy EU AI Act obligations -- both for internal compliance tracking and for supervisory interactions with DNB, AFM, and national market surveillance authorities.

This mapping covers the articles most relevant to FinTech companies deploying business AI agents (customer-facing, autonomous decision-makers). Articles specific to general-purpose AI model providers (Chapter V) are included only where they create obligations for downstream deployers.

## When to Use

- When assessing whether a new AI system triggers EU AI Act obligations
- When preparing compliance evidence for supervisory review or conformity assessment
- When conducting internal audits of AI governance against regulatory requirements
- When updating governance processes to address regulatory changes or new interpretive guidance
- During board-level reporting on regulatory compliance posture
- When onboarding legal counsel or external auditors on the organization's AI compliance approach

## Who Is Responsible

| Role | R | A | C | I |
|------|---|---|---|---|
| **Compliance Officer (2nd Line)** | X | | | | Maintains the compliance mapping, tracks evidence completeness, coordinates conformity assessment |
| **CAIO** | | X | | | Accountable for overall EU AI Act compliance posture; reports to board |
| **Legal Counsel** | | | X | | Consulted on legal interpretation of articles and enforcement implications |
| **Model Owner** | X | | | | Responsible for producing compliance evidence for their specific systems |
| **Internal Audit (3rd Line)** | | | X | | Independently verifies compliance evidence and mapping accuracy |
| **Board / Management Body** | | | | X | Informed of compliance posture via quarterly governance report |

## Regulatory Basis

- **EU AI Act (Regulation (EU) 2024/1689)** -- Primary regulation mapped in this document
- **SAFEST pillars** -- DNB Good Practice mapped to corresponding EU AI Act articles
- **DORA (Regulation (EU) 2022/2554)** -- Cross-referenced where AI-as-ICT overlaps apply (see [DORA AI Requirements](./dora-ai-requirements.md))
- **ISO/IEC 42001** -- AI management system standard aligned with EU AI Act conformity assessment

---

## 1. Risk Classification (Article 6 and Annex III)

### 1.1 Requirement Summary

Article 6 defines the criteria for classifying AI systems as high-risk. An AI system is high-risk if it falls within the use cases listed in Annex III. For FinTech, the most relevant Annex III categories are:

- **Annex III, Area 5(b):** AI systems intended to evaluate the creditworthiness of natural persons or establish their credit score
- **Annex III, Area 5(a):** AI systems intended to evaluate eligibility for public assistance benefits and services (relevant for financial inclusion products)
- **Annex III, Area 3:** AI systems intended for recruitment, worker management, or access to self-employment (relevant for internal HR AI)
- **Annex III, Area 8:** AI systems for law enforcement (relevant if supporting AML/fraud investigations provided to authorities)

### 1.2 Compliance Mapping

| Requirement | Compliance Evidence | Responsible Role | Framework Artifact |
|------------|-------------------|-----------------|-------------------|
| Classify each AI system against Annex III categories | Documented risk classification per AI system | Model Owner + Compliance Officer | [EU AI Act Risk Classification Checklist](../../01-discovery-governance/checklists/eu-ai-act-risk-classification.yaml) |
| Document classification rationale with legal basis | Written assessment explaining why a system is or is not high-risk | Compliance Officer + Legal | [Responsible Product Brief](../../01-discovery-governance/templates/responsible-product-brief.md) |
| Maintain AI system inventory with risk classifications | Central registry of all AI systems with risk tier | CAIO | [SAFEST S-01](./safest-checklist-detailed.md) -- AI system inventory |
| Review classification when system purpose or scope changes | Change management process triggers reclassification | Model Owner | [Change Management for AI](../../07-enterprise-implementation/process-integration/change-management-for-ai.md) |

---

## 2. Prohibited Practices (Article 5)

### 2.1 Requirement Summary

Article 5 prohibits specific AI practices outright. The most relevant for FinTech:

- **Art. 5(1)(a):** Subliminal, manipulative, or deceptive techniques that distort behavior causing significant harm
- **Art. 5(1)(b):** Exploitation of vulnerabilities of specific groups (age, disability, social/economic situation)
- **Art. 5(1)(c):** Social scoring by public authorities (less relevant for private FinTech, but relevant if providing services to public sector)
- **Art. 5(1)(d):** Real-time remote biometric identification in publicly accessible spaces (generally not relevant for FinTech)
- **Art. 5(1)(e):** Inferring emotions in workplace or education (relevant for internal AI)
- **Art. 5(1)(f):** Biometric categorization inferring sensitive attributes (race, political opinions, religious beliefs)

### 2.2 Compliance Mapping

| Requirement | Compliance Evidence | Responsible Role | Framework Artifact |
|------------|-------------------|-----------------|-------------------|
| Screen all AI systems for prohibited practices | Documented review confirming no prohibited practices | Compliance Officer | [Ethical Product Discovery Checklist](../../01-discovery-governance/checklists/ethical-product-discovery.yaml) |
| Ensure customer-facing agents do not use manipulative techniques | Behavioral review of agent outputs; guardrail configuration | Model Owner + Ethics Lead | [Customer-Facing Agent Safety](../../03-runtime-governance/agentic-workflows/customer-facing-agent-safety.md) |
| Ensure no exploitation of vulnerable groups | Fairness testing across vulnerable populations | ML Engineer | [Bias and Fairness Evals](../../02-development-governance/evaluations/bias-and-fairness-evals.md) |
| Annual re-screening of all production AI systems | Annual compliance audit includes Art. 5 screening | Internal Audit (3rd Line) | [Periodic Revalidation Schedule](../evaluations/periodic-revalidation-schedule.yaml) |

---

## 3. High-Risk Requirements (Articles 8-15)

### 3.1 Risk Management System (Article 9)

| Requirement | Article Reference | Compliance Evidence | Responsible Role | Framework Artifact |
|------------|------------------|-------------------|-----------------|-------------------|
| Establish a risk management system | Art. 9(1) | Documented risk management process covering the full AI lifecycle | CAIO | [Risk Tiering Model](../../07-enterprise-implementation/risk-based-adoption/risk-tiering-model.md) |
| Identify and analyze known and foreseeable risks | Art. 9(2)(a) | Risk assessment per AI system | Model Owner | [AI Ethics Impact Assessment](../../01-discovery-governance/templates/ai-ethics-impact-assessment.md) |
| Estimate and evaluate risks from foreseeable misuse | Art. 9(2)(b) | Misuse analysis documented | Security Engineer | [Red Teaming AI Systems](../guides/red-teaming-ai-systems.md) |
| Evaluate risks from interaction with other systems | Art. 9(2)(c) | System integration risk analysis | ML Engineer | [Multi-Agent Governance Framework](../../03-runtime-governance/agentic-workflows/multi-agent-governance-framework.md) |
| Adopt risk management measures | Art. 9(4) | Documented risk mitigations with residual risk assessment | Model Owner | [Vulnerability Assessment Template](../templates/vulnerability-assessment.md) |
| Test risk management measures | Art. 9(5-7) | Test plans and results | ML Engineer | [Test Plan for AI](../../02-development-governance/templates/test-plan-for-ai.md) |

### 3.2 Data and Data Governance (Article 10)

| Requirement | Article Reference | Compliance Evidence | Responsible Role | Framework Artifact |
|------------|------------------|-------------------|-----------------|-------------------|
| Training, validation, and test datasets must be subject to data governance practices | Art. 10(2) | Data governance policies and procedures | Data Engineer | [Data Quality Checklist](../../02-development-governance/checklists/data-quality-checklist.yaml) |
| Datasets shall be relevant, sufficiently representative, and free of errors | Art. 10(3) | Data quality assessments, representativeness analysis | Data Engineer | [Data Sheet Template](../../02-development-governance/templates/data-sheet.md) |
| Examine data for possible biases | Art. 10(2)(f) | Bias analysis reports on training data | ML Engineer | [Bias Assessment Report](../../02-development-governance/templates/bias-assessment-report.md) |
| Special categories of personal data only for bias monitoring | Art. 10(5) | DPIA covering use of sensitive data for bias detection | DPO + Compliance | [AI Ethics Impact Assessment](../../01-discovery-governance/templates/ai-ethics-impact-assessment.md) |

### 3.3 Technical Documentation (Article 11)

| Requirement | Article Reference | Compliance Evidence | Responsible Role | Framework Artifact |
|------------|------------------|-------------------|-----------------|-------------------|
| Draw up technical documentation before placing on market | Art. 11(1) | Comprehensive technical documentation per Annex IV | Model Owner | [Model Card Template](../../02-development-governance/templates/model-card.md) |
| Documentation must contain information per Annex IV | Art. 11(1), Annex IV | Completed model card + data sheet + test plan | Model Owner + ML Engineer | [Model Card](../../02-development-governance/templates/model-card.md), [Data Sheet](../../02-development-governance/templates/data-sheet.md), [Test Plan](../../02-development-governance/templates/test-plan-for-ai.md) |
| Keep documentation up to date | Art. 11(2) | Version-controlled documentation with change log | Model Owner | [Definition of Done for AI](../../02-development-governance/quality-gates/definition-of-done-ai.md) |

### 3.4 Record-Keeping and Logging (Article 12)

| Requirement | Article Reference | Compliance Evidence | Responsible Role | Framework Artifact |
|------------|------------------|-------------------|-----------------|-------------------|
| Automatic recording of events (logs) | Art. 12(1) | Logging infrastructure with defined retention | MLOps Engineer | [Model Monitoring Dashboard](../templates/model-monitoring-dashboard.md) |
| Logging must enable tracing of system operation | Art. 12(2) | End-to-end request tracing | MLOps Engineer | [Traceability with LangChain](../guides/traceability-with-langchain.md) |
| Logs retained for period appropriate to intended purpose | Art. 12(3) | Log retention policy (minimum 6 months per Art. 12(3)) | Data Engineer | [Monitoring Setup Checklist](../checklists/monitoring-setup-checklist.yaml) |

### 3.5 Transparency and Provision of Information (Article 13)

| Requirement | Article Reference | Compliance Evidence | Responsible Role | Framework Artifact |
|------------|------------------|-------------------|-----------------|-------------------|
| Design for sufficient transparency | Art. 13(1) | Explainability approach documented per system | ML Engineer | [Model Card Template](../../02-development-governance/templates/model-card.md) |
| Instructions of use for deployers | Art. 13(3) | User-facing documentation including capabilities, limitations, human oversight measures | Product Owner | [Responsible Product Brief](../../01-discovery-governance/templates/responsible-product-brief.md) |
| Information on system accuracy, robustness, cybersecurity | Art. 13(3)(b)(ii) | Performance metrics, robustness test results, security assessment | ML Engineer + Security | [Eval-Driven Development](../../02-development-governance/evaluations/eval-driven-development.md) |

### 3.6 Human Oversight (Article 14)

| Requirement | Article Reference | Compliance Evidence | Responsible Role | Framework Artifact |
|------------|------------------|-------------------|-----------------|-------------------|
| Design for effective human oversight | Art. 14(1) | Human oversight design documented | Model Owner | [Human-in-the-Loop Patterns](../../03-runtime-governance/agentic-workflows/human-in-the-loop-patterns.md) |
| Human oversight measures proportionate to risk | Art. 14(2) | Risk-proportionate oversight mechanisms | Model Owner | [Autonomous Decision Governance](../../03-runtime-governance/agentic-workflows/autonomous-decision-governance.md) |
| Ability to understand system capabilities and limitations | Art. 14(4)(a) | Training program for human overseers | CAIO | [AI Center of Excellence](../../07-enterprise-implementation/organizational-model/ai-center-of-excellence.md) |
| Ability to override or reverse outputs | Art. 14(4)(d) | Override mechanism documented and tested | ML Engineer | [Agent Permission Boundaries](../../03-runtime-governance/agentic-workflows/agent-permission-boundaries.md) |
| Ability to interrupt or stop the system | Art. 14(4)(e) | Kill switch mechanism documented and tested | MLOps Engineer | [Agent Fleet Operations](../../03-runtime-governance/agentic-workflows/agent-fleet-operations.md) |

### 3.7 Accuracy, Robustness, and Cybersecurity (Article 15)

| Requirement | Article Reference | Compliance Evidence | Responsible Role | Framework Artifact |
|------------|------------------|-------------------|-----------------|-------------------|
| Appropriate level of accuracy | Art. 15(1) | Accuracy metrics meeting acceptance criteria | ML Engineer | [Acceptance Criteria](../../01-discovery-governance/evaluations/defining-acceptance-criteria.md) |
| Resilience against errors, faults, inconsistencies | Art. 15(2) | Stress testing and edge case analysis | ML Engineer | [SAFEST S-04, S-05](./safest-checklist-detailed.md) |
| Resilience against adversarial exploitation | Art. 15(3) | Adversarial testing and red-teaming results | Security Engineer | [Red Teaming AI Systems](../guides/red-teaming-ai-systems.md) |
| Technical solutions for AI-specific vulnerabilities | Art. 15(4) | Vulnerability management program | Security Engineer | [Vulnerability Assessment Template](../templates/vulnerability-assessment.md), [AI Vulnerability Management](../guides/ai-vulnerability-management.md) |
| Cybersecurity measures | Art. 15(5) | Security controls implementation | Security Engineer | [Security Threat Model Checklist](../checklists/security-threat-model.yaml) |

---

## 4. Transparency Obligations for Certain AI Systems (Article 50)

### 4.1 Requirement Summary

Article 50 applies to all AI systems (not just high-risk) and imposes transparency requirements:

- **Art. 50(1):** Deployers must inform natural persons that they are interacting with an AI system (unless obvious)
- **Art. 50(2):** Deployers of emotion recognition or biometric categorization must inform persons
- **Art. 50(3):** Users of AI-generated content (deepfakes) must disclose AI involvement
- **Art. 50(4):** AI-generated text on matters of public interest must be labeled as AI-generated

### 4.2 Compliance Mapping

| Requirement | Compliance Evidence | Responsible Role | Framework Artifact |
|------------|-------------------|-----------------|-------------------|
| Inform users they are interacting with AI | AI disclosure in customer-facing interfaces | Product Owner | [Customer-Facing Agent Safety](../../03-runtime-governance/agentic-workflows/customer-facing-agent-safety.md) |
| AI-generated content labeled appropriately | Content labeling in agent outputs | ML Engineer | [Guardrail Deployment Checklist](../../03-runtime-governance/checklists/guardrail-deployment-checklist.yaml) |
| Transparency measures documented | Transparency implementation record | Compliance Officer | [Responsible Product Brief](../../01-discovery-governance/templates/responsible-product-brief.md) |

---

## 5. Obligations of Deployers of High-Risk AI (Article 26)

### 5.1 Compliance Mapping

| Requirement | Article Reference | Compliance Evidence | Responsible Role | Framework Artifact |
|------------|------------------|-------------------|-----------------|-------------------|
| Use high-risk AI in accordance with instructions of use | Art. 26(1) | Documented compliance with provider instructions | Model Owner | [Pre-Deployment Gate](../../02-development-governance/checklists/pre-deployment-gate.yaml) |
| Assign human oversight to competent persons | Art. 26(2) | Named human overseers with documented competency | CAIO | [RACI by AI Lifecycle Stage](../../07-enterprise-implementation/organizational-model/raci-by-ai-lifecycle-stage.md) |
| Ensure input data is relevant and representative | Art. 26(4) | Data quality monitoring in production | Data Engineer | [Data Quality Checklist](../../02-development-governance/checklists/data-quality-checklist.yaml) |
| Monitor operation based on instructions of use | Art. 26(5) | Operational monitoring system | MLOps Engineer | [Model Monitoring Dashboard](../templates/model-monitoring-dashboard.md) |
| Inform provider of serious incidents | Art. 26(5) | Incident reporting process to AI providers | Model Owner | [AI Incident Report Template](../templates/ai-incident-report.md) |
| Conduct FRIA (fundamental rights impact assessment) | Art. 27 | Completed FRIA for credit, insurance, essential services | Compliance Officer | [AI Ethics Impact Assessment](../../01-discovery-governance/templates/ai-ethics-impact-assessment.md) |
| Register in EU database before deployment | Art. 26(8), Art. 49(3) | EU database registration confirmation | Compliance Officer | Registration tracked in [SAFEST Compliance Tracker](./safest-compliance-tracker.yaml) |

---

## 6. Post-Market Monitoring (Article 72)

### 6.1 Compliance Mapping

| Requirement | Article Reference | Compliance Evidence | Responsible Role | Framework Artifact |
|------------|------------------|-------------------|-----------------|-------------------|
| Establish post-market monitoring system | Art. 72(1) | Documented monitoring system proportionate to AI risk | MLOps Engineer + Model Owner | [Monitoring Setup Checklist](../checklists/monitoring-setup-checklist.yaml) |
| Actively and systematically collect, document, and analyze data | Art. 72(2) | Data collection pipelines, analysis reports | MLOps Engineer | [Model Monitoring Dashboard](../templates/model-monitoring-dashboard.md) |
| Monitoring system based on post-market monitoring plan | Art. 72(3) | Written monitoring plan per AI system | Model Owner | [Continuous Online Evaluation](../../03-runtime-governance/evaluations/continuous-online-evaluation.md) |
| Post-market monitoring plan part of technical documentation | Art. 72(3) | Monitoring plan included in model card / technical docs | Model Owner | [Model Card Template](../../02-development-governance/templates/model-card.md) |

---

## 7. Serious Incident Reporting (Article 73)

### 7.1 Compliance Mapping

| Requirement | Article Reference | Compliance Evidence | Responsible Role | Framework Artifact |
|------------|------------------|-------------------|-----------------|-------------------|
| Report serious incidents to market surveillance authorities | Art. 73(1) | Incident reporting process and templates | Compliance Officer | [AI Incident Report Template](../templates/ai-incident-report.md) |
| Report within 15 calendar days of becoming aware | Art. 73(1) | Incident timeline tracking; SLA for regulatory notification | Compliance Officer | [Incident Response Checklist](../checklists/incident-response-checklist.yaml) |
| Immediately report widespread malfunctions | Art. 73(1) subparagraph 2 | Expedited reporting process for systemic issues | CAIO | [AI Incident Report Template](../templates/ai-incident-report.md) |
| Report must contain: nature of incident, corrective actions, unique identifier | Art. 73(4) | Standardized report format aligned with Art. 73(4) fields | Compliance Officer | [AI Incident Report Template](../templates/ai-incident-report.md) |

---

## 8. Quality Management System (Article 17)

### 8.1 Compliance Mapping

| Requirement | Article Reference | Compliance Evidence | Responsible Role | Framework Artifact |
|------------|------------------|-------------------|-----------------|-------------------|
| Establish quality management system | Art. 17(1) | Documented QMS covering AI lifecycle | CAIO | This governance framework as a whole |
| Strategy for regulatory compliance | Art. 17(1)(a) | Regulatory compliance strategy | Compliance Officer | This document + [DORA AI Requirements](./dora-ai-requirements.md) |
| Techniques and procedures for design, development, testing | Art. 17(1)(b) | Development governance procedures | ML Engineer | [Eval-Driven Development](../../02-development-governance/evaluations/eval-driven-development.md) |
| Procedures for data management | Art. 17(1)(c) | Data governance procedures | Data Engineer | [Data Quality Checklist](../../02-development-governance/checklists/data-quality-checklist.yaml) |
| Accountability framework | Art. 17(1)(e) | RACI matrix and governance roles | CAIO | [Governance Roles RACI](../../05-cross-cutting/governance-roles-raci.md) |
| Risk management system | Art. 17(1)(g) | AI risk management system | CAIO | [Risk Tiering Model](../../07-enterprise-implementation/risk-based-adoption/risk-tiering-model.md) |
| Post-market monitoring system | Art. 17(1)(h) | Monitoring system documentation | MLOps Engineer | [Model Monitoring Dashboard](../templates/model-monitoring-dashboard.md) |
| Serious incident reporting procedures | Art. 17(1)(i) | Incident reporting process | Compliance Officer | [Incident Response Checklist](../checklists/incident-response-checklist.yaml) |

---

## 9. Conformity Assessment (Articles 43, 6)

### 9.1 Assessment Route

For most FinTech AI systems classified as high-risk under Annex III Area 5 (credit scoring, creditworthiness), the conformity assessment route is:

- **Internal control procedure** (Annex VI) -- self-assessment by the provider
- **Not** third-party conformity assessment (unless the system involves biometric identification)

### 9.2 Compliance Mapping

| Requirement | Compliance Evidence | Responsible Role | Framework Artifact |
|------------|-------------------|-----------------|-------------------|
| Conformity assessment completed before deployment | Assessment report documenting compliance with Chapter III Section 2 | Compliance Officer + CAIO | All artifacts mapped in Sections 3-8 above |
| EU Declaration of Conformity (Article 47) | Signed declaration following Annex V format | CAIO (authorized signatory) | Produced from compliance evidence in this mapping |
| CE marking affixed (Article 48) | CE marking on AI system or documentation | Compliance Officer | Tracked in [SAFEST Compliance Tracker](./safest-compliance-tracker.yaml) |
| Registration in EU database (Article 49) | Confirmed registration before deployment | Compliance Officer | [SAFEST Compliance Tracker](./safest-compliance-tracker.yaml) |

---

## 10. Compliance Tracking Summary

| EU AI Act Chapter | Key Articles | Compliance Status | Evidence Completeness | Last Review |
|------------------|-------------|-------------------|----------------------|-------------|
| Prohibited Practices | Art. 5 | [ ] Compliant / [ ] Gap / [ ] N/A | ___% | YYYY-MM-DD |
| Risk Classification | Art. 6, Annex III | [ ] Compliant / [ ] Gap / [ ] N/A | ___% | YYYY-MM-DD |
| Risk Management | Art. 9 | [ ] Compliant / [ ] Gap / [ ] N/A | ___% | YYYY-MM-DD |
| Data Governance | Art. 10 | [ ] Compliant / [ ] Gap / [ ] N/A | ___% | YYYY-MM-DD |
| Technical Documentation | Art. 11 | [ ] Compliant / [ ] Gap / [ ] N/A | ___% | YYYY-MM-DD |
| Record-Keeping | Art. 12 | [ ] Compliant / [ ] Gap / [ ] N/A | ___% | YYYY-MM-DD |
| Transparency | Art. 13, Art. 50 | [ ] Compliant / [ ] Gap / [ ] N/A | ___% | YYYY-MM-DD |
| Human Oversight | Art. 14 | [ ] Compliant / [ ] Gap / [ ] N/A | ___% | YYYY-MM-DD |
| Accuracy/Robustness | Art. 15 | [ ] Compliant / [ ] Gap / [ ] N/A | ___% | YYYY-MM-DD |
| Deployer Obligations | Art. 26-27 | [ ] Compliant / [ ] Gap / [ ] N/A | ___% | YYYY-MM-DD |
| Quality Management | Art. 17 | [ ] Compliant / [ ] Gap / [ ] N/A | ___% | YYYY-MM-DD |
| Conformity Assessment | Art. 43 | [ ] Compliant / [ ] Gap / [ ] N/A | ___% | YYYY-MM-DD |
| Post-Market Monitoring | Art. 72 | [ ] Compliant / [ ] Gap / [ ] N/A | ___% | YYYY-MM-DD |
| Incident Reporting | Art. 73 | [ ] Compliant / [ ] Gap / [ ] N/A | ___% | YYYY-MM-DD |

---

## Cross-References

- [DORA AI Requirements](./dora-ai-requirements.md) -- companion regulatory mapping for DORA obligations specific to AI
- [SAFEST Checklist Detailed](./safest-checklist-detailed.md) -- DNB-specific checklist that operationalizes many EU AI Act requirements
- [EU AI Act Risk Classification Checklist](../../01-discovery-governance/checklists/eu-ai-act-risk-classification.yaml) -- decision tree for Art. 6 / Annex III classification
- [Governance Roles RACI](../../05-cross-cutting/governance-roles-raci.md) -- authoritative role definitions referenced throughout this mapping
- [Regulatory Reference Index](../../05-cross-cutting/regulatory-reference-index.md) -- master index of all regulatory references across the framework
- [Quarterly Governance Report](../../06-executive/quarterly-governance-report.md) -- template for reporting compliance posture to the board
- [Governance Dashboard Specification](../../06-executive/governance-dashboard-spec.md) -- dashboard that visualizes compliance status from this mapping
- [Three Lines of Defense for AI](../../07-enterprise-implementation/organizational-model/three-lines-of-defense-for-ai.md) -- governance model underlying the RACI assignments in this mapping

---

*Last updated: 2026-03-01* / *Version: 1.0* / *Classification: Internal / Regulatory Preparation*
