# Token Usage Forecast

## Purpose

This document defines the methodology for forecasting AI token usage and associated costs, enabling proactive budget planning and variance tracking. Accurate forecasting prevents budget overruns, supports capacity planning, and provides early warning of anomalous usage patterns.

Forecasting combines historical data, seasonal patterns, growth projections, and business event calendars to predict future consumption across the hierarchical budget architecture.

## When to Use

- During annual/quarterly budget planning cycles
- When onboarding new agents or scaling existing ones
- When negotiating vendor contracts based on volume commitments
- When investigating cost anomalies or unexpected usage spikes
- When preparing financial projections for executive leadership
- When optimizing token efficiency across the agent fleet

## Who Is Responsible

| Role | R/A/C/I | Responsibility |
|------|---------|---------------|
| **Finance Analyst** | Accountable | Owns forecasting methodology and variance analysis |
| **CAIO** | Responsible | Provides growth assumptions and strategic context |
| **MLOps Engineer** | Responsible | Provides historical usage data and technical constraints |
| **Product Manager** | Consulted | Provides roadmap and feature launch timelines |
| **Team Leads** | Consulted | Provide team-level growth projections |

## Regulatory Basis

- **DORA Article 9** -- ICT risk management including capacity planning
- **SOX** -- Financial planning accuracy for material expenditures
- **SAFEST S-10** -- Cost forecasting and budget management

---

## 1. Forecasting Methodology

### 1.1 Forecast Hierarchy

Forecasts are produced at multiple levels with bottom-up aggregation:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    FORECAST HIERARCHY                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  LEVEL 1: RUN-LEVEL FORECAST                                                 │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  • Average tokens per request by skill                              │   │
│  │  • Model mix (premium vs efficient)                                 │   │
│  │  • Cache hit rate assumptions                                       │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                              ↑                                              │
│  LEVEL 2: SKILL-LEVEL FORECAST                                               │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  • Request volume by skill                                          │   │
│  │  • Seasonality patterns                                             │   │
│  │  • Growth rate assumptions                                          │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                              ↑                                              │
│  LEVEL 3: AGENT-LEVEL FORECAST                                               │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  • Agent deployment timeline                                        │   │
│  │  • User adoption curves                                             │   │
│  │  • Feature launch impact                                            │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                              ↑                                              │
│  LEVEL 4: TEAM/ORG FORECAST                                                  │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  • Aggregated agent forecasts                                       │   │
│  │  • Shared infrastructure scaling                                    │   │
│  │  • Budget allocation optimization                                   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 1.2 Forecast Components

| Component | Description | Data Source |
|-----------|-------------|-------------|
| **Baseline** | Historical average usage | Last 90 days actuals |
| **Trend** | Growth or decline pattern | Month-over-month change |
| **Seasonality** | Weekly/monthly patterns | Same day last 12 weeks |
| **Events** | Known business events | Product roadmap, marketing calendar |
| **Anomalies** | One-time adjustments | Identified outliers removed |

### 1.3 Forecast Formula

```
Forecast = Baseline × Trend Factor × Seasonality Factor × Event Impact

Where:
- Baseline = Average daily usage (last 90 days, excluding anomalies)
- Trend Factor = (1 + monthly_growth_rate) ^ (months_ahead / 12)
- Seasonality Factor = Day-of-week or day-of-month multiplier
- Event Impact = Multiplier for known events (launches, campaigns)
```

---

## 2. Forecasting Models

### 2.1 Short-Term Forecast (1-4 weeks)

**Method:** Time-series with seasonality
**Accuracy Target:** ±10%
**Update Frequency:** Weekly

```python
# Simplified short-term forecast logic
def short_term_forecast(historical_data, weeks_ahead):
    baseline = historical_data.last_90_days.mean()
    trend = calculate_trend(historical_data)
    seasonality = extract_weekly_pattern(historical_data)
    
    forecast = []
    for week in range(weeks_ahead):
        week_forecast = baseline * (1 + trend) ** week
        for day in range(7):
            day_factor = seasonality[day]
            forecast.append(week_forecast * day_factor)
    
    return forecast
```

### 2.2 Medium-Term Forecast (1-6 months)

**Method:** Trend extrapolation with event adjustments
**Accuracy Target:** ±20%
**Update Frequency:** Monthly

| Input | Weight | Source |
|-------|--------|--------|
| Historical trend | 40% | Last 6 months |
| Product roadmap | 30% | PM input |
| Marketing calendar | 20% | Campaign schedule |
| Growth assumptions | 10% | CAIO strategic plan |

### 2.3 Long-Term Forecast (6-18 months)

**Method:** Scenario-based planning
**Accuracy Target:** ±30%
**Update Frequency:** Quarterly

