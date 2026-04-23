# DORA Requirements for AI Systems

## Purpose

This document maps the Digital Operational Resilience Act (DORA -- Regulation (EU) 2022/2554) requirements to AI-specific controls, treating AI models as ICT assets, AI agents as ICT services, and LLM providers as third-party ICT service providers. DORA does not explicitly mention AI, but its broad scope covering all ICT systems used by financial entities encompasses AI systems entirely. This mapping makes the implicit explicit: for every DORA chapter, it identifies the AI-specific interpretation, the controls required, and the framework artifacts that provide compliance evidence.

For FinTech companies deploying business AI agents in regulated financial services, DORA creates binding operational resilience obligations that overlay the EU AI Act's safety and rights-based requirements. Where the EU AI Act asks "is this AI system safe and fair?", DORA asks "will this AI system remain available, secure, and recoverable when things go wrong?"

## When to Use

- When assessing DORA compliance for AI systems during the deployment gate review
- When designing operational resilience for AI infrastructure (failover, rollback, disaster recovery)
- When onboarding a new LLM provider or AI cloud service and assessing third-party risk
- When preparing the Register of Information (Art. 28(3)) for DNB submission
- When designing incident reporting processes for AI-related ICT incidents
- When planning resilience testing (including threat-led penetration testing) for AI systems
- When reporting to the board on operational resilience of AI systems

## Who Is Responsible

| Role | R | A | C | I |
|------|---|---|---|---|
| **CISO / ICT Risk Manager** | X | | | | Owns the DORA compliance program; integrates AI into ICT risk management |
| **CAIO** | | X | | | Accountable for ensuring AI systems meet DORA requirements; co-owns with CISO |
| **MLOps / Platform Engineer** | X | | | | Implements resilience controls for AI infrastructure |
| **Model Owner** | | | X | | Consulted on system-specific resilience requirements and RTO/RPO targets |
| **Compliance Officer (2nd Line)** | | | X | | Validates DORA compliance evidence; coordinates DNB reporting |
| **Internal Audit (3rd Line)** | | | | X | Independently assesses DORA compliance for AI systems |
| **Board / Management Body** | | | | X | Informed of DORA compliance posture; ultimately accountable per Art. 5(2) |

## Regulatory Basis

- **DORA (Regulation (EU) 2022/2554)** -- Primary regulation mapped in this document
- **SAFEST items S-14, S-15, S-16, S-17, S-18, S-19a-d** -- DNB SAFEST items that operationalize DORA for AI
- **EU AI Act Articles 9, 15, 72** -- Cross-referenced where AI resilience overlaps with EU AI Act robustness requirements
- **DNB Good Practice for AI** -- Supervisory expectations for AI in financial services aligned with DORA
- **EBA ITS on Register of Information (Commission Implementing Regulation (EU) 2025/302)** -- Template format for Art. 28(3) Register

---

## 1. ICT Risk Management Framework (Articles 5-16)

### 1.1 AI as ICT: The Mapping Principle

DORA defines ICT broadly: "digital and data technologies encompassing all systems, processes, and resources used to manage information" (Art. 3(1)). AI systems fall within this definition:

| DORA Concept | AI Equivalent | Implication |
|-------------|--------------|-------------|
| ICT system | AI model + inference infrastructure + data pipeline | AI systems are ICT systems; all ICT risk management requirements apply |
| ICT service | AI agent capability (e.g., fraud detection, customer service) | AI agents are ICT services; resilience and continuity requirements apply |
| ICT asset | Trained model weights, training data, prompt templates, agent configurations | Must be inventoried, classified, and protected |
| ICT-related incident | AI failure, drift-induced degradation, prompt injection exploit, agent malfunction | Must be detected, reported, and remediated per DORA timelines |
| Third-party ICT service provider | LLM API provider (OpenAI, Anthropic, Google), cloud AI platform (Azure AI, AWS SageMaker), MLOps tool provider | Third-party risk management and Register of Information requirements apply |

### 1.2 Governance of ICT Risk (Article 5)

