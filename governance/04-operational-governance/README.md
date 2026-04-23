# Pillar 4: Operational Governance

## Purpose

Operational Governance ensures that AI systems remain safe, secure, performant, compliant, and accountable **over their entire production lifetime** -- from initial deployment through eventual decommissioning. While Runtime Governance asks "is it behaving correctly right now?", Operational Governance asks: **"Is it still safe over time? What happens when things go wrong? Are we meeting our regulatory obligations?"**

This pillar covers the long-term operational concerns: security hardening, incident management, drift detection, audit readiness, cost governance, regulatory reporting, and decommissioning. These are the concerns that keep a system in production confidently, not just initially, but for years.

## When to Use

Apply Operational Governance continuously throughout the production lifecycle:

- When managing an AI system in production (daily operations)
- When responding to an AI-related incident
- When conducting periodic model revalidation
- When preparing for a regulatory audit or examination
- When detecting and responding to data or concept drift
- When managing AI system costs and resource consumption
- When decommissioning an AI system that is no longer needed

**Trigger:** Operational Governance is not a one-time activity. It begins at deployment and continues until the system is fully decommissioned and audit records are archived.

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **Model Owner** | **Accountable** -- owns the system's operational health, triggers revalidation, manages the system's lifecycle |
| **MLOps / Platform Engineer** | **Responsible** -- operates monitoring, security controls, and infrastructure; executes incident response |
| **On-Call Engineer** | **Responsible** -- first responder for production incidents |
| **Compliance Officer (2nd Line)** | **Reviewer** -- conducts periodic reviews, validates regulatory compliance, reviews incident reports |
| **Internal Audit (3rd Line)** | **Assurer** -- provides independent assurance that governance is effective |
| **AI Governance Committee** | **Approver** -- approves material changes, revalidation outcomes, and decommissioning decisions |

## Regulatory Basis

- **EU AI Act Article 72** -- Post-market monitoring system for high-risk AI systems
- **EU AI Act Article 62** -- Reporting of serious incidents
- **DORA Article 11** -- ICT incident management procedures
- **DORA Article 8** -- ICT change management and risk assessment
- **SAFEST items S-12** (drift detection), **S-13** (fallback), **S-14** (recovery time), **S-20** (periodic revalidation), **A-11** (audit trail), **A-15** (incident process), **A-18** (root cause analysis)
- **DNB Good Practice** -- Ongoing model monitoring, periodic revalidation, incident reporting

---

## What This Pillar Covers

Operational Governance spans six domains. Files in this directory will address each domain as the framework matures.

### Domain 1: Security

Protecting AI systems from external attacks and internal misuse.

| Concern | Description | Key Activities |
|---------|-------------|---------------|
| **Prompt Injection Defense** | Protecting LLM-based systems from adversarial inputs | Regularly update prompt injection test suites; monitor guardrail bypass attempts; patch vulnerabilities |
| **Model Theft Protection** | Preventing unauthorized access to proprietary models | Access control, API rate limiting, model obfuscation for exposed endpoints |
| **Data Poisoning Detection** | Detecting manipulation of training or input data | Monitor data pipeline integrity, validate data source authenticity |
| **Access Control** | Ensuring only authorized users and systems can access AI components | RBAC for model endpoints, audit access logs, rotate credentials |
| **Supply Chain Security** | Governing third-party models and libraries | Vendor assessment, dependency scanning, license compliance |

Cross-reference: [Pre-Deployment Gate](../02-development-governance/checklists/pre-deployment-gate.yaml) (DEV-SEC-001 through DEV-SEC-004)

### Domain 2: Incident Management

Detecting, responding to, and learning from AI-specific incidents.

