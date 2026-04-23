# Model Monitoring Dashboard Specification

## Purpose

This document specifies the operational monitoring dashboard for production AI systems, designed for MLOps engineers, platform engineers, and on-call responders. Unlike the [executive governance dashboard](../../06-executive/governance-dashboard-spec.md) which provides strategic KPIs for board and CAIO consumption, this dashboard provides real-time operational telemetry: latency, error rates, throughput, cost, drift signals, and SLA adherence. It is the primary tool for detecting, diagnosing, and resolving production issues before they become governance incidents.

For agentic AI systems in regulated FinTech, operational monitoring is not optional -- it is the real-time enforcement layer for the governance commitments made during the Discovery and Development phases. Every SLA promised to DNB, every acceptance criterion approved at the deployment gate, every guardrail configured in runtime governance must have a corresponding metric on this dashboard.

## When to Use

- When deploying a new AI system to production -- the monitoring dashboard must be configured before the deployment gate is passed
- When the on-call engineer is triaging a production alert or incident
- During daily standups and weekly operational reviews for production AI systems
- When conducting the monthly monitoring health review required by the [monitoring setup checklist](../../04-operational-governance/checklists/monitoring-setup-checklist.yaml)
- When preparing evidence for SAFEST items S-12, S-14, T-15, T-17

## Who Is Responsible

| Role | R | A | C | I |
|------|---|---|---|---|
| **MLOps / Platform Engineer** | X | | | | Builds and maintains the dashboard, configures alerts, manages data pipelines |
| **Model Owner** | | X | | | Defines SLA targets and acceptable thresholds per model |
| **On-Call Engineer** | X | | | | Uses the dashboard for real-time triage and incident response |
| **Data Engineer** | | | X | | Consulted on data pipeline metrics and upstream data quality signals |
| **Compliance Officer (2nd Line)** | | | X | | Consulted on regulatory metric requirements; reviews SLA definitions |
| **CAIO** | | | | X | Informed via aggregate metrics surfaced in the [governance dashboard](../../06-executive/governance-dashboard-spec.md) |

## Regulatory Basis

- **SAFEST item S-12** -- Data drift detection with defined thresholds and response procedures
- **SAFEST item S-14** -- Recovery Time Objective with tested recovery procedures
- **SAFEST item T-15** -- AI performance dashboards with real-time visibility
- **SAFEST item T-17** -- Production monitoring dashboards covering availability, latency, error rates
- **EU AI Act Article 72** -- Post-market monitoring system for high-risk AI systems
- **EU AI Act Article 9(8)** -- Logging capability proportionate to risk
- **DORA Article 8** -- ICT risk management including detection of anomalous activities
- **DORA Article 10** -- Detection mechanisms for anomalous activities and ICT-related incidents
- **ISO/IEC 42001 Clause 9.1** -- Monitoring, measurement, analysis, and evaluation

---

## 1. Dashboard Architecture

### 1.1 Data Flow

```
Production AI System
        |
        v
+------------------+     +------------------+     +-------------------+
| Telemetry        |---->| Time-Series DB   |---->| Dashboard Engine   |
| Collectors       |     | (Prometheus /    |     | (Grafana /         |
| (OpenTelemetry,  |     |  InfluxDB /      |     |  Datadog /         |
|  LangSmith,      |     |  CloudWatch)     |     |  custom)           |
|  custom SDK)     |     +------------------+     +-------------------+
+------------------+            |                         |
        |                       v                         v
        |              +------------------+     +-------------------+
        +------------->| Alert Manager    |---->| Notification      |
                       | (PagerDuty /     |     | Channels          |
                       |  OpsGenie /      |     | (Slack, PagerDuty,|
                       |  AlertManager)   |     |  Email, Jira)     |
                       +------------------+     +-------------------+
```

### 1.2 Instrumentation Requirements

Every production AI system must emit the following telemetry signals using **OpenTelemetry gen_ai semantic conventions**:

