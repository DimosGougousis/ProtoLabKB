# Governance in CI/CD Pipelines

> **Purpose:** Define how automated governance gates integrate into CI/CD pipelines, transforming governance from a meeting-driven process into a code-driven, auditable, and repeatable system. Every AI model deployment passes through governance checks enforced by the pipeline, not by human memory.
>
> **When to Use:** During the Process Integration phase (Months 4-6 of the [Adoption Playbook](../risk-based-adoption/adoption-playbook.md)), and whenever a new AI system enters the development pipeline. This document is the reference specification for engineering teams configuring CI/CD governance gates.
>
> **Who Is Responsible:**
> - **Pipeline Configuration:** MLOps / DevOps Engineer (1st Line)
> - **Gate Criteria Definition:** CAIO + AI Ethics Board (2nd Line)
> - **Gate Override Approval:** CAIO or designated delegate (documented, audited)
> - **Audit of Gate Effectiveness:** Internal Audit (3rd Line)
>
> **Regulatory Basis:** SAFEST items S-03 (performance testing), S-04 (stress testing), S-05 (adversarial testing), S-13 (fallback procedures), F-03 (bias testing), T-12 (model cards), A-11 (decision audit trail), A-12 (model change log); EU AI Act Article 9 (risk management system), Article 15 (accuracy, robustness, cybersecurity); DORA Article 8 (ICT risk management framework).

---

## 1. Philosophy: Governance as Code

### 1.1 The Problem with Governance as Meetings

Traditional governance relies on review meetings, sign-off emails, and compliance checklists completed by hand. This approach fails at scale because:

- **It does not scale.** A FinTech deploying 20+ AI models cannot convene a governance board for each deployment.
- **It is not repeatable.** Human reviewers apply criteria inconsistently across reviews.
- **It is not auditable.** "We discussed it in a meeting" is not evidence a regulator will accept.
- **It creates bottlenecks.** Product teams wait days or weeks for approvals, breeding governance resentment.

### 1.2 The Alternative: Governance as Code

Governance as Code means:

1. **Governance criteria are defined in version-controlled configuration files** (YAML, JSON) -- not in meeting minutes or emails.
2. **Governance checks are executed automatically** by the CI/CD pipeline -- not by human reviewers for standard cases.
3. **Governance outcomes are immutable audit artifacts** (pipeline logs, test reports, signed attestations) -- not verbal approvals.
4. **Governance gates block deployment** when criteria are not met -- no exceptions without documented override.

This does not eliminate human judgment. It automates the 80% of governance that is mechanical (did the eval pass? did the bias test run? is the model card complete?) so that human reviewers can focus on the 20% that requires judgment (should we deploy this use case at all? are the edge cases acceptable?).

### 1.3 Alignment with Federated Governance Model

The CI/CD governance approach supports the [federated governance model](../organizational-model/ai-center-of-excellence.md): the central AI CoE defines the gate criteria (the ~75% of rules), and local product teams execute those gates autonomously through their pipelines without waiting for central approval on every deployment.

---

## 2. Pipeline Stages with Governance Checkpoints

```
+----------+    +----------+    +----------+    +----------+    +----------+
|          |    |          |    |          |    |          |    |          |
|  PRE-    |--->|  BUILD   |--->|  TEST    |--->|  DEPLOY  |--->|  POST-   |
|  COMMIT  |    |          |    |          |    |          |    |  DEPLOY  |
|          |    |          |    |          |    |          |    |          |
+----------+    +----------+    +----------+    +----------+    +----------+
     |               |               |               |               |
     v               v               v               v               v
+---------+    +---------+    +-----------+    +---------+    +-----------+
|Governance|   |Governance|   |Governance  |   |Governance|   |Governance  |
|Gate 1    |   |Gate 2    |   |Gate 3      |   |Gate 4    |   |Gate 5      |
|          |   |          |   |            |   |          |   |            |
|- Prompt  |   |- Eval    |   |- Safety   |   |- Risk-   |   |- Smoke    |
|  safety  |   |  suite   |   |  policy   |   |  tier    |   |  tests    |
|  scan    |   |  exec    |   |  validate |   |  approval|   |- Canary   |
|- Secret  |   |- Bias    |   |- Guardrail|   |- Deploy  |   |  analysis |
|  detect  |   |  test    |   |  test     |   |  gate    |   |- Auto     |
|- Schema  |   |- Model   |   |- Adversar.|   |          |   |  rollback |
|  valid.  |   |  card    |   |  test     |   |          |   |           |
+---------+    +---------+    +-----------+    +---------+    +-----------+
```

