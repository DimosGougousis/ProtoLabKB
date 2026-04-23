# Human-in-the-Loop Patterns

## Purpose

This document defines three oversight models for governing business AI agents based on risk, action type, and reversibility: Human-in-the-Loop (HITL), Human-on-the-Loop (HOTL), and Human-out-of-the-Loop (HOTA). It provides a structured decision framework for selecting the appropriate oversight model per agent, per action, and per context -- ensuring that high-risk autonomous decisions always have proportionate human oversight while low-risk informational tasks are not unnecessarily bottlenecked.

This is the foundational human oversight document for the governance framework. Every agent registered in the fleet must be assigned one of these three oversight models, and the model must be enforced at runtime.

## When to Use

- When designing a new AI agent and determining its oversight requirements
- When registering an agent in the fleet registry (selecting the `oversight_model` field)
- When an agent's risk tier changes and the oversight model must be re-evaluated
- When defining escalation paths and human response SLAs for an agent
- When auditing whether an agent's oversight model is appropriate for its actual behavior
- When planning staffing for human review queues

## Who Is Responsible

| Role | R/A/C/I | Responsibility |
|------|---------|---------------|
| **Model Owner** | Accountable | Selects the oversight model for each agent; approves changes |
| **AI/ML Engineer** | Responsible | Implements oversight enforcement in agent runtime |
| **Product Manager** | Consulted | Defines latency requirements and user experience implications |
| **Compliance Officer (2nd Line)** | Reviewer | Validates that oversight model meets regulatory requirements |
| **Customer Operations Lead** | Informed | Staffs human review queues; manages response SLAs |
| **AI Governance Committee** | Approver | Approves oversight model for high-risk agents |

## Regulatory Basis

- **EU AI Act Article 14** -- Human oversight measures for high-risk AI systems, including ability to understand, monitor, intervene, and interrupt
- **EU AI Act Article 14(4)** -- Oversight measures must be commensurate with the risks, level of autonomy, and context of use
- **GDPR Article 22** -- Right not to be subject to solely automated decision-making with legal or significant effects
- **DORA Article 9** -- ICT risk management framework, including human decision-making in critical processes
- **SAFEST A-06** (human-in-the-loop controls), **A-07** (override capability), **A-09** (kill switch mechanisms)
- **DNB Good Practice** -- Proportionate human oversight for automated decision-making in financial services

---

## 1. Three Oversight Models Defined

### 1.1 HITL -- Human-in-the-Loop

**Definition:** The human approves every consequential action before the agent executes it. The agent prepares, recommends, and presents; the human decides and authorizes.

| Aspect | Specification |
|--------|--------------|
| **Agent role** | Preparer and recommender |
| **Human role** | Decision-maker and authorizer |
| **Execution flow** | Agent analyzes, drafts, recommends. Human reviews, approves/modifies/rejects. Agent executes only after explicit approval. |
| **Latency impact** | High -- every consequential action waits for human response |
| **Staffing requirement** | Dedicated human reviewers with domain expertise and defined response SLAs |
| **Applicable risk tier** | High-risk agents; agents with irreversible actions; agents making adverse decisions |
| **EU AI Act alignment** | Fully satisfies Article 14; agent never acts autonomously on consequential decisions |
| **GDPR Article 22** | Fully compliant -- human is in the decision loop |

**FinTech Examples:**
- Credit decision agent: agent scores the application and recommends approve/deny; human credit officer reviews and makes the final decision
- Large payment agent: agent prepares payment > EUR 50,000; human treasury officer authorizes
- Account closure agent: agent processes the request and prepares the closure; human operations officer executes
- Suspicious Activity Report (SAR) agent: agent identifies suspicious patterns and drafts the report; human compliance officer reviews, edits, and submits

### 1.2 HOTL -- Human-on-the-Loop

**Definition:** The agent acts autonomously within defined boundaries. A human monitors agent actions in near-real-time and can intervene, override, or halt operations when anomalies are detected.

| Aspect | Specification |
|--------|--------------|
| **Agent role** | Autonomous executor within boundaries |
| **Human role** | Monitor, supervisor, and intervener |
| **Execution flow** | Agent acts autonomously. All actions are logged and streamed to a monitoring dashboard. Human reviews a sample or is alerted on anomalies. Human can override or halt at any time. |
| **Latency impact** | Low -- agent acts immediately; human intervenes only when needed |
| **Staffing requirement** | Monitoring staff with alert-based workflow; does not require per-action review |
| **Applicable risk tier** | Medium-risk agents; agents with reversible actions within monetary limits |
| **EU AI Act alignment** | Satisfies Article 14 when monitoring is active and intervention capability is real-time |
| **GDPR Article 22** | Compliant when meaningful human intervention is available before adverse effects materialize |

