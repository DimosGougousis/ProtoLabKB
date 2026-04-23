# Regression Testing for AI Systems

## Purpose

This document defines the regression testing framework for AI systems deployed in regulated FinTech environments. AI regression testing catches unintended degradations introduced by model updates, data refreshes, prompt changes, configuration modifications, or upstream dependency changes. Unlike traditional software regression testing -- which verifies that code changes do not break existing functionality -- AI regression testing must account for the stochastic nature of model outputs, the sensitivity of LLMs to prompt changes, and the emergent behavior of agentic systems.

A robust regression testing practice ensures that every change to an AI system is validated against a known-good baseline before reaching production, preventing silent quality degradation that could harm customers or violate regulatory requirements.

## When to Use

- Before deploying any model update, retraining, or fine-tuning to production
- Before deploying prompt changes, system instruction updates, or guardrail modifications
- After upstream data pipeline changes (new data sources, schema changes, feature engineering updates)
- After LLM provider model version updates (even minor versions)
- After infrastructure changes that affect model serving (new inference engine, hardware migration)
- After dependency updates (libraries, frameworks, embedding models)
- As part of the pre-deployment gate checklist (DEV-EVAL items)
- During periodic revalidation triggered by drift detection

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **ML Engineer** | **Responsible** -- designs regression test suites, maintains golden datasets, executes regression pipelines |
| **Model Owner** | **Accountable** -- defines regression acceptance criteria, approves or rejects regression results |
| **QA / Test Engineer** | **Responsible** -- integrates AI regression tests into CI/CD pipelines, maintains test infrastructure |
| **Compliance Officer (2nd Line)** | **Reviewer** -- validates that regression testing covers regulatory-critical behaviors |
| **AI Governance Committee** | **Informed** -- receives regression test pass/fail rates in quarterly governance reports |

## Regulatory Basis

- **SAFEST item S-03** -- Model performance metrics with thresholds that trigger remediation
- **SAFEST item S-22** -- Champion-challenger framework for comparing model versions
- **SAFEST item S-20** -- Validation frequency and revalidation triggers
- **EU AI Act Article 9(7)** -- Testing procedures shall be suitable to ensure the AI system complies with requirements throughout its lifecycle
- **EU AI Act Article 15(3)** -- High-risk AI systems shall be resilient as regards errors, faults, or inconsistencies
- **DORA Article 8(4)** -- ICT systems shall be tested before deployment and after significant changes
- **ISO/IEC 42001 Clause 8.4** -- AI system verification and validation

---

## 1. How AI Regression Testing Differs from Software Regression Testing

| Dimension | Traditional Software | AI Systems |
|-----------|---------------------|-----------|
| **Determinism** | Same input always produces same output | Outputs may vary due to stochasticity, temperature, sampling |
| **Correctness criteria** | Binary pass/fail per test case | Statistical thresholds across a dataset; acceptable ranges rather than exact matches |
| **Test oracle** | Expected output is known and fixed | Expected behavior is defined by distributions, not individual values |
| **Failure mode** | Clear error or incorrect output | Subtle quality degradation, shifted distributions, changed reasoning patterns |
| **Change impact** | Localized to modified code paths | A single model update can affect all outputs unpredictably |
| **Environment sensitivity** | Mostly deterministic | Sensitive to hardware (GPU vs CPU), library versions, random seeds, prompt formatting |
| **Regression scope** | Test the changed component | Must test the entire system because changes propagate non-linearly |

### Key Implication

AI regression tests must use **aggregate metrics over datasets**, not individual test case assertions. A single test case that produces a different output is not necessarily a regression -- it may be within the acceptable variability of the model. Regression is determined by comparing population-level metrics against baseline thresholds.

---

## 2. Golden Dataset Management

### 2.1 What Is a Golden Dataset

A golden dataset is a curated, versioned collection of input-output pairs that represent the system's expected behavior. It serves as the regression testing baseline. For agentic systems, golden datasets include expected tool call sequences, not just text outputs.

### 2.2 Golden Dataset Requirements

