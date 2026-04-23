# Eval-Driven Development: The AI Equivalent of TDD

## Purpose

Eval-driven development is the core methodology of this governance framework. It applies the discipline of test-driven development to AI systems: **define what "good" looks like first, encode it in automated evaluations, then build the feature to meet that bar.** No AI feature ships without automated acceptance criteria that demonstrate it works, is safe, and is fair.

This document defines the eval-first cycle, explains how it differs from traditional ML testing, describes eval suite structure, and provides worked examples for FinTech use cases.

## When to Use

- **Every time** an AI feature is developed, modified, or extended
- When retraining an existing model on new data
- When modifying prompts, guardrails, or agent behavior
- When integrating a third-party AI model into your system
- When adding new tools or capabilities to an existing agent

There are no exceptions. If the change affects AI system behavior, it requires eval-driven development.

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **AI/ML Engineer** | **Responsible** -- writes eval suites, implements features to pass them, maintains eval infrastructure |
| **Model Owner** | **Accountable** -- ensures eval suites exist and are passing before approving deployment |
| **Product Manager** | **Consulted** -- defines product-level acceptance criteria that feed into eval suites |
| **Compliance Officer** | **Reviewer** -- validates that eval suites cover fairness and regulatory requirements for limited/high-risk systems |

## Regulatory Basis

- **EU AI Act Article 9(7)** -- Testing of AI systems to ensure consistent performance
- **EU AI Act Article 15(1)** -- High-risk AI systems must be designed to achieve appropriate levels of accuracy
- **SAFEST items S-03** (acceptance criteria), **S-04** (edge cases), **S-05** (stress testing)
- **DNB Good Practice** -- Models must be validated before deployment and periodically thereafter

---

## 1. The Core Principle

> **No AI feature without automated acceptance criteria.**

This mirrors the Superpowers development methodology's iron rule: "No code without a failing test." In the AI context:

- A test suite validates that software works as specified.
- An **eval suite** validates that an AI system meets its acceptance criteria for quality, safety, and fairness.

The key difference: traditional tests are binary (pass/fail on exact outputs). AI evals are **statistical** (pass/fail on metric thresholds across a dataset). But the discipline is identical: define the bar first, then build to meet it.

---

## 2. The Eval-First Cycle

```
  +------------------+     +------------------+     +------------------+
  |  1. DEFINE       |     |  2. WRITE        |     |  3. RUN          |
  |     CRITERIA     | --> |     EVAL SUITE   | --> |     (SHOULD FAIL)|
  |                  |     |                  |     |                  |
  |  From Discovery  |     |  Automated tests |     |  Confirms eval   |
  |  Governance:     |     |  that encode     |     |  suite detects   |
  |  acceptance      |     |  each criterion  |     |  absence of      |
  |  criteria with   |     |  as a measurable |     |  the feature.    |
  |  metrics &       |     |  check.          |     |  If it passes,   |
  |  thresholds.     |     |                  |     |  the eval is     |
  |                  |     |                  |     |  broken.         |
  +------------------+     +------------------+     +------------------+
           |                                                 |
           |                                                 v
  +------------------+     +------------------+     +------------------+
  |  6. DEPLOY       |     |  5. RUN          |     |  4. BUILD        |
  |                  | <-- |     (SHOULD PASS) | <-- |     FEATURE      |
  |  Only after      |     |                  |     |                  |
  |  passing the     |     |  All criteria    |     |  Implement the   |
  |  pre-deployment  |     |  meet their      |     |  AI capability:  |
  |  gate.           |     |  thresholds.     |     |  train model,    |
  |                  |     |  If any fail,    |     |  write prompts,  |
  |                  |     |  fix before       |     |  build agent     |
  |                  |     |  proceeding.     |     |  workflow.        |
  +------------------+     +------------------+     +------------------+
```

### Step-by-Step

**Step 1: Define Criteria** -- The acceptance criteria come from Discovery Governance (see [Defining Acceptance Criteria](../../01-discovery-governance/evaluations/defining-acceptance-criteria.md)). Each criterion has a metric, threshold, measurement method, data source, and blocking flag.

**Step 2: Write Eval Suite** -- Translate each criterion into an automated evaluation. Use the [Acceptance Criteria Automation Template](acceptance-criteria-automation.yaml) to structure this. The eval suite is code: it runs against the AI system and produces pass/fail results for each criterion.