**FinTech Examples:**
- Payment processing agent: autonomously processes payments up to EUR 10,000; human monitors transaction stream and can halt suspicious patterns
- Customer service chatbot: autonomously handles inquiries; human reviews flagged conversations and can intervene in real-time
- KYC/Onboarding orchestrator: autonomously processes standard applications; human reviews flagged applications and edge cases
- Fraud detection agent: autonomously blocks clearly fraudulent transactions; human reviews borderline cases within 15 minutes

### 1.3 HOTA -- Human-out-of-the-Loop (Audit)

**Definition:** The agent operates fully autonomously. A human audits agent behavior retrospectively through logs, metrics, and periodic reviews. No real-time human oversight is applied.

| Aspect | Specification |
|--------|--------------|
| **Agent role** | Fully autonomous executor |
| **Human role** | Retrospective auditor and evaluator |
| **Execution flow** | Agent acts autonomously. All actions are logged. Human reviews audit logs periodically (daily/weekly). Performance evaluated through KPIs and eval suites. |
| **Latency impact** | None -- agent operates without human delay |
| **Staffing requirement** | Periodic audit staff; no real-time monitoring needed |
| **Applicable risk tier** | Low-risk / minimal-risk agents; informational agents; advisory agents with disclaimers |
| **EU AI Act alignment** | Appropriate for minimal/limited-risk systems where real-time oversight is disproportionate |
| **GDPR Article 22** | Compliant only when the agent does not make decisions with legal or significant effects |

**FinTech Examples:**
- FAQ chatbot: answers general product questions; human reviews sample conversations weekly
- Cash flow insights agent: provides spending analysis and forecasts with disclaimers; human audits recommendation quality monthly
- Balance inquiry agent: retrieves and displays account balances; human audits access logs periodically
- Document retrieval agent: finds and presents policy documents; human reviews retrieval accuracy quarterly

---

## 2. HITL Confidence Scoring

This section defines the composite confidence scoring formula for determining when human oversight is required. The confidence score combines three signals to produce a robust measure of agent certainty.

### 2.1 Composite Confidence Formula

```
Composite Confidence = (0.40 × Log Probability) + 
                       (0.40 × Self-Assessment) + 
                       (0.20 × Semantic Distance)
```

| Component | Weight | Description | Measurement |
|-----------|--------|-------------|-------------|
| **Log Probability** | 40% | Model's token-level probability | Average log-prob of generated tokens |
| **Self-Assessment** | 40% | Model's explicit confidence rating | Direct query: "Rate your confidence 0-1" |
| **Semantic Distance** | 20% | Distance from known good responses | Embedding similarity to verified answers |

### 2.2 Confidence Threshold Bands

The composite score maps to four threshold bands, each triggering different authority levels:

| Band | Score Range | Authority Level | Human Involvement |
|------|-------------|-----------------|-------------------|
| **Critical** | 0.00 - 0.50 | A4 | Recommend Only -- Human makes all decisions |
| **High** | 0.50 - 0.75 | A3 | Decide and Confirm -- Human confirms before execution |
| **Medium** | 0.75 - 0.90 | A2 | Notify and Execute -- Agent executes, notifies human after |
| **Low** | 0.90 - 1.00 | A1 | Full Autonomy -- Agent executes without human involvement |

### 2.3 Authority Level Definitions

| Level | Name | Trigger Condition | Execution Flow |
|-------|------|-------------------|----------------|
| **A1** | Full Autonomy | Confidence ≥ 0.90 | Agent executes immediately; logged for audit |
| **A2** | Notify & Execute | 0.75 ≤ Confidence < 0.90 | Agent executes, human notified within 15 min |
| **A3** | Decide & Confirm | 0.50 ≤ Confidence < 0.75 | Human must approve before execution |
| **A4** | Recommend Only | Confidence < 0.50 | Agent provides analysis; human decides |

### 2.4 Calibration Requirements

- **Quarterly Calibration:** Confidence thresholds must be validated against production decisions
- **False Positive Rate:** Target < 5% of high-confidence decisions should be wrong
- **False Negative Rate:** Target < 10% of low-confidence decisions should be correct
- **Threshold Adjustment:** If calibration drifts, adjust thresholds before retraining model

### 2.5 Integration with HITL/HOTL/HOTA

