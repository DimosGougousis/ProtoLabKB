# Jira Governance Workflows

## Purpose

This document defines the Jira configuration for tracking AI governance activities: custom issue types, workflow definitions with approval states, dashboards, JQL queries, and automation rules. Governance activities -- ethics reviews, bias assessments, model validations, and governance gate approvals -- must be tracked with the same rigor as engineering work. Without structured tracking, governance becomes ad-hoc: reviews are skipped, approvals are verbal, evidence is lost, and audit trails are incomplete. Jira is the system of record that turns governance intentions into auditable, measurable execution.

This configuration integrates with the YAML checklists used throughout the framework, creating a bridge between governance documentation and operational workflow management.

## When to Use

- When setting up Jira for AI governance tracking during the tooling integration phase (Months 7-9 of the [Adoption Playbook](../../07-enterprise-implementation/risk-based-adoption/adoption-playbook.md))
- When onboarding a new AI system and creating its governance tracking structure in Jira
- When configuring dashboards for governance stakeholders (Model Owners, Compliance Officers, CAIO)
- When automating governance workflow steps that are currently manual
- When integrating Jira with CI/CD pipelines for automated governance gate checks

## Who Is Responsible

| Role | R | A | C | I |
|------|---|---|---|---|
| **Jira Administrator** | X | | | | Configures issue types, workflows, custom fields, automations |
| **AI Governance PM** | | X | | | Defines governance workflow requirements; owns dashboard views |
| **CAIO** | | | X | | Approves workflow design; consulted on governance gate definitions |
| **Model Owner** | | | X | | Consulted on per-system workflow needs; primary user of governance tickets |
| **Compliance Officer (2nd Line)** | | | X | | Consulted on regulatory evidence requirements; approves audit trail design |
| **Engineering Teams** | | | | X | Informed of workflow changes; users of governance issue types |

## Regulatory Basis

- **SAFEST item A-04** -- RACI matrix for AI lifecycle; Jira workflows enforce RACI at the ticket level
- **SAFEST item A-15** -- Incident response plan; Jira tracks incident tickets with regulatory timelines
- **EU AI Act Article 17** -- Quality management system including procedures for design, development, and testing
- **EU AI Act Article 12** -- Record-keeping; Jira provides audit trail of governance decisions
- **DORA Article 13** -- ICT logging; Jira captures governance decision logs
- **ISO/IEC 42001 Clause 7.5** -- Documented information; Jira is the system of record for governance artifacts
- **Best practice** -- Structured governance tracking prevents "governance in name only" anti-patterns

---

## 1. Custom Issue Types

### 1.1 Issue Type Definitions

| Issue Type | Icon | Description | Default Priority | Typical Assignee |
|-----------|------|-------------|-----------------|-----------------|
| **AI Ethics Review** | Shield | Ethics impact assessment for a new or changed AI system. Triggered during Discovery governance. | High | Ethics Lead / Compliance Officer |
| **Bias Assessment** | Scale | Fairness and bias evaluation for an AI system. Triggered during Development governance and periodic revalidation. | High | ML Engineer |
| **Model Validation** | Checkmark | Independent model validation by 2nd line of defense. Triggered before deployment and during periodic revalidation. | Critical | Independent Validator (2nd Line) |
| **Governance Gate** | Gate | Approval checkpoint at lifecycle transitions (Discovery-to-Development, Development-to-Deployment, etc.). | Critical | Gate Approver (varies by gate) |
| **Drift Investigation** | Trend | Investigation of a detected drift event. Auto-created by monitoring alerts. | Medium | MLOps Engineer |
| **AI Incident** | Alert | Production AI incident requiring investigation and remediation. Linked to DORA reporting timelines. | Critical | On-Call Engineer / Model Owner |
| **Vulnerability Finding** | Bug | AI-specific vulnerability discovered during testing or advisory. | High | Security Engineer |
| **Compliance Evidence** | Document | Collection or production of specific compliance evidence for a regulatory requirement. | Medium | Varies by evidence type |

### 1.2 Custom Fields

