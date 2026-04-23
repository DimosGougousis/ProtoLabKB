# TDD for AI Products: Eval-First Development

## Purpose

This guide adapts the Superpowers Test-Driven Development methodology for AI/ML product development. In traditional software, the iron rule is "no code without a failing test." In AI, the equivalent is "no model, prompt, or agent without a failing eval." This document bridges the gap between engineering TDD discipline and the statistical, probabilistic nature of AI systems, providing concrete patterns for LLM-based agents, ML models, and agentic workflows in regulated FinTech.

Eval-first development is not aspirational -- it is the operational mechanism that makes governance enforceable. Without automated evaluations that run before every deployment, governance is documentation theater.

## When to Use

- Every time an AI feature is developed, modified, or extended (no exceptions)
- When writing or modifying prompts for LLM-based agents
- When training, fine-tuning, or retraining ML models
- When adding tools, capabilities, or permissions to an existing agent
- When integrating third-party AI models or APIs
- When onboarding AI/ML engineers to the governance-first development methodology

**Trigger:** Any change that affects AI system behavior triggers the eval-first cycle.

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **AI/ML Engineer** | **Responsible** -- writes eval suites, implements features to pass them, maintains eval infrastructure |
| **Model Owner** | **Accountable** -- ensures eval-first discipline is followed; no deployment without passing evals |
| **Product Manager** | **Consulted** -- defines product-level acceptance criteria that feed into eval suites |
| **Compliance Officer (2nd Line)** | **Reviewer** -- validates that eval suites cover regulatory requirements for limited/high-risk systems |
| **QA Lead** | **Informed** -- ensures eval infrastructure is maintained and CI/CD integration is operational |

## Regulatory Basis

- **EU AI Act Article 9(7)** -- Testing of AI systems to ensure consistent performance throughout the lifecycle
- **EU AI Act Article 15(1)** -- High-risk AI systems must achieve appropriate levels of accuracy, robustness, and cybersecurity
- **SAFEST S-03** -- Model performance metrics with acceptance thresholds
- **SAFEST S-04** -- Edge case analysis and boundary condition testing
- **SAFEST S-05** -- Stress testing under adverse conditions
- **SAFEST S-19** -- Independent model validation (2nd line)
- **DORA Article 25** -- Digital operational resilience testing

---

## 1. The Eval-First Cycle: RED-GREEN-REFACTOR for AI

### 1.1 Traditional TDD vs. Eval-First Development

| TDD Concept | AI Equivalent | Key Difference |
|-------------|--------------|----------------|
| Unit test | Unit eval | AI evals are statistical (pass/fail on thresholds over datasets), not binary |
| Failing test (RED) | Failing eval (eval below threshold) | A "failing eval" means the metric is below the acceptance threshold |
| Make the test pass (GREEN) | Make the eval pass (metric meets threshold) | May require training, fine-tuning, or prompt engineering iterations |
| Refactor | Optimize | Improve efficiency, reduce latency, simplify prompts -- without dropping below threshold |
| Test suite | Eval suite | Multi-dimensional: quality + safety + fairness + product metrics |
| CI/CD test gate | CI/CD eval gate | Automated gate that blocks deployment if any blocking eval fails |

### 1.2 The Cycle in Detail

```
STEP 1: DEFINE ACCEPTANCE CRITERIA (from Discovery Governance)
    |
    v
STEP 2: WRITE EVAL SUITE (automated, version-controlled)
    |
    v
STEP 3: RUN EVALS -- MUST FAIL (RED)
    |   If evals pass before building: your evals are broken or your bar is too low
    |
    v
STEP 4: BUILD / TRAIN / PROMPT ENGINEER (make evals pass)
    |
    v
STEP 5: RUN EVALS -- MUST PASS (GREEN)
    |   If any blocking eval fails: fix and re-run. Do NOT lower the threshold.
    |
    v
STEP 6: REFACTOR / OPTIMIZE
    |   Improve without breaking: latency, cost, prompt simplicity
    |   Re-run evals after every change. All must stay GREEN.
    |
    v
STEP 7: SUBMIT TO PRE-DEPLOYMENT GATE (eval results are evidence)
```

### 1.3 What "Failing" Means for AI

In traditional TDD, a test fails with an assertion error. In AI eval-first development, "failing" means different things depending on the system type:

| System Type | What "Failing" Means | Example |
|-------------|---------------------|---------|
| **ML classification model** | Metric below threshold on holdout dataset | Precision < 0.90 on fraud detection holdout set |
| **LLM prompt** | Eval score below threshold on curated test cases | Factual accuracy < 0.85 on 200 financial Q&A test cases |
| **Agent workflow** | Task completion rate below threshold on scenario suite | Agent completes < 90% of onboarding scenarios correctly |
| **RAG pipeline** | Retrieval or generation quality below threshold | Faithfulness score < 0.80 on RAGAS evaluation |
| **Guardrail** | Safety filter fails to catch test adversarial inputs | Prompt injection defense catches < 95% of test injection attempts |
| **Fairness metric** | Disparity between groups exceeds threshold | Approval rate difference between demographic groups > 2% |

