# Bias Assessment Report Template

## Purpose

This template provides a standardized format for documenting the results of fairness and bias analysis performed on AI systems. A completed bias assessment report is required evidence for the [Pre-Deployment Gate](../checklists/pre-deployment-gate.yaml) for all limited-risk and high-risk AI systems, and is recommended as best practice for minimal-risk systems that influence outcomes for individuals.

The report captures the full lifecycle of bias evaluation: which protected attributes were tested, which fairness metrics were applied, what disparities were discovered, what mitigations were implemented, and what residual risk remains. It serves as a regulatory compliance artifact, an internal governance record, and a communication tool for stakeholders who need to understand the fairness profile of the system.

This template is designed to work in conjunction with the [Bias and Fairness Evals](../evaluations/bias-and-fairness-evals.md) methodology guide and the [Bias Testing Checklist](../checklists/bias-testing-checklist.yaml).

## When to Use

- When completing fairness evaluation for any AI system classified as limited or high risk
- When preparing the evidence package for the Pre-Deployment Gate
- When performing periodic revalidation of a deployed model's fairness profile
- When a monitoring alert indicates potential fairness drift in production
- When responding to a regulatory inquiry about fairness testing
- When performing fairness evaluation after retraining on new data

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **AI/ML Engineer** | **Responsible** -- executes bias tests, compiles results, drafts the report |
| **Model Owner** | **Accountable** -- reviews the report, decides on mitigations, signs off on residual risk |
| **Compliance Officer (2nd Line)** | **Reviewer** -- independently validates the methodology and results for limited/high-risk systems |
| **AI Ethics Lead** | **Consulted** -- advises on metric selection, threshold calibration, and mitigation strategies |
| **Product Manager** | **Consulted** -- validates that fairness constraints are compatible with product requirements |
| **AI Governance Committee** | **Approver** -- reviews bias assessment as part of deployment approval for high-risk systems |

## Regulatory Basis

- **EU AI Act Article 10(2f)** -- Training data must be examined for possible biases that could lead to discrimination
- **EU AI Act Article 9** -- Risk management must address risks of bias and discrimination
- **EU AI Act Recital 44** -- High-risk AI systems designed to minimise risks of biased outputs
- **EU AI Act Article 13** -- Transparency about system limitations including bias
- **SAFEST items F-01** (fairness definition), **F-02** (protected attributes), **F-03** (bias testing), **F-04** (disparate impact analysis)
- **ECOA (Equal Credit Opportunity Act)** -- Prohibits discrimination in credit decisions
- **GDPR Article 22** -- Right not to be subject to fully automated decisions with legal effects
- **DNB Good Practice** -- Explicit expectation of bias testing in model validation
- **ISO/IEC 42001 Clause 6.1.2** -- Addressing AI-specific risks including bias

---

## Template Instructions

- Replace all `[FILL IN]` placeholders with information specific to your system and analysis
- Complete all sections; mark any section "Not Applicable" with a documented rationale
- Include actual numeric results, not just descriptions -- this report must contain evidence
- Store the report alongside the model artifacts and reference it in the model card
- Archive previous versions when the report is updated after revalidation

---

# Bias Assessment Report: [FILL IN: System Name]

## Document Metadata

| Field | Value |
|-------|-------|
| **Report Version** | [FILL IN: e.g., 1.0] |
| **System Name** | [FILL IN] |
| **System Version** | [FILL IN: model version, commit SHA, or deployment ID] |
| **Model Card Reference** | [FILL IN: link to model card] |
| **Risk Classification** | [FILL IN: Minimal / Limited / High] |
| **Assessment Date** | [FILL IN: YYYY-MM-DD] |
| **Assessment Type** | [FILL IN: Pre-deployment / Periodic revalidation / Triggered investigation] |
| **Prepared By** | [FILL IN: Name and role] |
| **Reviewed By** | [FILL IN: Name(s) and role(s)] |
| **Approval Status** | [Draft / Under Review / Approved / Action Required] |

