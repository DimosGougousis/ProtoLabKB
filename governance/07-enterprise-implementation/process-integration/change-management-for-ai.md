# Change Management for AI Systems

## Purpose

Define the Change Advisory Board (CAB) process for AI model deployments, updates, and configuration changes. AI systems require change management beyond traditional IT change management because model changes can subtly alter decision-making behavior without visible infrastructure changes. A credit scoring model retrained on new data is a material change even if no code was modified. This document ensures all AI changes are classified, assessed, approved, and verified in a manner that satisfies DORA ICT change management requirements.

## When to Use

- Before any AI model deployment, update, retraining, or configuration change in production
- When modifying guardrails, evaluation thresholds, or agent permission boundaries
- When updating third-party AI service versions or switching AI providers
- When changing training data sources, feature sets, or model architectures
- During DORA compliance assessments to demonstrate ICT change management for AI

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **Model Owner** | **Responsible** -- initiates change request, prepares impact assessment |
| **CAIO** | **Accountable** -- approves or delegates approval based on change classification |
| **ML Engineer** | **Responsible** -- executes technical change, performs post-change verification |
| **AI Risk Analyst** | **Consulted** -- reviews impact assessment for high-risk system changes |
| **Compliance Officer** | **Consulted** -- assesses regulatory impact of the change |
| **Change Advisory Board** | **Approves** -- normal and emergency changes for high-risk AI systems |
| **Internal Audit** | **Informed** -- receives change log for audit trail |

## Regulatory Basis

- **DORA Article 8(4)** -- ICT risk management framework must include policies for changes to ICT systems, including testing and approval procedures
- **DORA Article 9(4)(e)** -- identification and implementation of changes required to ICT systems
- **EU AI Act Article 9** -- risk management system must be a continuous iterative process throughout the lifecycle, including when changes are made
- **EU AI Act Article 17** -- quality management system must address procedures for modification of high-risk AI systems
- **SAFEST item A-12** -- model change log with documented rationale and approval
- **SAFEST item S-19** -- independent validation after material changes
- **SAFEST item S-13** -- fallback and rollback procedures
- **DNB Good Practice for AI** -- changes to AI systems require structured assessment and approval

---

## 1. Change Classification

### 1.1 AI Change Types

Not all AI changes carry the same risk. Classification determines the approval path.

| Classification | Description | Examples | Approval Authority | Lead Time |
|---------------|------------|---------|-------------------|-----------|
| **Standard** | Pre-approved, low-risk, repeatable changes with documented procedures | Monitoring threshold adjustment within approved range; scheduled retraining on same data source; config parameter tuning within tested bounds | Model Owner (pre-approved by CoE) | Same day |
| **Normal** | Non-routine changes that require assessment but are not urgent | New model version deployment; feature set changes; training data source addition; guardrail rule updates; agent permission boundary changes | CAIO or delegate (Limited risk); CAB (High risk) | 5 business days |
| **Emergency** | Changes required to prevent or resolve an active incident or critical vulnerability | Model producing harmful outputs; security vulnerability in AI pipeline; compliance violation discovered; critical performance degradation | CAIO (immediate); post-hoc CAB review within 5 days | Immediate |

### 1.2 Change Classification Decision Tree

```
Is the change responding to an active incident or critical vulnerability?
  YES --> Emergency Change
  NO  --> Is this change type pre-approved in the standard change catalog?
            YES --> Standard Change
            NO  --> Normal Change
```

### 1.3 Standard Change Catalog

Maintain a pre-approved catalog of standard changes. Each entry includes the change type, conditions, procedure, and rollback steps. The catalog is reviewed quarterly by the CAIO.

| Standard Change | Conditions for Pre-Approval | Procedure Reference |
|----------------|---------------------------|-------------------|
| Scheduled model retraining (same architecture, same data source) | Performance within 5% of baseline; no new data categories; no feature changes | SOP-AI-RETRAIN-001 |
| Monitoring alert threshold adjustment | Within CAIO-approved range; documented rationale | SOP-AI-MONITOR-001 |
| Eval suite addition (no removal) | Adding stricter or additional evaluation criteria | SOP-AI-EVAL-001 |
| Guardrail rule tightening (no relaxation) | More restrictive filtering; no permissive changes | SOP-AI-GUARD-001 |
| LLM prompt template update (non-customer-facing) | Internal tools only; no customer impact | SOP-AI-PROMPT-001 |

