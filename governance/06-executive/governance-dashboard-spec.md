# AI Governance Dashboard Specification

> **Purpose:** Define the requirements for an executive governance dashboard that provides a single pane of glass for AI governance health across the four governance pillars, enabling tiered stakeholders to monitor compliance, risk, and operational performance.
>
> **When to Use:** During the tooling integration phase (Months 7-9 of the [Adoption Playbook](../07-enterprise-implementation/risk-based-adoption/adoption-playbook.md)) or whenever the organization needs a centralized view of AI governance status.
>
> **Who Is Responsible:**
> - **Dashboard Owner:** CAIO (Chief AI Officer) or designated AI Governance PM
> - **Data Providers:** 1st Line product teams, MLOps, Compliance, Internal Audit
> - **Consumers:** Board, CAIO, AI Ethics Board, Product Teams, Regulators (on request)
>
> **Regulatory Basis:** SAFEST items T-15 (AI performance dashboards), T-17 (production monitoring dashboards), A-01 (board-level AI accountability); DNB Good Practice for AI; DORA Article 13 (ICT risk management reporting); EU AI Act Article 72 (post-market monitoring for high-risk AI).

---

## 1. Dashboard Philosophy

The governance dashboard is not a vanity metrics display. It is the operational backbone of the tiered governance architecture:

```
+=====================================================================+
|  TIER 1 -- STRATEGIC (Board / CAIO)                                 |
|  Dashboard View: Portfolio risk posture, regulatory compliance,      |
|  material incidents, governance maturity trajectory                   |
+=====================================================================+
         |
+=====================================================================+
|  TIER 2 -- POLICY (AI Ethics Board / Compliance)                    |
|  Dashboard View: Ethics review pipeline, bias audit results,         |
|  SAFEST completion rates, regulatory deadline tracking                |
+=====================================================================+
         |
+=====================================================================+
|  TIER 3 -- LIFECYCLE (Product Teams)                                |
|  Dashboard View: Model-level evals, deployment gate status,          |
|  guardrail performance, drift alerts                                 |
+=====================================================================+
         |
+=====================================================================+
|  TIER 4 -- RUNTIME (Automated Guardrails)                           |
|  Dashboard View: Real-time guardrail triggers, boundary violations,  |
|  escalation events, latency and availability                         |
+=====================================================================+
```

**Design Principles:**
1. **Drill-down, not dump.** Each tier sees only what it needs. Detail is available on demand, not by default.
2. **Traffic lights first, data second.** Every metric has a Green/Amber/Red status. Users see the signal before the number.
3. **Evidence-linked.** Every metric links to its source artifact (eval report, incident ticket, audit finding).
4. **Time-aware.** All metrics show trend over time, not just current state.

---

## 2. Tiered Dashboard Views

### 2.1 Board View (Tier 1 -- Strategic)

**Audience:** Board members, CEO, CAIO
**Refresh cadence:** Monthly (with real-time escalation for Red metrics)
**Maximum metrics on screen:** 12 (cognitive load limit for strategic decision-makers)

| Metric | Source | Green | Amber | Red |
|--------|--------|-------|-------|-----|
| AI Portfolio Risk Score | Aggregated from all model risk tiers | No high-risk models with open critical findings | 1-2 high-risk models with open findings | 3+ high-risk models with open critical findings |
| Governance Maturity Level | Self-assessment (see [Maturity Roadmap](../07-enterprise-implementation/risk-based-adoption/governance-maturity-roadmap.md)) | On track or ahead of 12-month target | 1 phase behind target | 2+ phases behind target |
| Material AI Incidents (quarter) | Incident management system | 0 material incidents | 1-2 material incidents, all resolved | 3+ material incidents or unresolved |
| SAFEST Compliance Score | SAFEST YAML checklists | >=85% items completed | 60-84% items completed | <60% items completed |
| Regulatory Deadline Adherence | Compliance calendar | All deadlines on track | 1 deadline at risk | Any deadline missed |
| AI Ethics Review Backlog | Ethics Board tracker | <=2 pending reviews | 3-5 pending reviews | 6+ pending reviews or any >30 days old |
| Autonomous Decision Error Rate | Runtime observability | <0.1% error rate | 0.1-0.5% error rate | >0.5% error rate |
| Human Oversight Model Distribution | Model registry | Aligned with risk policy | Minor deviations | High-risk models without required HITL |
| **AI Cost Trend (MTD)** | **Cost attribution dashboard** | **Within budget** | **5-10% over budget** | **>10% over budget** |
| **Budget Variance** | **Financial governance** | **<5% variance** | **5-15% variance** | **>15% variance** |
| **AI ROI** | **Value attribution** | **>200% ROI** | **100-200% ROI** | **<100% ROI** |
| **Cost Anomaly Alerts** | **Cost monitoring** | **0 active** | **1-2 minor** | **3+ or major** |

