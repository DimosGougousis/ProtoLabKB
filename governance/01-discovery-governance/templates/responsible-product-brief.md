# Responsible Product Brief Template

## Purpose

This template combines a standard Product Requirements Document (PRD) with built-in governance sections required by the Master AI Governance Framework. It ensures that ethical impact, regulatory classification, data governance, and human oversight requirements are defined alongside business requirements -- not as an afterthought, but as first-class product concerns.

Use this template instead of a standalone PRD whenever the product or feature involves AI/ML/LLM capabilities. The governance sections are mandatory for Limited and High-risk AI systems under the EU AI Act. For Minimal-risk systems, governance sections marked [MINIMAL-RISK: OPTIONAL] may be abbreviated but should not be skipped entirely.

## When to Use

- At the **start of the Discovery phase** for any new AI product or feature
- When an existing product is being augmented with AI capabilities for the first time
- When a material change in scope triggers re-classification (new use case, new data source, new user population)
- As the primary input to the [Discovery Gate](../README.md) review

**Trigger:** A product manager initiates work on an AI-powered product or feature.

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **Product Manager** | **Accountable** -- authors the brief, ensures all sections are completed, presents at Discovery Gate |
| **AI/ML Engineer** | **Responsible** -- contributes to technical feasibility, data requirements, and evaluation approach sections |
| **Ethics Lead / Responsible AI Lead** | **Consulted** -- reviews ethical impact assessment, stakeholder value map, and transparency requirements |
| **Compliance Officer (2nd Line)** | **Consulted** -- validates EU AI Act risk classification, reviews data governance and regulatory sections |
| **AI Governance Committee** | **Approver** -- grants Discovery Gate approval for Limited and High-risk systems |

## Regulatory Basis

- **EU AI Act Articles 9, 13, 14, Annex IV** -- Risk management documentation, transparency, and human oversight obligations
- **EU AI Act Article 6 + Annex III** -- High-risk classification criteria
- **GDPR Articles 13-14, 22, 35** -- Transparency, automated decision-making, and DPIA obligations
- **DORA Article 11** -- ICT risk management requirements for financial entities
- **DNB Good Practice for AI** -- Expectation of documented risk assessment prior to AI deployment

---

## TEMPLATE BEGINS HERE

> **Instructions:** Copy everything below this line into a new document. Replace all `[FILL IN]` placeholders. Delete instructional comments (lines starting with `>`) before finalizing. Sections marked `[MINIMAL-RISK: OPTIONAL]` may be abbreviated for Minimal-risk AI systems but should be completed for Limited and High-risk systems.

---

# Responsible Product Brief: [FILL IN: Product/Feature Name]

| Field | Value |
|-------|-------|
| **Author** | [FILL IN: Name, Role] |
| **Date** | [FILL IN: YYYY-MM-DD] |
| **Version** | [FILL IN: e.g., 1.0] |
| **Status** | Draft / Under Review / Approved / Rejected |
| **Risk Tier** | Minimal / Limited / High / Prohibited |
| **Discovery Gate Target Date** | [FILL IN: YYYY-MM-DD] |

---

## 1. Problem Statement

### 1.1 Problem Description

[FILL IN: What problem does this product solve? Who experiences this problem? What is the current state?]

> *Example (Fraud Detection):* Financial institutions processing card-not-present (CNP) transactions experience fraud rates of 0.12% by volume but 2.3% by value. Current rule-based systems generate a 14:1 false positive ratio, creating customer friction and operational cost. Genuine fraud losses exceed EUR 4.2M annually. An AI-powered fraud detection system would reduce false positives while maintaining or improving fraud catch rates.

### 1.2 Why AI?

[FILL IN: Why is AI/ML/LLM the right approach? What alternatives were considered and why were they insufficient?]

> *Example:* Rule-based systems cannot adapt to evolving fraud patterns without manual rule updates (average 6-week lag). ML models can detect novel fraud patterns in real-time and adapt to behavioral shifts. We evaluated enhanced rule engines and found they plateau at 8:1 false positive ratios.

