# Customer-Facing Agent Safety

## Purpose

This document defines safety patterns for AI agents that interact directly with customers -- chatbots, virtual assistants, autonomous advisors, and any AI system that communicates with or makes decisions affecting end users. Customer-facing agents present unique safety risks because they operate at the intersection of automated decision-making, regulatory compliance, and human vulnerability.

A customer-facing agent that provides incorrect financial advice, leaks personal data between sessions, or fails to detect a user in distress creates real-world harm that no amount of post-incident analysis can undo. Safety must be designed in, not bolted on.

## When to Use

- When designing any AI agent that communicates with customers (chat, voice, email)
- When deploying autonomous agents that make decisions affecting customers (lending, account management, trading)
- When reviewing safety controls for an existing customer-facing agent
- When responding to a safety incident involving customer interactions
- When conducting red-teaming exercises against customer-facing agents

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **Model Owner** | **Accountable** -- owns the agent's safety posture; approves safety configurations |
| **AI/ML Engineer** | **Responsible** -- implements safety guardrails, content filters, and escalation logic |
| **Product Manager** | **Consulted** -- defines customer experience requirements and acceptable escalation rates |
| **Compliance Officer (2nd Line)** | **Reviewer** -- validates regulatory compliance of agent behavior |
| **Customer Operations Lead** | **Consulted** -- defines escalation workflows and human handoff procedures |
| **AI Governance Committee** | **Approver** -- approves safety policies for high-risk customer-facing agents |

## Regulatory Basis

- **EU AI Act Article 52(1)** -- AI systems interacting with natural persons must disclose they are AI (transparency obligation)
- **EU AI Act Article 14** -- Human oversight measures for high-risk AI systems
- **EU AI Act Article 5(1)(a)** -- Prohibition of AI systems that deploy subliminal, manipulative, or deceptive techniques
- **Consumer Rights Directive (2011/83/EU)** -- Consumer protection obligations in digital services
- **MiFID II Articles 24-25** -- Suitability and appropriateness requirements for investment advice
- **GDPR Articles 13-14** -- Information obligations when processing personal data
- **SAFEST items S-13** (fallback procedures), **A-06** (human-in-the-loop), **T-01** (transparency), **T-03** (explainability)

---

## 1. Content Safety

### 1.1 Content Safety Guardrails

Every customer-facing agent must have output guardrails that prevent the following categories of unsafe content:

| Category | Description | Guardrail Action |
|----------|-------------|-----------------|
| **Harmful Content** | Violence, self-harm, illegal activities, dangerous instructions | Block output; log incident; substitute safe response |
| **Misleading Information** | Fabricated facts, hallucinated data, false claims about products or services | Detect via grounding checks; require factual citation; flag low-confidence outputs |
| **Non-Compliant Statements** | Statements that violate regulations (e.g., guaranteed returns, unauthorized medical advice) | Pattern-match against prohibited phrase list; block and substitute compliant language |
| **Discriminatory Content** | Responses that treat users differently based on protected attributes | Fairness guardrails on output; monitor for differential treatment patterns |
| **Manipulative Content** | Responses designed to pressure, deceive, or exploit users | Block dark-pattern language; monitor for upselling pressure metrics |
| **Profane or Offensive Content** | Inappropriate language, insults, offensive material | Content filter on all outputs; immediate block |

### 1.2 Content Safety Implementation

```
  Agent generates response
       |
       v
  +---------------------------+
  | OUTPUT SAFETY PIPELINE    |
  |                           |
  | 1. Factual grounding      |
  |    check (hallucination   |
  |    detection)             |
  |                           |
  | 2. Regulatory compliance  |
  |    scan (prohibited       |
  |    phrases, unauthorized  |
  |    claims)                |
  |                           |
  | 3. Content safety filter  |
  |    (harmful, offensive,   |
  |    manipulative)          |
  |                           |
  | 4. PII leakage scan       |
  |    (no cross-session      |
  |    data exposure)         |
  |                           |
  | 5. Confidence threshold   |
  |    check (low-confidence  |
  |    responses flagged)     |
  +---------------------------+
       |
       v (if all checks pass)
  Deliver response to customer
       |
       v (if any check fails)
  Substitute safe fallback response
  Log the blocked content for review
  Escalate if safety-critical
```

