# Eval Gate Integration: Wiring Evaluations into CI/CD

## Purpose

This guide describes how to integrate AI evaluation results into your CI/CD pipeline as blocking quality gates. Eval gates are the enforcement mechanism that prevents underperforming, unsafe, or unfair AI systems from reaching production. Without eval gates, eval-driven development is a recommendation; with eval gates, it is a requirement.

## When to Use

- When setting up or modifying the CI/CD pipeline for any AI system
- When adding new acceptance criteria that must be enforced automatically
- When transitioning from manual evaluation to automated gates
- When implementing the [pre-deployment gate checklist](../checklists/pre-deployment-gate.yaml) in your pipeline

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **Platform / DevOps Engineer** | **Responsible** -- implements the pipeline integration, configures gate logic |
| **AI/ML Engineer** | **Responsible** -- writes and maintains the eval suite that gates call |
| **Model Owner** | **Accountable** -- ensures gates are active and correctly configured for the system's risk tier |
| **Compliance Officer (2nd Line)** | **Reviewer** -- validates that gate configuration matches governance requirements |

## Regulatory Basis

- **EU AI Act Article 9(7)** -- Testing must be suitable for the intended purpose and against predefined metrics
- **EU AI Act Article 15** -- Accuracy, robustness, and cybersecurity levels must be maintained
- **SAFEST items S-03** (acceptance criteria enforced), **S-06** (adversarial testing), **A-03** (deployment approval)
- **DORA Article 8** -- ICT change management procedures must include testing requirements

---

## 1. Architecture Overview

```
  Code Change          Eval Runner           Gate Decision         Deploy/Block
  (PR or merge)   -->  (runs eval suite) --> (compares results  --> (proceed or
                                              to thresholds)         halt pipeline)

  +---------------+    +------------------+   +------------------+   +-----------+
  |               |    |                  |   |                  |   |           |
  | Git push /    |--->| Pull eval suite  |-->| For each         |-->| All hard  |
  | PR created    |    | from repo        |   | criterion:       |   | gates     |
  |               |    |                  |   |                  |   | passed?   |
  |               |    | Run against      |   | metric >= thresh |   |           |
  |               |    | current system   |   | ? PASS : FAIL    |   | YES: next |
  |               |    |                  |   |                  |   | stage     |
  |               |    | Collect results  |   | Any hard gate    |   |           |
  |               |    | as JSON/YAML     |   | failed? BLOCK    |   | NO: block |
  |               |    |                  |   |                  |   | + notify  |
  +---------------+    +------------------+   +------------------+   +-----------+
                              |                        |
                              v                        v
                       +------------------+   +------------------+
                       | Store results    |   | Log decision     |
                       | as artifact      |   | to audit trail   |
                       +------------------+   +------------------+
```

---

## 2. Gate Types

### Hard Gates (Blocking)

**Definition:** If a hard gate fails, the pipeline stops. The deployment cannot proceed. Manual override requires explicit approval from the AI Governance Committee.

**When to use hard gates:**

| Criterion Type | Example | Rationale |
|---------------|---------|-----------|
| Safety violations | Zero tolerance for financial advice from a routing agent | Safety failures cause immediate customer harm and regulatory risk |
| Core accuracy below business minimum | Fraud detection precision < 0.90 | Below this threshold, too many legitimate transactions are blocked |
| Fairness violations | Demographic parity ratio < 0.80 | Below this threshold, the system discriminates and violates EU AI Act |
| Regulatory requirements | AI disclosure not present in customer interactions | EU AI Act Article 50 violation |
| Data integrity | Training-serving skew detected above threshold | Model is operating on different data than it was trained on |

### Soft Gates (Warning)

**Definition:** If a soft gate fails, the pipeline issues a warning but continues. The warning is logged, the model owner is notified, and the issue is tracked for resolution.

**When to use soft gates:**

| Criterion Type | Example | Rationale |
|---------------|---------|-----------|
| Stretch targets | Customer satisfaction above 4.5 (when minimum is 4.0) | Desirable but not blocking; tracks improvement over time |
| Non-critical metrics | Escalation rate slightly above target | Warrants investigation but does not indicate system failure |
| Emerging metrics | New fairness metric being trialed | Not yet validated enough to block deployments |
| Performance optimization | Latency slightly above ideal (but within SLA) | Track for optimization; does not impact correctness |

### Hard Gate Override Protocol

In exceptional circumstances, a hard gate failure may need to be overridden (e.g., critical security patch that must deploy despite a non-related eval regression). The override requires:

1. Written justification from the Model Owner
2. Approval from the AI Governance Committee chair (or designated deputy)
3. Time-bound remediation plan (when the failing criteria will be fixed)
4. Override logged in the audit trail with the justification and approval
5. Remediation tracked in the sprint backlog

