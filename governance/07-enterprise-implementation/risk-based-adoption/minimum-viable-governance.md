# Minimum Viable Governance (MVG)

> **Purpose:** Define the lightest governance profile that is still defensible for minimal and limited-risk AI systems, so that FinTechs can establish baseline governance quickly without drowning in process for low-risk systems.
>
> **Regulatory Basis:** EU AI Act (residual obligations for all AI); DNB Good Practice for AI (applies to all AI in financial services); SAFEST checklist (proportional application).
>
> **Key Principle:** Even the lowest-risk AI system in a regulated financial institution must have some governance. MVG defines the absolute floor. If you cannot do these 10 items, you are not ready to use AI in a regulated environment.

---

## 1. When to Use Minimum Viable Governance

MVG applies to:
- AI systems classified as **minimal risk** under the [Risk Tiering Model](risk-tiering-model.md)
- AI systems classified as **limited risk** during their initial deployment phase (with a commitment to upgrade to standard governance within 90 days)
- **Proof-of-concept / pilot AI systems** that are not yet serving customers in production

MVG does NOT apply to:
- Any AI system classified as **high risk** (use full governance -- see [Risk Tiering Model](risk-tiering-model.md))
- Any AI system that directly makes or materially influences decisions about customers
- Any AI system processing special category personal data (GDPR Article 9)
- Any AI system operating in production for customer-facing decisions

---

## 2. The MVG Checklist: 10 Items for Day One

These 10 items are the absolute minimum. They can be completed in 1-2 days for a simple AI system.

| # | Item | SAFEST Ref | Deliverable | Effort |
|---|------|-----------|-------------|--------|
| **1** | **Register the AI system** in the AI system inventory with: name, purpose, risk classification, data inputs, outputs, model owner | S-01 | One row in the AI system inventory spreadsheet/database | 30 min |
| **2** | **Assign a model owner** -- a named individual accountable for this system's performance, compliance, and risk | A-05 | Name recorded in inventory | 5 min |
| **3** | **Write a basic model card** -- one page covering: what it does, what data it uses, known limitations, when not to trust it | T-12 | 1-page markdown document in the model's repository | 2 hours |
| **4** | **Document the algorithm choice** -- why this approach and not a simpler alternative (rule-based, lookup table, manual process) | S-02 | One paragraph in the model card | 30 min |
| **5** | **Define 3 acceptance criteria** -- measurable metrics that must pass before deployment and during operation | S-03 | 3 metrics with thresholds documented in the model card | 1 hour |
| **6** | **Run the acceptance criteria** -- actually execute the evaluations, record the results, and confirm all 3 pass | S-03 | Evaluation results stored alongside the model card | 2 hours |
| **7** | **Document the fallback** -- what happens if this AI system fails or produces garbage? Who gets notified? What manual process takes over? | S-13 | One section in the model card or a separate half-page document | 1 hour |
| **8** | **Enable basic logging** -- log inputs, outputs, and errors so you can investigate issues after the fact | A-11 | Logging configuration documented; logs flowing to centralized system | 1-2 hours |
| **9** | **Complete AI literacy training** -- the model owner and anyone operating this system has completed the organization's general AI awareness training | K-09 | Training completion record | Varies |
| **10** | **Schedule the annual review** -- set a calendar reminder for 12 months from deployment to review whether the risk tier is still correct and the model card is still accurate | S-20 | Calendar entry with model owner and 2nd line reviewer | 5 min |

### Total Estimated Effort: 1-2 working days

---

## 3. MVG Documentation Template

Use this template for the basic model card (item 3). Copy it into a markdown file named `model-card-[system-name].md` in the model's repository.