| Requirement | AI-Specific Control | Compliance Evidence | Framework Artifact |
|------------|---------------------|-------------------|-------------------|
| Management body defines, approves, oversees ICT risk management framework | Board approves AI risk appetite; CAIO reports AI ICT risk | Board minutes documenting AI risk approval | [Board-Level AI Accountability](../../07-enterprise-implementation/organizational-model/board-level-ai-accountability.md) |
| Management body bears ultimate responsibility for ICT risk | Board accountable for AI operational resilience | AI governance in board charter | [AI Governance Committee Charter](../../07-enterprise-implementation/organizational-model/ai-governance-committee-charter.md) |
| Adequate budget for ICT security and resilience | Dedicated budget for AI monitoring, testing, resilience | Budget allocation documented | [CAIO role](../../05-cross-cutting/governance-roles-raci.md) -- budget mandate |
| ICT risk management framework documented and reviewed annually | AI-inclusive ICT risk framework reviewed annually | Documented framework with review log | [Risk Tiering Model](../../07-enterprise-implementation/risk-based-adoption/risk-tiering-model.md) |

### 1.3 ICT Risk Management (Articles 6-7)

| Requirement | Article | AI-Specific Control | Framework Artifact |
|------------|---------|---------------------|-------------------|
| Comprehensive ICT risk management framework | Art. 6(1) | AI systems included in enterprise ICT risk register | [SAFEST S-01](./safest-checklist-detailed.md) -- AI system inventory |
| Identify all ICT assets and their dependencies | Art. 6(2) | Map AI model dependencies (data sources, APIs, compute, third-party models) | [Model Card Template](../../02-development-governance/templates/model-card.md) |
| Continuous identification of ICT risk sources | Art. 6(3) | Continuous monitoring of AI-specific risks (drift, adversarial, bias) | [Model Monitoring Dashboard](../templates/model-monitoring-dashboard.md) |
| Proportionate ICT risk management | Art. 6(5) | Risk-proportionate controls based on AI risk tier | [Risk Tiering Model](../../07-enterprise-implementation/risk-based-adoption/risk-tiering-model.md) |
| Simplified framework for qualifying entities | Art. 7 | Reduced requirements for smaller FinTechs meeting Art. 7 criteria | [Minimum Viable Governance](../../07-enterprise-implementation/risk-based-adoption/minimum-viable-governance.md) |

### 1.4 Identification (Article 8)

| Requirement | AI-Specific Control | Compliance Evidence | Framework Artifact |
|------------|---------------------|-------------------|-------------------|
| Identify, classify, document all ICT assets | Maintain AI system inventory with model versions, dependencies, risk tiers | AI system registry | [SAFEST S-01](./safest-checklist-detailed.md) |
| Identify all ICT-supported business functions | Map AI agents to business functions (fraud detection, customer service, AML, credit scoring) | Business function mapping | [Responsible Product Brief](../../01-discovery-governance/templates/responsible-product-brief.md) |
| Identify sources of ICT risk | AI-specific risk identification: model failure, data poisoning, prompt injection, agent malfunction, vendor lock-in | Risk assessment per AI system | [AI Ethics Impact Assessment](../../01-discovery-governance/templates/ai-ethics-impact-assessment.md) |
| Perform ICT risk assessment at least annually | Annual AI risk assessment covering all production systems | Annual assessment report | [Periodic Revalidation Schedule](../evaluations/periodic-revalidation-schedule.yaml) |

### 1.5 Protection and Prevention (Article 9)

| Requirement | AI-Specific Control | Compliance Evidence | Framework Artifact |
|------------|---------------------|-------------------|-------------------|
| Implement ICT security policies | AI security policies covering model access, data access, prompt security, agent permissions | Security policy documentation | [Security Threat Model Checklist](../checklists/security-threat-model.yaml) |
| Access control and authentication | Model API access control; agent permission boundaries; principle of least privilege for tool access | Access control implementation | [Agent Permission Boundaries](../../03-runtime-governance/agentic-workflows/agent-permission-boundaries.md) |
| ICT change management | Model versioning; prompt template versioning; configuration management for agent deployments | Change management records | [Change Management for AI](../../07-enterprise-implementation/process-integration/change-management-for-ai.md) |
| Patch management | Model updates; guardrail updates; vulnerability remediation for AI components | Patch/update records | [AI Vulnerability Management](../guides/ai-vulnerability-management.md) |

### 1.6 Detection (Article 10)