---

## 3. CI/CD Integration Patterns

### 3.1 GitHub Actions

```yaml
# .github/workflows/ai-eval-gate.yml
name: AI Evaluation Gate

on:
  pull_request:
    paths:
      - 'models/**'
      - 'prompts/**'
      - 'agents/**'
      - 'eval_suite/**'

jobs:
  eval-gate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: pip install -r requirements-eval.txt

      - name: Run eval suite (pre-merge stage)
        run: |
          python -m eval_suite.runner \
            --stage pre_merge \
            --config eval_suite/config.yaml \
            --output eval_results/pr-${{ github.event.number }}.json

      - name: Check gate decision
        run: |
          python -m eval_suite.gate_check \
            --results eval_results/pr-${{ github.event.number }}.json \
            --fail-on hard_gate_failure

      - name: Upload eval results
        uses: actions/upload-artifact@v4
        with:
          name: eval-results
          path: eval_results/

      - name: Post eval summary to PR
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const results = JSON.parse(
              fs.readFileSync('eval_results/pr-${{ github.event.number }}.json')
            );
            // Format and post results as PR comment
            // (implementation details depend on eval result format)
```

### 3.2 GitLab CI

```yaml
# .gitlab-ci.yml (AI eval gate stages)
stages:
  - eval
  - gate-decision
  - deploy

ai-eval:
  stage: eval
  script:
    - pip install -r requirements-eval.txt
    - python -m eval_suite.runner --stage pre_merge --output eval_results/
  artifacts:
    paths:
      - eval_results/
    expire_in: 90 days
  rules:
    - changes:
        - models/**
        - prompts/**
        - agents/**

gate-check:
  stage: gate-decision
  script:
    - python -m eval_suite.gate_check --results eval_results/ --fail-on hard_gate_failure
  dependencies:
    - ai-eval
  rules:
    - changes:
        - models/**
        - prompts/**
        - agents/**
```

### 3.3 General Pattern (Any CI/CD System)

Regardless of the specific CI/CD platform, the integration follows this pattern:

```
Pipeline Stage 1: Run Evals
  Input:  eval suite config, model/agent under test
  Action: Execute all eval criteria for the current pipeline stage
  Output: Structured results file (JSON or YAML) with:
          - criterion_id
          - metric_value
          - threshold
          - pass_fail
          - gate_type (hard | soft)

Pipeline Stage 2: Gate Decision
  Input:  Eval results file
  Action: Parse results, apply gate logic:
          - If any hard gate FAILED: exit with non-zero code (block pipeline)
          - If only soft gates FAILED: log warning, continue
          - If all gates PASSED: continue
  Output: Gate decision logged to audit trail

Pipeline Stage 3: Deploy (conditional)
  Input:  Gate decision = PASS
  Action: Deploy the AI system to the target environment
  Output: Deployment record with eval results attached
```

---

## 4. Which Criteria Should Be Hard Gates vs. Soft Gates

### Decision Framework

| Question | If YES | If NO |
|----------|--------|-------|
| Would a failure cause direct customer harm? | **Hard gate** | Consider soft gate |
| Would a failure violate a regulation (EU AI Act, GDPR)? | **Hard gate** | Consider soft gate |
| Would a failure create unacceptable financial risk? | **Hard gate** | Consider soft gate |
| Is this the primary business metric for the system? | **Hard gate** | Consider soft gate |
| Is this a zero-tolerance safety criterion? | **Hard gate** | N/A |
| Is this a stretch target beyond the minimum viable bar? | Soft gate | N/A |
| Is this a new metric still being calibrated? | Soft gate | Consider hard gate |

### Recommended Gate Configuration by Risk Tier

| Risk Tier | Hard Gates | Soft Gates |
|-----------|-----------|------------|
| **Minimal** | Core accuracy metric (1-2 criteria), latency SLA | Stretch targets, optimization metrics |
| **Limited** | Core accuracy (2-3), fairness (1-2), safety (1-2), transparency (1) | Product satisfaction, stretch targets |
| **High** | Core accuracy (3+), fairness (2+), safety (all), transparency (all), independent validation | Optimization targets, emerging metrics |

---

## 5. Dashboard for Eval Results Tracking

Maintain a dashboard that provides visibility into eval results over time. The dashboard should answer these questions:

### Required Dashboard Views