---

## 2. Change Request Template

Every Normal and Emergency change requires a formal change request. Standard changes require only a log entry.

### 2.1 AI Change Request Form

```markdown
# AI Change Request -- CR-AI-[YYYY]-[NNN]

## 1. Change Summary
- **Change title:** [Brief description]
- **AI system affected:** [System name from AI inventory]
- **Risk tier of affected system:** [High / Limited / Minimal]
- **Change classification:** [Standard / Normal / Emergency]
- **Requested by:** [Name, role]
- **Date submitted:** [YYYY-MM-DD]
- **Target implementation date:** [YYYY-MM-DD]

## 2. Change Description
[What is changing? Be specific: model version, data source, feature set,
configuration parameter, architecture, guardrail, agent permission, etc.]

## 3. Business Justification
[Why is this change needed? What problem does it solve? What is the cost
of NOT making this change?]

## 4. Impact Assessment
### 4.1 Performance Impact
- Will model accuracy/precision/recall change? [Expected direction and magnitude]
- Have pre-deployment evaluations been run on the proposed change? [Yes/No -- attach results]

### 4.2 Fairness Impact
- Could this change affect fairness metrics for any protected group? [Yes/No/Unknown]
- Have bias evaluations been run on the proposed change? [Yes/No -- attach results]

### 4.3 Customer Impact
- Will customers experience different behavior? [Yes/No -- describe]
- Is customer communication required? [Yes/No -- plan attached]

### 4.4 Regulatory Impact
- Does this change affect regulatory compliance? [Yes/No -- specify regulation]
- Does this change require regulatory notification? [Yes/No -- specify]

### 4.5 Dependent Systems
- What systems consume this AI system's output? [List]
- Have dependent system owners been notified? [Yes/No]

## 5. Evaluation Results
[Attach or link to pre-change evaluation results for the proposed change]

## 6. Rollback Plan
- **Rollback trigger:** [What conditions trigger rollback?]
- **Rollback procedure:** [Step-by-step rollback instructions]
- **Rollback time:** [Estimated time to complete rollback]
- **Previous version preserved:** [Yes/No -- location]

## 7. Post-Change Verification
- **Verification steps:** [How will you confirm the change worked correctly?]
- **Verification timeline:** [When will verification occur? How long?]
- **Success criteria:** [Specific metrics and thresholds]

## 8. Approvals
| Role | Name | Decision | Date | Notes |
|------|------|----------|------|-------|
| Model Owner | | | | |
| AI Risk Analyst (high-risk) | | | | |
| Compliance Officer (if regulatory impact) | | | | |
| CAIO / CAB | | | | |
```

---

## 3. Impact Assessment for Model Changes

### 3.1 Impact Categories

| Impact Dimension | Assessment Questions | Risk Indicator |
|-----------------|---------------------|---------------|
| **Decision scope** | Does the change affect which decisions the AI makes or how it makes them? | High if yes |
| **Data scope** | Does the change introduce new data sources, categories, or increase data volume significantly? | High if new sensitive data |
| **Population scope** | Does the change affect which customers or products the AI serves? | High if expanding scope |
| **Behavioral scope** | Does the change alter the AI's response patterns, tone, or decision boundaries? | High for customer-facing agents |
| **Integration scope** | Does the change affect how the AI interacts with other systems? | Medium-High if downstream impact |
| **Regulatory scope** | Does the change trigger new regulatory obligations or affect existing compliance? | High if yes |

### 3.2 Impact Scoring