**Financial Governance Metrics (New):**

| Metric | Description | Board Relevance |
|--------|-------------|-----------------|
| **AI Cost Trend** | Month-to-date AI spend vs budget | Visibility into material expenditure |
| **Budget Variance** | Deviation from forecast | Early warning of cost overruns |
| **AI ROI** | Return on AI investment | Justification for continued investment |
| **Cost Anomaly Alerts** | Unusual spending patterns | Detection of Shadow AI or inefficiency |

**Tier 4 Cost Anomaly Alerting:**
- Real-time alerts for cost spikes >200% of baseline
- Automatic kill switch triggers for runaway costs
- Daily cost anomaly reports to operations team

**Board View Wireframe Description:**

The board view occupies a single screen with no scrolling required.

- **Top banner:** Organization name, reporting period, overall governance health (single traffic light).
- **Left column (40%):** AI Portfolio Summary -- a treemap visualization where each rectangle represents an AI system, sized by business impact, colored by risk tier (red = high, amber = limited, green = minimal). Clicking a rectangle drills into the model detail view.
- **Right column (60%):** Eight metric cards arranged in a 2x4 grid. Each card shows: metric name, current value, trend arrow (up/down/flat), traffic light indicator. Clicking a card drills into the pillar-level view.
- **Bottom bar:** Next board reporting date, number of open action items from previous board meeting.

### 2.2 CAIO View (Tier 2 -- Portfolio Risk)

**Audience:** CAIO, AI Ethics Board, Head of Compliance
**Refresh cadence:** Weekly
**Maximum metrics on screen:** 24

| Metric Category | Specific Metrics | Source |
|-----------------|-----------------|--------|
| **Portfolio Overview** | Total models in production, models by risk tier, new deployments this period, pending retirements | Model registry |
| **Discovery Pipeline** | Models in discovery phase, pending risk classifications, ethics reviews in queue, ethics reviews overdue | Jira governance workflows (see [Jira integration](../07-enterprise-implementation/tooling-integration/jira-governance-workflows.md)) |
| **Development Quality** | Eval suite pass rates (by model), bias test results (pass/fail/conditional), deployment gate status (open/blocked) | CI/CD pipeline (see [CI/CD governance](../07-enterprise-implementation/process-integration/governance-in-cicd.md)) |
| **Runtime Health** | Guardrail trigger rate (per model), agent boundary violations, human escalation rate, false positive/negative rates | Runtime observability platform |
| **Operational Status** | Open incidents by severity, mean time to resolution, drift alerts (active/acknowledged), next revalidation dates | Incident management, monitoring |
| **Compliance** | SAFEST completion by pillar, EU AI Act obligations met/outstanding, DORA compliance items, audit findings open/closed | GRC platform, YAML checklists |

**CAIO View Wireframe Description:**

- **Top row:** Four pillar health cards (Discovery, Development, Runtime, Operational) each showing a composite traffic light and top-3 metrics.
- **Middle section:** Tabbed view -- one tab per pillar. Default tab is whichever pillar has the worst health score.
- **Right sidebar:** Regulatory deadline timeline (vertical timeline showing next 90 days of deadlines).
- **Bottom section:** Action items assigned to CAIO, sorted by priority.

### 2.3 Team View (Tier 3 -- Operational)

**Audience:** Product teams, ML engineers, DevOps/MLOps
**Refresh cadence:** Real-time (with 5-minute aggregation)
**Scope:** Filtered to the team's own models only

