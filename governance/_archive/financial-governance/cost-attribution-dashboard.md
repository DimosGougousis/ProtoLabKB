# Cost Attribution Dashboard

## Purpose

This document specifies the hierarchical cost attribution dashboard for AI agent operations, providing visibility from board-level ROI metrics to per-token attribution. The dashboard implements the 5 cost dimensions from agent-fleet-operations.md with hierarchical budget caps: Organization → Team → Agent → Skill → Run.

Financial governance ensures that AI investments deliver measurable value while preventing cost overruns and enabling data-driven budget decisions.

## When to Use

- When setting up cost tracking for AI agent deployments
- When allocating AI budgets across teams and use cases
- When analyzing ROI of agent investments
- When identifying cost optimization opportunities
- When preparing financial reports for executive leadership
- When conducting chargeback/showback for AI resource consumption

## Who Is Responsible

| Role | R/A/C/I | Responsibility |
|------|---------|---------------|
| **Finance Controller** | Accountable | Owns cost attribution methodology and budget variance analysis |
| **CAIO** | Responsible | Defines AI investment strategy and ROI targets |
| **MLOps / Platform Engineer** | Responsible | Implements cost tracking infrastructure |
| **Product Manager** | Consulted | Defines business value metrics for ROI calculation |
| **Team Leads** | Consulted | Manage team-level budgets and cost optimization |
| **Procurement** | Consulted | Manages vendor contracts and pricing |

## Regulatory Basis

- **DORA Article 9** -- ICT risk management including cost management
- **SOX** -- Financial reporting accuracy for material AI expenditures
- **SAFEST S-10** -- Cost management and budget controls
- **SAFEST S-11** -- Resource utilization monitoring

---

## 1. Hierarchical Budget Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    HIERARCHICAL BUDGET ARCHITECTURE                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  LEVEL 1: ORGANIZATION                                                       │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Annual AI Budget: $X,XXX,XXX                                       │   │
│  │  • Model API costs                                                  │   │
│  │  • Infrastructure (compute, storage)                                │   │
│  │  • Platform tooling (observability, evaluation)                     │   │
│  │  • Personnel (AI/ML engineers, data scientists)                     │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                              │                                              │
│                              ▼                                              │
│  LEVEL 2: TEAM                                                               │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Team A Budget: $XXX,XXX        Team B Budget: $XXX,XXX             │   │
│  │  • Allocated from org budget    • Allocated from org budget         │   │
│  │  • Shared infrastructure        • Shared infrastructure             │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                              │                                              │
│                              ▼                                              │
│  LEVEL 3: AGENT                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Agent 1: $XX,XXX               Agent 2: $XX,XXX                    │   │
│  │  Agent 3: $XX,XXX               Agent 4: $XX,XXX                    │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                              │                                              │
│                              ▼                                              │
│  LEVEL 4: SKILL                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Skill A: $X,XXX                Skill B: $X,XXX                     │   │
│  │  Skill C: $X,XXX                Skill D: $X,XXX                     │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                              │                                              │
│                              ▼                                              │
│  LEVEL 5: RUN                                                                │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Run 1: $X.XX                   Run 2: $X.XX                        │   │
│  │  • Input tokens: XXX            • Input tokens: XXX                 │   │
│  │  • Output tokens: XX            • Output tokens: XX                 │   │
│  │  • Model: gpt-4o                • Model: gpt-4o-mini                │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 1.1 Budget Cap Configuration

Each level has configurable caps with alert thresholds:

| Level | Cap Type | Alert Thresholds | Enforcement |
|-------|----------|------------------|-------------|
| Organization | Annual budget | 50%, 75%, 90%, 100% | Executive escalation at 90% |
| Team | Quarterly allocation | 50%, 75%, 90%, 100% | Team lead notification at 75% |
| Agent | Monthly budget | 75%, 90%, 100% | Auto-throttle at 100% |
| Skill | Weekly budget | 75%, 90%, 100% | Model downgrade at 90% |
| Run | Per-execution | N/A | Hard stop at limit |