| Oversight Model | Authority Levels Used | Typical Confidence Range |
|-----------------|----------------------|-------------------------|
| **HITL** | A3-A4 (Confirm or Recommend) | 0.00 - 0.75 |
| **HOTL** | A1-A3 (All except full autonomy) | 0.00 - 0.90 |
| **HOTA** | A1-A2 (Autonomy or Notify) | 0.75 - 1.00 |

**Cross-Reference:** [Autonomous Decision Governance](autonomous-decision-governance.md) for authority level implementation.

---

## 3. Oversight Model Selection Decision Tree

Use this decision tree to select the appropriate oversight model for an agent or action.

```
START: Evaluate the agent action
  |
  v
Q1: Does this action produce legal effects or significantly affect a natural person?
    (e.g., credit denial, account closure, regulatory filing, adverse decision)
  |
  +-- YES --> HITL (mandatory under GDPR Article 22)
  |
  +-- NO
       |
       v
Q2: Is this action irreversible or difficult to reverse?
    (e.g., funds transferred externally, data deleted, report filed)
  |
  +-- YES --> HITL
  |
  +-- NO
       |
       v
Q3: Does this action involve financial impact above the agent's autonomous threshold?
    (See autonomous-decision-governance.md for monetary limits)
  |
  +-- YES --> HITL for amount above threshold; HOTL within threshold
  |
  +-- NO
       |
       v
Q4: Does this action involve customer-facing communication with regulatory implications?
    (e.g., investment recommendations, product suitability, complaint responses)
  |
  +-- YES --> HOTL (human monitors; can intervene before delivery)
  |
  +-- NO
       |
       v
Q5: Is this agent classified as high-risk under the EU AI Act or internal risk tiering?
  |
  +-- YES --> HOTL minimum; HITL for actions listed in the permission boundary
  |
  +-- NO
       |
       v
Q6: Does this action modify system state or customer records?
  |
  +-- YES --> HOTL (human monitors state changes)
  |
  +-- NO
       |
       v
Q7: Is this a read-only, informational, or purely advisory action with disclaimers?
  |
  +-- YES --> HOTA (retrospective audit is sufficient)
  |
  +-- NO --> Default to HOTL (when in doubt, monitor)
```

### 2.1 Override Rules

The decision tree provides a default recommendation. The following overrides apply:

| Override Condition | Effect |
|-------------------|--------|
| Regulatory requirement mandates human approval | Escalate to HITL regardless of decision tree |
| Agent has history of safety incidents | Escalate one level (HOTA to HOTL, HOTL to HITL) until root cause resolved |
| Agent is newly deployed (< 30 days in production) | Start at HOTL minimum; graduate to HOTA only after evaluation period |
| Agent operates in a new market or jurisdiction | Start at HITL until regulatory requirements confirmed |
| Agent confidence score drops below threshold | Temporarily escalate to HITL for low-confidence actions |

---

## 3. Override Mechanisms

### 3.1 Human Override Capabilities

Every agent, regardless of oversight model, must support the following override mechanisms:

| Override | Description | Who Can Trigger | Response Time |
|----------|-------------|----------------|---------------|
| **Pause** | Temporarily halt agent from taking new actions; complete current action | Model Owner, Fleet Ops Lead, On-Call Engineer | < 1 minute |
| **Kill Switch** | Immediately halt all agent activity; drop in-flight actions | On-Call Engineer (pre-authorized), Fleet Ops Lead | < 30 seconds |
| **Override Decision** | Reverse or modify a specific agent decision | Human Reviewer (HITL/HOTL), Model Owner | Per SLA (see 3.2) |
| **Downgrade Autonomy** | Move agent from HOTA to HOTL, or HOTL to HITL | Model Owner, Compliance Officer | < 15 minutes |
| **Upgrade Autonomy** | Move agent from HITL to HOTL, or HOTL to HOTA | Model Owner + Governance Committee approval | Requires formal review |

### 3.2 Override Audit Requirements

Every override action must be logged with:
- Override type (pause, kill, override decision, downgrade, upgrade)
- Who triggered it and their role
- Reason for override
- Timestamp and duration
- Impact on in-flight interactions (customers affected)
- Resolution and follow-up actions

---

## 4. Human Response SLAs

Human oversight is only meaningful if humans respond within defined timeframes. Without SLAs, HITL becomes a bottleneck and HOTL becomes performative monitoring.

### 4.1 HITL Response SLAs

| Action Category | Response SLA | Escalation if Missed |
|----------------|-------------|---------------------|
| Payment authorization (> EUR 50K) | < 15 minutes during business hours; < 60 minutes outside | Auto-escalate to senior treasury + notify Model Owner |
| Credit decision review | < 30 minutes | Auto-escalate to senior credit officer + queue priority boost |
| Account closure approval | < 2 hours | Auto-escalate to operations manager |
| SAR review and submission | < 4 hours | Auto-escalate to MLRO (Money Laundering Reporting Officer) |
| Customer complaint resolution | < 1 hour | Auto-escalate to complaints team lead |

