# Defining Acceptance Criteria for AI Systems

## Purpose

This guide provides a structured approach for defining measurable acceptance criteria **before any AI development begins**. Acceptance criteria are the quantitative bar that an AI system must clear to be considered fit for deployment. They are the "shift-left" anchor of the entire governance framework -- the mechanism by which product, engineering, compliance, and business stakeholders agree on what "good enough" means before a single line of code is written.

Without predefined acceptance criteria, teams fall into two traps: shipping AI systems that do not meet business needs, or endlessly iterating without a clear definition of done. Both are expensive. Both are preventable.

## When to Use

- **After risk classification** (see [EU AI Act Risk Classification](../checklists/eu-ai-act-risk-classification.yaml)) and **before any development sprint**
- When defining the evaluation strategy for a new AI system (see [Evaluation Strategy Template](evaluation-strategy-template.yaml))
- When the scope of an existing AI system changes materially (new use case, new population, new data)
- When regulatory requirements change and existing criteria need updating

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **Product Manager** | **Accountable** -- defines product-level criteria (business outcomes, user experience) |
| **AI/ML Engineer** | **Responsible** -- defines AI quality criteria (accuracy, calibration, latency) and implements measurement |
| **Compliance Officer (2nd Line)** | **Consulted** -- validates that criteria cover regulatory requirements (fairness, explainability, documentation) |
| **Business Stakeholder** | **Consulted** -- validates that business KPI thresholds reflect operational reality |
| **AI Governance Committee** | **Approver** -- approves criteria for limited and high-risk systems |

## Regulatory Basis

- **EU AI Act Article 9(2)(a)** -- Risk management must include identification and analysis of known and foreseeable risks, including performance metrics
- **EU AI Act Article 15** -- High-risk AI systems must achieve appropriate levels of accuracy, robustness, and cybersecurity
- **SAFEST items S-03** (pre-deployment acceptance criteria), **S-04** (edge case analysis), **F-03** (bias testing), **F-04** (fairness metrics)
- **DNB Good Practice** -- Expectation that model performance criteria are defined and monitored

---

## 1. Why Acceptance Criteria Must Be Defined During Discovery

### The Cost of Late Criteria Definition

| When Criteria Are Defined | Consequence |
|--------------------------|-------------|
| **During Discovery** (correct) | Teams build toward a known target. Eval suites can be written before features. Stakeholders align on trade-offs early. Deployment decisions are evidence-based. |
| **During Development** (too late) | Criteria are retrofitted to match what was already built. The bar is set to whatever the model achieves, not what the business needs. Bias testing is an afterthought. |
| **At Deployment** (far too late) | Ship-or-delay panic. Criteria are watered down to avoid blocking a release. Governance is theater. |
| **Never** (governance failure) | No objective basis for deployment decisions. No basis for monitoring. No way to detect degradation. Regulatory non-compliance. |

### The Principle

**Acceptance criteria are a contract between Discovery and Development.** Discovery defines what "good" looks like. Development builds to meet that bar. Runtime monitors against that bar. Operational governance revalidates that bar periodically.

This mirrors the Superpowers development methodology: "No code without a failing test." In the AI governance context: **No AI feature without predefined acceptance criteria.**

---

## 2. The Acceptance Criteria Framework

Every acceptance criterion must have five components:

| Component | Description | Example |
|-----------|-------------|---------|
| **Metric** | What is being measured | Precision for fraud detection |
| **Threshold** | The minimum acceptable value | >= 0.92 |
| **Measurement Method** | How the metric is computed | Evaluated on holdout test set of 10,000 labeled transactions |
| **Data Source** | Where the evaluation data comes from | Production transaction sample from Q4 2025, stratified by amount band |
| **Blocking** | Whether failure blocks deployment | Yes -- hard gate |

A criterion without all five components is incomplete and must not be accepted at the Discovery Gate.

---

## 3. Categories of Acceptance Criteria

### 3.1 Product-Level Criteria

Product-level criteria measure whether the AI system achieves its intended business outcome from the user's perspective.

