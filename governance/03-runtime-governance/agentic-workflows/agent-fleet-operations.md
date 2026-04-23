# Agent Fleet Operations

## Purpose

This document is the **master bridge** between the Agent Fleet Command Dashboard (operational visibility) and the Agentic Governance Framework (policy, process, and MLOps backbone). It defines how every concept visible in the dashboard -- agent health, KPIs, SLAs, risk mitigations, MLOps lifecycle, governance compliance, and cost -- maps to a specific governance artifact, policy, or process in this framework.

Without this bridge document, the dashboard becomes a monitoring tool with no governance teeth, and the governance framework becomes a policy library with no operational visibility. Together, they form a closed loop: the framework defines what good looks like; the dashboard shows whether the fleet is achieving it.

## When to Use

- When registering a new agent in the fleet and configuring its dashboard presence
- When defining KPIs, SLAs, and RACI ownership for an agent
- When creating or tracking risk mitigation plans for agent-specific risks
- When establishing cost governance policies for agent operations
- When mapping dashboard panels to their source governance artifacts
- When onboarding new team members to the fleet operations model
- When auditing fleet-wide governance compliance

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **Fleet Operations Lead** | **Accountable** -- owns fleet-wide operational health, dashboard accuracy, and escalation procedures |
| **Model Owner (per agent)** | **Responsible** -- owns individual agent health, KPI compliance, and mitigation plan execution |
| **MLOps / Platform Engineer** | **Responsible** -- implements health checks, monitoring pipelines, cost tracking, and MLOps lifecycle automation |
| **Product Manager** | **Consulted** -- defines business KPIs, SLA targets, and customer impact thresholds |
| **Compliance Officer (2nd Line)** | **Reviewer** -- validates that fleet governance meets regulatory requirements; reviews governance tab data |
| **AI Governance Committee** | **Approver** -- approves fleet-wide policies; reviews fleet health quarterly |

## Regulatory Basis

- **EU AI Act Article 72** -- Post-market monitoring system for high-risk AI systems
- **EU AI Act Article 9** -- Risk management system maintained throughout the AI system lifecycle
- **EU AI Act Article 14** -- Human oversight measures for high-risk AI systems
- **EU AI Act Article 12** -- Record-keeping obligations for high-risk AI systems
- **DORA Article 9** -- ICT risk management framework, including third-party and operational risk
- **SAFEST items T-15** (AI performance dashboards), **T-17** (production monitoring), **S-12** (drift detection), **S-20** (periodic revalidation), **A-01** (board-level accountability)
- **DNB Good Practice** -- Continuous monitoring, model inventory, and operational risk management

---

## 1. Agent Registry Specification

Every agent operating in production must be registered in the fleet registry before it can be monitored, governed, or appear on the dashboard. The registry is the single source of truth for what agents exist, what they do, and who is responsible.

### 1.1 Registry Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `agent_id` | string | Globally unique identifier for this agent instance | `agent:payments-agent-prod-01` |
| `agent_name` | string | Human-readable name | "Payments Agent" |
| `agent_type` | enum | Classification per [Multi-Agent Governance Framework](multi-agent-governance-framework.md) Sec. 1 | `autonomous_actor` |
| `version` | semver | Current deployed version | `2.3.1` |
| `model_id` | string | Identifier of the underlying LLM or ML model | `gpt-4o-2026-02` |
| `model_version` | string | Specific model version or checkpoint | `gpt-4o-2026-02-15` |
| `deployment_environment` | enum | `dev`, `staging`, `prod` | `prod` |
| `health_state` | enum | Current operational health (see Sec. 2) | `healthy` |
| `risk_tier` | enum | Per [Risk Tiering Model](../../07-enterprise-implementation/risk-based-adoption/risk-tiering-model.md) | `high` |
| `oversight_model` | enum | HITL, HOTL, or HOTA (see [Human-in-the-Loop Patterns](human-in-the-loop-patterns.md)) | `HOTL` |
| `nhi_identity` | string | Machine Identity / NHI identifier in IAM (see [Agent Permission Boundaries](agent-permission-boundaries.md)) | `nhi:payments-agent-prod-01` |
| `permission_boundary_ref` | string | Reference to the agent's permission boundary definition | `PB-PAYMENTS-v2.3` |
| `health_check_endpoint` | URL | Endpoint for automated health checks | `https://agents.internal/payments/health` |
| `health_check_interval_seconds` | integer | Frequency of health checks | `30` |
| `functions` | list[string] | Actions this agent is authorized to perform | `["initiate_payment", "verify_account", "check_balance"]` |
| `out_of_scope` | list[string] | Actions explicitly denied to this agent | `["close_account", "modify_credit_limit", "access_other_customer_data"]` |
| `kpis` | list[KPI] | KPIs with SLA targets and RACI ownership (see Sec. 3) | See Section 3 |
| `owner` | string | Individual accountable for this agent | "Maria Chen, Model Owner" |
| `team` | string | Team responsible for operations | "Payments AI Team" |
| `compliance_frameworks` | list[string] | Applicable regulations | `["EU AI Act", "PSD2", "GDPR", "DORA"]` |
| `created_date` | datetime | When the agent was first registered | `2026-01-15T09:00:00Z` |
| `last_deployment_date` | datetime | When the current version was deployed | `2026-02-20T14:30:00Z` |

