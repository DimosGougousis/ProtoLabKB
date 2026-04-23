# Verification Before Deployment: The Iron Law for AI Releases

## Purpose

This document applies the Superpowers "iron law" -- no claim without evidence -- to AI model and agent releases. In traditional software, "it should work now" is not acceptable without a passing test suite and manual verification. In AI, the stakes are higher: an unverified model can cause financial harm, regulatory violations, and discriminatory outcomes at scale. This guide defines the verification checklist, automated verification pipeline, manual verification gates, evidence collection requirements, and sign-off workflow that must be completed before any AI system enters production.

Verification is not testing. Testing produces data. Verification is the act of reading that data, confirming it supports the claim, and recording that a human confirmed it. Verification closes the loop between "tests ran" and "we are confident this system is safe to deploy."

## When to Use

- Before every deployment of an AI system to production
- Before every model retrain or update that will be deployed
- Before every material change to prompts, guardrails, or agent behavior
- Before upgrading third-party AI model versions (e.g., GPT-4 to GPT-4o migration)
- Before expanding an existing AI system to new user populations or geographies

**Trigger:** The team believes the AI system is ready for deployment. Someone says "it's ready" or "tests are passing."

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **Model Owner** | **Accountable** -- signs off that verification is complete; bears accountability for deployment decision |
| **AI/ML Engineer** | **Responsible** -- executes verification steps, collects evidence, assembles verification package |
| **QA Lead** | **Responsible** -- validates that automated verification pipeline produced complete results |
| **Compliance Officer (2nd Line)** | **Reviewer** -- independently reviews verification evidence for limited/high-risk systems |
| **AI Governance Committee** | **Approver** -- approves deployment based on verification evidence for limited/high-risk systems |

## Regulatory Basis

- **EU AI Act Article 9(7)** -- Testing shall be carried out at appropriate points during development and before placing on the market
- **EU AI Act Article 16(a)** -- Providers must ensure high-risk AI systems comply before deployment
- **SAFEST S-19** -- Independent model validation before production use
- **SAFEST S-20** -- Validation methodology documentation
- **SAFEST S-21** -- Backtesting on historical data
- **SAFEST S-22** -- Benchmarking against alternative approaches
- **SAFEST A-03** -- Formal approval process with documented sign-off
- **DORA Article 25** -- Digital operational resilience testing before deployment
- **DNB Good Practice** -- Models must be validated before deployment; validation must be independent of development

---

## 1. The Iron Law Applied to AI

### 1.1 The Principle

> **Before claiming any AI system is ready for deployment, you must:**
> 1. IDENTIFY what evidence would prove the claim
> 2. RUN the full verification (fresh, complete, from scratch)
> 3. READ the full output (not just the summary; check exit codes, count failures)
> 4. CONFIRM the output supports the claim (not "close enough" -- actually supports it)
> 5. RECORD the verification (who verified, when, what they checked, what the results were)
>
> Skip any step and the claim is unverified. Unverified claims do not pass the deployment gate.

### 1.2 Rationalization Prevention for AI Releases

| What Teams Say | What Verification Requires |
|----------------|--------------------------|
| "The eval suite is passing" | Show the eval suite results. When did it last run? Against what data? What version of the model? |
| "We've been testing for weeks" | Show the most recent full run. Historical testing is good; deployment evidence must be current. |
| "It's the same model, just retrained on new data" | New data means new behavior. Run the full eval suite. Run regression analysis. Show results. |
| "The fairness metrics are fine" | Define "fine." Show the metrics against thresholds. Show per-group breakdown. |
| "We tested it manually and it looks good" | Manual testing complements automated verification. Show both. |
| "The previous version was approved, and this is only a minor change" | Every deployment needs its own verification. Show evidence for this version. |
| "We're confident" | Confidence is not evidence. Show evidence. |

---

## 2. Verification Checklist

Complete this checklist for every deployment. Each item requires evidence (a link to a report, screenshot, or artifact).

### 2.1 Automated Verification

| # | Verification Item | Evidence Required | Status | Evidence Ref |
|---|------------------|-------------------|--------|-------------|
| V-01 | Full eval suite ran against the exact version being deployed | Eval suite results with model version hash and timestamp | [ ] | |
| V-02 | All blocking eval criteria are PASSING | Eval results showing pass/fail for each blocking criterion | [ ] | |
| V-03 | No eval was skipped, disabled, or modified since the last approved threshold change | Diff of eval suite since last deployment showing no threshold changes | [ ] | |
| V-04 | Regression analysis ran against the previously deployed version | Regression comparison report with per-metric delta | [ ] | |
| V-05 | No blocking regressions detected (no metric decreased beyond tolerance) | Regression report with pass/fail for each regression check | [ ] | |
| V-06 | Fairness metrics computed across all identified protected groups | Fairness report with per-group metrics and threshold comparison | [ ] | |
| V-07 | Adversarial testing completed (for limited/high-risk) | Adversarial test results (prompt injection, jailbreak, data extraction) | [ ] | |
| V-08 | CI/CD pipeline completed successfully with all gates passing | CI/CD pipeline run log with gate pass/fail status | [ ] | |

