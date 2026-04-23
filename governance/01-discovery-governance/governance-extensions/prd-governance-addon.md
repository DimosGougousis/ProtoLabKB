# PRD Governance Add-on

## Purpose

This document provides governance extensions for the PRD (Product Requirements Document) phase of AI product development. It is designed to be used alongside an external AI Product Development Toolkit -- specifically, it injects governance questions, checklists, and requirements into the PRD creation process so that governance is embedded at the point of product definition, not bolted on later.

The AI Product Dev Toolkit (a separate repository) provides the core product management methodology: problem validation, user research, feature prioritization, and PRD authoring. This add-on provides the governance layer that must accompany every AI-powered PRD in a regulated FinTech environment.

**This document does not replace the AI Product Dev Toolkit's PRD process. It extends it with governance-specific content.**

## When to Use

- When authoring a PRD for any product or feature that includes AI/ML/LLM capabilities
- When reviewing an existing PRD for governance completeness before the [Discovery Gate](../README.md)
- When onboarding product managers who are new to AI governance requirements
- As a reference during PRD review sessions where governance stakeholders are present

**Trigger:** A product manager begins or reviews a PRD for an AI-powered product or feature.

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **Product Manager** | **Accountable** -- integrates governance questions into the PRD using this add-on |
| **Ethics Lead** | **Consulted** -- reviews answers to ethical considerations and stakeholder impact sections |
| **Compliance Officer** | **Consulted** -- reviews risk classification and data provenance sections |
| **Data Protection Officer** | **Consulted** -- reviews data governance requirements, particularly for personal data |
| **AI Governance Committee** | **Informed** -- receives completed PRD with governance sections for Discovery Gate review |

## Regulatory Basis

- **EU AI Act Article 9(2)** -- Risk management system must identify and analyze known and foreseeable risks at the design stage
- **EU AI Act Article 13** -- High-risk AI systems must be designed to enable transparency
- **EU AI Act Article 14** -- High-risk AI systems must be designed to enable human oversight
- **GDPR Article 25** -- Data protection by design and by default
- **GDPR Article 35** -- Data Protection Impact Assessment required for high-risk processing
- **DORA Article 5(2)** -- ICT risk management framework must be documented and reviewed

---

## How This Add-on Works with the AI Product Dev Toolkit

The AI Product Dev Toolkit provides a structured PRD process with phases, templates, and review cadences. This governance add-on integrates at specific points in that process:

```
AI Product Dev Toolkit PRD Process         Governance Add-on Injection Points
========================================   =====================================
1. Problem Definition                 ---> + Ethical framing questions (Section 1)
2. User Research & Personas           ---> + Affected population analysis (Section 2)
3. Solution Hypothesis                ---> + AI necessity justification (Section 3)
4. Requirements Specification         ---> + Governance requirements (Section 4)
5. Success Metrics                    ---> + Governance metrics (Section 5)
6. PRD Review & Approval              ---> + Governance review checklist (Section 6)
```

**Integration instructions:**

1. Begin the PRD using the AI Product Dev Toolkit's standard template
2. At each phase listed above, pause and answer the corresponding governance questions from this add-on
3. Incorporate governance answers directly into the PRD (use the [Responsible Product Brief](../templates/responsible-product-brief.md) template if starting from scratch)
4. Before PRD approval, complete the governance review checklist (Section 6 of this document)

Alternatively, use the [Responsible Product Brief](../templates/responsible-product-brief.md) template which pre-integrates all governance sections into a single document.

---

## Section 1: Ethical Framing Questions for Problem Definition

When defining the problem that the AI product will solve, answer these additional governance questions:

### 1.1 Harm Landscape

