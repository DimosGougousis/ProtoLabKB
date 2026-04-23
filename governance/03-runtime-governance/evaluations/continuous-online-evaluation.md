# Continuous Online Evaluation

## Purpose

This guide defines how to evaluate AI systems continuously in production. Pre-deployment testing validates the system on historical data under controlled conditions. Continuous online evaluation validates the system on **real traffic, real users, and real-world dynamics** over time. It catches problems that offline testing cannot: data drift, concept drift, unexpected user behavior, emerging failure modes, and gradual performance degradation.

Without continuous evaluation, you discover problems from customer complaints, regulatory investigations, or media reports -- not from data.

## When to Use

- From the moment an AI system enters production until it is decommissioned
- When deploying a new version of an existing AI system (shadow mode, canary)
- When monitoring for drift, degradation, or emerging failure patterns
- When collecting user feedback to validate AI system quality
- When running A/B tests to compare AI system variants

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **MLOps / Platform Engineer** | **Responsible** -- implements and operates the monitoring infrastructure |
| **Model Owner** | **Accountable** -- defines what is monitored, reviews alerts, makes intervention decisions |
| **On-Call Engineer** | **Responsible** -- first responder for production monitoring alerts |
| **Compliance Officer (2nd Line)** | **Reviewer** -- reviews fairness monitoring dashboards; escalates concerns |
| **AI Governance Committee** | **Informed** -- receives periodic evaluation summaries; approves changes triggered by monitoring |

## Regulatory Basis

- **EU AI Act Article 72** -- Post-market monitoring system for high-risk AI systems
- **EU AI Act Article 9(3)** -- Risk management throughout the AI system lifecycle
- **SAFEST items S-12** (drift detection), **S-20** (periodic revalidation), **F-11** (fairness monitoring), **A-11** (audit trail)
- **DNB Good Practice** -- Continuous monitoring of model performance in production

---

## 1. Online vs. Offline Evaluation

| Dimension | Offline Evaluation | Online Evaluation |
|-----------|-------------------|-------------------|
| **Data** | Historical holdout set, curated test cases | Live production traffic |
| **When** | Before deployment, periodically on schedule | Continuously while system is live |
| **Environment** | Controlled test environment | Real production environment with real users |
| **What it catches** | Known failure modes, regression on benchmarks | Emerging failures, drift, user behavior changes, real-world edge cases |
| **Labels** | Available immediately (pre-labeled test data) | Often delayed (outcome labels arrive later) or unavailable (require human annotation) |
| **Speed** | Fast (run on demand) | Slow (requires time to accumulate traffic and outcomes) |
| **Limitation** | Misses real-world dynamics | More expensive; harder to run controlled experiments |

**Both are necessary.** Offline evaluation provides fast feedback during development. Online evaluation provides ground-truth validation in production. Neither alone is sufficient.

---

## 2. Deployment Strategies for Safe Evaluation

### 2.1 Shadow Mode

**What it is:** The new AI system runs alongside the existing system (or human process), processing the same inputs, but its outputs are logged without being shown to users or acted upon.

**When to use:** First-time deployment of a new AI system; major model version changes for high-risk systems.

```
  Customer Input
       |
       +----> Existing System ----> Serves the customer (production)
       |
       +----> New AI System ------> Outputs logged only (shadow)
                                         |
                                         v
                                    Compare outputs:
                                    - Agreement rate
                                    - Quality metrics
                                    - Fairness metrics
```

**Governance requirements:**
- Shadow mode duration: minimum 2 weeks for limited risk; minimum 4 weeks for high risk
- Compare shadow outputs to existing system / ground truth on all acceptance criteria
- Proceed to canary only when shadow metrics meet or exceed thresholds
- Log shadow outputs for audit trail evidence

### 2.2 Canary Deployment

**What it is:** The new AI system serves a small percentage of production traffic (e.g., 5-10%), while the existing system handles the rest. Performance is compared between the two populations.

**When to use:** After shadow mode confirms acceptable performance; when you need real user interaction data.

```
  Customer Traffic
       |
       +---- 95% ----> Existing System (control)
       |
       +---- 5% -----> New AI System (canary)
                              |
                              v
                         Monitor:
                         - All acceptance criteria
                         - Error rates vs. control
                         - User satisfaction vs. control
                         - Fairness across groups
```

**Governance requirements:**
- Start at 5% traffic; increase in stages (5% -> 25% -> 50% -> 100%) only if metrics hold
- Each stage requires minimum 48 hours of stable metrics
- Automatic rollback if any hard-gate metric breaches its threshold
- For high-risk systems: 2nd line review at each traffic increase stage

### 2.3 A/B Testing

**What it is:** Controlled experiment comparing two or more AI system variants to determine which performs better on specified metrics. Users are randomly assigned to variants.

**When to use:** Comparing model versions, prompt strategies, guardrail configurations, or agent behaviors.

