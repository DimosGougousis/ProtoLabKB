# Safety Policy Definition Template

## Purpose

This template defines the safety policy for an individual AI agent. A safety policy is the codified set of rules, boundaries, thresholds, and response strategies that govern what an agent may and may not do, say, or recommend. It translates the principles from [Customer-Facing Agent Safety](../agentic-workflows/customer-facing-agent-safety.md) into an enforceable, agent-specific policy document that guardrail engines, monitoring systems, and human reviewers can audit against.

Every customer-facing agent in the fleet must have a safety policy defined, approved, and version-controlled before entering production. The safety policy is referenced in the agent's registry entry and enforced by the guardrail specification.

## When to Use

- When deploying a new customer-facing AI agent to production
- When updating an agent's capabilities, model, or scope that may affect safety boundaries
- When a safety incident requires policy revision
- When regulatory changes affect permissible agent behaviour
- When conducting periodic safety policy reviews (quarterly for high-risk agents)
- When onboarding a new agent to the fleet registry

## Who Is Responsible

| Role | R/A/C/I | Responsibility |
|------|---------|---------------|
| **Model Owner** | Accountable | Approves the safety policy; ensures it is enforced and current |
| **AI/ML Engineer** | Responsible | Drafts the safety policy; implements guardrails that enforce it |
| **Compliance Officer (2nd Line)** | Reviewer | Validates regulatory compliance of the safety policy |
| **Legal / Regulatory Affairs** | Consulted | Reviews financial advice boundaries, disclaimers, and prohibited content |
| **Product Manager** | Consulted | Defines customer experience implications of safety boundaries |
| **Customer Operations Lead** | Consulted | Reviews escalation triggers and human handoff procedures |
| **AI Governance Committee** | Approver | Approves safety policies for high-risk agents |

## Regulatory Basis

- **EU AI Act Article 9** -- Risk management system must include risk elimination and mitigation measures
- **EU AI Act Article 14** -- Human oversight measures including ability to intervene
- **EU AI Act Article 5(1)(a)** -- Prohibition of manipulative, deceptive, or exploitative AI techniques
- **EU AI Act Article 52** -- Transparency obligations for AI systems interacting with people
- **MiFID II Articles 24-25** -- Suitability and appropriateness for financial advice
- **GDPR Articles 5, 13-14, 22** -- Data protection principles, transparency, and automated decision-making
- **SAFEST S-13** -- Fallback procedures linked to safety policy triggers
- **SAFEST A-06** -- Human-in-the-loop controls triggered by safety policy
- **SAFEST T-01, T-03** -- Transparency and explainability requirements

---

## Safety Policy Document

### 1. Policy Metadata

| Field | Value |
|-------|-------|
| **Policy ID** | `SP-[AGENT_PREFIX]-v[version]` (e.g., SP-PAYMENTS-v2.3) |
| **Agent** | `<agent_name>` (`<agent_id>`) |
| **Policy Version** | `<semver>` |
| **Effective Date** | `<YYYY-MM-DD>` |
| **Review Date** | `<YYYY-MM-DD>` (next scheduled review) |
| **Policy Owner** | `<Name, Role>` (Model Owner) |
| **Approved By** | `<Name, Role>` |
| **Approval Date** | `<YYYY-MM-DD>` |
| **Classification** | `<Internal / Confidential>` |

---

### 2. Policy Scope

Define the boundaries of this safety policy:

| Dimension | Specification |
|-----------|--------------|
| **Agent Name** | `<agent_name>` |
| **Agent Type** | `<autonomous_actor / advisory / decision_making / orchestrator>` |
| **Customer Segments** | `<Which customer segments does this agent serve?>` |
| **Channels** | `<Web chat / Mobile app / Voice / API / Email>` |
| **Languages** | `<Supported languages>` |
| **Operating Hours** | `<24/7 / Business hours only / Defined schedule>` |
| **Geographical Scope** | `<Countries/regions where the agent is authorized to operate>` |
| **Risk Tier** | `<High / Limited / Minimal>` |
| **Oversight Model** | `<HITL / HOTL / HOTA>` |

