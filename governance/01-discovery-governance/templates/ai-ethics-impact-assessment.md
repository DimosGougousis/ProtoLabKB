# AI Ethics Impact Assessment

> **Master AI Governance Framework -- Discovery Pillar**
> Template for ethical impact analysis before building an AI product.

| Field            | Value                                |
|------------------|--------------------------------------|
| **Framework**    | Master AI Governance Framework       |
| **Pillar**       | 01-Discovery                         |
| **Artifact**     | AI Ethics Impact Assessment Template |
| **Version**      | 1.0.0                                |
| **Last Updated** | 2026-02-28                           |
| **Owner**        | AI Ethics & Governance Office        |

**Cross-references:**
- [`../checklists/ethical-product-discovery.yaml`](../checklists/ethical-product-discovery.yaml) -- Pre-build ethics checklist
- [`../checklists/user-agency-assessment.yaml`](../checklists/user-agency-assessment.yaml) -- User agency scoring
- [`../templates/stakeholder-value-map.md`](../templates/stakeholder-value-map.md) -- Stakeholder analysis detail
- [`../../02-development-governance/`](../../02-development-governance/) -- Development-phase controls
- [`../../03-runtime-governance/`](../../03-runtime-governance/) -- Runtime monitoring
- [`../../04-operational-governance/`](../../04-operational-governance/) -- Incident and audit

---

## 1. Assessment Metadata

| Field                    | Value                                    |
|--------------------------|------------------------------------------|
| **Product / Feature**    | [FILL IN: Product or feature name]       |
| **Product Owner**        | [FILL IN: Name and role]                 |
| **Assessment Author**    | [FILL IN: Name and role]                 |
| **Assessment Date**      | [FILL IN: YYYY-MM-DD]                    |
| **AI System Type**       | [FILL IN: e.g., classification, generation, agentic workflow] |
| **EU AI Act Risk Class** | [FILL IN: Unacceptable / High / Limited / Minimal] |
| **Regulatory Scope**     | [FILL IN: e.g., EU AI Act, FCA, SEC, ECOA] |
| **Version**              | [FILL IN: Assessment version, e.g., 1.0] |
| **Status**               | [FILL IN: Draft / In Review / Approved / Rejected] |

### Reviewers

| Role                    | Name           | Review Date | Decision          |
|-------------------------|----------------|-------------|-------------------|
| Ethics Board Chair      | [FILL IN]      | [FILL IN]   | [Pending/Approved/Rejected] |
| Product Manager         | [FILL IN]      | [FILL IN]   | [Pending/Approved/Rejected] |
| Compliance Officer      | [FILL IN]      | [FILL IN]   | [Pending/Approved/Rejected] |
| Data Protection Officer | [FILL IN]      | [FILL IN]   | [Pending/Approved/Rejected] |
| Engineering Lead        | [FILL IN]      | [FILL IN]   | [Pending/Approved/Rejected] |

---

## 2. Purpose and Necessity

### 2.1 Problem Statement

[FILL IN: What problem does this AI system solve? Why is AI necessary -- could the problem be solved without AI? What is the cost of NOT building this system?]

### 2.2 Intended Purpose

[FILL IN: The specific, bounded purpose of the AI system. Per EU AI Act Art. 9, the purpose must be clearly defined and documented.]

### 2.3 Necessity and Proportionality

| Question | Answer |
|----------|--------|
| Could this problem be solved without AI? | [FILL IN] |
| What is the marginal benefit of AI over non-AI approaches? | [FILL IN] |
| Is the complexity and risk of AI proportionate to the benefit? | [FILL IN] |
| What is the minimum viable AI needed (simplest model that delivers value)? | [FILL IN] |

**Risk Rating:** [High / Medium / Low]

> **Example -- Credit Scoring AI:** The problem (credit assessment) can be solved without AI using manual underwriting, but AI reduces processing time from 5 days to 15 minutes and may reduce human bias in initial screening. The marginal benefit is substantial for high-volume lending. A logistic regression model is the minimum viable approach before considering neural networks.

---

## 3. Stakeholder Analysis

*Reference: [`../templates/stakeholder-value-map.md`](../templates/stakeholder-value-map.md) for full stakeholder mapping.*