| Score | Definition | Governance Requirement |
|-------|-----------|----------------------|
| **Critical** | Change fundamentally alters AI behavior, scope, or risk profile | CAB approval + CAIO sign-off + 2nd line review + Board notification |
| **Major** | Change materially affects performance, fairness, or customer experience | CAB approval + CAIO sign-off |
| **Moderate** | Change has measurable but contained effect within existing risk boundaries | CAIO or delegate approval |
| **Minor** | Change has negligible effect on AI behavior or performance | Model Owner approval (log only) |

---

## 4. Approval Workflow

### 4.1 Normal Change Workflow

```
Model Owner submits CR-AI
         |
         v
AI Steward pre-screens
(classification, completeness)
         |
         v
+-- Is affected system High-Risk? --+
|                                     |
| YES                                 | NO
v                                     v
CAB reviews                    CAIO/delegate reviews
(within 5 business days)       (within 3 business days)
         |                            |
         v                            v
+----- Approved? -----+     +----- Approved? -----+
|  YES  |  NO  | DEFER|     |  YES  |  NO  | DEFER|
v       v      v      v     v       v      v
Deploy  Return  Fix &  Deploy  Return  Fix &
        with    re-     with    re-
        rationale submit rationale submit
         |                            |
         v                            v
Post-change verification       Post-change verification
(within 24-48 hours)           (within 24-48 hours)
         |                            |
         v                            v
Close CR-AI                    Close CR-AI
(evidence attached)            (evidence attached)
```

### 4.2 Emergency Change Workflow

| Step | Action | Owner | Timeline |
|------|--------|-------|----------|
| 1 | Declare emergency change with rationale | Model Owner or On-Call Engineer | Immediate |
| 2 | CAIO (or on-call delegate) grants verbal approval | CAIO | Within 30 minutes |
| 3 | Execute change with minimum viable verification | ML Engineer | As fast as safely possible |
| 4 | Document the change retroactively using CR-AI template | Model Owner | Within 24 hours |
| 5 | CAB post-hoc review of emergency change | CAB | Within 5 business days |
| 6 | Determine if permanent fix or rollback needed | CAB + Model Owner | At post-hoc review |

---

## 5. Rollback Requirements

### 5.1 Mandatory Rollback Capabilities

Every AI system deployment must have a tested rollback capability. This is not optional.

| Requirement | Description | SAFEST Ref |
|------------|------------|-----------|
| **Previous version preserved** | The prior model version, configuration, and weights must be stored and deployable | S-13 |
| **Rollback procedure documented** | Step-by-step instructions that any on-call engineer can follow | S-13 |
| **Rollback tested** | Rollback procedure must be tested in staging before production deployment | S-04 |
| **Rollback time SLA** | Maximum time to complete rollback, defined per risk tier | S-13 |
| **Rollback trigger criteria** | Specific, measurable conditions that automatically trigger rollback | S-12 |

### 5.2 Rollback Time SLAs

| System Risk Tier | Maximum Rollback Time | Trigger |
|-----------------|----------------------|---------|
| High Risk | 15 minutes | Automated (monitoring triggers) or manual (on-call decision) |
| Limited Risk | 1 hour | Manual decision by Model Owner or On-Call Engineer |
| Minimal Risk | 4 hours | Manual decision by Model Owner |

### 5.3 FinTech Example: Fraud Detection Model Rollback

A fraud detection model (high-risk) is redeployed with an updated feature set. Post-deployment monitoring detects a 15% increase in false positive rate within 30 minutes.

- **Rollback trigger:** false positive rate exceeds 110% of baseline for >15 minutes
- **Automated action:** monitoring system alerts on-call engineer + rolls back to previous model version
- **Rollback time:** 8 minutes (within 15-minute SLA)
- **Post-rollback:** CR-AI updated with rollback evidence; root cause analysis initiated; CAB post-hoc review scheduled

---

## 6. Post-Change Verification

### 6.1 Verification Checklist