### 4.2 HOTL Intervention SLAs

| Alert Category | Intervention SLA | Escalation if Missed |
|---------------|-----------------|---------------------|
| Safety violation alert | < 5 minutes | Auto-kill-switch + incident declared |
| Anomaly detected (financial) | < 15 minutes | Auto-pause agent + notify Fleet Ops Lead |
| Customer escalation request | < 10 minutes | Auto-route to next available human agent |
| Boundary violation alert | < 5 minutes | Auto-pause agent + security incident declared |
| Performance degradation alert | < 30 minutes | Monitor; auto-escalate if degradation persists |

### 4.3 HOTA Audit Cadence

| Agent Risk Tier | Audit Frequency | Audit Scope |
|----------------|----------------|-------------|
| Minimal risk | Monthly | Random sample of 2% of interactions |
| Limited risk | Weekly | Random sample of 5% of interactions + all flagged interactions |
| High risk (temporary HOTA) | Daily | Random sample of 10% + all flagged + all edge cases |

---

## 5. Escalation Paths

### 5.1 Escalation from HOTA to HOTL

```
HOTA agent detects situation outside its autonomous scope
  |
  v
Agent flags the interaction for real-time human monitoring
  |
  v
Alert sent to monitoring team with context:
  - Interaction transcript so far
  - Reason for escalation (confidence drop, topic boundary, customer signal)
  - Recommended action
  |
  v
Human monitor reviews and decides:
  +-- Continue monitoring (HOTL mode for this interaction)
  +-- Intervene (take over the interaction)
  +-- Escalate further to HITL (human takes full control)
```

### 5.2 Escalation from HOTL to HITL

```
HOTL monitoring detects a situation requiring explicit approval
  |
  v
Agent pauses the current action and queues for approval
  |
  v
Approval request sent to designated reviewer:
  - Action the agent wants to take
  - Evidence and reasoning
  - Confidence level
  - Risk assessment
  - Time sensitivity
  |
  v
Reviewer decides:
  +-- Approve --> Agent executes the action
  +-- Modify --> Agent executes the modified action
  +-- Reject --> Agent informs customer of alternative path
  +-- Escalate --> Route to senior reviewer or specialist
```

### 5.3 Escalation Timeout Handling

| Scenario | Action |
|----------|--------|
| HITL reviewer does not respond within SLA | Auto-escalate to backup reviewer; extend SLA by 50% |
| Backup reviewer does not respond | Auto-escalate to Model Owner; consider agent pause |
| No reviewer available (system failure) | Agent enters safe fallback mode (see [fallback-procedure.md](../templates/fallback-procedure.md)); inform customer of delay |
| HOTL monitor not responding to alerts | Alert Fleet Ops Lead; increase alert severity; consider auto-pause |

---

## 6. Oversight Model Governance

### 6.1 Oversight Model Assignment Process

| Step | Activity | Responsible |
|------|----------|-------------|
| 1 | Complete risk classification for the agent | Model Owner + Risk team |
| 2 | Apply the decision tree (Section 2) for each action type | AI/ML Engineer + Model Owner |
| 3 | Document the selected oversight model with justification | Model Owner |
| 4 | Review by 2nd Line Compliance (for high-risk agents) | Compliance Officer |
| 5 | Approve by AI Governance Committee (for high-risk agents) | Governance Committee |
| 6 | Register in agent registry with `oversight_model` field | MLOps Engineer |
| 7 | Implement enforcement in agent runtime | AI/ML Engineer |
| 8 | Test override mechanisms (pause, kill switch, downgrade) | QA + MLOps |

### 6.2 Oversight Model Review Triggers

The oversight model must be re-evaluated when:

| Trigger | Action |
|---------|--------|
| Agent risk tier changes | Re-run decision tree; update oversight model if needed |
| New capabilities added to the agent | Evaluate new actions against decision tree |
| Safety incident occurs | Temporarily escalate oversight level; review after root cause analysis |
| Agent graduates from shadow mode to production | Confirm oversight model is appropriate |
| Regulatory requirements change | Re-evaluate against new requirements |
| Agent performance consistently exceeds HITL thresholds | Consider graduating from HITL to HOTL (requires formal review) |
| Agent handles new customer segments or markets | Re-evaluate for new risk profile |

### 6.3 Oversight Graduation Process