### 1.2 Registry Governance

- **Registration is mandatory.** No agent may operate in production without a registry entry. Unregistered agents are treated as unauthorized software and must be shut down.
- **Registry reviews:** Every registry entry is reviewed quarterly by the Model Owner and annually by 2nd Line Compliance.
- **Version tracking:** Every deployment updates the `version`, `model_version`, and `last_deployment_date` fields. The registry maintains a full version history.
- **Decommissioning:** When an agent is retired, its registry entry is marked as `decommissioned` (not deleted) and audit logs are retained per the retention policy in [Multi-Agent Governance Framework](multi-agent-governance-framework.md) Sec. 5.2.
- **Template:** See [Agent Registry Entry Template](../templates/agent-registry-entry.yaml) for the YAML template.

---

## 2. Agent Health Model

The Agent Fleet Command Dashboard displays three health states per agent: **Healthy**, **Degraded**, and **Critical**. The governance framework defines five degradation levels (see [Multi-Agent Governance Framework](multi-agent-governance-framework.md) Sec. 8.1). This section maps between the two.

### 2.1 Dashboard-to-Framework Health Mapping

| Dashboard State | Color | Framework Degradation Levels | Description |
|----------------|-------|----------------------------|-------------|
| **Healthy** | Green | Normal | All systems operational. Agent performing within all SLA thresholds. No active alerts. |
| **Degraded** | Amber | Reduced, Assisted | One or more KPIs breaching warning thresholds. Partial capability loss. Agent may be operating with reduced autonomy or with human assistance. |
| **Critical** | Red | Manual, Emergency | Agent failing to meet SLAs. Safety or compliance metrics breached. Agent may be in manual fallback or circuit-breaker state. Immediate intervention required. |

### 2.2 Health State Determination Logic

```
Health State = f(KPI compliance, system availability, safety metrics, drift status)

IF any safety metric breached (boundary violation, compliance violation):
    state = CRITICAL
ELIF any hard-gate KPI breached AND breach duration > 15 minutes:
    state = CRITICAL
ELIF any KPI in warning zone OR drift detected OR availability < 99.5%:
    state = DEGRADED
ELSE:
    state = HEALTHY
```

### 2.3 Health State Transitions

| From | To | Trigger | Required Action |
|------|----|---------|----------------|
| Healthy | Degraded | KPI warning threshold breached for > 5 minutes | Alert Model Owner; begin investigation |
| Healthy | Critical | Safety metric breached OR system failure | Alert Fleet Ops Lead + Model Owner; activate incident response |
| Degraded | Critical | Breach persists > 30 minutes OR additional metrics breach | Escalate to Fleet Ops Lead; consider fallback activation |
| Degraded | Healthy | All KPIs return to green for > 15 minutes | Auto-resolve; log recovery event |
| Critical | Degraded | Primary breach resolved; secondary issues remain | Model Owner confirms partial recovery; maintain elevated monitoring |
| Critical | Healthy | All breaches resolved; root cause identified and mitigated | Model Owner + Fleet Ops Lead confirm recovery; post-incident review required |

### 2.4 Health Check Implementation

Every agent must expose a health check endpoint that returns:

```json
{
  "agent_id": "agent:payments-agent-prod-01",
  "timestamp": "2026-03-01T10:15:30Z",
  "health_state": "healthy",
  "checks": {
    "model_available": true,
    "tool_connectivity": true,
    "latency_p95_ms": 450,
    "error_rate_last_5m": 0.002,
    "active_circuit_breakers": [],
    "last_successful_interaction": "2026-03-01T10:15:12Z"
  }
}
```

---

## 3. Per-Agent KPI/SLA Governance

Every agent in the fleet has a set of KPIs, each with an SLA target and RACI ownership. The dashboard displays these KPIs with real-time values and traffic-light status.

### 3.1 KPI Definition Structure

Each KPI is defined with the following fields:

