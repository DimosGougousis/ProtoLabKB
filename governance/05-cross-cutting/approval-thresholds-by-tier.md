# Approval Thresholds by Risk Tier

> **Document Type:** Decision Rules / Operating Logic
> **Version:** 1.0
> **Effective Date:** 2026-04-28
> **Owner:** Chief AI Officer (CAIO)
> **Approved By:** AI Governance Council
> **Review Cycle:** Semi-annual, or upon risk tier change for any agent
> **Next Review:** 2026-10-28

---

## Purpose

This document defines the **operating logic** that most organizations miss: who approves what, under which conditions, and with which artifacts. It translates the risk tiers defined in the [AI Governance Policy](ai-governance-policy.md) into concrete decision rules, required artifacts, and launch gates.

## When to Use

- When a new AI system is ready for deployment approval
- When an existing AI system changes risk tier (e.g., Tier 1 → Tier 2 after adding API integrations)
- When a model update, prompt change, or data refresh requires re-approval
- When the Governance Council needs to verify approval completeness

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **Technical Owner** | Assembles required artifacts and submits approval request |
| **Policy Owner** | Confirms business readiness and signs off on intended use |
| **Security Lead** | Validates security and adversarial resilience controls |
| **Governance Council** | Reviews and approves Tier 2; recommends Tier 3 to Board |
| **Board of Directors** | Approves Tier 3 deployments |

## Regulatory Basis

- **EU AI Act Article 9(2)** — Risk management measures proportionate to risk level
- **EU AI Act Article 14(3)** — Human oversight measures appropriate to risk
- **ISO/IEC 42001 Clause 8.1** — Operational planning and control
- **ISO/IEC 42001 Clause 8.4** — AI system lifecycle processes
- **NIST AI RMF MG-1.1** — Risk response strategies defined and implemented
- **NIST AI RMF MS-2.1** — Pre-deployment evaluation performed

---

## 1. Decision Rule Summary

| Risk Tier | Primary Approver(s) | Escalation | Launch Gate |
|-----------|-------------------|------------|-------------|
| **Tier 1 — Advisory** | Technical Owner + Security Lead | None (Council notified) | Automated CI/CD gate |
| **Tier 2 — Conditional Autonomy** | Governance Council | Board (if residual risk Critical) | Council review meeting |
| **Tier 3 — High Autonomy** | Board of Directors | N/A (highest authority) | Board session |

### The Rule Set

```
IF risk_tier = 1
  AND model_card = complete
  AND eval_suite = passed
  AND security_review = passed
  THEN approve(Technical Owner + Security Lead)
  AND notify(Governance Council)

IF risk_tier = 2
  AND all Tier 1 requirements = met
  AND risk_assessment = complete
  AND human_oversight_plan = approved
  AND kill_switch = tested
  AND legal_review = complete (if customer-facing)
  THEN approve(Governance Council)

IF risk_tier = 3
  AND all Tier 2 requirements = met
  AND red_team_exercise = complete
  AND PE_validation = complete (if structural)
  AND incident_response_plan = board-approved
  AND residual_risk != "Critical"
  THEN recommend(Governance Council → Board)
  AND approve(Board of Directors)

IF residual_risk = "Critical" (any tier)
  THEN escalate(Board of Directors)
  AND require(unanimous Council recommendation)
```

---

## 2. Tier 1 — Advisory Agents

**Examples:** DFM analysis agents (CNC, injection molding, sheet metal, 3D printing), router classifier, materials recommender.

**Characteristics:** Read-only recommendations; no API calls to production systems; no autonomous actions; human decides what to do with outputs.

### 2.1 Required Artifacts

| Artifact | Owner | Completeness Criteria |
|----------|-------|----------------------|
| [Model Card](../02-development-governance/templates/model-card.md) | Technical Owner | All mandatory fields populated; limitations documented |
| [Eval Suite Results](../02-development-governance/evaluations/) | Technical Owner | Accuracy >90% on golden dataset; safety evals passed; no critical failures |
| [Input Sanitization Verification](../../ai-implementation-workstreams/01-agentic-ready-implementations/work-package-01-input-sanitization.md) | Security Lead | WP01 active; test results documented |
| [Agent Tier Classification](../01-discovery-governance/templates/agent-tier-classification.yaml) | Technical Owner | Tier 1 confirmed; classification rationale documented |
| [Source Grounding Data Contract](../protolabs/source-grounding-data-contract.yaml) | Technical Owner | Citation enforcement active (if knowledge-based) |

### 2.2 Approval Process