### 1.3 Why Now?

[FILL IN: What has changed that makes this the right time? Market pressure, regulatory change, technology maturity, competitive threat?]

---

## 2. Users and Stakeholders

### 2.1 Primary Users

| User Segment | Description | Key Need | Volume |
|-------------|-------------|----------|--------|
| [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |

> *Example:*
> | Fraud Analysts | Operations team reviewing flagged transactions | Reduce false positives so they can focus on genuine fraud | 45 analysts, reviewing ~2,000 alerts/day |
> | Cardholders | End customers whose transactions are scored | Seamless payment experience without false declines | 3.2M active cardholders |

### 2.2 Affected Populations

> This section is **mandatory for all risk tiers**. Even Minimal-risk systems affect people.

[FILL IN: Who is affected by this system's decisions, even if they are not direct users? Include populations that may be disproportionately impacted.]

| Affected Population | How They Are Affected | Potential for Disproportionate Impact |
|---------------------|----------------------|--------------------------------------|
| [FILL IN] | [FILL IN] | [FILL IN: Yes/No + explanation] |

> *Example:*
> | International travelers | Higher false decline rates due to unusual location patterns | Yes -- travelers from certain regions may face higher friction |
> | Elderly cardholders | May be flagged for unusual online purchase patterns if newly adopting e-commerce | Yes -- behavioral baselines may not represent this segment |

### 2.3 Stakeholder Value Map

> *Cross-reference: See [stakeholder analysis questions](../governance-extensions/prd-governance-addon.md#stakeholder-impact-analysis) for the full question set.*

Map how this product creates or destroys value for each stakeholder group:

| Stakeholder | Value Created | Value at Risk | Mitigation |
|-------------|--------------|---------------|------------|
| [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |

> *Example:*
> | Cardholders | Reduced fraud losses, faster resolution | False declines, loss of purchasing power, privacy concerns | Human review for high-value declines, opt-out for enhanced monitoring |
> | Fraud Analysts | Better signal-to-noise ratio, reduced alert fatigue | Deskilling if over-reliant on model, job displacement if headcount is reduced | Maintain analyst training, position AI as augmentation not replacement |
> | Merchants | Lower chargeback rates, improved authorization rates | Increased transaction latency if scoring is slow | SLA: scoring adds <50ms to authorization flow |
> | Regulators | Reduced systemic fraud risk, improved compliance posture | Opaque decision-making if model is unexplainable | Provide model cards and explanability reports per EU AI Act Art. 13 |

---

## 3. Success Metrics

> *Cross-reference: See [AI Quality Metrics Catalog](../evaluations/ai-quality-metrics-catalog.md) for the full metrics reference. See [Defining Acceptance Criteria](../evaluations/defining-acceptance-criteria.md) for how to set thresholds.*

### 3.1 Business Metrics

| Metric | Current Baseline | Target | Measurement Method |
|--------|-----------------|--------|-------------------|
| [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |

### 3.2 AI Quality Metrics

| Metric | Threshold | Measurement Frequency | Eval Method |
|--------|-----------|----------------------|-------------|
| [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |

> *Example:*
> | False positive rate | <5:1 ratio (vs. current 14:1) | Daily | Offline eval on labeled transactions |
> | Fraud detection rate (recall) | >=95% of fraud by value caught | Daily | Comparison against confirmed fraud cases |
> | Fairness (demographic parity) | <2% variance in false decline rate across demographic groups | Monthly | Bias audit using [pre-deployment gate](../../02-development-governance/checklists/pre-deployment-gate.yaml) |
> | Latency (P99) | <50ms scoring time | Continuous | APM monitoring |

### 3.3 Governance Metrics

| Metric | Target | Purpose |
|--------|--------|---------|
| Explainability coverage | [FILL IN: % of decisions with explanation available] | EU AI Act Art. 13 compliance |
| Human override rate | [FILL IN: expected range] | Validate human oversight is functional |
| Audit trail completeness | 100% of decisions logged with inputs, outputs, and model version | DORA Art. 11, EU AI Act Art. 12 |

---

## 4. Requirements

### 4.1 Functional Requirements

| ID | Requirement | Priority | Acceptance Criterion |
|----|-------------|----------|---------------------|
| FR-001 | [FILL IN] | Must / Should / Could | [FILL IN] |

### 4.2 Non-Functional Requirements

| ID | Requirement | Target | Measurement |
|----|-------------|--------|-------------|
| NFR-001 | [FILL IN] | [FILL IN] | [FILL IN] |

### 4.3 Constraints

[FILL IN: Technical, regulatory, organizational, budgetary, or timeline constraints that shape the solution.]

---

## 5. Ethical Impact Assessment

> **Required for all risk tiers.** Depth of analysis scales with risk tier.
> *Cross-reference: See [ethical considerations checklist](../governance-extensions/prd-governance-addon.md#ethical-considerations-checklist) for the full question set.*

### 5.1 Potential Harms

For each harm category, assess whether this product could cause harm and describe the mechanism:

| Harm Category | Applicable? | Description | Severity | Likelihood | Mitigation |
|---------------|-------------|-------------|----------|------------|------------|
| **Discrimination / Bias** | [Yes/No] | [FILL IN] | [Low/Med/High/Critical] | [Low/Med/High] | [FILL IN] |
| **Privacy Violation** | [Yes/No] | [FILL IN] | [Low/Med/High/Critical] | [Low/Med/High] | [FILL IN] |
| **Financial Harm** | [Yes/No] | [FILL IN] | [Low/Med/High/Critical] | [Low/Med/High] | [FILL IN] |
| **Loss of Autonomy** | [Yes/No] | [FILL IN] | [Low/Med/High/Critical] | [Low/Med/High] | [FILL IN] |
| **Manipulation / Deception** | [Yes/No] | [FILL IN] | [Low/Med/High/Critical] | [Low/Med/High] | [FILL IN] |
| **Safety / Physical Harm** | [Yes/No] | [FILL IN] | [Low/Med/High/Critical] | [Low/Med/High] | [FILL IN] |
| **Environmental Impact** | [Yes/No] | [FILL IN] | [Low/Med/High/Critical] | [Low/Med/High] | [FILL IN] |
| **Erosion of Social Trust** | [Yes/No] | [FILL IN] | [Low/Med/High/Critical] | [Low/Med/High] | [FILL IN] |

> *Example (Fraud Detection):*
> | **Discrimination / Bias** | Yes | Model may learn geographic or behavioral proxies for ethnicity or age, resulting in higher false decline rates for certain demographic groups. | High | Medium | Monthly bias audits on false decline rates segmented by demographic proxies; mandatory fairness thresholds in eval suite. |
> | **Financial Harm** | Yes | False declines cause direct financial harm to cardholders who cannot complete legitimate purchases. | Medium | High | Human review for declines above EUR 500; customer appeal process with 24-hour SLA. |

### 5.2 Irreversibility Assessment

[FILL IN: Can the system's decisions be reversed? What is the cost of reversal? What is the window for correction?]

> *Example:* Transaction blocks can be reversed within seconds by fraud analysts. However, repeated false declines may cause merchants to lose customers permanently -- this reputational harm is difficult to reverse.

### 5.3 Power Asymmetry Analysis

[FILL IN: Does this system create or reinforce a power imbalance between the organization and affected individuals? How?]

> *Example:* Cardholders have limited ability to understand why a transaction was declined. The organization holds all the information (model scores, feature importance) while the cardholder receives only a binary outcome. Mitigation: provide decline reason codes per EU AI Act Art. 13 transparency requirements.

---

## 6. EU AI Act Risk Classification

> **Required for all AI systems.** Complete the full [EU AI Act Risk Classification Checklist](../checklists/eu-ai-act-risk-classification.yaml) and summarize results here.
> *Cross-reference: See [risk classification questions](../governance-extensions/prd-governance-addon.md#risk-classification-questions) for PRD-phase classification guidance.*

### 6.1 Classification Summary

| Question | Answer |
|----------|--------|
| Is this system in a prohibited category (Art. 5)? | [FILL IN: Yes/No -- if Yes, STOP] |
| Does this system fall under Annex III high-risk categories? | [FILL IN: Yes/No + which category] |
| Is this system a safety component of a product covered by Union harmonisation legislation? | [FILL IN: Yes/No] |
| Does this system interact with natural persons (chatbot, emotion recognition, biometric categorization, deep fake)? | [FILL IN: Yes/No -- if Yes, Limited risk at minimum] |
| **Determined Risk Tier** | **[FILL IN: Minimal / Limited / High / Prohibited]** |

### 6.2 Classification Rationale

[FILL IN: Explain the reasoning behind the risk tier determination. Reference specific EU AI Act articles and Annex III categories.]

> *Example:* The fraud detection system evaluates natural persons' creditworthiness and determines access to financial services (Annex III, point 5(b)). This classifies it as **High-risk** under EU AI Act Article 6(2). Additionally, the system processes personal transaction data, triggering GDPR Article 35 DPIA requirements.

### 6.3 Governance Intensity Implications

Based on the risk tier, the following governance requirements apply:

| Governance Area | Minimal | Limited | High |
|----------------|---------|---------|------|
| Documentation depth | Summary | Standard | Comprehensive |
| Eval suite scope | Core metrics | Core + fairness | Core + fairness + robustness + explainability |
| Human oversight model | HOTA permitted | HOTL minimum | HITL required for critical decisions |
| Monitoring frequency | Monthly | Weekly | Continuous |
| Audit cadence | Annual | Semi-annual | Quarterly |
| Incident response SLA | 72 hours | 24 hours | 4 hours |

---

## 7. Data Governance Requirements

> *Cross-reference: See [data provenance requirements](../governance-extensions/prd-governance-addon.md#data-provenance-requirements) for the full data governance question set.*

### 7.1 Data Inventory

| Data Source | Data Type | Personal Data? | Special Category? | Lawful Basis | Retention Period |
|-------------|-----------|---------------|-------------------|-------------|-----------------|
| [FILL IN] | [FILL IN] | [Yes/No] | [Yes/No] | [FILL IN: GDPR Art. 6 basis] | [FILL IN] |

> *Example:*
> | Transaction history (12 months) | Structured -- amount, merchant, location, timestamp | Yes | No | Legitimate interest (fraud prevention) | 5 years (regulatory) |
> | Device fingerprint data | Semi-structured -- device ID, IP, browser | Yes | No | Legitimate interest (fraud prevention) | 90 days |
> | Confirmed fraud labels | Structured -- boolean, investigation notes | Yes | No | Legal obligation (AML reporting) | 7 years |

### 7.2 Data Quality Requirements

| Requirement | Standard | Measurement |
|-------------|----------|-------------|
| Completeness | [FILL IN: % of required fields populated] | [FILL IN] |
| Accuracy | [FILL IN: error rate threshold] | [FILL IN] |
| Timeliness | [FILL IN: max data age at scoring time] | [FILL IN] |
| Label quality | [FILL IN: label accuracy for training data] | [FILL IN] |
| Representativeness | [FILL IN: demographic coverage requirements] | [FILL IN] |

### 7.3 Data Provenance

[FILL IN: Where does each data source come from? What is the chain of custody? Are there third-party data providers? What contracts govern data use?]

---

## 8. Transparency Requirements

> **Required for Limited and High-risk systems.** EU AI Act Art. 13 mandates transparency for high-risk systems; Art. 52 mandates disclosure for certain limited-risk systems (chatbots, emotion recognition, deep fakes).

### 8.1 Disclosure Obligations

| Disclosure Type | Required? | Implementation Plan |
|----------------|-----------|-------------------|
| AI disclosure (users must know they are interacting with AI) | [FILL IN: Yes/No] | [FILL IN] |
| Decision explanation (users must understand the basis for decisions affecting them) | [FILL IN: Yes/No] | [FILL IN] |
| Right to human review (users must be able to request human intervention) | [FILL IN: Yes/No] | [FILL IN] |
| Data processing transparency (users must know what data is used) | [FILL IN: Yes/No] | [FILL IN] |

### 8.2 Explainability Approach

[FILL IN: What level of explainability will this system provide? What methods will be used (feature importance, counterfactual explanations, natural language explanations)?]

> *Example:* The fraud detection system will provide: (1) top-3 contributing factors for each fraud score as feature importance values, (2) reason codes mapped to human-readable decline reasons for cardholder-facing communications, (3) full SHAP value explanations available to fraud analysts in the review interface.

### 8.3 Model Card Commitment

[FILL IN: Will a model card be produced? What sections will it cover? When will it be published?]

> *Cross-reference: Model cards are produced during Development Governance. See [eval-driven development](../../02-development-governance/evaluations/eval-driven-development.md) for model card requirements.*

---

## 9. Human Oversight Model

> **Required for all risk tiers.** The level of human oversight must be proportionate to risk.

### 9.1 Oversight Model Selection

Select the human oversight model for this system:

| Model | Description | When Appropriate |
|-------|-------------|-----------------|
| **HITL** (Human-in-the-Loop) | A human reviews and approves every AI output before it takes effect. | High-risk decisions with significant individual impact (e.g., loan denial, account closure). |
| **HOTL** (Human-on-the-Loop) | AI acts autonomously but a human monitors outputs and can intervene. | Medium-risk decisions where speed matters but oversight is needed (e.g., fraud alerts, transaction scoring). |
| **HOTA** (Human-out-of-the-Loop) | AI acts fully autonomously. Human oversight is periodic and retrospective. | Low-risk, high-volume decisions where latency requirements preclude real-time human review (e.g., spam filtering, content categorization). |

**Selected Model:** [FILL IN: HITL / HOTL / HOTA]

**Justification:** [FILL IN: Why is this the right level of oversight for the risk profile of this system?]

> *Example:* **HOTL** -- Fraud scoring is HOTL: the model scores transactions autonomously in real-time (<50ms), but fraud analysts review all transactions flagged above the alert threshold. For declines above EUR 5,000, the system escalates to HITL: a senior analyst must approve the decline before it takes effect. Below the alert threshold, the system operates HOTA for the scoring function, with monthly retrospective audits.

### 9.2 Override Mechanisms

[FILL IN: How can a human override the system's decision? What is the process? What is logged?]

### 9.3 Escalation Triggers

| Trigger | Escalation Path | Response SLA |
|---------|----------------|-------------|
| [FILL IN] | [FILL IN] | [FILL IN] |

> *Cross-reference: Escalation policies are detailed in [Runtime Governance](../../03-runtime-governance/). Define triggers here; implement escalation flows there.*

---

## 10. Evaluation Strategy Overview

> *Cross-reference: The full evaluation strategy is documented in the [Evaluation Strategy Template](../evaluations/evaluation-strategy-template.yaml). This section provides a summary for the product brief.*

### 10.1 Pre-Deployment Evaluation

[FILL IN: What evaluations must pass before this system goes live? Reference the acceptance criteria from Section 3.]

### 10.2 Post-Deployment Evaluation

[FILL IN: What continuous evaluations will monitor this system in production? What thresholds trigger alerts or rollback?]

> *Cross-reference: See [continuous online evaluation](../../03-runtime-governance/evaluations/continuous-online-evaluation.md) for the full post-deployment evaluation framework.*

### 10.3 Periodic Re-Evaluation

[FILL IN: How often will this system undergo comprehensive re-evaluation? What triggers an ad-hoc re-evaluation?]

---

## 11. Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation | Owner |
|------|-----------|--------|------------|-------|
| [FILL IN] | [Low/Med/High] | [Low/Med/High] | [FILL IN] | [FILL IN: Role] |

---

## 12. Dependencies and Constraints

### 12.1 Technical Dependencies

[FILL IN: Infrastructure, APIs, data pipelines, model serving infrastructure, third-party services.]

### 12.2 Organizational Dependencies

[FILL IN: Teams, approvals, budget, hiring, training.]

### 12.3 Regulatory Dependencies

[FILL IN: Pending regulatory guidance, ongoing supervisory dialogue, regulatory sandbox participation.]

---

## 13. Timeline and Milestones

| Milestone | Target Date | Governance Gate |
|-----------|------------|----------------|
| Discovery Gate approval | [FILL IN] | [Discovery Gate](../README.md) |
| Development complete | [FILL IN] | [Pre-deployment Gate](../../02-development-governance/checklists/pre-deployment-gate.yaml) |
| Production deployment | [FILL IN] | Go-live approval |
| First quarterly review | [FILL IN] | [Continuous evaluation](../../03-runtime-governance/evaluations/continuous-online-evaluation.md) baseline established |

---

## 14. Appendices

### Appendix A: Discovery Gate Readiness Checklist

Before submitting this brief for Discovery Gate review, verify:

- [ ] All `[FILL IN]` placeholders have been replaced with actual content
- [ ] EU AI Act risk classification checklist completed ([link](../checklists/eu-ai-act-risk-classification.yaml))
- [ ] Ethical impact assessment (Section 5) reviewed by Ethics Lead
- [ ] Data governance requirements (Section 7) reviewed by Data Protection Officer
- [ ] Human oversight model (Section 9) justified and documented
- [ ] Acceptance criteria (Section 3) are measurable and have defined thresholds
- [ ] Evaluation strategy template completed ([link](../evaluations/evaluation-strategy-template.yaml))
- [ ] Stakeholder value map (Section 2.3) includes all affected parties
- [ ] Cross-references to Development and Runtime governance artifacts confirmed

### Appendix B: Governance Artifact Cross-Reference Map

| This Brief Section | Related Framework Artifact | Pillar |
|-------------------|---------------------------|--------|
| Section 3 (Success Metrics) | [Defining Acceptance Criteria](../evaluations/defining-acceptance-criteria.md) | Discovery |
| Section 3 (Success Metrics) | [AI Quality Metrics Catalog](../evaluations/ai-quality-metrics-catalog.md) | Discovery |
| Section 5 (Ethical Impact) | [PRD Governance Add-on](../governance-extensions/prd-governance-addon.md) | Discovery |
| Section 6 (Risk Classification) | [EU AI Act Risk Classification](../checklists/eu-ai-act-risk-classification.yaml) | Discovery |
| Section 8 (Transparency) | [Eval-Driven Development](../../02-development-governance/evaluations/eval-driven-development.md) | Development |
| Section 9 (Human Oversight) | [Continuous Online Evaluation](../../03-runtime-governance/evaluations/continuous-online-evaluation.md) | Runtime |
| Section 10 (Evaluation Strategy) | [Evaluation Strategy Template](../evaluations/evaluation-strategy-template.yaml) | Discovery |
| Section 10 (Evaluation Strategy) | [Eval Gate Integration](../../02-development-governance/evaluations/eval-gate-integration.md) | Development |
| Section 10 (Post-Deployment) | [Continuous Online Evaluation](../../03-runtime-governance/evaluations/continuous-online-evaluation.md) | Runtime |

---

*Template version: 1.0*
*Last updated: 2026-02-28*
*Classification: Internal / Regulatory Preparation*
*Framework: [Product Governance for Agentic AI Workflows](../../README.md)*