| Concern | Description | Key Activities |
|---------|-------------|---------------|
| **Detection** | Identifying AI incidents from monitoring signals | Alert rules, anomaly detection, user complaint routing |
| **Classification** | Determining severity and scope of AI incidents | AI-specific severity matrix (safety violation vs. performance degradation vs. bias detection) |
| **Response** | Containing and resolving AI incidents | Circuit breaker activation, rollback, manual fallback, customer communication |
| **Root Cause Analysis** | Understanding why the incident occurred | Audit trail reconstruction, data analysis, model behavior analysis |
| **Prevention** | Ensuring the incident does not recur | Eval suite expansion, guardrail updates, process improvements |
| **Regulatory Reporting** | Reporting serious incidents as required by regulation | EU AI Act Article 62 reporting for serious incidents; DORA incident reporting |

Cross-reference: [Continuous Online Evaluation](../03-runtime-governance/evaluations/continuous-online-evaluation.md) (alerting thresholds and response procedures)

### Domain 3: Drift Detection and Revalidation

Detecting when the world has changed in ways that affect AI system performance.

| Concern | Description | Key Activities |
|---------|-------------|---------------|
| **Data Drift** | Input feature distributions changing vs. training data | Monitor statistical distribution of input features; alert on significant shifts |
| **Concept Drift** | The relationship between inputs and outputs changing | Monitor prediction accuracy against delayed outcome labels; compare to baseline |
| **Performance Drift** | Gradual degradation of model performance over time | Continuous evaluation against acceptance criteria; trend analysis |
| **Triggered Revalidation** | When drift detection triggers a full model reassessment | Execute full eval suite on current data; compare to deployment baseline; decide: retrain, recalibrate, or decommission |
| **Scheduled Revalidation** | Regular comprehensive model review independent of drift signals | Annual for all systems; quarterly for high-risk (see [Risk Tiering Model](../07-enterprise-implementation/risk-based-adoption/risk-tiering-model.md)) |

Cross-reference: [Evaluation Strategy Template](../01-discovery-governance/evaluations/evaluation-strategy-template.yaml) (data source refresh schedules and escalation thresholds)

### Domain 4: Audit and Compliance

Maintaining audit readiness and meeting regulatory reporting obligations.

| Concern | Description | Key Activities |
|---------|-------------|---------------|
| **Audit Trail Integrity** | Ensuring decision logs are complete, tamper-resistant, and queryable | Verify audit trail completeness; test decision reconstruction capability; archive per retention policy |
| **Regulatory Reporting** | Producing reports required by supervisors | EU AI Act conformity documentation updates; DNB reporting; DORA ICT incident reports |
| **Audit Preparation** | Being ready for regulatory examination at any time | Maintain current model cards, eval results, governance artifacts; conduct internal audit rehearsals |
| **Evidence Management** | Organizing governance evidence so it can be produced on demand | Evidence linked from every checklist item; centralized evidence repository; version-controlled |
| **Compliance Gap Analysis** | Identifying gaps between current governance and evolving requirements | Annual compliance review; regulatory change monitoring; gap remediation planning |

Cross-reference: [Three Lines of Defense](../07-enterprise-implementation/organizational-model/three-lines-of-defense-for-ai.md) (audit responsibilities by line)

### Domain 5: Cost Governance

Managing the financial aspects of AI system operation.

| Concern | Description | Key Activities |
|---------|-------------|---------------|
| **Compute Cost Monitoring** | Tracking LLM API costs, GPU usage, inference costs | Cost dashboards per system, cost alerts, budget thresholds |
| **Cost-per-Decision** | Understanding the unit economics of AI decisions | Track total cost / total decisions; compare to human decision cost |
| **Cost Optimization** | Reducing costs without degrading quality | Model distillation, caching, batching, prompt optimization, model selection |
| **Budget Planning** | Forecasting AI operational costs | Volume projections, cost-per-unit trends, seasonal patterns |
| **Chargebacks** | Allocating AI costs to the business units that consume them | Cost attribution by product, team, or use case |

### Domain 6: Decommissioning

Responsibly retiring AI systems that are no longer needed, no longer performing, or no longer compliant.

| Concern | Description | Key Activities |
|---------|-------------|---------------|
| **Decommission Triggers** | When should an AI system be retired? | Performance below acceptable thresholds with no remediation path; regulation prohibits the use case; business need no longer exists; replacement system proven superior |
| **Decommission Process** | How to retire safely | Transition plan to replacement (human process or new system); customer communication; data archival; model artifact archival; audit trail preservation |
| **Post-Decommission** | Obligations after shutdown | Retain audit records per retention policy; maintain ability to explain past decisions for regulatory inquiries; update AI system inventory |