| Requirement | AI-Specific Control | Compliance Evidence | Framework Artifact |
|------------|---------------------|-------------------|-------------------|
| Detect anomalous activities promptly | AI monitoring for drift, performance degradation, anomalous agent behavior, security events | Monitoring dashboard with alerting | [Model Monitoring Dashboard](../templates/model-monitoring-dashboard.md) |
| Multiple layers of control | Layered detection: guardrail triggers, performance monitoring, drift detection, security monitoring | Detection architecture documented | [Monitoring Setup Checklist](../checklists/monitoring-setup-checklist.yaml) |
| Detection mechanisms enabling multi-source analysis | Correlation of AI metrics with infrastructure, security, and business metrics | Integrated monitoring platform | [Eval Reporting Dashboard](../evaluations/eval-reporting-dashboard.md) |

### 1.7 Response and Recovery (Articles 11-12)

| Requirement | Article | AI-Specific Control | Framework Artifact |
|------------|---------|---------------------|-------------------|
| ICT business continuity policy | Art. 11(1) | AI-specific continuity: fallback procedures, manual alternatives, degraded mode | [SAFEST S-13, S-17](./safest-checklist-detailed.md) |
| Recovery plans with RTO and RPO | Art. 11(2) | Model rollback RTO; data pipeline recovery RPO; agent failover time | [SAFEST S-14, S-16](./safest-checklist-detailed.md) |
| Impact analysis of severe disruptions | Art. 11(4) | Payment chain impact analysis for AI failure scenarios | [SAFEST S-15](./safest-checklist-detailed.md) |
| Test business continuity plans | Art. 11(6) | Periodic DR tests including AI model rollback and failover | [Regression Testing for AI](../evaluations/regression-testing-for-ai.md) |
| Learning and evolving from incidents | Art. 12(1) | Post-incident review with governance process improvements | [AI Incident Report Template](../templates/ai-incident-report.md) |
| Communication plans for ICT disruptions | Art. 12(2) | Communication templates for AI incidents (internal, regulatory, customer) | [Drift Detection Runbook](../templates/drift-detection-runbook.md) -- Section 7 |

### 1.8 ICT Logging (Articles 13-14)

| Requirement | Article | AI-Specific Control | Framework Artifact |
|------------|---------|---------------------|-------------------|
| Logging policies for ICT operations | Art. 13(1) | AI request/response logging; agent action logging; tool invocation logging | [Traceability with LangChain](../guides/traceability-with-langchain.md) |
| Log retention appropriate to business activity | Art. 13(2) | AI log retention: 90 days hot, 2 years cold minimum | [Monitoring Setup Checklist](../checklists/monitoring-setup-checklist.yaml) |
| Logs available for supervisory review | Art. 13(3) | AI audit trail accessible for DNB inspection | [Model Monitoring Dashboard](../templates/model-monitoring-dashboard.md) -- Section 1.2 |

---

## 2. ICT-Related Incident Management (Articles 17-23)

### 2.1 Incident Classification for AI Systems

| DORA Incident Criteria (Art. 18) | AI-Specific Interpretation | Example |
|--------------------------------|---------------------------|---------|
| Number of clients affected | Users receiving degraded or incorrect AI outputs | Fraud model fails to flag 500 fraudulent transactions |
| Duration of the incident | Time from AI malfunction to resolution/rollback | Agent provides incorrect financial guidance for 4 hours before detection |
| Geographical spread | Regions affected by AI failure | Regional model serving incorrect results due to localized data drift |
| Data losses | Customer data exposed through AI system | Prompt injection extracts PII from agent context window |
| Impact on financial services | Disruption to AI-supported financial processes | Credit scoring AI unavailable; loan applications cannot be processed |
| Economic impact | Financial losses from AI malfunction | Incorrect fraud scoring leads to approved fraudulent transactions |

### 2.2 Incident Reporting Timeline (Article 19)

| Report | Deadline | AI-Specific Content | Framework Artifact |
|--------|----------|---------------------|-------------------|
| **Initial notification** | 4 hours after classifying as major | AI system affected, scope of impact, immediate response actions | [AI Incident Report Template](../templates/ai-incident-report.md) -- Part 1 |
| **Intermediate report** | 72 hours after initial | Root cause analysis (if available), remediation plan, model rollback status | [AI Incident Report Template](../templates/ai-incident-report.md) -- Part 2 |
| **Final report** | 1 month after initial | Complete root cause analysis, corrective actions, governance improvements | [AI Incident Report Template](../templates/ai-incident-report.md) -- Part 3 |

