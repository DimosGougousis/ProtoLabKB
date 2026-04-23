# Model Card Template

## Purpose

This template provides a standardized format for documenting AI models and LLM-based systems deployed within the organization. Model cards are a primary governance artifact: they capture what a model is, what it does, how well it performs, what risks it carries, and how it is maintained. Completed model cards are required for the [Pre-Deployment Gate](../checklists/pre-deployment-gate.yaml) and serve as living documents throughout the model's operational lifecycle.

This template is designed for both traditional ML models (classifiers, regression models, ranking systems) and LLM-based systems (chatbots, agents, RAG pipelines, content generators). Sections marked with **(LLM)** are specifically relevant to LLM-based systems; sections marked with **(ML)** are specifically relevant to traditional ML. All other sections apply universally.

## When to Use

- When deploying any new AI model or LLM-based system (required before the Pre-Deployment Gate)
- When making material changes to an existing model (new version, new training data, modified prompts)
- During periodic revalidation (see [Continuous Online Evaluation](../../03-runtime-governance/evaluations/continuous-online-evaluation.md))
- When onboarding a third-party AI model or API
- When the AI Governance Committee reviews a model for deployment approval

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **Model Owner** | **Accountable** -- ensures the model card is complete, accurate, and current |
| **AI/ML Engineer** | **Responsible** -- fills in technical sections (architecture, performance, limitations) |
| **Product Manager** | **Consulted** -- validates intended use, out-of-scope uses, and product context |
| **Compliance Officer** | **Reviewer** -- validates regulatory compliance sections |
| **AI Governance Committee** | **Approver** -- reviews model card as part of deployment approval (limited/high risk) |

## Regulatory Basis

- **EU AI Act Article 11** -- Technical documentation requirements for high-risk AI systems
- **EU AI Act Article 13** -- Transparency requirements, including information about AI system capabilities and limitations
- **EU AI Act Annex IV** -- Detailed documentation requirements
- **DORA Article 9** -- ICT risk management framework documentation
- **SAFEST item T-12** -- Model card / model documentation requirement
- **DNB Good Practice** -- Model documentation as part of model risk management

---

## Template Instructions

- Replace all `[FILL IN]` placeholders with actual information
- Delete sections marked **(LLM)** if this is a traditional ML model, or **(ML)** if this is an LLM system
- For multi-model systems (e.g., a RAG pipeline with an embedding model and a generation model), create one model card for the overall system and reference sub-model cards if needed
- Store completed model cards in the model registry alongside the model artifacts
- Update the model card with every material change; maintain a version history

---

# Model Card: [FILL IN: Model/System Name]

## Document Metadata

| Field | Value |
|-------|-------|
| **Model Card Version** | [FILL IN: e.g., 1.0] |
| **Last Updated** | [FILL IN: YYYY-MM-DD] |
| **Author(s)** | [FILL IN: Names and roles] |
| **Reviewer(s)** | [FILL IN: Names and roles] |
| **Approval Status** | [Draft / Under Review / Approved / Superseded] |
| **Next Review Date** | [FILL IN: YYYY-MM-DD] |

---

## 1. Model Details

| Field | Value |
|-------|-------|
| **Model Name** | [FILL IN] |
| **Model Version** | [FILL IN: Semantic version, e.g., 2.1.0] |
| **Model Type** | [FILL IN: Classification / Regression / Generative (LLM) / Agent / RAG Pipeline / Multi-Agent System / Other] |
| **Architecture** | [FILL IN: e.g., "XGBoost classifier", "Fine-tuned GPT-4o", "LangGraph agent with Claude 3.5 Sonnet backbone"] |
| **Base Model** | [FILL IN: For LLM systems, specify the foundation model and version, e.g., "Claude 3.5 Sonnet (anthropic, 2024-10-22)"] |
| **Framework** | [FILL IN: e.g., scikit-learn, PyTorch, LangChain, LangGraph, custom] |
| **Model Size** | [FILL IN: Parameter count for ML models; for LLM systems, note if using an API or self-hosted] |
| **Input Format** | [FILL IN: What the model accepts as input] |
| **Output Format** | [FILL IN: What the model produces as output] |
| **Risk Classification** | [FILL IN: Minimal / Limited / High / Unacceptable, per EU AI Act Risk Classification](../../01-discovery-governance/checklists/eu-ai-act-risk-classification.yaml) |
| **SAFEST Classification** | [FILL IN: Reference SAFEST checklist items that apply] |

### 1.1 System Architecture (for multi-component systems)

