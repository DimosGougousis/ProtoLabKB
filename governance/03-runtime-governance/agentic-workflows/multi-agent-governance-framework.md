# Multi-Agent Governance Framework

## Purpose

This document defines the governance framework for business AI agent systems -- from single customer-facing agents to complex multi-agent orchestration architectures. It addresses the unique governance challenges that emerge when AI systems act autonomously: making decisions, taking actions, delegating to sub-agents, and interacting with customers in ways that are difficult to fully predict during development.

This is the **key differentiator** of this governance framework. Traditional AI governance treats models as static prediction engines. Agentic AI governance must address autonomy, unpredictability, compound errors, delegation chains, and accountability gaps that do not exist in traditional ML systems.

## When to Use

- When designing any AI system that can take actions (not just predict)
- When deploying customer-facing AI agents (chatbots, advisors, service agents)
- When building multi-agent architectures (orchestrator + sub-agents)
- When defining permission boundaries for agent tool use
- When establishing human-in-the-loop policies for autonomous decisions
- When auditing or reviewing an existing agent system's governance posture

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **Product Manager** | **Accountable** -- defines the agent's purpose, scope, and customer-facing behavior boundaries |
| **AI/ML Engineer** | **Responsible** -- implements permission boundaries, delegation protocols, audit logging, and safety mechanisms |
| **Model Owner** | **Accountable** -- owns the agent's production behavior and governance compliance |
| **Compliance Officer (2nd Line)** | **Reviewer** -- validates that agent governance meets regulatory requirements, especially for autonomous decisions |
| **AI Governance Committee** | **Approver** -- approves permission boundaries and human-in-the-loop policies for limited/high-risk agents |

## Regulatory Basis

- **EU AI Act Article 14** -- Human oversight of AI systems, including ability to interrupt
- **EU AI Act Article 9** -- Risk management for foreseeable misuse and unintended behaviors
- **EU AI Act Article 50** -- Transparency obligations for AI systems interacting with natural persons
- **GDPR Article 22** -- Right not to be subject to solely automated decision-making with legal or significant effects
- **SAFEST items A-06** (human-in-the-loop), **A-07** (override capability), **A-09** (kill switch), **A-11** (audit trail), **T-06** (customer disclosure), **T-07** (decision explanation)
- **DNB Good Practice** -- Explainability and human oversight expectations for AI in financial services

---

## 1. Types of Business AI Agents

Understanding what type of agent you are governing is the first step. Different agent types carry different governance requirements.

| Agent Type | Description | Autonomy Level | FinTech Examples | Governance Intensity |
|-----------|-------------|---------------|-----------------|---------------------|
| **Informational** | Retrieves and presents information; does not take actions | Low | FAQ chatbot, balance inquiry bot, product information agent | Standard (limited risk) |
| **Advisory** | Analyzes data and provides recommendations; human decides | Medium | Spending insights agent, investment idea generator, credit improvement advisor | Standard to intensive |
| **Decision-Making** | Makes decisions that affect customers or operations | High | Fraud decisioning agent, credit scoring agent, claims processing agent | Intensive (high risk) |
| **Autonomous Actor** | Takes actions on behalf of the customer or organization | Very High | Payment execution agent, account modification agent, automated trading agent | Maximum (high risk) |
| **Orchestrator** | Coordinates multiple sub-agents to accomplish complex tasks | Very High | Customer onboarding orchestrator, complaint resolution orchestrator | Maximum (high risk) |

### Governance Implication

As autonomy increases, governance requirements increase proportionally:

- **Informational agents** need transparency (disclosure) and accuracy (grounding).
- **Advisory agents** need the above plus fairness (unbiased recommendations) and clear disclaimers.
- **Decision-making agents** need the above plus human oversight, audit trails, and explanation mechanisms.
- **Autonomous actors** need the above plus permission boundaries, rollback capabilities, and real-time monitoring.
- **Orchestrators** need the above for every sub-agent they coordinate, plus delegation chain governance.

---

## 2. Governance Challenges Unique to Agents