| Signal Type | Collection Method | Minimum Granularity | Retention |
|-------------|------------------|---------------------|-----------|
| Request/response logs | OpenTelemetry spans with gen_ai.* attributes | Per-request | 90 days hot, 2 years cold |
| Latency metrics | OpenTelemetry histogram | Per-request, aggregated per minute | 13 months |
| Error counts | Counter metric | Per-request, aggregated per minute | 13 months |
| Throughput | Counter metric | Per-minute aggregation | 13 months |
| Cost signals | Custom metric | Per-request (token count, API cost) | 13 months |
| Model prediction outputs | Structured log | Sampled (10% minimum for non-PII) | 90 days |
| Drift statistics | Batch computation | Hourly or daily depending on volume | 13 months |
| Agent tool invocations | Structured log | Per-invocation | 90 days |
| Guardrail trigger events | Counter + log | Per-trigger | 13 months |

#### OpenTelemetry gen_ai.* Semantic Conventions

The dashboard uses OpenTelemetry's gen_ai semantic conventions for standardized AI system observability:

| Attribute | Description | Example |
|-----------|-------------|---------|
| `gen_ai.system` | The AI system/provider | "openai", "anthropic", "azure_openai" |
| `gen_ai.request.model` | Model identifier | "gpt-4o-2026-02" |
| `gen_ai.request.max_tokens` | Max tokens requested | 4096 |
| `gen_ai.request.temperature` | Sampling temperature | 0.7 |
| `gen_ai.usage.input_tokens` | Input tokens consumed | 150 |
| `gen_ai.usage.output_tokens` | Output tokens generated | 42 |
| `gen_ai.response.finish_reason` | Why generation stopped | "stop", "length", "content_filter" |
| `gen_ai.operation.name` | Operation type | "chat", "completion", "embedding" |

**Reference:** [OpenTelemetry Gen AI Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/attributes-registry/gen-ai/)

**Implementation Example:**
```python
from opentelemetry import trace
from opentelemetry.semconv.ai import GenAIAttributes

tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("agent_execution") as span:
    span.set_attribute(GenAIAttributes.GEN_AI_SYSTEM, "openai")
    span.set_attribute(GenAIAttributes.GEN_AI_REQUEST_MODEL, "gpt-4o")
    span.set_attribute(GenAIAttributes.GEN_AI_USAGE_INPUT_TOKENS, input_tokens)
    span.set_attribute(GenAIAttributes.GEN_AI_USAGE_OUTPUT_TOKENS, output_tokens)
```

---

## 2. Key Metrics Catalog

### 2.1 Availability and Latency

| Metric | Definition | Target | Alert Threshold | Alert Severity |
|--------|-----------|--------|-----------------|----------------|
| **Uptime** | Percentage of time the AI endpoint returns non-error responses | 99.9% (monthly) | < 99.5% over 5-min window | P1 -- Page |
| **P50 Latency** | Median end-to-end response time including model inference | Model-specific (define at deployment) | > 2x baseline | P2 -- Urgent |
| **P95 Latency** | 95th percentile response time | Model-specific | > 3x baseline | P2 -- Urgent |
| **P99 Latency** | 99th percentile response time | Model-specific | > 5x baseline | P1 -- Page |
| **Error Rate (5xx)** | Percentage of requests returning server errors | < 0.1% | > 1% over 5-min window | P1 -- Page |
| **Error Rate (4xx)** | Percentage of requests returning client errors | < 1% | > 5% over 5-min window | P2 -- Urgent |
| **Timeout Rate** | Percentage of requests exceeding timeout threshold | < 0.5% | > 2% over 5-min window | P1 -- Page |

### 2.2 Throughput and Capacity

| Metric | Definition | Target | Alert Threshold | Alert Severity |
|--------|-----------|--------|-----------------|----------------|
| **Requests per Second (RPS)** | Current request volume | N/A (baseline) | > 150% of peak baseline | P3 -- Warning |
| **Queue Depth** | Pending requests awaiting processing | < 100 | > 500 | P2 -- Urgent |
| **Concurrent Connections** | Active connections to AI endpoint | Infrastructure-dependent | > 80% of capacity | P2 -- Urgent |
| **GPU / CPU Utilization** | Compute resource usage for inference | < 70% average | > 90% sustained for 5 min | P2 -- Urgent |
| **Memory Utilization** | RAM usage for model serving | < 80% | > 90% | P1 -- Page |
| **Batch Processing Lag** | Delay in offline/batch AI pipelines | < 15 min behind schedule | > 60 min behind | P2 -- Urgent |