---

## 2. Eval Suite Design Patterns for LLM-Based Agents

### 2.1 Property-Based Testing for Prompts

Traditional tests verify specific outputs. Property-based tests verify that outputs satisfy properties regardless of the specific content. This is essential for LLM agents where exact outputs are non-deterministic.

| Property | What It Tests | Example for a FinTech Agent |
|----------|--------------|---------------------------|
| **Format compliance** | Output matches expected structure | Agent response always includes a disclaimer when discussing fees |
| **Scope adherence** | Agent stays within its defined domain | Agent never provides investment advice when scoped to savings products |
| **Tone consistency** | Output maintains required tone | Agent never uses aggressive language during collections interactions |
| **Factual grounding** | Claims are supported by retrieved context | Agent citations match actual product terms and conditions |
| **Safety invariants** | Output never contains prohibited content | Agent never discloses other customers' information |
| **Regulatory compliance** | Output includes required disclosures | Agent always states "This is not financial advice" when discussing product features |
| **Refusal behavior** | Agent correctly refuses out-of-scope requests | Agent refuses to execute trades when scoped to informational support |

### 2.2 Deterministic vs. Statistical Eval Strategies

| Eval Type | When to Use | Threshold Approach | Run Frequency |
|-----------|-------------|-------------------|---------------|
| **Deterministic assertion** | Safety-critical properties that must never fail | 100% pass rate; single failure = blocking | Every commit |
| **Statistical threshold** | Quality metrics that are probabilistic | Pass if metric >= threshold over N test cases | Every commit, with N >= 100 |
| **Multi-run aggregation** | LLM outputs with high variance | Run eval K times, pass if mean metric >= threshold | Pre-merge, pre-deploy |
| **Human-in-the-loop eval** | Subjective quality that automated metrics cannot capture | Expert annotator agreement >= threshold | Weekly, pre-release |

### 2.3 Example: Eval Suite for a Customer Service Agent

```
eval_suite/
  deterministic/
    test_never_discloses_pii.py           # Safety invariant: 100% pass required
    test_always_discloses_ai_nature.py    # Regulatory: EU AI Act Art. 50
    test_never_provides_investment_advice.py  # Scope: agent is informational only
    test_always_offers_human_escalation.py   # HITL requirement

  statistical/
    test_response_accuracy.py             # >= 85% on 500 curated Q&A pairs
    test_response_relevance.py            # >= 90% relevance score on test queries
    test_faithfulness_to_sources.py       # >= 80% RAGAS faithfulness on RAG evals
    test_tone_appropriateness.py          # >= 95% appropriate tone classification

  fairness/
    test_response_quality_by_language.py  # Quality parity across supported languages
    test_escalation_rate_by_topic.py      # No topic-based bias in escalation triggers
    test_sentiment_parity.py             # Consistent tone regardless of customer sentiment

  adversarial/
    test_prompt_injection_resistance.py   # >= 95% defense rate on injection test suite
    test_jailbreak_resistance.py          # >= 98% refusal rate on jailbreak attempts
    test_data_extraction_resistance.py    # 100% pass: never leaks system prompt or training data

  integration/
    test_end_to_end_scenarios.py          # 20 full conversation scenarios, >= 85% completion
    test_handoff_to_human.py             # Correct handoff in 100% of escalation triggers
    test_tool_use_accuracy.py            # Agent uses correct tool in >= 90% of tool-requiring queries
```

---

## 3. Regression Test Suites for Model Updates

### 3.1 The Regression Problem in AI

When you update a model (retrain, fine-tune, swap LLM version, modify prompt), you risk degrading performance on previously passing scenarios. Regression testing for AI requires:

| Requirement | Implementation |
|-------------|---------------|
| **Golden dataset** | A curated, versioned set of test cases that must always pass. Never modify to accommodate model changes. |
| **Regression baseline** | Stored eval results from the last approved version. New version must meet or exceed. |
| **Differential analysis** | Compare new version vs. baseline on every metric. Flag any metric that decreased by > 1%. |
| **Failure case analysis** | For any test case that flipped from pass to fail, require manual review before deployment. |

### 3.2 Regression Suite Structure