| Metric | Description | Typical Threshold | Measurement Method |
|--------|-------------|-------------------|-------------------|
| **Task Completion Rate** | Percentage of user tasks the AI system resolves without human intervention | >= 70% for customer service; >= 90% for document processing | Count of successfully completed tasks / total tasks, measured over 1,000+ interactions |
| **User Satisfaction Score** | Post-interaction user rating (e.g., CSAT, NPS) | CSAT >= 4.0/5.0 | Post-interaction survey, minimum 200 responses |
| **Escalation Rate** | Percentage of interactions that require human takeover | <= 25% for customer service agents | Count of escalations / total interactions |
| **Time to Resolution** | Average time from user request to resolution | <= 3 minutes for simple queries | Timestamp analysis from interaction logs |
| **Business KPI Impact** | Measurable effect on a target business metric | Fraud losses reduced by >= 15% vs. rules-based baseline | A/B test or pre-post comparison over 30-day period |

### 3.2 AI Quality Criteria

AI quality criteria measure the technical performance of the model or LLM.

| Metric | Description | Typical Threshold | When to Use |
|--------|-------------|-------------------|-------------|
| **Accuracy** | Fraction of correct predictions | >= 0.95 for binary classification | General classification tasks |
| **Precision** | Fraction of positive predictions that are correct | >= 0.90 for fraud detection | When false positives are costly (blocking legitimate transactions) |
| **Recall** | Fraction of actual positives correctly identified | >= 0.85 for AML screening | When false negatives are costly (missing suspicious transactions) |
| **F1 Score** | Harmonic mean of precision and recall | >= 0.88 | When both false positives and false negatives matter |
| **AUC-ROC** | Area under the receiver operating characteristic curve | >= 0.95 for credit scoring | When comparing model discrimination ability |
| **Calibration (Brier Score)** | How well predicted probabilities match actual outcomes | <= 0.10 | When probability estimates drive decisions (risk scoring) |
| **Latency (P95)** | 95th percentile response time | <= 200ms for real-time decisions | All production systems |

For a comprehensive list, see the [AI Quality Metrics Catalog](ai-quality-metrics-catalog.md).

### 3.3 LLM-Specific Criteria

For systems built on large language models, additional criteria address the unique failure modes of generative AI.

| Metric | Description | Typical Threshold | Measurement Method |
|--------|-------------|-------------------|-------------------|
| **Hallucination Rate** | Percentage of responses containing fabricated facts | <= 2% for customer-facing financial information | Human evaluation of 500+ sampled responses against ground truth |
| **Safety Violation Rate** | Percentage of responses that violate safety policies (harmful content, unauthorized advice) | 0% for critical categories; <= 0.1% for borderline categories | Automated safety classifier + human review of flagged responses |
| **Instruction Following Score** | Percentage of responses that correctly follow the system prompt constraints | >= 98% | Automated eval suite with 200+ test cases covering each constraint |
| **Groundedness Score** | Percentage of factual claims that can be traced to source documents (for RAG systems) | >= 95% | Automated citation verification against retrieved documents |
| **Toxicity Score** | Rate of responses flagged by toxicity classifiers | <= 0.05% | Perspective API or equivalent on full response corpus |
| **Refusal Accuracy** | Correctly refuses out-of-scope requests without refusing valid ones | False refusal rate <= 5%; Correct refusal rate >= 99% | Test suite with 100 in-scope and 100 out-of-scope requests |

### 3.4 Fairness Criteria

Fairness criteria ensure the AI system does not discriminate against protected groups. Required for limited and high-risk systems.

| Metric | Description | Typical Threshold | When to Use |
|--------|-------------|-------------------|-------------|
| **Demographic Parity Ratio** | Ratio of positive prediction rates between groups | >= 0.80 (four-fifths rule) | When equal treatment across groups is the goal |
| **Equalized Odds Difference** | Maximum difference in TPR or FPR across groups | <= 0.10 | When equal error rates across groups matter (credit scoring, fraud detection) |
| **Calibration Across Groups** | Difference in Brier scores between groups | <= 0.05 | When probability estimates must be equally reliable across groups |
| **Disparate Impact Ratio** | Selection rate for protected group / selection rate for reference group | >= 0.80 | Legal standard in employment and lending decisions |