---

## 1. Scope of Assessment

### 1.1 System Description

[FILL IN: Brief description of the AI system, its purpose, and the decisions or outputs it produces that could have differential impact across groups.]

### 1.2 Decision Type and Impact

| Field | Value |
|-------|-------|
| **Decision type** | [FILL IN: e.g., credit approval, risk scoring, content generation, customer routing] |
| **Impact level** | [FILL IN: e.g., material financial impact / service quality / informational only] |
| **Affected population** | [FILL IN: e.g., loan applicants, existing customers, all users] |
| **Estimated affected individuals** | [FILL IN: e.g., ~50,000 applicants per year] |
| **Jurisdiction** | [FILL IN: e.g., EU (Netherlands), UK, US] |

### 1.3 Assessment Scope

| Scope Dimension | Details |
|-----------------|---------|
| **Protected attributes tested** | [FILL IN: list all] |
| **Intersectional groups tested** | [FILL IN: list pairwise or higher-order intersections] |
| **Metrics applied** | [FILL IN: list all fairness metrics used] |
| **Data sources** | [FILL IN: test data sources and their provenance] |
| **Time period covered** | [FILL IN: data collection or test period] |
| **Components tested** | [FILL IN: full pipeline / model only / specific component] |

---

## 2. Protected Attributes Tested

### 2.1 Direct Attributes

| Attribute | Legal Basis | Groups Tested | Sample Size per Group | Data Source |
|-----------|------------|---------------|----------------------|-------------|
| [FILL IN: e.g., Gender] | [FILL IN: EU Gender Equality Directive] | [FILL IN: Male (n=X), Female (n=X), Non-binary (n=X)] | [FILL IN] | [FILL IN] |
| [FILL IN: e.g., Age band] | [FILL IN: Employment Equality Directive] | [FILL IN: 18-25 (n=X), 26-35 (n=X), ...] | [FILL IN] | [FILL IN] |
| [FILL IN: e.g., Nationality] | [FILL IN: Racial Equality Directive] | [FILL IN] | [FILL IN] | [FILL IN] |

### 2.2 Proxy Variables Analyzed

| Proxy Variable | Protected Attribute Proxied | Correlation Strength | Action Taken |
|---------------|----------------------------|---------------------|-------------|
| [FILL IN: e.g., Postal code] | [FILL IN: e.g., Ethnicity, Income] | [FILL IN: e.g., Pearson r=0.42] | [FILL IN: e.g., Feature removed / monitored / retained with justification] |
| [FILL IN: e.g., University attended] | [FILL IN: e.g., Socioeconomic status] | [FILL IN] | [FILL IN] |

---

## 3. Fairness Metrics and Results

### 3.1 Demographic Parity

Demographic parity (statistical parity) measures whether the positive outcome rate is equal across groups.

**Metric:** P(positive outcome | group) should be approximately equal across all groups.
**Threshold:** Ratio between any two groups must be within [FILL IN: e.g., 0.80 -- 1.25] (four-fifths rule).

| Protected Attribute | Group | N | Positive Outcome Rate | Ratio vs. Reference Group | Pass/Fail |
|---------------------|-------|---|----------------------|--------------------------|-----------|
| [FILL IN] | [Reference group] | [FILL IN] | [FILL IN: e.g., 0.72] | 1.00 (reference) | -- |
| [FILL IN] | [Group B] | [FILL IN] | [FILL IN: e.g., 0.68] | [FILL IN: e.g., 0.94] | [Pass/Fail] |
| [FILL IN] | [Group C] | [FILL IN] | [FILL IN: e.g., 0.61] | [FILL IN: e.g., 0.85] | [Pass/Fail] |

**Overall demographic parity result:** [PASS / FAIL -- summarize]

### 3.2 Equalized Odds

Equalized odds measures whether the true positive rate (TPR) and false positive rate (FPR) are equal across groups.

