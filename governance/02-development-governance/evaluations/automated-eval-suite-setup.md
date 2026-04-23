# Automated Eval Suite Setup

## Purpose

This guide provides step-by-step instructions for setting up automated evaluation pipelines for AI systems. An eval suite is the collection of automated tests, benchmarks, and measurements that verify your AI system meets its [acceptance criteria](../../01-discovery-governance/evaluations/defining-acceptance-criteria.md) before and after deployment. It is the infrastructure backbone of [eval-driven development](eval-driven-development.md).

Without automated eval suites, governance is manual paperwork. With them, governance is code.

## When to Use

- When setting up a new AI project (the eval suite should exist before the first model iteration)
- When migrating from manual evaluation to automated pipelines
- When integrating AI evals into CI/CD (see [eval-gate-integration.md](eval-gate-integration.md))
- When onboarding a new team to eval-driven development practices

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **AI/ML Engineer** | **Responsible** -- builds and maintains eval suite infrastructure, writes eval cases |
| **MLOps Engineer** | **Responsible** -- integrates eval suites into CI/CD pipelines and monitoring |
| **Model Owner** | **Accountable** -- ensures eval suite exists, is comprehensive, and passes before deployment |
| **Product Manager** | **Consulted** -- provides product-level acceptance criteria that feed into eval cases |
| **Compliance Officer** | **Reviewer** -- validates that eval suite covers regulatory requirements for the system's risk tier |

## Regulatory Basis

- **EU AI Act Article 9(7)** -- High-risk AI systems must be tested to ensure consistent performance
- **EU AI Act Article 15** -- Systems must achieve appropriate levels of accuracy, robustness, and cybersecurity
- **SAFEST items S-03** (acceptance criteria), **S-04** (edge case testing), **S-05** (stress testing), **S-19** (independent validation)
- **DNB Good Practice** -- Automated and reproducible model validation is expected for supervised AI systems

---

## 1. Eval Suite Architecture

An eval suite consists of four layers, each building on the previous:

```
Layer 4: Product Evals          (business value, user satisfaction)
Layer 3: Safety & Fairness Evals (bias, toxicity, compliance)
Layer 2: Functional Evals        (accuracy, latency, tool use, instruction following)
Layer 1: Smoke Tests              (system health, API connectivity, schema validation)
```

### Layer 1: Smoke Tests

**Purpose:** Verify the system is operational before running expensive evaluations.

| Test | What It Checks | Failure Action |
|------|---------------|----------------|
| API health check | Model endpoint responds with 200 | Block all further evals |
| Schema validation | Input/output schemas match expected format | Block further evals |
| Latency check | Response time < 2x baseline P95 | Warn; proceed with caution |
| Token limit test | System handles max-length inputs without crash | Block deployment |
| Error handling | System returns graceful errors for invalid inputs | Block deployment |

### Layer 2: Functional Evals

**Purpose:** Verify the AI system produces correct outputs for known inputs.

| Eval Type | Description | Minimum Dataset Size |
|-----------|------------|---------------------|
| **Golden dataset eval** | Compare outputs against human-labeled ground truth | >= 200 examples per task type |
| **Regression suite** | Fixed test cases that must always pass (prevents known-bug recurrence) | >= 50 cases, grows over time |
| **Edge case suite** | Adversarial and boundary inputs that test robustness | >= 30 cases per identified edge case category |
| **Tool use eval** | For agents: verify correct tool selection, parameter extraction, and execution | >= 20 cases per tool |
| **Instruction following** | For LLM systems: verify the system follows its system prompt and guardrails | >= 50 instruction-compliance test cases |

### Layer 3: Safety & Fairness Evals

**Purpose:** Verify the system does not cause harm and treats all users equitably.

| Eval Type | Description | Framework Reference |
|-----------|------------|---------------------|
| **Bias eval** | Test for disparate outcomes across protected attributes | [bias-and-fairness-evals.md](bias-and-fairness-evals.md) |
| **Toxicity eval** | Test for harmful, offensive, or inappropriate outputs | [llm-eval-patterns.md](llm-eval-patterns.md) |
| **Hallucination eval** | Test for factually incorrect or fabricated information | [llm-eval-patterns.md](llm-eval-patterns.md) |
| **Safety boundary eval** | Test that guardrails prevent out-of-scope behavior | [guardrail-specification.yaml](../../03-runtime-governance/templates/guardrail-specification.yaml) |
| **PII leakage eval** | Test that the system does not expose personal data | [security-threat-model.yaml](../../04-operational-governance/checklists/security-threat-model.yaml) |