### 2.3 Model Quality Metrics

| Metric | Definition | Target | Alert Threshold | Alert Severity |
|--------|-----------|--------|-----------------|----------------|
| **Primary Eval Metric** | Model-specific (AUC-ROC, F1, accuracy, BLEU) | Defined at deployment gate | > 5% degradation from baseline | P1 -- Page |
| **Prediction Confidence Distribution** | Mean and variance of model confidence scores | Stable vs. reference | KL-divergence > 0.1 | P2 -- Urgent |
| **Null/Empty Response Rate** | Percentage of responses that are empty or null | < 0.1% | > 1% | P1 -- Page |
| **Guardrail Trigger Rate** | Percentage of responses blocked by guardrails | Baseline-dependent | > 2x baseline over 1 hour | P2 -- Urgent |
| **Hallucination Rate** | Percentage of responses flagged as hallucinated (via eval) | < 2% (sampled) | > 5% | P1 -- Page |
| **Toxicity Rate** | Percentage of responses flagged as toxic/harmful | 0% target | Any detection | P1 -- Page |

### 2.4 Cost Metrics

| Metric | Definition | Target | Alert Threshold | Alert Severity |
|--------|-----------|--------|-----------------|----------------|
| **Cost per Request** | Average API/inference cost per request | Budget-dependent | > 150% of budget per-request cost | P3 -- Warning |
| **Daily Spend** | Total AI infrastructure + API spend per day | Budget-dependent | > 120% of daily budget | P2 -- Urgent |
| **Token Usage (LLM)** | Input + output tokens per request | Model-specific | > 2x baseline average | P3 -- Warning |
| **Monthly Burn Rate** | Projected monthly cost based on trailing 7-day average | Budget allocation | > 110% of monthly allocation | P2 -- Urgent |
| **Cost per Successful Outcome** | Cost divided by successful (non-error, non-guardrail-blocked) responses | Business-defined | > 200% of target | P3 -- Warning |

### 2.5 Drift Metrics

| Metric | Definition | Target | Alert Threshold | Alert Severity |
|--------|-----------|--------|-----------------|----------------|
| **Data Drift Score** | PSI or KS statistic comparing production vs. reference features | PSI < 0.1 | PSI > 0.2 | P2 -- Urgent |
| **Concept Drift Score** | Model performance on labeled subset vs. baseline | < 3% degradation | > 5% degradation | P2 -- Urgent |
| **Prompt Drift** | Semantic similarity of prompt distributions vs. reference | Cosine similarity > 0.9 | < 0.8 | P3 -- Warning |
| **Tool-Use Drift** | Distribution of agent tool selections vs. baseline | Chi-squared p > 0.05 | p < 0.01 | P3 -- Warning |
| **Label Drift** | Distribution of model output labels vs. baseline | PSI < 0.1 | PSI > 0.2 | P2 -- Urgent |

See the [drift detection evaluations](../evaluations/drift-detection-evals.md) for detailed statistical test methodology and the [drift detection runbook](./drift-detection-runbook.md) for investigation and remediation procedures.

### 2.6 Agentic System Metrics

| Metric | Definition | Target | Alert Threshold | Alert Severity |
|--------|-----------|--------|-----------------|----------------|
| **Task Completion Rate** | Percentage of agent tasks completed successfully | > 95% | < 90% over 1 hour | P2 -- Urgent |
| **Permission Boundary Violations** | Agent attempts to invoke unauthorized tools or exceed scope | 0 | Any violation | P1 -- Page |
| **Delegation Chain Depth** | Average and max depth of multi-agent delegation | < 3 average | Max > 5 | P3 -- Warning |
| **Human Escalation Rate** | Percentage of interactions escalated to human | Baseline-dependent | > 2x baseline | P3 -- Warning |
| **Tool Invocation Failure Rate** | Percentage of tool calls that fail | < 1% | > 5% | P2 -- Urgent |
| **Autonomous Decision Count** | Number of autonomous decisions per hour | Baseline-dependent | > 150% of baseline | P3 -- Warning |

