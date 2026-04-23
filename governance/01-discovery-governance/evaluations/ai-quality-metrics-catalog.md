# AI Quality Metrics Catalog

## Purpose

This catalog provides a comprehensive reference of metrics for evaluating AI systems across six categories: classification, regression, LLM behavior, fairness, product outcomes, and business impact. Use this catalog when selecting metrics for acceptance criteria (see [Defining Acceptance Criteria](defining-acceptance-criteria.md)) and evaluation strategies (see [Evaluation Strategy Template](evaluation-strategy-template.yaml)).

## When to Use

- During Discovery Governance, when defining acceptance criteria for a new AI system
- During Development Governance, when building eval suites (see [eval-driven development](../../02-development-governance/evaluations/eval-driven-development.md))
- When reviewing or updating the evaluation strategy for an existing system
- When selecting metrics for [continuous online evaluation](../../03-runtime-governance/evaluations/continuous-online-evaluation.md) in production

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **AI/ML Engineer** | **Responsible** -- selects appropriate metrics based on system type and use case |
| **Product Manager** | **Consulted** -- ensures selected metrics align with business objectives |
| **Compliance Officer** | **Consulted** -- validates that fairness metrics cover regulatory requirements |

## Regulatory Basis

- **EU AI Act Article 15** -- High-risk systems must achieve appropriate levels of accuracy
- **SAFEST items S-03** (acceptance criteria), **F-03** (bias testing), **F-04** (fairness metrics selection)
- **DNB Good Practice** -- Model performance must be measurable and monitored

---

## 1. Classification Metrics

For AI systems that assign inputs to discrete categories (e.g., fraud/not-fraud, approved/denied, category A/B/C).

| Metric | Definition | When to Use | Typical Threshold | FinTech Relevance |
|--------|-----------|-------------|-------------------|-------------------|
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN). Fraction of all predictions that are correct. | Balanced datasets where all errors are equally costly. **Not suitable** for imbalanced datasets (e.g., fraud detection). | >= 0.95 (varies by task) | General performance indicator; insufficient alone for most FinTech use cases |
| **Precision** | TP / (TP + FP). Of all items predicted positive, how many are actually positive? | When **false positives are costly**. A false positive in fraud detection blocks a legitimate customer transaction. | >= 0.90 for customer-impacting decisions | Fraud detection: high precision means fewer legitimate transactions blocked |
| **Recall (Sensitivity)** | TP / (TP + FN). Of all actual positives, how many did we catch? | When **false negatives are costly**. A false negative in AML means a suspicious transaction goes undetected. | >= 0.85 for regulatory screening; >= 0.95 for safety-critical | AML screening: high recall means fewer suspicious transactions missed |
| **F1 Score** | 2 * (Precision * Recall) / (Precision + Recall). Harmonic mean of precision and recall. | When both false positives and false negatives matter and you need a single balanced metric. | >= 0.88 | General-purpose metric when precision-recall tradeoff must be balanced |
| **AUC-ROC** | Area under the Receiver Operating Characteristic curve. Measures the model's ability to distinguish between classes across all threshold settings. | When comparing model discrimination ability independent of a specific operating threshold. | >= 0.95 for high-risk decisions; >= 0.80 for informational systems | Credit scoring model comparison: which model better separates good from bad credit? |
| **AUC-PR** | Area under the Precision-Recall curve. More informative than AUC-ROC for imbalanced datasets. | When the positive class is rare (fraud, AML alerts). AUC-ROC can be misleadingly high on imbalanced data. | >= 0.70 (varies significantly by prevalence) | Fraud detection: better reflects model performance when fraud is < 1% of transactions |
| **Specificity** | TN / (TN + FP). Of all actual negatives, how many did we correctly identify as negative? | When false positive rate must be controlled. | >= 0.99 for high-volume screening | Transaction monitoring: specificity of 0.99 still means 1% of legitimate transactions flagged |
| **Matthews Correlation Coefficient (MCC)** | Correlation between predicted and actual classes, accounting for all four confusion matrix cells. Range: -1 to +1. | When you need a single metric that is robust to class imbalance. More reliable than accuracy on imbalanced data. | >= 0.70 | Recommended as primary metric for imbalanced FinTech classification tasks |
| **Log Loss** | Negative log-likelihood of the predicted probability for the true class. Penalizes confident wrong predictions more heavily. | When predicted probabilities (not just classes) matter. | <= 0.30 | Credit scoring: penalizes a model that is confidently wrong about a customer's risk |
| **Cohen's Kappa** | Agreement between predicted and actual classes, adjusted for chance agreement. | When evaluating agreement beyond random chance, especially useful for multi-class problems. | >= 0.60 (substantial agreement) | Document classification, transaction categorization |