| Field Name | Field Type | Applies To | Purpose |
|-----------|-----------|-----------|---------|
| **AI System ID** | Single Select (populated from AI registry) | All governance types | Links ticket to specific AI system |
| **Risk Tier** | Single Select (High/Medium/Low) | All governance types | EU AI Act risk classification |
| **SAFEST Reference** | Multi-Select | All governance types | Links to specific SAFEST items being addressed |
| **Regulatory Reference** | Text (multi-line) | All governance types | Specific regulation article (e.g., "EU AI Act Art. 9(2)") |
| **Evidence Link** | URL | All governance types | Link to evidence artifact (Confluence, SharePoint, Git) |
| **Governance Stage** | Single Select (Discovery/Development/Runtime/Operational) | Governance Gate | Which lifecycle stage this gate belongs to |
| **Gate Type** | Single Select (Discovery Gate/Development Gate/Deployment Gate/Retirement Gate) | Governance Gate | Specific gate being evaluated |
| **Drift Type** | Single Select (Data/Concept/Prompt/Tool-Use) | Drift Investigation | Type of drift detected |
| **Drift Severity** | Single Select (P1/P2/P3/P4) | Drift Investigation | Alert severity from monitoring |
| **Incident Severity** | Single Select (Sev1/Sev2/Sev3/Sev4) | AI Incident | Incident severity classification |
| **DORA Reporting Required** | Checkbox | AI Incident | Whether DORA Art. 19 reporting is triggered |
| **DORA Deadline** | Date | AI Incident | Regulatory reporting deadline |
| **Approval Decision** | Single Select (Approved/Rejected/Conditional) | Governance Gate, Model Validation | Formal approval outcome |
| **Approval Condition** | Text (multi-line) | Governance Gate | Conditions for conditional approval |
| **Approver** | User Picker | Governance Gate, Model Validation | Person who approved/rejected |

---

## 2. Workflow Definitions

### 2.1 AI Ethics Review Workflow

```
[Open] --> [In Assessment] --> [Under Review] --> [Approved / Rejected / Conditional]
  |                                                      |
  |                                                      +--> [Conditions Met] --> [Closed]
  |
  +--> [Not Applicable] --> [Closed]
```

| Status | Who Acts | Actions Required | Transition Conditions |
|--------|---------|-----------------|----------------------|
| **Open** | Ethics Lead | Assign assessor; link to AI system | Assignee set |
| **In Assessment** | Ethics Assessor | Complete [AI Ethics Impact Assessment](../../01-discovery-governance/templates/ai-ethics-impact-assessment.md) | Assessment document attached |
| **Under Review** | Ethics Lead + Compliance Officer | Review assessment; conduct stakeholder consultation if needed | Two reviewers have provided input |
| **Approved** | Ethics Lead | Document approval rationale; link evidence | Approval Decision = Approved |
| **Rejected** | Ethics Lead | Document rejection rationale; specify required changes | Approval Decision = Rejected |
| **Conditional** | Ethics Lead | Document conditions; set follow-up date | Approval Decision = Conditional |
| **Conditions Met** | Model Owner | Provide evidence that conditions are satisfied | All conditions verified |
| **Not Applicable** | Ethics Lead | Document why ethics review is not applicable (low-risk only) | Risk Tier = Low AND justification provided |
| **Closed** | System (automatic) | Archive for audit trail | Final state reached |

### 2.2 Bias Assessment Workflow

```
[Open] --> [Data Collection] --> [Analysis] --> [Report Drafted] --> [Under Review] --> [Accepted / Remediation Required]
                                                                                              |
                                                                                              +--> [Remediation In Progress] --> [Re-Assessment] --> [Accepted]
```

| Status | Who Acts | Actions Required |
|--------|---------|-----------------|
| **Open** | ML Engineer | Assign assessor; define assessment scope (which model, which segments) |
| **Data Collection** | Data Engineer | Gather production data by protected group; prepare evaluation dataset |
| **Analysis** | ML Engineer | Run bias evaluation suite per [Bias and Fairness Evals](../../02-development-governance/evaluations/bias-and-fairness-evals.md) |
| **Report Drafted** | ML Engineer | Complete [Bias Assessment Report](../../02-development-governance/templates/bias-assessment-report.md) |
| **Under Review** | Compliance Officer + Ethics Lead | Review bias findings against regulatory thresholds |
| **Accepted** | Compliance Officer | No material bias detected; document results |
| **Remediation Required** | Model Owner | Material bias detected; mitigation plan required within 10 business days |
| **Remediation In Progress** | ML Engineer | Implement bias mitigation (retraining, re-weighting, threshold adjustment) |
| **Re-Assessment** | Independent Reviewer | Verify bias is remediated; run evaluation suite again |