| Field | Description | Example |
|-------|-------------|---------|
| `kpi_name` | Human-readable metric name | "Task Completion Rate" |
| `metric_id` | Machine-readable identifier | `task_completion_rate` |
| `definition` | Precise definition of how the metric is calculated | "Percentage of user requests fully resolved without escalation" |
| `target` | SLA target value | `>= 92%` |
| `warning_threshold` | Value that triggers a Degraded state | `< 90%` |
| `critical_threshold` | Value that triggers a Critical state | `< 85%` |
| `measurement_window` | Time window for calculation | "Rolling 1 hour" |
| `data_source` | Where the metric data comes from | "Interaction outcome logs" |
| `raci` | RACI assignment for this KPI | See below |

### 3.2 RACI Ownership for KPIs

| KPI Category | Responsible | Accountable | Consulted | Informed |
|-------------|-------------|-------------|-----------|----------|
| **Task Completion** | AI/ML Engineer | Model Owner | Product Manager | Fleet Ops Lead |
| **Safety / Compliance** | AI/ML Engineer | Compliance Officer | Model Owner | AI Governance Committee |
| **User Satisfaction** | Product Manager | Model Owner | Customer Ops Lead | Fleet Ops Lead |
| **Latency / Performance** | MLOps Engineer | Model Owner | AI/ML Engineer | Product Manager |
| **Cost** | MLOps Engineer | Fleet Ops Lead | Model Owner | Finance |
| **Fairness** | AI/ML Engineer | Model Owner | Compliance Officer | AI Governance Committee |

### 3.3 SLA Breach Escalation

```
KPI value crosses warning threshold
    |
    v
Automated alert to Responsible party
Monitor for recovery (15-minute window)
    |
    +-- Recovery within 15 min --> Log event; no escalation
    |
    +-- No recovery in 15 min --> Escalate to Accountable party
         |
         +-- KPI value crosses critical threshold at any point
              |
              v
         Incident declared
         Fleet Ops Lead + Model Owner + Compliance (if safety KPI) notified
         Fallback procedures evaluated (see fallback-procedure.md)
         Post-incident review required within 48 hours
```

### 3.4 Example: Payments Agent KPIs

| KPI | Target | Warning | Critical | Owner (R) | Owner (A) |
|-----|--------|---------|----------|-----------|-----------|
| Task Completion Rate | >= 92% | < 90% | < 85% | AI/ML Engineer | Model Owner |
| Payment Accuracy | >= 99.5% | < 99% | < 98% | AI/ML Engineer | Model Owner |
| Avg Response Time | < 3s | > 5s | > 10s | MLOps Engineer | Model Owner |
| Escalation Rate | < 15% | > 20% | > 30% | AI/ML Engineer | Product Manager |
| Boundary Violation Rate | 0% | > 0% | > 0% | AI/ML Engineer | Compliance Officer |
| CSAT Score | >= 4.2 | < 4.0 | < 3.5 | Product Manager | Model Owner |
| Fraud Detection Precision | >= 95% | < 93% | < 90% | AI/ML Engineer | Model Owner |

---

## 4. Risk Mitigation Plan Governance

Each agent may have one or more active risk mitigation plans. The dashboard tracks mitigation progress with done/active/pending step indicators. This section governs how mitigation plans are created, tracked, and closed.

### 4.1 Mitigation Plan Lifecycle

```
Risk Identified (from eval, audit, incident, or monitoring)
    |
    v
Mitigation Plan Created
  - Risk description and severity assigned
  - Steps defined with owners, deadlines, and evidence requirements
  - Plan reviewed by Model Owner
  - Plan approved by 2nd Line (for high-risk agents)
    |
    v
Execution Phase
  - Steps tracked as pending -> active -> done
  - Dashboard shows progress bar per plan
  - Weekly status updates from step owners
  - Missed deadlines trigger escalation
    |
    v
Plan Closure
  - All steps completed with evidence documented
  - Residual risk assessment performed
  - Model Owner signs off
  - 2nd Line validates closure (for high-risk agents)
  - Plan archived in governance evidence store
```

### 4.2 Mitigation Step States

| State | Dashboard Indicator | Description |
|-------|-------------------|-------------|
| **Pending** | Grey circle | Step not yet started; waiting for prerequisite or scheduled start date |
| **Active** | Blue circle (animated) | Step currently in progress; owner is working on it |
| **Done** | Green checkmark | Step completed; evidence documented |
| **Overdue** | Red exclamation | Step past its deadline and not completed |
| **Blocked** | Orange warning | Step cannot proceed due to a dependency or blocker |

### 4.3 Escalation for Overdue Steps

