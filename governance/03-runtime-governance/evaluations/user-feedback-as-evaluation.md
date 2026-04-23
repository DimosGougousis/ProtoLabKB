# User Feedback as Evaluation

## Purpose

This document defines how to incorporate user feedback signals -- both explicit and implicit -- into the continuous evaluation loop for customer-facing AI agents. In regulated FinTech, user feedback is not merely a product improvement input; it is a governance-grade signal that validates whether agents are meeting acceptance criteria, regulatory obligations, and customer outcome expectations in production.

Traditional LLM evaluation relies on offline benchmarks and automated metrics. User feedback closes the gap between what evaluations measure and what customers actually experience. When a customer retries a question, abandons a session, or corrects the agent, that behaviour is evaluation data that no synthetic test suite can replicate.

## When to Use

- When designing the evaluation strategy for any customer-facing AI agent
- When setting up production monitoring and observability pipelines
- When defining KPIs and SLAs for agents in the fleet registry
- When investigating performance degradation or rising escalation rates
- When conducting periodic revalidation of agent quality (SAFEST S-20)
- When building the feedback-to-eval pipeline for continuous improvement

## Who Is Responsible

| Role | R/A/C/I | Responsibility |
|------|---------|---------------|
| **Model Owner** | Accountable | Defines which feedback signals are collected and how they map to evaluation criteria |
| **AI/ML Engineer** | Responsible | Implements feedback collection, pipeline processing, and integration with eval frameworks |
| **Product Manager** | Consulted | Defines customer experience quality expectations; interprets feedback trends |
| **MLOps / Platform Engineer** | Responsible | Operates feedback ingestion pipelines and observability infrastructure |
| **Compliance Officer (2nd Line)** | Reviewer | Validates that feedback collection complies with GDPR consent requirements and data minimization |
| **Data Analyst** | Responsible | Performs statistical analysis on feedback data; detects bias and significance issues |

## Regulatory Basis

- **EU AI Act Article 72** -- Post-market monitoring system must include collection and analysis of user feedback
- **EU AI Act Article 9(3)** -- Risk management system must account for risks identified from real-world use
- **GDPR Article 6** -- Lawful basis for processing feedback data (legitimate interest or consent)
- **GDPR Articles 13-14** -- Information obligations when collecting feedback data from users
- **SAFEST S-20** -- Periodic revalidation using production performance evidence
- **SAFEST T-15** -- AI performance dashboards incorporating user experience metrics
- **SAFEST F-11** -- Fairness monitoring informed by differential feedback patterns across user segments
- **DNB Good Practice** -- Continuous monitoring including customer outcome assessment

---

## 1. Feedback Signal Taxonomy

### 1.1 Explicit Feedback Signals

Explicit feedback is intentionally provided by the user through structured interaction elements.

| Signal | Collection Method | Strength | Limitation |
|--------|------------------|----------|------------|
| **Thumbs up / thumbs down** | In-chat button after each agent response | Low friction; high volume; binary quality signal | No nuance; subject to position bias (users more likely to rate bad experiences) |
| **Star rating (1-5)** | Post-interaction survey prompt | More granular than binary; familiar pattern | Higher friction; lower response rate; central tendency bias |
| **Free-text comment** | Optional comment field with rating | Rich qualitative signal; captures failure modes not anticipated by eval suite | Low volume; requires NLP processing; may contain PII |
| **Topic-specific rating** | Multi-dimension survey (accuracy, helpfulness, speed, clarity) | Diagnostic power -- identifies which aspect failed | Survey fatigue; very low completion rates beyond 3 questions |
| **CSAT (Customer Satisfaction Score)** | Post-interaction "How satisfied were you?" (1-5 or 1-7 scale) | Industry-standard; benchmarkable | Lagging indicator; not specific to individual agent responses |
| **CES (Customer Effort Score)** | "How easy was it to resolve your issue?" (1-7) | Measures friction, which correlates with agent effectiveness | Single-dimensional; misses accuracy issues |

### 1.2 Implicit Feedback Signals