### 2.3 Governance Gate Workflow

```
[Open] --> [Evidence Collection] --> [Checklist Review] --> [Gate Review Meeting] --> [Approved / Rejected / Conditional]
                                                                                           |
                                                                                           +--> [Conditional] --> [Conditions Addressed] --> [Re-Review] --> [Approved]
```

| Status | Who Acts | Actions Required |
|--------|---------|-----------------|
| **Open** | Model Owner | Create gate ticket; link all prerequisite tickets (ethics review, bias assessment, validation) |
| **Evidence Collection** | Model Owner + Team | Attach all evidence artifacts; complete relevant YAML checklist |
| **Checklist Review** | AI Governance PM | Verify YAML checklist completeness; verify all prerequisite tickets are in Approved/Accepted status |
| **Gate Review Meeting** | Gate Approvers (per RACI) | Formal review meeting; approve, reject, or conditionally approve |
| **Approved** | Gate Approver | Record approval decision, approver name, date; unblock deployment |
| **Rejected** | Gate Approver | Record rejection rationale; specify what must be remediated |
| **Conditional** | Gate Approver | Record conditions; set deadline for condition satisfaction |
| **Conditions Addressed** | Model Owner | Provide evidence that conditions are met |
| **Re-Review** | Gate Approver | Verify conditions met; approve or re-reject |

### 2.4 AI Incident Workflow

```
[Detected] --> [Acknowledged] --> [Investigating] --> [Mitigated] --> [Root Cause Analysis] --> [Corrective Actions] --> [Closed]
     |                                                      |
     |                                                      +--> [Escalated] --> [Investigating]
     |
     +--> [DORA Reporting] (parallel track for major incidents)
```

| Status | Who Acts | SLA |
|--------|---------|-----|
| **Detected** | Monitoring System (auto-created) | N/A |
| **Acknowledged** | On-Call Engineer | 5 min (P1), 30 min (P2), 4 hours (P3) |
| **Investigating** | On-Call Engineer + Model Owner | Ongoing |
| **Mitigated** | On-Call Engineer | MTTR target per severity |
| **Escalated** | Engineering Manager / CAIO | When resolution exceeds SLA |
| **Root Cause Analysis** | Model Owner | Within 5 business days |
| **Corrective Actions** | Model Owner + ML Engineer | Within 10 business days |
| **DORA Reporting** | Compliance Officer | 4h initial / 72h intermediate / 1 month final |
| **Closed** | Model Owner | After corrective actions verified |

---

## 3. JQL Queries for Dashboards

### 3.1 CAIO Dashboard Queries

```jql
-- All open governance gates across all AI systems
project = "AI Governance" AND issuetype = "Governance Gate" AND status != Closed ORDER BY priority DESC, created ASC

-- Overdue governance gates (open longer than 10 business days)
project = "AI Governance" AND issuetype = "Governance Gate" AND status NOT IN (Approved, Closed) AND created <= -10d ORDER BY created ASC

-- Active AI incidents by severity
project = "AI Governance" AND issuetype = "AI Incident" AND status NOT IN (Closed) ORDER BY "Incident Severity" ASC

-- DORA-reportable incidents with deadlines
project = "AI Governance" AND issuetype = "AI Incident" AND "DORA Reporting Required" = Yes AND status != Closed ORDER BY "DORA Deadline" ASC

-- Ethics reviews pending decision
project = "AI Governance" AND issuetype = "AI Ethics Review" AND status IN ("Under Review") ORDER BY priority DESC

-- Monthly governance throughput (completed gates this month)
project = "AI Governance" AND issuetype = "Governance Gate" AND status = Approved AND resolved >= startOfMonth() ORDER BY resolved DESC
```

### 3.2 Model Owner Dashboard Queries

```jql
-- My AI system's open governance items
project = "AI Governance" AND "AI System ID" = "{system_id}" AND status != Closed ORDER BY priority DESC

-- My pending bias assessments
project = "AI Governance" AND issuetype = "Bias Assessment" AND "AI System ID" = "{system_id}" AND status NOT IN (Accepted, Closed) ORDER BY created ASC

-- My drift investigations
project = "AI Governance" AND issuetype = "Drift Investigation" AND "AI System ID" = "{system_id}" AND status != Closed ORDER BY "Drift Severity" ASC

-- My upcoming revalidation deadlines
project = "AI Governance" AND issuetype = "Model Validation" AND "AI System ID" = "{system_id}" AND status = Open AND duedate <= 30d ORDER BY duedate ASC
```