```markdown
# Model Card: [System Name]

## Overview
- **System name:** [Name]
- **Model owner:** [Name, role]
- **Risk tier:** [Minimal / Limited]
- **Date deployed:** [YYYY-MM-DD]
- **Next review date:** [YYYY-MM-DD, +12 months]

## Purpose
[2-3 sentences: What does this system do? What business problem does it solve?]

## Algorithm
- **Approach:** [e.g., gradient-boosted trees, neural network, LLM API call, rule-based with ML scoring]
- **Why this approach:** [1-2 sentences: Why not a simpler alternative?]
- **Third-party components:** [List any vendor AI/ML services used]

## Data
- **Input data:** [What data does the system consume?]
- **Training data:** [Brief description of training data source, size, date range -- or "N/A" for rule-based/API-based systems]
- **Personal data:** [Yes/No. If yes, what categories? Legal basis under GDPR?]

## Acceptance Criteria
| # | Metric | Threshold | Last Measured | Result | Pass? |
|---|--------|-----------|---------------|--------|-------|
| 1 | [e.g., Accuracy] | [e.g., > 95%] | [Date] | [Value] | [Y/N] |
| 2 | [e.g., Latency p99] | [e.g., < 200ms] | [Date] | [Value] | [Y/N] |
| 3 | [e.g., Error rate] | [e.g., < 0.1%] | [Date] | [Value] | [Y/N] |

## Known Limitations
[Bullet list: when should you NOT trust this system? What are its failure modes?
 What data does it handle poorly?]

## Fallback Procedure
- **If the system fails:** [What happens? Who is notified?]
- **Manual alternative:** [What process replaces the AI?]
- **Recovery:** [How is the system restored?]

## Logging
- **What is logged:** [Inputs, outputs, errors, latency]
- **Where logs are stored:** [System/location]
- **Retention period:** [Duration]

## Change History
| Date | Change | Changed By |
|------|--------|-----------|
| [Date] | Initial deployment | [Name] |
```

---

## 4. MVG Evaluation Strategy

For MVG, you need exactly 3 acceptance criteria. Choose them based on what matters most for this system.

### Recommended Metric Categories

| Category | Example Metrics | When to Use |
|----------|----------------|-------------|
| **Correctness** | Accuracy, precision, recall, F1, mean absolute error | Any prediction or classification system |
| **Reliability** | Error rate, uptime, p99 latency, timeout rate | Any production system |
| **Safety** | False positive rate, false negative rate, out-of-distribution detection rate | Any system where errors have consequences |

### Example: 3 Acceptance Criteria for an Internal Log Anomaly Detector

| # | Metric | Threshold | Rationale |
|---|--------|-----------|-----------|
| 1 | Precision (anomalies correctly identified / total flagged) | > 70% | Keeps alert fatigue manageable |
| 2 | Recall (anomalies detected / total actual anomalies) | > 85% | Catches most real issues |
| 3 | P99 latency | < 5 seconds | Does not block log pipeline |

### Example: 3 Acceptance Criteria for an Internal Forecasting Model

| # | Metric | Threshold | Rationale |
|---|--------|-----------|-----------|
| 1 | MAPE (Mean Absolute Percentage Error) | < 15% | Forecast is useful for capacity planning |
| 2 | Directional accuracy (correct trend direction) | > 80% | Planning decisions are directionally sound |
| 3 | Coverage (% of scenarios where model produces output) | > 99% | Model handles edge cases gracefully |

---

## 5. Review Cadence

### Minimal Risk: Annual Review

For minimal-risk AI systems, conduct one governance review per year. The review should take 1-2 hours and cover:

| Review Item | Check | Action if Fails |
|------------|-------|----------------|
| Is the risk tier still correct? | Has the system's scope, data, or impact changed? | Reclassify and upgrade governance if needed |
| Is the model card still accurate? | Do purpose, data, limitations sections reflect current state? | Update the model card |
| Do acceptance criteria still pass? | Re-run the 3 evaluations | Investigate; retrain or remediate |
| Is the fallback still viable? | Does the manual alternative still work with current volumes? | Update fallback procedure |
| Are logs being collected? | Spot-check log completeness and retention | Fix logging pipeline |
| Is the model owner still in role? | Has the person left or changed roles? | Reassign ownership |

### Limited Risk: Semi-Annual Review + 90-Day Upgrade Path

