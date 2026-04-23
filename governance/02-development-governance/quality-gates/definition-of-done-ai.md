# Definition of Done for AI Features

## Purpose

This document defines what "done" means for AI features in a regulated FinTech environment. Traditional software Definition of Done (DoD) covers code quality, testing, and documentation. AI features require additional dimensions: model performance validation, fairness assessment, governance review, and operational readiness. An AI feature that passes unit tests but has not been evaluated for bias, documented in a model card, or configured for production monitoring is not done -- it is incomplete and unsafe to deploy.

This DoD is inspired by the Microsoft Responsible AI framework and adapted for the Three Lines of Defense governance model used in financial services.

## When to Use

- As the acceptance criteria for completing any sprint item that involves AI/ML/LLM capabilities
- During sprint reviews to determine whether an AI feature can be accepted
- As the checklist for the Model Owner before submitting to the pre-deployment gate
- When onboarding new team members to understand governance expectations for AI work

**Trigger:** A team member or team marks an AI feature as "done" in their sprint tracking system.

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **AI/ML Engineer** | **Responsible** -- completes all technical DoD items; assembles evidence |
| **Model Owner** | **Accountable** -- verifies all DoD items are satisfied before accepting the feature as done |
| **Product Manager** | **Consulted** -- confirms product-level acceptance criteria are met |
| **Ethics Lead** | **Consulted** -- reviews governance DoD items for limited/high-risk systems |
| **Compliance Officer (2nd Line)** | **Reviewer** -- validates governance DoD completeness for limited/high-risk systems |
| **Scrum Master** | **Informed** -- ensures DoD is applied consistently in sprint ceremonies |

## Regulatory Basis

- **EU AI Act Article 9** -- Risk management system must include testing and verification
- **EU AI Act Article 11** -- Technical documentation requirements for high-risk systems
- **EU AI Act Article 15** -- Accuracy, robustness, and cybersecurity requirements
- **SAFEST S-03** -- Acceptance criteria with performance thresholds
- **SAFEST T-12** -- Technical documentation (model card, data sheet)
- **SAFEST A-03** -- Formal approval process
- **SAFEST S-13, S-14** -- Fallback and recovery procedures
- **DORA Article 8** -- ICT risk management framework requirements

---

## 1. Definition of Done: Three Dimensions

The AI DoD has three dimensions that must all be satisfied. A feature is not done until all applicable items across all three dimensions are complete.

```
+---------------------------+
|   TECHNICAL DoD           |  "Does it work correctly?"
|   (1st Line: Eng/Product) |
+---------------------------+
            |
            v
+---------------------------+
|   GOVERNANCE DoD          |  "Is it safe, fair, and compliant?"
|   (2nd Line: Risk/Compl)  |
+---------------------------+
            |
            v
+---------------------------+
|   OPERATIONAL DoD         |  "Can we run it safely in production?"
|   (Shared: Eng + Ops)     |
+---------------------------+
```

---

## 2. Technical Definition of Done

These items verify that the AI feature works correctly and meets its acceptance criteria.

### 2.1 Model / Agent Performance

| # | DoD Item | Applicability | Status |
|---|---------|---------------|--------|
| T-01 | Acceptance criteria are defined with measurable metrics and explicit thresholds | All | [ ] |
| T-02 | Automated eval suite exists, is version-controlled, and covers all acceptance criteria | All | [ ] |
| T-03 | Eval suite ran against the current version and ALL blocking criteria PASS | All | [ ] |
| T-04 | Eval results include model/agent version hash, data version, and execution timestamp | All | [ ] |
| T-05 | For model updates: regression analysis shows no blocking regressions against the previous version | Updates only | [ ] |
| T-06 | Edge cases identified during discovery are documented and tested | Limited, High | [ ] |
| T-07 | Stress testing completed: system tested under adverse conditions (high load, degraded inputs) | Limited, High | [ ] |

### 2.2 Code Quality

| # | DoD Item | Applicability | Status |
|---|---------|---------------|--------|
| T-08 | Code reviewed by at least one peer (standard code review) | All | [ ] |
| T-09 | No critical or high-severity static analysis findings | All | [ ] |
| T-10 | Prompt templates and system instructions are version-controlled | LLM systems | [ ] |
| T-11 | Agent tool definitions are version-controlled with permission boundaries documented | Agent systems | [ ] |
| T-12 | Feature flags configured for gradual rollout (if applicable) | All | [ ] |

### 2.3 Data Quality

| # | DoD Item | Applicability | Status |
|---|---------|---------------|--------|
| T-13 | Training data provenance is documented (source, collection date, size, preprocessing) | ML models | [ ] |
| T-14 | Eval data is separate from training data (no contamination) | All | [ ] |
| T-15 | Data quality checks pass (completeness, accuracy, representativeness) | ML models | [ ] |
| T-16 | For fine-tuned LLMs: fine-tuning data is versioned and documented | Fine-tuned LLMs | [ ] |

---

## 3. Governance Definition of Done

These items verify that the AI feature has been assessed for ethical, fairness, and regulatory compliance.

