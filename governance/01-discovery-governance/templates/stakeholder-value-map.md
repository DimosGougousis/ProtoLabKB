# Stakeholder Value Map Template

## Purpose

This template provides a structured approach for mapping the value an AI system delivers to -- and the risks it imposes on -- every stakeholder group. In regulated FinTech, AI systems rarely affect only their direct users. A credit scoring model affects applicants, loan officers, the bank's risk function, regulators, and the broader community. A fraud detection agent affects cardholders, merchants, operations teams, and the financial system's integrity.

Traditional product discovery focuses narrowly on user value. This template expands the lens to include all groups who receive value from or bear risk because of the AI system. The completed Stakeholder Value Map becomes a mandatory input to the [Discovery Gate](../README.md) review and feeds directly into the [AI Ethics Impact Assessment](./ai-ethics-impact-assessment.md) and the [Ethical Discovery Workshop](../governance-extensions/ethical-discovery-workshop.md).

The DNB SAFEST framework (Soundness, Accountability, Fairness, Ethics, Skills, Transparency) requires financial institutions to demonstrate that they have considered the interests of all affected parties before deploying AI systems. The EU AI Act's fundamental rights impact assessment (Article 29a) requires high-risk AI system deployers to assess impacts on affected persons. This template operationalizes both requirements.

## When to Use

- During the **Discovery phase**, before writing a PRD or Responsible Product Brief
- When evaluating whether to proceed with an AI solution versus a non-AI alternative
- When a material change in scope (new user group, new data source, new geography) triggers re-assessment
- As input to the [Ethical Discovery Workshop](../governance-extensions/ethical-discovery-workshop.md)
- When preparing a fundamental rights impact assessment under the EU AI Act

**Trigger:** A product team begins exploring an AI-powered product or feature and needs to understand its full stakeholder impact before committing to development.

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **Product Manager** | **Accountable** -- facilitates stakeholder identification, completes the value map, presents findings at Discovery Gate |
| **UX Researcher** | **Responsible** -- contributes user and affected population insights from research activities |
| **Ethics Lead / Responsible AI Lead** | **Consulted** -- reviews stakeholder completeness, challenges blind spots, validates vulnerability assessments |
| **Compliance Officer (2nd Line)** | **Consulted** -- validates regulatory stakeholder considerations, reviews fundamental rights impact dimensions |
| **Business Sponsor** | **Consulted** -- provides business value and strategic alignment perspective |
| **AI Governance Committee** | **Informed** -- receives completed value map as part of Discovery Gate documentation |

## Regulatory Basis

- **EU AI Act Article 9(2)(a)** -- Risk management must identify and analyze known and foreseeable risks to health, safety, and fundamental rights
- **EU AI Act Article 29a** -- Fundamental rights impact assessment for high-risk AI deployers
- **GDPR Article 35** -- Data Protection Impact Assessment must assess risks to the rights and freedoms of natural persons
- **DNB Good Practice for AI (SAFEST)** -- Fairness and Accountability dimensions require stakeholder impact analysis
- **ISO/IEC 42001 Clause 4.2** -- Understanding the needs and expectations of interested parties

---

## TEMPLATE BEGINS HERE

> **Instructions:** Copy everything below this line into a new document. Replace all `[FILL IN]` placeholders. Delete instructional comments (lines starting with `>`) before finalizing.

---

# Stakeholder Value Map: [FILL IN: AI System Name]

| Field | Value |
|-------|-------|
| **Author** | [FILL IN: Name, Role] |
| **Date** | [FILL IN: YYYY-MM-DD] |
| **Version** | [FILL IN: e.g., 1.0] |
| **AI System** | [FILL IN: Name and brief description] |
| **Risk Classification** | Minimal / Limited / High / Prohibited |
| **Related PRD/Brief** | [FILL IN: Link to Responsible Product Brief or PRD] |

---

## 1. Stakeholder Identification Matrix

Use the matrix below to systematically identify all stakeholders. Do not skip any category. If a category genuinely has no stakeholders for this system, write "None identified" and explain why.

### 1.1 Direct Stakeholders (interact with the system or its outputs)

