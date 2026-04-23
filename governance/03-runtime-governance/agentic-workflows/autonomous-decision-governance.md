# Autonomous Decision Governance

## Purpose

This document governs how business AI agents make decisions autonomously -- defining what agents can decide alone, what requires human approval, and what is permanently outside agent authority. It provides a decision authority matrix, monetary limits, confidence thresholds, reversibility classifications, and regulatory constraints that together form the decision-making envelope for each agent.

Without explicit decision governance, agents either become bottlenecked (everything requires human approval) or ungoverned (agents make decisions humans would not approve). This document establishes the middle ground: structured autonomy within defined boundaries.

## When to Use

- When defining what decisions an agent is authorized to make
- When setting monetary limits for autonomous agent actions
- When classifying decisions by reversibility and risk
- When designing confidence thresholds for agent decision-making
- When mapping regulatory constraints to agent decision authority
- When reviewing agent decision patterns after incidents

## Who Is Responsible

| Role | R/A/C/I | Responsibility |
|------|---------|---------------|
| **Model Owner** | Accountable | Defines decision authority matrix for each agent |
| **Product Manager** | Consulted | Defines business requirements and customer experience for decision speed |
| **AI/ML Engineer** | Responsible | Implements confidence thresholds, decision validation, and audit logging |
| **Compliance Officer (2nd Line)** | Reviewer | Validates that decision authority respects regulatory constraints |
| **AI Governance Committee** | Approver | Approves decision authority for high-risk agents |
| **Legal Counsel** | Consulted | Advises on regulatory decision boundaries |

## Regulatory Basis

- **EU AI Act Article 14** -- Human oversight requirements for decisions made by high-risk AI
- **EU AI Act Article 9** -- Risk management for foreseeable risks of autonomous decision-making
- **GDPR Article 22** -- Right not to be subject to solely automated decisions with legal or significant effects
- **MiFID II Articles 24-25** -- Suitability and appropriateness requirements for investment decisions
- **PSD2** -- Strong customer authentication and payment authorization requirements
- **SAFEST A-01** (accountability), **A-06** (human-in-the-loop), **S-03** (acceptance criteria)
- **DNB Good Practice** -- Proportionate governance for automated decision-making in financial services

---

## 1. Decision Authority Matrix

### 1.1 Authority Levels

| Level | Name | Description | Human Involvement |
|-------|------|-------------|-------------------|
| **A1** | Full Autonomy | Agent decides and executes without any human involvement | None -- retrospective audit only |
| **A2** | Notify and Execute | Agent decides and executes, but notifies a human of the decision | Post-execution notification |
| **A3** | Decide and Confirm | Agent decides but requires human confirmation before execution | Pre-execution confirmation |
| **A4** | Recommend Only | Agent analyzes and recommends; human makes the final decision | Human is the decision-maker |
| **A5** | Prohibited | Agent must never make this decision; always escalate to human | Agent cannot participate in this decision |

### 1.2 Decision Authority Matrix for FinTech Agents

| Decision Type | Payments Agent | Customer Service Agent | KYC/Onboarding Agent | Treasury Agent | Fraud Detection Agent |
|--------------|---------------|----------------------|---------------------|---------------|----------------------|
| Answer FAQ | A1 | A1 | A1 | A1 | A1 |
| Provide account balance | A1 | A1 | N/A | A1 | A1 |
| Process payment < EUR 1,000 | A1 | N/A | N/A | A1 | N/A |
| Process payment EUR 1,000-10,000 | A2 | N/A | N/A | A2 | N/A |
| Process payment EUR 10,000-50,000 | A3 | N/A | N/A | A3 | N/A |
| Process payment > EUR 50,000 | A4 | N/A | N/A | A4 | N/A |
| Block suspicious transaction | A1 | N/A | N/A | N/A | A1 |
| Unblock flagged transaction | A4 | N/A | N/A | N/A | A4 |
| Approve standard KYC | N/A | N/A | A3 | N/A | N/A |
| Reject KYC application | N/A | N/A | A4 | N/A | N/A |
| Issue refund < EUR 50 | N/A | A2 | N/A | N/A | N/A |
| Issue refund EUR 50-500 | N/A | A3 | N/A | N/A | N/A |
| Issue refund > EUR 500 | N/A | A4 | N/A | N/A | N/A |
| Recommend investment | N/A | N/A | N/A | A4 | N/A |
| Execute trade < EUR 10,000 | N/A | N/A | N/A | A2 | N/A |
| Execute trade > EUR 10,000 | N/A | N/A | N/A | A3 | N/A |
| File SAR (Suspicious Activity Report) | A5 | A5 | A5 | A5 | A4 |
| Close customer account | A5 | A5 | A5 | A5 | A5 |
| Modify credit limit | A5 | A5 | A5 | A5 | A5 |
| Send marketing communication | A5 | A4 | A5 | A5 | A5 |