### 2.3 Compliance Mapping

| Requirement | Article | AI-Specific Control | Framework Artifact |
|------------|---------|---------------------|-------------------|
| Establish incident management process | Art. 17(1) | AI incident detection, classification, escalation, and resolution procedures | [Incident Response Checklist](../checklists/incident-response-checklist.yaml) |
| Classify ICT-related incidents | Art. 18 | AI incident severity classification (P1-P4) with AI-specific criteria | [Model Monitoring Dashboard](../templates/model-monitoring-dashboard.md) -- Section 4.1 |
| Report major ICT-related incidents | Art. 19 | Regulatory notification for major AI incidents within DORA timelines | [AI Incident Report Template](../templates/ai-incident-report.md) |
| Significant cyber threats reporting | Art. 19a | Report AI-specific threats (novel attack vectors, zero-day in LLM providers) | [Vulnerability Assessment Template](../templates/vulnerability-assessment.md) |
| Centralized incident logging | Art. 21 | AI incident register as part of enterprise ICT incident log | [SAFEST Compliance Tracker](./safest-compliance-tracker.yaml) |
| Post-incident review | Art. 22 | Root cause analysis and governance process improvement after AI incidents | [AI Incident Report Template](../templates/ai-incident-report.md) -- post-mortem section |

---

## 3. Digital Operational Resilience Testing (Articles 24-27)

### 3.1 General Testing Requirements (Article 24-25)

| Requirement | Article | AI-Specific Control | Framework Artifact |
|------------|---------|---------------------|-------------------|
| Establish ICT testing program | Art. 24(1) | AI-specific testing program: model validation, adversarial testing, resilience testing | [Test Plan for AI](../../02-development-governance/templates/test-plan-for-ai.md) |
| Proportionate testing approach | Art. 24(2) | Risk-proportionate testing intensity based on AI risk tier | [Risk Tiering Model](../../07-enterprise-implementation/risk-based-adoption/risk-tiering-model.md) |
| Testing by independent parties | Art. 24(4) | Independent model validation (2nd line of defense) | [SAFEST S-19](./safest-checklist-detailed.md) -- independent validation |
| Vulnerability assessments | Art. 25(1)(a) | AI-specific vulnerability assessment covering OWASP Top 10 for LLMs and AVID taxonomy | [Vulnerability Assessment Template](../templates/vulnerability-assessment.md) |
| Network security assessments | Art. 25(1)(b) | API security testing for AI endpoints; inter-agent communication security | [Security Threat Model Checklist](../checklists/security-threat-model.yaml) |
| Penetration testing | Art. 25(1)(e) | Red-teaming AI systems: prompt injection, jailbreaking, data extraction attempts | [Red Teaming AI Systems](../guides/red-teaming-ai-systems.md) |
| Source code reviews | Art. 25(1)(f) | Review of agent orchestration code, guardrail implementations, tool integration code | [Verification Before Deployment](../../02-development-governance/guides/verification-before-deployment.md) |
| Scenario-based testing | Art. 25(1)(g) | AI failure scenario testing: model unavailability, drift events, adversarial attacks, agent loops | [Regression Testing for AI](../evaluations/regression-testing-for-ai.md) |

### 3.2 Threat-Led Penetration Testing (Article 26-27)

Applicable to financial entities identified by competent authorities for advanced testing.

| Requirement | Article | AI-Specific Control | Framework Artifact |
|------------|---------|---------------------|-------------------|
| TLPT covering critical functions | Art. 26(1) | TLPT scope includes AI systems supporting critical financial functions | [Red Teaming AI Systems](../guides/red-teaming-ai-systems.md) |
| TLPT at least every 3 years | Art. 26(1) | AI red-teaming schedule aligned with TLPT cycle | [Periodic Revalidation Schedule](../evaluations/periodic-revalidation-schedule.yaml) |
| Testing must include ICT third-party service providers | Art. 26(3) | TLPT must include testing of LLM provider interfaces and attack surface | [Red Teaming AI Systems](../guides/red-teaming-ai-systems.md) |
| TLPT performed by qualified testers | Art. 27 | AI red team members must have AI/ML adversarial expertise | [AI Center of Excellence](../../07-enterprise-implementation/organizational-model/ai-center-of-excellence.md) |

---