---

## 2. Cost Dimensions

The dashboard tracks 5 cost dimensions from agent-fleet-operations.md:

### 2.1 Model API Costs

| Metric | Description | Attribution |
|--------|-------------|-------------|
| Input tokens | Tokens sent to model | Per-run, aggregated to skill/agent/team |
| Output tokens | Tokens generated by model | Per-run, aggregated to skill/agent/team |
| Model tier | gpt-4o, gpt-4o-mini, etc. | Cost per 1K tokens varies by tier |
| Caching savings | Discounted cached tokens | Tracked as cost optimization |

**Formula:**
```
Model Cost = (Input Tokens / 1000 × Input Rate) + 
             (Output Tokens / 1000 × Output Rate) -
             (Cached Tokens / 1000 × Cache Discount)
```

### 2.2 Infrastructure Costs

| Metric | Description | Attribution Method |
|--------|-------------|-------------------|
| Compute (GPU/CPU) | Agent runtime compute | Per-pod utilization × duration |
| Memory | RAM allocation | Allocated GB × duration |
| Storage | Model weights, logs, data | Per-GB provisioned |
| Network | Data transfer | Per-GB transferred |

### 2.3 Platform Tooling Costs

| Tool Category | Examples | Attribution |
|---------------|----------|-------------|
| Observability | Langfuse, LangSmith, Arize | Per-trace, per-event |
| Evaluation | Braintrust, Giskard | Per-evaluation run |
| Guardrails | Guardrails AI, NeMo | Per-request |
| Vector Store | Pinecone, Weaviate | Per-query, per-storage |

### 2.4 Personnel Costs

| Role | Cost Attribution | Method |
|------|------------------|--------|
| AI/ML Engineers | Development time | Hours × rate per agent/skill |
| MLOps Engineers | Platform support | Allocated by agent usage |
| Data Scientists | Model improvement | Project-based allocation |

### 2.5 Overhead Costs

| Category | Description | Allocation |
|----------|-------------|------------|
| Shared infrastructure | Kubernetes, networking | Proportional to resource usage |
| Security | Scanning, compliance | Equal allocation across agents |
| Governance | Review, audit | By risk tier (high-risk = higher allocation) |

---

## 3. Dashboard Views

### 3.1 Executive View (Tier 1)

**Audience:** Board, CEO, CFO, CAIO
**Refresh:** Daily

| Metric | Current | Trend | Target |
|--------|---------|-------|--------|
| Total AI Spend (MTD) | $XXX,XXX | ↑ 12% | $XXX,XXX |
| Budget Variance | +X% | → | ±5% |
| Cost per Agent Interaction | $X.XX | ↓ 8% | $X.XX |
| AI ROI | XXX% | ↑ 15% | >200% |
| Cost Anomaly Alerts | X | ↓ | 0 |

**Visualizations:**
- Cost trend line (6 months)
- Budget vs actual by quarter
- ROI by agent category
- Cost anomaly heatmap

### 3.2 Team View (Tier 2)

**Audience:** Team leads, engineering managers
**Refresh:** Hourly

| Metric | Value | Budget | Variance |
|--------|-------|--------|----------|
| Team AI Spend (MTD) | $XX,XXX | $XX,XXX | +X% |
| Agent Count | XX | - | - |
| Avg Cost per Agent | $X,XXX | $X,XXX | -X% |
| Top Cost Driver | [Skill Name] | - | - |

**Visualizations:**
- Cost breakdown by agent
- Skill-level cost attribution
- Model usage distribution
- Budget burn-down chart

### 3.3 Agent View (Tier 3)

**Audience:** AI/ML engineers, product managers
**Refresh:** Real-time

| Metric | Value | Alert |
|--------|-------|-------|
| Current Run Cost | $X.XX | - |
| Token Usage | XXX in / XX out | - |
| Model Used | gpt-4o | - |
| Cost per 1K Interactions | $X.XX | 🟡 |