**Scenarios:**
- **Conservative:** 50% of projected growth
- **Base Case:** 100% of projected growth
- **Aggressive:** 150% of projected growth

---

## 3. Budget Variance Tracking

### 3.1 Variance Calculation

```
Variance % = (Actual - Forecast) / Forecast × 100

Variance $ = Actual - Forecast
```

### 3.2 Variance Categories

| Category | Threshold | Explanation | Action |
|----------|-----------|-------------|--------|
| **Green** | ±10% | Within normal range | Continue monitoring |
| **Yellow** | ±10-25% | Elevated variance | Investigate cause |
| **Red** | >±25% | Significant variance | Immediate action required |

### 3.3 Variance Root Cause Analysis

| Cause | Indicators | Investigation |
|-------|------------|---------------|
| **Volume Change** | Requests ↑/↓, tokens/request constant | Check user adoption, feature launches |
| **Model Mix Shift** | Avg cost/token ↑/↓, volume constant | Check routing logic, complexity scores |
| **Efficiency Change** | Tokens/request ↑/↓ | Check prompt engineering, context window usage |
| **Price Change** | Cost ↑/↓, usage constant | Check vendor pricing, contract terms |
| **Anomaly** | Single-day spike | Check for errors, attacks, or batch jobs |

---

## 4. ROI per Agent/Skill

### 4.1 Value Attribution

| Value Type | Metric | Calculation |
|------------|--------|-------------|
| **Time Savings** | Hours saved × hourly rate | (Manual time - Agent time) × FTE cost |
| **Error Reduction** | Errors avoided × cost per error | (Baseline error rate - Current rate) × Volume |
| **Revenue Impact** | Direct attribution | Conversion lift × Transaction value |
| **Scale Benefit** | Volume without headcount | Additional volume / Manual capacity per FTE |

### 4.2 ROI Calculation per Agent

```
Agent ROI = (Value Generated - Agent Cost) / Agent Cost × 100

Agent Cost = Model tokens + Infrastructure + Platform tools + Allocated personnel

Value Generated = Σ(Time Savings + Error Reduction + Revenue Impact + Scale Benefit)
```

### 4.3 ROI Tracking Dashboard

| Agent/Skill | Monthly Cost | Monthly Value | ROI | Trend |
|-------------|--------------|---------------|-----|-------|
| Customer Support Bot | $5,000 | $25,000 | 400% | ↑ |
| Fraud Detection | $3,000 | $15,000 | 400% | → |
| Document Processor | $2,000 | $2,500 | 25% | ↓ |
| Research Assistant | $1,000 | $800 | -20% | ↓ |

---

## 5. Forecasting Workflow

### 5.1 Monthly Forecast Cycle

```
Week 1: Data Collection
  ├── Gather actuals from previous month
  ├── Update trend calculations
  ├── Collect event calendar from PMs
  └── Identify anomalies

Week 2: Model Run
  ├── Run short-term forecast (4 weeks)
  ├── Run medium-term forecast (6 months)
  ├── Update long-term scenarios
  └── Calculate confidence intervals

Week 3: Review & Adjust
  ├── Present to team leads
  ├── Incorporate feedback
  ├── Adjust for known changes
  └── Finalize numbers

Week 4: Publish & Monitor
  ├── Publish to cost attribution dashboard
  ├── Set budget alerts
  ├── Communicate to stakeholders
  └── Begin variance tracking
```

### 5.2 Forecast Accuracy Review

| Metric | Target | Review Frequency |
|--------|--------|------------------|
| 1-week forecast accuracy | ±10% | Weekly |
| 4-week forecast accuracy | ±15% | Monthly |
| 12-week forecast accuracy | ±25% | Quarterly |
| Bias (systematic over/under) | <5% | Monthly |

---

## 6. Anomaly Detection

### 6.1 Detection Methods

| Method | Description | Sensitivity |
|--------|-------------|-------------|
| **Statistical** | Z-score > 3 from mean | High |
| **Rule-based** | >150% of forecast | Medium |
| **ML-based** | Isolation forest, autoencoder | Adaptive |

### 6.2 Anomaly Response

| Severity | Criteria | Response |
|----------|----------|----------|
| **Info** | 2-3σ deviation | Log for review |
| **Warning** | 3-4σ or >150% forecast | Alert team lead |
| **Critical** | >4σ or >200% forecast | Page on-call + investigate |

---

## 7. Related Artifacts

- [Cost Attribution Dashboard](cost-attribution-dashboard.md) -- Hierarchical cost tracking
- [Budget Cap Config](../../04-operational-governance/templates/budget-cap-config.yaml) -- Budget enforcement
- [Governance Dashboard Spec](../governance-dashboard-spec.md) -- Executive reporting

---

*Last updated: 2026-03-26 / Version: 1.0 / Classification: Internal*