### 2.2 Manual Verification

| # | Verification Item | Evidence Required | Status | Evidence Ref |
|---|------------------|-------------------|--------|-------------|
| V-09 | A human reviewed a representative sample of model/agent outputs | Review notes with sample size, selection method, and findings | [ ] | |
| V-10 | Edge cases identified in the model card were tested manually | Edge case test results with pass/fail for each documented edge case | [ ] | |
| V-11 | Fallback procedure was tested and confirmed working | Fallback test execution record with timestamp and outcome | [ ] | |
| V-12 | Rollback procedure was tested and confirmed working | Rollback test execution record with recovery time measurement | [ ] | |
| V-13 | Monitoring dashboards are configured and displaying data | Screenshot of monitoring dashboard with live data | [ ] | |
| V-14 | Alert thresholds are configured and a test alert was triggered | Test alert confirmation (sent, received, acknowledged) | [ ] | |

### 2.3 Documentation Verification

| # | Verification Item | Evidence Required | Status | Evidence Ref |
|---|------------------|-------------------|--------|-------------|
| V-15 | Model card is current and accurately reflects the version being deployed | Model card with version number matching deployment version | [ ] | |
| V-16 | Data sheet documents the training data used for this version | Data sheet with dataset version and hash | [ ] | |
| V-17 | Known limitations are documented and communicated to stakeholders | Limitations section in model card, reviewed by Model Owner | [ ] | |
| V-18 | Runbook exists for operational support of this system | Runbook document, reviewed by operations team | [ ] | |

### 2.4 Governance Verification

| # | Verification Item | Evidence Required | Status | Evidence Ref |
|---|------------------|-------------------|--------|-------------|
| V-19 | Risk classification is current and has not changed since last review | Risk classification confirmation or re-classification document | [ ] | |
| V-20 | Pre-deployment gate checklist is complete with all critical items addressed | Completed pre-deployment-gate.yaml with evidence references | [ ] | |
| V-21 | Approval obtained from the designated authority for this risk tier | Signed approval with approver name, role, date, and any conditions | [ ] | |
| V-22 | For high-risk: 2nd line (compliance/risk) has independently reviewed evidence | 2nd line review report with findings and sign-off | [ ] | |

---

## 3. Automated Verification Pipeline

### 3.1 Pipeline Architecture

```
[Deployment Request]
    |
    v
[Stage 1: Environment Verification]
    - Verify deployment target is correct (staging/canary/production)
    - Verify model version matches the approved version
    - Verify configuration matches the approved configuration
    |
    v
[Stage 2: Full Eval Suite Execution]
    - Run ALL eval tiers (unit, integration, system)
    - Run against FRESH data (not cached results)
    - Record execution timestamp, model version hash, data version hash
    |
    v
[Stage 3: Regression Analysis]
    - Load baseline results from previous approved deployment
    - Compare every metric against baseline
    - Flag regressions that exceed tolerance
    |
    v
[Stage 4: Fairness Verification]
    - Run Fairlearn metrics across all protected groups
    - Compare against governance thresholds
    - Generate fairness evidence report
    |
    v
[Stage 5: Operational Readiness Check]
    - Verify monitoring endpoints are responding
    - Verify alert routing is configured
    - Verify fallback endpoint is healthy
    - Verify audit logging is writing
    |
    v
[Stage 6: Evidence Package Assembly]
    - Collect all stage results into a single evidence package
    - Generate summary report with overall PASS/FAIL
    - Store evidence package in governance evidence repository
    |
    v
[Manual Review Gate]
    - Model Owner reviews evidence package
    - Signs off on verification (or requests re-verification)
```

### 3.2 Evidence Package Contents

```
verification-evidence/
  {system_name}/
    {version}/
      {timestamp}/
        summary.json                    # Overall PASS/FAIL with summary
        eval-suite-results.json         # Full eval suite results
        regression-analysis.json        # Regression comparison
        fairness-report.json            # Fairlearn output
        adversarial-test-results.json   # Prompt injection/jailbreak results
        operational-readiness.json      # Monitoring/alerting/fallback check
        manual-review-notes.md          # Human review notes
        sign-off.json                   # Approver name, role, date, conditions
```

---

## 4. Sign-Off Workflow

### 4.1 Sign-Off Authority by Risk Tier

| Risk Tier | Sign-Off Authority | Additional Requirements |
|-----------|-------------------|------------------------|
| **Minimal** | Model Owner + Tech Lead | Verification checklist complete; no blocking failures |
| **Limited** | Model Owner + AI Governance Committee | Verification checklist complete; fairness report reviewed by Ethics Lead |
| **High** | Model Owner + AI Governance Committee + Board Sponsor | Verification checklist complete; 2nd line independent review; FRIA completed |

### 4.2 Sign-Off Template