---

## 3. Gate 1: Pre-Commit Hooks

**Trigger:** Every `git commit` on AI-related code paths.
**Blocking:** Yes -- commit is rejected if checks fail.
**Execution time target:** <10 seconds.

### 3.1 Checks

| Check | Tool | What It Does | Failure Action |
|-------|------|-------------|----------------|
| Prompt safety scanning | Custom linter / Semgrep rules | Scans prompt templates for injection vulnerabilities, unsafe patterns, and hardcoded PII | Block commit; display specific line and issue |
| Secret detection | git-secrets / detect-secrets / truffleHog | Detects API keys, tokens, credentials in code and config | Block commit; require secret removal |
| Schema validation | YAML/JSON schema validator | Validates guardrail config files, eval config files, and model card YAML against required schemas | Block commit; display schema violations |
| Prompt template linting | Custom rules | Checks system prompts for required elements: role boundaries, safety instructions, escalation triggers | Block commit; list missing required elements |

### 3.2 Configuration Example (pre-commit)

```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: prompt-safety-scan
        name: Prompt Safety Scanner
        entry: scripts/governance/prompt-safety-scan.sh
        language: script
        files: '(prompts|templates)/.*\.(yaml|yml|txt|md)$'

      - id: secret-detection
        name: Secret Detection
        entry: detect-secrets-hook
        language: python
        args: ['--baseline', '.secrets.baseline']

      - id: guardrail-schema-validation
        name: Guardrail Config Schema Validation
        entry: scripts/governance/validate-guardrail-schema.sh
        language: script
        files: '(guardrails|safety)/.*\.(yaml|yml|json)$'

      - id: model-card-schema
        name: Model Card Schema Validation
        entry: scripts/governance/validate-model-card.sh
        language: script
        files: 'model-cards/.*\.(yaml|yml)$'
```

---

## 4. Gate 2: Build Stage -- Automated Evaluation

**Trigger:** Every push to a feature branch or pull request.
**Blocking:** Yes -- merge is blocked if eval thresholds are not met.
**Execution time target:** <15 minutes (parallelized).

### 4.1 Checks

| Check | Tool / Framework | What It Does | Pass Criteria |
|-------|-----------------|-------------|--------------|
| Eval suite execution | DeepEval / RAGAS / custom | Runs the full evaluation suite defined for this model: accuracy, relevance, faithfulness, hallucination rate | All metrics above threshold defined in `eval-config.yaml` |
| Bias and fairness testing | Giskard / Aequitas / Fairlearn | Tests model outputs across protected groups for disparate impact, equal opportunity, demographic parity | No protected group below fairness threshold |
| Regression testing | DeepEval / custom | Compares eval results against the previous production version | No metric degrades by more than defined tolerance |
| Model card completeness | Custom validator | Checks that the model card YAML has all required fields populated (not empty, not placeholder) | 100% of required fields populated |
| Dependency vulnerability scan | Snyk / pip-audit / npm audit | Scans AI/ML dependencies for known vulnerabilities | No critical or high vulnerabilities |

### 4.2 Eval Configuration (YAML-Driven)

Gate criteria are defined in a version-controlled YAML file, not in pipeline scripts. This means governance criteria changes are tracked in git history and reviewed like code.