| # | Verification Item | Timeline | Owner |
|---|------------------|----------|-------|
| 1 | Core performance metrics within expected range | Within 1 hour | ML Engineer |
| 2 | Fairness metrics unchanged or improved | Within 4 hours | Data Scientist |
| 3 | Error rates at or below pre-change levels | Within 4 hours | ML Engineer |
| 4 | No unexpected customer complaints or escalations | Within 24 hours | Product Manager |
| 5 | Dependent systems operating normally | Within 4 hours | ML Engineer |
| 6 | Logging and audit trail capturing correctly | Within 1 hour | ML Engineer |
| 7 | Guardrails and safety controls functioning | Within 1 hour | ML Engineer |
| 8 | Model card updated with change details | Within 48 hours | Model Owner |
| 9 | AI system inventory updated | Within 48 hours | Model Owner |

### 6.2 Extended Monitoring Period

After any Normal or Emergency change to a high-risk system, an extended monitoring period applies:

| Monitoring Aspect | Duration | Escalation Threshold |
|------------------|----------|---------------------|
| Performance metrics (accuracy, latency) | 14 days | >5% degradation from baseline |
| Fairness metrics | 14 days | Any statistically significant shift |
| Customer complaints related to AI behavior | 30 days | >2x baseline complaint rate |
| Dependent system health | 7 days | Any downstream anomaly |

---

## 7. DORA Implications for AI Change Management

### 7.1 DORA Requirements Mapping

| DORA Requirement | AI Change Management Response |
|-----------------|------------------------------|
| **Art. 8(4)** -- ICT change management policies | This document + Standard Change Catalog + CR-AI template |
| **Art. 9(4)(e)** -- identification of required ICT changes | AI risk register review triggers change identification |
| **Art. 11(1)** -- ICT-related incident management | Emergency change process integrates with AI incident response |
| **Art. 12** -- Classification of ICT-related incidents | Change-related incidents classified using AI severity framework |
| **Art. 16(1)** -- Testing of ICT tools and systems | Pre-deployment evaluation and post-change verification |

### 7.2 Audit Trail Requirements

Under DORA, the change management audit trail must be preserved and available for supervisory review:

| Audit Record | Retention Period | Location |
|-------------|-----------------|----------|
| Change request (CR-AI) | 5 years minimum | GRC platform or document repository |
| Impact assessment | 5 years minimum | Attached to CR-AI |
| Approval records (who, when, decision) | 5 years minimum | Workflow system or signed documents |
| Pre-change evaluation results | 5 years minimum | Evaluation pipeline output repository |
| Post-change verification results | 5 years minimum | Monitoring system + evidence repository |
| Rollback records (if triggered) | 5 years minimum | Incident management system |

---

## 8. Change Management Metrics

Track these metrics to assess change management effectiveness:

| Metric | Target | Measurement |
|--------|--------|------------|
| Change success rate (no rollback required) | >95% | Per quarter |
| Mean time from CR submission to approval | <5 business days (normal) | Per quarter |
| Emergency changes as % of total changes | <10% | Per quarter |
| Post-change incidents within 14 days | <5% of changes | Per quarter |
| Rollback time vs. SLA | 100% within SLA | Per change |
| Changes without documented rollback plan | 0 | Per change |

---

## Cross-References

- **Governance in CI/CD:** [governance-in-cicd.md](governance-in-cicd.md) -- automated governance gates that enforce change requirements in the pipeline
- **Governance in Agile Sprints:** [governance-in-agile-sprints.md](governance-in-agile-sprints.md) -- how change requests fit into sprint ceremonies
- **Risk Tiering Model:** [../risk-based-adoption/risk-tiering-model.md](../risk-based-adoption/risk-tiering-model.md) -- risk tier determines approval authority
- **Full Governance Profile:** [../risk-based-adoption/full-governance-profile.md](../risk-based-adoption/full-governance-profile.md) -- high-risk system change requirements
- **AI Incident Report Template:** [../../04-operational-governance/templates/ai-incident-report.md](../../04-operational-governance/templates/ai-incident-report.md) -- when changes cause incidents
- **SAFEST Checklist:** [../../04-operational-governance/regulatory/safest-checklist-detailed.md](../../04-operational-governance/regulatory/safest-checklist-detailed.md) -- items A-12, S-13, S-19

---

*Last updated: 2026-03-01*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