- Step overdue by **1-3 business days:** Automated reminder to step owner + notification to Model Owner.
- Step overdue by **4-7 business days:** Escalation to Fleet Ops Lead. Requires revised deadline with justification.
- Step overdue by **> 7 business days:** Escalation to AI Governance Committee. Agent risk tier may be temporarily elevated.

### 4.4 Template

See [Risk Mitigation Plan Template](../templates/risk-mitigation-plan.md) for the full template with a FinTech example.

---

## 5. Agent Cost Governance

The dashboard provides a cost tab per agent with five cost dimensions. This section defines the governance framework for agent cost management.

### 5.1 Five Cost Dimensions

| Dimension | Definition | Measurement | Dashboard Display |
|-----------|-----------|-------------|-------------------|
| **Monthly Total Cost** | Total operating cost of the agent across all dimensions | Sum of all cost components | Headline number with month-over-month trend |
| **Cost per Interaction** | Average cost per customer interaction | Monthly total / number of interactions | Bar chart with daily breakdown |
| **LLM Token Cost** | Cost of input and output tokens consumed by the LLM | Token count * provider pricing | Stacked bar (input vs. output tokens) |
| **Tool Call Cost** | Cost of external API calls, database queries, and tool invocations | Per-call pricing from tool providers | Breakdown by tool type |
| **Infrastructure Cost** | Compute, storage, networking costs for the agent runtime | Cloud provider billing allocation | Monthly allocation with utilization percentage |

### 5.2 Budget Allocation and Alerting

| Control | Threshold | Action |
|---------|-----------|--------|
| **Monthly budget cap** | 100% of allocated budget | Alert Model Owner + Fleet Ops Lead; evaluate cost optimization |
| **Cost per interaction ceiling** | 150% of target cost per interaction | Alert MLOps; investigate token usage or tool call anomalies |
| **Daily cost anomaly** | > 2x daily average | Automated alert; potential runaway loop or abuse |
| **Token usage spike** | > 3x rolling 7-day average | Alert AI/ML Engineer; check for prompt inflation or reasoning loops |

### 5.3 Cost Optimization Governance

Cost optimization must not compromise safety, accuracy, or compliance. Every cost optimization proposal must include:

1. **Impact assessment:** What is the expected effect on task completion, safety, and user satisfaction?
2. **A/B test requirement:** Cost optimizations for high-risk agents require A/B testing (see [Agent Performance Evals](../evaluations/agent-performance-evals.md) Sec. 9).
3. **Rollback plan:** If the optimization degrades quality, how quickly can it be reversed?
4. **Compliance check:** Does the optimization affect audit trail completeness or regulatory compliance?

---

## 6. MLOps Lifecycle Governance

The dashboard provides an MLOps tab per agent showing drift status, retraining history, model versions, and A/B test results. This section governs the MLOps lifecycle for fleet agents.

### 6.1 Drift Detection and Response

| Drift Type | Detection Method | Dashboard Indicator | Response |
|-----------|-----------------|--------------------|---------  |
| **Data Drift** | Distribution comparison on input features (PSI, KL divergence) | Amber/Red drift badge | Investigate root cause; assess impact on agent performance |
| **Concept Drift** | Performance metric degradation over time | Trending-down arrow on KPIs | Evaluate retraining; check if business rules changed |
| **Prompt Drift** | Behavioral divergence from prompt intent (measured via eval suite) | Eval score trend line | Re-evaluate prompt; run regression tests |
| **Tool Drift** | External tool API changes or performance degradation | Tool health indicators | Update tool integrations; re-test tool-use accuracy |

### 6.2 Retraining Triggers and Approval Gates

| Trigger | Who Initiates | Approval Required | Evidence Required |
|---------|--------------|-------------------|-------------------|
| **Drift detected** (automated) | MLOps pipeline | Model Owner approves retraining plan | Drift detection report; impact analysis |
| **Performance degradation** (KPI breach) | Model Owner | Model Owner + 2nd Line for high-risk | Performance trend data; root cause analysis |
| **Scheduled retraining** (periodic) | MLOps pipeline | Model Owner sign-off | Retraining plan; data quality assessment |
| **Regulatory change** | Compliance Officer | AI Governance Committee | Regulatory impact assessment; updated eval suite |
| **Security incident** | Security Engineer | Model Owner + Security Lead | Incident report; vulnerability assessment |

### 6.3 Model Version Promotion