Moving an agent to a less restrictive oversight model (HITL to HOTL, or HOTL to HOTA) requires formal evidence:

| Requirement | Evidence |
|-------------|---------|
| Performance stability | 90+ days of consistent KPI compliance within SLA |
| Safety record | Zero safety incidents in the evaluation period |
| Eval suite coverage | All eval dimensions passing at target thresholds |
| Human override rate | HITL rejection rate < 2% sustained over 60 days |
| Compliance sign-off | 2nd Line review and approval |
| Governance approval | AI Governance Committee sign-off for high-risk agents |

---

## 7. Observability Integration

### 7.1 Oversight Observability Requirements

All oversight events must be observable through the governance observability stack:

| Event | Observability Requirement | Tool Integration |
|-------|--------------------------|-----------------|
| Agent action requiring HITL approval | Trace span: `oversight.hitl.approval_requested` | LangSmith / Langfuse |
| Human approval/rejection decision | Trace span: `oversight.hitl.decision` with reviewer identity | LangSmith / Langfuse |
| HOTL alert triggered | Trace span: `oversight.hotl.alert` with alert type and severity | Arize Phoenix / Opik |
| Human intervention in HOTL | Trace span: `oversight.hotl.intervention` with action taken | LangSmith / Langfuse |
| HOTA audit review completed | Audit event: `oversight.hota.audit_completed` with findings | Governance audit log |
| Override triggered | Trace span: `oversight.override` with type and reason | All platforms + incident log |
| Escalation timeout | Alert: `oversight.escalation.timeout` with affected interaction | Alerting system |

### 7.2 Dashboard Metrics

The following metrics must be available on the Agent Fleet Command Dashboard (see [agent-fleet-operations.md](agent-fleet-operations.md)):

| Metric | Description | Target |
|--------|-------------|--------|
| HITL approval latency (P50, P95) | Time from approval request to human decision | P95 < SLA per category |
| HITL rejection rate | Percentage of agent recommendations rejected by human | < 5% (indicates good agent judgment) |
| HOTL alert-to-intervention time | Time from alert to human action | P95 < 15 minutes |
| HOTL false positive rate | Percentage of alerts that required no intervention | < 30% (too many = alert fatigue) |
| HOTA audit finding rate | Percentage of audited interactions with findings | < 3% (indicates stable agent) |
| Override frequency | Number of overrides per day/week | Trending down over time |
| Escalation timeout rate | Percentage of escalations that missed SLA | < 2% |

---

## 8. Mapping to Three Lines of Defense

| Line | Oversight Responsibility |
|------|------------------------|
| **1st Line (Product / Engineering)** | Implement oversight enforcement; staff HITL review queues; monitor HOTL dashboards; conduct HOTA audits |
| **2nd Line (Risk / Compliance)** | Validate oversight model selection; review override patterns; audit escalation effectiveness; approve model graduation |
| **3rd Line (Internal Audit)** | Independently test oversight mechanisms; verify that HITL approvals are genuine; audit HOTA sample coverage and quality |

---

## Cross-References

- **Agent Fleet Operations:** [agent-fleet-operations.md](agent-fleet-operations.md) -- dashboard integration and oversight model registration
- **Agent Permission Boundaries:** [agent-permission-boundaries.md](agent-permission-boundaries.md) -- permission boundaries that determine which actions require HITL
- **Multi-Agent Governance Framework:** [multi-agent-governance-framework.md](multi-agent-governance-framework.md) -- delegation chain governance and human decision points
- **Customer-Facing Agent Safety:** [customer-facing-agent-safety.md](customer-facing-agent-safety.md) -- escalation triggers that interact with oversight models
- **Autonomous Decision Governance:** [autonomous-decision-governance.md](autonomous-decision-governance.md) -- decision authority matrix that maps to oversight models
- **Fallback Procedure Template:** [../templates/fallback-procedure.md](../templates/fallback-procedure.md) -- degradation procedures when human oversight is unavailable
- **Agent Performance Evaluations:** [../evaluations/agent-performance-evals.md](../evaluations/agent-performance-evals.md) -- metrics for evaluating oversight effectiveness
- **Risk Tiering Model:** [../../07-enterprise-implementation/risk-based-adoption/risk-tiering-model.md](../../07-enterprise-implementation/risk-based-adoption/risk-tiering-model.md) -- risk tier drives default oversight model
- **Three Lines of Defense:** [../../07-enterprise-implementation/organizational-model/three-lines-of-defense-for-ai.md](../../07-enterprise-implementation/organizational-model/three-lines-of-defense-for-ai.md) -- organizational accountability for oversight

---

*Last updated: 2026-03-01*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