```yaml
# regression-suite-config.yaml
regression:
  golden_dataset: "datasets/golden_v3.jsonl"  # Never modified for model convenience
  baseline_version: "v2.4.1"
  baseline_results: "results/v2.4.1_baseline.json"

  blocking_regressions:
    - metric: "accuracy"
      max_decrease: 0.01          # Block if accuracy drops more than 1%
    - metric: "safety_pass_rate"
      max_decrease: 0.00          # Block if ANY safety test regresses
    - metric: "fairness_gap"
      max_increase: 0.005         # Block if fairness gap widens by 0.5%

  warning_regressions:
    - metric: "latency_p95"
      max_increase_pct: 10        # Warn if latency increases by 10%
    - metric: "cost_per_inference"
      max_increase_pct: 20        # Warn if cost increases by 20%

  flip_analysis:
    enabled: true
    require_review_for_flips: true  # Any test case that changes pass->fail requires review
    reviewer: "model_owner"
```

### 3.3 Model Update Eval Workflow

| Phase | Action | Gate |
|-------|--------|------|
| 1. Pre-update | Run full eval suite on current (baseline) version. Store results. | Results stored as baseline |
| 2. Update | Apply model change (retrain, prompt modification, LLM version swap) | No gate |
| 3. Post-update | Run identical eval suite on new version | All blocking evals pass |
| 4. Regression check | Compare new results against baseline | No blocking regressions |
| 5. Flip analysis | Review every test case that flipped pass-to-fail | Model Owner approves each flip |
| 6. Deploy | Submit to pre-deployment gate with comparison report | Pre-deployment gate passes |

---

## 4. CI/CD Integration

### 4.1 Eval Gate Architecture

```
Code Change (prompt, model config, agent logic)
    |
    v
[CI Pipeline Triggered]
    |
    +--> [Unit Evals]         -- Run on every commit (< 5 min)
    |       |
    |       +--> FAIL? --> Block merge. Fix and re-run.
    |       |
    |       +--> PASS
    |
    +--> [Integration Evals]  -- Run on PR/merge request (< 30 min)
    |       |
    |       +--> FAIL? --> Block merge. Fix and re-run.
    |       |
    |       +--> PASS
    |
    +--> [System Evals]       -- Run pre-deployment (< 2 hours)
    |       |
    |       +--> FAIL? --> Block deployment. Fix and re-run.
    |       |
    |       +--> PASS
    |
    +--> [Regression Check]   -- Run pre-deployment
    |       |
    |       +--> REGRESSION? --> Block deployment. Review flips.
    |       |
    |       +--> NO REGRESSION
    |
    v
[Pre-Deployment Gate] --> Evidence package includes all eval results
```

### 4.2 Eval Tier Requirements by Risk Level

| Eval Tier | Minimal Risk | Limited Risk | High Risk |
|-----------|-------------|-------------|-----------|
| **Unit evals** | Required (quality only) | Required (quality + safety) | Required (quality + safety + fairness) |
| **Integration evals** | Recommended | Required | Required |
| **System evals** | Optional | Required | Required + adversarial |
| **Regression check** | Recommended | Required | Required + flip review |
| **Human-in-the-loop eval** | Optional | Recommended | Required |
| **Independent validation (2nd line)** | Not required | Recommended | Required |

---

## 5. Common Anti-Patterns and Fixes

### 5.1 Anti-Pattern: Eval-After Development

**Symptom:** Team builds the model or prompt first, then writes evals that confirm what was already built.

**Why it is dangerous:** Thresholds are unconsciously set to match current performance. The eval suite validates the model rather than the requirements.

**Fix:** Acceptance criteria and thresholds must come from Discovery Governance before development begins. Document the threshold origin: "Threshold set by [Product Manager/Compliance] on [date] based on [business requirement/regulatory requirement]."

### 5.2 Anti-Pattern: Green-Only Testing

**Symptom:** Evals never fail. Team has never seen a red eval. Everyone assumes the system is excellent.

**Why it is dangerous:** Either the evals are trivially easy or the system is being tested against its own training data.

**Fix:** Every eval suite must include adversarial cases that probe the system's limits. A suite that never fails is a suite that is not testing hard enough. Add edge cases from incident reports and red-teaming exercises.

### 5.3 Anti-Pattern: Threshold Shopping

**Symptom:** Team adjusts thresholds downward when the model fails to meet them, citing "unrealistic expectations."

**Why it is dangerous:** Undermines the entire eval-first discipline. The threshold becomes meaningless.

**Fix:** Threshold changes require the same approval as the original threshold: Product Manager for product metrics, Compliance Officer for regulatory metrics, Ethics Lead for fairness metrics. Document every threshold change with rationale and approval.

### 5.4 Anti-Pattern: Eval Data Contamination

**Symptom:** Eval dataset overlaps with training data. Model scores perfectly on evals but poorly on novel inputs.

**Fix:** Strict separation between training, validation, and eval datasets. Eval datasets must be managed by a different team or stored in a separate, access-controlled repository. Use hash-based deduplication checks between training and eval sets.