```
DEV Environment
  |
  v (Eval suite passes; AI/ML Engineer approves)
STAGING Environment
  |
  v (Shadow mode comparison passes; Model Owner approves)
  v (2nd Line review for high-risk agents)
PROD Environment -- Canary (5% traffic)
  |
  v (Canary metrics match or exceed baseline for 48h)
PROD Environment -- Gradual Rollout (25% -> 50% -> 100%)
  |
  v (Full rollout stable for 1 week)
PROD Environment -- Previous version decommissioned
```

**Governance requirements for each stage:**
- **DEV to STAGING:** Full eval suite passes all acceptance criteria. No safety regressions.
- **STAGING to PROD (canary):** Shadow mode results demonstrate parity or improvement. Model Owner signs off. 2nd Line review for high-risk agents.
- **PROD canary to full rollout:** All KPIs within SLA during canary period. No new safety incidents. Model Owner confirms.
- **Rollout to decommission of old version:** Old version retained for 30 days as rollback target. Audit logs from old version archived.

### 6.4 Rollback Policies

| Scenario | Rollback Speed | Decision Authority | Process |
|----------|---------------|-------------------|---------|
| **Safety metric breach** | Immediate (< 5 minutes) | On-Call Engineer (pre-authorized) | Automated rollback to previous stable version |
| **KPI breach (critical)** | Fast (< 30 minutes) | Model Owner | Manual rollback with brief impact assessment |
| **KPI breach (warning, persistent)** | Planned (< 4 hours) | Model Owner | Evaluate root cause; rollback if no fix available |
| **Cost anomaly** | Fast (< 30 minutes) | Fleet Ops Lead | Investigate cause; rollback if cost is unsustainable |

### 6.5 A/B Test Governance

| Governance Element | Requirement |
|-------------------|-------------|
| **Pre-registration** | A/B test hypothesis, primary metric, duration, and sample size documented before launch |
| **Safety floor** | All variants must meet minimum safety thresholds; no variant may be unsafe |
| **Traffic allocation** | Start at 5% for new variant; increase only after 48h of stable metrics |
| **Duration** | Minimum 1 week for prompt changes; minimum 2 weeks for model changes; minimum 4 weeks for oversight model changes |
| **Statistical rigor** | Results evaluated at p < 0.05 significance level; account for multiple comparisons |
| **Decision log** | Outcome and decision rationale documented in the agent's change log |
| **2nd Line review** | Required for high-risk agents before test launch and at each traffic increase |

---

## 7. Governance Compliance Tab

The dashboard provides a governance tab per agent showing compliance status, audit findings, bias metrics, and incident history. This section defines the data sources and governance processes behind each panel.

### 7.1 Compliance Status Indicators

| Indicator | Source Framework Artifact | Green | Amber | Red |
|-----------|--------------------------|-------|-------|-----|
| **SAFEST Compliance** | SAFEST YAML checklists | All applicable items complete | 1-3 items outstanding | > 3 items outstanding or any critical item missing |
| **EU AI Act Readiness** | Risk classification + obligation mapping | All obligations met | 1-2 obligations in progress | Any obligation overdue |
| **Permission Boundary Current** | [Agent Permission Boundaries](agent-permission-boundaries.md) | Reviewed within last 90 days | Review overdue by < 30 days | Review overdue by > 30 days |
| **Eval Suite Current** | [Agent Performance Evals](../evaluations/agent-performance-evals.md) | All evals passing | 1-2 evals failing (non-safety) | Safety eval failing |
| **Audit Findings** | Internal/external audit reports | No open findings | Open findings with remediation plan | Overdue findings |

### 7.2 Bias and Fairness Monitoring

| Metric | Measurement | Dashboard Display |
|--------|-------------|-------------------|
| **Demographic Parity Ratio** | Outcome rate ratio across protected groups | Bar chart per group; threshold line at 0.8 |
| **Equal Opportunity Ratio** | True positive rate ratio across groups | Line chart over time |
| **Disparate Impact** | Selection rate ratio (four-fifths rule) | Traffic light per protected attribute |
| **Fairness Drift** | Change in fairness metrics over time | Trend arrows with alerts on degradation |

### 7.3 Incident History

| Field | Description |
|-------|-------------|
| **Incident ID** | Unique identifier linked to incident management system |
| **Date** | When the incident occurred |
| **Severity** | P1 (Critical), P2 (High), P3 (Medium), P4 (Low) |
| **Category** | Safety violation, performance degradation, cost anomaly, compliance breach, availability outage |
| **Resolution** | Brief description of how it was resolved |
| **Root Cause** | Category of root cause (model, data, prompt, tool, infrastructure, process) |
| **Preventive Action** | Link to mitigation plan or policy change |

---

## 8. Fleet Dashboard Data Contract

This table maps every dashboard panel to its source governance artifact, data source, and refresh frequency. This is the authoritative reference for dashboard data integrity.