```
Technical Owner submits artifacts
        |
        v
Security Lead reviews (2 business days)
        |
        v
  +---------------------------+
  | APPROVED or REJECTED      |
  |                           |
  | If approved:              |
  |   → CI/CD gate unlocks    |
  |   → Council notified      |
  |                           |
  | If rejected:              |
  |   → Gaps documented       |
  |   → Re-submit when fixed  |
  +---------------------------+
```

### 2.3 Re-Approval Triggers

| Change Type | Re-Approval Required? | Who Approves |
|-------------|----------------------|-------------|
| Prompt template change | No (logged in change log) | Technical Owner |
| Model version upgrade (same vendor) | No (eval suite must re-pass) | Technical Owner |
| KB article refresh | No (freshness check must pass) | Technical Owner |
| New vendor model | Yes | Security Lead |
| Adding API/tool integration | Yes (reclassify to Tier 2) | Governance Council |
| Accuracy drops below 90% | Yes (deployment paused) | Security Lead |

---

## 3. Tier 2 — Conditional Autonomy Agents

**Examples:** Quote generation agent, production scheduling agent, quality inspection agent.

**Characteristics:** Can invoke tools and APIs (ERP, MES, CRM); generates outputs that affect business commitments; human approval required for exceptions or high-value decisions.

### 3.1 Required Artifacts

All Tier 1 artifacts, **plus:**

| Artifact | Owner | Completeness Criteria |
|----------|-------|----------------------|
| [Risk Assessment](../01-discovery-governance/templates/risk-management-plan.md) | Policy Owner | Full risk register with mitigations; residual risks documented |
| [Human Oversight Plan](../03-runtime-governance/human-in-the-loop-patterns.md) | Technical Owner | Defines which decisions require human approval; approval workflow documented |
| [Kill Switch Test Report](../03-runtime-governance/agentic-workflows/customer-facing-agent-safety.md) | Safety Officer | Kill switch activates within 30 seconds; test evidence documented |
| [Legal Review](../05-cross-cutting/regulatory-reference-index.md) | Legal Counsel | Required if customer-facing; compliance sign-off documented |
| [Incident Response Plan](../04-operational-governance/templates/ai-incident-report.md) | Safety Officer | Escalation paths defined; Sev1/Sev2 response procedures documented |
| [Bias and Fairness Assessment](../02-development-governance/evaluations/bias-and-fairness-evals.md) | Technical Owner | Required if outputs affect pricing or access; no discriminatory patterns |

### 3.2 Approval Process

```
Technical Owner submits artifacts (5 business days before Council meeting)
        |
        v
  +---------------------------+
  | PRE-REVIEW                |
  |                           |
  | Council members review    |
  | artifacts independently   |
  | (5 business days)         |
  +---------------------------+
        |
        v
  +---------------------------+
  | COUNCIL MEETING           |
  |                           |
  | 1. Presenter summary      |
  | 2. Q&A                    |
  | 3. Closed deliberation    |
  | 4. Decision               |
  +---------------------------+
        |
        v
  +---------------------------+
  | OUTCOME                   |
  |                           |
  | Approved:                 |
  |   → Deployment authorized |
  |                           |
  | Conditionally Approved:   |
  |   → Conditions must be    |
  |     met before deployment |
  |                           |
  | Rejected:                 |
  |   → Gaps documented       |
  |   → Re-submit next month  |
  |                           |
  | Escalated:                |
  |   → Board review required |
  +---------------------------+
```

### 3.3 Re-Approval Triggers

| Change Type | Re-Approval Required? | Who Approves |
|-------------|----------------------|-------------|
| Prompt template change | No (logged + eval re-pass) | Technical Owner |
| Model version upgrade | Yes | Governance Council |
| New API integration | Yes | Governance Council |
| Autonomy boundary expansion | Yes (may trigger Tier 3 reclassification) | Governance Council + Board |
| Kill switch modification | Yes | Safety Officer + Council |
| Vendor change | Yes | Governance Council |
| Sev1 incident | Yes (deployment paused until re-approval) | Governance Council |

---

## 4. Tier 3 — High Autonomy Agents

**Examples:** Autonomous parameter optimizer, autonomous quality control agent, self-adjusting production scheduler.

**Characteristics:** Acts independently within defined boundaries; human oversight by exception only; outputs directly affect production, pricing, or safety-critical decisions.

### 4.1 Required Artifacts

All Tier 1 and Tier 2 artifacts, **plus:**