### Layer 4: Product Evals

**Purpose:** Verify the AI feature delivers value to users and the business.

| Eval Type | Description | Framework Reference |
|-----------|------------|---------------------|
| **Task success simulation** | Simulate user tasks and measure completion rate | [product-success-metrics.md](../../01-discovery-governance/evaluations/product-success-metrics.md) |
| **User preference eval** | Compare AI output variants using human preference ratings | [ab-testing-for-ai.md](../../03-runtime-governance/evaluations/ab-testing-for-ai.md) |
| **Cost-per-interaction** | Measure compute and API costs per evaluation run | [agent-performance-evals.md](../../03-runtime-governance/evaluations/agent-performance-evals.md) |

---

## 2. Setting Up Your Eval Suite

### Step 1: Define Eval Requirements

Before writing any eval code, document what you need to evaluate using the [evaluation strategy template](../../01-discovery-governance/evaluations/evaluation-strategy-template.yaml):

```yaml
eval_suite:
  system_name: "customer-support-agent"
  risk_tier: "limited"  # minimal | limited | high | unacceptable

  layers:
    smoke_tests:
      required: true
      run_frequency: "every_deployment"

    functional_evals:
      required: true
      golden_dataset_size: 500
      regression_suite_size: 75
      run_frequency: "every_deployment"

    safety_fairness_evals:
      required: true  # always required for limited and high risk
      bias_attributes: ["age", "gender", "nationality"]
      run_frequency: "every_deployment_and_weekly"

    product_evals:
      required: true
      primary_metric: "task_success_rate"
      target: 0.85
      run_frequency: "weekly"
```

### Step 2: Build the Eval Dataset

| Dataset Type | Source | Maintenance |
|-------------|--------|-------------|
| **Golden dataset** | Human-labeled examples from production data (anonymized) | Refresh quarterly with new production samples |
| **Regression cases** | Failed cases from production incidents and bug reports | Grows continuously; never remove cases |
| **Edge cases** | Red-team sessions, adversarial testing, compliance scenarios | Review and expand after each red-team exercise |
| **Synthetic cases** | LLM-generated test cases for coverage gaps | Validate synthetic cases with human review before adding |

**Data governance requirements:**
- All eval datasets must be anonymized (no real PII)
- Eval datasets must be version-controlled alongside the model
- Changes to eval datasets require review and approval
- Eval dataset provenance must be documented (source, creation date, labelers)

### Step 3: Implement Eval Runners

Choose an eval framework appropriate to your system type:

| System Type | Recommended Frameworks | Why |
|------------|----------------------|-----|
| **LLM applications** | Giskard, Ragas, DeepEval, custom harness | LLM-specific metrics (hallucination, faithfulness, toxicity) |
| **Traditional ML** | Giskard, MLflow, custom scikit-learn pipeline | Standard ML metrics with drift detection |
| **Agent systems** | Custom harness + LangSmith/Arize Phoenix traces | Need to eval tool use, delegation, and multi-step reasoning |
| **RAG systems** | Ragas, custom harness | Retrieval quality + generation quality |

### Step 4: Define Pass/Fail Criteria

Every eval must have an unambiguous pass/fail threshold:

```yaml
eval_gates:
  - name: "accuracy_gate"
    metric: "f1_score"
    threshold: 0.88
    operator: ">="
    blocking: true  # deployment blocked if this fails

  - name: "bias_gate"
    metric: "demographic_parity_difference"
    threshold: 0.05
    operator: "<="
    blocking: true

  - name: "latency_gate"
    metric: "p95_latency_ms"
    threshold: 2000
    operator: "<="
    blocking: false  # warning only
    alert_channel: "#ai-ops"

  - name: "hallucination_gate"
    metric: "hallucination_rate"
    threshold: 0.03
    operator: "<="
    blocking: true
```

### Step 5: Integrate into CI/CD

See [eval-gate-integration.md](eval-gate-integration.md) for detailed CI/CD integration patterns. The minimum viable integration:

```
Code Change → Build → Layer 1 (Smoke) → Layer 2 (Functional) → Layer 3 (Safety)
                                                                        ↓
                                                              All gates pass?
                                                              ↓           ↓
                                                            Yes          No
                                                              ↓           ↓
                                                        Deploy to    Block + notify
                                                        staging      model owner
```

