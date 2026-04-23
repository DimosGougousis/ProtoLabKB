# Ethical Discovery Workshop

## Purpose

This document provides a facilitation guide for running a structured ethics workshop during the discovery phase of AI product development. The workshop brings cross-functional stakeholders together to systematically identify ethical risks, map stakeholder impacts, and document mitigations before any code is written. In regulated FinTech, ethical risk identification at the discovery stage prevents costly late-stage redesigns and regulatory objections.

The workshop format is inspired by the Ethical OS toolkit, adapted for the specific concerns of financial services AI: algorithmic discrimination, creditworthiness assessment bias, and the amplification of existing financial inequalities.

## When to Use

- During the discovery phase of any AI-powered product or feature, after the initial problem definition but before PRD finalization
- When a new AI use case is being evaluated for feasibility and desirability
- When expanding an existing AI system to new populations, geographies, or decision types
- When a regulatory or compliance review identifies ethical concerns that need structured exploration
- Annually, as a refresh exercise for AI systems already in production

**Trigger:** A product team begins discovery for an AI-powered product or feature and needs to assess ethical risks with cross-functional input.

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **Ethics Lead** | **Responsible** -- facilitates the workshop, prepares materials, documents findings |
| **Product Manager** | **Accountable** -- ensures the workshop happens and findings are incorporated into the PRD |
| **AI/ML Engineer** | **Participant** -- provides technical context on AI capabilities and limitations |
| **UX Designer** | **Participant** -- represents the user perspective and interaction design implications |
| **Compliance Officer (2nd Line)** | **Participant** -- identifies regulatory constraints and precedents |
| **Customer-Facing Staff** | **Participant** -- brings real-world customer context (complaints, edge cases, vulnerabilities) |
| **Data Protection Officer** | **Consulted** -- reviews data ethics findings post-workshop |
| **AI Governance Committee** | **Informed** -- receives workshop findings as input to Discovery Gate review |

## Regulatory Basis

- **EU AI Act Article 9(2)(a)** -- Risk management must include identification and analysis of known and foreseeable risks, which this workshop systematically surfaces
- **EU AI Act Article 27** -- Fundamental Rights Impact Assessment for high-risk AI systems requires structured stakeholder impact analysis
- **SAFEST E-01** -- Ethical framework must be defined and applied during AI system development
- **SAFEST E-09** -- Assessment of potential for manipulation or exploitation of vulnerable users
- **SAFEST E-12** -- Fundamental rights impact assessment (contributes evidence)
- **SAFEST F-01** -- Identification of protected characteristics and potential discrimination vectors
- **DNB Good Practice** -- Expectation that AI governance includes ethical risk assessment at the design stage

---

## Workshop Overview

| Attribute | Details |
|-----------|---------|
| **Duration** | 2 hours (strictly timeboxed) |
| **Participants** | 5-8 people (cross-functional, see RACI above) |
| **Facilitator** | Ethics Lead (or designated governance champion) |
| **Preparation** | 30 minutes facilitator prep + pre-read distribution (1 day before) |
| **Output** | Ethical Discovery Workshop Findings Report (template in Section 7) |

### Pre-Workshop Preparation

**Facilitator tasks (1 day before):**

1. Distribute the product concept brief or draft PRD to all participants
2. Distribute the "Pre-Workshop Primer" (Section 1 below) for 15-minute pre-read
3. Prepare the workshop room (physical or virtual) with collaborative workspace (whiteboard, Miro, FigJam)
4. Print or share the exercise templates from Sections 3-5
5. Identify 2-3 real-world examples of AI ethical failures relevant to the use case (see Section 2)

**Participant tasks (before workshop):**

1. Read the product concept brief or draft PRD (15 minutes)
2. Read the Pre-Workshop Primer (15 minutes)
3. Think about one person they know personally who might be affected by this system

---

## Section 1: Pre-Workshop Primer (Distribute Before Workshop)

Share this primer with participants 1 day before the workshop.

### What This Workshop Is

This is a structured exercise to identify who might be harmed by the proposed AI system and how. It is not a debate about whether to build the system -- that is a separate decision. The goal is to surface risks that can be mitigated, constraints that must be respected, and scenarios that must be tested.

### Key Concepts for the Workshop

| Concept | Definition | Example in FinTech |
|---------|-----------|-------------------|
| **Affected population** | Anyone impacted by the AI system's decisions, including non-users | A person denied credit by an AI they never interacted with directly |
| **Proxy discrimination** | Using a neutral feature that correlates with a protected characteristic | Using postcode as a feature that correlates with ethnicity |
| **Feedback loop** | When AI decisions create data that reinforces future decisions | Denying credit to a group reduces their credit history, leading to more denials |
| **Automation bias** | Human operators over-relying on AI recommendations | A fraud analyst approving every AI flag without independent review |
| **Asymmetric impact** | When errors affect different groups differently | False fraud flags disproportionately affecting international transfer users |

