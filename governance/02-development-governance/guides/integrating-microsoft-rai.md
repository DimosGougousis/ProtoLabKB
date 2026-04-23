# Integrating Microsoft Responsible AI Toolbox

## Purpose

This guide provides instructions for using the Microsoft Responsible AI (RAI) Toolbox to generate interpretability reports, fairness assessments, and error analysis that satisfy governance requirements for regulated FinTech AI systems. The RAI Toolbox consists of four components: Fairlearn (bias metrics), InterpretML (model explanations), Error Analysis (systematic failure pattern identification), and Counterfactual Analysis (what-if scenarios). Together, they produce the evidence artifacts required by the pre-deployment gate for SAFEST items F-01 through F-04 and T-01 through T-02.

This is not a general RAI Toolbox tutorial. It focuses on producing governance-grade evidence: how to configure each tool to generate reports that satisfy regulatory reviewers and internal governance committees.

## When to Use

- When building fairness assessments for ML models that make decisions about individuals (credit scoring, fraud detection, insurance pricing)
- When regulatory requirements demand model interpretability and explainability documentation (EU AI Act Art. 13, 86)
- When the pre-deployment gate requires bias metrics across protected groups (DEV-FAIR-001 through DEV-FAIR-005)
- When investigating systematic failure patterns in model performance
- When generating "what-if" counterfactual explanations for adverse decisions

**Trigger:** An AI/ML engineer needs to produce fairness, interpretability, or error analysis evidence for a governance gate.

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **AI/ML Engineer** | **Responsible** -- runs RAI Toolbox analyses, generates reports, interprets findings |
| **Model Owner** | **Accountable** -- ensures RAI analysis is completed before deployment; reviews findings and decides on mitigations |
| **Ethics Lead** | **Consulted** -- reviews fairness metric selection and threshold decisions |
| **Compliance Officer (2nd Line)** | **Reviewer** -- validates RAI reports for regulatory adequacy (limited/high-risk systems) |
| **Data Scientist** | **Responsible** -- conducts deep-dive analysis on identified bias or error patterns |

## Regulatory Basis

- **EU AI Act Article 10(2)(f)** -- Examination of training data for possible biases
- **EU AI Act Article 13** -- Transparency requirements for high-risk AI systems
- **EU AI Act Article 86** -- Right to explanation for high-risk AI system decisions
- **SAFEST F-01** -- Identification of protected characteristics
- **SAFEST F-02** -- Proxy variable analysis
- **SAFEST F-03** -- Bias testing across protected groups with defined thresholds
- **SAFEST F-04** -- Fairness metric selection and justification
- **SAFEST T-01** -- Model interpretability and explainability methods
- **SAFEST T-02** -- Feature importance and decision factor transparency
- **GDPR Article 22** -- Right not to be subject to solely automated decision-making (requires meaningful explanations)

---

## 1. Installation and Setup

### 1.1 Installation

```bash
# Core RAI Toolbox components
pip install fairlearn              # Fairness metrics and mitigation
pip install interpret              # InterpretML: model explanations
pip install erroranalysis          # Error Analysis: systematic failure patterns
pip install dice-ml                # DiCE: counterfactual explanations

# For the integrated RAI dashboard (Jupyter-based)
pip install raiwidgets

# Verify installation
python -c "import fairlearn; import interpret; print('RAI Toolbox ready')"
```

---

## 2. Fairlearn: Bias Metrics and Assessment

### 2.1 Identifying Protected Characteristics

Before running Fairlearn, document which protected characteristics are relevant. This maps to SAFEST F-01.

| Protected Characteristic | Proxy Features to Monitor | FinTech Relevance |
|-------------------------|--------------------------|-------------------|
| Gender | First name, title, household composition | Credit scoring, insurance pricing |
| Age | Account tenure, product history | Lending, investment recommendations |
| Ethnicity / National origin | Postcode, language preference, name patterns | Fraud detection, AML screening |
| Disability | Interaction patterns, accessibility feature usage | Customer service AI, account management |
| Religion | Transaction timing patterns, merchant categories | Fraud detection (false positives on religious holiday spending) |

### 2.2 Computing Fairness Metrics