```yaml
# governance/eval-config.yaml
model_name: fraud-detection-agent-v2
risk_tier: high  # Determines which gates apply (see Section 8)

eval_thresholds:
  accuracy:
    metric: accuracy_score
    minimum: 0.95
    blocking: true
  faithfulness:
    metric: faithfulness_score
    minimum: 0.90
    blocking: true
  hallucination_rate:
    metric: hallucination_rate
    maximum: 0.02
    blocking: true
  relevance:
    metric: answer_relevancy
    minimum: 0.85
    blocking: false  # Warning only for limited-risk; blocking for high-risk

fairness_thresholds:
  protected_attributes:
    - gender
    - age_group
    - nationality
  metric: equalized_odds_difference
  maximum: 0.05
  blocking: true

regression_tolerance:
  max_degradation_percent: 2.0
  blocking: true

model_card:
  required_fields:
    - model_name
    - model_version
    - intended_use
    - out_of_scope_uses
    - training_data_description
    - evaluation_results
    - ethical_considerations
    - limitations
    - risk_tier
    - model_owner
  blocking: true
```

### 4.3 Pipeline Example (GitHub Actions)

```yaml
# .github/workflows/ai-governance-build.yml
name: AI Governance Build Gate

on:
  pull_request:
    paths:
      - 'models/**'
      - 'agents/**'
      - 'prompts/**'
      - 'guardrails/**'

jobs:
  governance-eval:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Load governance config
        id: config
        run: |
          RISK_TIER=$(yq '.risk_tier' governance/eval-config.yaml)
          echo "risk_tier=$RISK_TIER" >> $GITHUB_OUTPUT

      - name: Run evaluation suite
        run: |
          python -m governance.run_evals \
            --config governance/eval-config.yaml \
            --output reports/eval-results.json

      - name: Run bias testing
        run: |
          python -m governance.run_fairness \
            --config governance/eval-config.yaml \
            --output reports/fairness-results.json

      - name: Run regression tests
        run: |
          python -m governance.run_regression \
            --config governance/eval-config.yaml \
            --baseline reports/baseline-eval.json \
            --output reports/regression-results.json

      - name: Validate model card
        run: |
          python -m governance.validate_model_card \
            --config governance/eval-config.yaml \
            --model-card model-cards/fraud-detection-agent.yaml

      - name: Governance gate decision
        run: |
          python -m governance.gate_decision \
            --eval-results reports/eval-results.json \
            --fairness-results reports/fairness-results.json \
            --regression-results reports/regression-results.json \
            --config governance/eval-config.yaml

      - name: Upload governance artifacts
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: governance-reports
          path: reports/
          retention-days: 365  # Regulatory retention
```

---

## 5. Gate 3: Test Stage -- Safety and Adversarial Testing

**Trigger:** After build stage passes, before staging deployment.
**Blocking:** Yes for high-risk models; warning for limited-risk.
**Execution time target:** <30 minutes.

### 5.1 Checks

| Check | What It Does | Tool | Applies To |
|-------|-------------|------|-----------|
| Safety policy validation | Verifies the model's guardrail configuration matches the required safety policies for its risk tier | Custom validator against policy YAML | All risk tiers |
| Guardrail functional testing | Tests that input/output guardrails actually block the categories they are configured to block | NeMo Guardrails test suite / custom | All risk tiers |
| Adversarial testing (red team) | Automated adversarial prompts targeting known vulnerability categories: jailbreaks, prompt injection, information extraction | Garak / custom red team suite | High-risk models |
| Agent permission boundary testing | Verifies the agent cannot access tools, APIs, or data outside its defined permission scope | Custom sandbox test harness | Agent-based systems |
| Escalation path testing | Verifies the agent correctly escalates to a human when it should | Custom test scenarios | Agent-based systems with HITL/HOTL |
| Fallback behavior testing | Verifies the system degrades gracefully when the AI model is unavailable | Chaos engineering / custom | All risk tiers |

