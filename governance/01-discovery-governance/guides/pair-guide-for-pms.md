# PAIR Guide for Product Managers

## Purpose

This guide adapts the Google PAIR (People + AI Research) framework for Product Managers working on AI-powered products in regulated FinTech. PAIR provides research-backed design patterns for building AI products that people can understand, trust appropriately, and use effectively. This guide translates those patterns into actionable product decisions, with specific attention to the regulatory and ethical requirements of financial services.

PAIR's central insight is that AI products fail not when the model is inaccurate, but when the human-AI interaction is poorly designed. A credit scoring model with 95% accuracy still fails if applicants cannot understand why they were rejected, if loan officers over-rely on its recommendations, or if users cannot correct its mistakes. Product Managers are responsible for designing the interaction layer where these failures occur -- or are prevented.

This guide covers four core PAIR themes relevant to FinTech AI: user agency, mental model alignment, calibrated trust, and error recovery. Each section provides the underlying principle, practical product decisions, governance implications, and concrete FinTech examples.

## When to Use

- During **Discovery and Design phases** when defining how users will interact with AI features
- When designing human-in-the-loop (HITL) workflows for high-risk AI decisions
- When writing user stories or acceptance criteria for AI-powered features
- When reviewing UX designs for AI products before the Development Gate
- When preparing the interaction design section of a [Responsible Product Brief](../templates/responsible-product-brief.md)

**Trigger:** A product manager is making decisions about how users will experience, interact with, or be affected by AI capabilities.

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **Product Manager** | **Accountable** -- applies PAIR patterns to product decisions, documents interaction design rationale |
| **UX Designer** | **Responsible** -- translates PAIR patterns into interface designs, conducts usability testing |
| **AI/ML Engineer** | **Consulted** -- advises on what the model can and cannot support (confidence scores, explanations, uncertainty) |
| **Ethics Lead** | **Consulted** -- reviews user agency and fairness implications of interaction patterns |
| **Compliance Officer** | **Consulted** -- validates that interaction patterns meet EU AI Act transparency and human oversight requirements |

## Regulatory Basis

- **EU AI Act Article 13** -- Transparency requirements: high-risk AI systems must enable users to interpret output and use it appropriately
- **EU AI Act Article 14** -- Human oversight: high-risk AI systems must enable natural persons to understand the system's capacities and limitations, and to decide not to use the system or to override its output
- **EU AI Act Article 52** -- Transparency obligations for certain AI systems (chatbots, deepfakes, emotion recognition)
- **GDPR Article 22** -- Right not to be subject to a decision based solely on automated processing
- **GDPR Articles 13-14** -- Right to meaningful information about the logic involved in automated decision-making
- **DNB SAFEST (Transparency)** -- Financial institutions must ensure AI systems are transparent to users and supervisors
- **EBA Guidelines on Loan Origination (2020)** -- Credit decisions must be explainable to applicants

---

## 1. User Agency: When Should the AI Act, Suggest, or Defer?

### The PAIR Principle

User agency describes the degree of control users have over AI-driven outcomes. PAIR identifies a spectrum of automation from full human control to full AI autonomy. The critical product decision is where on this spectrum each AI capability should sit -- and this decision must be made deliberately, not by default.

### The Agency Spectrum

```
HUMAN CONTROL ◄──────────────────────────────────────────────► AI AUTONOMY

  INFORM         SUGGEST          RECOMMEND        ACT             ACT
  (AI provides   (AI offers       (AI selects      (AI acts,       (AI acts
   data, human    options,         preferred        human can       autonomously,
   decides)       human picks)     option,          review/         no human
                                   human            reverse)        review)
                                   approves)
```

### Agency Decision Framework for FinTech

Use this framework to determine the appropriate agency level for each AI capability in your product.

| Factor | Indicates Higher Human Agency | Indicates Higher AI Agency |
|--------|-------------------------------|---------------------------|
| **Reversibility** | Decision is difficult or impossible to reverse (credit denial, account closure) | Decision is easily reversible (UI personalization, notification timing) |
| **Consequence severity** | Significant financial, legal, or personal impact | Minor impact, low stakes |
| **Regulatory requirement** | Regulation requires human involvement (GDPR Art. 22, EU AI Act Art. 14) | No regulatory human-in-the-loop requirement |
| **User expectation** | Users expect to make this decision themselves | Users expect this to be automated |
| **Model uncertainty** | Model confidence is low or variable | Model confidence is consistently high |
| **Vulnerable population** | Decision disproportionately affects vulnerable groups | Uniform impact across populations |
| **Error cost asymmetry** | False positives and false negatives have very different costs | Error costs are symmetric |