| Challenge | Description | Why Traditional AI Governance Does Not Address It |
|-----------|-------------|--------------------------------------------------|
| **Autonomy** | Agents act without human approval for each action. The governance challenge is defining which actions require approval and which do not. | Traditional governance assumes a human makes the final decision based on the model's output. |
| **Unpredictability** | LLM-based agents can produce novel, unexpected behaviors that were not tested during development. | Traditional models have a fixed output space; agents can compose novel action sequences. |
| **Compound Errors** | In multi-step workflows, a small error in step 1 cascades through steps 2-5, producing a large error at the end. | Traditional governance evaluates single predictions; compound error propagation is not addressed. |
| **Delegation** | When Agent A delegates to Agent B, who is accountable for Agent B's actions? Can Agent B expand its own permissions? | Traditional governance has one model, one owner. Delegation chains create accountability gaps. |
| **Tool Use Risk** | Each tool an agent can invoke represents a capability and a risk surface. An agent with database write access can cause more harm than one with read-only access. | Traditional models do not invoke tools; their risk surface is limited to their output. |
| **Conversation Context** | Agents accumulate context over multi-turn conversations, and earlier context influences later decisions. Adversarial context injection can manipulate agent behavior. | Traditional models process each input independently. |
| **Customer Trust** | Customers may not realize they are interacting with an AI, or may attribute human-level judgment to the agent. | Traditional models operate behind the scenes; agents interact directly with customers. |

---

## 3. Permission Boundary Model

Every agent operates within a defined permission boundary. The permission boundary specifies exactly what the agent can and cannot do across five action categories.

### 3.1 Permission Categories

| Permission | Definition | Example: Customer Service Agent | Example: Payment Agent |
|-----------|-----------|--------------------------------|----------------------|
| **READ** | Access and retrieve information | Read customer account details, transaction history, product catalog | Read account balance, payment history, beneficiary list |
| **WRITE** | Create or modify data | Log interaction notes, update ticket status | Create payment records, update beneficiary details |
| **DECIDE** | Make a judgment or classification | Classify query topic, determine sentiment, assess urgency | Determine if payment passes fraud checks |
| **ACT** | Execute an action with real-world consequences | Send an email, initiate a callback, apply a promotional offer | Execute a payment, modify a standing order |
| **ESCALATE** | Transfer control to a human or higher-authority agent | Route to human agent, flag for supervisor review | Route payment for manual approval, flag suspicious transaction |

### 3.2 Permission Boundary Definition Template

```yaml
agent_permission_boundary:
  agent_name: "Customer Onboarding Agent"
  agent_type: "orchestrator"
  risk_tier: "high"

  permissions:
    read:
      allowed:
        - "customer_application_data"
        - "identity_document_images"
        - "sanctions_screening_results"
        - "credit_bureau_data"
      denied:
        - "other_customers_data"
        - "internal_employee_data"
        - "system_configuration"

    write:
      allowed:
        - "application_status_updates"
        - "verification_results"
        - "audit_log_entries"
      denied:
        - "customer_account_creation"   # Must be done by human or dedicated service
        - "credit_limit_modifications"
        - "sanctions_list_modifications"

    decide:
      allowed:
        - "identity_verification_pass_fail"
        - "document_authenticity_assessment"
        - "application_completeness_check"
      denied:
        - "final_account_approval"      # Requires human approval
        - "sanctions_match_resolution"   # Requires human review
        - "credit_limit_determination"   # Separate high-risk system

    act:
      allowed:
        - "request_additional_documents_from_customer"
        - "send_status_update_to_customer"
        - "invoke_identity_verification_service"
      denied:
        - "open_customer_account"        # Human-approved action
        - "send_rejection_letter"        # Human-reviewed communication
        - "file_suspicious_activity_report"  # Regulatory action requires human

    escalate:
      triggers:
        - "sanctions_screening_returns_potential_match"
        - "identity_verification_confidence_below_0.85"
        - "customer_explicitly_requests_human_agent"
        - "application_flagged_as_politically_exposed_person"
        - "three_consecutive_document_verification_failures"
      target: "senior_onboarding_analyst"
      sla: "respond_within_15_minutes"
```

### 3.3 Permission Boundary Enforcement

Permission boundaries must be **enforced at runtime**, not merely documented. Enforcement mechanisms:

| Mechanism | Description | When to Use |
|-----------|-------------|-------------|
| **Tool-level access control** | Each tool the agent can invoke has an explicit allowlist of agents that can call it | Always -- baseline enforcement |
| **Action validation layer** | A middleware component that validates every agent action against its permission boundary before execution | Always -- catches boundary violations |
| **Rate limiting** | Maximum number of actions per time period (e.g., max 10 payment executions per minute) | Autonomous actors with financial impact |
| **Amount limiting** | Maximum monetary value per action (e.g., payments up to EUR 500 without human approval) | Payment agents, account modification agents |
| **Scope limiting** | Agent can only act on data within its defined scope (e.g., only the current customer's data) | Always -- prevents cross-customer data access |

---

## 4. Delegation Chain Governance

When an orchestrator agent delegates tasks to sub-agents, governance must track and control the entire chain.

### 4.1 Delegation Rules

| Rule | Description | Rationale |
|------|-----------|-----------|
| **No permission escalation** | A sub-agent cannot have broader permissions than the agent that delegated to it | Prevents privilege escalation through delegation |
| **Accountability flows up** | The orchestrator is accountable for the actions of all agents it delegates to | Clear accountability prevents "it was the sub-agent's fault" arguments |
| **Delegation must be logged** | Every delegation event (who delegated what to whom, when, with what context) is recorded in the audit trail | Auditability of the full decision chain |
| **Delegation depth limit** | Maximum number of delegation levels (e.g., orchestrator -> sub-agent -> sub-sub-agent, max depth 3) | Prevents runaway delegation chains that become unauditable |
| **Result validation** | The delegating agent must validate sub-agent outputs before using them in further decisions | Prevents compound errors from propagating unchecked |

### 4.2 Delegation Chain Example

```
  Customer Onboarding Orchestrator (risk tier: high)
  |
  |-- Delegates to: KYC Verification Agent (risk tier: high)
  |   |
  |   |-- Invokes: Identity verification service (external API)
  |   |-- Invokes: Document authenticity checker (internal model)
  |   |-- Returns: verification_result {status, confidence, evidence}
  |   |
  |   Orchestrator validates: confidence >= 0.85? If not, escalate.
  |
  |-- Delegates to: Risk Scoring Agent (risk tier: high)
  |   |
  |   |-- Reads: customer application data, credit bureau data
  |   |-- Invokes: Credit risk model
  |   |-- Returns: risk_score, risk_factors, recommendation
  |   |
  |   Orchestrator validates: risk_score within expected range?
  |   Risk factors make sense given application data?
  |
  |-- Delegates to: Compliance Screening Agent (risk tier: high)
  |   |
  |   |-- Invokes: Sanctions screening service
  |   |-- Invokes: PEP (Politically Exposed Person) check
  |   |-- Returns: screening_result {clear | potential_match | match}
  |   |
  |   Orchestrator: if potential_match or match -> ESCALATE to human
  |
  |-- Decision Point: All sub-agent results collected
  |   |
  |   If all clear + risk acceptable: recommend approval to human reviewer
  |   If any concern: escalate with full context to senior analyst
  |   NEVER: approve the account autonomously (permission denied)
```

---

## 5. Decision Audit Trail Requirements

Every agent action and decision must be logged in sufficient detail to reconstruct the full decision chain after the fact.

### 5.1 Required Audit Trail Fields

| Field | Description | Example |
|-------|-----------|---------|
| **trace_id** | Unique identifier linking all events in a single user interaction | "trace-2026-02-28-abc123" |
| **timestamp** | When the event occurred (UTC, millisecond precision) | "2026-02-28T14:30:22.456Z" |
| **agent_id** | Which agent performed the action | "kyc-verification-agent-v2.1" |
| **action_type** | What type of action (read, write, decide, act, escalate, delegate) | "decide" |
| **action_detail** | Specific action taken | "identity_verification_pass_fail" |
| **input_summary** | Summary of inputs used for the decision (not full PII) | "document_type: passport, country: NL" |
| **output** | The result of the action | "status: verified, confidence: 0.92" |
| **reasoning** | The agent's explanation for its action (for LLM agents: the reasoning chain) | "Document matches face photo with 92% confidence; metadata consistent" |
| **delegated_by** | If this was a delegated task, which agent delegated it | "onboarding-orchestrator-v1.3" |
| **permission_check** | Was the action within the agent's permission boundary? | "allowed: true" |
| **model_version** | Version of the underlying model or prompt | "kyc-model-v2.1-20260215" |

### 5.2 Audit Trail Retention

| Risk Tier | Retention Period | Query Capability |
|-----------|-----------------|-----------------|
| Minimal | 1 year | Basic search by trace_id and timestamp |
| Limited | 3 years | Search by trace_id, agent_id, action_type, timestamp range |
| High | 5 years (or as required by financial regulation) | Full reconstruction of any decision chain; exportable for regulatory requests |

---

## 6. Human-in-the-Loop Decision Points

Define explicitly when a human must approve before the agent can proceed. This is not a vague "human oversight" aspiration -- it is a concrete specification of decision points.

### 6.1 Decision Framework

| When Must a Human Approve? | Examples | Implementation |
|---------------------------|---------|----------------|
| **Financial impact above threshold** | Payments > EUR 500, credit limit changes > EUR 1,000 | Agent presents recommendation with evidence; human approves/rejects in approval queue |
| **Irreversible actions** | Account closure, data deletion, regulatory filing | Agent prepares the action; human executes it |
| **Adverse decisions affecting customers** | Application rejection, account restriction, service denial | Agent recommends with reasoning; human reviews and communicates to customer |
| **Regulatory actions** | Suspicious activity reports, regulatory notifications | Agent flags and prepares draft; human reviews, edits, and submits |
| **Low confidence decisions** | Agent confidence below defined threshold (e.g., < 0.85) | Agent escalates with context; human makes the decision |
| **Sensitive customer situations** | Vulnerability indicators, complaints, distress signals | Agent transfers to human immediately |
| **Novel situations** | Query or scenario not covered by training or eval suite | Agent acknowledges limitation and escalates |

### 6.2 Human-in-the-Loop Workflow

```
  Agent reaches decision point requiring human approval
       |
       v
  Agent prepares approval request:
  - Recommended action
  - Evidence and reasoning
  - Confidence level
  - Risk assessment
  - Alternative options (if applicable)
       |
       v
  Approval request enters human queue
  (with SLA: respond within X minutes/hours)
       |
       +-- Human APPROVES --> Agent executes approved action
       |                      Audit trail: "approved by [human], [timestamp]"
       |
       +-- Human MODIFIES --> Agent executes modified action
       |                      Audit trail: "modified by [human]: [changes], [timestamp]"
       |
       +-- Human REJECTS --> Agent informs customer of delay / alternative
                             Audit trail: "rejected by [human]: [reason], [timestamp]"
```

---

## 7. Inter-Agent Communication Protocols

When agents communicate with each other (delegation, data sharing, result passing), governance requires structured protocols.

### 7.1 Communication Standards

| Requirement | Description | Rationale |
|------------|-----------|-----------|
| **Structured messages** | Inter-agent messages use a defined schema, not free-text | Prevents prompt injection between agents; enables validation |
| **Input validation** | Receiving agent validates all inputs from delegating agent | Sub-agent must not trust orchestrator inputs blindly |
| **Output validation** | Delegating agent validates all outputs from sub-agent | Orchestrator must verify sub-agent results before using them |
| **No credential passing** | Agents do not share credentials; each agent authenticates independently | Prevents credential leakage across the agent chain |
| **Context isolation** | Sub-agents receive only the context necessary for their task, not the full conversation history | Least-privilege principle applied to information sharing |

### 7.2 Communication Logging

All inter-agent communication is logged in the audit trail with:
- Sender agent ID and receiver agent ID
- Message content (or summary for large payloads)
- Timestamp
- Validation result (input accepted or rejected)

---

## 8. Error Handling and Graceful Degradation

Agent systems must degrade gracefully when problems occur, rather than failing silently or producing harmful outputs.

### 8.1 Degradation Hierarchy

| Level | Situation | Agent Behavior |
|-------|----------|----------------|
| **Normal** | All systems operational, confidence high | Agent operates autonomously within permissions |
| **Reduced** | One sub-agent unavailable or returning errors | Orchestrator skips the unavailable step; informs customer of limitation; continues with available capabilities |
| **Assisted** | Agent confidence low or novel situation detected | Agent presents options to customer but defers decision to human |
| **Manual** | Multiple failures or critical error detected | Agent transfers to human with full context; provides summary of what has been completed and what remains |
| **Emergency** | Safety violation detected or system integrity compromised | Circuit breaker activated; all agent actions halted; customer informed; incident team notified |

### 8.2 Error Handling Rules

1. **Never guess when uncertain.** If the agent cannot determine the right action with sufficient confidence, escalate to a human.
2. **Never compound errors.** If a sub-agent returns an error, the orchestrator must not proceed as if the step succeeded.
3. **Always inform the customer.** If the agent's capability is reduced, tell the customer what it can and cannot do.
4. **Log everything.** Error conditions are the most important events to log -- they are the ones you will need to investigate.
5. **Fail open, not closed** (for informational agents). A failed FAQ lookup should say "I cannot find that information" not silently return nothing.
6. **Fail closed, not open** (for decision-making agents). A failed fraud check should block the transaction, not approve it.

---

## 9. Customer Transparency

### 9.1 When Must the Customer Know They Are Interacting with an Agent?

| Scenario | Disclosure Required? | Regulatory Basis |
|----------|---------------------|-----------------|
| Customer interacts with a chatbot or voice agent | **Yes, always** | EU AI Act Art. 50(1) |
| Agent generates content shown to the customer (emails, reports, summaries) | **Yes** -- content must be labeled as AI-generated | EU AI Act Art. 50(2) |
| Agent makes a decision affecting the customer (application outcome, fraud flag) | **Yes** -- customer must be informed of AI involvement and have the right to explanation | GDPR Art. 22; EU AI Act Art. 86 |
| Agent recommends products or services to the customer | **Yes** -- customer must know recommendation is AI-generated | EU AI Act Art. 50; consumer protection |
| Agent operates entirely behind the scenes (e.g., internal fraud scoring) | **Partial** -- customer has right to explanation if adversely affected | GDPR Art. 22 |

### 9.2 Disclosure Implementation

| Mechanism | Description | When |
|-----------|-------------|------|
| **Session opening disclosure** | "I am an AI assistant. I can help with [scope]. For complex matters, I can connect you with a human agent." | Start of every customer interaction |
| **Action disclosure** | "I am going to [action]. This will [consequence]." | Before any agent action with customer impact |
| **Decision disclosure** | "Based on [factors], the recommendation is [outcome]. This assessment was made by an AI system." | When communicating any decision |
| **Limitation disclosure** | "I am not able to help with [out-of-scope topic]. Let me connect you with someone who can." | When agent reaches its capability boundary |
| **Right to human** | "Would you prefer to speak with a human agent? I can transfer you now." | Available at any point in the interaction |

---

## 10. Regulatory Compliance for Autonomous Decisions

### 10.1 GDPR Article 22 Compliance

When an AI agent makes a decision that produces legal effects or similarly significantly affects a natural person, GDPR Article 22 applies:

| Requirement | Implementation for Agent Systems |
|------------|--------------------------------|
| **Right not to be subject to solely automated decisions** | Ensure human-in-the-loop for adverse decisions (application rejections, account restrictions, service denials) |
| **Right to obtain human intervention** | Implement escalation path that the customer can invoke at any time |
| **Right to express their point of view** | Agent must accept and record customer objections; route to human for review |
| **Right to contest the decision** | Implement appeals process; agent must explain how to appeal |
| **Right to meaningful information about the logic** | Agent must be able to explain the key factors in any decision |

### 10.2 EU AI Act Compliance for Agent Systems

| EU AI Act Requirement | Agent Implementation |
|----------------------|---------------------|
| **Art. 14: Human oversight** | Permission boundaries, HITL decision points, kill switch |
| **Art. 50: Transparency** | Customer disclosure at session start and for AI-generated content |
| **Art. 9: Risk management** | Permission boundaries, error handling, graceful degradation |
| **Art. 12: Record-keeping** | Decision audit trail with full reconstruction capability |
| **Art. 13: Transparency of operation** | Documented agent architecture, permission boundaries, decision logic |

---

## 11. Example: Governing a Multi-Agent Customer Onboarding System

### System Architecture

A FinTech uses a multi-agent system for customer onboarding (opening a bank account):

```
  Customer
     |
     v
  Onboarding Orchestrator (limited risk)
     |
     +-- KYC Agent (high risk)
     |   - Verifies identity documents
     |   - Performs liveness check
     |   - Checks against identity databases
     |
     +-- Risk Scoring Agent (high risk)
     |   - Assesses customer risk profile
     |   - Checks credit bureau data
     |   - Produces risk score and factors
     |
     +-- Compliance Screening Agent (high risk)
     |   - Sanctions screening
     |   - PEP (Politically Exposed Person) check
     |   - Adverse media screening
     |
     +-- Communication Agent (limited risk)
         - Sends status updates to customer
         - Requests additional documents
         - Answers customer questions about the process
```

### Governance Configuration

| Governance Element | Configuration |
|-------------------|---------------|
| **Overall risk tier** | High (contains high-risk sub-agents; Annex III category 1(a) and 5) |
| **Customer disclosure** | Communication Agent discloses AI nature at session start; all generated messages labeled as AI |
| **HITL decision points** | Final account approval requires human; sanctions match requires human; application rejection requires human |
| **Permission boundaries** | See Section 3.2 example above |
| **Delegation depth** | Max 2 levels (orchestrator -> sub-agent -> external service) |
| **Escalation triggers** | Sanctions match, low KYC confidence, PEP flag, customer requests human |
| **Audit trail** | Full trace from customer application through every sub-agent action to final decision |
| **Kill switch** | Orchestrator can be shut down independently; individual sub-agents can be disabled while others continue |
| **Fallback** | If any sub-agent fails: orchestrator informs customer of delay, routes to manual onboarding process |
| **Fairness monitoring** | KYC pass rates and risk scores monitored for demographic parity across nationality, age, gender |
| **Eval suite** | End-to-end onboarding scenario tests; sub-agent unit evals; fairness evals; adversarial prompt injection tests |

### Governance Evidence Required for Deployment

1. Risk classification for each sub-agent individually and for the orchestrated system
2. Permission boundary definitions for each agent (approved by Governance Committee)
3. HITL decision point specification (approved by Compliance)
4. Eval suite passing all acceptance criteria (including fairness)
5. Shadow mode results showing onboarding quality matches or exceeds manual process
6. Customer disclosure UX reviewed and approved
7. Audit trail tested: full decision reconstruction demonstrated
8. Kill switch tested: system shuts down cleanly within 30 seconds
9. Fallback tested: manual onboarding process activates when orchestrator is disabled

---

## Cross-References

- **Defining Acceptance Criteria:** [../../01-discovery-governance/evaluations/defining-acceptance-criteria.md](../../01-discovery-governance/evaluations/defining-acceptance-criteria.md) -- acceptance criteria for agent systems
- **Eval-Driven Development:** [../../02-development-governance/evaluations/eval-driven-development.md](../../02-development-governance/evaluations/eval-driven-development.md) -- eval suite methodology for agent features
- **Pre-Deployment Gate:** [../../02-development-governance/checklists/pre-deployment-gate.yaml](../../02-development-governance/checklists/pre-deployment-gate.yaml) -- agent-specific items in the deployment checklist (DEV-SEC-004, DEV-HUM-001 through DEV-HUM-004)
- **Continuous Online Evaluation:** [../evaluations/continuous-online-evaluation.md](../evaluations/continuous-online-evaluation.md) -- production monitoring for agent systems
- **Risk Tiering Model:** [../../07-enterprise-implementation/risk-based-adoption/risk-tiering-model.md](../../07-enterprise-implementation/risk-based-adoption/risk-tiering-model.md) -- risk classification including agent-specific considerations
- **Three Lines of Defense:** [../../07-enterprise-implementation/organizational-model/three-lines-of-defense-for-ai.md](../../07-enterprise-implementation/organizational-model/three-lines-of-defense-for-ai.md) -- accountability model for agent governance
- **Glossary:** [../../05-cross-cutting/glossary.md](../../05-cross-cutting/glossary.md) -- definitions of agent, orchestrator, sub-agent, delegation chain, permission boundary, HITL, HOTL, HIC

---

*Last updated: 2026-02-28*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