Protected attributes to evaluate (select those relevant to the use case):

- Age groups
- Gender
- Nationality / ethnicity
- Geographic region (as proxy for socioeconomic status)
- Customer tenure (as proxy for economic vulnerability)

See SAFEST items F-01 (protected characteristics identification) and F-02 (proxy variable analysis) for guidance on identifying relevant attributes.

---

## 4. Template: Acceptance Criteria Table

Use this template to document acceptance criteria for your AI system. Fill one row per criterion. This table becomes an input to the [Evaluation Strategy Template](evaluation-strategy-template.yaml).

```markdown
| ID | Category | Metric | Threshold | Measurement Method | Data Source | Blocking | Regulatory Ref |
|----|----------|--------|-----------|-------------------|-------------|----------|----------------|
| AC-001 | Product | Task completion rate | >= 70% | Sampled interaction analysis | Production logs, 1,000+ interactions | Yes | -- |
| AC-002 | AI Quality | Precision | >= 0.92 | Holdout test set evaluation | Labeled test set, N=10,000 | Yes | S-03 |
| AC-003 | AI Quality | Recall | >= 0.85 | Holdout test set evaluation | Labeled test set, N=10,000 | Yes | S-03 |
| AC-004 | Fairness | Demographic parity ratio | >= 0.80 | Subgroup analysis on test set | Test set stratified by protected attributes | Yes | F-03, F-04 |
| AC-005 | LLM | Hallucination rate | <= 2% | Human evaluation of sampled responses | 500 randomly sampled production responses | Yes | -- |
| AC-006 | LLM | Safety violation rate | 0% (critical) | Safety classifier + human review | All production responses | Yes | -- |
| AC-007 | Performance | P95 latency | <= 200ms | Load testing | Simulated production traffic | No (soft) | -- |
```

---

## 5. Example: Acceptance Criteria for a Customer-Facing Fraud Alert Chatbot

### Context

A FinTech deploys a chatbot that helps customers understand why their transaction was flagged as potentially fraudulent. The chatbot retrieves the fraud detection model's reasoning and explains it in natural language. It can also help the customer confirm or dispute the flag.

**Risk tier:** Limited (customer-facing chatbot with transparency obligation; does not make the fraud decision itself)

### Acceptance Criteria

| ID | Category | Metric | Threshold | Measurement Method | Data Source | Blocking |
|----|----------|--------|-----------|-------------------|-------------|----------|
| AC-001 | Product | Task completion rate (customer resolves alert without calling support) | >= 65% | Interaction outcome tracking | Production logs over 30 days, N >= 2,000 interactions | Yes |
| AC-002 | Product | Customer satisfaction (post-interaction CSAT) | >= 3.8 / 5.0 | Post-chat survey | Survey responses, N >= 300 | Yes |
| AC-003 | Product | Escalation rate to human agent | <= 30% | Escalation event tracking | Production logs | No (soft) |
| AC-004 | LLM | Hallucination rate (fabricated fraud reasons) | 0% | Human evaluation of sampled explanations vs. actual fraud model output | 500 sampled responses per month | Yes |
| AC-005 | LLM | Safety violation rate (providing financial advice, disclosing internal policies) | 0% | Automated safety classifier + monthly human audit | All production responses | Yes |
| AC-006 | LLM | Instruction following (stays within scope, does not promise outcomes) | >= 98% | Automated eval suite with 200 test scenarios | Curated test suite | Yes |
| AC-007 | LLM | Groundedness (explanations match actual fraud model output) | >= 95% | Automated comparison of chatbot explanation to fraud model features | 500 sampled response-model pairs | Yes |
| AC-008 | Fairness | Equal explanation quality across customer segments | Qualitative review shows no systemic differences | Human review of explanation quality stratified by customer segment | 50 responses per segment, 4 segments | No (soft) |
| AC-009 | Performance | P95 response latency | <= 3 seconds | Performance monitoring | Production latency metrics | Yes |
| AC-010 | Transparency | AI disclosure rate (customer informed they are talking to AI) | 100% | Automated check: every conversation starts with disclosure | Production conversation logs | Yes |