```python
from fairlearn.metrics import (
    MetricFrame,
    demographic_parity_difference,
    equalized_odds_difference,
    demographic_parity_ratio,
    false_positive_rate,
    false_negative_rate,
    selection_rate
)
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Example: Credit scoring model fairness assessment
y_true = test_data["actual_outcome"]        # Ground truth
y_pred = model.predict(test_features)       # Model predictions
sensitive_features = test_data["age_group"] # Protected characteristic

# Create MetricFrame for comprehensive analysis
metric_frame = MetricFrame(
    metrics={
        "accuracy": accuracy_score,
        "precision": precision_score,
        "recall": recall_score,
        "selection_rate": selection_rate,       # Approval rate
        "false_positive_rate": false_positive_rate,
        "false_negative_rate": false_negative_rate,
    },
    y_true=y_true,
    y_pred=y_pred,
    sensitive_features=sensitive_features
)

# View per-group metrics
print(metric_frame.by_group)

# Compute disparity metrics
print(f"Demographic parity difference: {demographic_parity_difference(y_true, y_pred, sensitive_features=sensitive_features):.4f}")
print(f"Equalized odds difference: {equalized_odds_difference(y_true, y_pred, sensitive_features=sensitive_features):.4f}")
print(f"Demographic parity ratio: {demographic_parity_ratio(y_true, y_pred, sensitive_features=sensitive_features):.4f}")
```

### 2.3 Fairness Metric Selection for Governance

Different fairness metrics encode different values. Document your selection and justify it -- this maps to SAFEST F-04.

| Metric | What It Measures | When to Choose | FinTech Example |
|--------|-----------------|----------------|-----------------|
| **Demographic Parity** | Equal approval rates across groups | When equal access is the primary concern | Loan approval rates should not differ by gender |
| **Equalized Odds** | Equal true positive and false positive rates across groups | When prediction accuracy matters equally for all groups | Fraud detection should not have higher false positive rates for specific nationalities |
| **Predictive Parity** | Equal precision across groups | When the cost of false positives is high for affected individuals | When a false fraud flag blocks account access |
| **Calibration** | Equal probability of outcome given the score, across groups | When scores are used for decision-making with different cutoffs | Credit scores should mean the same thing regardless of demographic |

> *Governance note:* Fairness metrics can mathematically conflict. It is impossible to simultaneously satisfy demographic parity and equalized odds when base rates differ between groups. Document which metric you prioritize, why, and what trade-offs you accept. This documentation is required by SAFEST F-04.

### 2.4 Governance Thresholds

| Metric | Threshold (High-Risk) | Threshold (Limited) | Action if Exceeded |
|--------|----------------------|--------------------|--------------------|
| Demographic parity difference | <= 0.02 (2%) | <= 0.05 (5%) | Block deployment; investigate and mitigate |
| Equalized odds difference | <= 0.03 (3%) | <= 0.05 (5%) | Block deployment; investigate and mitigate |
| Demographic parity ratio | >= 0.80 (80% rule) | >= 0.80 | Block deployment; investigate and mitigate |
| Per-group accuracy minimum | No group below 80% | No group below 75% | Block deployment; retrain with balanced data |

### 2.5 Generating Governance Evidence

```python
# Export fairness report for governance evidence
report = {
    "system_name": "Credit Scoring Model v2.1",
    "assessment_date": "2026-03-01",
    "protected_characteristics": ["age_group", "gender", "region"],
    "metrics_by_group": metric_frame.by_group.to_dict(),
    "demographic_parity_difference": demographic_parity_difference(y_true, y_pred, sensitive_features=sensitive_features),
    "equalized_odds_difference": equalized_odds_difference(y_true, y_pred, sensitive_features=sensitive_features),
    "governance_thresholds": {
        "demographic_parity_difference": 0.02,
        "equalized_odds_difference": 0.03,
    },
    "pass_fail": "PASS" if all_thresholds_met else "FAIL",
    "assessor": "AI/ML Engineer",
    "reviewer": "Ethics Lead"
}

import json
with open("governance-evidence/credit_scoring/v2.1/fairlearn_report.json", "w") as f:
    json.dump(report, f, indent=2, default=str)
```

---

## 3. InterpretML: Model Explanations

### 3.1 Global Explanations

Global explanations describe overall model behavior -- which features matter most across all predictions.

```python
from interpret.glassbox import ExplainableBoostingClassifier
from interpret import show

# Option 1: Use an inherently interpretable model (preferred for high-risk)
ebm = ExplainableBoostingClassifier()
ebm.fit(X_train, y_train)

# Generate global explanation
global_explanation = ebm.explain_global()
show(global_explanation)

# Option 2: Explain a black-box model post-hoc
from interpret.blackbox import ShapExplainer

shap_explainer = ShapExplainer(model, X_train)
shap_global = shap_explainer.explain_global()
show(shap_global)
```