**Governance requirements:**
- Define primary and secondary metrics before the test starts (not after)
- Specify minimum sample size for statistical significance
- Run for sufficient duration to capture temporal patterns (weekday/weekend, beginning/end of month)
- For customer-facing experiments: ensure all variants meet minimum safety and fairness thresholds (no variant is allowed to be unsafe, even experimentally)
- Document results and decision in the model change log

---

## 3. Real-Time Metric Monitoring

### 3.1 What to Monitor

Monitor the same metrics defined in your [Evaluation Strategy](../../01-discovery-governance/evaluations/evaluation-strategy-template.yaml), adapted for real-time production data.

| Metric Category | Examples | Monitoring Frequency | Data Source |
|-----------------|----------|---------------------|-------------|
| **AI Quality** | Prediction confidence distribution, output consistency, latency | Real-time (per request or per minute) | Production logs |
| **Product** | Task completion rate, escalation rate, user satisfaction signals | Near-real-time (per hour or per day) | Interaction logs, feedback signals |
| **Safety** | Safety violation count, guardrail trigger rate, prompt injection attempt rate | Real-time (per request) | Guardrail logs |
| **Fairness** | Metric values per protected group | Daily or weekly (requires sufficient sample per group) | Production logs stratified by group |
| **Data Quality** | Input feature distributions, missing value rates, out-of-range inputs | Real-time | Data pipeline monitoring |
| **Business** | Cost per decision, false positive/negative rates (when outcome labels available) | Daily or weekly | Outcome data, financial data |

### 3.2 Proxy Metrics for Delayed Labels

In many production settings, ground truth labels are not immediately available (e.g., you do not know if a transaction was truly fraudulent until days later). Use proxy metrics for real-time monitoring:

| Delayed Label | Proxy Metric | Rationale |
|--------------|-------------|-----------|
| Fraud confirmed (days later) | Prediction confidence distribution, customer dispute rate | Shifts in confidence distribution may indicate drift; increased disputes may indicate false positives rising |
| Customer satisfaction (post-survey, delayed) | Escalation rate, session length, repeat contact rate | Operational metrics correlate with satisfaction and are available immediately |
| Default outcome (months later) | Application score distribution, early payment behavior | Score distribution shifts indicate model behavior change |
| AML alert quality (weeks later) | Alert volume, analyst override rate | Sudden changes in volume or override rates indicate model behavior change |

---

## 4. User Feedback Loops

### 4.1 Explicit Feedback

| Feedback Type | Implementation | How to Use |
|--------------|----------------|------------|
| **Thumbs up / down** | Simple binary rating after each AI interaction | Track approval rate over time; investigate drops; sample downvoted interactions for root cause analysis |
| **Star rating** | 1-5 star rating after task completion | More granular than binary; enables trend analysis and comparison across features |
| **Free-text feedback** | Optional comment field after interaction | Rich qualitative data; sample and categorize regularly; use for eval suite improvement |
| **Correction / override** | User corrects the AI output (e.g., recategorizes a transaction) | Direct signal of AI error; use as labeled data for retraining and eval suite expansion |

### 4.2 Implicit Feedback

| Signal | What It Indicates | How to Capture |
|--------|-------------------|----------------|
| **Escalation to human** | AI could not handle the interaction | Log escalation events with context |
| **Repeated query** | AI response was insufficient or wrong | Detect repeat queries within a session |
| **Session abandonment** | User gave up on the AI interaction | Track incomplete sessions |
| **Time on task** | Unusually long or short interactions may indicate confusion or irrelevance | Log interaction duration |
| **Click-through rate** | Whether users act on AI recommendations | Track actions following AI suggestions |

### 4.3 Feedback Governance

- **Sampling:** Not all feedback needs human review. Establish a sampling strategy (e.g., review 100% of 1-star ratings, 10% of 3-star, 1% of 5-star).
- **Response time:** Negative feedback patterns must trigger investigation within the response times defined in the [Evaluation Strategy escalation thresholds](../../01-discovery-governance/evaluations/evaluation-strategy-template.yaml).
- **Feedback loop to evals:** Every confirmed AI error from user feedback should become a new test case in the eval suite. This prevents regression and continuously strengthens the evaluation.
- **Bias in feedback:** User feedback may be biased (e.g., certain demographics more likely to leave feedback). Monitor feedback sample composition and adjust interpretation accordingly.

---

## 5. Alerting Thresholds and Response Procedures

### 5.1 Alert Levels

| Level | Definition | Trigger Example | Response |
|-------|-----------|-----------------|----------|
| **Info** | Normal operation; metric fluctuation within expected range | Daily metric summary shows all green | No action; log for trend analysis |
| **Warning** | Metric trending toward threshold but not yet breached | Precision dropped from 0.94 to 0.92 (threshold is 0.90) for 3 consecutive days | Model Owner investigates within 2 business days; check for data drift, upstream changes |
| **Breach** | Metric has crossed its defined threshold | Precision = 0.88, below threshold of 0.90 | Model Owner and 2nd Line notified within 4 hours. Determine: can we fix quickly, or must we roll back? |
| **Critical** | Safety-critical metric breached; immediate harm possible | Safety violation detected in production; guardrail bypassed | Immediate action (< 1 hour). Activate kill switch or rollback. Incident declared. Committee notified. |