| # | Stakeholder Group | Description | Interaction Type | Estimated Scale |
|---|-------------------|-------------|------------------|-----------------|
| D1 | [FILL IN] | [FILL IN: Who are they?] | [User / Recipient / Operator] | [FILL IN: Approximate number] |
| D2 | [FILL IN] | [FILL IN] | [User / Recipient / Operator] | [FILL IN] |
| D3 | [FILL IN] | [FILL IN] | [User / Recipient / Operator] | [FILL IN] |

> *Example (AI Credit Scoring):*
> | D1 | Loan applicants | Individuals applying for personal loans via the digital channel | Recipient of AI decision | ~150,000/year |
> | D2 | Loan officers | Bank employees who review AI recommendations and make final decisions for borderline cases | Operator / Override authority | ~45 FTE |
> | D3 | Customer service agents | Handle applicant inquiries about decisions, including explanation requests | Operator / Communicator | ~120 FTE |

### 1.2 Indirect Stakeholders (affected by the system but do not interact with it)

| # | Stakeholder Group | Description | How They Are Affected | Estimated Scale |
|---|-------------------|-------------|----------------------|-----------------|
| I1 | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |
| I2 | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |

> *Example (AI Credit Scoring):*
> | I1 | Family members of rejected applicants | Household members who depend on the applicant's access to credit | Indirect financial impact from credit denial | ~300,000/year |
> | I2 | Competing lenders | Other financial institutions whose competitive position is affected | Market dynamics shift if AI enables faster, cheaper decisioning | Industry-wide |

### 1.3 Vulnerable Populations

| # | Stakeholder Group | Vulnerability Factor | Why They Are Disproportionately Affected | Protection Measures Needed |
|---|-------------------|---------------------|------------------------------------------|---------------------------|
| V1 | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |
| V2 | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |

> *Example (AI Credit Scoring):*
> | V1 | Thin-file applicants | Limited credit history (recent immigrants, young adults, gig workers) | AI model may lack sufficient data to assess creditworthiness, leading to systematic rejection | Alternative data consideration, manual review pathway, appeals process |
> | V2 | Historically redlined communities | Systemic discrimination embedded in historical lending data | Model trained on historical data may perpetuate geographic discrimination patterns | Bias testing by geography, fairness constraints, disparate impact analysis |

### 1.4 Institutional Stakeholders

| # | Stakeholder Group | Interest in the System | Oversight Role |
|---|-------------------|----------------------|----------------|
| S1 | [FILL IN] | [FILL IN] | [FILL IN] |
| S2 | [FILL IN] | [FILL IN] | [FILL IN] |

> *Example (AI Credit Scoring):*
> | S1 | National regulator (e.g., DNB, BaFin, FCA) | Fair lending compliance, consumer protection, systemic risk | Supervisory examination, model validation requirements |
> | S2 | Internal Audit (3rd Line) | Model risk management, governance compliance | Independent model validation, governance process audits |
> | S3 | Data Protection Authority | GDPR compliance for automated decision-making | DPIA review, complaints investigation |

### 1.5 Societal Stakeholders

| # | Stakeholder Group | Societal Interest | Potential Systemic Impact |
|---|-------------------|-------------------|--------------------------|
| C1 | [FILL IN] | [FILL IN] | [FILL IN] |

> *Example (AI Credit Scoring):*
> | C1 | General public / civil society | Financial inclusion, non-discrimination | If multiple banks adopt similar AI models, systemic bias could widen the credit gap for disadvantaged groups |
> | C2 | Academic / research community | Transparency, reproducibility | Lack of transparency may impede research on algorithmic fairness in lending |

---

## 2. Value-Risk Assessment Per Stakeholder Group

For each stakeholder identified in Section 1, assess both the value the system delivers and the risks it creates. Use the impact dimensions defined below.

### 2.1 Impact Dimensions

| Dimension | Description | Examples |
|-----------|-------------|----------|
| **Financial** | Direct monetary gain or loss to the stakeholder | Revenue, cost savings, denied access to credit, fraud losses |
| **Operational** | Changes to how the stakeholder works or operates | Process efficiency, workload changes, skill requirements |
| **Reputational** | Impact on trust, brand perception, or public standing | Customer trust, regulatory standing, media coverage |
| **Social** | Broader effects on communities, inclusion, or rights | Financial inclusion, discrimination, community access to services |
| **Autonomy** | Impact on the stakeholder's ability to make informed choices | Understanding of AI decisions, ability to contest, opt-out options |
| **Safety** | Physical, psychological, or financial safety effects | Stress from incorrect decisions, financial hardship from errors |