| View | Content | Audience |
|------|---------|----------|
| **System Health Summary** | Current pass/fail status for all eval criteria per AI system | Model Owner, Engineering Lead |
| **Trend Analysis** | Metric values over time (last 30/90/365 days) with threshold lines | Model Owner, Compliance |
| **Gate Decision Log** | History of gate decisions (pass, fail, override) with timestamps and approvers | Compliance, Audit |
| **Failure Analysis** | Breakdown of gate failures by criterion category, frequency, and root cause | Engineering Lead, Model Owner |
| **Cross-System Comparison** | Eval results across all AI systems, highlighting systems with recurring failures | AI Governance Committee |

### Dashboard Data Model

```
eval_result:
  id: unique_id
  system_name: string
  criterion_id: string (e.g., "FC-01")
  metric_name: string
  metric_value: float
  threshold: float
  pass_fail: boolean
  gate_type: "hard" | "soft"
  pipeline_stage: "pre_merge" | "pre_deploy" | "periodic"
  pipeline_run_id: string
  timestamp: datetime
  commit_sha: string
  triggered_by: string (user or automation)
```

---

## 6. Alerting When Evals Degrade Over Time

Eval degradation detection catches the scenario where metrics gradually worsen over time, crossing the threshold suddenly after weeks of slow decline.

### Alerting Rules

| Alert Type | Trigger | Action | Notification |
|-----------|---------|--------|-------------|
| **Threshold Warning** | Metric within 10% of threshold for 3 consecutive runs | Investigate trend. Is data changing? Is the model degrading? | Model Owner via dashboard and Slack/email |
| **Threshold Breach** | Metric crosses threshold | Hard gate: pipeline blocked. Soft gate: warning logged. | Model Owner + 2nd Line |
| **Trend Degradation** | Metric trending downward for 5 consecutive runs (even if above threshold) | Proactive investigation before threshold is reached | Model Owner |
| **Eval Suite Stale** | No eval run for > 7 days (periodic evals) or > 30 days (data refresh) | Check if eval pipeline is broken or disabled | Platform Engineer |
| **New Failure Mode** | Previously unseen error type appears in eval results | Investigate, add to adversarial test suite, update eval suite | Model Owner + AI/ML Engineer |

### Alerting Integration

```yaml
# Example alerting configuration
alerting:
  channels:
    - type: "slack"
      webhook_url: "${SLACK_EVAL_ALERTS_WEBHOOK}"
      severity: ["breach", "degradation"]
    - type: "email"
      recipients: ["model-owner@company.com", "second-line@company.com"]
      severity: ["breach"]
    - type: "pagerduty"
      service_key: "${PAGERDUTY_EVAL_SERVICE}"
      severity: ["breach"]  # Only for high-risk systems with safety criteria
```

---

## 7. Implementation Checklist

| # | Item | Priority | Status |
|---|------|----------|--------|
| 1 | Eval suite code exists in version control alongside model/agent code | Critical | [ ] |
| 2 | CI/CD pipeline runs eval suite on every code change affecting AI behavior | Critical | [ ] |
| 3 | Hard gates block pipeline on failure; soft gates log warnings | Critical | [ ] |
| 4 | Eval results stored as pipeline artifacts with retention >= 1 year | Important | [ ] |
| 5 | Gate decisions logged to audit trail with criterion details and approver | Critical | [ ] |
| 6 | Dashboard displays current eval status and historical trends | Important | [ ] |
| 7 | Alerting configured for threshold warning, breach, and trend degradation | Important | [ ] |
| 8 | Hard gate override protocol documented and requires Committee approval | Critical | [ ] |
| 9 | Eval data versioned and separated from training data | Critical | [ ] |
| 10 | Periodic eval runs scheduled for production monitoring | Important | [ ] |

---

## Cross-References

- **Eval-Driven Development:** [eval-driven-development.md](eval-driven-development.md) -- the methodology that produces the eval suites wired into gates
- **Acceptance Criteria Automation:** [acceptance-criteria-automation.yaml](acceptance-criteria-automation.yaml) -- machine-executable criteria definitions consumed by gates
- **Pre-Deployment Gate:** [../checklists/pre-deployment-gate.yaml](../checklists/pre-deployment-gate.yaml) -- the checklist that eval gates help satisfy
- **Defining Acceptance Criteria:** [../../01-discovery-governance/evaluations/defining-acceptance-criteria.md](../../01-discovery-governance/evaluations/defining-acceptance-criteria.md) -- source of thresholds used in gates
- **Continuous Online Evaluation:** [../../03-runtime-governance/evaluations/continuous-online-evaluation.md](../../03-runtime-governance/evaluations/continuous-online-evaluation.md) -- production-side continuation of eval monitoring
- **Governance in Agile Sprints:** [../../07-enterprise-implementation/process-integration/governance-in-agile-sprints.md](../../07-enterprise-implementation/process-integration/governance-in-agile-sprints.md) -- how gate setup work fits into sprint planning

---

*Last updated: 2026-02-28*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