### 3.1 Ethics and Fairness

| # | DoD Item | Applicability | Status |
|---|---------|---------------|--------|
| G-01 | Risk classification (EU AI Act tier) is confirmed and documented | All | [ ] |
| G-02 | Protected characteristics relevant to this use case are identified | Limited, High | [ ] |
| G-03 | Bias testing completed across identified protected groups | Limited, High | [ ] |
| G-04 | All fairness metrics are within governance thresholds | Limited, High | [ ] |
| G-05 | Fairness metric selection is documented with justification for chosen metrics | High | [ ] |
| G-06 | Proxy variable analysis completed: no features serve as unintended proxies for protected characteristics | High | [ ] |
| G-07 | Ethics review completed by Ethics Lead (or self-assessment for minimal risk) | Limited, High | [ ] |
| G-08 | For high-risk: Fundamental Rights Impact Assessment (FRIA) completed | High | [ ] |

### 3.2 Transparency and Explainability

| # | DoD Item | Applicability | Status |
|---|---------|---------------|--------|
| G-09 | AI disclosure is implemented: users know they are interacting with AI | Limited, High | [ ] |
| G-10 | Explanation mechanism is implemented for decisions affecting individuals | Limited, High | [ ] |
| G-11 | Explainability method is documented with known limitations | High | [ ] |
| G-12 | For customer-facing agents: agent identity is registered (machine identity / NHI) | Agent systems | [ ] |

### 3.3 Human Oversight

| # | DoD Item | Applicability | Status |
|---|---------|---------------|--------|
| G-13 | Human oversight model is defined: HITL, HOTL, or HOTA | All | [ ] |
| G-14 | Override mechanism is implemented: a human can override any AI decision | Limited, High | [ ] |
| G-15 | Escalation paths are defined and implemented | Agent systems | [ ] |
| G-16 | For high-risk: automation bias mitigation measures are in place | High | [ ] |

### 3.4 Documentation

| # | DoD Item | Applicability | Status |
|---|---------|---------------|--------|
| G-17 | Model card is complete and current | All | [ ] |
| G-18 | Data sheet is complete (for ML models using training data) | ML models | [ ] |
| G-19 | Known limitations are documented and communicated | All | [ ] |
| G-20 | AI system is registered in the organizational AI inventory | All | [ ] |

---

## 4. Operational Definition of Done

These items verify that the AI feature can be safely operated, monitored, and recovered in production.

### 4.1 Monitoring

| # | DoD Item | Applicability | Status |
|---|---------|---------------|--------|
| O-01 | Production monitoring is configured: metrics are collected, dashboards are built | All | [ ] |
| O-02 | Alert thresholds are defined and configured | All | [ ] |
| O-03 | Observability platform is receiving traces (LangSmith, Arize Phoenix, Opik, or Langfuse) | LLM/Agent systems | [ ] |
| O-04 | Drift detection is configured (input distribution monitoring) | ML models (Limited, High) | [ ] |
| O-05 | Cost monitoring is configured (per-inference cost tracking) | LLM systems | [ ] |

### 4.2 Resilience

| # | DoD Item | Applicability | Status |
|---|---------|---------------|--------|
| O-06 | Fallback procedure is documented: what happens when the AI fails | All | [ ] |
| O-07 | Fallback procedure has been tested in staging | Limited, High | [ ] |
| O-08 | Rollback procedure is documented: how to revert to the previous version | All | [ ] |
| O-09 | Rollback procedure has been tested | Limited, High | [ ] |
| O-10 | Kill switch (circuit breaker) is implemented and tested | Limited, High | [ ] |

### 4.3 Audit Trail

| # | DoD Item | Applicability | Status |
|---|---------|---------------|--------|
| O-11 | Audit trail logging is configured: all inputs, outputs, and decisions are logged | All | [ ] |
| O-12 | Log retention meets regulatory requirements (minimum 5 years for high-risk in financial services) | Limited, High | [ ] |
| O-13 | Logs are queryable for incident investigation and regulatory request response | Limited, High | [ ] |
| O-14 | PII handling in logs complies with GDPR (redaction or pseudonymization where required) | All | [ ] |

### 4.4 Operational Readiness

| # | DoD Item | Applicability | Status |
|---|---------|---------------|--------|
| O-15 | Runbook exists for operational support (troubleshooting, common issues, escalation) | All | [ ] |
| O-16 | On-call team is identified and trained on this system | Limited, High | [ ] |
| O-17 | Incident response procedure is configured for this system | Limited, High | [ ] |
| O-18 | Periodic revalidation schedule is defined | Limited, High | [ ] |

---

## 5. DoD by Risk Tier

Not all DoD items apply to all risk tiers. Use this summary to determine the minimum DoD for each tier.