### Notes on This Example

- **AC-004 and AC-005 are zero-tolerance hard gates.** A fraud explanation chatbot that fabricates reasons or gives financial advice is a compliance and reputational disaster. There is no acceptable threshold above zero.
- **AC-003 is a soft gate** because some escalation is expected and healthy -- the goal is not zero escalation but manageable escalation.
- **AC-008 uses qualitative review** because fairness in explanation quality is difficult to quantify with a single number. Human review is appropriate here; the criterion is still defined and measured.
- **AC-010 is a regulatory requirement** under EU AI Act Article 50(1). It is non-negotiable.

---

## 6. Process: From Criteria to Evaluation Strategy

Acceptance criteria feed directly into the evaluation strategy:

```
  Acceptance Criteria              Evaluation Strategy               Eval Suite
  (this document)                  (evaluation-strategy-template)    (Development Governance)

  Define WHAT must be true   -->   Define HOW it will be measured --> Implement automated tests
                                   and WHEN                          that verify the criteria
```

After completing acceptance criteria:

1. Transfer them into the [Evaluation Strategy Template](evaluation-strategy-template.yaml)
2. For each criterion, specify the evaluation frequency (pre-deployment, continuous, periodic)
3. Define escalation thresholds (what metric breach level triggers what action)
4. Submit the evaluation strategy for review at the Discovery Gate

The evaluation strategy then becomes the input for [eval-driven development](../../02-development-governance/evaluations/eval-driven-development.md) in Development Governance, where criteria are implemented as automated evaluation suites.

---

## 7. Common Mistakes

| Mistake | Why It Happens | How to Avoid |
|---------|---------------|-------------|
| **Defining criteria after the model is built** | Team is eager to start building; criteria feel like overhead | Make the Discovery Gate mandatory: no criteria, no sprint work |
| **Setting thresholds based on what the model achieves** | Team does not know what threshold to set, so they benchmark first | Set thresholds based on business requirements and user impact, not model capability |
| **Using only accuracy** | Accuracy is the most familiar metric | Use the [AI Quality Metrics Catalog](ai-quality-metrics-catalog.md) to select task-appropriate metrics |
| **Ignoring fairness criteria** | "We do not collect protected attributes" | Proxy variables exist (see SAFEST F-02). Use inference or external data for fairness evaluation |
| **Setting impossible thresholds** | Aspirational thinking without feasibility check | Consult ML engineers on achievable ranges; set stretch targets as soft gates, minimum viable thresholds as hard gates |
| **Too few criteria** | Minimizing governance effort | High-risk systems need 10+ criteria; minimal risk needs at least 3 |
| **No measurement method specified** | Criterion seems obvious | If you cannot describe how to measure it, it is not a criterion -- it is a wish |

---

## Cross-References

- **Risk Classification:** [EU AI Act Risk Classification Checklist](../checklists/eu-ai-act-risk-classification.yaml) -- determines how many criteria are needed
- **Metrics Catalog:** [AI Quality Metrics Catalog](ai-quality-metrics-catalog.md) -- comprehensive reference for selecting metrics
- **Evaluation Strategy:** [Evaluation Strategy Template](evaluation-strategy-template.yaml) -- where criteria are formalized into a measurement plan
- **Eval-Driven Development:** [eval-driven-development.md](../../02-development-governance/evaluations/eval-driven-development.md) -- how criteria become automated eval suites
- **Pre-Deployment Gate:** [pre-deployment-gate.yaml](../../02-development-governance/checklists/pre-deployment-gate.yaml) -- where criteria are verified before deployment
- **Continuous Evaluation:** [continuous-online-evaluation.md](../../03-runtime-governance/evaluations/continuous-online-evaluation.md) -- how criteria are monitored in production
- **Risk Tiering Model:** [risk-tiering-model.md](../../07-enterprise-implementation/risk-based-adoption/risk-tiering-model.md) -- governance requirements by tier

---

*Last updated: 2026-02-28*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