Implicit feedback is inferred from user behaviour without requiring deliberate action.

| Signal | Detection Method | What It Indicates | FinTech Example |
|--------|-----------------|-------------------|-----------------|
| **Retry rate** | User rephrases the same question within the same session | Agent failed to understand or answer correctly | Customer asks "What's my balance?" then "Show me how much money I have" |
| **Escalation request** | User explicitly asks for a human agent | Agent unable to meet the user's need or trust threshold | "I want to speak to a real person about this payment" |
| **Session abandonment** | User leaves mid-conversation without resolution | Agent failed or frustrated the user | Customer drops off after 3 failed attempts to initiate a payment |
| **Correction patterns** | User corrects the agent's output | Agent provided incorrect information | "No, my address is X, not Y" |
| **Repeated interactions** | Same user returns for the same issue within 24-48 hours | Issue was not actually resolved | Customer contacts support again about the same failed transfer |
| **Task completion without confirmation** | User does not confirm a completed action or ignores suggestions | Agent's output was irrelevant or unhelpful | Agent suggests account type but customer switches to a different page |
| **Time to resolution** | Elapsed time from first message to issue resolution | Longer times suggest agent inefficiency or confusion | 15-minute session for a balance inquiry that should take 30 seconds |
| **Message count per session** | Number of conversational turns before resolution | High turn count suggests agent is not converging on the answer | 12 messages to answer a simple account question |
| **Copy-paste from agent** | User copies the agent's response (in web interfaces) | Indicates the response was useful and actionable | Customer copies IBAN or transaction reference |
| **Click-through on links** | User clicks on links or resources provided by the agent | Agent's recommendations were relevant | Customer clicks on the "Schedule a callback" link |

---

## 2. Feedback-to-Evaluation Pipeline

### 2.1 Pipeline Architecture

```
User Interaction
    |
    v
+----------------------------+
| FEEDBACK COLLECTION LAYER  |
| - Explicit: ratings, text  |
| - Implicit: behavior logs  |
+----------------------------+
    |
    v
+----------------------------+
| INGESTION AND ENRICHMENT   |
| - PII scrubbing            |
| - Session context linking  |
| - Agent version tagging    |
| - Timestamp normalization  |
+----------------------------+
    |
    v
+----------------------------+
| ANALYSIS ENGINE            |
| - Sentiment classification |
| - Topic extraction         |
| - Statistical aggregation  |
| - Bias detection           |
+----------------------------+
    |
    v
+----------------------------+
| EVAL INTEGRATION LAYER     |
| - Map to KPI metrics       |
| - Feed eval dashboards     |
| - Trigger alert thresholds |
| - Update eval datasets     |
+----------------------------+
    |
    v
+----------------------------+
| GOVERNANCE OUTPUTS         |
| - Fleet dashboard KPIs     |
| - Drift detection signals  |
| - Retraining triggers      |
| - Compliance evidence      |
+----------------------------+
```

### 2.2 Pipeline Processing Steps

| Step | Description | Tools / Platform | Owner |
|------|-------------|-----------------|-------|
| **1. Collection** | Capture explicit and implicit signals with session ID, agent ID, timestamp, agent version | Application SDK, event tracking | AI/ML Engineer |
| **2. PII Scrubbing** | Remove or mask personal data from free-text feedback before processing | Presidio, custom regex pipeline | MLOps Engineer |
| **3. Enrichment** | Link feedback to session metadata: agent_id, model_version, interaction type, user segment | Observability platform (LangSmith, Arize Phoenix, Langfuse) | MLOps Engineer |
| **4. Storage** | Store processed feedback in analytics warehouse with retention per GDPR requirements | Data warehouse (BigQuery, Snowflake) | Data Engineer |
| **5. Analysis** | Aggregate, trend, segment; run statistical significance tests | Analytics pipeline (dbt, Python) | Data Analyst |
| **6. Eval mapping** | Convert feedback aggregates into eval metrics; update KPI dashboards | Eval framework integration | AI/ML Engineer |
| **7. Alerting** | Trigger alerts when feedback-derived metrics breach warning/critical thresholds | Alerting system (PagerDuty, Opsgenie) | MLOps Engineer |