| # | Question | Your Answer |
|---|----------|-------------|
| 1 | What is the worst outcome if this system makes an incorrect decision? | |
| 2 | Who bears the cost of errors -- the organization, the user, or a third party? | |
| 3 | Could this system's decisions create irreversible consequences for any individual? | |
| 4 | Does this problem genuinely require AI, or is AI being applied because it is available rather than because it is the best tool? | |
| 5 | If this system did not exist, what would happen? Is the current state actually harmful enough to justify the risks of an AI solution? | |

### 1.2 Historical Context

| # | Question | Your Answer |
|---|----------|-------------|
| 6 | Has this problem domain historically involved discrimination or bias? (e.g., lending has documented disparate impact; fraud detection has geographic bias) | |
| 7 | Are there documented cases where AI has caused harm in this domain? What happened and why? | |
| 8 | What existing regulatory or industry guidance exists for AI in this domain? | |

> *FinTech example:* For a credit scoring product, question 6 is critical. Lending has a long history of redlining and disparate impact. The PRD must explicitly acknowledge this history and describe how the proposed system will avoid repeating it.

### 1.3 Power Dynamics

| # | Question | Your Answer |
|---|----------|-------------|
| 9 | Does this system shift decision-making power away from individuals toward the organization? | |
| 10 | Can affected individuals understand, contest, or appeal the system's decisions? | |
| 11 | Does the affected population have meaningful alternatives if they object to AI-based decisions? | |

---

## Section 2: Affected Population Analysis for User Research

When conducting user research, extend it to include affected populations who are not direct users but are impacted by the system's decisions.

### 2.1 Affected Population Identification

For each affected population, complete this analysis:

| Population Segment | How They Are Affected | Can They Opt Out? | Vulnerability Factors | Potential for Disproportionate Impact |
|--------------------|-----------------------|-------------------|-----------------------|--------------------------------------|
| [Identify segment] | [Direct/indirect impact] | [Yes/No/Partial] | [Age, language, digital literacy, economic status, etc.] | [Yes/No + explanation] |

### 2.2 Protected Characteristics Screening

Assess whether the system's decisions could vary based on protected characteristics, either directly or through proxy variables:

| Protected Characteristic | Could the System's Decisions Correlate with This? | Through What Mechanism? | Mitigation |
|-------------------------|---------------------------------------------------|------------------------|------------|
| Race / Ethnicity | [Yes/No] | [e.g., geographic data as proxy] | |
| Gender | [Yes/No] | [e.g., name-based inference] | |
| Age | [Yes/No] | [e.g., account tenure as proxy] | |
| Disability | [Yes/No] | [e.g., interaction patterns] | |
| Religion | [Yes/No] | [e.g., transaction timing patterns] | |
| National Origin | [Yes/No] | [e.g., language, location] | |
| Socioeconomic Status | [Yes/No] | [e.g., transaction amounts, merchant categories] | |

> *FinTech example:* A transaction fraud detection system using merchant category codes (MCCs) may disproportionately flag transactions at merchants frequently used by specific ethnic communities (e.g., international money transfer services). This proxy effect must be documented and mitigated.

### 2.3 Stakeholder Impact Analysis

For each stakeholder group, map the full impact spectrum:

| # | Question | Your Answer |
|---|----------|-------------|
| 1 | Who benefits most from this system? Who benefits least? | |
| 2 | Who bears the most risk from this system? Who bears the least? | |
| 3 | Is there a group that bears high risk but receives low benefit? If so, is this ethically justifiable? | |
| 4 | How will you gather feedback from affected populations who are not direct users? | |
| 5 | What recourse mechanisms exist for individuals who are harmed by the system? | |
| 6 | How will you communicate the existence and nature of the AI system to affected populations? | |

---

## Section 3: Risk Classification Questions

These questions determine the EU AI Act risk tier and the resulting governance intensity. Complete these before investing significant effort in the PRD -- a prohibited classification means the product cannot proceed.

### 3.1 Prohibited Practices Check (EU AI Act Art. 5)

Answer each question. If any answer is "Yes," escalate immediately to the Compliance Officer.