---

## 2. Decision Confidence Thresholds

### 2.1 Composite Confidence Scoring

This framework uses a composite confidence score that combines multiple signals for robust authority level assignment. See [Human-in-the-Loop Patterns](human-in-the-loop-patterns.md) Section 2 for the full confidence scoring methodology.

**Composite Formula:**
```
Confidence = (0.40 × Log Probability) + 
             (0.40 × Self-Assessment) + 
             (0.20 × Semantic Distance)
```

### 2.2 Confidence-Based Authority Routing

Agent decisions are routed to authority levels based on composite confidence scores:

| Confidence Band | Score Range | Authority Level | Execution Model |
|----------------|-------------|-----------------|-----------------|
| **Critical** | 0.00 - 0.50 | A4 | Recommend Only -- Human decides |
| **High** | 0.50 - 0.75 | A3 | Decide & Confirm -- Human approves first |
| **Medium** | 0.75 - 0.90 | A2 | Notify & Execute -- Agent acts, notifies after |
| **Low** | 0.90 - 1.00 | A1 | Full Autonomy -- Agent executes immediately |

### 2.3 Decision Category Thresholds

Minimum confidence thresholds vary by decision category:

| Decision Category | A1 Threshold | A2 Threshold | A3/A4 Action |
|-------------------|--------------|--------------|--------------|
| Informational response | 0.90 | 0.75 | Add hedging; cite source |
| Financial data retrieval | 0.95 | 0.90 | Escalate to human |
| Transaction processing | 0.99 | 0.95 | Require re-confirmation |
| Fraud determination (block) | 0.80 | 0.70 | Block & queue for review |
| Fraud determination (unblock) | N/A (always A4) | N/A | Always human decision |
| Identity verification | 0.92 | 0.85 | Escalate to KYC analyst |
| Risk scoring | 0.90 | 0.85 | Flag for human review |
| Regulatory filing | 0.95 | 0.90 | Legal review required |
| Customer communication | 0.85 | 0.75 | Draft review for sensitive |

### 2.4 Model Routing by Confidence Band

The governance pipeline can route requests to different models based on confidence requirements:

| Confidence Band | Model Selection | Rationale |
|-----------------|-----------------|-----------|
| Critical (A4) | Most capable model | Maximize accuracy for human-reviewed decisions |
| High (A3) | High-capability model | Reliable decisions with human oversight |
| Medium (A2) | Standard model | Balance cost and quality for autonomous execution |
| Low (A1) | Efficient model | Cost-optimized for high-confidence simple cases |

**Routing Configuration Example:**
```yaml
model_routing:
  critical_band:
    min_confidence: 0.00
    max_confidence: 0.50
    model: "gpt-4o"  # Most capable
    hitl_required: true
  
  high_band:
    min_confidence: 0.50
    max_confidence: 0.75
    model: "gpt-4o-mini"  # Capable but faster
    hitl_required: true
  
  medium_band:
    min_confidence: 0.75
    max_confidence: 0.90
    model: "gpt-4o-mini"
    hitl_required: false
    notification_required: true
  
  low_band:
    min_confidence: 0.90
    max_confidence: 1.00
    model: "gpt-4o-mini"  # Efficient
    hitl_required: false
```

### 2.5 Confidence Calibration

- **Quarterly Calibration:** Validate confidence scores against production decision outcomes
- **Calibration Metrics:**
  - Expected Calibration Error (ECE): Target < 0.05
  - Maximum Calibration Error (MCE): Target < 0.10
  - Brier Score: Track over time
- **Drift Detection:** Alert if calibration degrades > 10% from baseline
- **Remediation:** If calibration drifts, retrain confidence head or adjust thresholds

**Cross-Reference:** [Human-in-the-Loop Patterns](human-in-the-loop-patterns.md) Section 2 for confidence scoring details

---

## 3. Monetary Limits

### 3.1 Autonomous Transaction Limits

| Agent Type | Autonomous Limit (A1/A2) | Confirmation Required (A3) | Human Only (A4/A5) |
|-----------|-------------------------|---------------------------|-------------------|
| Payments Agent | < EUR 1,000 per transaction | EUR 1,000 - 50,000 | > EUR 50,000 |
| Customer Service Agent (refunds) | < EUR 50 per refund | EUR 50 - 500 | > EUR 500 |
| Treasury Agent (trades) | < EUR 10,000 per trade | EUR 10,000 - 100,000 | > EUR 100,000 |
| Treasury Agent (investments) | N/A (always A4) | N/A | All amounts |

### 3.2 Cumulative Limits