### 3.2 Local Explanations (Individual Decisions)

Local explanations are required for GDPR Art. 22 compliance -- explaining individual decisions.

```python
# Explain a specific prediction (e.g., loan denial)
local_explanation = ebm.explain_local(X_test.iloc[[42]])
show(local_explanation)

# For governance: generate explanation text for the affected individual
def generate_decision_explanation(model, features, feature_names):
    """Generate human-readable explanation for an individual decision."""
    local_exp = model.explain_local(features)
    importances = local_exp.data(0)["scores"]

    top_factors = sorted(
        zip(feature_names, importances),
        key=lambda x: abs(x[1]),
        reverse=True
    )[:3]

    explanation = "The main factors in this decision were:\n"
    for feature, importance in top_factors:
        direction = "positively" if importance > 0 else "negatively"
        explanation += f"  - Your {feature} influenced the decision {direction}\n"

    return explanation
```

### 3.3 Connecting Interpretability to Governance

| Governance Requirement | InterpretML Output | How to Use |
|----------------------|-------------------|-----------|
| SAFEST T-01: Explainability method documented | Global explanation report | Include in model card under "Explainability Method" |
| SAFEST T-02: Feature importance transparency | Feature importance rankings | Include in model card under "Key Decision Factors" |
| GDPR Art. 22: Individual decision explanations | Local explanations for adverse decisions | Generate and store with each adverse decision |
| EU AI Act Art. 86: Right to explanation | Human-readable explanation text | Serve via API to customer-facing interfaces |
| DEV-TRANS-003: Explainability method with limitations | Method description + known limitations | Document in pre-deployment gate evidence |

---

## 4. Error Analysis: Systematic Failure Patterns

### 4.1 Identifying Failure Cohorts

Error Analysis identifies subgroups of data where the model systematically underperforms -- critical for discovering hidden bias patterns.

```python
from erroranalysis import ModelAnalyzer

# Analyze model errors
analyzer = ModelAnalyzer(
    model=model,
    dataset=X_test,
    true_y=y_test,
    feature_names=feature_names,
    categorical_features=categorical_features
)

# Generate error analysis report
report = analyzer.create_error_report()

# Identify cohorts with highest error rates
# Example output: "Applicants with income < 30000 AND region = 'rural'
#                  have 35% error rate vs. 8% overall"
```

### 4.2 Governance Implications of Error Cohorts

| Error Cohort Finding | Governance Action |
|---------------------|-------------------|
| Cohort with high error rate correlates with protected characteristic | Potential bias -- escalate to Ethics Lead for SAFEST F-03 review |
| Cohort with high error rate is a vulnerable population | Document in model card as known limitation; implement targeted monitoring |
| Cohort error rate exceeds governance threshold | Block deployment for that cohort; implement fallback to human decision-making |
| Cohort represents a rare but high-impact scenario | Add to edge case test suite (SAFEST S-04); monitor in production |

---

## 5. Counterfactual Analysis: What-If Scenarios

### 5.1 Generating Counterfactual Explanations

Counterfactual explanations answer: "What would need to change for this decision to be different?" This is the most intuitive form of explanation for affected individuals.

```python
import dice_ml

# Set up DiCE
data_interface = dice_ml.Data(
    dataframe=training_data,
    continuous_features=["income", "debt_ratio", "employment_years"],
    outcome_name="outcome"
)

model_interface = dice_ml.Model(model=model, backend="sklearn")

explainer = dice_ml.Dice(data_interface, model_interface)

# Generate counterfactuals for a denied application
denied_application = X_test.iloc[[42]]

counterfactuals = explainer.generate_counterfactuals(
    denied_application,
    total_CFs=3,                    # Generate 3 alternative scenarios
    desired_class="approved",       # What would lead to approval
    features_to_vary=["income", "debt_ratio", "employment_years"]  # Actionable features only
)

counterfactuals.visualize_as_dataframe()
```

### 5.2 Governance Constraints on Counterfactuals

| Constraint | Rationale | Implementation |
|-----------|-----------|----------------|
| Only vary actionable features | Do not suggest changing age, gender, or ethnicity | Set `features_to_vary` to exclude protected and immutable characteristics |
| Counterfactuals must be realistic | Do not suggest "increase income by 10x" | Set feasibility constraints on feature ranges |
| Counterfactuals must not reveal model internals | Do not expose exact thresholds or weights | Provide directional guidance, not precise values |
| Document counterfactual limitations | Counterfactuals show one path, not the only path | Include disclaimer in user-facing explanations |