### 2.2 Value-Risk Matrix

Complete one row per stakeholder group identified in Section 1.

| Stakeholder | Value Delivered | Value Rating | Primary Risks | Risk Rating | Net Assessment | Mitigation Priority |
|-------------|----------------|--------------|---------------|-------------|----------------|---------------------|
| [D1] | [FILL IN] | High/Med/Low | [FILL IN] | High/Med/Low | [Positive/Neutral/Negative] | [Critical/High/Medium/Low] |
| [D2] | [FILL IN] | High/Med/Low | [FILL IN] | High/Med/Low | [Positive/Neutral/Negative] | [Critical/High/Medium/Low] |

> *Example (AI Credit Scoring):*
> | Loan applicants | Faster decisions (minutes vs. days), broader access for some segments | High | Opaque decisions, potential bias, reduced human judgment | High | Conditional Positive (if mitigations work) | Critical |
> | Loan officers | Reduced manual workload, decision support | Medium | Deskilling, over-reliance on AI, reduced professional judgment | Medium | Positive | Medium |
> | Thin-file applicants | Potential for alternative data to expand access | Medium | Higher rejection rates if model is not designed for thin-file scenarios | High | Negative (without mitigation) | Critical |
> | Regulators | Improved consistency and auditability of lending decisions | Medium | New supervisory challenges, model risk concentration | Medium | Neutral | High |

### 2.3 Detailed Risk Narratives

For each stakeholder with a Risk Rating of High or a Mitigation Priority of Critical, provide a narrative risk description.

#### [Stakeholder Group Name]

| Field | Detail |
|-------|--------|
| **Risk Description** | [FILL IN: Describe the specific risk in concrete terms] |
| **Impact Dimensions** | [FILL IN: Which dimensions from 2.1 are affected?] |
| **Severity** | [Critical / High / Medium / Low] |
| **Likelihood** | [Almost Certain / Likely / Possible / Unlikely / Rare] |
| **Reversibility** | [Easily reversible / Reversible with effort / Partially reversible / Irreversible] |
| **Existing Controls** | [FILL IN: What controls already exist?] |
| **Additional Mitigations Needed** | [FILL IN: What new controls are required?] |
| **Residual Risk After Mitigation** | [High / Medium / Low / Acceptable] |

> *Example (AI Credit Scoring -- Thin-file applicants):*
> | **Risk Description** | Applicants with fewer than 3 trade lines are rejected at a rate 2.8x higher than the general population. The model has insufficient signal to differentiate creditworthy thin-file applicants from high-risk ones, defaulting to rejection. |
> | **Impact Dimensions** | Financial (denied credit), Social (financial exclusion), Autonomy (limited understanding of why) |
> | **Severity** | High |
> | **Likelihood** | Almost Certain (based on historical data analysis) |
> | **Reversibility** | Reversible with effort (applicant can reapply, but delay causes financial harm) |
> | **Existing Controls** | Manual review for all rejections above a threshold |
> | **Additional Mitigations Needed** | Alternative data sources, dedicated thin-file model variant, mandatory explanation letter, expedited appeals process |
> | **Residual Risk After Mitigation** | Medium |

---

## 3. Value Distribution Analysis

This section evaluates whether the AI system's value is distributed fairly across stakeholder groups, or whether some groups systematically bear costs while others capture benefits.

### 3.1 Value Distribution Summary

| Stakeholder Group | Captures Value? | Bears Risk? | Distribution Fair? | Justification |
|-------------------|----------------|-------------|-------------------|---------------|
| [FILL IN] | Yes / No / Partially | Yes / No / Partially | Yes / No / Unclear | [FILL IN] |

### 3.2 Distributional Fairness Assessment

Answer each question:

| # | Question | Answer |
|---|----------|--------|
| 1 | Do any stakeholder groups bear significant risk while receiving no value from the system? | [FILL IN] |
| 2 | Are vulnerable populations disproportionately exposed to risks compared to the value they receive? | [FILL IN] |
| 3 | Does the system's value primarily accrue to the organization while risks are externalized to users or communities? | [FILL IN] |
| 4 | Are there mechanisms for stakeholders who bear risks to be compensated or protected? | [FILL IN] |
| 5 | If this system's risk distribution were made public, would it be defensible to regulators, media, and civil society? | [FILL IN] |

### 3.3 Redistribution Actions