### One Question to Bring

> "Who is the person who is most harmed if this system makes a mistake, and what does their day look like after that mistake?"

---

## Section 2: Workshop Agenda

| Time | Duration | Activity | Section |
|------|----------|----------|---------|
| 0:00 | 10 min | **Opening: Context and Ground Rules** | Section 2.1 |
| 0:10 | 25 min | **Exercise 1: Stakeholder Impact Mapping** | Section 3 |
| 0:35 | 5 min | Break | |
| 0:40 | 30 min | **Exercise 2: Ethical Risk Brainstorming** | Section 4 |
| 1:10 | 5 min | Break | |
| 1:15 | 25 min | **Exercise 3: "Who Gets Harmed?" Deep Dive** | Section 5 |
| 1:40 | 15 min | **Synthesis and Prioritization** | Section 6 |
| 1:55 | 5 min | **Close: Next Steps and Commitments** | Section 6.3 |

### 2.1 Opening: Context and Ground Rules (10 minutes)

**Facilitator script:**

> "We are here to stress-test the ethical profile of [product name]. Our goal is not to decide whether to build it, but to identify risks we must address if we do. There are no wrong answers. We want dissent -- the person who raises an uncomfortable scenario is the most valuable person in this room."

**Ground rules:**

1. No dismissing concerns with "that won't happen" -- document everything, evaluate probability later
2. Speak from the perspective of affected people, not the organization
3. Regulatory constraints are facts, not opinions -- compliance input is not negotiable
4. The output of this workshop is binding on the PRD -- identified risks require documented mitigations
5. Timebox discipline: facilitator will enforce time limits to cover all exercises

### 2.2 Real-World Examples (2-3 minutes within opening)

Present 1-2 brief examples of AI ethical failures relevant to the use case domain. Use these to calibrate the group on the types of risks that actually materialize.

**Example set for common FinTech use cases:**

| Use Case Domain | Real-World Ethical Failure | What Went Wrong |
|----------------|--------------------------|-----------------|
| Credit scoring | Apple Card gender bias (2019): spouses with identical financial profiles received dramatically different credit limits | The model used features that correlated with gender without explicit gender input |
| Fraud detection | Legitimate transactions by immigrant communities flagged at disproportionate rates due to international transfer patterns | Training data underrepresented these transaction patterns, treating normal behavior as anomalous |
| Collections | Automated debt collection messages sent at vulnerable times (late night, weekends) increasing psychological distress | System optimized for contact rate without considering debtor well-being |
| Customer service AI | AI chatbot providing incorrect financial advice that users relied upon for investment decisions | No guardrails on the scope of advice the AI could give; no disclaimers |
| AML screening | Name-matching algorithms producing excessive false positives for common names in certain ethnicities | String-matching bias compounded by limited training data diversity |

---

## Section 3: Exercise 1 -- Stakeholder Impact Mapping (25 minutes)

### 3.1 Instructions

1. **Identify all stakeholders** affected by the proposed AI system (5 minutes, individual brainstorming)
2. **Map each stakeholder** on the Impact Grid below (10 minutes, group discussion)
3. **Identify imbalances** -- groups that bear high risk with low benefit (10 minutes, group discussion)

### 3.2 Stakeholder Identification Prompts

Ask participants to identify people in these categories:

| Category | Prompt | Examples in FinTech |
|----------|--------|-------------------|
| **Direct users** | Who interacts with the AI system directly? | App users, customer service callers |
| **Decision subjects** | Who is the subject of an AI-driven decision? | Loan applicants, fraud investigation targets |
| **Data subjects** | Whose data does the AI use? | Account holders, transaction counterparties |
| **Downstream affected** | Who is affected by the AI's decisions indirectly? | Family members of denied loan applicants, merchants of flagged transactions |
| **System operators** | Who operates or oversees the AI? | Fraud analysts, customer service supervisors |
| **Bystanders** | Who may be affected without any interaction? | Competitors' customers if AI creates market distortion |

### 3.3 Impact Grid

For each stakeholder group, map their position:

```
                    HIGH BENEFIT
                         |
                         |
    Allies               |              Winners
    (Benefit from AI,    |              (Benefit from AI,
     low risk to them)   |               low risk to them)
                         |
  LOW RISK ──────────────┼────────────── HIGH RISK
                         |
    Bystanders           |              Vulnerable
    (Low benefit,        |              (Low benefit,
     low risk)           |               HIGH risk)
                         |
                    LOW BENEFIT
```

**Critical governance finding:** Any stakeholder group that falls in the "Vulnerable" quadrant (high risk, low benefit) requires explicit justification and mitigation in the PRD. If no justification exists, the product concept must be redesigned.

### 3.4 Stakeholder Impact Documentation Template