| DoD Item Range | Minimal Risk | Limited Risk | High Risk |
|---------------|-------------|-------------|-----------|
| **Technical: T-01 to T-07** | T-01 to T-05 | T-01 to T-07 | T-01 to T-07 |
| **Technical: T-08 to T-16** | T-08, T-09, T-14 | T-08 to T-14 | T-08 to T-16 |
| **Governance: G-01 to G-08** | G-01 | G-01 to G-04, G-07 | G-01 to G-08 |
| **Governance: G-09 to G-12** | None | G-09, G-10, G-12 | G-09 to G-12 |
| **Governance: G-13 to G-16** | G-13 | G-13 to G-15 | G-13 to G-16 |
| **Governance: G-17 to G-20** | G-17 (brief), G-20 | G-17 to G-20 | G-17 to G-20 |
| **Operational: O-01 to O-05** | O-01, O-02 | O-01 to O-04 | O-01 to O-05 |
| **Operational: O-06 to O-10** | O-06, O-08 | O-06 to O-10 | O-06 to O-10 |
| **Operational: O-11 to O-14** | O-11 | O-11 to O-14 | O-11 to O-14 |
| **Operational: O-15 to O-18** | O-15 | O-15 to O-18 | O-15 to O-18 |
| **Total items** | ~15 | ~35 | ~45 |
| **Estimated DoD effort** | 2-4 hours | 1-2 days | 3-5 days |

---

## 6. Using the DoD in Sprint Ceremonies

### 6.1 Sprint Planning

When estimating AI work items, factor in DoD effort:

| Risk Tier | DoD Overhead to Add to Estimates |
|-----------|--------------------------------|
| Minimal | Add 10-15% to implementation estimate |
| Limited | Add 25-35% to implementation estimate |
| High | Add 40-60% to implementation estimate |

### 6.2 Sprint Review

During sprint review, the Model Owner confirms DoD completion:

> "Feature X meets the Definition of Done. All [N] applicable items are complete. The evidence package is stored at [location]. The verification sign-off was completed by [name] on [date]."

If any DoD item is incomplete:

> "Feature X is NOT done. [N] DoD items remain: [list]. The feature carries over to the next sprint. It is NOT eligible for deployment."

### 6.3 Retrospective

Track DoD-related metrics in retrospectives:

| Metric | What It Tells You |
|--------|-------------------|
| Average DoD completion time | Are DoD items taking longer than expected? Need better tooling or process? |
| DoD items most often incomplete at sprint end | Which governance activities are bottlenecks? |
| Features that deployed without full DoD | Governance compliance rate (target: 100%) |
| Post-deployment issues traceable to skipped DoD items | Evidence that DoD items prevent production issues |

---

## 7. DoD Checklist Template

```markdown
# Definition of Done Checklist

## Feature Information
- **Feature/Story:** [FILL IN]
- **Sprint:** [FILL IN]
- **Risk Tier:** [Minimal / Limited / High]
- **Model Owner:** [FILL IN]
- **Completion Date:** [FILL IN]

## Technical DoD
- [ ] T-01: Acceptance criteria defined
- [ ] T-02: Eval suite exists
- [ ] T-03: All blocking evals PASSING
- [ ] T-04: Eval results include version/timestamp
[... complete per risk tier ...]

## Governance DoD
- [ ] G-01: Risk classification confirmed
[... complete per risk tier ...]

## Operational DoD
- [ ] O-01: Monitoring configured
[... complete per risk tier ...]

## Verification
- [ ] Full verification checklist completed
- [ ] Evidence package assembled at: [LINK]

## Sign-Off
| Role | Name | Date |
|------|------|------|
| Model Owner | | |
| Product Manager | | |
```

---

## Cross-References

| Topic | Artifact | Location |
|-------|----------|----------|
| Release criteria (machine-readable) | Release Criteria | [quality-gates/release-criteria.yaml](release-criteria.yaml) |
| Verification before deployment | Verification Before Deployment | [guides/verification-before-deployment.md](../guides/verification-before-deployment.md) |
| Pre-deployment gate checklist | Pre-Deployment Gate | [pre-deployment-gate.yaml](../checklists/pre-deployment-gate.yaml) |
| Eval-driven development | Eval-Driven Development | [evaluations/eval-driven-development.md](../evaluations/eval-driven-development.md) |
| Model card template | Model Card | [templates/model-card.md](../templates/model-card.md) |
| Data sheet template | Data Sheet | [templates/data-sheet.md](../templates/data-sheet.md) |
| Bias assessment report | Bias Assessment Report | [templates/bias-assessment-report.md](../templates/bias-assessment-report.md) |
| Monitoring setup checklist | Monitoring Setup Checklist | [monitoring-setup-checklist.yaml](../../04-operational-governance/checklists/monitoring-setup-checklist.yaml) |
| Governance in agile sprints | Governance in Agile Sprints | [governance-in-agile-sprints.md](../../07-enterprise-implementation/process-integration/governance-in-agile-sprints.md) |
| Three Lines of Defense | Three Lines of Defense for AI | [three-lines-of-defense-for-ai.md](../../07-enterprise-implementation/organizational-model/three-lines-of-defense-for-ai.md) |

---

*Last updated: 2026-03-01*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
*Framework: [Product Governance for Agentic AI Workflows](../../README.md)*