### 5.3 FinTech-Specific Counterfactual Patterns

| Use Case | Counterfactual Question | Actionable Insight for Customer |
|----------|------------------------|-------------------------------|
| Credit denial | "What income level would lead to approval?" | "Reducing your debt-to-income ratio could improve your eligibility" |
| Fraud flag | "What transaction pattern would not be flagged?" | Internal use only -- do not share with customers (gaming risk) |
| Insurance pricing | "What factors increased my premium?" | "Your driving history and vehicle type are the primary factors" |
| Account restriction | "What would lift the restriction?" | "Completing identity verification would resolve this restriction" |

---

## 6. Integrated RAI Dashboard

### 6.1 Building the Governance Dashboard

```python
from raiwidgets import ResponsibleAIDashboard
from responsibleai import RAIInsights

# Create integrated RAI analysis
rai_insights = RAIInsights(model, X_train, X_test, y_test, y_train,
                           task_type="classification",
                           categorical_features=categorical_features)

# Add all analysis components
rai_insights.explainer.add()
rai_insights.error_analysis.add()
rai_insights.counterfactual.add(total_CFs=3, desired_class="approved")

# Compute
rai_insights.compute()

# Launch interactive dashboard
ResponsibleAIDashboard(rai_insights)
```

### 6.2 Exporting Dashboard Results for Evidence

```python
# Save RAI Insights for governance records
rai_insights.save("governance-evidence/credit_scoring/v2.1/rai_insights/")

# Generate static report for governance committee review
# (Dashboard is interactive; static report is for audit trail)
```

---

## 7. Mapping RAI Toolbox Outputs to Governance Gates

| Pre-Deployment Gate Item | RAI Toolbox Component | Output |
|--------------------------|----------------------|--------|
| DEV-FAIR-001: Protected characteristics identified | Fairlearn -- MetricFrame configuration | List of sensitive features used |
| DEV-FAIR-002: Proxy variable analysis | InterpretML -- feature importance + correlation with sensitive features | Report on proxy correlations |
| DEV-FAIR-003: Bias testing across groups | Fairlearn -- MetricFrame by_group + disparity metrics | Per-group metric report with pass/fail |
| DEV-FAIR-004: Fairness metric selection justified | Documentation of metric choice rationale | Written justification (not tool-generated) |
| DEV-TRANS-001: AI disclosure | N/A (UX concern) | N/A |
| DEV-TRANS-002: Explanation mechanism | InterpretML local explanations + DiCE counterfactuals | Explanation generation capability evidence |
| DEV-TRANS-003: Explainability method documented | InterpretML global explanations | Feature importance report + method description |
| DEV-EVAL-004: Edge case analysis | Error Analysis -- failure cohort identification | Cohort report with error rates |

---

## Cross-References

| Topic | Artifact | Location |
|-------|----------|----------|
| Eval-driven development methodology | Eval-Driven Development | [evaluations/eval-driven-development.md](../evaluations/eval-driven-development.md) |
| TDD for AI products | TDD for AI Products | [guides/tdd-for-ai-products.md](tdd-for-ai-products.md) |
| Giskard integration | Integrating Giskard | [guides/integrating-giskard.md](integrating-giskard.md) |
| Bias testing checklist | Bias Testing Checklist | [bias-testing-checklist.yaml](../checklists/bias-testing-checklist.yaml) |
| Bias and fairness evaluations | Bias and Fairness Evals | [bias-and-fairness-evals.md](../evaluations/bias-and-fairness-evals.md) |
| Pre-deployment gate | Pre-Deployment Gate | [pre-deployment-gate.yaml](../checklists/pre-deployment-gate.yaml) |
| Model card template | Model Card | [templates/model-card.md](../templates/model-card.md) |
| Bias assessment report template | Bias Assessment Report | [templates/bias-assessment-report.md](../templates/bias-assessment-report.md) |
| SAFEST Fairness pillar | SAFEST Checklist Detailed | [safest-checklist-detailed.md](../../04-operational-governance/regulatory/safest-checklist-detailed.md) |
| Tool landscape | Tool Landscape | [tool-landscape.md](../../05-cross-cutting/tool-landscape.md) |

---

*Last updated: 2026-03-01*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
*Framework: [Product Governance for Agentic AI Workflows](../../README.md)*