```
[FILL IN: Diagram or description of the system architecture.
For agentic systems, show the agent orchestration flow, tool connections,
and guardrail positions. Example:]

User Query --> Input Guardrail --> Router Agent --> [Tool A | Tool B | Knowledge Base]
                                        |
                                        v
                                   Response Generator --> Output Guardrail --> User
```

---

## 2. Intended Use

### 2.1 Primary Use Cases

| Use Case | Description | Target Users |
|----------|-------------|-------------|
| [FILL IN] | [FILL IN: What the model does in this use case] | [FILL IN: Who uses it] |
| [FILL IN] | [FILL IN] | [FILL IN] |

### 2.2 Intended Users and Context

- **End users:** [FILL IN: e.g., "Dutch retail banking customers via mobile app chat interface"]
- **Internal users:** [FILL IN: e.g., "Customer service agents using the AI assistant"]
- **Operating environment:** [FILL IN: e.g., "Production cloud environment, 24/7 availability, customer-facing"]
- **Decision authority:** [FILL IN: "Fully autonomous" / "Human-in-the-loop" / "Human-on-the-loop" / "Advisory only"]
- **Human escalation criteria:** [FILL IN: When must the system escalate to a human?]

### 2.3 Out-of-Scope Uses

The following uses are explicitly **not supported** and may produce unreliable or harmful results:

| Out-of-Scope Use | Why It Is Out of Scope | Mitigation |
|------------------|----------------------|-----------|
| [FILL IN: e.g., "Providing personalized investment advice"] | [FILL IN: e.g., "Model is not trained on investment data; regulatory requirements not met"] | [FILL IN: e.g., "Guardrail blocks investment advice queries; escalates to licensed advisor"] |
| [FILL IN] | [FILL IN] | [FILL IN] |

---

## 3. Training Data (ML) / Knowledge Base and Prompts (LLM)

### 3.1 Training Data (ML)

| Field | Value |
|-------|-------|
| **Dataset Name** | [FILL IN] |
| **Data Card Reference** | [FILL IN: Link to data card if available] |
| **Dataset Size** | [FILL IN: Number of samples, features] |
| **Date Range** | [FILL IN: Time period covered by training data] |
| **Data Sources** | [FILL IN: Where the data comes from] |
| **Preprocessing Steps** | [FILL IN: Key preprocessing and feature engineering] |
| **Known Data Limitations** | [FILL IN: Missing groups, historical biases, collection biases] |
| **Data Governance** | [FILL IN: GDPR compliance, consent basis, retention policy] |

### 3.2 Knowledge Base (LLM)

| Field | Value |
|-------|-------|
| **Knowledge Sources** | [FILL IN: e.g., "Bank product documentation, FAQ database, regulatory text"] |
| **Knowledge Base Size** | [FILL IN: Number of documents, total tokens] |
| **Update Frequency** | [FILL IN: How often the knowledge base is refreshed] |
| **Embedding Model** | [FILL IN: Model used for vectorization] |
| **Retrieval Strategy** | [FILL IN: e.g., "Hybrid search (semantic + keyword), top-5 retrieval"] |

### 3.3 Prompt Architecture (LLM)

| Component | Description | Version |
|-----------|-------------|---------|
| **System Prompt** | [FILL IN: Summary of system prompt purpose and key instructions] | [FILL IN: Version/hash] |
| **Few-Shot Examples** | [FILL IN: Number and type of examples included] | [FILL IN] |
| **Tool Definitions** | [FILL IN: Tools available to the agent and their descriptions] | [FILL IN] |
| **Guardrail Prompts** | [FILL IN: Safety-specific prompt components] | [FILL IN] |

---

## 4. Evaluation Results

### 4.1 Performance Metrics

Results from the eval suite as defined in [Eval-Driven Development](../evaluations/eval-driven-development.md).

| Metric | Value | Threshold | Pass/Fail | Eval Dataset |
|--------|-------|-----------|-----------|-------------|
| [FILL IN: e.g., "Accuracy"] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |
| [FILL IN: e.g., "Faithfulness"] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |
| [FILL IN: e.g., "Latency P95"] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |

For LLM-specific evaluation patterns used, see [LLM Eval Patterns](../evaluations/llm-eval-patterns.md).

### 4.2 Fairness Metrics

Results from the fairness evaluation suite as defined in [Bias and Fairness Evals](../evaluations/bias-and-fairness-evals.md).