For limited-risk AI systems initially deployed under MVG:
- **At deployment:** Complete all 10 MVG items.
- **Within 90 days:** Upgrade to standard governance (22 items from [Risk Tiering Model](risk-tiering-model.md)).
- **Ongoing:** Semi-annual review.

---

## 6. When to Escalate to Full Governance

Upgrade from MVG to standard or full governance when any of these triggers occur:

| Trigger | Escalate To | Timeframe |
|---------|------------|-----------|
| System begins making or influencing customer-facing decisions | Standard (Limited) or Full (High) | Before going live to customers |
| System processes special category personal data (GDPR Art. 9) | At least Standard (Limited) | Immediately |
| Regulatory authority requests information about this system | At least Standard (Limited) | Within 30 days |
| Acceptance criteria fail at annual review | At least Standard (Limited) | Before resuming operation |
| System scope expands beyond original purpose | Reclassify using [decision tree](risk-tiering-model.md) | Before expanded use begins |
| Incident occurs involving this system | Reclassify using [decision tree](risk-tiering-model.md) | Within 2 weeks of incident |
| System output is used as input to a high-risk system | Reassess as potential component of high-risk system | Before integration |
| Multiple minimal-risk systems combined create material aggregate risk | Assess aggregate governance needs | At AI Governance Committee |

---

## 7. What MVG Does NOT Cover (and Why)

MVG intentionally omits the following. Understand what you are accepting:

| Omitted Item | Why Omitted in MVG | Risk Accepted |
|-------------|-------------------|---------------|
| Independent model validation (S-19) | Disproportionate for minimal-risk systems | Self-review risk; mitigated by annual review |
| Bias/fairness testing (F-03) | Not required for systems without customer impact | Undetected bias in internal tools; low impact |
| Continuous monitoring dashboards (T-17) | Overhead not justified for minimal risk | Slower detection of degradation; mitigated by logging |
| Human-in-the-loop design (A-06) | Not required for non-consequential systems | Automated decisions without human review; acceptable for internal tools |
| Customer transparency (T-06) | No customer interaction for minimal-risk | N/A for internal systems |
| FRIA (E-12) | Only required for high-risk | No fundamental rights assessment; acceptable for internal tools |
| Adversarial testing (S-06) | Disproportionate for minimal risk | Adversarial vulnerability; low incentive for internal tools |

---

## 8. MVG Implementation Checklist

Use this checklist when deploying a new minimal-risk AI system.

| # | Item | Done? | Date | Owner |
|---|------|-------|------|-------|
| 1 | System registered in AI inventory (S-01) | [ ] | | |
| 2 | Model owner assigned (A-05) | [ ] | | |
| 3 | Basic model card written (T-12) | [ ] | | |
| 4 | Algorithm choice documented (S-02) | [ ] | | |
| 5 | 3 acceptance criteria defined (S-03) | [ ] | | |
| 6 | Acceptance criteria evaluated and passing (S-03) | [ ] | | |
| 7 | Fallback procedure documented (S-13) | [ ] | | |
| 8 | Basic logging enabled (A-11) | [ ] | | |
| 9 | AI literacy training completed (K-09) | [ ] | | |
| 10 | Annual review date scheduled (S-20) | [ ] | | |
| -- | **Team lead sign-off** | [ ] | | |

---

## Cross-References

- **Risk Tiering Model:** [risk-tiering-model.md](risk-tiering-model.md) -- determines when MVG applies vs. standard or full governance
- **Adoption Playbook:** [adoption-playbook.md](adoption-playbook.md) -- MVG is the governance floor established in Month 3-4
- **Three Lines of Defense:** [../organizational-model/three-lines-of-defense-for-ai.md](../organizational-model/three-lines-of-defense-for-ai.md) -- MVG is primarily a 1st line responsibility with light 2nd line oversight
- **Governance in Agile Sprints:** [../process-integration/governance-in-agile-sprints.md](../process-integration/governance-in-agile-sprints.md) -- how MVG items fit into sprint workflows
- **SAFEST Checklist:** See the parent AIGovernance repository at `docs/06-licensing-preparation/safest-checklist-dnb-pre-application.md`

---

*Last updated: 2026-02-28*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
