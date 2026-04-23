# Integrating the Thoughtworks Responsible Tech Playbook

> **Pillar:** Discovery Governance
> **Purpose:** Practical guide for applying Thoughtworks Responsible Tech tools during AI product discovery in regulated FinTech environments.
> **Cross-references:** [Ethical Discovery Workshop](../governance-extensions/ethical-discovery-workshop.md) | [Bias Assessment Report Template](../../02-development-governance/templates/bias-assessment-report.md)

---

## 1. Overview of the Thoughtworks Responsible Tech Playbook

The Thoughtworks Responsible Tech Playbook is a collection of tools, activities, and frameworks designed to help product teams identify and mitigate potential harms before they are built into technology. Unlike compliance checklists applied after development, these tools are designed to operate at the earliest stages of product ideation and discovery.

For FinTech organizations building AI-driven products (credit decisioning, fraud detection, customer service agents, trading recommendations), early-stage harm identification is not optional. Regulatory bodies including the FCA, OCC, CFPB, and EBA increasingly expect institutions to demonstrate that they considered fairness, transparency, and consumer protection before deployment, not merely after.

### Core Principles

The playbook operates on several principles that align with this governance framework:

- **Proactive over reactive.** Identify potential harms before writing code, not after complaints arrive.
- **Inclusive deliberation.** Bring diverse perspectives into the room: product, engineering, legal, compliance, risk, and affected community representatives.
- **Structured activities over informal discussion.** Use repeatable, documented processes that produce governance artifacts.
- **Continuous reassessment.** Revisit conclusions as the product evolves.

### Tools Covered in This Guide

| Tool | Purpose | Best Used During |
|------|---------|------------------|
| Targeting Prospectus | Map who is affected by the AI system | Early discovery, before requirements |
| Ethical OS Toolkit | Identify risk zones and potential harms | Discovery and design phases |
| Consequence Scanning | Structured team activity for harm analysis | Sprint planning, design reviews |

---

## 2. Targeting Prospectus: Mapping Who Is Affected

### What It Is

The Targeting Prospectus is a structured exercise that maps all groups who could be affected by an AI system, including those who are not direct users. Traditional product discovery focuses on users and customers. The Targeting Prospectus expands the lens to include indirect stakeholders, vulnerable populations, and communities.

### How to Conduct a Targeting Prospectus

**Step 1: Identify direct users and beneficiaries.**

List every person or group who will directly interact with or benefit from the AI system. For a credit decisioning model, this includes loan applicants, loan officers, and underwriters.

**Step 2: Identify indirect stakeholders.**

List groups who do not use the system but are affected by its outputs. For credit decisioning, this includes rejected applicants' families, communities with reduced credit access, and competing lenders whose practices may be disrupted.

**Step 3: Identify vulnerable populations.**

Explicitly name groups who may be disproportionately affected due to existing disadvantages. In FinTech, this includes historically redlined communities, gig economy workers with non-traditional income, recent immigrants with thin credit files, and elderly customers unfamiliar with digital interfaces.

**Step 4: Map power dynamics.**

For each group, document their ability to understand, contest, or opt out of the AI system's decisions. A wealthy applicant who is denied credit can hire a lawyer. A low-income applicant may not know they have the right to an explanation.

**Step 5: Document the prospectus.**

Produce a written artifact that lists all identified groups, their relationship to the system, their vulnerability level, and their power to respond. This artifact feeds into the [Ethical Discovery Workshop](../governance-extensions/ethical-discovery-workshop.md).

### Targeting Prospectus Output Template

```
System Name: [AI system under analysis]
Date: [Date of analysis]
Participants: [Names and roles]

| Group | Relationship | Vulnerability Level | Power to Respond | Notes |
|-------|-------------|---------------------|-------------------|-------|
| [Group] | Direct user / Indirect / Community | Low / Medium / High | High / Medium / Low | [Context] |
```

### FinTech Application: Responsible Lending AI

When building an AI-powered lending product, the Targeting Prospectus reveals groups that traditional product discovery misses:

- **Thin-file applicants** who lack conventional credit history but may be creditworthy.
- **Small business owners** whose personal and business finances are entangled.
- **Joint applicants** where one party may be financially coerced.
- **Communities** where the lending model's aggregate decisions could constitute geographic discrimination (digital redlining).

---

## 3. Ethical OS Toolkit: Risk Zones for AI Harm

### What It Is

The Ethical OS Toolkit provides a set of risk zones that help teams systematically consider categories of harm that technology can cause. Rather than asking teams to brainstorm harms from scratch, it provides structured categories to evaluate against.

### The Eight Risk Zones Applied to AI

