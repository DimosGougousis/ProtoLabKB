# Drift Detection Runbook

## Purpose

This runbook provides step-by-step investigation and remediation procedures for each type of drift detected in production AI systems: data drift, concept drift, prompt drift, and tool-use drift. It translates drift detection alerts from the [monitoring dashboard](./model-monitoring-dashboard.md) into concrete actions -- who investigates, what evidence to gather, when to escalate, and which remediation options are available. For regulated FinTech, drift is not just a model quality concern -- a drifted model may no longer satisfy the acceptance criteria under which it was validated and approved for deployment, creating regulatory non-compliance risk.

## When to Use

- When a drift alert fires on the [monitoring dashboard](./model-monitoring-dashboard.md) (Section 2.5)
- When periodic drift analysis (weekly or monthly) reveals a trend toward threshold breach
- When a model revalidation identifies unexplained performance changes
- When a customer complaint or incident investigation suggests the model is behaving differently than at deployment
- When preparing for SAFEST item S-12 evidence on drift detection and response

## Who Is Responsible

| Role | R | A | C | I |
|------|---|---|---|---|
| **MLOps / Platform Engineer** | X | | | | Investigates drift alerts, executes remediation procedures |
| **Model Owner** | | X | | | Decides on remediation approach, approves retraining or rollback |
| **Data Engineer** | X | | | | Investigates data pipeline changes that may cause data drift |
| **ML Engineer** | | | X | | Consulted on model retraining, threshold adjustment, prompt updates |
| **Compliance Officer (2nd Line)** | | | X | | Consulted on whether drift invalidates regulatory compliance evidence |
| **CAIO** | | | | X | Informed of Severity 1 drift events that affect high-risk systems |

## Regulatory Basis

- **SAFEST item S-12** -- Data drift detection: mechanisms to detect production data distribution changes with defined thresholds and response procedures
- **SAFEST item S-20** -- Validation frequency: periodic revalidation triggered by material changes including drift
- **EU AI Act Article 72** -- Post-market monitoring including changes that may affect compliance
- **EU AI Act Article 9(2)(b)** -- Risk management for reasonably foreseeable changes
- **DORA Article 8** -- ICT risk management including detection of anomalous activities
- **ISO/IEC 42001 Clause 9.1** -- Monitoring, measurement, analysis, and evaluation

---

## 1. Drift Type Overview

| Drift Type | Definition | Detection Method | Typical Causes | Severity Default |
|-----------|-----------|-----------------|----------------|-----------------|
| **Data Drift** | Statistical distribution of input features shifts from training/reference data | PSI, KS test, Jensen-Shannon divergence | Seasonal changes, upstream data schema changes, new customer segments, market shifts | P2 -- Urgent |
| **Concept Drift** | Relationship between inputs and correct outputs changes over time | Performance metric degradation on labeled data | Market regime change, new fraud patterns, regulatory changes, customer behavior evolution | P2 -- Urgent |
| **Prompt Drift** | Distribution of user prompts/queries shifts from what the system was designed for | Embedding similarity, topic clustering | Product changes, new use cases, customer base changes, adversarial probing | P3 -- Warning |
| **Tool-Use Drift** | Agent tool selection patterns deviate from expected baseline | Chi-squared test, tool frequency analysis | Tool availability changes, prompt template updates, model version changes, emerging capabilities | P3 -- Warning |

---

## 2. Data Drift Investigation

### 2.1 Alert Triage

**Trigger:** PSI > 0.2 or KS statistic p-value < 0.01 for any monitored feature.

**Step 1: Identify the drifted features**
- Open the monitoring dashboard, filter to the affected model
- Navigate to Row 4 (Drift Detection)
- List all features with PSI > 0.2 or p-value < 0.01
- Note: drift in a single low-importance feature may be P4; drift in multiple high-importance features is P1

**Step 2: Check for upstream data pipeline changes**
- Query data pipeline logs for the past 7 days
- Check: Did a new data source come online? Was a schema changed? Did a provider update their API?
- Check: Did ETL jobs fail or produce partial data?
- If an upstream change is identified, this may be a data quality issue rather than true drift

**Step 3: Assess feature importance**
- Cross-reference drifted features with the model's feature importance ranking
- High-importance feature drifted: escalate to P2 or higher
- Low-importance feature drifted: log and monitor, maintain at P3

