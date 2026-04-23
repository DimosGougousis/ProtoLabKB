# Risk Mitigation Plan Template

## Purpose

This template provides a structured format for documenting, tracking, and governing risk mitigation plans for AI agents in the fleet. Every identified risk that requires active mitigation must be tracked through this template to ensure visibility on the Agent Fleet Command Dashboard, clear ownership of each step, deadline accountability, evidence-based closure, and audit-ready documentation.

Risk mitigation plans are living documents that transition through creation, execution, and closure. The Agent Fleet Command Dashboard visualizes plan progress in real time, enabling Fleet Operations and 2nd Line Compliance to monitor fleet-wide risk posture at a glance.

## When to Use

- When a risk is identified through continuous evaluation, audit, incident, or monitoring alert
- When the AI Governance Committee or 2nd Line Compliance requires a formal mitigation plan
- When a risk from the risk register requires active remediation steps
- When a regulatory finding mandates corrective action for an agent
- When an agent's risk tier is elevated and remediation steps are defined

## Who Is Responsible

| Role | R/A/C/I | Responsibility |
|------|---------|---------------|
| **Model Owner** | Accountable | Owns the mitigation plan; approves steps, deadlines, and closure |
| **AI/ML Engineer** | Responsible | Executes technical mitigation steps; provides evidence of completion |
| **MLOps / Platform Engineer** | Responsible | Executes infrastructure and deployment mitigation steps |
| **Product Manager** | Consulted | Assesses customer impact; provides input on mitigation priorities |
| **Compliance Officer (2nd Line)** | Reviewer | Reviews plan for regulatory adequacy; validates closure for high-risk agents |
| **Fleet Operations Lead** | Informed | Monitors plan progress on the fleet dashboard; escalates overdue steps |
| **AI Governance Committee** | Approver | Approves mitigation plans for critical-severity risks |

## Regulatory Basis

- **EU AI Act Article 9** -- Risk management system must include measures to eliminate or mitigate identified risks
- **EU AI Act Article 72** -- Post-market monitoring findings must result in corrective action
- **DORA Article 11** -- ICT incident management and corrective measures
- **SAFEST S-12** -- Drift detection must trigger mitigation action
- **SAFEST S-20** -- Periodic revalidation findings must be addressed through mitigation plans
- **DNB Good Practice** -- Documented risk mitigation with clear ownership and deadlines

---

## Risk Mitigation Plan

### Plan Metadata

| Field | Value |
|-------|-------|
| **Plan ID** | `MP-[AGENT_PREFIX]-YYYY-NNN` (e.g., MP-PAY-2026-003) |
| **Agent** | `<agent_name>` (`<agent_id>`) |
| **Risk ID** | `RISK-[AGENT_PREFIX]-YYYY-NNN` (link to risk register entry) |
| **Risk Description** | `<Clear description of the risk and its potential impact>` |
| **Severity** | `<Critical / High / Medium / Low>` |
| **Risk Category** | `<Model / Data / Prompt / Tool / Infrastructure / Process / Compliance>` |
| **Identified By** | `<Name, Role>` |
| **Identified Date** | `<YYYY-MM-DD>` |
| **Identification Source** | `<Evaluation / Audit / Incident / Monitoring Alert / Red-Team / Customer Feedback>` |
| **Plan Created Date** | `<YYYY-MM-DD>` |
| **Plan Owner** | `<Name, Role>` (Model Owner) |
| **Target Closure Date** | `<YYYY-MM-DD>` |
| **Plan Status** | `<Open / In Progress / Closed / Overdue>` |

### Severity Classification

| Severity | Definition | Approval Required | Dashboard Color |
|----------|-----------|-------------------|-----------------|
| **Critical** | Direct customer harm, regulatory breach, or financial loss risk | AI Governance Committee | Red |
| **High** | Significant performance degradation, potential compliance issue, or reputational risk | Model Owner + 2nd Line Compliance | Orange |
| **Medium** | Measurable quality reduction, operational inefficiency, or emerging risk trend | Model Owner | Amber |
| **Low** | Minor quality improvement opportunity, cosmetic issue, or proactive hardening | Model Owner | Blue |