---

## 3. Dashboard Layout

### 3.1 Panel Organization

The dashboard is organized into rows. Each row is collapsible. The default view shows rows 1-3 expanded; rows 4-6 collapsed.

```
+=====================================================================+
| ROW 1: SERVICE HEALTH (always visible)                               |
| [Uptime SLI] [P50/P95/P99 Latency] [Error Rate] [RPS] [Active Alerts] |
+=====================================================================+
| ROW 2: MODEL QUALITY (always visible)                                |
| [Primary Eval Metric] [Confidence Distribution] [Guardrail Triggers]  |
| [Hallucination Rate] [Toxicity Rate]                                  |
+=====================================================================+
| ROW 3: COST (always visible)                                         |
| [Daily Spend] [Cost per Request] [Token Usage] [Monthly Burn Rate]    |
+=====================================================================+
| ROW 4: DRIFT DETECTION (collapsed by default)                        |
| [Data Drift PSI] [Concept Drift] [Prompt Drift] [Tool-Use Drift]     |
+=====================================================================+
| ROW 5: AGENTIC OPERATIONS (collapsed by default, agent systems only) |
| [Task Completion] [Permission Violations] [Delegation Depth]          |
| [Escalation Rate] [Tool Failures]                                     |
+=====================================================================+
| ROW 6: INFRASTRUCTURE (collapsed by default)                         |
| [CPU/GPU Utilization] [Memory] [Queue Depth] [Connections]            |
+=====================================================================+
```

### 3.2 Time Range Controls

| Preset | Use Case |
|--------|----------|
| Last 15 minutes | Active incident triage |
| Last 1 hour | Recent alert investigation |
| Last 6 hours | Shift handoff review |
| Last 24 hours | Daily standup review |
| Last 7 days | Weekly trend analysis |
| Last 30 days | Monthly SLA reporting |
| Custom range | Incident post-mortem analysis |

### 3.3 Filtering and Drill-Down

The dashboard must support filtering by:

- **AI System / Model ID** -- isolate metrics for a single production model
- **Environment** -- production, staging, canary
- **Region** -- if multi-region deployment
- **Agent ID** -- for multi-agent systems, filter by specific agent
- **Customer segment** -- if relevant for fairness monitoring
- **Risk tier** -- high-risk, medium-risk, low-risk per EU AI Act classification

---

## 4. Alerting Rules

### 4.1 Alert Severity Definitions

| Severity | Response Time | Notification Channel | Escalation |
|----------|--------------|---------------------|------------|
| **P1 -- Page** | Immediate (< 5 min acknowledgement) | PagerDuty / phone call to on-call | Auto-escalate to secondary on-call after 15 min if unacknowledged |
| **P2 -- Urgent** | Within 30 min | Slack #ai-ops-alerts + Jira ticket auto-created | Auto-escalate to P1 if unresolved after 2 hours |
| **P3 -- Warning** | Within 4 hours (business hours) | Slack #ai-ops-monitoring + Jira ticket | Review in next daily standup |
| **P4 -- Info** | Next business day | Logged to monitoring system | Review in weekly ops review |

### 4.2 Alert Routing

```
P1 Alert Triggered
  |
  +--> PagerDuty: On-Call Engineer (primary)
  +--> Slack: #ai-ops-critical
  +--> Jira: Auto-create INC ticket (Severity 1)
  |
  +-- If unacknowledged after 15 min:
       +--> PagerDuty: On-Call Engineer (secondary)
       +--> Slack: @model-owner
       |
       +-- If unacknowledged after 30 min:
            +--> PagerDuty: Engineering Manager
            +--> Email: CAIO (informational)
```