**Step 4: Evaluate impact on model output**
- Check model quality metrics (Row 2) for correlation with the drift event
- Run a sample of recent predictions through the model validation suite
- Compare output distributions (predictions, confidence scores) before and after drift onset

**Step 5: Document findings**
- Record in the drift investigation ticket:
  - Which features drifted and by how much
  - Identified root cause (if known)
  - Impact on model performance (measured or estimated)
  - Recommended remediation

### 2.2 Escalation Criteria for Data Drift

| Condition | Action |
|-----------|--------|
| Single low-importance feature, PSI 0.2-0.3, no performance impact | Log, monitor, schedule review at weekly ops meeting |
| Multiple features drifted, or single high-importance feature | Escalate to Model Owner; target remediation within 7 days |
| PSI > 0.5 on any feature, or measurable performance degradation | Escalate to P1; initiate compensating controls (increased human review, tighter guardrails) |
| Drift on features related to protected attributes (age, gender, ethnicity proxies) | Immediately notify Compliance Officer; run bias evaluation |

### 2.3 Remediation Options for Data Drift

| Option | When to Use | Procedure | Governance Impact |
|--------|------------|-----------|------------------|
| **Adjust monitoring thresholds** | Drift reflects a legitimate new normal (e.g., seasonal shift) | Update baseline reference distribution; document justification; get Model Owner approval | Update the monitoring setup checklist; note in quarterly governance report |
| **Update feature engineering** | Upstream data format changed but semantics are preserved | Update feature pipeline; validate feature distributions; run regression tests | No governance gate required if functionally equivalent |
| **Retrain model** | Drift reflects genuine distribution shift that degrades performance | Follow retraining procedure (Section 5); pass through deployment gate | Requires full deployment gate review per [pre-deployment gate](../../02-development-governance/checklists/pre-deployment-gate.yaml) |
| **Rollback to previous model** | Performance degradation is severe and no quick fix is available | Execute rollback within RTO; notify Model Owner and Compliance | Document as incident per [incident report template](./ai-incident-report.md) |
| **Apply input filters** | Drift is caused by a specific data anomaly (e.g., bad data source) | Add input validation rules to data pipeline; quarantine anomalous data | Update data quality checklist |

---

## 3. Concept Drift Investigation

### 3.1 Alert Triage

**Trigger:** Primary evaluation metric degrades > 5% from baseline on labeled production data.

**Step 1: Confirm the signal is real**
- Check: Is the labeled dataset for concept drift detection itself representative? (labeling lag is common)
- Check: Is the sample size sufficient for statistical significance?
- If using human labels: verify labeling quality has not degraded (label drift vs. concept drift)

**Step 2: Identify the drift pattern**
- **Sudden concept drift:** Performance drops sharply on a specific date -- look for external events (regulation change, market event, product launch, fraud pattern evolution)
- **Gradual concept drift:** Performance degrades slowly over weeks -- look for slow-moving trends (customer behavior evolution, demographic shifts)
- **Recurring concept drift:** Performance oscillates -- look for cyclical patterns (seasonality, business cycles)

**Step 3: Segment the impact**
- Break down performance by customer segment, transaction type, geographic region
- Identify: Is the drift universal or concentrated in specific segments?
- Concentrated drift may indicate a new fraud pattern or a segment the model was never trained on

**Step 4: Compare with data drift**
- Check: Does concept drift correlate with a data drift event?
- If yes: data drift may be the root cause; resolve data drift first and re-evaluate
- If no: the underlying relationship has changed; retraining is likely necessary

**Step 5: Assess regulatory impact**
- Does the degraded performance breach the acceptance criteria defined at the deployment gate?
- If yes: the model may no longer be compliant with the conditions under which it was approved
- Notify Compliance Officer and initiate revalidation

### 3.2 Escalation Criteria for Concept Drift

| Condition | Action |
|-----------|--------|
| < 3% degradation, not trending worse | Log, increase monitoring frequency, schedule review |
| 3-5% degradation, or trending worse over 2+ weeks | Escalate to Model Owner; begin retraining preparation |
| > 5% degradation on primary metric | Escalate to P1; apply compensating controls; begin emergency retraining or rollback |
| Performance below deployment gate acceptance criteria | Notify Compliance Officer; consider model suspension per [SAFEST S-20](../regulatory/safest-checklist-detailed.md) |
| Degradation concentrated in protected group segments | Immediately notify Compliance Officer; run full [bias assessment](../../02-development-governance/templates/bias-assessment-report.md) |