| Metric | Source | Green | Amber | Red |
|--------|--------|-------|-------|-----|
| Model eval pass rate | CI/CD eval pipeline | >=95% pass rate | 80-94% pass rate | <80% pass rate |
| Bias test results | Fairness testing suite | All protected groups within tolerance | 1 group marginal | Any group outside tolerance |
| Deployment gate status | CI/CD governance gates | All gates passed | Non-blocking gates failed | Blocking gate failed |
| Guardrail trigger rate | Runtime guardrail logs | <1% of requests trigger guardrails | 1-5% trigger rate | >5% trigger rate |
| Agent boundary violations | Permission boundary monitor | 0 violations in 7 days | 1-3 violations in 7 days | 4+ violations or any critical |
| Escalation rate to human | Escalation tracking | Within expected range for model type | 10-20% above expected | >20% above expected |
| Data drift score | Drift detection pipeline | No significant drift detected | Drift detected, within tolerance | Drift exceeds tolerance threshold |
| Latency P99 | APM tooling | <SLA threshold | 80-100% of SLA threshold | >SLA threshold |
| Incident backlog | Incident management | 0 open incidents for this model | 1-2 open, within SLA | 3+ open or any SLA breach |

**Team View Wireframe Description:**

- **Header:** Team name, number of models owned, composite team health score.
- **Model selector:** Dropdown or card grid showing all models owned by this team, each with a mini traffic light.
- **Selected model detail:** Full-width panel showing all 9 metrics above in a 3x3 grid.
- **Trend charts:** Below the metrics grid, time-series charts (7-day, 30-day, 90-day) for key metrics.
- **Action panel:** Links to create incident, trigger revalidation, view model card, open eval results.

---

## 3. Per-Pillar Metric Definitions

### 3.1 Discovery Pillar Metrics

| Metric ID | Metric | Calculation | Data Source | SAFEST Ref |
|-----------|--------|-------------|-------------|-----------|
| DISC-01 | Models in pipeline | Count of AI systems in Discovery phase | Model registry / Jira | S-01 |
| DISC-02 | Pending risk classifications | Count of models without assigned risk tier | Model registry | S-01 |
| DISC-03 | Ethics reviews pending | Count of open AI Governance Review issues | Jira / Ethics Board tracker | A-03 |
| DISC-04 | Ethics review cycle time | Median days from submission to decision | Jira | A-03 |
| DISC-05 | Risk tier distribution | Percentage breakdown: High / Limited / Minimal | Model registry | S-01 |
| DISC-06 | Rejected use cases (quarter) | Count of AI proposals rejected by Ethics Board | Ethics Board minutes | E-03 |

### 3.2 Development Pillar Metrics

| Metric ID | Metric | Calculation | Data Source | SAFEST Ref |
|-----------|--------|-------------|-------------|-----------|
| DEV-01 | Eval suite pass rate | Passed evals / Total evals (per model, per sprint) | CI/CD pipeline | S-03 |
| DEV-02 | Bias test results | Pass / Conditional Pass / Fail per protected group | Fairness testing suite (Giskard, Aequitas) | F-03 |
| DEV-03 | Deployment gate status | Open / Blocked / Passed for each model pending deployment | CI/CD governance gates | A-03 |
| DEV-04 | Model card completeness | Percentage of required model card fields populated | Model card registry | T-12 |
| DEV-05 | Red team findings (open) | Count of unresolved adversarial test findings | Security testing tracker | S-05 |
| DEV-06 | Code review governance coverage | Percentage of AI PRs with governance review completed | Git platform | A-04 |

### 3.3 Runtime Pillar Metrics

| Metric ID | Metric | Calculation | Data Source | SAFEST Ref |
|-----------|--------|-------------|-------------|-----------|
| RUN-01 | Guardrail trigger rate | Guardrail-triggered requests / Total requests | Guardrail runtime logs | S-13 |
| RUN-02 | Agent boundary violations | Count of tool-use or scope violations by agents | Permission boundary monitor | A-11 |
| RUN-03 | Human escalation rate | Escalations to human / Total agent decisions | Escalation tracking system | S-13 |
| RUN-04 | Oversight model distribution | Count of models per oversight mode: HITL / HOTL / HOTA | Model registry | A-01 |
| RUN-05 | Mean time to human takeover | Average seconds from escalation trigger to human response | Escalation logs | S-13 |
| RUN-06 | Prompt injection attempts | Count of detected prompt injection / jailbreak attempts | Input guardrail logs | S-08 |
| RUN-07 | Output safety violations | Count of outputs caught by safety filters | Output guardrail logs | S-13 |

### 3.4 Operational Pillar Metrics