### FinTech Examples by Agency Level

#### Level 1: INFORM (AI provides data, human decides)

**Use case: Portfolio risk dashboard for wealth advisors**

The AI system analyzes market conditions and portfolio composition to identify potential risks. It surfaces data and analysis. The advisor makes all investment decisions.

Product decisions:
- Display risk indicators alongside the advisor's existing workflow, not in a separate screen
- Show the underlying data that drives each risk indicator, not just the conclusion
- Allow advisors to dismiss or annotate risk alerts with reasoning
- Never auto-execute trades based on risk analysis

Why this level: Investment advice is a fiduciary obligation. The advisor bears personal liability. Regulatory frameworks (MiFID II) require the advisor to form their own opinion.

#### Level 2: SUGGEST (AI offers options, human picks)

**Use case: KYC document verification**

The AI system analyzes uploaded identity documents and suggests whether each document is valid, potentially fraudulent, or requires additional review. It presents all options to the KYC analyst.

Product decisions:
- Present AI assessment alongside the original document image, never as a standalone verdict
- Show multiple interpretations when confidence is split (e.g., "75% likely valid, 20% possibly expired, 5% potentially altered")
- Allow the analyst to select any option regardless of AI ranking
- Log the analyst's reasoning when they disagree with the AI suggestion

Why this level: Document verification has legal consequences (AML regulations). False negatives (accepting fraudulent documents) create regulatory liability. False positives (rejecting valid documents) harm customers.

#### Level 3: RECOMMEND (AI selects preferred option, human approves)

**Use case: Credit limit adjustment recommendations**

The AI system analyzes customer behavior and recommends specific credit limit increases or decreases. A loan officer reviews and approves or modifies each recommendation.

Product decisions:
- Present the recommendation with a clear rationale (key factors, confidence level)
- Provide a one-click approval path for high-confidence recommendations
- Require a justification field when the officer overrides the AI recommendation
- Track override rates as a signal for model quality and officer training needs

Why this level: Credit limit changes have financial impact but are reversible. The model has strong historical performance. Regulatory requirements can be met with human approval at the point of decision.

#### Level 4: ACT WITH REVIEW (AI acts, human can review and reverse)

**Use case: Real-time fraud transaction blocking**

The AI system evaluates transactions in real-time and blocks those it classifies as fraudulent. Fraud analysts review blocked transactions and can release legitimate ones.

Product decisions:
- Block transactions immediately (speed is essential for fraud prevention)
- Notify the customer that a transaction has been held for review
- Provide a self-service channel for customers to confirm legitimate transactions
- Staff the review queue to ensure blocked transactions are reviewed within 30 minutes
- Escalate automatically if the review SLA is at risk

Why this level: Fraud prevention requires sub-second decisions. The cost of not blocking (actual fraud loss) exceeds the cost of temporary blocking (customer inconvenience). Customers can quickly unblock legitimate transactions.

#### Level 5: FULL AUTONOMY (AI acts, no human review)

**Use case: Chatbot routing of general inquiries**

The AI system classifies incoming customer inquiries and routes them to the appropriate service queue. No human reviews the routing decision.

Product decisions:
- Provide a "this isn't right" escape hatch so customers can redirect themselves
- Monitor routing accuracy through downstream resolution metrics
- Set confidence thresholds below which the system defaults to a human triage agent
- Never route complaints, escalations, or vulnerability indicators without human review

Why this level: Routing is low-stakes, easily reversible, and high-volume. The cost of human review exceeds the cost of occasional misrouting. Customer self-correction provides an effective feedback loop.

### Governance Implications of Agency Decisions

Document your agency decisions in the Responsible Product Brief. For each AI capability, record:

| AI Capability | Agency Level | Regulatory Basis | Override Mechanism | Monitoring |
|---------------|-------------|------------------|-------------------|------------|
| [Feature] | [Level 1-5] | [Applicable regulation] | [How users override] | [How you measure agency effectiveness] |

---

## 2. Mental Model Alignment: How Users Understand AI

### The PAIR Principle

Users interact with AI based on their mental model of how the system works. If their mental model is wrong, they will misuse the system even when it functions correctly. A loan officer who believes the AI "knows everything about the applicant" will defer too readily. A customer who believes the chatbot "is just a search engine" will not trust its calculations.