### 3.3 Remediation Options for Concept Drift

| Option | When to Use | Procedure | Governance Impact |
|--------|------------|-----------|------------------|
| **Retrain on recent data** | New patterns exist in recent production data | Collect and label recent data; retrain; validate; deploy through gate | Full [deployment gate](../../02-development-governance/checklists/pre-deployment-gate.yaml) review |
| **Online learning update** | Model supports incremental learning | Apply incremental updates with validation; monitor for stability | Requires Model Owner approval and regression testing |
| **Ensemble with new model** | Legacy model handles base case; new model handles emerged pattern | Train specialized model for new pattern; combine via ensemble or routing | Architecture change -- requires design review and deployment gate |
| **Rule-based overlay** | Drift is caused by a specific, identifiable pattern change | Add business rules to handle the specific new pattern alongside model predictions | Document rule rationale; include in next model retraining cycle |
| **Model suspension + manual fallback** | Performance is below acceptable threshold and no quick fix exists | Activate fallback procedure per [SAFEST S-13](../regulatory/safest-checklist-detailed.md); route to manual review | Document as P1 incident; CAIO notification required |

---

## 4. Prompt Drift Investigation

### 4.1 Alert Triage

**Trigger:** Cosine similarity of prompt embedding distribution vs. reference drops below 0.8.

**Step 1: Characterize the new prompt distribution**
- Sample 100-200 recent prompts from the drifted period
- Run topic clustering to identify new topic areas
- Compare with the prompt categories used during development and testing

**Step 2: Identify the source of new prompts**
- Product change: Did the product team add a new feature or use case that channels different queries to the agent?
- Customer base change: Did a new customer segment onboard with different interaction patterns?
- Adversarial activity: Are the new prompts attempting prompt injection or jailbreaking? (cross-reference with [OWASP guide](../guides/owasp-top10-llm-guide.md))
- Organic evolution: Are customers naturally discovering new ways to use the system?

**Step 3: Evaluate system performance on new prompts**
- Run the system's evaluation suite on a sample of the new prompt distribution
- Measure: accuracy, safety compliance, guardrail trigger rate, hallucination rate
- Compare with baseline performance on the reference prompt distribution

**Step 4: Assess safety implications**
- Do new prompts attempt to make the agent perform actions outside its [permission boundaries](../../03-runtime-governance/agentic-workflows/agent-permission-boundaries.md)?
- Does the system hallucinate more on the new prompt distribution?
- Do new prompts trigger topics the agent was not designed to handle (financial advice, personal data requests)?

### 4.2 Escalation Criteria for Prompt Drift

| Condition | Action |
|-----------|--------|
| New prompts are within design scope, system performs well | Update reference distribution; log as expected evolution |
| New prompts reveal a gap in evaluation coverage | Add new test cases to eval suite; no immediate system change needed |
| System performs poorly on new prompts but no safety risk | Escalate to Model Owner; prioritize prompt template or system prompt update |
| New prompts include adversarial patterns | Escalate to Security team; update guardrails; file [vulnerability assessment](./vulnerability-assessment.md) |
| System provides harmful, non-compliant, or hallucinated responses to new prompts | P1 escalation; apply immediate guardrail restrictions; consider scope reduction |

### 4.3 Remediation Options for Prompt Drift

| Option | When to Use | Procedure | Governance Impact |
|--------|------------|-----------|------------------|
| **Update reference distribution** | Drift reflects legitimate, safe expansion of use | Recompute embeddings with expanded prompt set; update thresholds | Document new scope; update system documentation |
| **Update system prompt / prompt templates** | System needs better instruction for new prompt types | Revise prompts; test on new distribution; validate safety | Requires prompt change review per development governance |
| **Add guardrails for new prompt categories** | New prompts include out-of-scope or risky topics | Configure topic-based guardrails; test guardrail effectiveness | Update [guardrail deployment checklist](../../03-runtime-governance/checklists/guardrail-deployment-checklist.yaml) |
| **Expand training data / fine-tuning** | Model cannot handle new prompts adequately with prompt engineering alone | Collect examples; fine-tune or retrain; validate | Full [deployment gate](../../02-development-governance/checklists/pre-deployment-gate.yaml) review |
| **Restrict system scope** | New prompts represent a use case the system should not handle | Update guardrails to redirect or refuse; communicate scope to users | Product decision -- requires Product Owner + Model Owner alignment |

