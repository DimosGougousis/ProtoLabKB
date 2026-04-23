# Evaluation Reporting Dashboard Specification

## Purpose

This document specifies the requirements for an evaluation results dashboard that consolidates all AI evaluation data -- regression tests, drift detection, fairness assessments, safety checks, and performance metrics -- into a unified reporting interface. The eval dashboard serves as the operational evaluation nerve center for engineering and product teams (Tier 3 in the governance dashboard hierarchy), while feeding aggregate signals upward to the executive governance dashboard at Tier 1/2.

The eval dashboard is distinct from the executive governance dashboard: it is designed for practitioners who need to understand detailed evaluation results, investigate anomalies, and make model-level decisions. The executive dashboard consumes aggregate signals from this dashboard.

## When to Use

- When implementing the evaluation infrastructure for AI governance
- When designing monitoring and alerting for AI system quality
- When onboarding new AI systems that require evaluation visibility
- When preparing for regulatory audits that require evidence of ongoing evaluation
- When investigating evaluation failures or unexpected metric changes
- When building stakeholder-specific views of evaluation health

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **MLOps / Platform Engineer** | **Responsible** -- builds and maintains the dashboard infrastructure, data pipelines, and integrations |
| **Model Owner** | **Accountable** -- defines which metrics appear for each model, sets alert thresholds, reviews results |
| **Product Manager** | **Consumer** -- uses the dashboard to understand model quality trends and make product decisions |
| **Compliance Officer (2nd Line)** | **Consumer** -- uses the dashboard to verify ongoing regulatory compliance of AI systems |
| **CAIO** | **Informed** -- receives aggregate eval health from the executive dashboard, which sources from this dashboard |

## Regulatory Basis

- **SAFEST item T-17** -- Monitoring dashboards: real-time visibility into AI system performance, fairness metrics, drift indicators, and operational health
- **SAFEST item S-03** -- Model performance metrics with thresholds that trigger remediation
- **SAFEST item F-11** -- Production fairness monitoring: dashboards, alert thresholds, and response procedures
- **EU AI Act Article 72** -- Post-market monitoring system for high-risk AI
- **EU AI Act Article 9(2)(a)** -- Risk management system shall consist of a continuous iterative process with monitoring
- **DORA Article 13** -- ICT risk management reporting

---

## 1. Dashboard Architecture

### 1.1 Relationship to Executive Governance Dashboard

```
+========================================================+
|  EXECUTIVE GOVERNANCE DASHBOARD (Tier 1/2)              |
|  File: ../../06-executive/governance-dashboard-spec.md  |
|  Audience: Board, CAIO, Compliance                      |
|  Content: Aggregate signals, traffic lights, trends     |
+========================================================+
         ^
         | Aggregate signals (Green/Amber/Red per system)
         |
+========================================================+
|  EVAL REPORTING DASHBOARD (Tier 3) -- THIS DOCUMENT     |
|  Audience: ML Engineers, Model Owners, Product Managers |
|  Content: Detailed metrics, per-eval results, trends    |
+========================================================+
         ^
         | Raw evaluation data
         |
+========================================================+
|  MODEL MONITORING DASHBOARD (Tier 4)                    |
|  File: ../templates/model-monitoring-dashboard.md       |
|  Audience: MLOps, On-Call Engineers                      |
|  Content: Real-time ops metrics, latency, errors, cost  |
+========================================================+
```

### 1.2 Data Sources

| Source | Data Type | Refresh Cadence |
|--------|----------|----------------|
| Regression test pipeline | Pass/fail results, metric deltas, golden dataset coverage | On every pipeline run (event-driven) |
| Drift detection pipeline | PSI, KL divergence, MMD scores per feature | Daily (high-risk), weekly (limited-risk) |
| Fairness evaluation pipeline | Fairness metrics per protected group | Weekly (high-risk), monthly (limited-risk) |
| Safety evaluation pipeline | Guardrail bypass rates, adversarial test results | Weekly |
| Production performance monitoring | Accuracy, F1, AUC-ROC against delayed labels | As labels become available |
| Red-team results | Vulnerability findings, severity distribution | After each red-team campaign |
| A/B test results | Experiment metrics, statistical significance | Duration of each experiment |
| LLM observability platforms | Trace quality scores, reasoning coherence, tool-use patterns | Continuous |