### 5.2 Safety Policy Configuration (GitOps)

Safety policies are version-controlled YAML files. Changing a safety policy requires a pull request with review from the AI Ethics Board or designated safety reviewer.

```yaml
# guardrails/policies/fraud-detection-agent-safety.yaml
model: fraud-detection-agent-v2
risk_tier: high
last_reviewed: 2026-02-15
reviewed_by: ai-ethics-board

input_guardrails:
  - type: prompt_injection_detection
    action: block_and_log
    sensitivity: high
  - type: pii_detection
    action: mask_and_proceed
    categories: [ssn, credit_card, bank_account]
  - type: topic_restriction
    action: block_and_escalate
    blocked_topics: [investment_advice, legal_advice, medical_advice]

output_guardrails:
  - type: factuality_check
    action: flag_for_review
    threshold: 0.85
  - type: toxicity_filter
    action: block_and_log
    threshold: 0.1
  - type: pii_leakage_prevention
    action: redact_and_log
    categories: [ssn, credit_card, bank_account, internal_account_id]

agent_boundaries:
  allowed_tools:
    - transaction_lookup
    - account_status_check
    - fraud_alert_create
  forbidden_tools:
    - account_modify
    - payment_initiate
    - user_data_export
  max_delegation_depth: 2
  require_human_approval_for:
    - fraud_alert_escalation_to_law_enforcement
    - account_freeze
```

### 5.3 Agent-Specific Pipeline Checks

For agentic AI systems, the pipeline includes additional checks that do not apply to traditional ML models:

| Check | Description | Why It Matters |
|-------|-------------|---------------|
| Tool-use permission verification | Verify the agent's tool manifest matches the approved permissions in the safety policy | Prevents privilege escalation -- agents should not gain new tool access without governance review |
| Sandbox configuration validation | Verify the agent runs in the correct sandbox environment (network isolation, filesystem restrictions) | Prevents agents from accessing systems outside their scope |
| Delegation chain depth test | Verify multi-agent systems respect maximum delegation depth | Prevents unbounded agent-to-agent delegation that bypasses human oversight |
| Autonomous decision boundary test | Verify the agent escalates decisions above its authority threshold | Ensures human oversight model (HITL/HOTL/HOTA) is correctly implemented |

---

## 6. Gate 4: Deploy Stage -- Risk-Tier Based Approval

**Trigger:** All previous gates passed; deployment to production requested.
**Blocking:** Yes -- no production deployment without gate passage.

### 6.1 Risk-Tier Deployment Rules

The level of human approval required depends on the model's risk tier, as defined in the [Risk Tiering Model](../risk-based-adoption/risk-tiering-model.md):

| Risk Tier | Deployment Approval | Who Approves | Max Wait Time |
|-----------|-------------------|-------------|---------------|
| **Minimal** | Automated -- deploy on green pipeline | Pipeline (no human required) | 0 (immediate) |
| **Limited** | Semi-automated -- team lead approval via PR merge | Product Team Lead + one 2nd Line reviewer | 4 business hours |
| **High** | Manual -- governance board approval via signed attestation | CAIO or AI Ethics Board delegate + Compliance + Model Owner | 5 business days |

### 6.2 Deployment Approval Attestation (High-Risk)

For high-risk AI systems, the deployment gate requires a signed attestation stored as a pipeline artifact:

```yaml
# governance/deployment-attestation.yaml
model_name: fraud-detection-agent-v2
model_version: 2.3.1
risk_tier: high
deployment_environment: production

attestation:
  eval_results_reviewed: true
  eval_results_ref: "pipeline-run-12345/reports/eval-results.json"
  fairness_results_reviewed: true
  fairness_results_ref: "pipeline-run-12345/reports/fairness-results.json"
  adversarial_test_results_reviewed: true
  adversarial_test_ref: "pipeline-run-12345/reports/adversarial-results.json"
  model_card_current: true
  model_card_ref: "model-cards/fraud-detection-agent.yaml"
  safety_policy_current: true
  safety_policy_ref: "guardrails/policies/fraud-detection-agent-safety.yaml"
  rollback_plan_documented: true
  rollback_plan_ref: "docs/runbooks/fraud-detection-rollback.md"

approvals:
  - role: model_owner
    name: "[FILL IN]"
    approved: true
    date: "[FILL IN]"
  - role: caio_delegate
    name: "[FILL IN]"
    approved: true
    date: "[FILL IN]"
  - role: compliance
    name: "[FILL IN]"
    approved: true
    date: "[FILL IN]"
```