---

## 3. Eval Suite Governance by Risk Tier

The depth and frequency of eval suites scales with the system's [risk tier](../../07-enterprise-implementation/risk-based-adoption/risk-tiering-model.md):

| Requirement | Minimal Risk | Limited Risk | High Risk |
|------------|-------------|-------------|-----------|
| **Smoke tests** | Required | Required | Required |
| **Golden dataset size** | >= 100 | >= 300 | >= 1000 |
| **Regression suite** | Recommended | Required | Required |
| **Bias eval** | Recommended | Required | Required (all protected attributes) |
| **Safety eval** | Basic | Required | Required + red-team validated |
| **Product eval** | Recommended | Required | Required |
| **Run frequency** | Per deployment | Per deployment + weekly | Per deployment + daily |
| **Independent validation** | Not required | Recommended | Required (2nd line review) |
| **Eval dataset review** | Annual | Quarterly | Monthly |

---

## 4. Monitoring and Maintaining Eval Suites

### Eval Suite Health Indicators

| Indicator | Healthy | Unhealthy | Action |
|-----------|---------|-----------|--------|
| **Pass rate trend** | Stable or improving | Declining over 3+ runs | Investigate model degradation or data drift |
| **Eval coverage** | All acceptance criteria have corresponding evals | Gaps between acceptance criteria and evals | Add missing eval cases |
| **Eval runtime** | Completes within CI/CD time budget | Exceeds 30 min for pre-deployment suite | Optimize or parallelize; consider sampling |
| **False positive rate** | < 5% of failures are non-issues | > 10% of failures are flaky or irrelevant | Review and fix flaky evals |
| **Dataset freshness** | Refreshed per schedule | Overdue for refresh by > 1 month | Schedule immediate dataset update |

### When to Update Your Eval Suite

| Trigger | Action |
|---------|--------|
| Production incident caused by AI | Add regression test case for the specific failure mode |
| New feature or capability added | Add functional and safety evals for the new capability |
| Data distribution shift detected | Refresh golden dataset with new production samples |
| Red-team exercise completed | Add discovered vulnerabilities as eval cases |
| Regulatory requirement change | Review and update safety/fairness eval coverage |
| Model retrained on new data | Run full eval suite before promoting new model version |

---

## 5. Eval Suite Checklist

Use this checklist when reviewing whether an eval suite is production-ready:

```yaml
eval_suite_readiness:
  - id: ES-01
    check: "Golden dataset exists with >= minimum size for risk tier"
    status: pending
  - id: ES-02
    check: "All acceptance criteria from evaluation strategy have corresponding eval cases"
    status: pending
  - id: ES-03
    check: "Pass/fail thresholds are defined for every eval"
    status: pending
  - id: ES-04
    check: "Eval suite runs in CI/CD pipeline and blocks deployment on failure"
    status: pending
  - id: ES-05
    check: "Bias eval covers all protected attributes relevant to the use case"
    status: pending
  - id: ES-06
    check: "Eval dataset is anonymized (no real PII)"
    status: pending
  - id: ES-07
    check: "Eval dataset is version-controlled"
    status: pending
  - id: ES-08
    check: "Eval results are logged and queryable for audit"
    status: pending
  - id: ES-09
    check: "Regression suite includes cases from all previous production incidents"
    status: pending
  - id: ES-10
    check: "Eval suite runtime fits within CI/CD time budget"
    status: pending
```

---

## Related Documents

- [Eval-Driven Development](eval-driven-development.md) -- the methodology this infrastructure supports
- [Acceptance Criteria Automation](acceptance-criteria-automation.yaml) -- machine-executable acceptance criteria template
- [Eval Gate Integration](eval-gate-integration.md) -- wiring eval suites into CI/CD pipelines
- [Defining Acceptance Criteria](../../01-discovery-governance/evaluations/defining-acceptance-criteria.md) -- what to measure (upstream input)
- [AI Quality Metrics Catalog](../../01-discovery-governance/evaluations/ai-quality-metrics-catalog.md) -- which metrics to use
- [LLM Eval Patterns](llm-eval-patterns.md) -- LLM-specific evaluation techniques
- [Bias and Fairness Evals](bias-and-fairness-evals.md) -- fairness evaluation methods
- [Pre-Deployment Gate](../../02-development-governance/checklists/pre-deployment-gate.yaml) -- the gate that eval suites feed into