### 2.3 Observability Platform Integration

Feedback data must be correlated with trace-level observability data to enable root cause analysis.

| Platform | Integration Pattern | What It Adds |
|----------|-------------------|-------------|
| **LangSmith** | Attach feedback scores to traced runs via `run_id`; use feedback API | Links user satisfaction to specific LLM calls, tool invocations, and prompt variants |
| **Arize Phoenix** | Stream feedback as evaluation labels on production traces | Enables drill-down from low-satisfaction sessions to specific failure points |
| **Langfuse** | Use Langfuse scores API to attach feedback ratings to generations | Correlates feedback with token usage, latency, and model version |
| **Opik** | Log feedback as experiment metrics alongside model outputs | Supports A/B comparisons of user feedback across model versions |

---

## 3. Sentiment Analysis on Free-Text Feedback

### 3.1 Classification Model

Free-text feedback must be classified into actionable categories:

| Category | Examples | Action |
|----------|----------|--------|
| **Accuracy complaint** | "Wrong balance", "That's not my transaction" | Flag for factual grounding review; check data source integration |
| **Helpfulness complaint** | "You didn't answer my question", "That's not what I asked" | Flag for intent alignment review; check retrieval relevance |
| **Safety concern** | "You shouldn't have said that", "That advice could lose me money" | Immediate flag for safety review; possible incident report |
| **Speed complaint** | "This is taking too long", "Why so slow?" | Flag for latency investigation; check performance KPIs |
| **Positive feedback** | "That was exactly what I needed", "Very helpful" | Log as positive signal; use for eval dataset curation |
| **Feature request** | "Can you also show my credit card balance?" | Route to product backlog; not an eval signal |

### 3.2 Sentiment Processing Requirements

- Use a dedicated sentiment classification model (not the production LLM) to avoid self-evaluation bias.
- Classification must support the languages in which the agent operates.
- Confidence threshold for automated classification: >= 0.80. Below that, route to human review queue.
- Sentiment classification results are stored alongside the original feedback for audit purposes.

---

## 4. Statistical Significance and Sample Size

### 4.1 Minimum Sample Requirements

| Decision Type | Minimum Sample Size | Significance Level | Power | Notes |
|---------------|--------------------|--------------------|-------|-------|
| **Is the agent meeting its CSAT target?** | 385 ratings per measurement period | alpha = 0.05 | 0.80 | For +/- 5% margin of error on a 1-5 scale |
| **Has CSAT changed between model versions?** | 500 per version | alpha = 0.05 | 0.80 | Two-sample t-test; detects 0.2-point difference |
| **A/B test on feedback-derived metric** | Depends on effect size; minimum 1,000 per variant | alpha = 0.05 | 0.80 | See [A/B Testing for AI](ab-testing-for-ai.md) for sample size calculators |
| **Weekly trend detection** | 200+ ratings per week | -- | -- | Below 200, trends are unreliable; report with confidence intervals |

### 4.2 Reporting with Confidence Intervals

All feedback-derived metrics reported on dashboards must include confidence intervals:

- CSAT: report as "4.2 (+/- 0.1, 95% CI)" not just "4.2"
- Thumbs-up rate: report as "78% (+/- 3%, 95% CI)" not just "78%"
- When sample sizes are below minimum thresholds, display a warning indicator on the dashboard

---

## 5. Feedback Bias Mitigation

### 5.1 Known Biases in User Feedback