| Risk Zone | AI-Specific Concerns |
|-----------|---------------------|
| 1. Truth, Disinformation, Propaganda | LLM hallucination in customer communications; fabricated financial data |
| 2. Addiction and Dopamine Economy | Gamified trading interfaces; AI-driven engagement that encourages over-trading |
| 3. Economic and Asset Inequality | Credit models that systematically disadvantage low-income applicants |
| 4. Machine Ethics and Algorithmic Bias | Discrimination in automated decisioning; proxy variables for protected characteristics |
| 5. Surveillance State | Excessive data collection for fraud detection; behavioral monitoring without consent |
| 6. Data Control and Monetization | Use of customer data beyond stated purposes; selling insights derived from financial behavior |
| 7. Implicit Trust and User Understanding | Customers not understanding that AI made their credit decision; opacity of automated processes |
| 8. Hateful and Criminal Actors | Adversarial attacks on fraud models; exploitation of AI customer service for social engineering |

### How to Use the Risk Zones

**For each risk zone, ask three questions:**

1. **Does our AI system create or amplify risks in this zone?** Be specific about mechanisms.
2. **Who is most affected?** Cross-reference with the Targeting Prospectus.
3. **What would a news headline look like if this risk materialized?** This surfaces reputational and regulatory consequences.

**Document findings per zone.** Not every zone will be relevant to every system. Document both relevant zones and the reasoning for zones deemed not applicable.

### FinTech Application: Ethical Fraud Detection

Fraud detection AI operates at the intersection of several risk zones:

- **Surveillance (Zone 5):** Transaction monitoring collects extensive behavioral data. Governance must define retention limits and purpose restrictions.
- **Algorithmic Bias (Zone 4):** Fraud models can develop higher false-positive rates for certain demographics, effectively denying service to legitimate customers from specific backgrounds.
- **Implicit Trust (Zone 7):** When a fraud model blocks a transaction, the customer often receives no meaningful explanation. Governance must define minimum explanation standards.

---

## 4. Consequence Scanning: Structured Team Activity

### What It Is

Consequence scanning is a facilitated activity where the team collectively examines the intended and unintended consequences of a product decision, feature, or AI system. It produces documented assessments that become governance artifacts.

### Running a Consequence Scan

**Duration:** 60-90 minutes per feature or system component.
**Participants:** Product owner, tech lead, designer, compliance representative, domain expert.
**Materials:** Targeting Prospectus (completed), feature description, whiteboard or digital board.

**Step 1: State the intent (10 minutes).**

Clearly articulate what the AI system is intended to do and for whom. Write this on the board. Ensure all participants agree on the stated intent.

**Step 2: Identify intended consequences (15 minutes).**

List all the positive outcomes the system is designed to produce. Be specific: "faster credit decisions" is vague; "reduce decision time from 5 days to 30 seconds for pre-qualified applicants" is actionable.

**Step 3: Identify unintended consequences (30 minutes).**

For each intended consequence, ask: "What could go wrong? Who could be harmed? What could be misused?" Use the Ethical OS risk zones as prompts. Document every consequence raised without debating feasibility.

**Step 4: Categorize and prioritize (15 minutes).**

For each unintended consequence, assess:
- **Likelihood:** How likely is this to occur? (Low / Medium / High)
- **Severity:** If it occurs, how severe is the harm? (Low / Medium / High)
- **Detectability:** Would we know if this happened? (Easy / Hard / Invisible)

**Step 5: Decide and document (15 minutes).**

For each high-priority consequence, the team decides:
- **Accept:** The risk is within appetite. Document the reasoning.
- **Mitigate:** Define specific mitigations. Add to the backlog.
- **Redesign:** The feature needs fundamental changes before proceeding.

### Consequence Scan Output

```
Feature/System: [Name]
Date: [Date]
Participants: [Names]

| Consequence | Type | Likelihood | Severity | Detectability | Decision | Action |
|-------------|------|-----------|----------|---------------|----------|--------|
| [Description] | Intended / Unintended | L/M/H | L/M/H | Easy/Hard/Invisible | Accept/Mitigate/Redesign | [Action item] |
```

---

## 5. Integration into Sprint Ceremonies

### Sprint Planning

During sprint planning, for any story involving AI components:

1. Check whether a consequence scan has been completed for the feature area. If not, schedule one before implementation begins.
2. Review existing consequence scan outputs for relevant mitigations that need to be included in the story's acceptance criteria.
3. Include governance artifact creation in story estimates. Fairness analysis, documentation, and verification are not afterthoughts.

### Design Reviews

During design reviews for AI features:

1. Present the Targeting Prospectus alongside the design. Ask: "Have we considered all affected groups in this design?"
2. Walk through relevant Ethical OS risk zones. Ask: "Does this design create or amplify risks in any zone?"
3. Document any new concerns raised and feed them back into the consequence scan.

### Retrospectives

Include responsible tech as a retrospective topic quarterly:

1. Were consequence scans completed before implementation?
2. Did any unintended consequences materialize that were not identified?
3. Are governance artifacts being maintained as the product evolves?

### Definition of Done (AI Stories)

Add the following to the team's Definition of Done for AI-related stories:

- [ ] Consequence scan completed or confirmed current
- [ ] Targeting Prospectus reviewed for this feature
- [ ] Identified mitigations implemented or tracked in backlog
- [ ] Governance artifacts updated (see [Bias Assessment Report Template](../../02-development-governance/templates/bias-assessment-report.md))
- [ ] Verification evidence collected (see [Verification Before Deployment](../../02-development-governance/guides/verification-before-deployment.md))

---

## 6. When to Use Which Tool

### Product Lifecycle Mapping

| Phase | Primary Tool | Secondary Tool | Output |
|-------|-------------|----------------|--------|
| Ideation | Targeting Prospectus | Ethical OS Risk Zones | Stakeholder map, risk zone assessment |
| Discovery | Consequence Scanning | Targeting Prospectus | Consequence register, mitigation backlog |
| Design | Consequence Scanning | Ethical OS Risk Zones | Updated consequence register, design constraints |
| Development | — | Consequence Scan review | Verification requirements (see [Verification Guide](../../02-development-governance/guides/verification-before-deployment.md)) |
| Pre-deployment | — | All tools (review) | Final governance review artifact |
| Post-deployment | Consequence Scan (revisit) | Targeting Prospectus (update) | Updated assessments based on real-world evidence |

### Decision Guide

- **Starting a new AI product?** Begin with the Targeting Prospectus, then run a full [Ethical Discovery Workshop](../governance-extensions/ethical-discovery-workshop.md).
- **Adding AI to an existing product?** Start with a consequence scan focused on the AI component.
- **Reviewing an existing AI system?** Use Ethical OS risk zones to structure the review, then update the Targeting Prospectus.
- **Responding to a complaint or incident?** Use consequence scanning retrospectively to identify what was missed and update governance artifacts.

---

## 7. FinTech Applications

### Responsible Lending AI

| Tool | Application |
|------|-------------|
| Targeting Prospectus | Map all affected groups: applicants, rejected applicants, communities, co-signers, dependents |
| Ethical OS | Focus on Zone 3 (Economic Inequality), Zone 4 (Algorithmic Bias), Zone 7 (Implicit Trust) |
| Consequence Scanning | Scan each model feature: income estimation, risk scoring, pricing, limit setting |

### Ethical Fraud Detection

| Tool | Application |
|------|-------------|
| Targeting Prospectus | Map affected groups: flagged customers, blocked merchants, false-positive victims |
| Ethical OS | Focus on Zone 4 (Algorithmic Bias), Zone 5 (Surveillance), Zone 8 (Criminal Actors) |
| Consequence Scanning | Scan detection thresholds, blocking actions, escalation workflows |

### AI Customer Service Agents

| Tool | Application |
|------|-------------|
| Targeting Prospectus | Map affected groups: customers, vulnerable customers, agents displaced by AI, regulators |
| Ethical OS | Focus on Zone 1 (Truth/Hallucination), Zone 7 (Implicit Trust), Zone 4 (Bias) |
| Consequence Scanning | Scan agent capabilities: financial advice, complaint handling, product recommendations |

---

## 8. Governance Artifact Checklist

At the end of discovery, the following artifacts should exist and be stored in the governance repository:

- [ ] Targeting Prospectus (completed and reviewed)
- [ ] Ethical OS Risk Zone Assessment (per risk zone evaluation)
- [ ] Consequence Scan Register (all scans with decisions and actions)
- [ ] Ethics assessment summary (output from [Ethical Discovery Workshop](../governance-extensions/ethical-discovery-workshop.md))
- [ ] Identified governance requirements for development phase
- [ ] Risk register entries for identified harms (feed into [AI Vulnerability Management](../../04-operational-governance/guides/ai-vulnerability-management.md))

These artifacts serve as evidence for regulatory inquiries and internal audit. They demonstrate that the organization considered fairness, transparency, and consumer protection proactively, not reactively.

---

*Next steps: Conduct an [Ethical Discovery Workshop](../governance-extensions/ethical-discovery-workshop.md) to bring the team together around these tools, then carry governance requirements into the [Development Governance](../../02-development-governance/) phase.*