### Multi-Class Extensions

For systems with more than two classes (e.g., transaction categorization into 10+ categories):

| Metric | Definition | When to Use |
|--------|-----------|-------------|
| **Macro-Averaged F1** | Average F1 across all classes, treating each class equally | When all classes are equally important regardless of prevalence |
| **Weighted-Averaged F1** | Average F1 weighted by class prevalence | When class importance correlates with prevalence |
| **Top-K Accuracy** | Whether the correct class appears in the top K predictions | When showing multiple suggestions (e.g., transaction category recommendations) |
| **Confusion Matrix** | Full N x N matrix of predictions vs. actuals | Always -- provides the most complete picture of classification behavior |

---

## 2. Regression Metrics

For AI systems that predict continuous values (e.g., transaction amount prediction, customer lifetime value, risk scores on a continuous scale).

| Metric | Definition | When to Use | Typical Threshold | FinTech Relevance |
|--------|-----------|-------------|-------------------|-------------------|
| **MAE (Mean Absolute Error)** | Average of absolute differences between predicted and actual values. Robust to outliers. | When all errors are equally important regardless of direction. | Domain-specific (e.g., <= EUR 50 for transaction amount prediction) | Revenue forecasting, expense categorization amount prediction |
| **RMSE (Root Mean Squared Error)** | Square root of the average of squared differences. Penalizes large errors more than MAE. | When large errors are disproportionately costly. | Domain-specific | Risk score prediction where being very wrong is much worse than being slightly wrong |
| **R-squared (R2)** | Proportion of variance in the target explained by the model. Range: -infinity to 1.0. | When assessing overall model explanatory power. | >= 0.80 for production use; >= 0.60 for exploratory models | Credit risk modeling: how much of the default variance does the model explain? |
| **MAPE (Mean Absolute Percentage Error)** | Average of absolute percentage differences. Scale-independent. | When relative error matters more than absolute error. | <= 10% for forecasting tasks | Revenue forecasting: 5% error on EUR 1M is different from 5% error on EUR 100 |
| **Quantile Loss** | Evaluates predictions at specific quantiles (e.g., 10th, 50th, 90th percentile). | When the distribution of predictions matters, not just the average. | Domain-specific | VaR (Value at Risk) models: accuracy at the tails matters more than the mean |

---

## 3. LLM Metrics

For systems built on large language models (chatbots, agents, document processors, content generators).