---

### Mitigation Steps

| # | Step Description | Owner | Deadline | Status | Evidence Required | Evidence Provided |
|---|-----------------|-------|----------|--------|-------------------|-------------------|
| 1 | `<Description of first mitigation action>` | `<Name, Role>` | `<YYYY-MM-DD>` | `<Pending / Active / Done / Overdue / Blocked>` | `<What constitutes proof of completion>` | `<Link or description of evidence>` |
| 2 | `<Description of second mitigation action>` | `<Name, Role>` | `<YYYY-MM-DD>` | `<Status>` | `<Evidence required>` | `<Evidence provided>` |
| 3 | `<...>` | `<...>` | `<...>` | `<...>` | `<...>` | `<...>` |

### Step Status Definitions

| Status | Dashboard Indicator | Meaning |
|--------|-------------------|---------|
| **Pending** | Grey circle | Not started; awaiting prerequisite or scheduled start date |
| **Active** | Blue circle (animated) | In progress; owner is actively working on it |
| **Done** | Green checkmark | Completed; evidence documented and verified |
| **Overdue** | Red exclamation | Past deadline and not completed; escalation triggered |
| **Blocked** | Orange warning | Cannot proceed due to dependency or external factor |

---

### Progress Tracking

| Metric | Value |
|--------|-------|
| **Total Steps** | `<N>` |
| **Done** | `<N>` |
| **Active** | `<N>` |
| **Pending** | `<N>` |
| **Overdue** | `<N>` |
| **Blocked** | `<N>` |
| **Completion Percentage** | `<N/Total * 100>%` |

---

### Escalation Rules for Overdue Steps

| Overdue Duration | Escalation Action | Escalation Target |
|-----------------|-------------------|-------------------|
| **1-3 business days** | Automated reminder to step owner + notification to Model Owner | Step Owner, Model Owner |
| **4-7 business days** | Formal escalation. Revised deadline with written justification required. | Fleet Operations Lead |
| **> 7 business days** | Governance escalation. Agent risk tier may be temporarily elevated. | AI Governance Committee |
| **> 14 business days (Critical/High severity)** | Mandatory review by 2nd Line. Consider agent capability restriction. | Compliance Officer, AI Governance Committee |

---

### Plan Closure Criteria

The mitigation plan may only be closed when ALL of the following conditions are met:

- [ ] All mitigation steps have status "Done" with evidence documented
- [ ] Residual risk assessment has been performed and documented
- [ ] Verification evidence confirms the risk is mitigated (e.g., eval results, monitoring data)
- [ ] Model Owner has formally signed off on plan closure
- [ ] For High/Critical severity: 2nd Line Compliance has validated closure
- [ ] Post-mitigation monitoring period (minimum 2 weeks) has passed without recurrence
- [ ] Plan and all evidence archived in governance evidence store

### Residual Risk Assessment

| Field | Value |
|-------|-------|
| **Residual Risk Level** | `<None / Acceptable / Requires Monitoring / Requires Further Action>` |
| **Residual Risk Description** | `<Description of any remaining risk after mitigation>` |
| **Ongoing Monitoring** | `<What metrics or checks will be monitored to detect recurrence>` |
| **Next Review Date** | `<YYYY-MM-DD>` |

### Closure Sign-Off

| Approver | Name | Date | Signature |
|----------|------|------|-----------|
| **Model Owner** | `<Name>` | `<YYYY-MM-DD>` | `<Signed>` |
| **2nd Line Compliance** (High/Critical only) | `<Name>` | `<YYYY-MM-DD>` | `<Signed>` |

---

## FinTech Example: Cross-Border Payment Routing

### Plan Metadata