```markdown
# Deployment Verification Sign-Off

## System Information
- **System Name:** [FILL IN]
- **Version:** [FILL IN]
- **Model/Agent Hash:** [FILL IN]
- **Deployment Target:** [staging / canary / production]
- **Deployment Date:** [FILL IN]

## Verification Summary
- **Automated verification:** PASS / FAIL
- **Manual verification:** PASS / FAIL
- **Documentation verification:** PASS / FAIL
- **Governance verification:** PASS / FAIL
- **Overall:** PASS / FAIL

## Blocking Issues
- [List any unresolved blocking issues, or "None"]

## Conditions
- [List any conditions on the deployment, or "None"]
- [e.g., "Canary deployment to 5% traffic for 7 days before full rollout"]
- [e.g., "Daily fairness metric review for first 30 days"]

## Sign-Off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Model Owner | | | |
| Tech Lead | | | |
| Ethics Lead (Limited/High) | | | |
| Compliance Officer (Limited/High) | | | |
| AI Governance Committee Chair (Limited/High) | | | |
| Board Sponsor (High only) | | | |

## Evidence Package Location
[Link to full evidence package in governance repository]
```

---

## 5. Post-Deployment Verification

Verification does not end at deployment. Post-deployment verification confirms that the system behaves in production as it did in testing.

### 5.1 Post-Deployment Verification Checklist

| # | Verification Item | Timeline | Evidence Required |
|---|------------------|----------|-------------------|
| PD-01 | Production metrics match pre-deployment eval results (within 5% tolerance) | 24 hours post-deployment | Production metric comparison report |
| PD-02 | No spike in error rates, latency, or fallback triggers | 48 hours post-deployment | Monitoring dashboard screenshot |
| PD-03 | Fairness metrics in production match pre-deployment assessment | 7 days post-deployment (sufficient data) | Production fairness report |
| PD-04 | No customer complaints or incidents attributable to the new version | 7 days post-deployment | Incident log review |
| PD-05 | Canary deployment metrics confirm safe to proceed with full rollout | Per canary plan timeline | Canary comparison report |

### 5.2 Rollback Triggers

If any post-deployment verification item fails, initiate rollback:

| Trigger | Action | Authority |
|---------|--------|-----------|
| Production accuracy drops > 5% vs. pre-deployment | Automatic rollback (if configured) or manual rollback | Model Owner |
| Fairness metric exceeds governance threshold in production | Manual rollback within 4 hours | Model Owner + Ethics Lead |
| Customer-impacting incident attributable to new version | Immediate rollback | On-call engineer (notify Model Owner) |
| Safety violation detected (harmful output, data leak) | Immediate kill switch activation | Any team member (notify all stakeholders) |

---

## 6. Common Verification Failures and Resolutions

| Failure | Root Cause | Resolution |
|---------|-----------|------------|
| Eval suite passes in CI but fails in verification pipeline | Different data versions or environment configurations | Standardize eval data and environment; use containerized eval execution |
| Regression analysis shows improvement on some metrics but regression on others | Model trade-offs changed during optimization | Review each regression individually; get Model Owner approval for accepted trade-offs |
| Fairness metrics pass overall but fail for a small subgroup | Subgroup underrepresented in testing | Add subgroup-specific test cases; do not average away subgroup issues |
| Manual review finds issues not caught by automated evals | Eval suite coverage gap | Add new eval cases for every manually discovered issue; update eval suite |
| Monitoring dashboard shows no data after deployment | Instrumentation not deployed or misconfigured | Block full rollout until monitoring is confirmed working |

---

## Cross-References

| Topic | Artifact | Location |
|-------|----------|----------|
| Pre-deployment gate checklist | Pre-Deployment Gate | [pre-deployment-gate.yaml](../checklists/pre-deployment-gate.yaml) |
| Eval-driven development | Eval-Driven Development | [evaluations/eval-driven-development.md](../evaluations/eval-driven-development.md) |
| TDD for AI products | TDD for AI Products | [guides/tdd-for-ai-products.md](tdd-for-ai-products.md) |
| Definition of done for AI | Definition of Done for AI | [quality-gates/definition-of-done-ai.md](../quality-gates/definition-of-done-ai.md) |
| Release criteria | Release Criteria | [quality-gates/release-criteria.yaml](../quality-gates/release-criteria.yaml) |
| CI/CD eval gate integration | Eval Gate Integration | [eval-gate-integration.md](../evaluations/eval-gate-integration.md) |
| Continuous online evaluation | Continuous Online Evaluation | [continuous-online-evaluation.md](../../03-runtime-governance/evaluations/continuous-online-evaluation.md) |
| Model card template | Model Card | [templates/model-card.md](../templates/model-card.md) |
| Incident response | Incident Response Checklist | [incident-response-checklist.yaml](../../04-operational-governance/checklists/incident-response-checklist.yaml) |
| SAFEST S-19 to S-22 | SAFEST Checklist Detailed | [safest-checklist-detailed.md](../../04-operational-governance/regulatory/safest-checklist-detailed.md) |

---

*Last updated: 2026-03-01*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
*Framework: [Product Governance for Agentic AI Workflows](../../README.md)*