### 3.3 Compliance Officer Dashboard Queries

```jql
-- All open regulatory evidence items
project = "AI Governance" AND issuetype = "Compliance Evidence" AND status != Closed ORDER BY duedate ASC

-- Vulnerability findings requiring regulatory notification
project = "AI Governance" AND issuetype = "Vulnerability Finding" AND status NOT IN (Closed, "Risk Accepted") AND priority IN (Critical, High) ORDER BY priority DESC

-- All high-risk AI system governance status
project = "AI Governance" AND "Risk Tier" = High AND status != Closed ORDER BY issuetype ASC, priority DESC

-- SAFEST compliance items not yet completed
project = "AI Governance" AND issuetype = "Compliance Evidence" AND "SAFEST Reference" IS NOT EMPTY AND status NOT IN (Closed, Completed) ORDER BY "SAFEST Reference" ASC
```

---

## 4. YAML Checklist Integration

### 4.1 Integration Strategy

The YAML checklists in this governance framework (e.g., `pre-deployment-gate.yaml`, `bias-testing-checklist.yaml`, `monitoring-setup-checklist.yaml`) must be connected to Jira tickets to create a single source of truth:

| Integration Approach | Description | Tooling |
|---------------------|-------------|---------|
| **Checklist Plugin** | Render YAML checklist items as Jira checklist sub-items within a governance ticket | Jira Checklist Pro plugin or similar |
| **Sub-task Generation** | Auto-generate Jira sub-tasks from YAML checklist items | Jira automation rule (see Section 5) |
| **Link to Git** | YAML file in Git repo linked to Jira ticket; status synced via CI/CD | Jira-GitHub/GitLab integration |
| **Custom Field Sync** | YAML completion percentage calculated and synced to a custom field on the parent ticket | CI/CD pipeline + Jira REST API |

### 4.2 Recommended Approach: Sub-Task Generation

For each governance gate ticket, auto-generate sub-tasks from the relevant YAML checklist:

1. When a Governance Gate ticket is created with `Gate Type = Deployment Gate`:
   - Read `02-development-governance/checklists/pre-deployment-gate.yaml`
   - For each checklist item with `priority: critical` or `priority: high`, create a Jira sub-task
   - Sub-task title: `[{item.id}] {item.item}`
   - Sub-task description includes: `regulatory_ref`, `evidence_ref` placeholder
   - Sub-task assignee: determined by RACI for that checklist item

2. When all sub-tasks are in `Done` status, the parent ticket automatically transitions to `Checklist Review`

### 4.3 Checklist-to-Issue Mapping

| YAML Checklist | Jira Issue Type | Trigger |
|---------------|----------------|---------|
| `ethical-product-discovery.yaml` | AI Ethics Review sub-tasks | Ethics Review ticket created |
| `bias-testing-checklist.yaml` | Bias Assessment sub-tasks | Bias Assessment ticket created |
| `pre-deployment-gate.yaml` | Governance Gate sub-tasks | Deployment Gate ticket created |
| `model-validation-checklist.yaml` | Model Validation sub-tasks | Model Validation ticket created |
| `monitoring-setup-checklist.yaml` | Compliance Evidence sub-tasks | Monitoring setup verification |
| `incident-response-checklist.yaml` | AI Incident sub-tasks | AI Incident ticket created |
| `security-threat-model.yaml` | Vulnerability Finding sub-tasks | Security assessment initiated |
| `guardrail-deployment-checklist.yaml` | Governance Gate sub-tasks | Runtime governance gate |

---

## 5. Automation Rules

### 5.1 Ticket Creation Automations

| Trigger | Action | Purpose |
|---------|--------|---------|
| New AI system registered in inventory | Create AI Ethics Review + Governance Gate (Discovery) tickets | Ensure every new system enters governance pipeline |
| Monitoring alert creates Drift Investigation | Auto-populate AI System ID, Drift Type, Drift Severity from alert metadata | Reduce manual data entry; ensure consistency |
| P1 incident detected | Create AI Incident ticket; set DORA Reporting Required = Yes if criteria met; calculate DORA Deadline | Ensure regulatory timelines are tracked from detection |
| Quarterly revalidation schedule triggers | Create Model Validation tickets for all systems due for revalidation | Prevent missed revalidation deadlines |