Individual transaction limits are insufficient. Cumulative limits prevent agents from circumventing per-transaction caps:

| Cumulative Limit | Threshold | Action |
|-----------------|-----------|--------|
| Daily transaction volume per agent | EUR 100,000 | Pause autonomous processing; require human review for remaining transactions |
| Hourly transaction count | 200 transactions | Alert Model Owner; investigate potential abuse or runaway loop |
| Per-customer daily total | EUR 25,000 | Require human confirmation for additional transactions |
| Single-session cumulative | EUR 15,000 | Escalate to human for session remainder |

### 3.3 Limit Review Process

- Monetary limits are reviewed quarterly by Model Owner + Compliance Officer
- Any request to increase limits requires AI Governance Committee approval
- Limit changes must be accompanied by updated eval test cases
- Temporary limit increases for specific events (e.g., holiday trading volume) require written approval with expiration date

---

## 4. Regulatory Decision Boundaries

### 4.1 Decisions Agents Must Never Make Alone

The following decisions must always involve a human, regardless of agent confidence or monetary amount:

| Decision | Regulatory Basis | Required Human Role |
|----------|-----------------|-------------------|
| Deny a credit application | GDPR Art. 22 (automated decisions with significant effects) | Licensed credit officer |
| Restrict or close a customer account | Consumer protection; duty of care | Senior operations officer |
| File a Suspicious Activity Report | AML regulations; MLRO responsibility | Money Laundering Reporting Officer |
| Determine regulatory reporting obligation | Various financial regulations | Compliance officer |
| Provide personalized investment advice | MiFID II suitability requirements | Licensed investment advisor |
| Make a PEP (Politically Exposed Person) determination | AML regulations | Senior compliance analyst |
| Deny a complaint or compensation claim | Consumer protection; regulatory complaints handling | Complaints officer |
| Issue a binding contractual commitment | Contract law | Authorized signatory |

### 4.2 Decisions Agents May Assist With

For the decisions above, agents may still provide valuable assistance:

| Agent Contribution | Human Responsibility |
|-------------------|---------------------|
| Gather and organize relevant data | Verify data completeness and accuracy |
| Apply scoring models and present results | Interpret scores in context |
| Draft a recommendation with reasoning | Review, modify, and make the final decision |
| Identify relevant regulations and requirements | Apply professional judgment |
| Prepare documentation and reports | Review, sign, and submit |

---

## 5. Decision Reversibility Classification

### 5.1 Reversibility Categories

| Category | Definition | Examples | Governance Implication |
|----------|-----------|----------|----------------------|
| **Fully Reversible** | Action can be completely undone with no lasting effect | Displaying information, providing a recommendation, internal classification | Lower oversight required; A1 or A2 authority |
| **Partially Reversible** | Action can be reversed but with some residual impact | Payment that can be recalled (within timeframe), refund, account settings change | Moderate oversight; A2 or A3 authority |
| **Difficult to Reverse** | Action can technically be reversed but with significant effort or impact | Completed cross-border payment, published communication | Higher oversight; A3 or A4 authority |
| **Irreversible** | Action cannot be reversed | Filed regulatory report, deleted data, closed account, external notification sent | Maximum oversight; A4 or A5 authority |

### 5.2 Reversibility Impact on Oversight Model

```
Decision reversibility classification
  |
  v
Fully Reversible --> Minimum oversight: HOTA + A1/A2 authority
  |
Partially Reversible --> Standard oversight: HOTL + A2/A3 authority
  |
Difficult to Reverse --> Elevated oversight: HOTL + A3/A4 authority
  |
Irreversible --> Maximum oversight: HITL + A4/A5 authority
```

---

## 6. Decision Audit Requirements

### 6.1 Audit Fields per Decision

Every autonomous agent decision must be logged with:

| Field | Description | Retention |
|-------|-------------|-----------|
| `decision_id` | Unique identifier for this decision | Per retention policy |
| `chain_id` | Link to delegation chain (if applicable) | Same as chain |
| `agent_id` | Which agent made the decision | Per retention policy |
| `decision_type` | Classification of the decision | Per retention policy |
| `authority_level` | A1-A5 classification applied | Per retention policy |
| `confidence_score` | Agent's confidence in the decision | Per retention policy |
| `inputs_summary` | Key inputs used (not raw PII) | Per retention policy |
| `reasoning_trace` | Agent's reasoning chain (LLM trace) | 1 year full / 5 years summary |
| `outcome` | The decision made | Per retention policy |
| `reversibility` | Reversibility classification | Per retention policy |
| `monetary_impact` | Financial impact if applicable | Per retention policy |
| `human_involvement` | Who reviewed/approved, if any | Per retention policy |
| `regulatory_classification` | Which regulations apply | Per retention policy |