**Step 3: Run (Should Fail)** -- Run the eval suite against the current system (which does not yet have the new feature). The evals should **fail** because the feature does not exist. This step validates that the eval suite is actually testing something meaningful. If the evals pass before you build the feature, either the criteria are too weak or the eval suite is broken.

**Step 4: Build Feature** -- Implement the AI capability. Train the model, write the prompts, build the agent workflow, connect the tools. Focus on making the evals pass, not on ad-hoc manual testing.

**Step 5: Run (Should Pass)** -- Run the full eval suite. All criteria must meet their thresholds. If any blocking criterion fails, the feature is not ready. Fix the issue and re-run. Do not lower the threshold to match the model's performance.

**Step 6: Deploy** -- Only after passing the [Pre-Deployment Gate](../checklists/pre-deployment-gate.yaml). The eval results are part of the deployment evidence package.

---

## 3. How This Differs from Traditional ML Testing

| Traditional ML Testing | Eval-Driven Development |
|-----------------------|-------------------------|
| Test after building the model | Define tests before building |
| Test on a single holdout set | Test across multiple dimensions (quality, safety, fairness, product) |
| Pass/fail based on a single metric (usually accuracy) | Pass/fail based on multiple metrics with explicit thresholds |
| Tests are one-time, pre-deployment | Evals run continuously: pre-deployment + production monitoring |
| Tests are owned by ML engineers | Evals are owned by the product team (criteria) and ML engineers (implementation) |
| No connection to business outcomes | Product metrics and business metrics are part of the eval suite |
| Fairness testing is optional | Fairness testing is a required eval dimension for limited/high-risk systems |
| Manual "looks good" review | Automated, reproducible, version-controlled eval results |

---

## 4. Eval Suite Structure

An eval suite has three levels, mirroring the test pyramid in traditional software:

### 4.1 Unit Evals (Component-Level)

Test individual components of the AI system in isolation.

| What is Tested | Example | Tooling |
|---------------|---------|---------|
| Single model performance on a labeled dataset | Precision/recall of fraud classifier on holdout set | scikit-learn metrics, custom eval scripts |
| Single prompt behavior on a test case set | LLM instruction following on 200 curated scenarios | Custom eval harness, LangSmith, Braintrust |
| Single guardrail effectiveness | Input filter blocks all 100 adversarial prompts in test suite | Guardrail testing framework |
| Data pipeline correctness | Feature engineering produces expected outputs for known inputs | Great Expectations, dbt tests |

**Characteristics:** Fast (seconds to minutes), deterministic for ML models (probabilistic for LLMs, so run multiple times and aggregate), run on every code change.

### 4.2 Integration Evals (Subsystem-Level)

Test combinations of components working together.

| What is Tested | Example | Tooling |
|---------------|---------|---------|
| RAG pipeline end-to-end | Retrieval finds the right documents AND the LLM generates a grounded answer | Custom eval pipeline, RAGAS |
| Agent tool use | Agent correctly selects and invokes the right tool for a given task | Agent eval framework, LangSmith |
| Model + guardrail chain | Model generates output, guardrail filters it, final output meets quality bar | End-to-end eval pipeline |
| Multi-step workflow | Agent completes a 3-step customer onboarding flow correctly | Scenario-based eval framework |

**Characteristics:** Slower (minutes), may involve external services, run on feature branches and before merge.

### 4.3 System Evals (End-to-End)

Test the complete AI system as a user would experience it.

| What is Tested | Example | Tooling |
|---------------|---------|---------|
| Full user scenario completion | Customer asks about a flagged transaction, gets an explanation, confirms or disputes | End-to-end scenario runner |
| Fairness across the full pipeline | Demographic parity measured on end-to-end system output, not just the model | Full pipeline fairness evaluation |
| Production-like load and latency | System handles 1,000 concurrent requests within latency thresholds | Load testing + eval verification |
| Adversarial robustness | System handles prompt injection attempts across the full attack surface | Red-team scenario suite |

**Characteristics:** Slow (minutes to hours), requires production-like environment, run before deployment and periodically in production.

---

## 5. Example: Building a Transaction Categorization Agent