### 5.2 Workflow Automations

| Trigger | Action | Purpose |
|---------|--------|---------|
| All Governance Gate sub-tasks marked Done | Transition parent to Checklist Review | Auto-advance when evidence is complete |
| Governance Gate approved | Notify Model Owner, update deployment pipeline flag | Unblock deployment automation |
| Governance Gate rejected | Notify Model Owner; create follow-up task with rejection reasons | Ensure rejected gates produce actionable follow-ups |
| AI Incident not acknowledged within SLA | Escalate to secondary on-call; notify Engineering Manager | Enforce incident response SLAs |
| DORA Deadline approaching (48h warning) | Notify Compliance Officer and CAIO | Prevent missed regulatory deadlines |
| Bias Assessment result = Remediation Required | Create linked Remediation ticket; set 10-day SLA | Automate remediation tracking |

### 5.3 Reporting Automations

| Schedule | Action | Audience |
|----------|--------|---------|
| Weekly (Monday 09:00) | Generate governance status email: open gates, open incidents, upcoming deadlines | CAIO, AI Governance PM |
| Monthly (1st business day) | Generate governance throughput report: gates passed/failed, incidents resolved, drift events | AI Governance Committee |
| Quarterly (per [supervisory reporting calendar](../../07-enterprise-implementation/process-integration/supervisory-reporting-calendar.md)) | Generate regulatory evidence summary: SAFEST completion, EU AI Act compliance status | Compliance Officer, CAIO |

---

## 6. Dashboard Configuration

### 6.1 CAIO Governance Dashboard

| Gadget | Type | Data Source |
|--------|------|-------------|
| **Governance Pipeline** | Kanban board | All Governance Gate tickets, grouped by status |
| **AI Incident Tracker** | Filter results | Active AI Incidents sorted by severity |
| **DORA Deadline Calendar** | Calendar | AI Incidents with DORA Reporting Required = Yes |
| **Governance Gate Throughput** | Pie chart | Governance Gates resolved this quarter by decision (Approved/Rejected/Conditional) |
| **Risk Heat Map** | 2D chart | AI Systems by Risk Tier vs. open governance items count |
| **Compliance Evidence Progress** | Progress bar | Percentage of Compliance Evidence tickets completed per regulation |

### 6.2 Model Owner Dashboard

| Gadget | Type | Data Source |
|--------|------|-------------|
| **My System Status** | Filter results | All open governance items for my AI system(s) |
| **Next Gate** | Single stat | Next Governance Gate by due date |
| **Drift Alerts** | Filter results | Open Drift Investigations for my system(s) |
| **Revalidation Calendar** | Calendar | Upcoming Model Validation due dates |
| **Evidence Checklist Progress** | Checklist view | Sub-task completion for current governance gate |

---

## Cross-References

- [Governance in CI/CD](../../07-enterprise-implementation/process-integration/governance-in-cicd.md) -- integration of Jira governance gates with deployment pipelines
- [Governance in Agile Sprints](../../07-enterprise-implementation/process-integration/governance-in-agile-sprints.md) -- how governance tickets fit into sprint planning
- [Supervisory Reporting Calendar](../../07-enterprise-implementation/process-integration/supervisory-reporting-calendar.md) -- reporting schedule that drives Jira automation triggers
- [RACI by AI Lifecycle Stage](../../07-enterprise-implementation/organizational-model/raci-by-ai-lifecycle-stage.md) -- role definitions used for Jira ticket assignment
- [GRC Platform Integration](./grc-platform-integration.md) -- how Jira governance data feeds into GRC platforms
- [Automated Compliance Checks](./automated-compliance-checks.md) -- CI/CD automation that creates Jira evidence tickets
- [Pre-Deployment Gate Checklist](../../02-development-governance/checklists/pre-deployment-gate.yaml) -- primary YAML checklist integrated with Jira
- [Incident Response Checklist](../../04-operational-governance/checklists/incident-response-checklist.yaml) -- incident checklist that drives AI Incident sub-tasks
- [Model Monitoring Dashboard](../../04-operational-governance/templates/model-monitoring-dashboard.md) -- source of alerts that auto-create Jira tickets

---

*Last updated: 2026-03-01* / *Version: 1.0* / *Classification: Internal / Regulatory Preparation*