| Stakeholder Group | Benefit | Risk | Quadrant | Mitigation Required? |
|-------------------|---------|------|----------|---------------------|
| [FILL IN] | [Describe benefit] | [Describe risk] | [Winners/Allies/Bystanders/Vulnerable] | [Yes/No] |

---

## Section 4: Exercise 2 -- Ethical Risk Brainstorming (30 minutes)

### 4.1 Risk Zone Exploration

Adapted from the Ethical OS Risk Zones. For each zone, brainstorm risks specific to the proposed AI system. Timebox: 3 minutes per zone, facilitator rotates.

| Zone | Prompt | FinTech-Specific Considerations |
|------|--------|-------------------------------|
| **1. Truth and Disinformation** | Could this AI generate, amplify, or fail to detect false information? | Financial advice accuracy, hallucinated account balances, fabricated regulatory citations |
| **2. Economic Inequality** | Could this AI widen economic gaps between groups? | Credit access disparities, fee optimization that penalizes low-balance accounts, wealth-biased recommendations |
| **3. Addiction and Manipulation** | Could this AI create compulsive behaviors or manipulate decisions? | Gamified spending challenges, urgency-driven product offers, emotional manipulation in financial distress |
| **4. Surveillance and Privacy** | Could this AI enable excessive monitoring or data exploitation? | Transaction pattern profiling beyond stated purposes, behavioral scoring from app usage patterns |
| **5. Data Control and Consent** | Who controls the data the AI uses, and is consent meaningful? | Third-party data enrichment without user awareness, model training on historical data collected under different consent |
| **6. Exclusion and Power** | Could this AI exclude people from services or concentrate decision power? | Digital literacy barriers, language exclusion, automated gatekeeping of financial services |
| **7. Algorithmic Bias** | Could this AI discriminate based on protected characteristics, directly or through proxies? | Proxy discrimination in credit scoring, geographic bias in fraud detection, age bias in risk models |
| **8. Trust Erosion** | Could this AI damage trust in the organization or financial system? | Unexplainable decisions, inconsistent outcomes for similar cases, loss of human accountability |

### 4.2 Risk Brainstorming Template

For each identified risk, document using this structure:

| Field | Value |
|-------|-------|
| **Risk zone** | [Zone number and name] |
| **Risk description** | [One sentence: what could go wrong] |
| **Who is harmed** | [Specific stakeholder group(s)] |
| **Severity** | [Low / Medium / High / Critical] |
| **Likelihood** | [Low / Medium / High] |
| **Detectability** | [How would we know if this happened?] |
| **Existing precedent** | [Has this happened elsewhere? Reference if known] |
| **Potential mitigation** | [Initial ideas -- will be refined after workshop] |

---

## Section 5: Exercise 3 -- "Who Gets Harmed?" Deep Dive (25 minutes)

### 5.1 Instructions

Select the top 3 risks from Exercise 2 (by combined severity and likelihood). For each, run the "Who Gets Harmed?" analysis below.

### 5.2 Harm Chain Analysis

For each selected risk, trace the chain from AI action to human harm:

```
AI Action → Immediate Effect → Who Notices → Who Is Affected → What Harm → How Severe → How Reversible
```

**Worked example -- Credit scoring bias:**

```
AI Action:          Credit model weights postcode heavily
Immediate Effect:   Applicants from certain postcodes receive lower scores
Who Notices:        Applicants see denial; analysts may not see the pattern
Who Is Affected:    Residents of historically underserved neighborhoods (correlated with ethnicity)
What Harm:          Denied access to credit; reinforces financial exclusion
How Severe:         High -- affects housing, education, business opportunities
How Reversible:     Low -- denied applicants build no credit history, compounding future denials
```

**Worked example -- Fraud detection false positives:**

```
AI Action:          Fraud model flags international transfers as high-risk
Immediate Effect:   Transactions blocked or delayed for review
Who Notices:        Sender's transaction fails; recipient does not receive funds
Who Is Affected:    Immigrant communities sending remittances; international merchants
What Harm:          Financial disruption, delayed essential payments, emotional distress
How Severe:         Medium-High -- may affect rent payments, family support
How Reversible:     Medium -- can be unblocked, but delay damage is done
```

### 5.3 Harm Chain Documentation Template

| Step | Risk 1: [Name] | Risk 2: [Name] | Risk 3: [Name] |
|------|----------------|----------------|----------------|
| AI Action | | | |
| Immediate Effect | | | |
| Who Notices | | | |
| Who Is Affected | | | |
| What Harm | | | |
| How Severe | | | |
| How Reversible | | | |
| Proposed Mitigation | | | |
| Eval to Detect | | | |

### 5.4 Feedback Loop Assessment

For each harm chain, assess whether a feedback loop could amplify the harm over time:

| Question | Risk 1 | Risk 2 | Risk 3 |
|----------|--------|--------|--------|
| Does the AI's decision create data that influences future decisions? | | | |
| Could the harm compound over repeated interactions? | | | |
| Is there a mechanism to break the feedback loop? | | | |
| What monitoring would detect the loop forming? | | | |

---

## Section 6: Synthesis and Prioritization (15 minutes)

### 6.1 Risk Prioritization Matrix

Consolidate all identified risks and prioritize:

| Risk ID | Description | Severity | Likelihood | Risk Score | Mitigation Status | Owner |
|---------|-------------|----------|------------|------------|-------------------|-------|
| ETH-001 | [From Exercise 2] | [H/M/L] | [H/M/L] | [S x L] | [Identified / Designed / Tested / None] | [Role] |

### 6.2 Governance Commitments

Based on the workshop findings, document commitments that flow into the PRD:

| Commitment | How It Affects the PRD | Deadline |
|------------|----------------------|----------|
| [e.g., "Postcode must not be a direct model feature"] | Add to acceptance criteria: fairness parity across geographic regions | Before PRD sign-off |
| [e.g., "False positive rates must be equal across nationality groups"] | Add fairness metric to eval suite: FPR parity within 2% | Before development |
| [e.g., "Users must be able to appeal any automated credit decision"] | Add appeal mechanism to UX requirements | Before design sign-off |

### 6.3 Close: Next Steps

| Action | Owner | Deadline |
|--------|-------|----------|
| Compile workshop findings into the Findings Report (Section 7 template) | Ethics Lead | 2 business days after workshop |
| Incorporate commitments into the PRD | Product Manager | Before PRD review |
| Add identified fairness metrics to the evaluation strategy | AI/ML Engineer | Before development sprint planning |
| Review findings with DPO for data ethics implications | Ethics Lead | 1 week after workshop |
| Present findings at AI Governance Committee (for Limited/High-risk) | Product Manager | Next scheduled Committee meeting |

---

## Section 7: Workshop Findings Report Template

```markdown
# Ethical Discovery Workshop Findings

## Workshop Metadata
- **Product/Feature:** [FILL IN]
- **Date:** [FILL IN]
- **Facilitator:** [FILL IN]
- **Participants:** [List names and roles]
- **Duration:** [FILL IN]

## Risk Classification
- **EU AI Act Risk Tier:** [Minimal / Limited / High]
- **Primary ethical risk zones:** [List top 3 zones from Exercise 2]

## Stakeholder Impact Summary
[Summarize Impact Grid findings. Highlight any "Vulnerable" quadrant stakeholders.]

## Top Risks Identified
[List top 5-7 risks with severity, likelihood, and proposed mitigations]

## Harm Chain Analysis
[Include completed harm chains for top 3 risks from Exercise 3]

## Feedback Loop Risks
[Document any identified feedback loops and proposed circuit-breakers]

## Governance Commitments
[List all commitments from Section 6.2]

## Unresolved Questions
[List any questions the workshop raised but could not answer]

## Next Steps
[From Section 6.3]

## Sign-Off
| Role | Name | Date |
|------|------|------|
| Ethics Lead (Facilitator) | | |
| Product Manager | | |
```

---

## Cross-References

| Topic | Artifact | Location |
|-------|----------|----------|
| PRD governance questions | PRD Governance Add-on | [governance-extensions/prd-governance-addon.md](prd-governance-addon.md) |
| UX governance checklist | UX Governance Add-on | [governance-extensions/ux-governance-addon.md](ux-governance-addon.md) |
| Ethics impact assessment template | AI Ethics Impact Assessment | [templates/ai-ethics-impact-assessment.md](../templates/ai-ethics-impact-assessment.md) |
| Ethical product discovery checklist | Ethical Product Discovery | [checklists/ethical-product-discovery.yaml](../checklists/ethical-product-discovery.yaml) |
| Affected population analysis | PRD Governance Add-on Section 2 | [governance-extensions/prd-governance-addon.md](prd-governance-addon.md#section-2-affected-population-analysis-for-user-research) |
| Stakeholder value mapping | Stakeholder Value Map | [templates/stakeholder-value-map.md](../templates/stakeholder-value-map.md) |
| Bias and fairness evaluations | Bias and Fairness Evals | [bias-and-fairness-evals.md](../../02-development-governance/evaluations/bias-and-fairness-evals.md) |
| Bias testing checklist | Bias Testing Checklist | [bias-testing-checklist.yaml](../../02-development-governance/checklists/bias-testing-checklist.yaml) |
| SAFEST Fairness pillar | SAFEST Checklist Detailed | [safest-checklist-detailed.md](../../04-operational-governance/regulatory/safest-checklist-detailed.md) |

---

*Last updated: 2026-03-01*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
*Framework: [Product Governance for Agentic AI Workflows](../../README.md)*