### Context

A FinTech wants to build an AI agent that automatically categorizes customer transactions (groceries, rent, salary, entertainment, etc.) to power a personal finance management (PFM) feature.

**Risk tier:** Limited (customer-facing feature with transparency obligation; does not make financial decisions)

### Step 1: Acceptance Criteria (from Discovery)

| ID | Metric | Threshold | Blocking |
|----|--------|-----------|----------|
| AC-001 | Top-1 accuracy on 15 categories | >= 85% | Yes |
| AC-002 | Top-3 accuracy | >= 95% | Yes |
| AC-003 | Categorization latency (P95) | <= 100ms | Yes |
| AC-004 | Customer override rate (customers correcting the category) | <= 10% after 30 days | No (soft) |
| AC-005 | Equal accuracy across merchant country of origin | Accuracy difference <= 5% across top 10 countries | Yes |
| AC-006 | AI disclosure: category labeled as "AI-suggested" in UI | 100% | Yes |

### Step 2: Write Eval Suite

```
eval_suite/
  unit/
    test_categorization_accuracy.py      # AC-001, AC-002: model accuracy on holdout set
    test_categorization_latency.py       # AC-003: latency under load
    test_fairness_by_country.py          # AC-005: accuracy parity across merchant countries
  integration/
    test_end_to_end_categorization.py    # Full pipeline: raw transaction -> category
    test_ui_disclosure.py                # AC-006: verify "AI-suggested" label in response
  system/
    test_production_scenario.py          # 100 real transaction scenarios end-to-end
    test_load.py                         # 10,000 concurrent categorization requests
```

### Step 3: Run (Should Fail)

Before building the categorization model, run the eval suite. Results:

```
AC-001: Top-1 accuracy = 0.00 (no model exists)     FAIL
AC-002: Top-3 accuracy = 0.00                        FAIL
AC-003: Latency = N/A (no endpoint)                  FAIL
AC-005: Accuracy parity = N/A                        FAIL
AC-006: AI disclosure = missing                      FAIL
```

Good. The eval suite correctly detects the absence of the feature.

### Step 4: Build Feature

- Train a transaction categorization model on historical labeled data
- Build the serving endpoint
- Add "AI-suggested" label to the API response
- Implement the UI integration

### Step 5: Run (Should Pass)

```
AC-001: Top-1 accuracy = 0.87 (threshold: >= 0.85)  PASS
AC-002: Top-3 accuracy = 0.96 (threshold: >= 0.95)  PASS
AC-003: Latency P95 = 45ms (threshold: <= 100ms)    PASS
AC-005: Max accuracy diff across countries = 3.2%    PASS
        (threshold: <= 5%)
AC-006: AI disclosure present = 100%                 PASS
```

All blocking criteria pass. Proceed to the pre-deployment gate.

---

## 6. Common Anti-Patterns

### Anti-Pattern 1: Eval Theater

**Symptom:** Eval suites exist but are designed to pass. Thresholds are set after observing model performance. Test data overlaps with training data.

**Why it is dangerous:** Creates a false sense of safety. The eval suite gives a green light that means nothing.

**How to detect:** Ask: "Were these thresholds defined before or after the model was built?" If after, it is eval theater.

**Fix:** Thresholds come from Discovery Governance, not from Development. The bar is set by business requirements and regulatory needs, not by model capability.

### Anti-Pattern 2: Overfitting to Evals

**Symptom:** The model scores perfectly on the eval suite but performs poorly on real production traffic. The team optimized specifically for the eval dataset rather than the underlying task.

**How to detect:** Compare eval suite performance to production metrics. A large gap indicates overfitting.

**Fix:** Use held-out eval data that the development team cannot access during training. Rotate eval datasets periodically. Include production traffic samples in eval cycles.

### Anti-Pattern 3: Single-Metric Obsession

**Symptom:** The team tracks only accuracy (or only F1, or only latency). Other dimensions (fairness, safety, product outcomes) are ignored.

**How to detect:** Count the number of distinct metrics in the eval suite. If fewer than 3 for minimal risk or 5 for limited risk, the suite is incomplete.

**Fix:** Use the multi-dimensional criteria framework from [Defining Acceptance Criteria](../../01-discovery-governance/evaluations/defining-acceptance-criteria.md). Every eval suite must cover quality, safety/fairness, and product dimensions.