Product Managers must design the product to build accurate mental models, not just correct ones. The goal is not to teach users how neural networks function. The goal is to ensure users understand what the system can do, what it cannot do, and when it might be wrong.

### Mental Model Design Decisions

#### 2.1 Capability Communication

| Decision | Pattern | Anti-Pattern |
|----------|---------|-------------|
| **What does the AI do?** | "This tool analyzes your transaction history to suggest a monthly budget" | "AI-powered budgeting" (vague, overpromising) |
| **What does the AI NOT do?** | "This tool does not predict future income or account for irregular expenses" | Omitting limitations (users discover them through failure) |
| **What data does it use?** | "Based on your last 12 months of transactions in this account" | "Based on your financial profile" (unclear scope) |
| **How confident is it?** | "This recommendation is based on strong historical patterns" vs. "This is an initial estimate that may change with more data" | Presenting all outputs with equal confidence |

#### 2.2 FinTech Examples of Mental Model Misalignment

**Dangerous mental model: "The AI approved my loan, so I can afford it."**

Reality: The AI assessed creditworthiness based on the bank's risk appetite, not the applicant's personal financial wellbeing. An approved loan may still be unaffordable.

Product response: Include affordability indicators alongside the approval decision. Display monthly payment as a percentage of income. Show total interest cost over the loan term. Use language that separates "eligible" from "affordable."

**Dangerous mental model: "The fraud alert means my account has been compromised."**

Reality: Fraud alerts are probabilistic. Most are false positives triggered by unusual-but-legitimate behavior (traveling, large purchase, new merchant).

Product response: Use graded language ("We noticed an unusual transaction and want to confirm it's yours" instead of "Fraud detected on your account"). Provide easy self-service confirmation. Show the specific transaction in question so the customer can quickly assess it.

**Dangerous mental model: "The chatbot gave me investment advice."**

Reality: The chatbot provided general information, not personalized advice. Regulatory frameworks (MiFID II) distinguish sharply between information and advice.

Product response: Include persistent disclaimers that are contextual, not boilerplate. When the conversation approaches advice-like territory, redirect to a licensed advisor. Log conversations that cross the information-advice boundary for compliance review.

### 2.3 Mental Model Alignment Checklist

Use this checklist during design reviews:

- [ ] The product communicates what the AI does in concrete, specific terms
- [ ] The product communicates what the AI does not do (stated limitations)
- [ ] Users can discover what data the AI uses for its outputs
- [ ] Confidence or uncertainty is communicated when it varies meaningfully
- [ ] First-time users receive onboarding that sets accurate expectations
- [ ] The product does not use anthropomorphic language that implies understanding or judgment (e.g., "the AI thinks," "the AI believes")
- [ ] Error states are described in terms of what went wrong, not just that something went wrong
- [ ] Users from the target population have been tested for mental model accuracy

---

## 3. Calibrated Trust: Avoiding Over-Reliance and Under-Trust

### The PAIR Principle

Trust calibration is the degree to which a user's trust in the AI matches the AI's actual reliability. Both over-trust and under-trust cause harm:

- **Over-trust (automation bias):** Users accept AI outputs without scrutiny, even when wrong. In FinTech, this leads to approving loans the model should not have approved, missing fraud the model missed, or accepting chatbot answers that are incorrect.
- **Under-trust (automation aversion):** Users ignore AI outputs even when correct. This wastes the system's value and creates inconsistency (some users trust the AI, others do not, producing unequal outcomes).

### Trust Calibration Strategies

#### 3.1 Provide Calibration Information

| Strategy | Implementation | FinTech Example |
|----------|---------------|-----------------|
| **Show confidence levels** | Display model confidence alongside each output | Fraud score shown as a percentage with color coding: green (>90% legitimate), yellow (60-90%), red (<60% legitimate) |
| **Show historical accuracy** | Display the model's track record for similar cases | "For applicants with similar profiles, this model's approval recommendations have been correct 94% of the time" |
| **Show disagreement signals** | Highlight when multiple models or data sources disagree | "Our primary model recommends approval, but the affordability check flags a concern. Review recommended." |
| **Show edge case warnings** | Alert users when the current case is unusual for the model | "This applicant's profile differs significantly from the model's training data. Treat the recommendation with additional caution." |

#### 3.2 Design Against Over-Reliance