### 3.1 Who Benefits?

| Stakeholder Group     | Benefit                              | Magnitude |
|-----------------------|--------------------------------------|-----------|
| [FILL IN: e.g., Loan applicants] | [FILL IN: e.g., Faster decisions] | [High/Medium/Low] |
| [FILL IN]             | [FILL IN]                            | [FILL IN] |
| [FILL IN]             | [FILL IN]                            | [FILL IN] |

### 3.2 Who Is Harmed or At Risk?

| Stakeholder Group     | Potential Harm                       | Severity  | Mitigation |
|-----------------------|--------------------------------------|-----------|------------|
| [FILL IN: e.g., Thin-file applicants] | [FILL IN: e.g., Unfair denial] | [High/Medium/Low] | [FILL IN] |
| [FILL IN]             | [FILL IN]                            | [FILL IN] | [FILL IN] |
| [FILL IN]             | [FILL IN]                            | [FILL IN] | [FILL IN] |

### 3.3 Who Is Excluded?

[FILL IN: Identify groups who cannot access or use the AI system. Consider digital literacy, language, disability, internet access, and documentation requirements.]

**Risk Rating:** [High / Medium / Low]

> **Example -- Credit Scoring AI:** Primary beneficiaries are applicants with strong credit histories (faster approvals) and the bank (lower processing costs). At-risk groups include thin-file applicants (immigrants, young adults) who may be systematically scored lower due to limited data. Excluded groups include individuals without digital access who cannot use the online application.

---

## 4. Bias Risk Assessment

### 4.1 Protected Characteristics

| Characteristic | Relevant? | Proxy Features Identified | Mitigation |
|---------------|-----------|--------------------------|------------|
| Race / Ethnicity | [Yes/No] | [FILL IN: e.g., zip code, name] | [FILL IN] |
| Gender | [Yes/No] | [FILL IN] | [FILL IN] |
| Age | [Yes/No] | [FILL IN] | [FILL IN] |
| Disability | [Yes/No] | [FILL IN] | [FILL IN] |
| Religion | [Yes/No] | [FILL IN] | [FILL IN] |
| Socioeconomic Status | [Yes/No] | [FILL IN] | [FILL IN] |

### 4.2 Bias Sources

