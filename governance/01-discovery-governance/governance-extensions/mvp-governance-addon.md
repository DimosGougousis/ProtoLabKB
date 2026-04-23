# MVP Governance Add-on

## Purpose

This document defines the minimum governance requirements that must be met before an AI product enters the MVP (Minimum Viable Product) build phase. It provides governance gates, templates, and decision frameworks that balance speed-to-market with responsible AI obligations.

Building an MVP is an investment of engineering resources, data infrastructure, and organizational attention. This add-on ensures that before those resources are committed, the team has answered three critical questions: (1) Is this AI system legally permissible? (2) Have we assessed who could be harmed and how? (3) Do we have the minimum data governance controls to collect and use data responsibly?

The MVP phase is the last opportunity to course-correct cheaply. Once development begins, the cost of addressing fundamental governance issues (wrong risk classification, unethical use case, inadequate data governance) increases by an order of magnitude.

## When to Use

- After the PRD phase is complete and the product has passed the [Discovery Gate](../README.md)
- Before committing engineering resources to build an MVP
- When transitioning from concept validation (paper prototypes, design sprints) to technical validation (working code, real data)
- When a "quick experiment" or proof-of-concept is proposed that involves real user data or real AI inference

**Trigger:** The team is ready to move from concept to build. Someone says "let's build an MVP" or "let's run a quick experiment with the model."

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **Product Manager** | **Accountable** -- ensures MVP governance sign-off is obtained before build begins |
| **AI/ML Engineer** | **Responsible** -- assesses technical feasibility of governance requirements within MVP constraints |
| **Compliance Officer (2nd Line)** | **Consulted** -- validates risk classification and confirms minimum governance is adequate |
| **Data Protection Officer** | **Consulted** -- reviews data governance plan, particularly for MVP data collection |
| **Ethics Lead** | **Consulted** -- reviews ethical impact assessment before resources are committed |
| **AI Governance Committee** | **Approver** -- grants MVP build authorization for Limited and High-risk systems |

## Regulatory Basis

- **EU AI Act Article 9(2)(a)** -- Risk management must include identification and analysis of known and foreseeable risks *before deployment* (MVP with real data constitutes pre-deployment risk exposure)
- **EU AI Act Article 10** -- Data governance requirements apply to training and validation data, including MVP data
- **GDPR Article 25** -- Data protection by design and by default applies from the earliest stages of processing design
- **GDPR Article 35(1)** -- DPIA required *before* processing that is likely to result in high risk
- **DORA Article 8(4)** -- Financial entities must identify and classify ICT-supported business functions, including AI experiments
- **DNB Good Practice for AI** -- Expectation of governance proportional to risk, applied before operational use

---

## Gate 1: Risk Classification Gate

### Objective

Confirm the EU AI Act risk tier before any MVP build activity begins. This gate determines the governance intensity for the entire MVP phase and all subsequent lifecycle phases.

### Prerequisites

The following must exist before this gate can be evaluated:

1. A completed PRD or [Responsible Product Brief](../templates/responsible-product-brief.md) that passed the [Discovery Gate](../README.md)
2. A completed [EU AI Act Risk Classification Checklist](../checklists/eu-ai-act-risk-classification.yaml)
3. A documented understanding of who the affected populations are

### Risk Classification Decision

| Risk Tier | MVP Build Authorization | Conditions |
|-----------|------------------------|------------|
| **Prohibited** | NOT AUTHORIZED. Full stop. | Escalate to Compliance. The product concept must be redesigned or abandoned. |
| **High** | AUTHORIZED with full governance. | AI Governance Committee + Board-level sponsor approval required. All MVP governance artifacts (Sections 3-5 of this document) must be completed. DPIA must be initiated. |
| **Limited** | AUTHORIZED with standard governance. | AI Governance Committee approval required. MVP governance artifacts (Sections 3-5) must be completed. Transparency obligations must be addressed in MVP design. |
| **Minimal** | AUTHORIZED with streamlined governance. | Product Manager + Tech Lead approval sufficient. Abbreviated MVP governance sign-off (Section 6, fast-track version). |

### FinTech-Specific Risk Classification Guidance

Most FinTech AI use cases fall into specific Annex III categories. Use this quick reference for common FinTech applications:

| FinTech Use Case | Likely Risk Tier | Annex III Reference | Rationale |
|-----------------|-----------------|---------------------|-----------|
| Credit scoring / loan decisioning | **High** | Annex III, 5(b) | Evaluates creditworthiness of natural persons |
| Fraud detection (transaction scoring) | **High** | Annex III, 5(b) | Determines access to financial services (false declines restrict access) |
| AML suspicious activity detection | **High** | Annex III, 5(b) + 6(a) | Affects access to services; may involve law enforcement referral |
| Customer service chatbot | **Limited** | Art. 50(1) | Interacts with natural persons; must disclose AI nature |
| Insurance underwriting / pricing | **High** | Annex III, 5(b) | Evaluates risk and determines pricing for natural persons |
| Internal document processing | **Minimal** | N/A | No direct impact on natural persons' rights or access to services |
| Marketing personalization | **Limited** | Art. 50 | Interacts with natural persons; potential for manipulation concerns |
| Collections prioritization | **High** | Annex III, 5(b) | Affects natural persons' treatment regarding existing financial obligations |

> *Cross-reference:* For the full classification methodology, see the [EU AI Act Risk Classification Checklist](../checklists/eu-ai-act-risk-classification.yaml) and the [governance intensity decision tree](../guides/product-development-lifecycle.md#governance-intensity-decision-tree).

---

## Gate 2: Ethics Review Gate

### Objective

Confirm that the ethical impact of the proposed AI system has been assessed and that identified risks have documented mitigations, before committing resources to the MVP build.

### Ethics Review Scope

The ethics review at the MVP stage is not a comprehensive ethical audit (that comes at the [Pre-Deployment Gate](../../02-development-governance/checklists/pre-deployment-gate.yaml)). It is a focused assessment of whether the fundamental ethical profile of the system is acceptable.

### Ethics Review Questions

| # | Question | Answer Required Before MVP |
|---|----------|--------------------------|
| 1 | **Fundamental permissibility:** Is this a system that *should* exist? Does it serve a legitimate need, or does it primarily extract value from vulnerable populations? | Yes |
| 2 | **Proportionality:** Is the level of AI autonomy proportionate to the stakes? Could a simpler system (rules, human process) achieve an acceptable outcome? | Yes |
| 3 | **Reversibility:** If the MVP causes harm, can that harm be reversed? What is the blast radius of a failure during MVP testing? | Yes |
| 4 | **Consent and awareness:** Will the people affected by the MVP know they are being affected by an AI system? | Yes |
| 5 | **Data ethics:** Is the data being used for the MVP collected with appropriate consent or legal basis? Is the use consistent with the purposes for which the data was originally collected? | Yes |
| 6 | **Vulnerable populations:** Could the MVP disproportionately affect vulnerable groups? If the MVP uses a limited dataset, could this create biased results that harm specific populations? | Yes |
| 7 | **Exit strategy:** If the ethics review at any later gate raises concerns, can development be halted and resources redirected without contractual or organizational lock-in? | Yes |

### Ethics Review Outcomes

| Outcome | Definition | Action |
|---------|------------|--------|
| **Approved** | No fundamental ethical objections; identified risks have acceptable mitigations | Proceed to MVP build |
| **Approved with conditions** | Ethical concerns exist but are manageable with specific constraints | Proceed with documented constraints (e.g., limited data scope, restricted user population, mandatory HITL) |
| **Deferred** | Insufficient information to make a determination | Gather additional information before re-review; do not build |
| **Rejected** | Fundamental ethical concerns that cannot be mitigated | Do not build. Redesign the concept or abandon the initiative. Document the reasons for the record. |

### Ethics Review Authority

| Risk Tier | Ethics Review Authority |
|-----------|------------------------|
| Minimal | Product Manager self-assessment (documented) |
| Limited | Ethics Lead review |
| High | Ethics Lead review + AI Governance Committee discussion |

---

## Gate 3: Data Governance Requirements for MVP

### Objective

Ensure that data used in the MVP phase -- for training, fine-tuning, evaluation, or inference -- meets minimum governance standards. MVP data practices often set precedents that persist into production. Getting data governance wrong at the MVP stage creates technical debt that is expensive to remediate.

### 3.1 MVP Data Governance Checklist

Complete this checklist before using any data in the MVP:

| # | Requirement | Status | Evidence | Notes |
|---|-------------|--------|----------|-------|
| 1 | All data sources are inventoried with documented provenance | [ ] | | |
| 2 | GDPR lawful basis is identified for all personal data processing | [ ] | | |
| 3 | Data use is consistent with the purposes for which it was collected (purpose limitation) | [ ] | | |
| 4 | Data minimization: only data necessary for the MVP is accessed | [ ] | | |
| 5 | Data retention period for MVP data is defined and communicated | [ ] | | |
| 6 | If using production data for MVP, appropriate anonymization or pseudonymization is applied | [ ] | | |
| 7 | If collecting new data for MVP, data subjects are informed per GDPR Art. 13/14 | [ ] | | |
| 8 | Third-party data has contractual terms permitting use for AI training/inference | [ ] | | |
| 9 | Data quality assessment is documented (completeness, accuracy, representativeness) | [ ] | | |
| 10 | Data access controls are in place (who can access MVP data and under what conditions) | [ ] | | |
| 11 | Labeling methodology is documented (if labeled data is used) | [ ] | | |
| 12 | Data versioning is in place so MVP results can be reproduced | [ ] | | |

### 3.2 MVP Data Environment

| Question | Answer |
|----------|--------|
| Where will MVP data be stored? | [FILL IN: Specific environment -- dev, staging, sandbox] |
| Is this environment compliant with your data classification policy? | [Yes/No] |
| Can MVP data be deleted after the MVP concludes? | [Yes/No -- describe constraints] |
| Is there a risk of MVP data leaking into production systems? | [Yes/No -- describe safeguards] |
| Will the MVP use real customer data, synthetic data, or both? | [FILL IN] |

### 3.3 Special Considerations for FinTech MVP Data

| Consideration | Applies? | Mitigation |
|---------------|----------|------------|
| Transaction data may reveal spending patterns linked to health, religion, or political views (GDPR special category data) | [Yes/No] | |
| AML-relevant data has regulatory retention obligations that override deletion requests | [Yes/No] | |
| Cross-border data transfers may apply if MVP infrastructure is in a different jurisdiction | [Yes/No] | |
| Payment card data is subject to PCI DSS regardless of purpose | [Yes/No] | |
| Customer data used in MVP must not be accessible to unauthorized internal parties (Chinese wall requirements) | [Yes/No] | |

---

## Minimum Viable Governance

### Concept

Just as a Minimum Viable Product strips a product to its essential features, Minimum Viable Governance (MVG) strips governance to its essential controls. MVG is not "no governance" -- it is the smallest set of governance activities that still meet regulatory obligations and ethical minimums.

MVG applies to the MVP phase of **Minimal-risk** systems. Limited and High-risk systems require full governance at the MVP stage (they cannot be streamlined further without regulatory exposure).

> *Cross-reference:* See [Minimum Viable Governance](../../07-enterprise-implementation/risk-based-adoption/minimum-viable-governance.md) for the enterprise-wide MVG framework.

### MVG for Minimal-Risk AI MVPs

| Governance Activity | Full Governance Requirement | MVG Equivalent |
|--------------------|----------------------------|----------------|
| Risk classification | Full [EU AI Act checklist](../checklists/eu-ai-act-risk-classification.yaml) | Abbreviated classification (decision tree result + one-paragraph rationale) |
| Ethical impact assessment | Full harm assessment with mitigations | Quick ethics screen: answer questions 1, 3, and 6 from Gate 2 |
| Data governance | Full data inventory with provenance | Data source list with lawful basis confirmation |
| Acceptance criteria | Full criteria with thresholds and eval strategy | Core metrics with informal thresholds (formalize before production) |
| Stakeholder analysis | Full stakeholder value map | List of affected populations with one-sentence impact description |
| Human oversight model | Full HITL/HOTL/HOTA analysis | Statement of oversight approach (can be informal) |
| Documentation | Responsible Product Brief (all sections) | One-page MVP governance memo covering risk tier, ethics screen, data sources, and oversight |

### MVG Does NOT Exempt

Even under MVG, these requirements are never waived:

1. **Prohibited practices check** -- always required, always a hard stop if violated
2. **Personal data lawful basis** -- GDPR applies regardless of product phase or risk tier
3. **Audit trail** -- all MVP decisions must be logged (even if logging is basic)
4. **Exit strategy** -- there must be a plan to shut down the MVP and delete data if governance issues emerge

---

## Governance Artifacts Required Before MVP Build

### Summary by Risk Tier

| Artifact | Minimal | Limited | High |
|----------|---------|---------|------|
| EU AI Act risk classification | Abbreviated | Full | Full |
| Ethics review outcome | Self-assessment | Ethics Lead signed | Committee-reviewed |
| Data governance checklist (Section 3.1) | Abbreviated (items 1-5) | Full | Full |
| MVP governance sign-off (Section 6) | Fast-track version | Full version | Full version |
| Responsible Product Brief | Summary version | Full | Full |
| Evaluation strategy | Core metrics only | Full [template](../evaluations/evaluation-strategy-template.yaml) | Full template + red-team plan |
| DPIA | Not required | If personal data | Required |
| AI Governance Committee approval | Not required | Required | Required |
| Board-level sponsor | Not required | Not required | Required |

---

## Balancing Speed-to-Market with Governance

### The Speed-Governance Tradeoff

Teams often perceive governance as a brake on speed. This section reframes the relationship: governance done right at the MVP stage *accelerates* later stages by preventing expensive rework.

| Without MVP Governance | With MVP Governance |
|------------------------|---------------------|
| Build fast, discover risk classification after building | Know risk classification before building; right-size governance from the start |
| Collect data first, figure out lawful basis later | Confirm lawful basis before collecting; avoid data deletion and re-collection |
| Launch MVP, then respond to ethics concerns reactively | Address ethics proactively; avoid reputational damage and stakeholder pushback |
| Scale into production, then retrofit compliance | Compliance-ready architecture from MVP onwards; avoid costly rearchitecture |
| Discover at pre-deployment gate that the system is High-risk | Know from day one; plan governance capacity into sprint velocity |

### Time Investment for MVP Governance

| Risk Tier | Estimated Governance Time for MVP Phase | Recommended Approach |
|-----------|----------------------------------------|---------------------|
| Minimal | 2-4 hours | Product Manager completes abbreviated governance memo in a single session |
| Limited | 1-2 days | Product Manager drafts governance sections; Ethics Lead and Compliance review asynchronously; one 60-minute alignment meeting |
| High | 3-5 days | Full governance artifact creation; Ethics Lead deep review; AI Governance Committee agenda item; DPO consultation |

### Practical Tips for Fast Governance

1. **Reuse prior classifications.** If your organization has already classified a similar system, reference that classification and document only the differences.
2. **Parallelize governance work.** While the PM works on the product brief, the Compliance Officer can begin risk classification, and the DPO can assess data governance requirements concurrently.
3. **Use templates.** The [Responsible Product Brief](../templates/responsible-product-brief.md) and the checklists in this pillar exist to eliminate blank-page paralysis.
4. **Timebox ethics review.** For Limited-risk systems, give the Ethics Lead a 90-minute timebox to provide feedback on the ethical impact assessment. Document the review even if it is brief.
5. **Do not defer classification.** The single most expensive governance mistake is building an MVP assuming Minimal-risk and discovering it is High-risk at the pre-deployment gate. The 30-minute classification exercise prevents this.

---

## Section 6: MVP Governance Sign-Off Template

### Full Version (Limited and High-Risk Systems)

Complete and obtain signatures before the MVP build begins.

```markdown
# MVP Governance Sign-Off

## Product Information
- **Product/Feature Name:** [FILL IN]
- **Product Manager:** [FILL IN]
- **MVP Build Start Date:** [FILL IN]
- **Target MVP Completion Date:** [FILL IN]

## Gate 1: Risk Classification
- **EU AI Act Risk Tier:** [Minimal / Limited / High]
- **Classification evidence:** [Link to completed risk classification checklist]
- **Prohibited practices check:** PASSED / FAILED
- **Governance intensity:** [Streamlined / Standard / Full]

## Gate 2: Ethics Review
- **Ethics review outcome:** [Approved / Approved with Conditions / Deferred / Rejected]
- **Conditions (if applicable):** [FILL IN]
- **Reviewer:** [FILL IN: Name, Role]
- **Review date:** [FILL IN]

## Gate 3: Data Governance
- **Data governance checklist completed:** [Yes / No]
- **Personal data processed:** [Yes / No]
- **GDPR lawful basis confirmed:** [Yes / No / N/A]
- **DPIA status:** [Required - Initiated / Required - Not Yet Initiated / Not Required]
- **Data environment:** [FILL IN: where MVP data will be stored]

## MVP Scope Constraints
- **User population for MVP:** [FILL IN: who will be exposed to the MVP]
- **Data scope for MVP:** [FILL IN: what data will be used]
- **Decision scope for MVP:** [FILL IN: what decisions will the AI make or influence]
- **Duration of MVP:** [FILL IN: planned duration before production decision]
- **Rollback plan:** [FILL IN: how will the MVP be shut down if needed]

## Evaluation Commitments
- **Core metrics to track during MVP:** [FILL IN]
- **Success threshold for proceeding to production:** [FILL IN]
- **Fairness metrics to track:** [FILL IN or N/A for Minimal-risk]

## Approvals

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Product Manager | | | |
| Tech Lead | | | |
| Ethics Lead | | | |
| Compliance Officer | | | |
| Data Protection Officer | | | |
| AI Governance Committee Chair | | | |
| Board-Level Sponsor (High-risk only) | | | |
```

### Fast-Track Version (Minimal-Risk Systems)

```markdown
# MVP Governance Sign-Off (Fast-Track)

- **Product/Feature Name:** [FILL IN]
- **Product Manager:** [FILL IN]
- **Date:** [FILL IN]

## Quick Classification
- **Risk Tier:** Minimal
- **Rationale (one paragraph):** [FILL IN: Why this is Minimal-risk, referencing
  the decision tree result]
- **Prohibited practices check:** PASSED

## Quick Ethics Screen
- Should this system exist? Does it serve a legitimate need? [FILL IN: Yes + brief rationale]
- If the MVP causes harm, can it be reversed? [FILL IN]
- Could it disproportionately affect vulnerable groups? [FILL IN]

## Data Sources
| Data Source | Personal Data? | Lawful Basis |
|-------------|---------------|-------------|
| [FILL IN] | [Yes/No] | [FILL IN] |

## Oversight
- **Human oversight approach:** [FILL IN: brief description]

## Approval
- **Product Manager:** [Name, Date]
- **Tech Lead:** [Name, Date]
```

---

## Cross-References

| Topic | Artifact | Location |
|-------|----------|----------|
| Full governance-integrated PRD template | Responsible Product Brief | [templates/responsible-product-brief.md](../templates/responsible-product-brief.md) |
| PRD-phase governance questions | PRD Governance Add-on | [governance-extensions/prd-governance-addon.md](prd-governance-addon.md) |
| Risk classification checklist | EU AI Act Risk Classification | [checklists/eu-ai-act-risk-classification.yaml](../checklists/eu-ai-act-risk-classification.yaml) |
| Governance intensity decision tree | Product Development Lifecycle | [guides/product-development-lifecycle.md](../guides/product-development-lifecycle.md#governance-intensity-decision-tree) |
| Acceptance criteria guide | Defining Acceptance Criteria | [evaluations/defining-acceptance-criteria.md](../evaluations/defining-acceptance-criteria.md) |
| Evaluation strategy template | Evaluation Strategy Template | [evaluations/evaluation-strategy-template.yaml](../evaluations/evaluation-strategy-template.yaml) |
| Minimum viable governance (enterprise) | Minimum Viable Governance | [minimum-viable-governance.md](../../07-enterprise-implementation/risk-based-adoption/minimum-viable-governance.md) |
| Pre-deployment gate | Pre-Deployment Gate Checklist | [pre-deployment-gate.yaml](../../02-development-governance/checklists/pre-deployment-gate.yaml) |
| Development eval methodology | Eval-Driven Development | [eval-driven-development.md](../../02-development-governance/evaluations/eval-driven-development.md) |
| Runtime monitoring | Continuous Online Evaluation | [continuous-online-evaluation.md](../../03-runtime-governance/evaluations/continuous-online-evaluation.md) |
| Risk tiering model | Risk Tiering Model | [risk-tiering-model.md](../../07-enterprise-implementation/risk-based-adoption/risk-tiering-model.md) |

---

*Last updated: 2026-02-28*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
*Framework: [Product Governance for Agentic AI Workflows](../../README.md)*