| Pattern | Description | FinTech Application |
|---------|-------------|---------------------|
| **Friction for high-stakes decisions** | Require deliberate confirmation for consequential actions | Before approving a large credit limit increase, require the officer to review and acknowledge three key risk factors |
| **Periodic manual cases** | Route some decisions to manual review regardless of AI confidence | Route 5% of AI-approved transactions for manual review to keep analysts' skills calibrated |
| **Disagreement tracking** | Monitor override rates and investigate when they drop too low | If loan officers override less than 2% of AI recommendations, investigate whether automation bias has set in |
| **Rotation and freshness** | Periodically change how AI outputs are presented | Vary the order of displayed factors so reviewers do not develop pattern-matching shortcuts |

#### 3.3 Design Against Under-Trust

| Pattern | Description | FinTech Application |
|---------|-------------|---------------------|
| **Show your work** | Provide explanations alongside AI outputs | Display the top three factors driving a credit recommendation so the officer understands the reasoning |
| **Incremental exposure** | Start with low-stakes suggestions and build trust over time | Introduce the fraud detection AI in advisory mode before enabling automatic blocking |
| **Peer comparison** | Show how other users (in aggregate) respond to similar AI outputs | "Loan officers approve 91% of applications that receive this recommendation" |
| **Feedback loops** | Let users see the outcome of following vs. ignoring AI recommendations | Monthly reports showing default rates for AI-approved vs. officer-overridden loans |

### 3.4 Trust Calibration Monitoring

Track these metrics to assess trust calibration across your user base:

| Metric | What It Measures | Target Range | Red Flag |
|--------|-----------------|--------------|----------|
| **Override rate** | % of AI recommendations changed by human | 5-20% (domain-dependent) | <2% (over-trust) or >50% (under-trust) |
| **Time-on-task** | Time spent reviewing AI output before acting | Varies by complexity | Consistently <5 seconds for complex decisions (rubber-stamping) |
| **Explanation engagement** | % of users who expand/view AI explanations | >30% for high-stakes decisions | <5% (not reading explanations) |
| **Feedback submission** | % of users providing correctness feedback | >10% | <1% (disengagement) |
| **Outcome differential** | Performance difference between AI-followed and AI-overridden decisions | Small or favoring AI | Large differential favoring overrides (model quality issue) |

---

## 4. Error Recovery: How Users Correct AI Mistakes

### The PAIR Principle

Every AI system makes mistakes. The quality of the product is determined not only by how often it is correct, but by how gracefully it handles being wrong. Users must be able to detect errors, understand what went wrong, correct the outcome, and have confidence that their correction will be respected.

In FinTech, error recovery is not just a UX concern -- it is a regulatory requirement. GDPR Article 22 grants individuals the right to obtain human intervention when subject to automated decisions. The EU AI Act Article 14 requires that humans can override AI outputs. These rights are meaningless if the product makes correction difficult, confusing, or invisible.

### 4.1 Error Recovery Design Framework

| Phase | Design Question | What to Build |
|-------|----------------|---------------|
| **Detection** | How will the user know the AI made an error? | Clear outcome communication, comparison to expectations, anomaly flagging |
| **Understanding** | How will the user understand what went wrong? | Explanation of the AI's reasoning, the data it used, and the decision boundary |
| **Correction** | How will the user fix the outcome? | Override mechanisms, escalation paths, appeal processes, undo functionality |
| **Prevention** | How will the user's correction improve the system? | Feedback loops, human override as training signal, systematic error analysis |

### 4.2 FinTech Error Recovery Patterns

#### Pattern: Contested Credit Decision

**Detection:** The applicant receives a clear decision letter explaining the outcome and the primary factors. The letter includes a specific reason code (not just "insufficient creditworthiness").

**Understanding:** The applicant can request a detailed explanation through the portal. The explanation shows the top five factors, how the applicant's profile compared to approved applicants, and which specific data points drove the decision.

**Correction:** The applicant can:
1. Submit additional documentation that the model did not consider (e.g., proof of additional income)
2. Request human review by a senior underwriter
3. File a formal appeal that triggers an independent review
4. Contact the ombudsman if internal processes do not resolve the dispute

**Prevention:** All overturned decisions are logged and analyzed quarterly to identify systematic model weaknesses. If a pattern of successful appeals emerges for a specific demographic or scenario, the model is retrained or the decision boundary is adjusted.

#### Pattern: False Fraud Block

**Detection:** The customer receives an immediate SMS/push notification explaining that a transaction was held and why (merchant category, amount, location).

**Understanding:** The notification includes the specific transaction details so the customer can immediately assess whether it was legitimate.