| Metric ID | Metric | Calculation | Data Source | SAFEST Ref |
|-----------|--------|-------------|-------------|-----------|
| OPS-01 | Incident count by severity | Count of AI incidents: Critical / High / Medium / Low | Incident management system | A-15 |
| OPS-02 | Mean time to resolution | Average hours from incident detection to resolution | Incident management system | A-15 |
| OPS-03 | Drift alerts (active) | Count of unresolved data or model drift alerts | Drift detection pipeline | S-12 |
| OPS-04 | Compliance status | SAFEST checklist completion percentage per pillar | YAML checklist aggregator | All |
| OPS-05 | Audit findings (open) | Count of open audit findings by severity | GRC platform / audit tracker | A-02 |
| OPS-06 | Revalidation overdue | Count of models past their revalidation due date | Model registry | S-03 |
| OPS-07 | Cost governance | AI infrastructure cost vs budget (percentage) | Cloud cost management | A-09 |

---

## 4. SAFEST Compliance Dashboard Section

A dedicated dashboard tab shows SAFEST framework completion status. This is the primary view for regulatory preparation and DNB engagement.

### 4.1 Pillar Completion View

| SAFEST Pillar | Total Items | Completed | In Progress | Not Started | N/A | Completion % |
|---------------|-------------|-----------|-------------|-------------|-----|-------------|
| **S** -- Security & Soundness | [N] | [N] | [N] | [N] | [N] | [%] |
| **A** -- Accountability | [N] | [N] | [N] | [N] | [N] | [%] |
| **F** -- Fairness | [N] | [N] | [N] | [N] | [N] | [%] |
| **E** -- Ethics | [N] | [N] | [N] | [N] | [N] | [%] |
| **S** -- Sustainability | [N] | [N] | [N] | [N] | [N] | [%] |
| **T** -- Transparency | [N] | [N] | [N] | [N] | [N] | [%] |
| **Overall** | [N] | [N] | [N] | [N] | [N] | [%] |

### 4.2 SAFEST Traffic Light Thresholds

| Status | Threshold | Dashboard Color | Action Required |
|--------|-----------|-----------------|-----------------|
| On Track | >=80% complete, no critical items outstanding | Green | Continue execution |
| At Risk | 50-79% complete, or any critical item not started | Amber | Escalate to CAIO; create remediation plan within 2 weeks |
| Off Track | <50% complete, or critical items overdue | Red | Board escalation; emergency remediation program |

### 4.3 Data Source

SAFEST metrics are computed by parsing the YAML checklist files maintained in this framework (see `01-discovery-governance/`, `02-development-governance/`, etc.). A scheduled job reads all `*.yaml` files, aggregates item statuses, and publishes to the dashboard.

---

## 5. Drill-Down Architecture

The dashboard supports four levels of drill-down:

```
Level 0: Organization Health     (Board View -- single screen)
    |
    v
Level 1: Pillar Health          (Click a pillar card to see all metrics for that pillar)
    |
    v
Level 2: Model Health           (Click a model to see all metrics for that specific model)
    |
    v
Level 3: Issue Detail           (Click a metric to see the underlying issue, eval result,
                                  incident ticket, or audit finding)
```

**Example drill-down path:**

1. Board sees "Runtime Health" card is Amber.
2. Clicks card --> sees Runtime pillar view: guardrail trigger rate is elevated for "Fraud Detection Agent v2.3."
3. Clicks model --> sees model detail: trigger rate spiked 3 days ago, correlated with a new transaction pattern.
4. Clicks metric --> opens the specific guardrail log entries, linked to the Jira investigation ticket.

Every drill-down level must include:
- **Breadcrumb navigation** back to higher levels
- **Time range selector** (24h, 7d, 30d, 90d, custom)
- **Export button** (PDF for board reporting, CSV for analysis)

---

## 6. Data Sources and Integration

### 6.1 Data Source Map