| Bias | Description | Mitigation |
|------|-------------|-----------|
| **Negativity bias** | Users are more likely to provide feedback after negative experiences than positive ones | Weight positive implicit signals (task completion, copy-paste) alongside explicit feedback; compare explicit-to-implicit ratio |
| **Selection bias** | Users who provide feedback are not representative of all users | Monitor feedback response rate; segment by user profile; compare behaviour of respondents vs. non-respondents |
| **Position bias** | Users rate the last response in a session, not the overall experience | Collect per-turn feedback where possible, not just end-of-session |
| **Acquiescence bias** | Users tend to agree or give positive ratings when asked | Use balanced scales; include both positive and negative anchor text |
| **Cultural bias** | Rating scales are interpreted differently across cultures | Normalize ratings by user locale; use behaviour-based (implicit) signals for cross-cultural comparison |
| **Extremity bias** | Users tend to give extreme ratings (1 or 5) and skip middle values | Report median alongside mean; use trimmed means for trend analysis |

### 5.2 Bias-Corrected Feedback Score

Calculate a composite feedback score that blends explicit and implicit signals to reduce individual bias effects:

```
Composite Score = w1 * normalized_explicit_score
               + w2 * (1 - retry_rate)
               + w3 * (1 - escalation_rate)
               + w4 * task_completion_rate
               + w5 * (1 - abandonment_rate)

Where: w1 + w2 + w3 + w4 + w5 = 1.0
Default weights: w1=0.30, w2=0.15, w3=0.15, w4=0.25, w5=0.15
```

Weights are calibrated per agent based on the relative informativeness of each signal in that agent's context. Calibration is reviewed quarterly.

---

## 6. Mapping Feedback to Eval Metrics

### 6.1 Feedback-to-KPI Mapping

| Feedback Signal | Maps to KPI | Dashboard Metric | Alert Condition |
|----------------|-------------|-----------------|-----------------|
| Thumbs down rate | Task quality | "Negative Feedback Rate" | > 15% over rolling 24h |
| CSAT score | User satisfaction | "CSAT Score" | < 4.0 (warning), < 3.5 (critical) |
| Retry rate | Task completion quality | "Retry Rate" | > 10% over rolling 4h |
| Escalation request rate | Agent capability | "Escalation Rate" | > 20% (warning), > 30% (critical) |
| Abandonment rate | Agent effectiveness | "Session Abandonment Rate" | > 25% over rolling 24h |
| Correction frequency | Factual accuracy | "User Correction Rate" | > 5% (warning), > 10% (critical) |
| Repeat interaction rate | Resolution quality | "Return Contact Rate (48h)" | > 15% over rolling 7 days |
| Negative sentiment in free text | Safety / quality | "Negative Sentiment Rate" | Spike > 2x baseline |

### 6.2 Feedback as Eval Dataset Source

User interactions with negative feedback become candidates for inclusion in the agent's evaluation dataset:

1. **Identify failing interactions:** Interactions with thumbs-down, corrections, escalation requests, or low CSAT
2. **Scrub PII:** Remove all personal data from the interaction record
3. **Annotate:** Have a human reviewer label the interaction with the failure mode (accuracy, helpfulness, safety, etc.)
4. **Add to eval suite:** Include as a test case in the agent's regression eval suite
5. **Verify fix:** When the failure is addressed, the new eval case must pass before deployment

This creates a continuously growing, production-grounded evaluation dataset that reflects real user needs.

---

## 7. FinTech Examples

### 7.1 Payments Agent Feedback Loop

| Scenario | Feedback Signal | Eval Action |
|----------|----------------|-------------|
| Customer initiates a EUR 500 transfer; agent confirms success, but transfer fails | Customer returns within 24h to report the issue (repeat interaction) + thumbs down | Add to eval dataset as "false confirmation" test case; investigate data source reliability |
| Customer asks for transaction history; agent shows wrong date range | Customer corrects: "I meant last month, not this month" (correction pattern) | Flag as intent misunderstanding; add date-range disambiguation test cases |
| Customer asks about FX rates; agent provides a rate that is 2 hours old | Customer escalates to human who provides the current rate | Add to eval dataset; review FX data source freshness requirements |

### 7.2 KYC/Onboarding Agent Feedback Loop