| Metric | Definition | When to Use | Typical Threshold | FinTech Relevance |
|--------|-----------|-------------|-------------------|-------------------|
| **Hallucination Rate** | Percentage of responses containing fabricated or unsupported factual claims. Measured via human evaluation or automated fact-checking against source documents. | All customer-facing LLM systems. **Zero tolerance for financial information.** | <= 2% general; 0% for financial facts | Customer-facing financial chatbot: hallucinating account balances or interest rates is a compliance disaster |
| **Groundedness Score** | Percentage of factual claims in the response that can be traced to retrieved source documents (for RAG systems). | All RAG-based systems. | >= 95% | Financial advisor agent grounding responses in product documentation and regulatory texts |
| **Safety Violation Rate** | Percentage of responses that violate defined safety policies (harmful content, unauthorized advice, data leakage). | All customer-facing and agent systems. | 0% for critical categories (financial advice without license, PII exposure); <= 0.1% for borderline | Agent that gives personalized investment advice without proper disclaimers = regulatory violation |
| **Instruction Following Score** | Percentage of responses that correctly adhere to all system prompt constraints (scope, tone, format, limitations). | All systems with defined behavioral boundaries. | >= 98% | Customer service agent staying within product scope and not making promises beyond authority |
| **Toxicity Score** | Rate of responses flagged by toxicity classifiers (hate speech, profanity, threats, discrimination). | All customer-facing systems. | <= 0.05% | Reputational protection: even one toxic response to a customer can become a PR incident |
| **Refusal Accuracy** | Correctly refuses out-of-scope requests without incorrectly refusing valid ones. Two sub-metrics: false refusal rate and missed refusal rate. | Systems with defined scope boundaries. | False refusal <= 5%; Missed refusal <= 1% | Agent that refuses to answer a legitimate question about account fees (false refusal) erodes trust |
| **Response Consistency** | Degree to which the system gives consistent answers to semantically equivalent questions. | Systems where consistency is expected (policy explanations, product information). | >= 90% consistency across paraphrased queries | Two customers asking the same question about loan terms must get the same answer |
| **BLEU Score** | Measures n-gram overlap between generated and reference text. Primarily for translation and structured text generation. | Translation systems, template-based generation, structured response evaluation. | >= 0.40 for translation; domain-specific otherwise | Automated report generation, regulatory filing summaries |
| **ROUGE Score** | Measures overlap (unigram, bigram, longest common subsequence) between generated and reference text. | Document summarization, report generation. | ROUGE-L >= 0.50 for summarization | Compliance report summarization, customer communication drafting |
| **Semantic Similarity** | Cosine similarity between embedding representations of generated and reference texts. | When meaning matters more than exact wording. | >= 0.85 | Customer query understanding: does the agent correctly interpret the customer's intent? |

---

## 4. Fairness Metrics

For ensuring AI systems do not discriminate against protected groups. Required for limited and high-risk systems (SAFEST F-03, F-04).

| Metric | Definition | When to Use | Typical Threshold | FinTech Relevance |
|--------|-----------|-------------|-------------------|-------------------|
| **Demographic Parity Ratio** | min(P(Y=1|G=g)) / max(P(Y=1|G=g)) across all groups g. Measures whether the positive prediction rate is equal across groups. | When equal treatment (equal approval rates) is the fairness goal. | >= 0.80 (four-fifths rule from US EEOC; widely adopted in EU practice) | Credit approval: are approval rates comparable across age groups, nationalities? |
| **Equalized Odds Difference** | max|TPR(g1) - TPR(g2)| or max|FPR(g1) - FPR(g2)| across all group pairs. | When equal accuracy across groups is the fairness goal (same error rates for all groups). | <= 0.10 | Fraud detection: does the system falsely flag transactions from one demographic more than others? |
| **Predictive Parity** | PPV (precision) is equal across groups. | When the meaning of a positive prediction must be consistent across groups. | Difference <= 0.05 | Risk scoring: a "high risk" score should mean the same probability of default for all groups |
| **Calibration Across Groups** | Predicted probabilities match observed outcomes equally well for all groups (measured via Brier score or calibration curves). | When probability estimates drive decisions and must be equally reliable for all groups. | Brier score difference <= 0.05 across groups | Credit scoring: risk probabilities must be equally calibrated for all customer segments |
| **Disparate Impact Ratio** | Selection rate for protected group / selection rate for reference group. | Legal standard in employment and lending; widely used as a regulatory benchmark. | >= 0.80 | Lending decisions: regulatory standard for demonstrating non-discrimination |
| **Equal Opportunity Difference** | Difference in TPR between groups. Focuses only on positive outcomes. | When false negatives are the primary fairness concern (denying benefits to deserving individuals). | <= 0.10 | Account approval: eligible customers from all groups should have equal approval rates |
| **Counterfactual Fairness** | Prediction does not change when the protected attribute is counterfactually altered while holding other attributes fixed. | When individual-level fairness is the concern (not just group-level statistics). | No threshold; measured as the percentage of predictions that change | Customer risk assessment: would the risk score change if only the customer's nationality changed? |