### 4.3 Alert Deduplication and Suppression

- **Deduplication window:** Identical alerts within 5 minutes are grouped into a single notification
- **Maintenance windows:** Scheduled maintenance (model redeployment, infrastructure upgrade) suppresses alerts for a defined period; must be registered in advance via the ops calendar
- **Flapping detection:** Alerts that fire and resolve more than 3 times within 30 minutes are grouped and escalated as a flapping alert (P2 minimum)
- **Dependency suppression:** If a parent infrastructure alert fires (e.g., database down), dependent model alerts are suppressed and linked to the parent incident

---

## 5. On-Call Procedures

### 5.1 On-Call Rotation

| Attribute | Requirement |
|-----------|-------------|
| **Rotation type** | Weekly rotation among qualified MLOps/platform engineers |
| **Team size** | Minimum 4 engineers in rotation (prevents burnout) |
| **Handoff** | Monday 09:00 CET; 30-minute overlap between outgoing and incoming on-call |
| **Handoff checklist** | Review open incidents, active alerts, recent deployments, upcoming maintenance windows |
| **Training** | All on-call engineers must complete AI incident response training (see [incident report template](./ai-incident-report.md)) |
| **Escalation contacts** | On-call engineer has direct contact for: Model Owners, Security team, Compliance Officer, CAIO (P1 only) |

### 5.2 Alert Response Procedure

**Step 1: Acknowledge** (within SLA per severity)
- Acknowledge the alert in PagerDuty/OpsGenie
- Post initial status in #ai-ops-critical (for P1/P2)

**Step 2: Assess**
- Open the monitoring dashboard filtered to the affected system
- Check Row 1 (Service Health) for scope of impact
- Check Row 2 (Model Quality) for model-specific degradation
- Determine: Is this infrastructure or model-level?

**Step 3: Diagnose**
- For latency/error issues: check Row 6 (Infrastructure), check upstream dependencies
- For model quality issues: check Row 4 (Drift Detection), review recent deployments
- For agent issues: check Row 5 (Agentic Operations), review permission violation logs
- For cost spikes: check Row 3 (Cost), identify source (token explosion, traffic spike, misconfigured retry)

**Step 4: Mitigate**
- Apply the appropriate runbook (see cross-references below)
- For model rollback: follow the [model rollback procedure](../../02-development-governance/guides/verification-before-deployment.md)
- For drift-related issues: follow the [drift detection runbook](./drift-detection-runbook.md)
- For security-related issues: follow the [OWASP LLM guide](../guides/owasp-top10-llm-guide.md)

**Step 5: Document**
- For P1/P2: initiate an [AI incident report](./ai-incident-report.md)
- For P3/P4: update the Jira ticket with findings and resolution
- Update the monitoring dashboard with any new thresholds or alerts discovered during investigation

---

## 6. SLA Monitoring

### 6.1 Internal SLAs

Each production AI system must have documented SLAs covering:

| SLA Category | Metric | Measurement Window | Reporting |
|-------------|--------|-------------------|-----------|
| **Availability** | Uptime percentage | Monthly, rolling 30 days | Dashboard Row 1 + monthly SLA report |
| **Latency** | P95 response time within target | Monthly, per-hour measurement | Dashboard Row 1 + monthly SLA report |
| **Quality** | Primary eval metric within threshold | Weekly, rolling 7 days | Dashboard Row 2 + weekly ops review |
| **Incident Response** | MTTR within SLA per severity | Per-incident | Incident report + monthly aggregate |
| **Recovery** | RTO within target | Per-incident (and tested quarterly) | Incident report + quarterly DR test |

### 6.2 SLA Breach Procedure

1. SLA breach detected by automated monitoring
2. Auto-generate SLA breach ticket in Jira (linked to the SLA definition document)
3. Model Owner notified immediately
4. Root cause analysis required within 5 business days
5. Corrective action plan due within 10 business days
6. SLA breach reported in the monthly operational review and surfaced in the [governance dashboard](../../06-executive/governance-dashboard-spec.md)
7. Repeated SLA breaches (3 in a quarter) trigger a formal governance review by the AI Governance Committee