---

## 2. Financial Advice Boundaries

In regulated FinTech, agents must operate within strict boundaries regarding financial guidance.

### 2.1 What Agents CAN Do

| Permitted | Example | Condition |
|-----------|---------|-----------|
| Provide factual product information | "Our savings account offers a variable interest rate, currently at 2.5% per annum" | Information must be current and verifiable |
| Present account data | "Your current balance is EUR 5,230.41" | Data sourced from authoritative system of record |
| Explain general financial concepts | "A fixed-rate mortgage means your interest rate does not change during the fixed period" | Must include disclaimer that this is general information, not personal advice |
| Execute customer-initiated transactions | Process a payment the customer explicitly requested | Within permission boundaries (see [Agent Permission Boundaries](agent-permission-boundaries.md)) |
| Direct customers to appropriate human advisors | "For personalized investment advice, I can connect you with a licensed financial advisor" | Always available as an escalation path |

### 2.2 What Agents MUST NOT Do

| Prohibited | Example of Violation | Regulatory Risk |
|-----------|---------------------|-----------------|
| Provide personalized investment advice | "Based on your profile, you should invest in index funds" | MiFID II suitability requirements; unlicensed advice |
| Guarantee returns or outcomes | "This investment will earn you at least 8% per year" | Consumer protection; misleading advertising |
| Recommend specific financial products without suitability assessment | "You should open our premium credit card" | MiFID II; Consumer Rights Directive |
| Minimize risk | "This investment is completely safe" | Misleading; all investments carry risk |
| Pressure customers into financial decisions | "This rate is only available today; you should act now" | Manipulative practices; EU AI Act Article 5 |
| Provide tax advice | "You can deduct this from your taxes" | Unauthorized professional advice |

### 2.3 Required Disclaimers

Every customer-facing agent that discusses financial topics must include appropriate disclaimers:

- **General information disclaimer:** "This is general information and not personal financial advice. Your individual circumstances may differ."
- **Investment risk disclaimer:** "Investments carry risk. You may lose some or all of your invested capital. Past performance is not a guarantee of future results."
- **Regulatory disclaimer:** "For personalized advice, please consult a licensed financial advisor."

Disclaimers must be delivered naturally within the conversation flow, not as walls of legal text that users will ignore.

---

## 3. Real-Time Regulatory Compliance

### 3.1 Compliance Rules Engine

Implement a real-time compliance rules engine that evaluates every agent response against applicable regulations before delivery:

| Rule Category | Example Rules | Action on Violation |
|--------------|---------------|-------------------|
| **Disclosure Rules** | Agent must identify as AI at start of conversation | Block interaction until disclosure delivered |
| **Product Suitability** | Agent must not recommend products to ineligible customers | Block recommendation; suggest human advisor |
| **Advertising Standards** | No superlative claims without evidence ("best," "guaranteed," "risk-free") | Rewrite response with compliant language |
| **Data Protection** | Agent must not request more data than necessary for the task | Block excessive data requests; enforce data minimization |
| **Record Keeping** | Financial interactions must be logged for regulatory audit | Log all interactions with timestamps and agent identity |
| **Cooling-Off Period** | Customers have a right to cancel certain financial products within a cooling-off period | Agent must inform customers of cooling-off rights before confirming transactions |

---

## 4. Escalation Triggers

### 4.1 Mandatory Escalation Conditions

The agent must immediately escalate to a human when any of the following conditions are detected:

| Trigger | Detection Method | Escalation Priority |
|---------|-----------------|---------------------|
| **Customer requests a human** | Keyword detection + intent classification | Immediate -- no delay or persuasion to stay with the agent |
| **Agent confidence below threshold** | Confidence score on agent's reasoning trace | High -- transfer within 60 seconds |
| **Financial decision above limit** | Parameter check on transaction amount | High -- per [Agent Permission Boundaries](agent-permission-boundaries.md) |
| **Complaint detected** | Sentiment analysis + complaint keyword detection | High -- route to complaints team |
| **Regulatory topic detected** | Topic classification identifies regulated advice territory | High -- route to licensed advisor |
| **User distress detected** | Emotional safety classifier (see Section 9) | Immediate -- route to trained support team |
| **Agent error detected** | Agent contradicts itself or provides verifiably wrong information | High -- correct and escalate for review |
| **Adversarial input detected** | Prompt injection or jailbreak attempt detected by input guardrails | Medium -- log, block, and continue with safe response |
| **Repeated failures** | Agent fails to resolve after 3 attempts on the same task | High -- escalate to human with full context |

### 4.2 Escalation Behavior

When an escalation trigger fires, the agent must:

1. **Acknowledge** the situation to the customer ("Let me connect you with a specialist who can help with this.")
2. **Transfer context** to the human operator (full conversation history, reasoning trace, escalation reason)
3. **Not attempt** to resolve the issue itself after the escalation decision
4. **Not discourage** the customer from speaking to a human ("Are you sure? I can probably help.")
5. **Log** the escalation event with trigger type, timestamp, and context for analysis

---

## 5. Confidence Thresholds for Autonomous Actions

| Action Type | Minimum Confidence for Autonomous Execution | Below Threshold Action |
|------------|---------------------------------------------|----------------------|
| Information provision (general) | 0.85 | Add hedging language: "Based on the information I have..." |
| Information provision (financial) | 0.95 | Escalate to human or cite source explicitly |
| Transaction execution | 0.99 | Require explicit customer confirmation before proceeding |
| Account modification | 0.99 | Require HITL approval |
| Complaint resolution | 0.90 | Escalate to complaints team |

---

## 6. Fallback and Graceful Degradation

### 6.1 Degradation Hierarchy

When the agent cannot complete a task, it must degrade gracefully through a defined hierarchy:

```
  Level 0: FULL SERVICE
  Agent handles the request autonomously
       |
       v (if agent cannot handle)
  Level 1: REDUCED AUTONOMY
  Agent provides information but asks customer to confirm actions
       |
       v (if still cannot handle)
  Level 2: GUIDED ESCALATION
  Agent explains what it cannot do and offers to connect to a human
       |
       v (if human unavailable)
  Level 3: SAFE FALLBACK
  Agent provides a safe, pre-scripted response with contact information
  "I am unable to help with this right now. Please contact us at
   [phone/email] during business hours, or I can have someone call you back."
       |
       v (if system failure)
  Level 4: EMERGENCY FALLBACK
  Static page or message displayed without agent involvement
  "Our AI assistant is currently unavailable. Please call [number]."
```

### 6.2 Graceful Degradation Rules

- The agent must never generate a response when it is uncertain and cannot verify. Silence is safer than hallucination.
- Every fallback level must provide the customer with a viable next step. Never leave the customer in a dead end.
- Fallback responses must be pre-approved by compliance and tested regularly.
- Log all degradation events for root cause analysis and agent improvement.

---

## 7. Session Context Safety

### 7.1 Data Isolation Between Sessions

| Requirement | Implementation |
|-------------|----------------|
| **No cross-session data leakage** | Each session operates in an isolated memory context. Customer A's data must never appear in Customer B's session. |
| **Session-scoped memory** | Agent memory (conversation history, retrieved data) is purged when the session ends. |
| **Authentication binding** | Agent can only access data belonging to the authenticated customer in the current session. |
| **PII scrubbing in logs** | Customer PII in conversation logs is masked or encrypted before storage. |
| **Context window hygiene** | Stale context from previous turns is managed to prevent the agent from confusing past and present information. |