---

## 2. Dashboard Views

### 2.1 Portfolio Summary View

**Purpose:** At-a-glance health of all AI systems under evaluation.

| Component | Description |
|-----------|-------------|
| **System health grid** | One row per AI system. Columns: system name, risk tier, last eval date, overall status (Green/Amber/Red), open issues count. Sortable by any column. |
| **Eval coverage heatmap** | Matrix showing which eval types have been run for each system in the current period. Cells colored by recency: green (within cadence), amber (approaching due), red (overdue). |
| **Trend sparklines** | Mini charts showing 90-day trend for key aggregate metrics: overall pass rate, average drift score, fairness compliance rate. |
| **Alert summary** | Count of open alerts by severity (Critical/High/Medium/Low). Clicking drills into the alert list. |

### 2.2 Per-Model View

**Purpose:** Deep dive into a single AI system's evaluation health.

| Component | Description |
|-----------|-------------|
| **Model identity header** | Model name, ID, version, risk tier, Model Owner, last deployment date, last eval date |
| **Acceptance criteria status** | Table of all acceptance criteria from the model card, each showing current value, threshold, status (Pass/Warn/Fail), and trend |
| **Regression history** | Timeline showing all regression test runs, colored by result. Click a run to see the full regression report |
| **Drift indicators** | Per-feature drift scores (PSI or selected metric) displayed as a bar chart, colored by severity. Time series showing drift evolution over 90 days |
| **Fairness panel** | Fairness metrics per protected group, displayed as a grouped bar chart. Disparate impact ratios highlighted if below 0.8 threshold |
| **Safety panel** | Guardrail bypass rate trend, adversarial test pass rate, last red-team results summary |
| **Agent behavior panel** | (For agentic systems) Tool call distribution, delegation patterns, permission boundary compliance rate |

### 2.3 Per-Eval View

**Purpose:** Detailed results of a specific evaluation run.

| Component | Description |
|-----------|-------------|
| **Eval metadata** | Eval type, run date, trigger (scheduled/event/manual), golden dataset version, environment |
| **Overall result** | PASS / WARN / FAIL with overall confidence |
| **Metric breakdown** | Table of every metric computed, with baseline value, current value, delta, tolerance, and pass/fail status |
| **Example-level results** | For WARN and FAIL cases, list of specific golden dataset examples that changed. Includes input, expected output, actual output, and diff. Sortable by delta magnitude |
| **Trace viewer** | (For LLM/agent systems) Embedded trace viewer showing reasoning spans for selected examples. Links to LangSmith, Arize Phoenix, or Langfuse trace |
| **Evidence artifacts** | Links to downloadable eval report, raw data, and screenshots for governance evidence storage |

### 2.4 Trend View

**Purpose:** Long-term evaluation health trends for strategic planning.

| Component | Description |
|-----------|-------------|
| **Metric time series** | Multi-line chart showing any selected metric over time (30d, 90d, 180d, 1y). Overlay deployment events, incidents, and retraining events as markers |
| **Regression pass rate trend** | Percentage of regression runs that pass, plotted over time. Declining trend indicates systemic quality issues |
| **Drift trend** | Aggregate drift score across the portfolio, plotted over time. Helps identify periods of systemic drift (e.g., market regime changes) |
| **Fairness trend** | Fairness compliance rate over time, broken down by protected group. Identifies emerging bias patterns |
| **Eval velocity** | Number of eval runs per week/month, by type. Ensures eval cadence is maintained |

---

## 3. Stakeholder-Specific Views

### 3.1 Engineering View

**Audience:** ML Engineers, Data Scientists, Platform Engineers

| Emphasis | Details |
|----------|---------|
| **Technical depth** | Full metric breakdowns, example-level results, trace access, raw data download |
| **Debugging tools** | Side-by-side output comparison, feature attribution for regressions, trace diff viewer |
| **Pipeline health** | Eval pipeline run history, execution times, failure reasons, queue depth |
| **Integration status** | CI/CD gate status, dependency version tracking, upstream data source health |