### 6.3 SLA Error Budget

Each production AI system has an error budget per quarter:

- **Availability:** 100% - SLA target = allowed downtime (e.g., 99.9% SLA = 43.2 min/month)
- **Quality:** Number of hours the primary eval metric can be below threshold before triggering a governance review
- **Spend:** Cost overrun allowance (typically 10% above monthly budget)

When error budget is exhausted, the team must prioritize reliability work over feature work until the budget is restored. This is enforced through sprint planning integration (see [governance in agile sprints](../../07-enterprise-implementation/process-integration/governance-in-agile-sprints.md)).

---

## 7. Dashboard Implementation Checklist

Before a production AI system can pass the deployment gate, the following dashboard components must be operational:

- [ ] All metrics in Section 2.1 (Availability and Latency) are instrumented and visible
- [ ] All metrics in Section 2.3 (Model Quality) have defined baselines and alert thresholds
- [ ] At least one cost metric from Section 2.4 is tracked and alerted
- [ ] Data drift detection from Section 2.5 is configured (see [drift detection evals](../evaluations/drift-detection-evals.md))
- [ ] For agentic systems: all metrics in Section 2.6 are instrumented
- [ ] Alert routing (Section 4.2) is tested with a synthetic alert
- [ ] On-call rotation (Section 5.1) has at least 4 engineers and a defined schedule
- [ ] SLA targets (Section 6.1) are documented and approved by the Model Owner
- [ ] Dashboard is registered in the monitoring setup checklist (see [monitoring setup checklist](../checklists/monitoring-setup-checklist.yaml))

---

## 8. Relationship to Executive Dashboard

This operational dashboard feeds into but is distinct from the [executive governance dashboard](../../06-executive/governance-dashboard-spec.md):

| Dimension | Operational Dashboard (this doc) | Executive Dashboard |
|-----------|----------------------------------|-------------------|
| **Audience** | MLOps, on-call engineers, model owners | Board, CAIO, AI Ethics Board |
| **Refresh** | Real-time (sub-minute) | Daily aggregate, monthly report |
| **Metrics** | Raw telemetry, detailed breakdowns | Traffic-light summaries, trends |
| **Purpose** | Detect and resolve production issues | Strategic oversight, compliance posture |
| **Drill-down** | Per-request, per-model, per-agent | Per-system, per-risk-tier |
| **Alert target** | Engineering teams | CAIO, Governance Committee |

Aggregate metrics from this dashboard flow to the executive dashboard via the data pipeline defined in the [governance dashboard spec](../../06-executive/governance-dashboard-spec.md), Section 7 (Data Integration).

---

## Cross-References

- [Executive Governance Dashboard Specification](../../06-executive/governance-dashboard-spec.md) -- strategic dashboard that consumes aggregated data from this operational dashboard
- [Monitoring Setup Checklist](../checklists/monitoring-setup-checklist.yaml) -- YAML checklist for verifying all monitoring is configured before deployment
- [Drift Detection Evaluations](../evaluations/drift-detection-evals.md) -- statistical test methodology for drift metrics
- [Drift Detection Runbook](./drift-detection-runbook.md) -- step-by-step investigation and remediation for drift alerts
- [AI Incident Report Template](./ai-incident-report.md) -- template initiated when P1/P2 alerts escalate to incidents
- [Eval Reporting Dashboard](../evaluations/eval-reporting-dashboard.md) -- dashboard focused on evaluation results rather than operational telemetry
- [OWASP Top 10 for LLMs Guide](../guides/owasp-top10-llm-guide.md) -- security-focused investigation procedures
- [Agent Fleet Operations](../../03-runtime-governance/agentic-workflows/agent-fleet-operations.md) -- operational procedures for multi-agent systems
- [Governance in Agile Sprints](../../07-enterprise-implementation/process-integration/governance-in-agile-sprints.md) -- error budget enforcement in sprint planning

---

*Last updated: 2026-03-01* / *Version: 1.0* / *Classification: Internal / Regulatory Preparation*