## 4. Third-Party ICT Risk Management (Articles 28-44)

### 4.1 AI Third-Party Landscape

| Third-Party Category | DORA Classification | Examples | Risk Level |
|---------------------|---------------------|----------|------------|
| **LLM API Provider** | ICT third-party service provider | OpenAI, Anthropic, Google (Gemini), Mistral | Critical -- if supporting core financial functions |
| **Cloud AI Platform** | ICT third-party service provider | Azure AI, AWS SageMaker, GCP Vertex AI | Critical -- compute and inference infrastructure |
| **Pre-trained Model Provider** | ICT third-party service provider | Hugging Face model downloads, domain-specific model vendors | High -- model supply chain risk |
| **MLOps Platform** | ICT third-party service provider | Weights & Biases, MLflow (hosted), DataRobot | High -- development and deployment tooling |
| **Training Data Provider** | ICT third-party service provider | Data vendors, annotation services, synthetic data providers | High -- data quality and provenance |
| **Guardrail / Safety Tool** | ICT third-party service provider | NeMo Guardrails (hosted), content moderation APIs | High -- safety-critical dependency |
| **Evaluation Service** | ICT third-party service provider | LLM evaluation platforms, bias testing services | Medium -- quality assurance tooling |

### 4.2 Contractual Requirements (Article 28, 30)

| Requirement | Article | AI-Specific Interpretation | Framework Artifact |
|------------|---------|---------------------------|-------------------|
| Written contractual arrangements | Art. 28(2) | Contracts with LLM providers must cover DORA requirements | [SAFEST S-19a](./safest-checklist-detailed.md) |
| Risk assessment before contracting | Art. 28(4) | AI vendor risk assessment covering model quality, security, availability, lock-in | [Pre-Deployment Gate](../../02-development-governance/checklists/pre-deployment-gate.yaml) |
| Register of Information | Art. 28(3) | All AI third-party arrangements registered in the Register of Information per EBA ITS format | [SAFEST S-19a-d](./safest-checklist-detailed.md) |
| Concentration risk assessment | Art. 29 | Assess dependency on single LLM provider; document fallback providers | [Agent Fleet Operations](../../03-runtime-governance/agentic-workflows/agent-fleet-operations.md) |
| Service level descriptions | Art. 30(2)(a) | SLAs for model API availability, latency, throughput, rate limits | Vendor contracts |
| Data processing locations | Art. 30(2)(b) | Where LLM inference occurs (EU/EEA/third country); GDPR adequacy | Vendor contracts + DPIA |
| Subcontracting chain | Art. 30(2)(e) | LLM provider's own dependencies (compute provider, data center, CDN) | [SAFEST S-19c](./safest-checklist-detailed.md) |
| Audit and access rights | Art. 30(2)(f) | Right to audit LLM provider's AI infrastructure and practices | Vendor contracts |
| Exit strategy | Art. 30(2)(g) | Plan for migrating off a specific LLM provider with defined timeline | Exit strategy document per AI system |
| Incident notification | Art. 30(2)(h) | LLM provider must notify of incidents affecting the AI service | Vendor contracts |

### 4.3 Key Contractual Clauses for LLM Providers

When contracting with LLM API providers, ensure the following AI-specific clauses are included:

| Clause | Purpose | DORA Reference |
|--------|---------|----------------|
| **Model version notification** | Provider must notify before deprecating or changing a model version | Art. 30(2)(a) |
| **Performance SLA** | Defined latency, throughput, and availability targets with penalties | Art. 30(2)(a) |
| **Data processing commitment** | No use of customer data for model training without explicit consent | Art. 30(2)(b), GDPR |
| **Inference location** | Inference executed within EU/EEA or approved jurisdictions | Art. 30(2)(b) |
| **Security incident notification** | Provider notifies within 24 hours of security incidents affecting the service | Art. 30(2)(h) |
| **Audit rights** | Right to audit or require SOC 2 / ISO 27001 reports | Art. 30(2)(f) |
| **Sub-processor disclosure** | Full disclosure of compute providers and data center locations | Art. 30(2)(e) |
| **Exit assistance** | Transition period and data export upon contract termination | Art. 30(2)(g) |
| **Model behavior commitment** | Commitment to maintain model behavior within defined parameters between versions | AI-specific best practice |
| **Content filtering transparency** | Disclosure of content filtering or safety layers that may affect output | AI-specific best practice |

