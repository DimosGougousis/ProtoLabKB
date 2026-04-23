# Drift Detection Evaluations for AI Systems

## Purpose

This document defines the automated detection framework for data drift, concept drift, prompt drift, and tool-use drift in production AI systems. It specifies detection methods, statistical tests, monitoring pipelines, alerting thresholds, severity classification, and response procedures. For agentic AI systems in FinTech, drift is not merely a model quality concern -- it is a regulatory compliance risk, because a drifted model may produce outputs that no longer meet the acceptance criteria under which it was validated and approved for production.

Drift detection is the early warning system that prevents silent degradation from becoming a customer-impacting incident or a regulatory finding.

## When to Use

- When deploying any AI system to production -- drift detection must be configured before go-live
- When reviewing monitoring coverage for existing production AI systems
- When investigating unexplained performance degradation or anomalous agent behavior
- When a scheduled or event-triggered revalidation identifies potential drift
- When preparing evidence for SAFEST item S-12 (data drift detection)
- When designing monitoring pipelines for new AI systems during Development Governance

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **MLOps / Platform Engineer** | **Responsible** -- implements drift detection pipelines, configures alerts, maintains monitoring infrastructure |
| **Model Owner** | **Accountable** -- defines drift thresholds per model, owns response decisions (retrain, recalibrate, rollback) |
| **Data Engineer** | **Responsible** -- monitors data pipeline quality and upstream data source stability |
| **Compliance Officer (2nd Line)** | **Reviewer** -- reviews drift reports for regulatory implications; validates that drift response meets SAFEST S-12 |
| **AI Governance Committee** | **Informed** -- receives quarterly drift trend reports; escalation target for Severity 1 drift events |
| **CAIO** | **Informed** -- receives aggregate drift posture in Tier 1 dashboard |

## Regulatory Basis

- **SAFEST item S-12** -- Data drift detection: mechanisms to detect when production data distributions deviate from training data, with defined thresholds and response procedures
- **SAFEST item S-20** -- Validation frequency: periodic revalidation triggered by material changes including drift
- **EU AI Act Article 72** -- Post-market monitoring system for high-risk AI, including monitoring for changes that may affect compliance
- **EU AI Act Article 9(2)(b)** -- Risk management must address risks from reasonably foreseeable changes in the intended use
- **DORA Article 8** -- ICT risk management includes detection of anomalous activities
- **ISO/IEC 42001 Clause 9.1** -- Monitoring, measurement, analysis, and evaluation

---

## 1. Drift Taxonomy

Not all drift is the same. Each drift type has different causes, detection methods, and response urgencies.

### 1.1 Data Drift (Covariate Shift)

**Definition:** The statistical distribution of input features in production diverges from the distribution in the training data, while the underlying relationship between inputs and outputs remains stable.

**FinTech examples:**
- Transaction amount distribution shifts due to seasonal patterns (holiday spending) or macroeconomic changes (inflation)
- Customer demographic mix changes as the product enters new markets
- Document types submitted for KYC shift from passports to national ID cards after geographic expansion
- Payment method distribution changes as new payment rails are adopted

**Why it matters:** Even if the input-output relationship is stable, the model may have poor performance in regions of the feature space that were underrepresented in training data.

### 1.2 Concept Drift

**Definition:** The underlying relationship between input features and the target variable changes over time. The same input that previously indicated "not fraud" now indicates "fraud" due to evolving fraud patterns.

**FinTech examples:**
- New fraud typologies emerge that the model was never trained on (e.g., AI-generated deepfake identity documents)
- Regulatory changes alter what constitutes a suspicious transaction (updated Wwft guidance)
- Market regime changes alter credit risk profiles (interest rate shifts, recession)
- Customer behavior patterns change post-pandemic (increased digital-only activity)

**Why it matters:** Concept drift directly degrades model accuracy. The model's learned relationships are no longer valid.

### 1.3 Prompt Drift

**Definition:** For LLM-based systems, the effectiveness of system prompts and few-shot examples degrades over time due to upstream model updates, context window changes, or evolving user interaction patterns.