| Field | Value |
|-------|-------|
| **Plan ID** | MP-PAY-2026-003 |
| **Agent** | Payments Agent (agent:payments-agent-prod-01) |
| **Risk ID** | RISK-PAY-2026-007 |
| **Risk Description** | Cross-border payment routing occasionally selects a non-optimal corridor, resulting in higher FX costs for the customer. Root cause: the routing model does not account for intra-day FX rate fluctuations when selecting the settlement corridor. Estimated customer impact: EUR 0.50-2.00 per affected transaction. Affects approximately 3% of cross-border payments. |
| **Severity** | Medium |
| **Risk Category** | Model |
| **Identified By** | Jan de Vries, AI/ML Engineer |
| **Identified Date** | 2026-02-15 |
| **Identification Source** | Continuous monitoring -- cost-per-transaction KPI showed periodic spikes correlated with FX volatility windows |
| **Plan Created Date** | 2026-02-16 |
| **Plan Owner** | Maria Chen, Model Owner |
| **Target Closure Date** | 2026-03-25 |
| **Plan Status** | In Progress |

### Mitigation Steps

| # | Step Description | Owner | Deadline | Status | Evidence Required | Evidence Provided |
|---|-----------------|-------|----------|--------|-------------------|-------------------|
| 1 | Analyze routing logs for non-optimal corridor selections over the past 30 days. Quantify frequency, affected corridors, and cost impact. | Jan de Vries, AI/ML Engineer | 2026-02-18 | Done | Analysis report with statistics | [Routing analysis report 2026-02-18](link-to-report) |
| 2 | Identify root cause: confirm hypothesis that model does not account for FX rate fluctuation timing in corridor selection. | Jan de Vries, AI/ML Engineer | 2026-02-20 | Done | Root cause analysis document | [RCA-PAY-2026-007](link-to-rca): Confirmed -- model uses daily FX rate snapshot (06:00 UTC) but high-volatility corridors see 1-3% intra-day variation |
| 3 | Implement FX rate freshness check in routing logic. Add real-time FX rate lookup (max 15-min staleness) for corridors with > 0.5% daily volatility. | Jan de Vries, AI/ML Engineer | 2026-03-05 | Active | Code review approved; unit tests passing; integration test with FX provider API | -- |
| 4 | A/B test updated routing logic against current baseline. Primary metric: cost-per-transaction for cross-border payments. Minimum 2-week test, 1,000 transactions per variant. | Erik Bakker, MLOps Engineer | 2026-03-15 | Pending | A/B test report with statistical significance (p < 0.05) | -- |
| 5 | Deploy updated routing logic to production after A/B test validation. Full rollout per model version promotion process. | Maria Chen, Model Owner | 2026-03-20 | Pending | Deployment confirmation; post-deployment monitoring for 5 business days | -- |

### Progress Tracking

| Metric | Value |
|--------|-------|
| **Total Steps** | 5 |
| **Done** | 2 |
| **Active** | 1 |
| **Pending** | 2 |
| **Overdue** | 0 |
| **Blocked** | 0 |
| **Completion Percentage** | 40% |

---

## Cross-References

- **Agent Fleet Operations:** [../agentic-workflows/agent-fleet-operations.md](../agentic-workflows/agent-fleet-operations.md) -- Sec. 4 (Risk Mitigation Plan Governance) defines lifecycle and dashboard visualization
- **Agent Registry Entry:** [agent-registry-entry.yaml](agent-registry-entry.yaml) -- Registry `active_mitigations` field links to this plan
- **Continuous Online Evaluation:** [../evaluations/continuous-online-evaluation.md](../evaluations/continuous-online-evaluation.md) -- monitoring that identifies risks requiring mitigation
- **AI Incident Report:** [../../04-operational-governance/templates/ai-incident-report.md](../../04-operational-governance/templates/ai-incident-report.md) -- incidents may generate mitigation plans
- **SAFEST Checklist:** [../../04-operational-governance/regulatory/safest-checklist-detailed.md](../../04-operational-governance/regulatory/safest-checklist-detailed.md) -- regulatory items that may require mitigation
- **Risk Tiering Model:** [../../07-enterprise-implementation/risk-based-adoption/risk-tiering-model.md](../../07-enterprise-implementation/risk-based-adoption/risk-tiering-model.md) -- severity classification aligned with risk tiers
- **Governance Dashboard Specification:** [../../06-executive/governance-dashboard-spec.md](../../06-executive/governance-dashboard-spec.md) -- executive view of mitigation progress

---

*Last updated: 2026-03-01* / *Version: 1.0* / *Classification: Internal / Regulatory Preparation*