| Stage | Bias Risk | Description | Mitigation |
|-------|-----------|-------------|------------|
| Problem Framing | [High/Medium/Low] | [FILL IN: Is the problem framed in a way that inherently disadvantages some groups?] | [FILL IN] |
| Data Collection | [High/Medium/Low] | [FILL IN: Does the training data under-represent or misrepresent groups?] | [FILL IN] |
| Feature Selection | [High/Medium/Low] | [FILL IN: Do features encode protected characteristics?] | [FILL IN] |
| Model Training | [High/Medium/Low] | [FILL IN: Does the optimization objective embed bias?] | [FILL IN] |
| Deployment | [High/Medium/Low] | [FILL IN: Does the deployment context change who is affected?] | [FILL IN] |
| Feedback Loops | [High/Medium/Low] | [FILL IN: Does the system's output influence future training data?] | [FILL IN] |

### 4.3 Fairness Metrics

| Metric | Selected? | Justification | Target Value |
|--------|-----------|---------------|--------------|
| Demographic Parity | [Yes/No] | [FILL IN] | [FILL IN] |
| Equalized Odds | [Yes/No] | [FILL IN] | [FILL IN] |
| Predictive Parity | [Yes/No] | [FILL IN] | [FILL IN] |
| Calibration | [Yes/No] | [FILL IN] | [FILL IN] |
| Individual Fairness | [Yes/No] | [FILL IN] | [FILL IN] |

**Risk Rating:** [High / Medium / Low]

---

## 5. Data Ethics

### 5.1 Data Sources

| Source | Type | Collection Method | Consent Basis | GDPR Lawful Basis | Restrictions |
|--------|------|-------------------|---------------|-------------------|-------------|
| [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN: Art. 6(1)(a-f)] | [FILL IN] |
| [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |

### 5.2 Data Ethics Checklist

| Question | Answer | Evidence |
|----------|--------|----------|
| Is all data ethically sourced with documented provenance? | [FILL IN] | [FILL IN] |
| Has data minimization been verified? | [FILL IN] | [FILL IN] |
| Are data subjects aware their data is used for AI training? | [FILL IN] | [FILL IN] |
| Can data subjects request deletion (right to erasure)? | [FILL IN] | [FILL IN] |
| Is third-party data vendor due diligence complete? | [FILL IN] | [FILL IN] |
| Is special category data (Art. 9 GDPR) involved? | [FILL IN] | [FILL IN] |
| Is data retention limited to necessary duration? | [FILL IN] | [FILL IN] |

**Risk Rating:** [High / Medium / Low]

---

## 6. Transparency Plan

### 6.1 Disclosure Strategy

| Audience | What Is Disclosed | How | When |
|----------|-------------------|-----|------|
| End Users | [FILL IN: AI involvement, scope, limitations] | [FILL IN: In-app notice, email, label] | [FILL IN: Before interaction] |
| Regulators | [FILL IN: Model documentation, bias reports] | [FILL IN: Regulatory filing, audit package] | [FILL IN: On request, quarterly] |
| Internal Teams | [FILL IN: Model cards, performance dashboards] | [FILL IN: Internal wiki, dashboards] | [FILL IN: Continuous] |
| Affected Non-Users | [FILL IN: How decisions about them are communicated] | [FILL IN: Notification letter, portal] | [FILL IN: At point of decision] |

### 6.2 Explainability Approach

| Stakeholder | Technique | Granularity | Format |
|-------------|-----------|-------------|--------|
| End Users | [FILL IN: e.g., Top-3 factors, counterfactuals] | [Per-decision] | [Plain language] |
| Regulators | [FILL IN: e.g., SHAP values, model cards] | [Model-level and per-decision] | [Technical report] |
| Internal Auditors | [FILL IN: e.g., Full feature importance, decision logs] | [Per-decision] | [Dashboard + logs] |

**Risk Rating:** [High / Medium / Low]

---

## 7. Accountability Structure

### 7.1 RACI Matrix

| Responsibility | Accountable | Responsible | Consulted | Informed |
|---------------|-------------|-------------|-----------|----------|
| Model Accuracy | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |
| Bias Monitoring | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |
| User Complaints | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |
| Regulatory Compliance | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |
| Incident Response | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |
| Data Governance | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |

### 7.2 Escalation Path

```
L1: Automated monitoring detects anomaly
    |
L2: ML Engineer investigates (SLA: 4 hours)
    |
L3: Product Manager + Compliance notified (SLA: 24 hours)
    |
L4: Ethics Board convened (SLA: 48 hours for high-risk)
    |
L5: Executive sponsor / Board notification (critical incidents)
```

**Risk Rating:** [High / Medium / Low]

---

## 8. Societal Impact

| Dimension | Assessment | Severity | Mitigation |
|-----------|-----------|----------|------------|
| Financial Inclusion | [FILL IN: Does the AI broaden or narrow access to financial services?] | [High/Medium/Low] | [FILL IN] |
| Market Stability | [FILL IN: Could widespread adoption destabilize markets?] | [High/Medium/Low] | [FILL IN] |
| Employment | [FILL IN: Which roles are displaced? What is the transition plan?] | [High/Medium/Low] | [FILL IN] |
| Digital Divide | [FILL IN: Does the AI disadvantage digitally excluded populations?] | [High/Medium/Low] | [FILL IN] |
| Trust in Financial System | [FILL IN: Does the AI erode or build public trust in finance?] | [High/Medium/Low] | [FILL IN] |

**Risk Rating:** [High / Medium / Low]

---

## 9. Environmental Impact

| Factor | Estimate | Methodology | Proportionality Check |
|--------|----------|-------------|----------------------|
| Training Compute (CO2e) | [FILL IN: e.g., 50 kg CO2e] | [FILL IN: Tool used, e.g., CodeCarbon] | [FILL IN: Justified by value delivered?] |
| Inference Compute (annual CO2e) | [FILL IN] | [FILL IN] | [FILL IN] |
| Hardware Lifecycle | [FILL IN: GPU/TPU procurement, end-of-life] | [FILL IN] | [FILL IN] |
| Data Storage | [FILL IN: Storage footprint over retention period] | [FILL IN] | [FILL IN] |

**Risk Rating:** [High / Medium / Low]

---

## 10. Human Oversight Plan

### 10.1 Oversight Model Selection

| Criterion | HITL (Human-in-the-Loop) | HOTL (Human-on-the-Loop) | HOTA (Human-over-the-Loop) |
|-----------|-------------------------|-------------------------|---------------------------|
| Description | Human approves every decision | Human monitors and can intervene | Human sets policy, reviews periodically |
| Risk Level | High-risk decisions | Medium-risk decisions | Low-risk decisions |
| Latency Tolerance | Seconds to minutes acceptable | Real-time preferred | Near real-time required |
| Volume | Low to medium | Medium to high | High volume |

**Selected Model:** [FILL IN: HITL / HOTL / HOTA and justification]

### 10.2 Oversight Implementation

| Element | Design | Evidence |
|---------|--------|----------|
| Who performs oversight? | [FILL IN: Role, qualifications, training] | [FILL IN] |
| What triggers human review? | [FILL IN: Thresholds, edge cases, random sampling] | [FILL IN] |
| How is automation complacency prevented? | [FILL IN: Calibration exercises, justification requirements] | [FILL IN] |
| What tools support the overseer? | [FILL IN: Dashboards, explanation interfaces] | [FILL IN] |
| What is the override SLA? | [FILL IN: Time from flag to human decision] | [FILL IN] |

**Risk Rating:** [High / Medium / Low]

> **Example -- Credit Scoring AI:** HITL for all loan approvals above $50,000 and all denials for protected-class applicants flagged by the bias monitor. HOTL for approvals under $50,000 with random 10% human audit. Human reviewers are senior credit analysts with annual AI oversight training. Automation complacency is mitigated by requiring reviewers to document independent rationale for any agreement with the AI.

---

## 11. Risk Summary

| Section | Risk Rating | Key Risks | Key Mitigations |
|---------|-------------|-----------|-----------------|
| Purpose & Necessity | [H/M/L] | [FILL IN] | [FILL IN] |
| Stakeholder Impact | [H/M/L] | [FILL IN] | [FILL IN] |
| Bias Risk | [H/M/L] | [FILL IN] | [FILL IN] |
| Data Ethics | [H/M/L] | [FILL IN] | [FILL IN] |
| Transparency | [H/M/L] | [FILL IN] | [FILL IN] |
| Accountability | [H/M/L] | [FILL IN] | [FILL IN] |
| Societal Impact | [H/M/L] | [FILL IN] | [FILL IN] |
| Environmental Impact | [H/M/L] | [FILL IN] | [FILL IN] |
| Human Oversight | [H/M/L] | [FILL IN] | [FILL IN] |

**Overall Risk Rating:** [FILL IN: High / Medium / Low]

**Recommendation:** [FILL IN: Proceed / Proceed with Conditions / Do Not Proceed]

---

## 12. Sign-Off

| Role | Name | Signature | Date | Decision |
|------|------|-----------|------|----------|
| Ethics Board Chair | [FILL IN] | _________ | [FILL IN] | [Approve / Conditional / Reject] |
| Product Manager | [FILL IN] | _________ | [FILL IN] | [Acknowledge risks and mitigations] |
| Compliance Officer | [FILL IN] | _________ | [FILL IN] | [Regulatory clearance granted / denied] |
| Data Protection Officer | [FILL IN] | _________ | [FILL IN] | [DPIA complete / required] |
| Engineering Lead | [FILL IN] | _________ | [FILL IN] | [Technical feasibility of mitigations] |

### Conditions for Approval (if applicable)

| # | Condition | Owner | Deadline | Status |
|---|-----------|-------|----------|--------|
| 1 | [FILL IN] | [FILL IN] | [FILL IN] | [Open / Closed] |
| 2 | [FILL IN] | [FILL IN] | [FILL IN] | [Open / Closed] |

### Next Review Date

[FILL IN: Date for mandatory reassessment. Maximum interval: 12 months or upon material change to the AI system, whichever is sooner.]

---

*This template is part of the Master AI Governance Framework. Updates are managed by the AI Ethics & Governance Office. For questions or feedback, contact the framework maintainers.*