**Visualizations:**
- Real-time cost meter
- Token usage gauge
- Model routing efficiency
- Cost trend (24 hours)

---

## 4. Model Routing by Complexity

The dashboard tracks and optimizes model routing decisions:

| Complexity Score | Model Selected | Avg Cost | Use Case |
|-----------------|---------------|----------|----------|
| 0.0 - 0.3 | gpt-4o-mini | $0.001 | Simple FAQ, standard queries |
| 0.3 - 0.7 | gpt-4o-mini + caching | $0.0005 | Common patterns, cached responses |
| 0.7 - 0.9 | gpt-4o | $0.01 | Complex reasoning, analysis |
| 0.9 - 1.0 | gpt-4o + HITL | $0.015 | Critical decisions, human review |

**Optimization Opportunities:**
- Route simple queries to cheaper models
- Increase cache hit rate
- Batch requests for volume discounts
- Optimize prompt length (input tokens)

---

## 5. ROI Tracking

### 5.1 Value Metrics

| Value Category | Metric | Measurement |
|----------------|--------|-------------|
| **Efficiency** | Hours saved vs manual process | Time tracking comparison |
| **Scale** | Volume handled without headcount increase | Throughput / FTE |
| **Quality** | Error rate reduction | Before/after comparison |
| **Speed** | Response time improvement | Latency comparison |
| **Revenue** | Direct revenue attribution | Conversion tracking |

### 5.2 ROI Calculation

```
ROI = (Value Generated - Total Cost) / Total Cost × 100

Where:
- Value Generated = Efficiency gains + Quality improvements + Revenue impact
- Total Cost = Model + Infrastructure + Platform + Personnel + Overhead
```

### 5.3 ROI Dashboard

| Agent/Skill | Cost | Value | ROI | Status |
|-------------|------|-------|-----|--------|
| Customer Service Bot | $50K | $200K | 300% | 🟢 |
| Fraud Detection | $30K | $150K | 400% | 🟢 |
| Document Processing | $20K | $30K | 50% | 🟡 |
| Research Assistant | $10K | $8K | -20% | 🔴 |

---

## 6. Budget Variance Tracking

### 6.1 Variance Analysis

| Variance | Threshold | Action |
|----------|-----------|--------|
| < 5% | Normal | Continue monitoring |
| 5-10% | Elevated | Notify team lead |
| 10-20% | High | Require explanation |
| > 20% | Critical | Executive escalation |

### 6.2 Variance Root Causes

| Cause | Indicator | Mitigation |
|-------|-----------|------------|
| Usage spike | Volume ↑, unit cost → | Throttle, queue |
| Model upgrade | Unit cost ↑, volume → | Rollback, optimize |
| Inefficient prompts | Tokens/request ↑ | Prompt engineering |
| New use case | New cost center | Budget reallocation |

---

## 7. Integration with Governance Pipeline

The cost attribution dashboard integrates with Layer 2 (Budget Check) of the governance enforcement pipeline:

```
Agent Request
    │
    v
┌─────────────────────────────────────┐
│ LAYER 2: BUDGET CHECK               │
│                                     │
│ 1. Query cost attribution system    │
│    for current spend vs budget      │
│                                     │
│ 2. Estimate cost of current request │
│    based on model + complexity      │
│                                     │
│ 3. Check: current + estimate < cap? │
│                                     │
│ 4. If yes: ALLOW with cost header   │
│    If no: BLOCK with budget error   │
└─────────────────────────────────────┘
```

---

## 8. Related Artifacts

- [Token Usage Forecast](token-usage-forecast.md) -- Budget forecasting methodology
- [Budget Cap Config](../../04-operational-governance/templates/budget-cap-config.yaml) -- YAML configuration
- [Governance Dashboard Spec](../governance-dashboard-spec.md) -- Executive dashboard integration
- [Agent Fleet Operations](../../03-runtime-governance/agentic-workflows/agent-fleet-operations.md) -- Cost dimensions reference

---

*Last updated: 2026-03-26 / Version: 1.0 / Classification: Internal*