| Scenario | Feedback Signal | Eval Action |
|----------|----------------|-------------|
| Document upload fails silently; agent proceeds without verification | Customer receives rejection email (repeat interaction + complaint) | Investigate error handling in document processing pipeline; add test case |
| Agent requests information the customer already provided in a previous step | Customer frustration: "I already told you that" (correction + retry) | Review context window management; add multi-turn memory test cases |
| Agent gives incorrect information about required documents for non-EU nationals | Customer provides wrong documents, causing delay | Add as regulatory accuracy test case; verify knowledge base completeness |

---

## 8. Feedback Collection Compliance

### 8.1 GDPR Requirements

| Requirement | Implementation |
|-------------|----------------|
| **Lawful basis** | Legitimate interest for operational feedback; explicit consent for free-text that may contain personal opinions |
| **Data minimization** | Collect only the minimum feedback needed; do not require free-text comments |
| **Retention** | Feedback data retained for 24 months maximum; anonymized aggregates may be retained longer |
| **Right of erasure** | Users can request deletion of their feedback; feedback pipeline must support erasure by user ID |
| **Transparency** | Privacy notice must explain that feedback is used to improve AI systems |
| **PII in free text** | Free-text feedback is PII-scrubbed before storage and analysis |

### 8.2 Feedback Collection UX

- Feedback prompts must be non-intrusive and optional. Never block the user's workflow to collect feedback.
- Do not prompt for feedback on every interaction. Use sampling (e.g., every 5th interaction) to avoid survey fatigue.
- Clearly state how feedback will be used: "Your feedback helps us improve this service."
- Provide an opt-out mechanism for recurring feedback prompts.

---

## 9. Feedback Review Cadence

| Activity | Frequency | Who | Output |
|----------|-----------|-----|--------|
| **Dashboard review** | Daily | Model Owner | Spot anomalies; trigger investigation if thresholds breached |
| **Trend analysis** | Weekly | Data Analyst + Model Owner | Weekly feedback summary; trend direction for all feedback KPIs |
| **Bias audit** | Monthly | Data Analyst + Compliance | Check for differential feedback patterns across user segments |
| **Eval dataset refresh** | Monthly | AI/ML Engineer | New eval cases from negative-feedback interactions added to suite |
| **Feedback pipeline health check** | Monthly | MLOps Engineer | Verify collection rates, pipeline latency, data quality |
| **Composite score calibration** | Quarterly | Model Owner + Data Analyst | Review and update feedback signal weights |
| **Governance review** | Quarterly | 2nd Line Compliance | Review feedback governance compliance; audit evidence |

---

## Cross-References

- **Continuous Online Evaluation:** [continuous-online-evaluation.md](continuous-online-evaluation.md) -- monitoring infrastructure that feedback feeds into
- **Agent Performance Evaluations:** [agent-performance-evals.md](agent-performance-evals.md) -- KPI definitions that feedback signals map to
- **A/B Testing for AI:** [ab-testing-for-ai.md](ab-testing-for-ai.md) -- statistical methodology for comparing feedback across variants
- **Agent Fleet Operations:** [../agentic-workflows/agent-fleet-operations.md](../agentic-workflows/agent-fleet-operations.md) -- dashboard integration for feedback-derived KPIs
- **Customer-Facing Agent Safety:** [../agentic-workflows/customer-facing-agent-safety.md](../agentic-workflows/customer-facing-agent-safety.md) -- safety signals that feedback may surface
- **Defining Acceptance Criteria:** [../../01-discovery-governance/evaluations/defining-acceptance-criteria.md](../../01-discovery-governance/evaluations/defining-acceptance-criteria.md) -- thresholds that feedback metrics validate
- **Traceability with LangChain:** [../../04-operational-governance/guides/traceability-with-langchain.md](../../04-operational-governance/guides/traceability-with-langchain.md) -- observability platforms referenced for feedback correlation
- **Glossary:** [../../05-cross-cutting/glossary.md](../../05-cross-cutting/glossary.md) -- definitions for CSAT, CES, implicit feedback, sentiment analysis

---

*Last updated: 2026-03-01* / *Version: 1.0* / *Classification: Internal / Regulatory Preparation*