If the distributional fairness assessment reveals imbalances, document planned corrective actions:

| Imbalance Identified | Affected Group | Corrective Action | Owner | Deadline |
|---------------------|----------------|-------------------|-------|----------|
| [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |

---

## 4. Stakeholder Engagement Plan

Document how each stakeholder group will be engaged throughout the AI system's lifecycle.

| Stakeholder Group | Engagement Method | Frequency | Purpose | Owner |
|-------------------|-------------------|-----------|---------|-------|
| [FILL IN] | [Interview / Survey / Advisory board / Complaint channel / Public consultation] | [FILL IN] | [FILL IN] | [FILL IN] |

> *Example (AI Credit Scoring):*
> | Loan applicants | Post-decision survey, complaint channel, annual focus groups | Ongoing / Annual | Understand experience, identify pain points, test explanations | UX Research |
> | Consumer advocacy groups | Annual consultation, ad hoc engagement on methodology changes | Annual / As needed | External perspective on fairness and access | Ethics Lead |
> | Regulators | Supervisory reporting, model documentation submission | Quarterly / On request | Compliance demonstration, proactive transparency | Compliance |

---

## 5. SAFEST Framework Alignment Check

Map the stakeholder value analysis against the DNB SAFEST dimensions to verify completeness.

| SAFEST Dimension | Relevant Stakeholders | Key Findings from Value Map | Gaps or Actions Needed |
|-----------------|----------------------|----------------------------|----------------------|
| **Soundness** | [FILL IN: Which stakeholders are affected by model reliability?] | [FILL IN] | [FILL IN] |
| **Accountability** | [FILL IN: Which stakeholders need clear accountability chains?] | [FILL IN] | [FILL IN] |
| **Fairness** | [FILL IN: Which stakeholders face fairness risks?] | [FILL IN] | [FILL IN] |
| **Ethics** | [FILL IN: Which stakeholders raise ethical concerns?] | [FILL IN] | [FILL IN] |
| **Skills** | [FILL IN: Which stakeholders need training or capability building?] | [FILL IN] | [FILL IN] |
| **Transparency** | [FILL IN: Which stakeholders need explanations or disclosures?] | [FILL IN] | [FILL IN] |

---

## 6. Sign-off and Discovery Gate Input

### 6.1 Summary Assessment

| Question | Answer |
|----------|--------|
| Total stakeholder groups identified | [FILL IN: Number] |
| Stakeholder groups with net negative assessment | [FILL IN: Number and names] |
| Critical mitigation priorities | [FILL IN: Number] |
| Distributional fairness issues identified | [FILL IN: Yes/No, brief summary] |
| Recommendation | Proceed / Proceed with conditions / Do not proceed |

### 6.2 Conditions for Proceeding (if applicable)

| # | Condition | Must be resolved by | Owner |
|---|-----------|-------------------|-------|
| 1 | [FILL IN] | [FILL IN: Phase/Date] | [FILL IN] |

### 6.3 Approvals

| Role | Name | Decision | Date |
|------|------|----------|------|
| Product Manager | [FILL IN] | Submitted | [FILL IN] |
| Ethics Lead | [FILL IN] | Reviewed / Approved / Concerns raised | [FILL IN] |
| Compliance Officer | [FILL IN] | Reviewed / Approved / Concerns raised | [FILL IN] |

---

## Related Documents

| Document | Location |
|----------|----------|
| Responsible Product Brief | [responsible-product-brief.md](./responsible-product-brief.md) |
| AI Ethics Impact Assessment | [ai-ethics-impact-assessment.md](./ai-ethics-impact-assessment.md) |
| Ethical Discovery Workshop | [ethical-discovery-workshop.md](../governance-extensions/ethical-discovery-workshop.md) |
| Integrating Thoughtworks Playbook | [integrating-thoughtworks-playbook.md](../guides/integrating-thoughtworks-playbook.md) |
| PAIR Guide for PMs | [pair-guide-for-pms.md](../guides/pair-guide-for-pms.md) |
| PRD Governance Add-on | [prd-governance-addon.md](../governance-extensions/prd-governance-addon.md) |
| Bias Assessment Report Template | [bias-assessment-report.md](../../02-development-governance/templates/bias-assessment-report.md) |

---

*Last updated: 2026-03-01*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
*Framework: [Product Governance for Agentic AI Workflows](../../README.md)*