| # | Prohibited Practice | Applicable? | Notes |
|---|---------------------|-------------|-------|
| 1 | Does this system deploy subliminal or manipulative techniques to distort behavior? | [Yes/No] | |
| 2 | Does this system exploit vulnerabilities of specific groups (age, disability, social situation)? | [Yes/No] | |
| 3 | Does this system perform social scoring -- evaluating or classifying persons based on social behavior or personality characteristics? | [Yes/No] | |
| 4 | Does this system perform real-time remote biometric identification in public spaces for law enforcement? | [Yes/No] | |
| 5 | Does this system infer emotions in workplace or educational contexts? | [Yes/No] | |
| 6 | Does this system create or expand facial recognition databases through untargeted scraping? | [Yes/No] | |

### 3.2 High-Risk Classification (EU AI Act Art. 6 + Annex III)

| # | High-Risk Category | Applicable? | Annex III Reference |
|---|-------------------|-------------|---------------------|
| 1 | Biometric identification and categorization of natural persons | [Yes/No] | Annex III, 1 |
| 2 | Management and operation of critical infrastructure | [Yes/No] | Annex III, 2 |
| 3 | Education and vocational training (access, assessment) | [Yes/No] | Annex III, 3 |
| 4 | Employment, workers management, access to self-employment | [Yes/No] | Annex III, 4 |
| 5 | Access to essential private/public services (credit scoring, insurance pricing, emergency dispatch) | [Yes/No] | Annex III, 5 |
| 6 | Law enforcement (risk assessment, evidence analysis) | [Yes/No] | Annex III, 6 |
| 7 | Migration, asylum, border control | [Yes/No] | Annex III, 7 |
| 8 | Administration of justice and democratic processes | [Yes/No] | Annex III, 8 |

> *FinTech relevance:* Most AI systems in financial services that make or influence decisions about individuals fall under Annex III, point 5 (access to essential services). This includes: credit scoring, loan approval/denial, insurance underwriting, AML suspicious activity flagging, and fraud-triggered account restrictions.

### 3.3 Governance Intensity Determination

Based on the answers above, determine governance intensity:

| If... | Then governance intensity is... | Reference |
|-------|-------------------------------|-----------|
| Any Section 3.1 answer is "Yes" | **PROHIBITED** -- Do not proceed | EU AI Act Art. 5 |
| Any Section 3.2 answer is "Yes" | **HIGH** -- Full governance at every lifecycle gate | EU AI Act Art. 6(2) |
| System interacts with natural persons (chatbot, etc.) | **LIMITED** -- Standard governance + transparency obligations | EU AI Act Art. 50 |
| None of the above | **MINIMAL** -- Streamlined governance, fast-track eligible | EU AI Act Art. 95 |