---

## 5. Tool-Use Drift Investigation

### 5.1 Alert Triage

**Trigger:** Chi-squared test p-value < 0.01 on tool selection distribution vs. baseline.

**Step 1: Map the distribution shift**
- Compare tool invocation frequencies: baseline period vs. current period
- Identify: Which tools are used more? Which are used less? Are any new tools being invoked?
- Visualize the distribution shift (bar chart of tool frequencies, baseline vs. current)

**Step 2: Correlate with system changes**
- Was a new tool added to the agent's toolkit? (Expected to cause distribution shift)
- Was a prompt template or system prompt updated? (May change tool selection behavior)
- Was the model version updated? (New model versions may have different tool-use preferences)
- Did the prompt distribution drift? (New prompts may require different tools)

**Step 3: Evaluate tool-use quality**
- For tools used more frequently: Are they being used correctly? Check tool call parameters and outcomes
- For tools used less frequently: Were they previously overused (improvement) or are needed uses being missed?
- Check for tool-use anti-patterns: repeated failed calls, unnecessary tool chains, tool calls with malformed parameters

**Step 4: Assess permission and safety implications**
- Is the agent attempting to use tools outside its [permission boundaries](../../03-runtime-governance/agentic-workflows/agent-permission-boundaries.md)?
- Are tool invocations resulting in unexpected side effects (database writes, API calls, financial transactions)?
- Cross-reference with [delegation chain audit](../../03-runtime-governance/agentic-workflows/delegation-chain-audit.md) for multi-agent systems

### 5.2 Escalation Criteria for Tool-Use Drift

| Condition | Action |
|-----------|--------|
| Shift explained by an intentional system change (new tool, prompt update) | Update baseline distribution; document as expected |
| Shift unexplained but tool-use quality is maintained | Investigate root cause; schedule deeper analysis |
| Agent is using tools incorrectly (wrong parameters, wrong context) | Escalate to ML Engineer; update prompt instructions or tool descriptions |
| Agent attempts unauthorized tool use or permission escalation | P1 escalation; restrict agent permissions immediately; file [vulnerability assessment](./vulnerability-assessment.md) |
| Tool-use drift correlates with increased customer complaints or errors | Escalate to Model Owner; consider rollback |

### 5.3 Remediation Options for Tool-Use Drift

| Option | When to Use | Procedure | Governance Impact |
|--------|------------|-----------|------------------|
| **Update baseline distribution** | Drift reflects legitimate evolution after intentional changes | Recompute baseline from post-change period; validate stability | Document new baseline; update monitoring config |
| **Update tool descriptions** | Agent misuses tools due to ambiguous descriptions | Clarify tool descriptions in agent configuration; test | Requires prompt/config change review |
| **Adjust tool permissions** | Agent accesses tools it should not or fails to use required tools | Update [permission boundaries](../../03-runtime-governance/agentic-workflows/agent-permission-boundaries.md) | Security change -- requires Security Engineer review |
| **Update system prompt** | Agent's tool selection strategy needs correction | Revise system prompt with clearer tool selection guidance | Requires prompt change review |
| **Retrain / fine-tune** | Tool-use behavior cannot be corrected via prompting | Retrain with correct tool-use examples | Full deployment gate review |

---

## 6. Retraining Procedure

When drift remediation requires model retraining, follow this procedure:

1. **Data collection:** Assemble a retraining dataset that includes recent production data capturing the new distribution. Ensure data quality per the [data quality checklist](../../02-development-governance/checklists/data-quality-checklist.yaml)
2. **Labeling:** Obtain ground truth labels for new data. For concept drift, this often requires human annotation
3. **Training:** Retrain the model using the updated dataset. Version the model and dataset
4. **Validation:** Run the full evaluation suite per [eval-driven development](../../02-development-governance/evaluations/eval-driven-development.md). The model must meet or exceed the acceptance criteria from the original deployment gate
5. **Bias testing:** Run the [bias testing checklist](../../02-development-governance/checklists/bias-testing-checklist.yaml) to verify no fairness regression
6. **Deployment gate:** Pass through the [pre-deployment gate](../../02-development-governance/checklists/pre-deployment-gate.yaml) -- drift-related retraining does not skip any gate checks
7. **Canary deployment:** Deploy to canary environment; monitor for 24-48 hours before full rollout
8. **Update baselines:** After full deployment, update all monitoring baselines and reference distributions
9. **Document:** Update the [model card](../../02-development-governance/templates/model-card.md) with the new training data and performance characteristics