**Threshold:** Maximum TPR difference across groups < [FILL IN: e.g., 0.05]; Maximum FPR difference < [FILL IN: e.g., 0.05].

| Protected Attribute | Group | N | TPR | FPR | TPR Diff from Reference | FPR Diff from Reference | Pass/Fail |
|---------------------|-------|---|-----|-----|------------------------|------------------------|-----------|
| [FILL IN] | [Reference] | [FILL IN] | [FILL IN] | [FILL IN] | 0.000 | 0.000 | -- |
| [FILL IN] | [Group B] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [Pass/Fail] |
| [FILL IN] | [Group C] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [Pass/Fail] |

**Overall equalized odds result:** [PASS / FAIL -- summarize]

### 3.3 Calibration

Calibration measures whether predicted probabilities correspond to actual outcome rates consistently across groups.

**Threshold:** Maximum calibration difference across groups at any decile < [FILL IN: e.g., 0.03].

| Protected Attribute | Group | N | Mean Predicted Probability | Actual Positive Rate | Calibration Gap | Pass/Fail |
|---------------------|-------|---|---------------------------|---------------------|-----------------|-----------|
| [FILL IN] | [Reference] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | -- |
| [FILL IN] | [Group B] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [Pass/Fail] |

**Overall calibration result:** [PASS / FAIL -- summarize]

### 3.4 Additional Metrics (if applicable)

| Metric | Description | Result | Threshold | Pass/Fail |
|--------|-----------|--------|-----------|-----------|
| [FILL IN: e.g., Predictive parity] | [FILL IN] | [FILL IN] | [FILL IN] | [Pass/Fail] |
| [FILL IN: e.g., Treatment equality] | [FILL IN] | [FILL IN] | [FILL IN] | [Pass/Fail] |

### 3.5 LLM-Specific Fairness Metrics (for LLM-based systems)

| Metric | Description | Result | Threshold | Pass/Fail |
|--------|-----------|--------|-----------|-----------|
| **Response quality parity** | Quality scores are consistent across demographic mentions | [FILL IN: score difference] | < 0.1 on 5-point scale | [Pass/Fail] |
| **Stereotype association** | Model does not associate demographic groups with stereotypes | [FILL IN: % of test cases with stereotypical associations] | < 2% | [Pass/Fail] |
| **Sentiment parity** | Sentiment of responses is neutral regardless of demographic context | [FILL IN: sentiment score difference] | < 0.05 | [Pass/Fail] |
| **Refusal parity** | Refusal rate is consistent regardless of demographic group mentioned | [FILL IN: max refusal rate difference] | < 3% | [Pass/Fail] |

---

## 4. Intersectional Analysis Results

| Intersection | Subgroup | N | Positive Outcome Rate | Ratio vs. Overall | Flag |
|-------------|----------|---|----------------------|-------------------|------|
| [FILL IN: e.g., Gender x Age] | [FILL IN: e.g., Female, 18-25] | [FILL IN] | [FILL IN] | [FILL IN] | [OK / Warning / Fail] |
| [FILL IN] | [FILL IN: e.g., Female, 65+] | [FILL IN] | [FILL IN] | [FILL IN] | [OK / Warning / Fail] |
| [FILL IN] | [FILL IN: e.g., Male, 18-25] | [FILL IN] | [FILL IN] | [FILL IN] | [OK / Warning / Fail] |

**Intersectional analysis findings:** [FILL IN: summarize any disparities found at intersections that were not visible in single-attribute analysis.]

---

## 5. Disparities Found

### 5.1 Summary of Disparities

| Disparity ID | Attribute(s) | Affected Group(s) | Metric | Observed Value | Threshold | Severity |
|-------------|-------------|-------------------|--------|----------------|-----------|----------|
| DISP-001 | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [Critical / Major / Minor] |
| DISP-002 | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [Critical / Major / Minor] |

### 5.2 Root Cause Analysis