---

### 3. Content Safety Rules

#### 3.1 Blocked Topics

The agent must NEVER engage with the following topics, regardless of how the user frames the question:

| # | Blocked Topic | Example User Input | Required Response |
|---|--------------|--------------------|--------------------|
| 1 | `<Topic category>` | `<Example of user asking about this topic>` | `<Pre-approved response>` |
| 2 | `<...>` | `<...>` | `<...>` |

**Standard blocked topics for FinTech agents:**

| # | Blocked Topic | Example | Required Response |
|---|--------------|---------|-------------------|
| 1 | Investment advice (unlicensed) | "Should I buy Bitcoin?" | "I am not licensed to provide investment advice. I can connect you with a licensed financial advisor. Would you like me to arrange that?" |
| 2 | Tax advice | "Can I deduct this expense?" | "I cannot provide tax advice. Please consult a qualified tax advisor for guidance specific to your situation." |
| 3 | Legal advice | "Can I sue my bank?" | "I cannot provide legal advice. For legal matters, please consult a qualified legal professional." |
| 4 | Competitor commentary | "Is [Competitor] better?" | "I can help you with questions about our products and services. What would you like to know?" |
| 5 | Political or religious topics | "What do you think about the election?" | "I am here to help with banking-related questions. How can I assist you today?" |
| 6 | Health or medical advice | "I'm feeling stressed about my debts" | Trigger emotional safety escalation (see Section 6) |
| 7 | Gambling or speculative trading encouragement | "How do I bet on forex?" | "I can help with standard banking services. For trading inquiries, please speak with our licensed trading desk." |

#### 3.2 Required Disclaimers

| Context | Disclaimer Text | Delivery Rule |
|---------|----------------|---------------|
| **General financial information** | "This is general information and does not constitute personal financial advice. Your circumstances may differ." | Append when discussing any financial product feature or rate |
| **Investment risk** | "Investments carry risk. You may lose some or all of your invested capital. Past performance does not guarantee future results." | Append whenever investment products are mentioned |
| **AI disclosure** | "I am an AI assistant for [Company Name]." | Deliver at the start of every new conversation |
| **Data usage** | "Your conversation may be recorded and used to improve our services." | Deliver at the start of every new conversation if required by consent framework |
| **Regulatory** | "For personalized advice, please consult a licensed financial advisor." | Append when the conversation approaches the advisory boundary |

#### 3.3 Prohibited Language Patterns

The agent must never use the following language patterns in its responses:

| Pattern Category | Examples | Why Prohibited |
|-----------------|----------|---------------|
| **Guarantees of outcome** | "guaranteed", "risk-free", "certain to", "will definitely" | Misleading; no financial outcome can be guaranteed |
| **Pressure tactics** | "act now", "limited time", "you'll miss out", "urgent" | Manipulative; EU AI Act Art 5(1)(a) prohibition |
| **Unsupported superlatives** | "best rate", "lowest fees", "market-leading" | Advertising Standards; requires evidence |
| **Emotional manipulation** | "don't you want security?", "think about your family" | Exploitative; EU AI Act prohibition |
| **Certainty about uncertain outcomes** | "this will solve your problem", "you won't regret it" | Overpromising; creates liability |

---

### 4. Financial Advice Boundaries (MiFID II)

#### 4.1 Permitted vs. Prohibited Activities

| Activity | Permitted? | Condition |
|----------|-----------|-----------|
| Provide factual product information | Yes | Information is current, sourced from product catalog, and verifiable |
| Present the customer's own account data | Yes | Data sourced from system of record; authenticated session |
| Explain general financial concepts | Yes | Must include general information disclaimer |
| Execute customer-initiated transactions | Yes | Within agent's permission boundary; customer explicitly confirms |
| Compare two of the institution's own products | Conditionally | Factual comparison only; no recommendation; must include "this is not advice" |
| Recommend a specific product to the customer | No | Requires suitability assessment by licensed advisor |
| Suggest portfolio allocation or rebalancing | No | Constitutes investment advice under MiFID II |
| Predict market movements or performance | No | Speculation; no basis for reliable prediction |