### Selecting Fairness Metrics

Fairness metrics can conflict with each other. It is mathematically impossible to satisfy all fairness criteria simultaneously (except when base rates are equal across groups). Use this guidance:

| If the primary concern is... | Use this metric | Rationale |
|------------------------------|----------------|-----------|
| Equal access to a benefit | Demographic Parity | Ensures equal approval/selection rates across groups |
| Equal error rates | Equalized Odds | Ensures the system is equally accurate for all groups |
| Equal meaning of predictions | Predictive Parity | Ensures a positive prediction carries the same weight for all groups |
| Regulatory compliance | Disparate Impact Ratio | Widely recognized legal standard |
| Individual fairness | Counterfactual Fairness | Addresses individual-level discrimination |

Document which fairness metrics you select and **why you chose them over alternatives**. This justification is a regulatory requirement for high-risk systems (SAFEST F-04).

---

## 5. Product Metrics

For measuring the AI system's impact on user experience and product outcomes.

| Metric | Definition | When to Use | Typical Threshold | FinTech Relevance |
|--------|-----------|-------------|-------------------|-------------------|
| **Task Completion Rate** | Percentage of user tasks successfully completed by the AI system without human intervention. | Customer-facing AI agents, chatbots, automated workflows. | >= 70% for conversational agents; >= 95% for straight-through processing | Customer service chatbot: how often does the customer get their question answered without calling support? |
| **User Satisfaction (CSAT)** | Post-interaction customer satisfaction score. | All customer-facing systems. | >= 4.0 / 5.0 | Direct measure of customer experience with the AI system |
| **Net Promoter Score (NPS)** | Likelihood that users would recommend the AI-powered feature. | Feature-level NPS for AI-specific experiences. | >= 30 (good); >= 50 (excellent) | Measures whether the AI feature builds or erodes customer trust |
| **Escalation Rate** | Percentage of interactions escalated to a human. | Conversational AI, decision-support systems. | <= 25% for general queries; <= 50% for complex financial topics | Measures AI system capability boundary; high escalation = system scope too broad |
| **Time to Resolution** | Average time from user request to resolution. | All customer-facing systems. | <= 3 min for simple queries; <= 10 min for complex queries | AI should be faster than human agents; if not, the business case weakens |
| **Automation Rate** | Percentage of eligible processes handled end-to-end by AI without human intervention. | Straight-through processing, document handling, claims processing. | >= 80% for low-complexity; >= 50% for medium-complexity | KYC document verification, payment processing, account opening |
| **Error Recovery Rate** | When the AI system makes an error, how often does it recover (correct itself or gracefully escalate) vs. compound the error. | Agent systems with multi-step workflows. | >= 90% | Agent that makes a mistake and then compounds it is worse than an agent that makes a mistake and escalates |

---

## 6. Business Metrics

For measuring the AI system's impact on business outcomes and operational efficiency.