For each disparity, document the root cause investigation:

**DISP-001: [FILL IN: Title]**

| Analysis Dimension | Finding |
|--------------------|---------|
| **Data-related cause** | [FILL IN: e.g., underrepresentation of group X in training data, biased labels, historical bias in outcome variable] |
| **Feature-related cause** | [FILL IN: e.g., proxy variable Z correlates with protected attribute] |
| **Model-related cause** | [FILL IN: e.g., model amplifies existing data disparities] |
| **Pipeline-related cause** | [FILL IN: e.g., preprocessing step disproportionately filters group X] |
| **Conclusion** | [FILL IN: primary root cause and confidence level] |

---

## 6. Mitigations Applied

### 6.1 Mitigation Actions

| Mitigation ID | For Disparity | Mitigation Type | Description | Impact on Disparity | Impact on Overall Performance |
|-------------- |-------------- |----------------|-------------|--------------------|-----------------------------|
| MIT-001 | DISP-001 | [Pre-processing / In-processing / Post-processing] | [FILL IN: e.g., Resampled training data to balance group representation] | [FILL IN: e.g., Demographic parity ratio improved from 0.72 to 0.88] | [FILL IN: e.g., Overall accuracy decreased by 0.3%] |
| MIT-002 | DISP-002 | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |

### 6.2 Mitigation Effectiveness

| Metric | Before Mitigation | After Mitigation | Threshold | Status |
|--------|-------------------|-----------------|-----------|--------|
| [FILL IN: e.g., Demographic parity ratio (Gender)] | [FILL IN: e.g., 0.72] | [FILL IN: e.g., 0.88] | [FILL IN: 0.80] | [Pass / Still failing] |
| [FILL IN: e.g., Overall accuracy] | [FILL IN: e.g., 0.94] | [FILL IN: e.g., 0.937] | [FILL IN: >= 0.92] | [Pass] |

### 6.3 Trade-Off Analysis

[FILL IN: Document any trade-offs between fairness metrics (e.g., improving demographic parity at the cost of calibration) or between fairness and overall performance. Explain why the chosen balance is appropriate for this use case and regulatory context.]

---

## 7. Residual Risk Assessment

### 7.1 Residual Disparities

| Disparity | Status After Mitigation | Residual Risk Level | Justification for Acceptance |
|-----------|------------------------|--------------------|-----------------------------|
| DISP-001 | [Resolved / Partially mitigated / Accepted] | [Low / Medium / High] | [FILL IN: why residual risk is acceptable given business context and regulatory requirements] |
| DISP-002 | [FILL IN] | [FILL IN] | [FILL IN] |

### 7.2 Monitoring Plan for Residual Risks

| Residual Risk | Monitoring Metric | Alert Threshold | Monitoring Frequency | Escalation Path |
|--------------|-------------------|-----------------|---------------------|-----------------|
| [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN: e.g., weekly] | [FILL IN: e.g., Model Owner -> AI Governance Committee] |

### 7.3 Overall Risk Verdict

| Assessment Dimension | Verdict |
|---------------------|---------|
| **All blocking fairness criteria met** | [Yes / No] |
| **Non-blocking disparities documented** | [Yes / N/A] |
| **Mitigations applied and effective** | [Yes / Partially / No] |
| **Residual risks at acceptable level** | [Yes / No] |
| **Monitoring plan in place** | [Yes / No] |
| **Overall fairness assessment** | [PASS / CONDITIONAL PASS / FAIL] |

---

## 8. FinTech Example: Loan Approval Fairness Assessment

The following is a condensed example showing how this template would be completed for a loan approval system.

### Scope

- **System:** Credit scoring model (gradient-boosted tree) used to approve or deny consumer loan applications
- **Decision:** Binary (approve / deny) based on a risk score threshold
- **Affected population:** ~80,000 loan applicants per year in the Netherlands
- **Protected attributes tested:** Age (5 bands), Gender (3 groups), Nationality (EU/non-EU)

