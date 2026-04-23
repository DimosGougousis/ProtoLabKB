# Product Success Metrics for AI Systems

## Purpose

This guide defines product-level evaluation metrics that measure whether an AI system delivers real value to users and the business. While [AI Quality Metrics](ai-quality-metrics-catalog.md) focus on technical model performance (accuracy, F1, AUC), product success metrics answer the higher-order question: **does this AI feature actually help users accomplish their goals and generate business outcomes?**

Product success metrics bridge the gap between "the model works" and "the product succeeds." A model with 99% accuracy that users ignore or distrust is a product failure. These metrics catch that.

## When to Use

- During Discovery Governance, when defining acceptance criteria for new AI features
- When building a business case for AI investment (ROI justification)
- During [continuous online evaluation](../../03-runtime-governance/evaluations/continuous-online-evaluation.md) to track production value delivery
- When deciding whether to iterate, pivot, or retire an AI feature
- During quarterly governance reviews (see [governance-in-quarterly-planning.md](../../07-enterprise-implementation/process-integration/governance-in-quarterly-planning.md))

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **Product Manager** | **Accountable** -- defines product success metrics aligned with business objectives |
| **AI/ML Engineer** | **Responsible** -- instruments metrics collection, builds dashboards |
| **UX Researcher** | **Consulted** -- designs user satisfaction studies, interprets behavioral data |
| **Business Stakeholder** | **Consulted** -- validates that metrics align with strategic goals |

## Regulatory Basis

- **EU AI Act Article 9(2)(b)** -- Risk management must consider risks when the system is used under intended purpose
- **SAFEST items S-03** (acceptance criteria), **A-01** (accountability for outcomes), **T-01** (transparency to users)
- **DNB Good Practice** -- AI systems must demonstrate measurable value aligned with organizational objectives

---

## 1. Task Completion Metrics

These measure whether users can accomplish their intended goals when interacting with AI features.

| Metric | Definition | Measurement Method | FinTech Example |
|--------|-----------|-------------------|-----------------|
| **Task Success Rate** | Percentage of user tasks completed successfully with AI assistance | Event logging: task_started vs. task_completed | 85% of users who start a loan application with AI pre-fill complete the application |
| **Time-to-Task-Completion** | Average time to complete a task with AI vs. without | A/B test comparing AI-assisted vs. manual flows | AI-assisted KYC verification completes in 3 min vs. 12 min manual |
| **Error Rate** | Percentage of tasks where user must correct AI output | Track edit/override events on AI-generated content | Users correct AI-suggested transaction categories 8% of the time |
| **Automation Rate** | Percentage of tasks fully automated without human intervention | Count tasks completed without human review or override | 72% of low-risk payment disputes resolved fully autonomously |
| **First-Contact Resolution** | Percentage of customer interactions resolved in a single session | Session tracking with outcome tagging | AI chatbot resolves 65% of customer queries without human escalation |

### How to Set Thresholds

1. **Baseline first:** Measure the metric without AI (manual process) for at least 30 days
2. **Minimum viable improvement:** AI must improve the baseline by at least 15% to justify deployment cost
3. **Regression threshold:** If the metric drops below baseline, trigger an immediate review
4. **Target:** Set aspirational targets based on industry benchmarks or business case assumptions

---

## 2. User Satisfaction Metrics

These capture subjective user experience with AI features.

| Metric | Definition | Measurement Method | Target Range |
|--------|-----------|-------------------|--------------|
| **Trust Score** | User-reported confidence in AI recommendations on a 1-5 scale | Post-interaction survey (e.g., "How confident are you in this recommendation?") | >= 3.8 / 5.0 |
| **Net Promoter Score (NPS)** | Likelihood to recommend the AI-powered feature | Standard NPS survey at regular intervals | >= +30 for AI features |
| **System Usability Scale (SUS)** | Standardized measure of perceived usability | 10-item SUS questionnaire | >= 72 (above average) |
| **AI Helpfulness Rating** | User rating of whether AI assistance was helpful | Thumbs up/down or 1-5 star rating after AI interaction | >= 80% positive |
| **Escalation Sentiment** | User satisfaction when escalated from AI to human | Post-escalation survey | >= 3.5 / 5.0 (escalation should not feel like failure) |

### Avoiding Survey Fatigue

- Sample 5-10% of interactions for surveys, not every interaction
- Rotate survey questions to cover different dimensions over time
- Use passive signals (time-on-task, click-through, return usage) as proxies between active surveys
- Trigger contextual micro-surveys (single question) rather than full questionnaires

---

## 3. Business Impact Metrics

These connect AI feature performance to organizational objectives.

| Metric | Definition | Measurement Method | FinTech Example |
|--------|-----------|-------------------|-----------------|
| **Revenue Impact** | Revenue directly attributable to AI feature | Attribution modeling or A/B test with revenue tracking | AI-powered cross-sell recommendations generate EUR 2.3M additional annual revenue |
| **Cost Reduction** | Operational cost saved by AI automation | Compare cost-per-transaction before/after AI deployment | Automated document processing reduces per-loan processing cost by EUR 45 |
| **Customer Retention** | Impact on customer churn rate | Cohort analysis: AI-served vs. non-AI-served customers | Customers using AI financial advisor have 12% lower annual churn |
| **Regulatory Efficiency** | Reduction in compliance costs or time | Track hours/cost for regulatory processes (KYC, AML reporting) | AI-assisted regulatory reporting reduces preparation time by 40% |
| **Risk Reduction** | Decrease in financial losses from fraud, defaults, etc. | Compare loss rates before/after AI deployment | AI fraud detection reduces false negative losses by EUR 1.8M/year |