---

## How This Pillar Connects to Others

### Inputs from Runtime Governance

| Input | Source | Used For |
|-------|--------|----------|
| Monitoring alerts and anomalies | [Continuous Online Evaluation](../03-runtime-governance/evaluations/continuous-online-evaluation.md) | Trigger incident response, drift investigation |
| Audit trail data | [Multi-Agent Governance](../03-runtime-governance/agentic-workflows/multi-agent-governance-framework.md) | Incident reconstruction, compliance reporting |
| Escalation events | Runtime guardrails | Incident classification, trend analysis |

### Feedback to Discovery Governance

| Feedback | Destination | Purpose |
|----------|-------------|---------|
| Incident learnings | [Discovery Governance](../01-discovery-governance/) | Inform risk classification for future systems; update acceptance criteria for current systems |
| Drift reports | Risk classification review | May trigger reclassification to higher or lower risk tier |
| User feedback patterns | Product discovery | Identify new feature opportunities, unmet needs, emerging risks |
| Decommission learnings | Governance improvement | Improve the governance framework itself based on operational experience |

### Relationship to Enterprise Implementation

| Connection | Related File | How They Interact |
|-----------|-------------|------------------|
| Operational activities by risk tier | [Risk Tiering Model](../07-enterprise-implementation/risk-based-adoption/risk-tiering-model.md) | Risk tier determines monitoring intensity, revalidation frequency, audit depth |
| Who does what in operations | [Three Lines of Defense](../07-enterprise-implementation/organizational-model/three-lines-of-defense-for-ai.md) | 1st line operates, 2nd line reviews, 3rd line audits |
| Governance Committee role | [AI Governance Committee Charter](../07-enterprise-implementation/organizational-model/ai-governance-committee-charter.md) | Committee reviews incident reports, approves revalidation outcomes, authorizes decommissioning |
| Sprint integration | [Governance in Agile Sprints](../07-enterprise-implementation/process-integration/governance-in-agile-sprints.md) | Operational improvements feed back into sprint backlogs |

---

## Key Operational Governance Principles

1. **Governance does not end at deployment.** Deployment is the beginning of operational governance, not the end of governance.

2. **Assume drift.** Every AI system will drift over time. The question is not whether, but when and how fast. Monitor proactively.

3. **Incidents are learning opportunities.** Every AI incident should result in a stronger eval suite, better guardrails, or improved processes. An incident without a prevention action is a wasted incident.

4. **Audit readiness is continuous.** Do not prepare for audits. Be permanently audit-ready. If you cannot produce governance evidence on demand, your governance is insufficient.

5. **Decommissioning is a governance act.** Shutting down an AI system requires as much governance discipline as deploying one. Data must be archived, audit trails preserved, customers transitioned.

6. **Cost is a governance concern.** An AI system that is too expensive to operate responsibly (including governance overhead) should not be in production. Cost governance prevents the scenario where governance is the first thing cut when budgets tighten.

---

## Getting Started

1. **Setting up operations for a newly deployed system?** Review the six domains above and establish monitoring, incident response, and revalidation processes proportional to the system's risk tier.

2. **Responding to an incident?** Follow the response procedure in [Continuous Online Evaluation](../03-runtime-governance/evaluations/continuous-online-evaluation.md) Section 5, then conduct root cause analysis and expand the eval suite.

3. **Preparing for a regulatory audit?** Verify that all governance artifacts are current, evidence references are valid, and the audit trail can reconstruct any past decision.

4. **Detecting drift?** Compare current metric values to deployment baselines. If significant drift is detected, trigger revalidation per the evaluation strategy's escalation thresholds.

5. **Considering decommissioning?** Document the rationale, plan the transition, communicate with affected stakeholders, archive artifacts, and update the AI system inventory.

---

*Last updated: 2026-02-28*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