### Key Results (Example)

| Attribute | Group | Approval Rate | Ratio vs. Reference | Equalized Odds TPR | Result |
|-----------|-------|--------------|---------------------|---------------------|--------|
| Gender | Male (ref) | 0.71 | 1.00 | 0.83 | -- |
| Gender | Female | 0.68 | 0.96 | 0.81 | Pass |
| Age | 26-35 (ref) | 0.74 | 1.00 | 0.85 | -- |
| Age | 18-25 | 0.52 | 0.70 | 0.68 | **FAIL** |
| Age | 65+ | 0.63 | 0.85 | 0.77 | Pass |
| Nationality | EU (ref) | 0.72 | 1.00 | 0.84 | -- |
| Nationality | Non-EU | 0.58 | 0.81 | 0.72 | Pass (marginal) |

### Disparity Found

- **DISP-001:** Young applicants (18-25) have a 30% lower approval rate than the reference group, violating the four-fifths threshold (0.70 < 0.80).
- **Root cause:** Training data contains historical bias -- younger applicants had fewer credit history features, leading to higher uncertainty scores. The model learned to penalize short credit histories, which disproportionately affects younger applicants.

### Mitigation Applied

- **MIT-001:** Introduced alternative data features for thin-file applicants (rent payment history, utility payments) and retrained with balanced sampling. Approval rate ratio for 18-25 group improved from 0.70 to 0.83 (above 0.80 threshold). Overall model AUC decreased by 0.4% (from 0.912 to 0.908), which remains above the 0.90 acceptance threshold.

### Residual Risk

- Non-EU nationality applicants remain at the lower boundary (0.81). Continuous monitoring alert set at 0.80; quarterly revalidation required.

---

## 9. Sign-Off

| Role | Name | Decision | Date | Signature |
|------|------|----------|------|-----------|
| **Model Owner** | [FILL IN] | [Approve / Reject / Request Changes] | [FILL IN] | [FILL IN] |
| **Compliance Officer** | [FILL IN] | [Approve / Reject / Request Changes] | [FILL IN] | [FILL IN] |
| **AI Ethics Lead** | [FILL IN] | [Approve / Reject / Request Changes] | [FILL IN] | [FILL IN] |
| **AI Governance Committee** | [FILL IN] | [Approve / Reject] | [FILL IN] | [FILL IN] |

---

## Cross-References

- [Bias and Fairness Evals](../evaluations/bias-and-fairness-evals.md) -- methodology guide for conducting fairness evaluations
- [Bias Testing Checklist](../checklists/bias-testing-checklist.yaml) -- checklist of required bias testing activities
- [Pre-Deployment Gate](../checklists/pre-deployment-gate.yaml) -- quality gate that requires this report
- [Model Card](model-card.md) -- model documentation that references this report's findings
- [Datasheet](data-sheet.md) -- training data documentation relevant to data-driven bias causes
- [Test Plan for AI](test-plan-for-ai.md) -- comprehensive test plan including fairness test design
- [Integrating Giskard](../guides/integrating-giskard.md) -- automated bias testing tooling
- [Integrating Microsoft RAI](../guides/integrating-microsoft-rai.md) -- Fairlearn for bias detection
- [Continuous Online Evaluation](../../03-runtime-governance/evaluations/continuous-online-evaluation.md) -- ongoing fairness monitoring
- [EU AI Act Risk Classification](../../01-discovery-governance/checklists/eu-ai-act-risk-classification.yaml) -- risk tier that determines testing rigor

---

## Document Metadata

| Field | Value |
|-------|-------|
| **Template Version** | 1.0.0 |
| **Last Updated** | 2026-03-01 |
| **Framework Alignment** | SAFEST F-01, F-02, F-03, F-04; EU AI Act Art. 9, 10(2f), 13; ISO/IEC 42001 |
| **Governance Pillar** | Development Governance |
| **Document Type** | Template |