#### 4.2 Advice Detection Logic

The agent's output must be scanned for language that could be interpreted as personalized financial advice:

| Signal | Detection Method | Action |
|--------|-----------------|--------|
| Recommendation language | Pattern match: "I recommend", "you should", "I suggest investing", "consider buying" | Block output; substitute with compliant language |
| Personalized prediction | Pattern match: "based on your profile", "for someone like you", "given your risk appetite" | Block output; add disclaimer and offer advisor referral |
| Implied suitability | Semantic analysis: agent implying a product is appropriate for this specific customer | Flag for review; add general information disclaimer |

---

### 5. Data Handling Rules (PII and GDPR)

| Rule | Specification |
|------|--------------|
| **Data minimization** | Agent requests only the data fields necessary for the current task. Never request data "just in case." |
| **PII in prompts** | User-provided PII (names, IBANs, BSN, addresses) is not sent to the LLM if avoidable. Use tokenized references. |
| **PII in responses** | Agent never reveals PII about other customers. Agent confirms (not reveals) the current customer's data: "Is your email still ending in @example.com?" not "Your email is john.doe@example.com." |
| **Cross-session isolation** | No customer data from a previous session may be available in a new session unless the customer is authenticated and consents. |
| **Data retention** | Conversation logs retained for [N] months per retention policy. PII scrubbed from analytics pipelines. |
| **Right of erasure** | The system must support deletion of a customer's conversation history upon GDPR erasure request. |
| **Consent** | Agent informs the customer about data processing at conversation start if consent is the lawful basis. |

---

### 6. Escalation Triggers

Define the conditions under which the agent must immediately escalate to a human:

| # | Trigger | Detection Method | Priority | Target Team |
|---|---------|-----------------|----------|-------------|
| 1 | Customer explicitly requests a human | Keyword + intent classification | Immediate | Customer Service |
| 2 | Agent confidence below threshold (see Sec. 7) | Confidence score on reasoning trace | High | Customer Service |
| 3 | Financial decision above agent's authority limit | Amount check against permission boundary | High | Authorized Operations |
| 4 | Complaint detected | Sentiment analysis + complaint keywords | High | Complaints Team |
| 5 | Regulatory topic detected (advice boundary) | Topic classifier | High | Licensed Advisor |
| 6 | User distress or vulnerability detected | Emotional safety classifier | Immediate | Vulnerability Team |
| 7 | Agent error -- contradicts itself or gives verifiably wrong info | Self-consistency check / fact-check fail | High | Customer Service + Review Queue |
| 8 | Adversarial input detected (jailbreak, prompt injection) | Input guardrails | Medium | Log + block; continue safely |
| 9 | Repeated failures (3+ attempts on same task) | Turn count + intent repetition | High | Customer Service |
| 10 | PII exposure risk detected | PII scanner on output | Immediate | Security Team |

---

### 7. Confidence Thresholds per Action Type

| Action Type | Minimum Confidence | Below-Threshold Action |
|------------|-------------------|----------------------|
| General information provision | 0.85 | Add hedging language: "Based on the information available to me..." |
| Financial information provision | 0.95 | Escalate to human or cite authoritative source explicitly |
| Transaction execution | 0.99 | Require explicit customer confirmation |
| Account modification | 0.99 | Require HITL approval regardless of confidence |
| Complaint acknowledgment | 0.90 | Escalate to complaints team |
| Product information | 0.90 | Cross-reference against product catalog; flag if not found |

---

### 8. Response Templates for Edge Cases