---

## 7. Communication Templates

### 7.1 P1 Drift Alert (Immediate Notification)

```
Subject: [P1] Critical Drift Detected — {System Name}
To: Model Owner, Compliance Officer, CAIO
CC: #ai-ops-critical

SEVERITY: P1 — Critical Drift
SYSTEM: {System Name} ({System ID})
DRIFT TYPE: {Data / Concept / Prompt / Tool-Use}
DETECTED AT: {Timestamp}
METRIC: {Metric name} = {Current value} (threshold: {Threshold value})

IMPACT ASSESSMENT:
- Model performance: {Measured or estimated impact}
- Customer impact: {Estimated number of affected users/transactions}
- Regulatory impact: {Below acceptance criteria: Yes/No}

IMMEDIATE ACTIONS:
- {Compensating controls applied}
- {Investigation in progress}

NEXT UPDATE: Within {2 hours / 4 hours}
INCIDENT TICKET: {Jira ticket URL}
```

### 7.2 Drift Resolution Summary

```
Subject: [RESOLVED] Drift Event — {System Name} — Root Cause: {Summary}
To: Model Owner, Compliance Officer
CC: #ai-ops-monitoring

DRIFT EVENT RESOLVED
SYSTEM: {System Name}
DRIFT TYPE: {Type}
DETECTED: {Start timestamp}
RESOLVED: {End timestamp}
DURATION: {Hours/days}

ROOT CAUSE: {Brief description}
REMEDIATION: {Action taken}
VERIFICATION: {How resolution was confirmed}

FOLLOW-UP ACTIONS:
- {Any remaining items, e.g., model retraining scheduled, baseline update}
- {Process improvements identified}

POST-MORTEM: {Scheduled date, if applicable}
```

### 7.3 Monthly Drift Status Report

```
Subject: Monthly Drift Report — {Month Year}
To: AI Governance Committee, CAIO
CC: Model Owners

DRIFT SUMMARY — {Month Year}

Total drift alerts fired: {N}
  - P1 (Critical): {N}
  - P2 (Urgent): {N}
  - P3 (Warning): {N}
  - P4 (Info): {N}

By drift type:
  - Data drift: {N} alerts across {N} systems
  - Concept drift: {N} alerts across {N} systems
  - Prompt drift: {N} alerts across {N} systems
  - Tool-use drift: {N} alerts across {N} systems

Remediations completed: {N}
  - Retraining: {N}
  - Threshold adjustment: {N}
  - Prompt update: {N}
  - Rollback: {N}
  - Risk accepted: {N}

Systems currently in drift (unresolved): {N}
  {List of systems with current drift status}

Trend: {Improving / Stable / Deteriorating} vs. previous month
```

---

## Cross-References

- [Model Monitoring Dashboard](./model-monitoring-dashboard.md) -- source of drift alerts; Section 2.5 defines drift metrics
- [Drift Detection Evaluations](../evaluations/drift-detection-evals.md) -- statistical test methodology for drift detection
- [AI Incident Report Template](./ai-incident-report.md) -- template for when drift escalates to an incident
- [Pre-Deployment Gate Checklist](../../02-development-governance/checklists/pre-deployment-gate.yaml) -- gate that retrained models must pass
- [Bias Testing Checklist](../../02-development-governance/checklists/bias-testing-checklist.yaml) -- fairness verification for retrained models
- [Agent Permission Boundaries](../../03-runtime-governance/agentic-workflows/agent-permission-boundaries.md) -- permission model relevant to tool-use drift
- [Monitoring Setup Checklist](../checklists/monitoring-setup-checklist.yaml) -- ensures drift monitoring is configured before deployment
- [SAFEST Compliance Tracker](../regulatory/safest-compliance-tracker.yaml) -- tracks SAFEST S-12, S-20 compliance
- [Governance Dashboard Specification](../../06-executive/governance-dashboard-spec.md) -- receives aggregate drift metrics for strategic view

---

*Last updated: 2026-03-01* / *Version: 1.0* / *Classification: Internal / Regulatory Preparation*