### Anti-Pattern 4: Manual-Only Evaluation

**Symptom:** "We review the model outputs manually before each deployment." No automated eval suite exists.

**Why it is dangerous:** Manual review is subjective, inconsistent, and does not scale. It misses statistical patterns that only automated evaluation on large datasets can detect.

**Fix:** Manual review is valuable for qualitative assessment but must complement, not replace, automated evals. The pre-deployment gate requires automated eval results.

### Anti-Pattern 5: Eval Suite Rot

**Symptom:** The eval suite was written once and never updated. The data is stale. New failure modes are not covered. The suite passes every time and no one pays attention.

**How to detect:** Check the last modification date of eval data and eval code. If unchanged for > 3 months, suspect rot.

**Fix:** Update eval suites after every incident, red-teaming exercise, or user feedback pattern. Add new test cases for each discovered failure mode. Treat the eval suite as a living artifact, not a one-time deliverable.

---

## 7. Tooling Recommendations

| Need | Tool Options | Notes |
|------|-------------|-------|
| **LLM Eval Framework** | Giskard, Braintrust, LangSmith, custom harness | Giskard has built-in fairness and safety evaluations; Braintrust offers logging and scoring; custom harnesses give full control |
| **ML Model Eval** | scikit-learn metrics, MLflow, Weights & Biases | Standard ML evaluation libraries with experiment tracking |
| **RAG Eval** | RAGAS, custom citation verification | Evaluate retrieval quality and response groundedness |
| **Fairness Testing** | Fairlearn, AI Fairness 360 (AIF360), custom analysis | Compute fairness metrics across protected groups |
| **Safety Testing** | Giskard scan, custom adversarial suites, Prompt Injection test suites | Test for jailbreaks, prompt injection, harmful outputs |
| **CI/CD Integration** | GitHub Actions, GitLab CI, Jenkins | Wire eval results into deployment gates (see [Eval Gate Integration](eval-gate-integration.md)) |
| **Eval Data Management** | DVC, LakeFS, custom versioned data storage | Version eval datasets; prevent training-eval data leakage |

---

## 8. Eval-Driven Development and the Pre-Deployment Gate

The output of eval-driven development feeds directly into the [Pre-Deployment Gate Checklist](../checklists/pre-deployment-gate.yaml):

| Pre-Deployment Gate Item | Eval-Driven Development Input |
|--------------------------|------------------------------|
| "All acceptance criteria passing" | Eval suite results from Step 5 |
| "Bias testing completed and within thresholds" | Fairness evals from the eval suite |
| "Model documentation complete" | Model card updated with eval results |
| "Adversarial testing completed" | Adversarial eval results (high-risk) |
| "Fallback procedure tested" | System eval covering degraded mode |

---

## Cross-References

- **Defining Acceptance Criteria:** [../../01-discovery-governance/evaluations/defining-acceptance-criteria.md](../../01-discovery-governance/evaluations/defining-acceptance-criteria.md) -- the source of criteria that drive eval suites
- **AI Quality Metrics Catalog:** [../../01-discovery-governance/evaluations/ai-quality-metrics-catalog.md](../../01-discovery-governance/evaluations/ai-quality-metrics-catalog.md) -- reference for selecting eval metrics
- **Acceptance Criteria Automation:** [acceptance-criteria-automation.yaml](acceptance-criteria-automation.yaml) -- template for machine-executable criteria
- **Eval Gate Integration:** [eval-gate-integration.md](eval-gate-integration.md) -- wiring evals into CI/CD
- **Pre-Deployment Gate:** [../checklists/pre-deployment-gate.yaml](../checklists/pre-deployment-gate.yaml) -- the gate that requires passing evals
- **Continuous Online Evaluation:** [../../03-runtime-governance/evaluations/continuous-online-evaluation.md](../../03-runtime-governance/evaluations/continuous-online-evaluation.md) -- how evals continue in production
- **Governance in Agile Sprints:** [../../07-enterprise-implementation/process-integration/governance-in-agile-sprints.md](../../07-enterprise-implementation/process-integration/governance-in-agile-sprints.md) -- how eval work fits into sprint planning

---

*Last updated: 2026-02-28*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