### 3.2 Product Manager View

**Audience:** Product Managers, Product Owners

| Emphasis | Details |
|----------|---------|
| **Business impact** | Metrics translated to business terms (e.g., "false positive rate" becomes "incorrectly blocked transactions per 1000") |
| **Customer experience** | Task completion rate, customer satisfaction proxy, escalation rate to human agents |
| **A/B test results** | Experiment outcomes with statistical significance, effect sizes, and recommendations |
| **Release readiness** | Traffic-light summary of whether the next version passes all eval gates |

### 3.3 Compliance View

**Audience:** Compliance Officers, Risk Managers, Internal Audit

| Emphasis | Details |
|----------|---------|
| **Regulatory mapping** | Each eval result linked to the regulatory requirement it satisfies (SAFEST item, EU AI Act article, DORA article) |
| **Evidence trail** | Timestamped, immutable eval reports with version-controlled golden datasets |
| **Compliance gaps** | Highlight any evaluation that is overdue per the required cadence |
| **Audit-ready reports** | One-click generation of compliance evidence packages per regulation |
| **Fairness focus** | Dedicated fairness compliance view with historical trends per protected group |

---

## 4. Alerting Integration

### 4.1 Alert Sources

| Source | Alert Condition | Severity |
|--------|----------------|----------|
| Regression pipeline | Any FAIL result | High |
| Regression pipeline | WARN result on high-risk system | Medium |
| Drift detection | Drift-1 or Drift-2 severity | High / Critical |
| Drift detection | Drift-3 sustained > 14 days | Medium (escalated) |
| Fairness monitoring | Disparate impact ratio < 0.8 for any protected group | High |
| Safety monitoring | Guardrail bypass rate > 5% | High |
| Eval cadence | Scheduled eval overdue by > 48 hours | Medium |
| Eval cadence | Scheduled eval overdue by > 7 days | High |

### 4.2 Alert Routing

| Severity | Notification Channel | Recipients |
|----------|---------------------|------------|
| **Critical** | PagerDuty + Slack + Email | On-Call Engineer, Model Owner, 2nd Line |
| **High** | Slack + Email | Model Owner, MLOps Lead |
| **Medium** | Slack + Dashboard notification | Model Owner |
| **Low** | Dashboard notification only | Visible to Model Owner on next login |

### 4.3 Alert Lifecycle

1. **Triggered:** Alert created and notifications sent
2. **Acknowledged:** Recipient confirms they are investigating (SLA: within response time per severity)
3. **Investigating:** Root cause analysis underway
4. **Resolved:** Issue fixed and verification eval passed
5. **Closed:** Resolution documented with governance evidence

---

## 5. Data Refresh and Retention

### 5.1 Refresh Cadence

| Data Type | Dashboard Refresh | Rationale |
|-----------|------------------|-----------|
| Regression results | Real-time (on pipeline completion) | Results are needed immediately to unblock deployments |
| Drift metrics | Hourly for continuous, daily for batch | Balance between timeliness and compute cost |
| Fairness metrics | Daily for high-risk, weekly for others | Fairness requires sufficient sample size for statistical significance |
| Safety metrics | Daily | Security-relevant metrics warrant near-real-time visibility |
| Trend data | Hourly aggregation, displayed at daily granularity | Sufficient for trend identification without noise |

### 5.2 Data Retention

| Data Type | Retention Period | Regulatory Basis |
|-----------|-----------------|-----------------|
| Eval reports | 10 years | EU AI Act technical documentation retention (Annex IV) |
| Raw eval results | 5 years | Alignment with Wwft audit trail retention |
| Metric time series | 3 years | Sufficient for trend analysis and regulatory inquiries |
| Alert history | 5 years | DORA incident management record-keeping |
| Golden datasets | Indefinite (all versions) | Required to reproduce any past evaluation |

---

## 6. Dashboard Technical Requirements

### 6.1 Non-Functional Requirements