| Metric | Definition | When to Use | Typical Threshold | FinTech Relevance |
|--------|-----------|-------------|-------------------|-------------------|
| **Cost per Decision** | Total cost (compute + human review + error correction) per AI-assisted decision. | All AI systems replacing or augmenting human decisions. | < cost of equivalent human decision | Fraud review: AI-assisted review at EUR 0.50/case vs. human review at EUR 5.00/case |
| **False Positive Cost** | Total business cost of false positive predictions (blocked transactions, unnecessary reviews, customer friction). | Classification systems with customer impact. | Quantified in EUR per period; target: decreasing trend | Fraud detection: each false positive = a blocked customer + support call + churn risk |
| **False Negative Cost** | Total business cost of false negative predictions (missed fraud, undetected AML, missed defaults). | Classification systems with regulatory or financial risk. | Quantified in EUR per period; target: within risk appetite | AML screening: each false negative = potential regulatory fine + reputational damage |
| **Processing Time** | Time from input to decision, including any human-in-the-loop steps. | All real-time and near-real-time systems. | Defined by SLA (e.g., < 500ms for transaction scoring, < 24h for KYC review) | Payment processing: scoring latency directly impacts transaction approval speed |
| **Throughput** | Number of decisions/predictions per unit of time. | High-volume systems. | Sufficient to handle peak load with headroom (e.g., >= 1.5x peak) | Transaction monitoring: must handle holiday-season volume spikes |
| **ROI of AI vs. Baseline** | Incremental business value delivered by the AI system compared to the previous approach (rules, human, no automation). | Investment justification and ongoing viability assessment. | Positive ROI within defined payback period | Quantifies whether the AI governance investment is justified by the AI system's value |

---

## 7. How to Select Metrics for Your System

### Step 1: Identify Your System Type

| System Type | Start With These Metric Categories |
|-------------|-------------------------------------|
| Binary classifier (fraud, AML, credit) | Classification + Fairness + Business |
| Multi-class classifier (categorization, routing) | Classification (multi-class) + Product |
| Regression (risk scoring, forecasting) | Regression + Fairness + Business |
| LLM chatbot / agent | LLM + Product + Fairness |
| LLM + RAG (knowledge assistant) | LLM (emphasis on groundedness) + Product |
| Multi-agent system | LLM + Product + Business + all agent-specific metrics from [multi-agent governance](../../03-runtime-governance/agentic-workflows/multi-agent-governance-framework.md) |

### Step 2: Select Minimum Metrics by Risk Tier

| Risk Tier | Minimum Metrics Required |
|-----------|--------------------------|
| Minimal | 3 metrics: at least 1 AI quality + 1 product + 1 business |
| Limited | 5+ metrics: at least 2 AI quality + 1 product + 1 fairness + 1 business |
| High | 10+ metrics: at least 3 AI quality + 2 product + 2 fairness + 2 business + LLM metrics if applicable |

### Step 3: Define Thresholds

For each selected metric:
1. Start with the typical threshold from this catalog
2. Adjust based on your specific business context (cost of errors, regulatory requirements, customer expectations)
3. Validate with the AI/ML engineer that the threshold is technically achievable
4. Get business stakeholder agreement that the threshold reflects operational needs
5. Document the threshold and rationale in the [Evaluation Strategy Template](evaluation-strategy-template.yaml)

---

## Cross-References

- **Defining Acceptance Criteria:** [defining-acceptance-criteria.md](defining-acceptance-criteria.md) -- how to use these metrics as acceptance criteria
- **Evaluation Strategy Template:** [evaluation-strategy-template.yaml](evaluation-strategy-template.yaml) -- where selected metrics are documented
- **Eval-Driven Development:** [../../02-development-governance/evaluations/eval-driven-development.md](../../02-development-governance/evaluations/eval-driven-development.md) -- how metrics become automated eval suites
- **Continuous Online Evaluation:** [../../03-runtime-governance/evaluations/continuous-online-evaluation.md](../../03-runtime-governance/evaluations/continuous-online-evaluation.md) -- how metrics are monitored in production
- **Multi-Agent Governance:** [../../03-runtime-governance/agentic-workflows/multi-agent-governance-framework.md](../../03-runtime-governance/agentic-workflows/multi-agent-governance-framework.md) -- additional metrics for multi-agent systems
- **Glossary:** [../../05-cross-cutting/glossary.md](../../05-cross-cutting/glossary.md) -- definitions of technical terms used in this catalog
- **Risk Tiering Model:** [../../07-enterprise-implementation/risk-based-adoption/risk-tiering-model.md](../../07-enterprise-implementation/risk-based-adoption/risk-tiering-model.md) -- governance requirements by tier

---

*Last updated: 2026-02-28*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