### 7.2 Multi-Tenant Safety

For agents serving multiple customer segments or brands from a shared infrastructure:

- Strict data partitioning: customer data, product catalogs, and compliance rules are segregated by tenant.
- Agent behavior must not reference one tenant's information while serving another.
- Monitoring must detect and alert on any cross-tenant data access.

---

## 8. Agent Impersonation Prevention

### 8.1 Transparency Requirements

Under the EU AI Act (Article 52), AI systems interacting with natural persons must disclose that the customer is interacting with AI, not a human.

| Requirement | Implementation |
|-------------|----------------|
| **Initial disclosure** | At the start of every conversation: "I am an AI assistant for [Company Name]. How can I help you today?" |
| **No human impersonation** | The agent must not claim to be human, use a human name as if it were a person, or imply it has human experiences |
| **Capability honesty** | The agent must not overstate its capabilities ("I can definitely resolve this" when it might need to escalate) |
| **Limitation transparency** | When the agent reaches its limits, it must say so clearly ("I do not have the expertise to advise on this; let me connect you to a specialist") |

### 8.2 Testing Transparency Compliance

Include transparency checks in the agent's eval suite:

- Test that the agent identifies as AI in 100% of conversation openings.
- Test that the agent does not claim to be human when directly asked.
- Test that the agent does not fabricate personal experiences or emotions.
- See [Agent Performance Evaluations](../evaluations/agent-performance-evals.md) for transparency compliance metrics.

---

## 9. Emotional Safety

### 9.1 Detecting User Distress

Customer-facing agents must be equipped to detect indicators of user distress, including but not limited to financial distress, mental health crisis, or expressions of self-harm.

| Signal | Detection Method | Required Response |
|--------|-----------------|-------------------|
| **Self-harm or suicide indicators** | Keyword detection + intent classification model | Immediate: provide crisis hotline information; escalate to trained human support |
| **Severe financial distress** | Sentiment analysis + financial context (missed payments, debt mentions) | Provide debt advice service contact information; escalate to specialist team |
| **Anger or frustration** | Sentiment analysis + escalation keyword detection | Acknowledge emotion; offer human support; do not argue or dismiss |
| **Vulnerability indicators** | Age-related confusion, language suggesting cognitive impairment | Escalate to specialist team trained in vulnerable customer support |

### 9.2 Emotional Safety Rules

- The agent must never dismiss, minimize, or argue with customer emotions.
- The agent must never provide mental health advice or diagnosis.
- Crisis responses (self-harm, suicide) must use pre-approved, clinically reviewed response templates.
- All emotional distress detections must be logged for review by the customer operations team.
- False positive rate on distress detection should be monitored; over-escalation is preferable to under-escalation.

---

## 10. Safety Testing Patterns

### 10.1 Adversarial Testing (Red-Teaming)

Conduct regular adversarial testing against customer-facing agents:

| Test Category | What to Test | Frequency |
|--------------|-------------|-----------|
| **Prompt injection** | Can the user manipulate the agent into ignoring its safety instructions? | Monthly + before every deployment |
| **Jailbreaking** | Can the user get the agent to produce prohibited content? | Monthly + before every deployment |
| **Data extraction** | Can the user trick the agent into revealing system prompts, other users' data, or internal information? | Monthly |
| **Social engineering** | Can the user manipulate the agent into bypassing permission boundaries? | Quarterly |
| **Boundary probing** | Can the user get the agent to provide financial advice it should not give? | Monthly |
| **Emotional manipulation** | Can the user manipulate the agent by feigning distress to bypass controls? | Quarterly |

### 10.2 Automated Safety Evaluation

Run automated safety eval suites continuously in production (see [Agent Performance Evaluations](../evaluations/agent-performance-evals.md), Section 10):