### 5.5 Anti-Pattern: Ignoring Non-Functional Evals

**Symptom:** Team evals for accuracy but not latency, cost, fairness, or safety.

**Fix:** Every eval suite must cover at minimum: (1) quality/accuracy, (2) safety, (3) fairness (for limited/high-risk). Use the multi-dimensional acceptance criteria from [Defining Acceptance Criteria](../../01-discovery-governance/evaluations/defining-acceptance-criteria.md).

---

## 6. Worked Example: Eval-First Development for a Lending Chatbot

### 6.1 Context

A FinTech company is building a chatbot that helps users understand their loan options. The chatbot retrieves product information and answers questions. It does not make lending decisions but influences user behavior (Limited risk under EU AI Act Art. 50).

### 6.2 Step 1: Acceptance Criteria (from Discovery)

| ID | Criterion | Metric | Threshold | Blocking |
|----|-----------|--------|-----------|----------|
| AC-001 | Response accuracy on product Q&A | Factual correctness (human-judged on 200 cases) | >= 90% | Yes |
| AC-002 | Faithfulness to source documents | RAGAS faithfulness score | >= 0.85 | Yes |
| AC-003 | AI disclosure in every conversation | Presence of disclosure message | 100% | Yes |
| AC-004 | Scope adherence: never provides personalized financial advice | Refusal rate on advice-seeking prompts | 100% | Yes |
| AC-005 | Response quality parity across languages (EN, NL) | Accuracy difference between languages | <= 5% | Yes |
| AC-006 | Prompt injection defense | Defense rate on 100 injection test cases | >= 95% | Yes |
| AC-007 | Human escalation offered when requested | Escalation success rate | 100% | Yes |
| AC-008 | Response latency P95 | Latency measurement | <= 3 seconds | No (soft) |

### 6.3 Step 2: Write Eval Suite

Write automated evals for each criterion. Run them. They must all fail (RED) because the chatbot does not exist yet.

### 6.4 Step 3: Build

Implement the chatbot: select LLM, write system prompt, build RAG pipeline, configure guardrails, add escalation logic.

### 6.5 Step 4: Run Evals (GREEN)

```
AC-001: Factual correctness = 92% (threshold: >= 90%)    PASS
AC-002: Faithfulness = 0.88 (threshold: >= 0.85)         PASS
AC-003: AI disclosure = 100%                              PASS
AC-004: Advice refusal = 100%                             PASS
AC-005: EN accuracy 92%, NL accuracy 89%, gap = 3%        PASS
AC-006: Injection defense = 97%                           PASS
AC-007: Escalation success = 100%                         PASS
AC-008: Latency P95 = 2.1s                                PASS
```

### 6.6 Step 5: Submit to Pre-Deployment Gate

Package eval results with model card, data sheet, and fairness assessment. Submit to the [Pre-Deployment Gate](../checklists/pre-deployment-gate.yaml).

---

## Cross-References

| Topic | Artifact | Location |
|-------|----------|----------|
| Core eval-driven methodology | Eval-Driven Development | [evaluations/eval-driven-development.md](../evaluations/eval-driven-development.md) |
| Acceptance criteria definition | Defining Acceptance Criteria | [defining-acceptance-criteria.md](../../01-discovery-governance/evaluations/defining-acceptance-criteria.md) |
| CI/CD eval gate implementation | Eval Gate Integration | [eval-gate-integration.md](../evaluations/eval-gate-integration.md) |
| Acceptance criteria automation | Acceptance Criteria Automation | [acceptance-criteria-automation.yaml](../evaluations/acceptance-criteria-automation.yaml) |
| Bias and fairness evaluation | Bias and Fairness Evals | [bias-and-fairness-evals.md](../evaluations/bias-and-fairness-evals.md) |
| LLM-specific eval patterns | LLM Eval Patterns | [llm-eval-patterns.md](../evaluations/llm-eval-patterns.md) |
| Pre-deployment gate checklist | Pre-Deployment Gate | [pre-deployment-gate.yaml](../checklists/pre-deployment-gate.yaml) |
| Giskard integration | Integrating Giskard | [guides/integrating-giskard.md](integrating-giskard.md) |
| Microsoft RAI integration | Integrating Microsoft RAI | [guides/integrating-microsoft-rai.md](integrating-microsoft-rai.md) |
| Verification before deployment | Verification Before Deployment | [guides/verification-before-deployment.md](verification-before-deployment.md) |
| Tool landscape | Tool Landscape | [tool-landscape.md](../../05-cross-cutting/tool-landscape.md) |

---

*Last updated: 2026-03-01*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
*Framework: [Product Governance for Agentic AI Workflows](../../README.md)*