| Artifact | Owner | Completeness Criteria |
|----------|-------|----------------------|
| [Red Team Exercise Report](../04-operational-governance/guides/red-teaming-ai-systems.md) | Security Lead | Adversarial testing complete; all critical findings remediated |
| [PE Validation Report](../02-development-governance/templates/model-card.md) | Professional Engineer | Required if agent produces structural design outputs; PE sign-off documented |
| [Board Incident Response Plan](../04-operational-governance/templates/ai-incident-report.md) | CAIO | Board notification procedures defined; board-level escalation path documented |
| [Continuous Monitoring Specification](../04-operational-governance/guides/drift-detection-runbook.md) | Technical Owner | Drift detection, misuse detection, and continuous eval specifications defined |
| [Autonomous Decision Governance](../03-runtime-governance/agentic-workflows/autonomous-decision-governance.md) | Safety Officer | Decision boundaries, override mechanisms, and audit trail specifications defined |
| [Vendor Lock-In Mitigation Plan](../05-cross-cutting/regulatory-reference-index.md) | Technical Owner | Required if dependent on third-party models; exit strategy documented |

### 4.2 Approval Process

```
Technical Owner submits artifacts to Council
        |
        v
  +---------------------------+
  | COUNCIL REVIEW            |
  |                           |
  | Full review per Tier 2    |
  | process                   |
  |                           |
  | Output: Recommendation    |
  | to Board (approve/reject) |
  +---------------------------+
        |
        v
  +---------------------------+
  | BOARD SESSION             |
  |                           |
  | 1. CAIO presents          |
  |    recommendation         |
  | 2. Board Q&A              |
  | 3. Board vote             |
  +---------------------------+
        |
        v
  +---------------------------+
  | OUTCOME                   |
  |                           |
  | Approved:                 |
  |   → Deployment authorized |
  |   → Enhanced monitoring   |
  |     activated             |
  |                           |
  | Rejected:                 |
  |   → Council documents     |
  |     gaps                  |
  |   → Re-submit when ready  |
  +---------------------------+
```

### 4.3 Re-Approval Triggers

All Tier 2 triggers, **plus:**

| Change Type | Re-Approval Required? | Who Approves |
|-------------|----------------------|-------------|
| Any model change | Yes | Council + Board |
| Autonomy boundary adjustment | Yes | Council + Board |
| Production environment change | Yes | Council + Board |
| Quarterly performance review | Mandatory review (may not require re-approval) | Council |

---

## 5. Shadow AI Prevention

No AI system may bypass these approval thresholds. The following controls prevent ungoverned deployments:

| Control | Implementation | Owner |
|---------|---------------|-------|
| **Centralized access control** | All AI model access through approved API gateways; no direct model access | Security Lead |
| **Role-based permissions** | Deployment permissions gated by risk tier; Tier 2+ requires Council role | Security Lead |
| **Audit logs** | All model invocations logged with agent ID, user ID, timestamp, input/output hash | Technical Owner |
| **CI/CD gate enforcement** | Deployment pipeline checks for approval record before production push | Head of Engineering |
| **Quarterly shadow AI scan** | Audit of all AI tool usage across the organization | Head of Internal Audit |

**Consequence:** Any AI system deployed without proper approval is immediately **quarantined** and the responsible Policy Owner is subject to governance review.

---

## 6. Approval Record Template

Every approved deployment must have an approval record:

```yaml
approval_record:
  approval_id: "APR-2026-001"
  agent_id: "cnc-machining-v2"
  risk_tier: "Tier 1"
  approval_date: "2026-05-06"
  approvers:
    - role: "Technical Owner"
      name: "[Name]"
      decision: "approved"
    - role: "Security Lead"
      name: "[Name]"
      decision: "approved"
  conditions: []
  artifacts_verified:
    - "model-card.md"
    - "dfm-accuracy-eval-suite.yaml"
    - "input-sanitization-verification.md"
    - "agent-tier-classification.yaml"
  re_approval_triggers:
    - "New vendor model"
    - "Adding API integration"
    - "Accuracy drops below 90%"
  expiry_date: "2027-05-06"
```

Approval records are stored in `governance/05-cross-cutting/approval-records/` and retained for **7 years**.

---

## Cross-References

| Document | Relationship |
|----------|-------------|
| [AI Governance Policy](ai-governance-policy.md) | Parent policy; this document implements Section 5 |
| [AI Governance Council Charter](ai-governance-council-charter.md) | Council decision process and authority |
| [Governance Roles & RACI](governance-roles-raci.md) | Detailed role definitions |
| [Agent Tier Classification](../01-discovery-governance/templates/agent-tier-classification.yaml) | How agents are classified into tiers |
| [Incident Severity Classification](../04-operational-governance/incident-severity-classification.md) | Incidents that trigger re-approval |
| [Governance by Stage Framework](../../docs/governance-by-stage-framework.md) | Per-stage governance gates |
| [ISO 42001 Gap Analysis](../../docs/iso-42001-gap-analysis.md) | Certification readiness |

---

*This document is version-controlled and auditable. Unauthorized modifications void governance compliance claims.*