### 4.4 Register of Information (Article 28(3))

The Register must include AI-specific entries per SAFEST S-19a-d:

| Register Field | AI-Specific Guidance |
|---------------|---------------------|
| **Service Provider ID** | LEI code of LLM provider entity |
| **Service Description** | Specific AI service (e.g., "GPT-4o inference API for customer support agent") |
| **Function Supported** | Financial function supported (e.g., "customer complaint resolution", "fraud alert investigation") |
| **Criticality Assessment** | Critical if AI supports core payment, credit, or AML functions |
| **Data Sensitivity** | Classification of data processed by the AI service |
| **Substitutability Assessment** | Can this AI service be replaced by another provider within the exit timeline? |
| **Subcontracting Chain** | Full chain from LLM provider to compute provider to data center operator |

---

## 5. DORA-AI Compliance Tracking Summary

| DORA Chapter | Key Articles | AI-Specific Focus | Compliance Status | Last Review |
|-------------|-------------|-------------------|-------------------|-------------|
| Governance | Art. 5 | Board accountability for AI risk | [ ] Compliant / [ ] Gap | YYYY-MM-DD |
| ICT Risk Management | Art. 6-9 | AI in ICT risk framework | [ ] Compliant / [ ] Gap | YYYY-MM-DD |
| Detection | Art. 10 | AI monitoring and alerting | [ ] Compliant / [ ] Gap | YYYY-MM-DD |
| Response & Recovery | Art. 11-12 | AI rollback, fallback, continuity | [ ] Compliant / [ ] Gap | YYYY-MM-DD |
| Logging | Art. 13-14 | AI audit trail and traceability | [ ] Compliant / [ ] Gap | YYYY-MM-DD |
| Incident Management | Art. 17-18 | AI incident classification | [ ] Compliant / [ ] Gap | YYYY-MM-DD |
| Incident Reporting | Art. 19-23 | AI incident notification | [ ] Compliant / [ ] Gap | YYYY-MM-DD |
| Resilience Testing | Art. 24-25 | AI adversarial testing | [ ] Compliant / [ ] Gap | YYYY-MM-DD |
| TLPT | Art. 26-27 | AI red-teaming | [ ] Compliant / [ ] Gap | YYYY-MM-DD |
| Third-Party Risk | Art. 28-30 | LLM provider management | [ ] Compliant / [ ] Gap | YYYY-MM-DD |
| Register of Information | Art. 28(3) | AI third-party registry | [ ] Compliant / [ ] Gap | YYYY-MM-DD |
| Concentration Risk | Art. 29 | LLM provider concentration | [ ] Compliant / [ ] Gap | YYYY-MM-DD |

---

## Cross-References

- [EU AI Act Compliance Mapping](./eu-ai-act-compliance-mapping.md) -- companion regulatory mapping for EU AI Act obligations
- [SAFEST Checklist Detailed](./safest-checklist-detailed.md) -- DNB checklist with DORA-specific items (S-14 through S-19d)
- [Model Monitoring Dashboard](../templates/model-monitoring-dashboard.md) -- operational monitoring that satisfies DORA Art. 10 detection requirements
- [AI Incident Report Template](../templates/ai-incident-report.md) -- incident documentation aligned with DORA Art. 17-19 reporting requirements
- [Vulnerability Assessment Template](../templates/vulnerability-assessment.md) -- vulnerability documentation for DORA Art. 25 testing requirements
- [Red Teaming AI Systems](../guides/red-teaming-ai-systems.md) -- adversarial testing procedures for DORA Art. 25-27
- [Agent Fleet Operations](../../03-runtime-governance/agentic-workflows/agent-fleet-operations.md) -- operational resilience for multi-agent systems
- [Three Lines of Defense for AI](../../07-enterprise-implementation/organizational-model/three-lines-of-defense-for-ai.md) -- governance model underlying DORA compliance structure
- [Regulatory Reference Index](../../05-cross-cutting/regulatory-reference-index.md) -- master index of all regulatory references across the framework
- [Board-Level AI Accountability](../../07-enterprise-implementation/organizational-model/board-level-ai-accountability.md) -- board oversight responsibilities per DORA Art. 5

---

*Last updated: 2026-03-01* / *Version: 1.0* / *Classification: Internal / Regulatory Preparation*