**FinTech examples:**
- LLM provider updates the base model version, subtly changing how it interprets existing system prompts
- Customer interaction patterns evolve, and the prompt's few-shot examples no longer represent typical queries
- Regulatory terminology changes, and the prompt's instructions reference outdated terms
- Agent guardrail prompts become less effective against new jailbreaking techniques

**Why it matters:** Prompt drift is invisible to traditional statistical monitoring. It requires LLM-specific evaluation methods.

### 1.4 Tool-Use Drift (Agentic Systems)

**Definition:** In agentic AI systems, the pattern of tool invocations changes over time -- the agent calls different tools, uses different parameter ranges, or invokes tools in different sequences than during validation.

**FinTech examples:**
- A customer service agent begins using the `escalate_to_supervisor` tool 40% more frequently after a model update
- A fraud detection agent starts invoking `block_account` directly instead of `flag_for_review`, bypassing the intended human-in-the-loop step
- A multi-agent system develops a new delegation pattern not covered by the original permission boundary tests
- An agent's tool call error rate increases because upstream API schemas changed

**Why it matters:** Tool-use drift can signal permission boundary erosion, changed model behavior, or upstream system changes that affect the agent's decision-making.

---

## 2. Detection Methods

### 2.1 Statistical Tests for Data Drift

| Test | What It Detects | Best For | Threshold Guidance |
|------|----------------|----------|-------------------|
| **Population Stability Index (PSI)** | Shift in score or feature distributions | Univariate continuous features, model score distributions | PSI < 0.1: no action; 0.1-0.25: investigate; > 0.25: significant drift |
| **Kullback-Leibler (KL) Divergence** | Information-theoretic distance between distributions | Probability distributions, categorical features | KL > 0.1: investigate; > 0.5: significant drift |
| **Maximum Mean Discrepancy (MMD)** | Multivariate distribution shift using kernel methods | High-dimensional feature spaces, embedding drift | p-value < 0.05: statistically significant drift |
| **Kolmogorov-Smirnov (KS) Test** | Maximum difference between two cumulative distributions | Univariate continuous features | p-value < 0.01 with Bonferroni correction for multiple features |
| **Chi-Square Test** | Distribution shift in categorical variables | Categorical features (country, product type, payment method) | p-value < 0.01 |
| **Wasserstein Distance (Earth Mover's Distance)** | Minimum cost of transforming one distribution into another | When magnitude of shift matters, not just statistical significance | Context-dependent; compare to baseline variability |
| **Jensen-Shannon Divergence** | Symmetric measure of distribution similarity | When a symmetric metric is preferred over KL divergence | JSD > 0.1: investigate; > 0.3: significant |

### 2.2 Concept Drift Detection

| Method | How It Works | When to Use |
|--------|-------------|-------------|
| **Performance monitoring against delayed labels** | Compare model predictions to actual outcomes once ground truth becomes available | Fraud detection (label available after investigation), credit scoring (label available at loan maturity) |
| **ADWIN (Adaptive Windowing)** | Maintains a variable-length window that shrinks when drift is detected | Streaming data with real-time label availability |
| **Page-Hinkley Test** | Detects changes in the mean of a sequence of observations | When monitoring a single performance metric over time |
| **DDM (Drift Detection Method)** | Monitors error rate and triggers when error rate exceeds a threshold based on standard deviation | Online learning scenarios with immediate feedback |
| **EDDM (Early Drift Detection Method)** | More sensitive variant of DDM that detects gradual drift earlier | When early detection of gradual concept drift is critical |

### 2.3 Prompt Drift Detection

| Method | How It Works | When to Use |
|--------|-------------|-------------|
| **Golden dataset re-evaluation** | Re-run a curated set of test cases against the system and compare outputs to baseline | After any LLM provider model update; on a scheduled cadence |
| **Semantic similarity tracking** | Compare current outputs to historical outputs for the same inputs using embedding similarity | Continuous monitoring for gradual prompt effectiveness degradation |
| **Guardrail bypass rate monitoring** | Track the percentage of interactions where guardrails are triggered or bypassed | Continuous; a rising bypass rate indicates prompt drift |
| **Eval suite regression** | Run the full eval suite from pre-deployment gate and compare scores to deployment baseline | Scheduled (weekly for high-risk, monthly for others) |

### 2.4 Tool-Use Drift Detection (Agentic Systems)

| Method | How It Works | When to Use |
|--------|-------------|-------------|
| **Tool call distribution monitoring** | Track which tools the agent calls and how often; compare to baseline distribution | Continuous for all agentic systems |
| **Tool parameter range monitoring** | Monitor the distribution of parameters passed to tools (e.g., refund amounts, account IDs) | Continuous; detect when parameter ranges exceed validation boundaries |
| **Sequence pattern analysis** | Detect changes in the typical sequence of tool calls within an interaction | When agent workflow patterns are well-defined |
| **Delegation chain monitoring** | In multi-agent systems, track which sub-agents are invoked and how delegation patterns change | Continuous for multi-agent architectures |

---

## 3. Monitoring Pipeline Architecture

### 3.1 Data Collection Layer

```
Production AI System
       |
       +---> Feature Store Snapshot (hourly/daily)
       |       -> Feature distributions
       |       -> Missing value rates
       |       -> Cardinality changes
       |
       +---> Prediction Log
       |       -> Model scores/outputs
       |       -> Confidence values
       |       -> Latency metrics
       |
       +---> Outcome Store (delayed)
       |       -> Ground truth labels
       |       -> Human override decisions
       |       -> Customer feedback
       |
       +---> Agent Trace Store
               -> Tool call logs (from LangSmith / Arize Phoenix / Langfuse)
               -> Reasoning spans
               -> Delegation events
```

### 3.2 Drift Computation Layer

**Scheduled drift checks (batch):**
- Run daily for high-risk systems, weekly for limited-risk, monthly for minimal-risk
- Compare current window (e.g., last 7 days) against reference window (training data distribution or deployment baseline)
- Compute all applicable statistical tests per feature
- Store results in drift metrics time series

**Continuous drift checks (streaming):**
- For high-volume, high-risk systems (e.g., real-time fraud detection)
- ADWIN or Page-Hinkley on key performance metrics
- Sliding window PSI computation on top features
- Tool call frequency anomaly detection for agentic systems

### 3.3 Alerting Layer

| Severity | Condition | Response Time | Notification |
|----------|----------|---------------|-------------|
| **Drift-1 (Critical)** | PSI > 0.25 on 3+ features simultaneously, OR concept drift confirmed with >10% performance drop, OR agent tool-use pattern violates permission boundaries | < 1 hour | Model Owner, On-Call Engineer, 2nd Line |
| **Drift-2 (High)** | PSI > 0.25 on 1-2 features, OR concept drift suspected with 5-10% performance drop, OR prompt drift causing guardrail bypass rate > 5% | < 4 hours | Model Owner, MLOps |
| **Drift-3 (Medium)** | PSI 0.1-0.25 on multiple features, OR gradual performance decline (2-5%) over 30 days | < 24 hours | Model Owner (automated notification) |
| **Drift-4 (Low)** | PSI 0.1-0.25 on 1-2 features, OR minor tool-use distribution changes within acceptable bounds | Next business day | Logged for trend analysis |

---

## 4. Drift Severity Classification

### 4.1 Classification Matrix

| Factor | Low (Drift-4) | Medium (Drift-3) | High (Drift-2) | Critical (Drift-1) |
|--------|--------------|------------------|----------------|-------------------|
| **Number of features drifted** | 1-2 features, PSI 0.1-0.25 | 3+ features, PSI 0.1-0.25 | 1-2 features, PSI > 0.25 | 3+ features, PSI > 0.25 |
| **Performance impact** | No measurable impact | 2-5% degradation trend | 5-10% degradation | > 10% degradation |
| **Customer impact** | None observable | Potential future impact | Measurable quality reduction | Direct customer harm |
| **Regulatory implication** | None | Monitoring documentation gap | Acceptance criteria breach | Validation assumptions invalidated |
| **Agent behavior change** | Minor parameter range shift | Tool call frequency shift > 20% | New tool call patterns | Permission boundary violation |

### 4.2 Escalation Criteria

- **Drift-4:** Logged and included in monthly drift report. No immediate action required.
- **Drift-3:** Model Owner reviews within 24 hours. If sustained for > 14 days, escalate to Drift-2.
- **Drift-2:** Investigation within 4 hours. Root cause analysis within 48 hours. If not resolved within 7 days, escalate to Drift-1.
- **Drift-1:** Immediate response. Consider circuit breaker activation and fallback to manual process (SAFEST S-13). Trigger event-based revalidation. Notify AI Governance Committee.

---

## 5. Response Procedures

### 5.1 Investigation Workflow

1. **Confirm drift is real** -- Rule out instrumentation errors, data pipeline issues, or seasonal patterns that are expected
2. **Characterize the drift** -- Which features? Which direction? How fast? Is it sudden or gradual?
3. **Assess impact** -- Is model performance actually degraded? Check against acceptance criteria from the model card
4. **Identify root cause** -- Upstream data source change? Market shift? Regulatory change? Customer behavior evolution? Provider model update?
5. **Document findings** -- Record in the drift detection log with evidence

### 5.2 Remediation Options

| Option | When to Use | Approval Required |
|--------|------------|------------------|
| **No action (monitor)** | Drift is within acceptable bounds and performance is stable | Model Owner |
| **Adjust thresholds** | Drift reflects a legitimate permanent shift in the operating environment | Model Owner + 2nd Line |
| **Update prompts** | Prompt drift due to LLM provider changes or evolving user patterns | Model Owner |
| **Retrain model** | Concept drift confirmed; current model no longer fits the data | Model Owner + Committee approval for high-risk |
| **Recalibrate model** | Model ranking is correct but probability calibration has shifted | Model Owner |
| **Rollback model** | Recent model update introduced regression; previous version was stable | Model Owner (immediate); Committee ratification within 48h |
| **Activate fallback** | Drift severity is critical and no immediate remediation is available | On-Call Engineer (immediate); Model Owner ratification |
| **Decommission system** | Drift is fundamental and the AI approach is no longer viable | Committee approval required |

### 5.3 Post-Remediation Verification

After any remediation action:
1. Re-run the full drift detection suite against the remediated system
2. Re-run the eval suite from the pre-deployment gate to confirm acceptance criteria are met
3. Document remediation in the model change log (SAFEST A-12)
4. Update the drift detection baseline if thresholds were legitimately adjusted
5. Update the model card with the drift event and remediation taken

---

## 6. Scheduled vs. Continuous Drift Checks

### 6.1 Minimum Cadence by Risk Tier

| Risk Tier | Data Drift | Concept Drift | Prompt Drift | Tool-Use Drift |
|-----------|-----------|---------------|-------------|---------------|
| **High-risk** (EU AI Act Annex III) | Daily batch + continuous streaming | Daily (where labels available) | Weekly eval suite re-run | Continuous |
| **Limited-risk** | Weekly batch | Weekly (where labels available) | Monthly eval suite re-run | Daily batch |
| **Minimal-risk** | Monthly batch | Monthly (where labels available) | Quarterly eval suite re-run | Weekly batch |

### 6.2 Event-Triggered Drift Checks

Run drift detection immediately (regardless of scheduled cadence) when:
- Upstream LLM provider announces a model version change
- A data pipeline source is modified or replaced
- A significant change in transaction volume occurs (> 2x normal)
- A regulatory change affects the domain the model operates in
- An incident is reported that could be drift-related
- A new market or customer segment is onboarded

---

## 7. Tooling Integration

### 7.1 Observability Platforms for Drift Detection

| Tool | Drift Detection Capability | Integration Point |
|------|---------------------------|-------------------|
| **Arize Phoenix** | Built-in drift monitors for embeddings, features, and predictions; automated PSI and KL divergence computation | Production feature and prediction logging; connects to drift alerting pipeline |
| **LangSmith** | Trace-level monitoring for prompt effectiveness; output quality scoring over time | Agent reasoning trace analysis; prompt drift detection via eval feedback |
| **Langfuse** | Open-source trace monitoring with custom scoring; track metric trends over time | Self-hosted option for sensitive FinTech data; prompt and agent behavior monitoring |
| **Opik** | Experiment tracking with baseline comparison; metric regression detection | Compare current production behavior against validation experiment baselines |
| **Evidently AI** | Dedicated drift detection library; PSI, KS, Wasserstein, MMD out of the box | Batch drift computation pipeline; generates drift reports for governance evidence |
| **NannyML** | Concept drift estimation without ground truth labels (CBPE, DLE methods) | When ground truth labels are delayed (e.g., credit default labels take months) |

### 7.2 Dashboard Integration

Drift detection results feed into two dashboards:
- **Model Monitoring Dashboard** (this pillar, `templates/model-monitoring-dashboard.md`) -- engineering/MLOps view with detailed drift metrics per feature
- **Governance Dashboard** (executive, `../../06-executive/governance-dashboard-spec.md`) -- Tier 1/2 view with aggregate drift posture (Green/Amber/Red per system)

---

## 8. FinTech-Specific Drift Considerations

### 8.1 Regulatory-Driven Drift

Financial regulation changes can cause concept drift by altering what constitutes a "correct" output:
- Updated Wwft (Anti-Money Laundering) guidance changes the definition of suspicious transactions
- PSD2 Strong Customer Authentication exemptions are modified, changing which transactions require SCA
- MiCAR implementation changes crypto-asset classification, affecting risk scoring

**Mitigation:** Maintain a regulatory change register. When relevant regulations change, trigger an event-based drift evaluation and update model acceptance criteria.

### 8.2 Seasonal and Cyclical Patterns

Financial data exhibits strong seasonal patterns (holiday spending, tax season, salary cycles). These must be distinguished from genuine drift:
- Maintain seasonal baselines in addition to overall baselines
- Compare current data to the same period in prior years, not just the most recent period
- Flag drift only when the current deviation exceeds historical seasonal variability

### 8.3 Market Regime Changes

Major economic events (interest rate changes, market crashes, pandemics) can cause sudden, fundamental shifts:
- Implement regime detection alongside drift detection
- Define "regime change" thresholds that are distinct from normal drift thresholds
- Document decision criteria for when a regime change warrants model retraining vs. manual process fallback

---

## Cross-References

- **Model Monitoring Dashboard:** [../templates/model-monitoring-dashboard.md](../templates/model-monitoring-dashboard.md) -- operational dashboard displaying drift metrics
- **Drift Detection Runbook:** [../templates/drift-detection-runbook.md](../templates/drift-detection-runbook.md) -- step-by-step procedures for drift response
- **Regression Testing for AI:** [regression-testing-for-ai.md](regression-testing-for-ai.md) -- detecting regressions that may be caused by drift-driven retraining
- **Continuous Online Evaluation:** [../../03-runtime-governance/evaluations/continuous-online-evaluation.md](../../03-runtime-governance/evaluations/continuous-online-evaluation.md) -- real-time performance monitoring that may detect drift symptoms
- **Eval Reporting Dashboard:** [eval-reporting-dashboard.md](eval-reporting-dashboard.md) -- visualization of drift trends alongside other eval metrics
- **Governance Dashboard Spec:** [../../06-executive/governance-dashboard-spec.md](../../06-executive/governance-dashboard-spec.md) -- executive-level drift posture reporting
- **SAFEST Checklist:** [../regulatory/safest-checklist-detailed.md](../regulatory/safest-checklist-detailed.md) -- S-12 (drift detection), S-20 (revalidation frequency)
- **Traceability Guide:** [../guides/traceability-with-langchain.md](../guides/traceability-with-langchain.md) -- observability tools for trace-level drift investigation
- **Tool Landscape:** [../../05-cross-cutting/tool-landscape.md](../../05-cross-cutting/tool-landscape.md) -- drift detection tool evaluations
- **RACI Matrix:** [../../05-cross-cutting/governance-roles-raci.md](../../05-cross-cutting/governance-roles-raci.md) -- drift response role assignments

---

*Last updated: 2026-03-01*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