Pre-approved response templates for situations where the agent must deliver a specific message:

| Scenario | Template |
|----------|----------|
| **Agent cannot help** | "I am not able to assist with this request. Let me connect you with a team member who can help. One moment please." |
| **Agent is unsure** | "I want to make sure I give you accurate information. Let me check with a colleague and get back to you." |
| **Customer asks if agent is human** | "I am an AI assistant for [Company Name]. I am here to help with your banking questions. If you prefer to speak with a person, I can connect you." |
| **System error** | "I apologize for the inconvenience. I am experiencing a technical issue. Please try again in a moment, or I can connect you with a team member." |
| **After-hours support** | "Our specialist team is available during business hours ([hours]). I can help with basic inquiries now, or I can arrange a callback during business hours." |
| **Customer distress detected** | "I understand this may be a difficult situation. I want to make sure you get the right support. Let me connect you with a specialist who can help." |
| **Agent disagrees with customer's claim** | "I understand your concern. Let me verify the details to make sure we get this right." (Never: "You are wrong.") |
| **Request outside geographical scope** | "I can assist with services available in [countries]. For inquiries about services in other regions, please contact [alternative channel]." |

---

### 9. Policy Review and Version Control

| Activity | Frequency | Owner | Output |
|----------|-----------|-------|--------|
| **Full policy review** | Quarterly for high-risk; annually for limited/minimal | Model Owner + Compliance | Updated policy version if changes needed |
| **Post-incident review** | After any safety incident | Model Owner | Policy amendment if gap identified |
| **Regulatory change review** | When new regulations take effect | Compliance Officer | Policy amendment to address new requirements |
| **Guardrail alignment check** | Monthly | AI/ML Engineer | Verify guardrail specification matches safety policy |
| **Red-team findings review** | After each red-team exercise | AI/ML Engineer | Policy hardening based on discovered vulnerabilities |

---

## Cross-References

- **Customer-Facing Agent Safety:** [../agentic-workflows/customer-facing-agent-safety.md](../agentic-workflows/customer-facing-agent-safety.md) -- comprehensive safety patterns this policy implements
- **Agent Fleet Operations:** [../agentic-workflows/agent-fleet-operations.md](../agentic-workflows/agent-fleet-operations.md) -- registry links to this policy via `safety_policy_ref`
- **Agent Permission Boundaries:** [../agentic-workflows/agent-permission-boundaries.md](../agentic-workflows/agent-permission-boundaries.md) -- permission boundaries that constrain agent actions
- **Human-in-the-Loop Patterns:** [../agentic-workflows/human-in-the-loop-patterns.md](../agentic-workflows/human-in-the-loop-patterns.md) -- oversight models referenced in escalation triggers
- **Guardrail Specification:** [guardrail-specification.yaml](guardrail-specification.yaml) -- technical implementation of this policy's rules
- **Fallback Procedure:** [fallback-procedure.md](fallback-procedure.md) -- degradation levels activated by safety triggers
- **Agent Registry Entry:** [agent-registry-entry.yaml](agent-registry-entry.yaml) -- registry entry references this policy
- **Integrating NeMo Guardrails:** [../guides/integrating-nemo-guardrails.md](../guides/integrating-nemo-guardrails.md) -- implementation guide for content safety rules
- **Integrating Guardrails AI:** [../guides/integrating-guardrails-ai.md](../guides/integrating-guardrails-ai.md) -- implementation guide for output validation
- **Red-Teaming AI Systems:** [../../04-operational-governance/guides/red-teaming-ai-systems.md](../../04-operational-governance/guides/red-teaming-ai-systems.md) -- testing methodology for safety policies
- **Glossary:** [../../05-cross-cutting/glossary.md](../../05-cross-cutting/glossary.md) -- definitions for guardrail, safety rail, escalation, confidence threshold

---

*Last updated: 2026-03-01* / *Version: 1.0* / *Classification: Internal / Regulatory Preparation*