| Requirement | Description | Rationale |
|-------------|-------------|-----------|
| **Representative** | Covers all major use cases, edge cases, and customer segments | Ensures regression testing reflects real-world operating conditions |
| **Balanced** | Proportional representation of all outcome classes and protected groups | Prevents regression in fairness metrics from going undetected |
| **Versioned** | Every golden dataset has a version number and change log | Enables traceability of what was tested and when |
| **Immutable per version** | Once a golden dataset version is released, it is never modified | Ensures comparability across regression runs |
| **Labeled with ground truth** | Each example has a verified correct output or acceptable output range | Provides the oracle for regression comparison |
| **Includes adversarial cases** | Contains known attack vectors (prompt injection, jailbreaking attempts) | Ensures security mitigations are not regressed |
| **Includes regulatory-critical cases** | Contains examples that specifically test regulatory compliance behaviors | Detects regression in compliance-critical functionality |

### 2.3 Golden Dataset Categories for FinTech

| Category | Examples | Minimum Size |
|----------|---------|-------------|
| **Core functionality** | Typical customer queries, standard transaction processing, routine risk assessments | 500+ examples |
| **Edge cases** | Boundary values, unusual transaction patterns, ambiguous inputs | 100+ examples |
| **Fairness-critical** | Cases spanning all protected groups, balanced representation | 200+ examples per protected group |
| **Safety-critical** | Cases where incorrect output could cause financial harm | 100+ examples |
| **Adversarial** | Prompt injection attempts, jailbreaking, social engineering | 100+ examples |
| **Regulatory** | Cases testing compliance behaviors (KYC, AML, disclosure requirements) | 50+ examples per regulatory domain |
| **Agent-specific** | Expected tool call sequences, delegation patterns, permission boundary tests | 100+ examples |

### 2.4 Golden Dataset Refresh Cadence

- **Quarterly:** Review and update golden datasets to include new edge cases discovered in production
- **Event-driven:** Add new cases whenever an incident reveals a gap in the golden dataset
- **Annual:** Comprehensive review of golden dataset representativeness against current production data distribution

---

## 3. Regression Test Suite Design

### 3.1 Test Layers

```
Layer 4: End-to-End Agent Regression
  (full agent workflow: input -> reasoning -> tool calls -> output)
     |
Layer 3: Integration Regression
  (model + guardrails + tools in combination)
     |
Layer 2: Component Regression
  (individual model, individual guardrail, individual tool)
     |
Layer 1: Unit Regression
  (prompt template rendering, feature engineering, data preprocessing)
```

### 3.2 Metrics per Layer

| Layer | Key Metrics | Threshold Type |
|-------|------------|----------------|
| **Unit** | Data preprocessing correctness, feature engineering output consistency | Exact match (deterministic) |
| **Component** | Model accuracy, F1, AUC-ROC, calibration error, latency p50/p95 | Statistical threshold (e.g., "F1 must not decrease by more than 2% from baseline") |
| **Integration** | Guardrail trigger rate, false positive/negative rates, output schema compliance | Statistical threshold with context-dependent tolerances |
| **End-to-End** | Task completion rate, customer satisfaction proxy, tool call accuracy, reasoning trace quality | Aggregate metrics with human-evaluated sample |

### 3.3 Pass/Fail Criteria

Regression test results are classified using a three-tier system:

| Result | Definition | Action |
|--------|-----------|--------|
| **PASS** | All metrics are within acceptable bounds of the baseline (within tolerance) | Proceed to next deployment gate |
| **WARN** | One or more metrics show degradation but remain within regulatory acceptance criteria | Model Owner reviews and makes go/no-go decision; document rationale |
| **FAIL** | One or more metrics breach regulatory acceptance criteria or show statistically significant degradation beyond tolerance | Deployment blocked; root cause investigation required |

**Tolerance definition:** For each metric, define:
- **Baseline value:** The metric value at the last approved deployment
- **Tolerance band:** The acceptable deviation (e.g., +/- 2% for accuracy, +/- 5ms for latency p50)
- **Hard floor:** The absolute minimum acceptable value regardless of baseline (e.g., accuracy must never drop below 90%)