### 5.2 Response Procedure

```
  Alert Received
       |
       v
  Is it CRITICAL?
       |
       +-- YES --> Activate circuit breaker / rollback
       |           Declare incident
       |           Notify Governance Committee
       |           Begin root cause analysis
       |
       +-- NO
            |
            Is it a BREACH?
            |
            +-- YES --> Notify Model Owner + 2nd Line
            |           Investigate root cause (within 4 hours)
            |           Determine: rollback, fix, or accept temporarily?
            |           If accept: document justification, set deadline for fix
            |
            +-- NO
                 |
                 Is it a WARNING?
                 |
                 +-- YES --> Model Owner reviews trend
                 |           Check: data drift? upstream change? seasonal?
                 |           Plan remediation if trend continues
                 |
                 +-- NO --> Log for trend analysis. No immediate action.
```

---

## 6. Dashboard Specification

### 6.1 Required Dashboards

| Dashboard | Audience | Content | Refresh Rate |
|-----------|----------|---------|-------------|
| **System Health** | Model Owner, On-Call | Real-time metric values vs. thresholds with red/amber/green status | Per minute |
| **Trend Analysis** | Model Owner, 2nd Line | 30/90/365-day metric trends with threshold lines and anomaly highlights | Daily |
| **Fairness Monitor** | Compliance, 2nd Line | Fairness metrics per protected group over time; demographic parity ratios | Weekly |
| **User Feedback** | Product Manager, Model Owner | Feedback scores, sentiment trends, top complaint categories | Daily |
| **Alert History** | On-Call, Model Owner | Alert timeline: when fired, who acknowledged, what action taken, resolution | Real-time |
| **Business Impact** | Product Manager, Executive | Business KPIs attributable to the AI system (cost savings, automation rate, error costs) | Weekly |

### 6.2 Dashboard Data Sources

| Data Source | What It Provides |
|-------------|-----------------|
| Production logs | Request/response data, latency, error rates |
| Guardrail logs | Safety filter triggers, blocked requests, injection attempts |
| Eval pipeline output | Periodic eval results against acceptance criteria |
| Feedback database | User ratings, corrections, escalation signals |
| Feature store / data pipeline | Input feature distributions for drift detection |
| Business systems | Outcome labels (when available), financial impact data |

---

## 7. Periodic Revalidation

In addition to real-time monitoring, conduct scheduled comprehensive evaluations:

| Cadence | Scope | Who Runs It | Applies To |
|---------|-------|-------------|------------|
| **Weekly** | LLM instruction following, safety eval, prompt injection resistance | AI/ML Engineer | LLM-based systems |
| **Monthly** | Full eval suite on production traffic sample; user feedback analysis | Model Owner | All systems |
| **Quarterly** | Full eval suite + fairness evaluation + 2nd line review | Model Owner + 2nd Line | Limited and high-risk systems |
| **Annually** | Full revalidation including risk reclassification review | 2nd Line + AI Governance Committee | All systems (mandatory) |
| **Triggered** | Full revalidation after material changes (data, model, scope) | Model Owner + 2nd Line | All tiers |

---

## Cross-References

- **Evaluation Strategy Template:** [../../01-discovery-governance/evaluations/evaluation-strategy-template.yaml](../../01-discovery-governance/evaluations/evaluation-strategy-template.yaml) -- defines the metrics, thresholds, and escalation rules monitored in production
- **Defining Acceptance Criteria:** [../../01-discovery-governance/evaluations/defining-acceptance-criteria.md](../../01-discovery-governance/evaluations/defining-acceptance-criteria.md) -- source of the acceptance thresholds used as monitoring targets
- **AI Quality Metrics Catalog:** [../../01-discovery-governance/evaluations/ai-quality-metrics-catalog.md](../../01-discovery-governance/evaluations/ai-quality-metrics-catalog.md) -- reference for metrics used in production monitoring
- **Eval-Driven Development:** [../../02-development-governance/evaluations/eval-driven-development.md](../../02-development-governance/evaluations/eval-driven-development.md) -- the eval suites adapted for continuous production use
- **Eval Gate Integration:** [../../02-development-governance/evaluations/eval-gate-integration.md](../../02-development-governance/evaluations/eval-gate-integration.md) -- CI/CD gates that complement production monitoring
- **Multi-Agent Governance:** [../agentic-workflows/multi-agent-governance-framework.md](../agentic-workflows/multi-agent-governance-framework.md) -- additional monitoring requirements for agent systems
- **Operational Governance:** [../../04-operational-governance/](../../04-operational-governance/) -- incident response when monitoring detects problems
- **Risk Tiering Model:** [../../07-enterprise-implementation/risk-based-adoption/risk-tiering-model.md](../../07-enterprise-implementation/risk-based-adoption/risk-tiering-model.md) -- monitoring intensity by risk tier

---

*Last updated: 2026-02-28*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