### 8.1 Agent Overview Panel

| Dashboard Element | Source Governance Artifact | Data Source | Refresh |
|-------------------|--------------------------|-------------|---------|
| Agent name, type, version | Agent Registry (Sec. 1) | Fleet registry database | On deployment |
| Health state indicator | Health Model (Sec. 2) | Health check endpoint + KPI aggregation | Every 30 seconds |
| Risk tier badge | [Risk Tiering Model](../../07-enterprise-implementation/risk-based-adoption/risk-tiering-model.md) | Registry + risk classification | On change |
| Oversight model label | [Human-in-the-Loop Patterns](human-in-the-loop-patterns.md) | Registry | On change |
| Owner and team | Agent Registry (Sec. 1) | Registry | On change |

### 8.2 KPI / SLA Panel

| Dashboard Element | Source Governance Artifact | Data Source | Refresh |
|-------------------|--------------------------|-------------|---------|
| KPI current value | KPI/SLA Governance (Sec. 3) | Production metrics pipeline | Per minute |
| SLA target line | KPI definition in registry | Registry | On change |
| Warning/critical thresholds | KPI definition in registry | Registry | On change |
| RACI ownership | RACI matrix (Sec. 3.2) | Registry | On change |
| Breach history | SLA Breach Escalation (Sec. 3.3) | Alerting system | Real-time |

### 8.3 Risk Mitigation Panel

| Dashboard Element | Source Governance Artifact | Data Source | Refresh |
|-------------------|--------------------------|-------------|---------|
| Active mitigation plans | Risk Mitigation Plan (Sec. 4) | Mitigation tracking system | Daily |
| Step progress (done/active/pending) | Mitigation Step States (Sec. 4.2) | Mitigation tracking system | On update |
| Overdue indicators | Escalation rules (Sec. 4.3) | Mitigation tracking system + calendar | Daily |
| Risk severity | Risk classification | Risk register | On change |

### 8.4 MLOps Panel

| Dashboard Element | Source Governance Artifact | Data Source | Refresh |
|-------------------|--------------------------|-------------|---------|
| Drift status badges | Drift Detection (Sec. 6.1) | Drift monitoring pipeline | Hourly |
| Retraining history | Retraining Triggers (Sec. 6.2) | MLOps pipeline logs | On event |
| Model version timeline | Version Promotion (Sec. 6.3) | Deployment pipeline | On deployment |
| A/B test results | A/B Test Governance (Sec. 6.5) | Experimentation platform | Per test |
| Rollback readiness | Rollback Policies (Sec. 6.4) | Deployment pipeline | On deployment |

### 8.5 Governance / Compliance Panel

| Dashboard Element | Source Governance Artifact | Data Source | Refresh |
|-------------------|--------------------------|-------------|---------|
| SAFEST compliance score | SAFEST YAML checklists | GRC platform | Weekly |
| EU AI Act readiness | Regulatory obligation mapping | Compliance tracker | Monthly |
| Permission boundary status | [Agent Permission Boundaries](agent-permission-boundaries.md) | Permission review log | On review |
| Bias / fairness metrics | [Agent Performance Evals](../evaluations/agent-performance-evals.md) | Fairness monitoring pipeline | Weekly |
| Incident history | Incident Management (Sec. 7.3) | Incident management system | Real-time |
| Audit findings | Internal audit reports | GRC platform | On audit |

### 8.6 Cost Panel

| Dashboard Element | Source Governance Artifact | Data Source | Refresh |
|-------------------|--------------------------|-------------|---------|
| Monthly total cost | Cost Governance (Sec. 5) | Cost aggregation pipeline | Daily |
| Cost per interaction | Cost Governance (Sec. 5.1) | Interaction logs + billing | Daily |
| LLM token cost | Cost Governance (Sec. 5.1) | LLM provider billing API | Daily |
| Tool call cost | Cost Governance (Sec. 5.1) | Tool invocation logs + pricing | Daily |
| Infrastructure cost | Cost Governance (Sec. 5.1) | Cloud provider billing | Daily |
| Budget utilization | Budget Alerting (Sec. 5.2) | Budget tracking system | Daily |
| Cost anomaly alerts | Cost Alerting (Sec. 5.2) | Anomaly detection pipeline | Real-time |

---

## 9. FinTech Fleet Example: 4-Agent Fleet

The following example illustrates a complete fleet configuration for a FinTech company operating four agents, as modeled in the Agent Fleet Command Dashboard reference implementation.

### 9.1 Fleet Composition