---

## 4. Automated Regression Pipeline

### 4.1 Pipeline Stages

```
Trigger (model update, data refresh, config change, dependency update)
    |
    v
[Stage 1] Environment Setup
    - Provision isolated test environment
    - Load pinned model version and dependencies
    - Load golden dataset (current version)
    |
    v
[Stage 2] Baseline Retrieval
    - Fetch baseline metrics from last approved deployment
    - Load tolerance bands and hard floors
    |
    v
[Stage 3] Regression Execution
    - Run golden dataset through the system
    - Collect predictions, tool calls, reasoning traces
    - Compute all metrics per layer
    |
    v
[Stage 4] Comparison
    - Compare each metric to baseline +/- tolerance
    - Classify each metric as PASS / WARN / FAIL
    - Aggregate to overall PASS / WARN / FAIL
    |
    v
[Stage 5] Reporting
    - Generate regression report with metric comparisons
    - Highlight any WARN or FAIL items with delta values
    - Store report as governance evidence
    |
    v
[Stage 6] Gate Decision
    - PASS: auto-proceed (for low-risk) or notify for approval (high-risk)
    - WARN: require Model Owner sign-off
    - FAIL: block deployment, create investigation ticket
```

### 4.2 CI/CD Integration

Regression tests integrate into the CI/CD pipeline at these points:

| Trigger | Pipeline Entry Point | Blocking? |
|---------|---------------------|-----------|
| Model code change (PR merge) | Pre-merge check | Yes -- PR cannot merge if regression fails |
| Model retraining (scheduled or manual) | Post-training validation | Yes -- retrained model cannot be promoted |
| Prompt or config change | Pre-deployment gate | Yes -- change cannot deploy if regression fails |
| Dependency update | Post-update verification | Yes -- update is reverted if regression fails |
| LLM provider model version change | Event-triggered validation | Yes -- system falls back to pinned version if regression fails |

---

## 5. Regression Root Cause Analysis

When a regression is detected, follow this structured investigation:

### 5.1 Investigation Steps

1. **Isolate the change:** What exactly changed since the last passing regression run? One change at a time.
2. **Identify affected examples:** Which golden dataset examples changed their output? Are they clustered by category, customer segment, or input type?
3. **Quantify the impact:** How many examples are affected? What is the magnitude of the metric change?
4. **Classify the regression type:**

| Regression Type | Description | Typical Cause |
|----------------|-------------|--------------|
| **Accuracy regression** | Overall performance metrics degraded | Model retraining on poor data; concept drift in training data |
| **Fairness regression** | Performance diverged across protected groups | Training data imbalance introduced; bias mitigation removed |
| **Safety regression** | Adversarial test cases now succeed where they previously failed | Guardrail weakened; prompt modification removed safety instructions |
| **Latency regression** | Response times increased beyond SLA | Model size increase; infrastructure change; inefficient prompt |
| **Behavioral regression** | Output style, format, or reasoning pattern changed | LLM provider model update; prompt template change |
| **Tool-use regression** | Agent calls different tools or uses different parameters | Model update changed tool-calling behavior; tool API schema change |

### 5.2 Root Cause Documentation

Every regression that causes a FAIL result must be documented with:
- Regression ID and date detected
- Change that triggered the regression
- Affected metrics with before/after values
- Root cause classification (from table above)
- Remediation action taken
- Verification that remediation resolved the regression

---

## 6. Regression Testing for Agentic Systems

### 6.1 Agent-Specific Regression Dimensions

| Dimension | What to Test | How to Measure |
|-----------|-------------|---------------|
| **Tool selection accuracy** | Does the agent select the correct tool for each task? | Compare tool call sequence against golden dataset expected sequence |
| **Tool parameter correctness** | Does the agent pass correct parameters to tools? | Validate parameters against expected ranges and schemas |
| **Delegation correctness** | In multi-agent systems, does the orchestrator delegate to the correct sub-agent? | Compare delegation targets against expected routing |
| **Permission boundary compliance** | Does the agent stay within its defined permission boundaries? | Verify no tool calls exceed the agent's authorized scope |
| **Reasoning quality** | Does the agent's reasoning chain remain coherent and correct? | Human evaluation of sampled reasoning traces; automated coherence scoring |
| **Fallback behavior** | Does the agent correctly fall back to human escalation when uncertain? | Test with ambiguous inputs; verify escalation rate is within bounds |