| Protected Attribute | Metric | Value | Threshold | Pass/Fail |
|--------------------|--------|-------|-----------|-----------|
| [FILL IN] | Disparate Impact Ratio | [FILL IN] | >= 0.85 | [FILL IN] |
| [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |

**Bias Assessment Report:** [FILL IN: Link to completed bias assessment report]

### 4.3 Safety Evaluation Results

| Safety Dimension | Test | Result | Threshold | Pass/Fail |
|-----------------|------|--------|-----------|-----------|
| Toxicity | [FILL IN: Test description] | [FILL IN] | [FILL IN] | [FILL IN] |
| Jailbreak Resistance | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |
| Policy Compliance | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |
| PII Leakage | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |

### 4.4 Adversarial Testing Results (High Risk Only)

| Attack Type | Number of Tests | Success Rate (attacker) | Threshold | Pass/Fail |
|------------|----------------|------------------------|-----------|-----------|
| [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |

---

## 5. Ethical Considerations

### 5.1 Potential Harms

| Harm Category | Description | Likelihood | Severity | Mitigation |
|--------------|-------------|-----------|----------|-----------|
| [FILL IN: e.g., "Discriminatory credit decisions"] | [FILL IN] | [Low/Medium/High] | [Low/Medium/High/Critical] | [FILL IN] |
| [FILL IN: e.g., "Hallucinated financial information"] | [FILL IN] | [Low/Medium/High] | [Low/Medium/High/Critical] | [FILL IN] |
| [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |

### 5.2 Stakeholder Impact

| Stakeholder | Positive Impact | Negative Impact | Mitigation |
|------------|----------------|-----------------|-----------|
| **Customers** | [FILL IN] | [FILL IN] | [FILL IN] |
| **Employees** | [FILL IN] | [FILL IN] | [FILL IN] |
| **Society** | [FILL IN] | [FILL IN] | [FILL IN] |

### 5.3 Human Oversight

- **Level of autonomy:** [FILL IN: Fully autonomous / Human-in-the-loop / Human-on-the-loop / Advisory]
- **Escalation mechanism:** [FILL IN: How and when does the system escalate to humans?]
- **Override capability:** [FILL IN: Can humans override the system's decisions? How?]
- **Monitoring frequency:** [FILL IN: How often is system behavior reviewed by humans?]

---

## 6. Limitations and Risks

### 6.1 Known Limitations

| Limitation | Impact | Mitigation |
|-----------|--------|-----------|
| [FILL IN: e.g., "Performance degrades for transactions in currencies not in training data"] | [FILL IN] | [FILL IN] |
| [FILL IN: e.g., "Latency increases under high concurrent load"] | [FILL IN] | [FILL IN] |
| [FILL IN] | [FILL IN] | [FILL IN] |

### 6.2 Failure Modes

| Failure Mode | Trigger | Expected Behavior | Fallback |
|-------------|---------|-------------------|----------|
| [FILL IN: e.g., "LLM API unavailable"] | [FILL IN] | [FILL IN] | [FILL IN: e.g., "Route to human agent queue"] |
| [FILL IN: e.g., "Knowledge base returns no results"] | [FILL IN] | [FILL IN] | [FILL IN] |
| [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |

### 6.3 Risks

| Risk ID | Risk Description | Likelihood | Impact | Residual Risk After Mitigation |
|---------|-----------------|-----------|--------|-------------------------------|
| [FILL IN] | [FILL IN] | [L/M/H] | [L/M/H/C] | [L/M/H] |

---

## 7. Environmental Impact

| Metric | Value |
|--------|-------|
| **Training Compute** | [FILL IN: GPU hours, instance type, cloud provider] |
| **Training Energy** | [FILL IN: kWh estimated] |
| **Training Carbon Footprint** | [FILL IN: kg CO2e estimated] |
| **Inference Compute per Request** | [FILL IN: Estimated tokens/request, compute cost] |
| **Daily Inference Volume** | [FILL IN: Expected requests per day] |
| **Annual Inference Carbon** | [FILL IN: Estimated annual kg CO2e for inference] |
| **Carbon Offset** | [FILL IN: Any offset measures in place] |

**Note:** For LLM API-based systems, request approximate carbon data from the API provider. If unavailable, estimate based on published benchmarks for the model size and provider's data center energy mix.

---

## 8. Machine Identity

This section documents how the model/system is identified within the organization's agent ecosystem. This is critical for audit trails, access control, and regulatory accountability.

### 8.1 System Identity

| Field | Value |
|-------|-------|
| **System ID** | [FILL IN: Unique identifier in the model registry, e.g., "ai-system-lending-explainer-v2"] |
| **Agent Registry Entry** | [FILL IN: Link to entry in the organization's agent/model registry] |
| **EU AI Act Registration** | [FILL IN: Registration ID in the EU AI database (required for high-risk systems)] |

### 8.2 Non-Human Identity (NHI) Credentials

For agentic systems that interact with other services, APIs, or databases:

| Credential Type | Identifier | Scope | Rotation Policy |
|----------------|-----------|-------|----------------|
| **Service Account** | [FILL IN: Service account name/ID] | [FILL IN: What systems can this agent access?] | [FILL IN: Rotation frequency] |
| **API Keys** | [FILL IN: Key identifier (not the key itself)] | [FILL IN: Which APIs?] | [FILL IN] |
| **OAuth Client** | [FILL IN: Client ID] | [FILL IN: Scopes granted] | [FILL IN] |
| **Database Access** | [FILL IN: Role/user] | [FILL IN: Read/Write, which tables?] | [FILL IN] |

### 8.3 Permission Boundaries

| Boundary | Description |
|----------|-------------|
| **Allowed Actions** | [FILL IN: What the agent is permitted to do autonomously] |
| **Restricted Actions** | [FILL IN: Actions requiring human approval before execution] |
| **Prohibited Actions** | [FILL IN: Actions the agent must never take] |
| **Data Access Scope** | [FILL IN: What data the agent can read and write] |
| **Rate Limits** | [FILL IN: Maximum requests per minute/hour to external services] |

### 8.4 Audit Trail Configuration

| Field | Value |
|-------|-------|
| **Logging System** | [FILL IN: Where agent actions are logged] |
| **Log Retention** | [FILL IN: How long logs are retained] |
| **Trace Correlation ID** | [FILL IN: How individual agent requests are traced across services] |
| **Immutability** | [FILL IN: Are logs tamper-proof? How?] |

---

## 9. Deployment Information

| Field | Value |
|-------|-------|
| **Deployment Environment** | [FILL IN: e.g., "AWS eu-west-1, Kubernetes cluster"] |
| **Deployment Method** | [FILL IN: e.g., "Blue-green deployment via CI/CD pipeline"] |
| **First Deployment Date** | [FILL IN: YYYY-MM-DD] |
| **Current Deployment Date** | [FILL IN: YYYY-MM-DD] |
| **Rollback Procedure** | [FILL IN: How to rollback to previous version] |
| **Canary / Shadow Configuration** | [FILL IN: Percentage of traffic, duration before full rollout] |
| **SLA** | [FILL IN: Availability target, latency target, error rate target] |
| **Monitoring Dashboard** | [FILL IN: Link to monitoring dashboard] |
| **Alerting Configuration** | [FILL IN: What triggers alerts and who receives them] |

---

## 10. Maintenance and Update Schedule

| Activity | Frequency | Responsible | Last Completed | Next Due |
|----------|-----------|-------------|---------------|----------|
| **Performance revalidation** | [FILL IN: e.g., Quarterly] | [FILL IN] | [FILL IN] | [FILL IN] |
| **Fairness audit** | [FILL IN: e.g., Quarterly for high risk] | [FILL IN] | [FILL IN] | [FILL IN] |
| **Knowledge base refresh** | [FILL IN: e.g., Weekly] | [FILL IN] | [FILL IN] | [FILL IN] |
| **Safety eval re-run** | [FILL IN: e.g., Monthly] | [FILL IN] | [FILL IN] | [FILL IN] |
| **Model retraining** | [FILL IN: e.g., On drift detection trigger] | [FILL IN] | [FILL IN] | [FILL IN] |
| **Prompt review** | [FILL IN: e.g., Bi-weekly] | [FILL IN] | [FILL IN] | [FILL IN] |
| **Dependency updates** | [FILL IN: e.g., Monthly security patches] | [FILL IN] | [FILL IN] | [FILL IN] |

---

## 11. Regulatory Compliance Status

### 11.1 EU AI Act

| Requirement | Article | Status | Evidence |
|------------|---------|--------|----------|
| Risk classification completed | Art. 6 | [Done / In Progress / Not Started] | [Link to classification] |
| Technical documentation | Art. 11 | [Done / In Progress / Not Started] | [This model card] |
| Transparency obligations | Art. 13 | [Done / In Progress / Not Started] | [FILL IN] |
| Human oversight measures | Art. 14 | [Done / In Progress / Not Started] | [FILL IN] |
| Accuracy and robustness | Art. 15 | [Done / In Progress / Not Started] | [FILL IN: Link to eval results] |
| Data governance | Art. 10 | [Done / In Progress / Not Started] | [FILL IN: Link to data card] |
| Quality management system | Art. 17 | [Done / In Progress / Not Started] | [FILL IN] |

### 11.2 DORA

| Requirement | Article | Status | Evidence |
|------------|---------|--------|----------|
| ICT risk management | Art. 6 | [Done / In Progress / Not Started] | [FILL IN] |
| Incident reporting | Art. 19 | [Done / In Progress / Not Started] | [FILL IN] |
| Third-party risk (if API-based) | Art. 28 | [Done / In Progress / Not Started] | [FILL IN] |
| Operational resilience testing | Art. 26 | [Done / In Progress / Not Started] | [FILL IN] |

### 11.3 Other Regulations

| Regulation | Requirement | Status | Evidence |
|-----------|-------------|--------|----------|
| GDPR | [FILL IN] | [Done / In Progress / Not Started] | [FILL IN] |
| [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |

---

## 12. Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN: e.g., "Initial model card"] |
| [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN: e.g., "Updated eval results after retraining on Q4 data"] |

---

## Example: Fraud Detection Alert Explainer

The following is a partially completed example showing how to fill in this template for a fraud detection alert explanation system.

### Model Details (Example)

| Field | Value |
|-------|-------|
| **Model Name** | Fraud Alert Explainer |
| **Model Version** | 1.2.0 |
| **Model Type** | Agent (RAG Pipeline + LLM Generation) |
| **Architecture** | LangGraph agent with Claude 3.5 Sonnet backbone, vector retrieval over fraud rule documentation |
| **Base Model** | Claude 3.5 Sonnet (Anthropic, 2024-10-22) |
| **Framework** | LangGraph + LangChain |
| **Input Format** | Fraud alert JSON (transaction details, risk score, triggered rules) |
| **Output Format** | Natural language explanation of why the transaction was flagged, addressed to the customer |
| **Risk Classification** | Limited (customer-facing explanations for automated fraud decisions) |

### Intended Use (Example)

| Use Case | Description | Target Users |
|----------|-------------|-------------|
| Fraud alert explanation | Generate plain-language explanations for customers whose transactions were flagged by the fraud detection system | Retail banking customers via mobile app notification |
| Agent assist | Provide customer service agents with pre-drafted explanations they can review and send to customers | Internal customer service team |

### Out-of-Scope Uses (Example)

| Out-of-Scope Use | Why | Mitigation |
|------------------|-----|-----------|
| Making fraud/not-fraud decisions | System explains decisions, does not make them | System receives decisions from upstream fraud model; guardrail prevents decision language |
| Providing legal advice about disputed transactions | Not qualified for legal advice | Guardrail detects legal queries; escalates to compliance team |

### Machine Identity (Example)

| Field | Value |
|-------|-------|
| **System ID** | ai-fraud-alert-explainer-v1.2 |
| **Service Account** | svc-fraud-explainer@internal.bank.nl |
| **API Keys** | anthropic-key-fraud-prod (Anthropic Claude API) |
| **Database Access** | fraud_alerts (read-only), customer_communications (write) |
| **Allowed Actions** | Read fraud alerts, generate explanations, write to customer notification queue |
| **Prohibited Actions** | Modify fraud scores, access account balances, initiate transactions |

---

## Cross-References

- **Eval-Driven Development:** [../evaluations/eval-driven-development.md](../evaluations/eval-driven-development.md) -- methodology for generating the eval results documented in this card
- **LLM Eval Patterns:** [../evaluations/llm-eval-patterns.md](../evaluations/llm-eval-patterns.md) -- evaluation patterns used for LLM-based systems
- **Bias and Fairness Evals:** [../evaluations/bias-and-fairness-evals.md](../evaluations/bias-and-fairness-evals.md) -- fairness evaluation methodology and bias assessment report template
- **Pre-Deployment Gate:** [../checklists/pre-deployment-gate.yaml](../checklists/pre-deployment-gate.yaml) -- requires a completed model card for deployment approval
- **EU AI Act Risk Classification:** [../../01-discovery-governance/checklists/eu-ai-act-risk-classification.yaml](../../01-discovery-governance/checklists/eu-ai-act-risk-classification.yaml) -- determines documentation depth required
- **Continuous Online Evaluation:** [../../03-runtime-governance/evaluations/continuous-online-evaluation.md](../../03-runtime-governance/evaluations/continuous-online-evaluation.md) -- ongoing monitoring that feeds back into model card updates
- **SAFEST Checklist:** [../../04-operational-governance/regulatory/safest-checklist-detailed.md](../../04-operational-governance/regulatory/safest-checklist-detailed.md) -- item T-12 requires this model card
- **Glossary:** [../../05-cross-cutting/glossary.md](../../05-cross-cutting/glossary.md) -- definitions of terms used in this template

---

*Last updated: 2026-02-28*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