| Agent | Type | Risk Tier | Oversight | Key Function |
|-------|------|-----------|-----------|-------------|
| **Payments Agent** | Autonomous Actor | High | HOTL | Processes customer payment requests; verifies accounts; initiates transfers up to EUR 10,000 |
| **Cash Flow Agent** | Advisory | Limited | HOTA | Analyzes customer cash flow patterns; provides spending insights and forecasts |
| **Treasury Agent** | Decision-Making | High | HITL | Manages corporate treasury operations; recommends investment allocations; executes within approved parameters |
| **KYC/Onboarding Agent** | Orchestrator | High | HOTL | Coordinates customer onboarding: identity verification, risk scoring, compliance screening |

### 9.2 Fleet-Wide Health Dashboard

```
+-------------------------------------------------------------------+
|  AGENT FLEET COMMAND                          2026-03-01 10:15 UTC |
+-------------------------------------------------------------------+
|                                                                   |
|  Payments Agent     [HEALTHY]  [HIGH] [HOTL]    Cost: EUR 12,450  |
|  |- Completion: 94% (>= 92%)                                     |
|  |- Accuracy: 99.7% (>= 99.5%)                                   |
|  |- Latency P95: 2.1s (< 3s)                                     |
|  |- Escalation: 12% (< 15%)                                      |
|                                                                   |
|  Cash Flow Agent    [HEALTHY]  [LTD]  [HOTA]    Cost: EUR 4,200   |
|  |- Forecast Accuracy: 87% (>= 85%)                               |
|  |- User Engagement: 72% (>= 65%)                                 |
|  |- Latency P95: 1.8s (< 5s)                                     |
|                                                                   |
|  Treasury Agent     [DEGRADED] [HIGH] [HITL]    Cost: EUR 8,900   |
|  |- Decision Accuracy: 96% (>= 95%)                               |
|  |- Approval Latency: 18min [WARNING] (< 15min)                   |
|  |- Portfolio Alignment: 98% (>= 97%)                              |
|                                                                   |
|  KYC/Onboarding     [HEALTHY]  [HIGH] [HOTL]    Cost: EUR 6,800   |
|  |- Onboarding Completion: 88% (>= 85%)                           |
|  |- KYC Accuracy: 99.2% (>= 99%)                                  |
|  |- Avg Processing Time: 4.2min (< 5min)                          |
|  |- Compliance Rate: 100% (= 100%)                                |
|                                                                   |
+-------------------------------------------------------------------+
|  Fleet Cost (MTD): EUR 32,350 / EUR 40,000 budget (81%)           |
|  Active Mitigations: 3  |  Open Incidents: 1 (P3)                 |
+-------------------------------------------------------------------+
```

### 9.3 Example: Payments Agent Full Configuration

```yaml
agent_id: "agent:payments-agent-prod-01"
agent_name: "Payments Agent"
agent_type: "autonomous_actor"
version: "2.3.1"
model_id: "gpt-4o-2026-02"
model_version: "gpt-4o-2026-02-15"
deployment_environment: "prod"
health_state: "healthy"
risk_tier: "high"
oversight_model: "HOTL"
nhi_identity: "nhi:payments-agent-prod-01"
permission_boundary_ref: "PB-PAYMENTS-v2.3"
health_check_endpoint: "https://agents.internal/payments/health"
health_check_interval_seconds: 30

functions:
  - "initiate_payment"
  - "verify_account"
  - "check_balance"
  - "check_transaction_history"
  - "verify_beneficiary"
  - "send_payment_confirmation"

out_of_scope:
  - "close_account"
  - "modify_credit_limit"
  - "access_other_customer_data"
  - "modify_standing_orders"
  - "reverse_completed_payment"

kpis:
  - name: "Task Completion Rate"
    target: ">= 92%"
    warning: "< 90%"
    critical: "< 85%"
    raci: { R: "AI/ML Engineer", A: "Model Owner", C: "Product Manager", I: "Fleet Ops" }
  - name: "Payment Accuracy"
    target: ">= 99.5%"
    warning: "< 99%"
    critical: "< 98%"
    raci: { R: "AI/ML Engineer", A: "Model Owner", C: "Compliance", I: "Fleet Ops" }
  - name: "Average Response Time"
    target: "< 3 seconds"
    warning: "> 5 seconds"
    critical: "> 10 seconds"
    raci: { R: "MLOps Engineer", A: "Model Owner", C: "AI/ML Engineer", I: "Product Manager" }
  - name: "Escalation Rate"
    target: "< 15%"
    warning: "> 20%"
    critical: "> 30%"
    raci: { R: "AI/ML Engineer", A: "Product Manager", C: "Customer Ops", I: "Fleet Ops" }
  - name: "Boundary Violation Rate"
    target: "0%"
    warning: "> 0%"
    critical: "> 0%"
    raci: { R: "AI/ML Engineer", A: "Compliance Officer", C: "Security", I: "Governance Committee" }

owner: "Maria Chen"
team: "Payments AI Team"
compliance_frameworks:
  - "EU AI Act"
  - "PSD2"
  - "GDPR"
  - "DORA"
```