| Data Source | Metrics Supplied | Integration Method | Refresh Frequency |
|-------------|-----------------|-------------------|-------------------|
| **Model Registry** (internal) | Portfolio inventory, risk tiers, owners, oversight modes | REST API | Real-time |
| **CI/CD Pipeline** (GitHub Actions / GitLab CI) | Eval pass rates, deployment gate status, governance check results | Webhook on pipeline completion | Per pipeline run |
| **Runtime Observability** (Datadog / Grafana / custom) | Guardrail triggers, latency, error rates, escalation events | Metrics API (Prometheus/OpenMetrics) | Real-time (5-min aggregation) |
| **Guardrail Platform** (NeMo Guardrails / Guardrails AI / custom) | Input/output safety violations, boundary violations | Event stream (Kafka / webhook) | Real-time |
| **Incident Management** (Jira / PagerDuty / ServiceNow) | Incident count, severity, MTTR, open/closed status | REST API | Hourly |
| **Jira Governance Workflows** | Ethics reviews, governance tasks, revalidation status | REST API / JQL queries | Hourly |
| **YAML Checklist Files** (this repository) | SAFEST completion percentages | Git-based parser (scheduled) | Daily |
| **GRC Platform** (ServiceNow GRC / Archer / OneTrust) | Audit findings, compliance status, regulatory deadlines | REST API | Daily |
| **Drift Detection** (Evidently AI / Fiddler / custom) | Data drift scores, feature drift, prediction drift | Metrics API | Per evaluation run |
| **Cost Management** (AWS Cost Explorer / GCP Billing / custom) | AI infrastructure spend vs budget | REST API | Daily |

### 6.2 GRC Platform Integration

For organizations using enterprise GRC platforms:

**ServiceNow GRC Integration:**
- Map SAFEST checklist items to ServiceNow Policy and Compliance modules
- AI incidents flow into ServiceNow Incident Management
- Dashboard pulls compliance status via ServiceNow REST API
- Audit findings from ServiceNow Audit Management appear in dashboard

**Archer Integration:**
- Map AI risk register entries to Archer risk objects
- Dashboard consumes Archer risk scores via API
- Regulatory deadline tracking synced with Archer compliance calendar

**OneTrust Integration:**
- AI privacy impact assessments tracked in OneTrust
- Data governance metrics (data lineage, consent status) pulled into dashboard

---

## 7. Alerting and Notification

### 7.1 Alert Thresholds

| Alert Level | Trigger | Notification Channel | Recipients |
|-------------|---------|---------------------|------------|
| **Critical** | Any metric turns Red | Immediate: Slack/Teams + Email + PagerDuty | CAIO, Model Owner, On-Call |
| **Warning** | Any metric turns Amber | Within 1 hour: Slack/Teams + Email | Model Owner, Team Lead |
| **Informational** | Metric trend worsening (3 consecutive periods) | Daily digest email | Model Owner |
| **Regulatory** | Regulatory deadline <30 days away | Weekly reminder escalating to daily at <7 days | CAIO, Head of Compliance |

### 7.2 Escalation Rules

1. **Red metric unresolved >24 hours:** Auto-escalate to CAIO with summary.
2. **Red metric unresolved >72 hours:** Auto-escalate to Board-level AI accountable member (see [Board-Level AI Accountability](../07-enterprise-implementation/organizational-model/board-level-ai-accountability.md)).
3. **Multiple Red metrics on same model:** Auto-create incident ticket, trigger [incident response playbook](../04-operational-governance/).
4. **SAFEST completion drops below threshold before regulatory deadline:** Emergency notification to CAIO and Head of Compliance.

---

## 8. Refresh Cadence Summary

| Dashboard View | Data Refresh | Report Generation | Distribution |
|----------------|-------------|-------------------|-------------|
| Board View | Monthly snapshot | Quarterly (aligned with [Quarterly Governance Report](quarterly-governance-report.md)) | Board pack |
| CAIO View | Weekly refresh | Monthly summary to AI Ethics Board | Email + dashboard |
| Team View | Real-time (5-min aggregation) | Sprint-level (every 2 weeks) | Dashboard + Slack |
| SAFEST Compliance | Daily | Monthly progress report | Email + GRC platform |
| Alert Dashboard | Real-time | On-event | Slack/Teams + PagerDuty |

---

## 9. Implementation Requirements

### 9.1 Technical Architecture

```
+------------------+    +------------------+    +------------------+
|  Data Sources    |    |  Data Pipeline   |    |  Dashboard UI    |
|                  |    |                  |    |                  |
| Model Registry   |--->| ETL / Streaming  |--->| Grafana /        |
| CI/CD Pipelines  |    | (Kafka / Airflow)|    | Superset /       |
| Observability    |    |                  |    | Custom React     |
| Guardrail Logs   |    | Data Warehouse   |    |                  |
| Jira / ServiceNow|    | (Postgres /      |    | Tiered views     |
| YAML Checklists  |    |  Snowflake /     |    | RBAC per tier    |
| GRC Platform     |    |  BigQuery)       |    | Drill-down       |
| Cost Management  |    |                  |    | Export (PDF/CSV) |
+------------------+    +------------------+    +------------------+
```