### ROI Calculation Template

```
AI Feature ROI = (Benefits - Costs) / Costs * 100

Benefits:
  + Revenue increase attributable to AI
  + Cost savings from automation
  + Risk reduction (avoided losses)
  + Regulatory efficiency gains

Costs:
  - Development and deployment costs
  - Infrastructure and compute costs
  - Ongoing monitoring and maintenance
  - Governance overhead (eval suites, audits, compliance)
  - Retraining and data costs
```

---

## 4. Adoption and Engagement Metrics

These track whether users actually use the AI feature.

| Metric | Definition | Target |
|--------|-----------|--------|
| **Feature Adoption Rate** | % of eligible users who use the AI feature at least once | >= 60% within 90 days of launch |
| **Active Usage Rate** | % of adopters who use the feature in any given month | >= 40% monthly active rate |
| **Feature Stickiness** | DAU/MAU ratio for the AI feature | >= 0.25 (users return multiple times per month) |
| **Override Rate** | % of AI recommendations that users manually override | Healthy range: 5-20% (too low may indicate blind trust; too high indicates distrust) |
| **Abandonment Rate** | % of users who start interacting with AI feature but abandon mid-task | <= 15% |

### Warning Signs

| Signal | Interpretation | Action |
|--------|---------------|--------|
| Adoption < 30% after 90 days | Users don't see value or don't know about the feature | Investigate UX, onboarding, and feature discoverability |
| Override rate > 40% | Users don't trust AI output | Review model quality, output presentation, and transparency |
| Override rate < 2% | Users may be blindly trusting AI | Add friction for high-stakes decisions; review HITL patterns |
| Abandonment > 25% | AI interaction is frustrating or confusing | UX research; check response times and error rates |

---

## 5. Fairness and Equity Metrics (Product Level)

While [bias-and-fairness-evals.md](../../02-development-governance/evaluations/bias-and-fairness-evals.md) covers technical fairness metrics, product-level fairness measures whether AI outcomes are equitable across user groups in practice.

| Metric | Definition | Measurement |
|--------|-----------|-------------|
| **Outcome Parity** | Similar task success rates across demographic groups | Compare task completion rates by group; flag if gap > 5 percentage points |
| **Service Quality Parity** | Similar response quality across groups | Compare AI helpfulness ratings, error rates, and time-to-completion by group |
| **Access Equity** | All user segments can access and use AI features equally | Track adoption and engagement rates by segment; identify underserved groups |
| **Escalation Disparity** | No group is disproportionately escalated from AI to human | Compare escalation rates by group; flag if ratio > 1.3x |

---

## 6. Connecting Product Metrics to Governance

### Metric-to-Governance Mapping

| Product Metric Category | Governance Gate | Framework Reference |
|------------------------|----------------|---------------------|
| Task Completion | Pre-deployment gate: minimum task success rate | [pre-deployment-gate.yaml](../../02-development-governance/checklists/pre-deployment-gate.yaml) |
| User Satisfaction | Continuous monitoring: alert if trust score drops | [continuous-online-evaluation.md](../../03-runtime-governance/evaluations/continuous-online-evaluation.md) |
| Business Impact | Quarterly review: ROI tracking | [governance-in-quarterly-planning.md](../../07-enterprise-implementation/process-integration/governance-in-quarterly-planning.md) |
| Adoption | Post-launch review: 30/60/90 day adoption check | [agent-fleet-operations.md](../../03-runtime-governance/agentic-workflows/agent-fleet-operations.md) |
| Fairness | Continuous: automated fairness disparity alerts | [bias-and-fairness-evals.md](../../02-development-governance/evaluations/bias-and-fairness-evals.md) |

### Integration with Eval Suites

Product success metrics should be encoded in the [evaluation strategy template](evaluation-strategy-template.yaml) alongside technical metrics. For each AI feature, define:

1. **Primary product metric** -- the single metric that best captures whether the feature delivers value (e.g., task success rate)
2. **Supporting product metrics** -- 2-3 additional metrics providing context (e.g., time-to-completion, user satisfaction)
3. **Business metric** -- the organizational KPI the feature contributes to (e.g., cost reduction, revenue)
4. **Fairness metric** -- at least one product-level fairness measure across protected groups

All four categories must have defined thresholds and automated measurement before the feature passes the [pre-deployment gate](../../02-development-governance/checklists/pre-deployment-gate.yaml).

---

## Related Documents

- [Defining Acceptance Criteria](defining-acceptance-criteria.md) -- how to write measurable acceptance criteria
- [AI Quality Metrics Catalog](ai-quality-metrics-catalog.md) -- technical model metrics (complements this document)
- [Evaluation Strategy Template](evaluation-strategy-template.yaml) -- template for combining product and technical metrics
- [Continuous Online Evaluation](../../03-runtime-governance/evaluations/continuous-online-evaluation.md) -- monitoring product metrics in production
- [Agent Performance Evals](../../03-runtime-governance/evaluations/agent-performance-evals.md) -- specialized metrics for business AI agents
- [Eval Reporting Dashboard](../../04-operational-governance/evaluations/eval-reporting-dashboard.md) -- visualizing product metrics