- Injection resistance test suite: 200+ adversarial prompts, run weekly
- Content safety test suite: 500+ test cases covering all prohibited content categories, run daily on a sample of production traffic
- Regulatory compliance test suite: 100+ scenarios covering financial advice boundaries, disclaimers, and disclosure requirements, run weekly

---

## 11. FinTech Agent Safety Examples

### 11.1 KYC/AML Agent Safety

An agent assisting with Know Your Customer and Anti-Money Laundering processes.

| Safety Concern | Mitigation |
|---------------|-----------|
| Agent must not reveal AML suspicion to the customer (tipping-off) | Hard guardrail: agent never mentions investigation, suspicious activity, or AML terms to the customer |
| Agent must not bypass identity verification steps | Sequential policy: each KYC step must complete successfully before the next begins |
| Agent must handle document verification failures safely | Graceful degradation: "I was unable to verify your document automatically. Let me connect you with a team member who can assist." |
| Customer data collected must be minimized | Agent requests only required fields; blocks over-collection |

### 11.2 Customer Complaint Agent Safety

| Safety Concern | Mitigation |
|---------------|-----------|
| Agent must not dismiss or minimize complaints | Sentiment-aware response generation; pre-approved acknowledgment templates |
| Agent must not make unauthorized commitments (refunds, compensation) | Permission boundary: complaint resolution actions above EUR 50 require human approval |
| Agent must log all complaints for regulatory reporting | All complaint interactions tagged and routed to complaints register |
| Agent must inform customer of their right to escalate | Mandatory at start of complaint: "If you are not satisfied with my response, I can connect you with a senior team member, or you can contact [external ombudsman]" |

### 11.3 Debt Collection Agent Boundaries

| Safety Concern | Mitigation |
|---------------|-----------|
| Agent must not use threatening or harassing language | Content safety filter with specific debt collection language rules |
| Agent must respect contact time restrictions | Temporal policy: agent cannot initiate contact outside permitted hours |
| Agent must inform customer of their rights | Required disclaimer at start of interaction covering dispute rights and debt advice services |
| Agent must detect and respond to vulnerability indicators | Emotional safety classifier triggers escalation to specialist vulnerability team |
| Agent must not misrepresent the debt or consequences | Factual grounding requirement: all debt figures sourced from authoritative system; no estimated or rounded figures |

---

## Cross-References

- **Agent Permission Boundaries:** [agent-permission-boundaries.md](agent-permission-boundaries.md) -- tool sovereignty and permission controls that safety patterns depend on
- **Human-in-the-Loop Patterns:** [human-in-the-loop-patterns.md](human-in-the-loop-patterns.md) -- oversight models and escalation workflows referenced throughout
- **Safety Policy Definition Template:** [../templates/safety-policy-definition.md](../templates/safety-policy-definition.md) -- template for codifying these safety patterns into enforceable policies
- **Agent Performance Evaluations:** [../evaluations/agent-performance-evals.md](../evaluations/agent-performance-evals.md) -- metrics for evaluating safety in production
- **Continuous Online Evaluation:** [../evaluations/continuous-online-evaluation.md](../evaluations/continuous-online-evaluation.md) -- monitoring infrastructure for safety metrics
- **Defining Acceptance Criteria:** [../../01-discovery-governance/evaluations/defining-acceptance-criteria.md](../../01-discovery-governance/evaluations/defining-acceptance-criteria.md) -- safety thresholds defined during discovery
- **Eval-Driven Development:** [../../02-development-governance/evaluations/eval-driven-development.md](../../02-development-governance/evaluations/eval-driven-development.md) -- safety eval suites developed before deployment
- **Glossary:** [../../05-cross-cutting/glossary.md](../../05-cross-cutting/glossary.md) -- definitions for guardrail, safety rail, escalation, graceful degradation

---

*Last updated: 2026-02-28*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