> *Cross-reference:* See the [governance intensity decision tree](../guides/product-development-lifecycle.md#governance-intensity-decision-tree) for a visual flowchart.

---

## Section 4: Data Provenance Requirements

### 4.1 Data Source Documentation

For every data source used by the AI system, document:

| # | Question | Your Answer |
|---|----------|-------------|
| 1 | What is the origin of this data? (Internal system, third-party provider, public dataset, user-generated) | |
| 2 | Under what legal basis is this data collected and processed? | |
| 3 | Is the data representative of the population the system will serve? What groups may be underrepresented? | |
| 4 | How old is the data? Is there a risk of temporal drift (data reflecting outdated patterns)? | |
| 5 | Has this data been used to train other models? Are there potential data leakage or contamination risks? | |
| 6 | What data quality checks are in place at the source? | |
| 7 | If third-party data, what contractual terms govern its use for AI training and inference? | |
| 8 | Is there a documented data lineage from source to model input? | |

### 4.2 Training Data Governance

| Requirement | Addressed? | Evidence |
|-------------|-----------|----------|
| Training data has documented provenance | [Yes/No] | |
| Training data has been assessed for bias | [Yes/No] | |
| Training data includes representative samples of all affected populations | [Yes/No] | |
| Training data excludes prohibited attributes (or includes them only for debiasing) | [Yes/No] | |
| Training data retention policy is documented | [Yes/No] | |
| Training data versioning is in place | [Yes/No] | |

### 4.3 Synthetic and Augmented Data

| # | Question | Your Answer |
|---|----------|-------------|
| 1 | Does the system use synthetic or augmented training data? | |
| 2 | If yes, what generation method is used, and has it been validated for representativeness? | |
| 3 | What proportion of training data is synthetic vs. real? | |
| 4 | Could synthetic data introduce artifacts that affect fairness or accuracy? | |

---

## Section 5: Governance Metrics for Success Criteria

When defining success metrics in the PRD, include these governance-specific metrics alongside business and product metrics:

### 5.1 Mandatory Governance Metrics

| Metric | Description | Minimum Threshold | Risk Tier Applicability |
|--------|-------------|-------------------|------------------------|
| **Fairness gap** | Maximum allowable difference in key outcome rates (e.g., false positive rate, approval rate) across protected groups | <2% absolute difference for High-risk; <5% for Limited | Limited, High |
| **Explainability coverage** | % of decisions for which an explanation can be generated | 100% for High-risk; 90% for Limited | Limited, High |
| **Human override rate** | Observed rate of human overrides of AI decisions in production | Track and report; no fixed threshold (anomalies investigated) | All tiers |
| **Audit trail completeness** | % of decisions with complete input-output-version logging | 100% | All tiers |
| **Consent compliance** | % of data subjects who have provided valid consent (where consent is the lawful basis) | 100% | If consent-based |
| **Transparency disclosure** | Evidence that users are informed of AI involvement | Binary: disclosed / not disclosed | Limited, High |

### 5.2 Recommended Governance Metrics

| Metric | Description | Why It Matters |
|--------|-------------|---------------|
| Time-to-explanation | How quickly can the system produce an explanation for a specific decision? | Regulatory response SLAs |
| Appeal resolution time | How quickly are user appeals of AI decisions resolved? | User trust and regulatory expectations |
| Model staleness | Time since last model retrain or update | Performance degradation risk |
| Data freshness | Age of most recent data used in inference | Temporal drift risk |

---

## Section 6: Governance Review Checklist for PRD Approval

Before the PRD is submitted for approval (or presented at the [Discovery Gate](../README.md)), complete this checklist:

### Ethical Considerations Checklist

- [ ] Harm landscape questions (Section 1.1) are answered completely
- [ ] Historical context of bias in this domain is documented (Section 1.2)
- [ ] Power dynamics between the system and affected individuals are assessed (Section 1.3)
- [ ] All affected populations are identified, including non-users (Section 2.1)
- [ ] Protected characteristics screening is completed (Section 2.2)
- [ ] Stakeholder impact analysis shows no group bearing high risk with low benefit without justification (Section 2.3)
- [ ] Irreversibility of decisions is assessed and mitigations documented
- [ ] Recourse mechanisms for affected individuals are defined

### Risk Classification Checklist

- [ ] Prohibited practices check is completed with no "Yes" answers (Section 3.1)
- [ ] High-risk classification is determined (Section 3.2)
- [ ] Governance intensity level is documented and communicated to all stakeholders (Section 3.3)
- [ ] Full [EU AI Act Risk Classification Checklist](../checklists/eu-ai-act-risk-classification.yaml) is completed

### Data Governance Checklist

- [ ] All data sources are documented with provenance (Section 4.1)
- [ ] Training data governance requirements are addressed (Section 4.2)
- [ ] Synthetic data risks are assessed (Section 4.3, if applicable)
- [ ] GDPR lawful basis is identified for all personal data processing
- [ ] Data retention policies are documented for all data sources

### Completeness Checklist

- [ ] Governance metrics are included in PRD success criteria (Section 5)
- [ ] Human oversight model is selected and justified (see [Responsible Product Brief](../templates/responsible-product-brief.md) Section 9)
- [ ] Transparency requirements are specified (see [Responsible Product Brief](../templates/responsible-product-brief.md) Section 8)
- [ ] Cross-references to Development Governance eval requirements are included
- [ ] PRD is reviewed by Ethics Lead (for Limited and High-risk systems)
- [ ] PRD is reviewed by Compliance Officer (for Limited and High-risk systems)
- [ ] PRD is reviewed by Data Protection Officer (if personal data is processed)

---

## Template: Governance Section for PRDs

If you are using a PRD template that does not have built-in governance sections (e.g., the AI Product Dev Toolkit's standard PRD template), add this governance section to the end of the PRD:

```markdown
## Governance

### Risk Classification
- **EU AI Act Risk Tier:** [Minimal / Limited / High]
- **Classification Rationale:** [Brief explanation referencing specific Art. and Annex]
- **Governance Intensity:** [Streamlined / Standard / Full]
- **Full classification:** [Link to completed eu-ai-act-risk-classification.yaml]

### Ethical Impact Summary
- **Primary harm risks:** [List top 3 identified harms]
- **Affected populations:** [List populations with potential for disproportionate impact]
- **Mitigations:** [Summarize key mitigations]
- **Full assessment:** [Link to ethical impact section of Responsible Product Brief]

### Human Oversight
- **Oversight model:** [HITL / HOTL / HOTA]
- **Justification:** [Brief rationale]
- **Override mechanism:** [How humans can override the system]

### Data Governance
- **Personal data processed:** [Yes / No]
- **Special category data:** [Yes / No]
- **Lawful basis:** [GDPR Article 6 basis]
- **DPIA required:** [Yes / No]
- **Data provenance documented:** [Yes / No]

### Governance Metrics
[Include metrics from Section 5.1 of this add-on]

### Evaluation Commitments
- **Pre-deployment eval suite:** [Link to evaluation strategy template]
- **Post-deployment monitoring:** [Link to continuous evaluation plan]
- **Bias audit cadence:** [Monthly / Quarterly / Semi-annual]
```

---

## Cross-References

| Topic | Artifact | Location |
|-------|----------|----------|
| Full governance-integrated PRD template | Responsible Product Brief | [templates/responsible-product-brief.md](../templates/responsible-product-brief.md) |
| Risk classification checklist | EU AI Act Risk Classification | [checklists/eu-ai-act-risk-classification.yaml](../checklists/eu-ai-act-risk-classification.yaml) |
| Acceptance criteria guide | Defining Acceptance Criteria | [evaluations/defining-acceptance-criteria.md](../evaluations/defining-acceptance-criteria.md) |
| Lifecycle and governance gates | Product Development Lifecycle | [guides/product-development-lifecycle.md](../guides/product-development-lifecycle.md) |
| MVP governance requirements | MVP Governance Add-on | [governance-extensions/mvp-governance-addon.md](mvp-governance-addon.md) |
| Development eval requirements | Eval-Driven Development | [eval-driven-development.md](../../02-development-governance/evaluations/eval-driven-development.md) |
| Pre-deployment checklist | Pre-Deployment Gate | [pre-deployment-gate.yaml](../../02-development-governance/checklists/pre-deployment-gate.yaml) |
| Continuous monitoring | Continuous Online Evaluation | [continuous-online-evaluation.md](../../03-runtime-governance/evaluations/continuous-online-evaluation.md) |
| Quality metrics reference | AI Quality Metrics Catalog | [ai-quality-metrics-catalog.md](../evaluations/ai-quality-metrics-catalog.md) |

---

*Last updated: 2026-02-28*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
*Framework: [Product Governance for Agentic AI Workflows](../../README.md)*