### 9.4 Example: Active Risk Mitigation Plan

```
Mitigation Plan: MP-PAY-2026-003
Agent: Payments Agent (agent:payments-agent-prod-01)
Risk: Cross-border payment routing occasionally selects non-optimal corridor
Severity: Medium
Identified: 2026-02-15

Steps:
  [DONE]    1. Analyze routing logs for non-optimal corridor selections (Owner: AI/ML Engineer, Completed: 2026-02-18)
  [DONE]    2. Identify root cause: model not accounting for FX rate fluctuation timing (Owner: AI/ML Engineer, Completed: 2026-02-20)
  [ACTIVE]  3. Implement FX rate freshness check in routing logic (Owner: AI/ML Engineer, Deadline: 2026-03-05)
  [PENDING] 4. A/B test updated routing against baseline (Owner: MLOps Engineer, Deadline: 2026-03-15)
  [PENDING] 5. Deploy to production after A/B test validation (Owner: Model Owner, Deadline: 2026-03-20)

Progress: 2/5 steps complete (40%)
```

---

## 10. Fleet-Wide Governance Policies

### 10.1 Fleet Operational Standards

| Standard | Requirement | Applies To |
|----------|------------|------------|
| **Health check frequency** | Minimum every 60 seconds for high-risk; every 5 minutes for limited/minimal | All agents |
| **KPI reporting latency** | KPI values available within 2 minutes of measurement | All agents |
| **Incident response time** | P1: < 15 min; P2: < 1 hour; P3: < 4 hours; P4: < 1 business day | All agents |
| **Rollback readiness** | Previous stable version available for immediate rollback at all times | All production agents |
| **Cost reporting** | Daily cost data available by 09:00 UTC next day | All agents |
| **Governance review** | Quarterly governance tab review by 2nd Line | High-risk agents |

### 10.2 Fleet Capacity Planning

- Monitor fleet-wide cost trends monthly. Project 3-month and 6-month costs based on traffic growth.
- Each agent's cost per interaction must be tracked against its business value (revenue enabled, cost saved, risk mitigated).
- Fleet budget allocation is reviewed quarterly by Fleet Ops Lead and Finance.

---

## Cross-References

- **Multi-Agent Governance Framework:** [multi-agent-governance-framework.md](multi-agent-governance-framework.md) -- agent types, permission model, delegation chains, degradation hierarchy
- **Agent Permission Boundaries:** [agent-permission-boundaries.md](agent-permission-boundaries.md) -- NHI identity, Agentic Tool Sovereignty, permission boundary definitions
- **Human-in-the-Loop Patterns:** [human-in-the-loop-patterns.md](human-in-the-loop-patterns.md) -- HITL/HOTL/HOTA oversight models referenced in registry
- **Customer-Facing Agent Safety:** [customer-facing-agent-safety.md](customer-facing-agent-safety.md) -- safety patterns that health and compliance metrics monitor
- **Agent Performance Evaluations:** [../evaluations/agent-performance-evals.md](../evaluations/agent-performance-evals.md) -- KPI definitions and eval methodology
- **Continuous Online Evaluation:** [../evaluations/continuous-online-evaluation.md](../evaluations/continuous-online-evaluation.md) -- monitoring infrastructure that feeds the dashboard
- **Agent Registry Entry Template:** [../templates/agent-registry-entry.yaml](../templates/agent-registry-entry.yaml) -- YAML template for agent registration
- **Risk Mitigation Plan Template:** [../templates/risk-mitigation-plan.md](../templates/risk-mitigation-plan.md) -- template for mitigation plans
- **Fallback Procedure Template:** [../templates/fallback-procedure.md](../templates/fallback-procedure.md) -- template for degradation procedures
- **Governance Dashboard Specification:** [../../06-executive/governance-dashboard-spec.md](../../06-executive/governance-dashboard-spec.md) -- executive dashboard that aggregates fleet data
- **Risk Tiering Model:** [../../07-enterprise-implementation/risk-based-adoption/risk-tiering-model.md](../../07-enterprise-implementation/risk-based-adoption/risk-tiering-model.md) -- risk classification referenced in registry

---

*Last updated: 2026-03-01*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