**Correction:** The customer can:
1. Confirm the transaction as legitimate via one-tap in the notification (releases the hold)
2. Call the fraud hotline for complex cases
3. Visit a branch for in-person verification

**Prevention:** Confirmed false positives feed back into the model. Customer-level patterns (e.g., "this customer frequently shops at this merchant") are incorporated to reduce future false positives for that customer.

#### Pattern: Chatbot Misinformation

**Detection:** The chatbot provides a confidence indicator with each response. Responses below a confidence threshold include the caveat: "I am not fully confident in this answer. Would you like me to connect you with a specialist?"

**Understanding:** The chatbot can explain what sources it used to generate the response and whether the question was similar to questions it has answered reliably before.

**Correction:** The customer can:
1. Rate the response as unhelpful or incorrect
2. Request escalation to a human agent at any point in the conversation
3. Flag specific statements as inaccurate

**Prevention:** Flagged responses trigger human review. Patterns of incorrect responses on specific topics trigger retraining or content updates. Escalation topics are analyzed to identify capability gaps.

### 4.3 Error Recovery Checklist

Use this checklist to assess whether your AI product has adequate error recovery:

- [ ] Users can identify when the AI has made an error (output is clear and specific enough to evaluate)
- [ ] Users can access an explanation of the AI's reasoning for any given output
- [ ] Users can override or reverse the AI's output through a clearly marked mechanism
- [ ] The override/reversal mechanism is no more than two clicks/taps from the AI output
- [ ] Users can escalate to a human decision-maker when they cannot resolve the error through self-service
- [ ] The escalation path has a defined SLA for response time
- [ ] User corrections are logged and analyzed for systematic error patterns
- [ ] Correction data feeds back into model improvement processes
- [ ] Error recovery processes are tested with users from vulnerable populations
- [ ] The error recovery process is documented in regulatory filings (DPIA, transparency documentation)

---

## 5. Applying PAIR Patterns to Your Product

### Quick-Reference Decision Matrix

When designing an AI feature, use this matrix to identify which PAIR patterns are most critical.

| Product Characteristic | Primary PAIR Focus | Secondary Focus |
|----------------------|-------------------|-----------------|
| AI makes consequential decisions about people | User Agency (Level 1-3), Error Recovery | Calibrated Trust |
| AI provides recommendations that humans act on | Calibrated Trust, Mental Model Alignment | User Agency |
| AI acts autonomously on behalf of users | Error Recovery, User Agency (Level 4-5) | Mental Model Alignment |
| AI generates content or communications | Mental Model Alignment, Error Recovery | Calibrated Trust |
| AI processes sensitive personal data | User Agency, Mental Model Alignment | Error Recovery |
| AI interacts directly with customers (chatbot) | Mental Model Alignment, Calibrated Trust | Error Recovery |

### Integration with Governance Artifacts

Document your PAIR decisions in the following governance artifacts:

| PAIR Theme | Governance Artifact | Section |
|------------|-------------------|---------|
| User Agency | [Responsible Product Brief](../templates/responsible-product-brief.md) | Section 5: Human Oversight Design |
| Mental Model Alignment | [UX Governance Add-on](../governance-extensions/ux-governance-addon.md) | Section 2: Transparency UX |
| Calibrated Trust | [Defining Acceptance Criteria](../evaluations/defining-acceptance-criteria.md) | Trust calibration metrics |
| Error Recovery | [UX Governance Add-on](../governance-extensions/ux-governance-addon.md) | Section 4: Error Recovery UX |

---

## Related Documents

| Document | Location |
|----------|----------|
| Responsible Product Brief | [responsible-product-brief.md](../templates/responsible-product-brief.md) |
| UX Governance Add-on | [ux-governance-addon.md](../governance-extensions/ux-governance-addon.md) |
| Stakeholder Value Map | [stakeholder-value-map.md](../templates/stakeholder-value-map.md) |
| Defining Acceptance Criteria | [defining-acceptance-criteria.md](../evaluations/defining-acceptance-criteria.md) |
| PRD Governance Add-on | [prd-governance-addon.md](../governance-extensions/prd-governance-addon.md) |
| Integrating Thoughtworks Playbook | [integrating-thoughtworks-playbook.md](./integrating-thoughtworks-playbook.md) |
| Ethical Discovery Workshop | [ethical-discovery-workshop.md](../governance-extensions/ethical-discovery-workshop.md) |

---

*Last updated: 2026-03-01*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
*Framework: [Product Governance for Agentic AI Workflows](../../README.md)*