### 6.2 Decision Audit Triggers

| Trigger | Audit Intensity |
|---------|----------------|
| A1 decision (full autonomy) | Standard logging; included in periodic HOTA audit sample |
| A2 decision (notify and execute) | Standard logging + notification record |
| A3 decision (decide and confirm) | Full logging + human confirmation record + reasoning trace |
| A4 decision (recommend only) | Full logging + recommendation + human decision + comparison of recommendation vs. outcome |
| Decision reversed by human | Full investigation logging; flag for pattern analysis |
| Decision appealed by customer | Full logging; retain for complaint resolution |

---

## 7. FinTech Decision Examples

### 7.1 Payment Approval Decision Flow

```
Customer requests payment of EUR 5,000 to a known beneficiary
  |
  v
Payments Agent evaluates:
  - Amount: EUR 5,000 (within A2 range: EUR 1,000-10,000)
  - Beneficiary: known, previously verified
  - Customer balance: sufficient
  - Fraud score: 0.03 (low risk)
  - Confidence: 0.97
  |
  v
Authority check: A2 (Notify and Execute)
  - Execute payment
  - Notify human operator of transaction
  - Log decision with full audit trail
```

### 7.2 Fraud Blocking Decision Flow

```
Transaction flagged by fraud model: EUR 2,500 to new international beneficiary
  |
  v
Fraud Detection Agent evaluates:
  - Fraud score: 0.82 (above blocking threshold of 0.80)
  - Pattern: unusual geography for this customer
  - Time: outside customer's typical transaction hours
  - Confidence in fraud determination: 0.85
  |
  v
Authority check: A1 (Full Autonomy for blocking)
  - Block transaction immediately
  - Notify customer of hold
  - Queue for human review (unblocking is A4)
  - Log decision with reasoning trace
```

### 7.3 Investment Recommendation Decision Flow

```
Customer asks Treasury Agent: "Should I invest in European bonds?"
  |
  v
Treasury Agent evaluates:
  - Decision type: Investment recommendation
  - Authority level: A4 (Recommend Only -- always requires human for investment advice)
  - Regulatory constraint: MiFID II suitability assessment required
  |
  v
Agent response:
  "I can share general information about European bonds, but for personalized
   investment advice tailored to your situation, I need to connect you with
   a licensed investment advisor. General information: [factual data only].
   Disclaimer: This is general information, not personal financial advice."
  |
  v
Log: decision_type=investment_query, authority=A4, action=provided_general_info,
     escalation=offered_human_advisor
```

---

## 8. Decision Governance Review

### 8.1 Quarterly Review Checklist

| Review Item | Reviewer | Evidence |
|-------------|----------|---------|
| Decision authority matrix is current and complete | Model Owner | Matrix document with last review date |
| Monetary limits are appropriate for current business volumes | Model Owner + Compliance | Transaction data analysis |
| Confidence thresholds are well-calibrated | AI/ML Engineer | Calibration report |
| A4/A5 decisions are being escalated correctly | Compliance Officer | Audit log analysis |
| Human override rate on A3 decisions is acceptable | Model Owner | Override rate report (target: < 5%) |
| No unauthorized A1/A2 decisions occurred | Internal Audit (3rd Line) | Permission violation report |
| Regulatory decision boundaries are respected | Compliance Officer | Compliance review report |

---

## Cross-References

- **Human-in-the-Loop Patterns:** [human-in-the-loop-patterns.md](human-in-the-loop-patterns.md) -- oversight models that map to authority levels
- **Agent Permission Boundaries:** [agent-permission-boundaries.md](agent-permission-boundaries.md) -- tool-level permissions that constrain decision authority
- **Delegation Chain Audit:** [delegation-chain-audit.md](delegation-chain-audit.md) -- audit trail for decisions made within delegation chains
- **Agent Fleet Operations:** [agent-fleet-operations.md](agent-fleet-operations.md) -- KPI tracking for decision quality metrics
- **Customer-Facing Agent Safety:** [customer-facing-agent-safety.md](customer-facing-agent-safety.md) -- safety guardrails for customer-impacting decisions
- **Multi-Agent Governance Framework:** [multi-agent-governance-framework.md](multi-agent-governance-framework.md) -- delegation rules and accountability model
- **Agent Performance Evaluations:** [../evaluations/agent-performance-evals.md](../evaluations/agent-performance-evals.md) -- confidence calibration and decision quality evaluation
- **Risk Tiering Model:** [../../07-enterprise-implementation/risk-based-adoption/risk-tiering-model.md](../../07-enterprise-implementation/risk-based-adoption/risk-tiering-model.md) -- risk tier determines default authority levels

---

*Last updated: 2026-03-01*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