### 9.2 Access Control (RBAC)

| Role | Dashboard Access Level | Can Export | Can Configure |
|------|-----------------------|-----------|---------------|
| Board Member | Board View only | PDF only | No |
| CAIO | All views | PDF + CSV | Yes |
| AI Ethics Board | CAIO View + SAFEST View | PDF + CSV | No |
| Compliance | CAIO View + SAFEST View + Audit View | PDF + CSV | No |
| Product Team Lead | Team View (own models) | CSV | No |
| ML Engineer | Team View (own models) | CSV | No |
| Internal Audit | All views (read-only) | PDF + CSV | No |
| Regulator (DNB) | Board View + SAFEST View (on request, read-only) | PDF | No |

### 9.3 Non-Functional Requirements

| Requirement | Target |
|-------------|--------|
| Dashboard page load time | <3 seconds |
| Real-time data latency | <5 minutes |
| Availability | 99.9% (DORA-aligned) |
| Data retention | 3 years (regulatory retention period) |
| Audit trail | All dashboard access logged (who viewed what, when) |
| Export format | PDF (board-quality), CSV (analysis), JSON (API) |

---

## 10. Agent Fleet Operations (Tier 3/4 Detail)

For per-agent operational dashboards used by product teams and MLOps engineers, this specification delegates to the **Agent Fleet Operations** document, which provides:

- **Agent Registry** -- Fleet-wide inventory with health states, risk tiers, oversight models, and NHI identities
- **Per-Agent KPI/SLA Governance** -- KPI definitions with warning/critical thresholds and RACI ownership per metric
- **Risk Mitigation Plan Tracking** -- Step-by-step remediation with done/active/pending status indicators
- **Agent Cost Governance** -- Five cost dimensions (monthly total, per-interaction, LLM tokens, tool calls, infrastructure)
- **MLOps Lifecycle** -- Drift detection, retraining governance, model version promotion, rollback policies, A/B test governance
- **Governance Compliance Tab** -- Per-agent SAFEST compliance, EU AI Act readiness, permission boundary status, bias metrics, incident history
- **Fleet Dashboard Data Contract** -- Authoritative mapping of every dashboard panel to its source governance artifact

**Reference:** [`03-runtime-governance/agentic-workflows/agent-fleet-operations.md`](../03-runtime-governance/agentic-workflows/agent-fleet-operations.md)

This document and the Agent Fleet Operations document together form the **two-system architecture**: this specification governs the executive governance dashboard (Tier 1-2 views), while Agent Fleet Operations governs the operational agent fleet dashboard (Tier 3-4 views).

---

## 11. Cross-References

| Related Artifact | Location | Relationship |
|-----------------|----------|-------------|
| Quarterly Governance Report | [06-executive/quarterly-governance-report.md](quarterly-governance-report.md) | Dashboard feeds the quarterly report |
| Board-Level AI Accountability | [07-enterprise/board-level-ai-accountability.md](../07-enterprise-implementation/organizational-model/board-level-ai-accountability.md) | Board view supports board oversight obligations |
| Governance in CI/CD | [07-enterprise/governance-in-cicd.md](../07-enterprise-implementation/process-integration/governance-in-cicd.md) | CI/CD pipelines are a primary data source |
| Jira Governance Workflows | [07-enterprise/jira-governance-workflows.md](../07-enterprise-implementation/tooling-integration/jira-governance-workflows.md) | Jira is a primary data source for governance task metrics |
| Governance Maturity Roadmap | [07-enterprise/governance-maturity-roadmap.md](../07-enterprise-implementation/risk-based-adoption/governance-maturity-roadmap.md) | Dashboard tracks maturity level progression |
| Risk Tiering Model | [07-enterprise/risk-tiering-model.md](../07-enterprise-implementation/risk-based-adoption/risk-tiering-model.md) | Risk tiers drive governance intensity displayed |
| SAFEST Checklists | Various YAML files across `01-` through `04-` directories | Source data for SAFEST compliance section |
| Three Lines of Defense | [07-enterprise/three-lines-of-defense-for-ai.md](../07-enterprise-implementation/organizational-model/three-lines-of-defense-for-ai.md) | RBAC maps to 3LoD responsibilities |

---

*Last updated: 2026-02-28*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