| Requirement | Specification |
|-------------|--------------|
| **Load time** | Portfolio summary view renders in < 3 seconds |
| **Data latency** | Real-time data reflects within 5 minutes of source update |
| **Concurrent users** | Support at least 50 concurrent users |
| **Access control** | Role-based access control aligned with governance roles; compliance view requires 2nd Line role |
| **Export** | All views exportable as PDF for governance evidence; data exportable as CSV for analysis |
| **Audit logging** | All dashboard access logged for regulatory audit trail |
| **Availability** | 99.5% uptime during business hours (lower than production systems since it is an internal tool) |

### 6.2 Visualization Patterns

| Pattern | When to Use | Implementation Notes |
|---------|------------|---------------------|
| **Traffic light (RAG)** | Any metric with defined Green/Amber/Red thresholds | Primary visual pattern; used consistently across all views |
| **Sparklines** | Summary views showing 90-day trends in minimal space | No axis labels; conveys direction, not precision |
| **Grouped bar charts** | Comparing metrics across groups (protected groups, model versions) | Always include statistical significance indicators |
| **Time series** | Trend views showing metric evolution | Include deployment markers, incident markers, and threshold lines |
| **Heatmaps** | Coverage matrices (eval types vs. systems) | Color by recency or pass/fail rate |
| **Diff views** | Comparing two evaluation runs side by side | Highlight changed values with color coding |

---

## 7. FinTech-Specific Dashboard Panels

### 7.1 Regulatory Compliance Panel

A dedicated panel showing evaluation compliance status against regulatory requirements:

| Requirement | Last Eval | Status | Next Due | Evidence |
|-------------|----------|--------|----------|---------|
| SAFEST S-03: Performance metrics | [date] | [Pass/Fail] | [date] | [link] |
| SAFEST S-12: Drift detection | [date] | [Pass/Fail] | [date] | [link] |
| SAFEST F-03: Bias testing | [date] | [Pass/Fail] | [date] | [link] |
| EU AI Act Art. 72: Post-market monitoring | [date] | [Active/Gap] | [date] | [link] |
| DORA Art. 25: Resilience testing | [date] | [Pass/Fail] | [date] | [link] |

### 7.2 Financial Impact Panel

Connects evaluation results to business metrics:

| Metric | Current | 30d Trend | Business Impact |
|--------|---------|-----------|----------------|
| Fraud detection false positive rate | [value] | [trend] | [blocked legitimate transactions per day] |
| AML alert precision | [value] | [trend] | [unnecessary investigations per month] |
| Credit scoring accuracy | [value] | [trend] | [estimated revenue impact] |
| Customer chatbot resolution rate | [value] | [trend] | [human escalation cost per month] |

---

## Cross-References

- **Governance Dashboard Spec:** [../../06-executive/governance-dashboard-spec.md](../../06-executive/governance-dashboard-spec.md) -- executive dashboard that consumes aggregate signals from this dashboard
- **Model Monitoring Dashboard:** [../templates/model-monitoring-dashboard.md](../templates/model-monitoring-dashboard.md) -- operational monitoring dashboard (Tier 4) feeding into this dashboard
- **Drift Detection Evals:** [drift-detection-evals.md](drift-detection-evals.md) -- drift metrics displayed in this dashboard
- **Regression Testing for AI:** [regression-testing-for-ai.md](regression-testing-for-ai.md) -- regression results displayed in this dashboard
- **Bias and Fairness Evals:** [../../02-development-governance/evaluations/bias-and-fairness-evals.md](../../02-development-governance/evaluations/bias-and-fairness-evals.md) -- fairness metrics displayed in this dashboard
- **Continuous Online Evaluation:** [../../03-runtime-governance/evaluations/continuous-online-evaluation.md](../../03-runtime-governance/evaluations/continuous-online-evaluation.md) -- production metrics feeding into this dashboard
- **Quarterly Governance Report:** [../../06-executive/quarterly-governance-report.md](../../06-executive/quarterly-governance-report.md) -- quarterly report draws from this dashboard
- **Tool Landscape:** [../../05-cross-cutting/tool-landscape.md](../../05-cross-cutting/tool-landscape.md) -- dashboard implementation tool options
- **RACI Matrix:** [../../05-cross-cutting/governance-roles-raci.md](../../05-cross-cutting/governance-roles-raci.md) -- role-based access control mapping

---

*Last updated: 2026-03-01*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