### 6.3 Deployment Gate Override

Sometimes a deployment must proceed despite a failed gate (e.g., an urgent security patch). Overrides are permitted but strictly governed:

1. **Only the CAIO or their designated delegate** can authorize an override.
2. **The override reason must be documented** in the pipeline as a signed artifact.
3. **A remediation ticket is automatically created** in Jira (see [Jira Governance Workflows](../tooling-integration/jira-governance-workflows.md)) with a deadline for resolving the failed gate condition.
4. **All overrides are reported** in the [Quarterly Governance Report](../../06-executive/quarterly-governance-report.md) and flagged in the [Governance Dashboard](../../06-executive/governance-dashboard-spec.md).
5. **Override frequency is a governance metric.** More than 2 overrides per quarter triggers a root cause analysis.

---

## 7. Gate 5: Post-Deploy -- Canary Analysis and Rollback

**Trigger:** Immediately after production deployment.
**Duration:** 24-72 hours depending on risk tier.
**Automatic rollback:** Yes, if canary metrics breach thresholds.

### 7.1 Post-Deploy Checks

| Check | Metric | Threshold | Rollback Trigger |
|-------|--------|-----------|-----------------|
| Smoke tests | Core functionality pass rate | 100% | Any smoke test failure |
| Error rate monitoring | 5xx errors / total requests | <0.1% (or no worse than baseline + 0.05%) | Exceeded for 5 minutes |
| Latency monitoring | P99 latency | <SLA threshold (or no worse than baseline + 20%) | Exceeded for 10 minutes |
| Guardrail trigger rate | Guardrail triggers / total requests | <baseline + 2 standard deviations | Exceeded for 15 minutes |
| Escalation rate | Escalations to human / total agent interactions | <baseline + 50% | Exceeded for 30 minutes |
| Output quality (sample) | Automated eval on sample of live outputs | >eval threshold from Gate 2 | Below threshold on 3 consecutive samples |

### 7.2 Canary Analysis Configuration

```yaml
# governance/canary-config.yaml
model_name: fraud-detection-agent-v2
risk_tier: high

canary:
  duration_hours: 72  # High-risk: 72h; Limited: 24h; Minimal: 4h
  traffic_percentage: 5  # Start with 5% of traffic
  ramp_schedule:
    - hour: 0
      traffic_pct: 5
    - hour: 24
      traffic_pct: 25
    - hour: 48
      traffic_pct: 50
    - hour: 72
      traffic_pct: 100

  auto_rollback:
    enabled: true
    conditions:
      - metric: error_rate
        threshold: 0.001
        window_minutes: 5
      - metric: guardrail_trigger_rate
        threshold_above_baseline_stddev: 2.0
        window_minutes: 15
      - metric: escalation_rate_increase_pct
        threshold: 50
        window_minutes: 30

  notifications:
    on_rollback:
      - channel: slack
        target: "#ai-incidents"
      - channel: pagerduty
        target: "ai-oncall"
    on_success:
      - channel: slack
        target: "#ai-deployments"
```

### 7.3 Automatic Rollback Procedure

When a canary analysis triggers an automatic rollback:

1. **Traffic is immediately routed** back to the previous stable version.
2. **An AI incident ticket** is automatically created (see [Jira Governance Workflows](../tooling-integration/jira-governance-workflows.md), issue type: AI Incident).
3. **The on-call engineer and model owner** are paged.
4. **Dashboard metrics** are updated to reflect the rollback event (see [Governance Dashboard](../../06-executive/governance-dashboard-spec.md)).
5. **The deployment cannot be retried** without a new pipeline run that passes all gates.

---

## 8. Risk-Tier Pipeline Profiles

Different risk tiers trigger different pipeline strictness. This is configured via the `risk_tier` field in `eval-config.yaml`.

| Pipeline Stage | Minimal Risk | Limited Risk | High Risk |
|---------------|-------------|-------------|-----------|
| Pre-commit hooks | Secret detection, schema validation | All minimal + prompt safety scan | All limited + prompt template linting |
| Eval suite | Core accuracy metrics | All minimal + relevance, faithfulness | All limited + hallucination rate, edge cases |
| Bias testing | Not required | Statistical fairness check | Full disparate impact analysis across all protected groups |
| Adversarial testing | Not required | Basic jailbreak test suite | Full red-team suite (Garak + custom) |
| Safety policy validation | Basic output filter | Input + output guardrails | Full guardrail suite + agent boundary tests |
| Model card | Minimal card (5 fields) | Standard card (10 fields) | Full card (all fields) |
| Deploy approval | Auto-deploy on green | Team lead + 2nd line review | CAIO + Compliance + Model Owner attestation |
| Canary duration | 4 hours | 24 hours | 72 hours |
| Post-deploy sampling | Daily | Hourly | Continuous |

---

## 9. GitOps for Safety Policies

### 9.1 Principle

All governance configuration -- eval thresholds, safety policies, guardrail configs, deployment attestations -- lives in git alongside the model code. This means:

- Every change to a governance rule has a commit message, author, and timestamp.
- Changes to governance criteria require pull request review (from 2nd Line).
- Governance configuration can be audited by diffing git history.
- Rollback of governance criteria is as simple as reverting a commit.

### 9.2 Repository Structure

```
governance/
  eval-config.yaml              # Eval thresholds per model
  canary-config.yaml            # Post-deploy canary settings
  deployment-attestation.yaml   # Signed deployment approval

guardrails/
  policies/                     # Safety policies per model
    fraud-detection-agent-safety.yaml
    customer-service-bot-safety.yaml
  schemas/                      # JSON schemas for validation
    safety-policy-schema.json
    eval-config-schema.json

model-cards/
  fraud-detection-agent.yaml
  customer-service-bot.yaml

scripts/
  governance/
    prompt-safety-scan.sh
    validate-guardrail-schema.sh
    validate-model-card.sh
```

### 9.3 CODEOWNERS for Governance Files

```
# .github/CODEOWNERS
governance/            @ai-ethics-board @caio
guardrails/policies/   @ai-ethics-board @caio
model-cards/           @model-owners @ai-ethics-board
```

This ensures that changes to governance configurations require review from the appropriate governance authority, enforced by the git platform -- not by human memory.

---

## 10. Integration with Eval Frameworks

### 10.1 Supported Frameworks

| Framework | Use Case | Pipeline Integration |
|-----------|---------|---------------------|
| **DeepEval** | LLM evaluation: faithfulness, relevance, hallucination, bias | Python test runner; outputs JSON for gate decision |
| **RAGAS** | RAG pipeline evaluation: context precision, answer relevancy, faithfulness | Python test runner; outputs JSON |
| **Giskard** | Bias/fairness testing, vulnerability scanning, robustness | Python API; outputs structured report |
| **Garak** | LLM adversarial testing (red-teaming) | CLI tool; outputs JSON vulnerability report |
| **Evidently AI** | Data drift detection, model monitoring | Python API; integrates with monitoring stack |
| **Custom eval harness** | Organization-specific eval criteria | Python script reading `eval-config.yaml` |

### 10.2 Gate Decision Logic

The gate decision script reads results from all eval frameworks and the governance config to produce a pass/fail decision:

```python
# Pseudocode for governance gate decision
def gate_decision(eval_results, fairness_results, config):
    failures = []
    warnings = []

    for metric, threshold in config['eval_thresholds'].items():
        actual = eval_results[metric]
        if threshold.get('blocking') and not meets_threshold(actual, threshold):
            failures.append(f"BLOCKING: {metric} = {actual}, required {threshold}")
        elif not meets_threshold(actual, threshold):
            warnings.append(f"WARNING: {metric} = {actual}, target {threshold}")

    for attr in config['fairness_thresholds']['protected_attributes']:
        actual = fairness_results[attr]
        if actual > config['fairness_thresholds']['maximum']:
            failures.append(f"BLOCKING: fairness ({attr}) = {actual}")

    if failures:
        print("GOVERNANCE GATE: FAILED")
        for f in failures:
            print(f"  - {f}")
        sys.exit(1)  # Block the pipeline

    if warnings:
        print("GOVERNANCE GATE: PASSED WITH WARNINGS")
        for w in warnings:
            print(f"  - {w}")
    else:
        print("GOVERNANCE GATE: PASSED")

    sys.exit(0)
```

---

## 11. Audit Trail and Compliance Evidence

Every governance gate execution produces artifacts that serve as regulatory evidence:

| Artifact | Storage | Retention | SAFEST Ref |
|----------|---------|-----------|-----------|
| Eval results (JSON) | Pipeline artifacts + S3/GCS | 3 years | S-03 |
| Fairness test results (JSON) | Pipeline artifacts + S3/GCS | 3 years | F-03 |
| Adversarial test results (JSON) | Pipeline artifacts + S3/GCS | 3 years | S-05 |
| Deployment attestation (signed YAML) | Git repository + pipeline artifacts | 3 years | A-03, A-11 |
| Pipeline execution logs | CI/CD platform | 3 years | A-11 |
| Gate override records | Git repository + Jira | 3 years | A-11 |
| Canary analysis results | Observability platform | 3 years | S-12 |

These artifacts provide the evidence chain that regulators (DNB, EU AI Act authorities) need when assessing compliance. The pipeline produces the evidence automatically -- teams do not need to manually compile audit packages.

---

## 12. Cross-References

| Related Artifact | Location | Relationship |
|-----------------|----------|-------------|
| Governance in Agile Sprints | [process-integration/governance-in-agile-sprints.md](governance-in-agile-sprints.md) | CI/CD gates implement the Definition of Done criteria |
| Risk Tiering Model | [risk-based-adoption/risk-tiering-model.md](../risk-based-adoption/risk-tiering-model.md) | Risk tier determines pipeline strictness (Section 8) |
| Jira Governance Workflows | [tooling-integration/jira-governance-workflows.md](../tooling-integration/jira-governance-workflows.md) | Failed gates auto-create Jira tickets |
| Governance Dashboard Spec | [06-executive/governance-dashboard-spec.md](../../06-executive/governance-dashboard-spec.md) | Pipeline results feed dashboard metrics |
| Quarterly Governance Report | [06-executive/quarterly-governance-report.md](../../06-executive/quarterly-governance-report.md) | Override frequency reported quarterly |
| AI Center of Excellence | [organizational-model/ai-center-of-excellence.md](../organizational-model/ai-center-of-excellence.md) | CoE defines gate criteria; teams execute pipelines |
| Three Lines of Defense | [organizational-model/three-lines-of-defense-for-ai.md](../organizational-model/three-lines-of-defense-for-ai.md) | 1st Line executes; 2nd Line reviews criteria; 3rd Line audits |
| Eval-Driven Development | [02-development-governance/](../../02-development-governance/) | Eval suites are built during development, executed in CI/CD |
| Runtime Guardrails | [03-runtime-governance/](../../03-runtime-governance/) | Guardrail configs tested in Gate 3, enforced in production |

---

*Last updated: 2026-02-28*
*Version: 1.0*
*Classification: Internal / Engineering*