### 6.2 Multi-Agent Regression Concerns

When testing multi-agent systems, regression testing must cover:
- **Interface contracts:** Verify that the message format between agents has not changed
- **Delegation chain integrity:** Verify that the full delegation chain produces the expected outcome
- **Error propagation:** Verify that errors in sub-agents are correctly handled by the orchestrator
- **Permission inheritance:** Verify that sub-agent permissions are still strict subsets of orchestrator permissions

---

## 7. Reporting and Governance Integration

### 7.1 Regression Report Contents

Every regression test run produces a report containing:
- Run metadata (date, trigger, system under test, golden dataset version, environment)
- Summary verdict (PASS / WARN / FAIL)
- Metric comparison table (baseline vs. current for every metric)
- Delta analysis (which metrics changed and by how much)
- Affected golden dataset examples (for WARN and FAIL items)
- Recommendation (proceed, investigate, block)

### 7.2 Governance Evidence

Regression test reports serve as governance evidence for:
- **SAFEST S-03:** Performance metrics with thresholds (demonstrated by pass/fail against thresholds)
- **SAFEST S-22:** Champion-challenger comparison (regression test compares new version to incumbent)
- **EU AI Act Article 9(7):** Testing procedures throughout the lifecycle
- **Pre-deployment gate:** DEV-EVAL items require passing regression tests

### 7.3 Trend Analysis

Track regression test results over time to identify patterns:
- **Increasing WARN rate:** May indicate gradual quality erosion or overly aggressive optimization
- **Recurring failures in the same category:** May indicate a systemic issue in that area
- **Longer regression resolution times:** May indicate insufficient team capacity or growing system complexity

---

## Cross-References

- **Drift Detection Evals:** [drift-detection-evals.md](drift-detection-evals.md) -- drift may trigger regression testing; regression testing validates drift remediation
- **Eval Reporting Dashboard:** [eval-reporting-dashboard.md](eval-reporting-dashboard.md) -- regression results feed into the eval dashboard
- **Pre-Deployment Gate:** [../../02-development-governance/checklists/pre-deployment-gate.yaml](../../02-development-governance/checklists/pre-deployment-gate.yaml) -- regression tests are a gate requirement
- **Eval-Driven Development:** [../../02-development-governance/evaluations/eval-driven-development.md](../../02-development-governance/evaluations/eval-driven-development.md) -- foundational eval practices that regression testing builds on
- **LLM Eval Patterns:** [../../02-development-governance/evaluations/llm-eval-patterns.md](../../02-development-governance/evaluations/llm-eval-patterns.md) -- evaluation methods applicable to regression testing
- **Continuous Online Evaluation:** [../../03-runtime-governance/evaluations/continuous-online-evaluation.md](../../03-runtime-governance/evaluations/continuous-online-evaluation.md) -- production monitoring that may detect regressions missed by pre-deployment testing
- **Model Card Template:** [../../02-development-governance/templates/model-card.md](../../02-development-governance/templates/model-card.md) -- acceptance criteria that regression tests validate
- **SAFEST Checklist:** [../regulatory/safest-checklist-detailed.md](../regulatory/safest-checklist-detailed.md) -- S-03, S-20, S-22
- **Governance in CI/CD:** [../../07-enterprise-implementation/process-integration/governance-in-cicd.md](../../07-enterprise-implementation/process-integration/governance-in-cicd.md) -- how regression tests integrate into deployment pipelines
- **RACI Matrix:** [../../05-cross-cutting/governance-roles-raci.md](../../05-cross-cutting/governance-roles-raci.md) -- regression testing role assignments

---

*Last updated: 2026-03-01*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
