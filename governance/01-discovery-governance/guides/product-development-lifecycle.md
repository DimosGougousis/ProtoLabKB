# AI Product Development Lifecycle with Governance Gates

## Purpose

This guide defines the end-to-end lifecycle for AI products within the Master AI Governance Framework. It maps governance gates, role responsibilities, and regulatory framework alignment (ISO/IEC 42001) to each lifecycle phase. The goal is to embed governance into the natural flow of product development so that compliance is achieved through process, not retroactive audits.

This is the master reference for understanding when governance activities happen, who is responsible, and what must be true before an AI product advances from one phase to the next.

## When to Use

- When initiating a new AI product or feature -- use this guide to understand the full journey and plan governance activities accordingly
- When an AI product is transitioning between phases -- use the governance gate criteria to confirm readiness
- When onboarding new team members -- use this guide to explain how governance integrates with product development
- When audit or regulatory review requires evidence of a structured lifecycle -- point to this guide and its associated artifacts

**Trigger:** Any AI product initiative at any lifecycle stage.

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **Product Manager** | **Accountable** -- owns lifecycle progression, ensures governance gates are met before advancing |
| **AI/ML Engineer** | **Responsible** -- delivers technical artifacts required at each gate, implements eval suites |
| **Data Scientist** | **Responsible** -- contributes to data governance, model development, and evaluation activities |
| **Compliance Officer (2nd Line)** | **Consulted** -- validates regulatory alignment at each gate, reviews documentation |
| **Risk Manager** | **Consulted** -- assesses risk profile at each gate transition, validates risk mitigations |
| **AI Governance Committee** | **Approver** -- grants gate approval for Limited and High-risk systems |
| **Ethics Lead** | **Consulted** -- reviews ethical implications at Discovery and pre-deployment gates |

## Regulatory Basis

- **EU AI Act Articles 9, 17** -- Risk management system and quality management system spanning the full lifecycle
- **ISO/IEC 42001:2023** -- AI Management System (AIMS) Plan-Do-Check-Act cycle
- **DORA Articles 5-11** -- ICT risk management framework for financial entities
- **DNB Good Practice for AI** -- Expectation of governance throughout AI system lifecycle

---

## Lifecycle Overview

```
  +----------+     +-----------+     +------------+     +-------------+
  |          |     |           |     |            |     |             |
  | IDEATION +---->+ DISCOVERY +---->+ DEFINITION +---->+ DEVELOPMENT |
  |          |     |           |     |            |     |             |
  +----------+     +-----------+     +------------+     +------+------+
       |               |                  |                     |
   Gate 0          Gate 1             Gate 2                Gate 3
  Screening     Discovery Gate    Definition Gate       Development Gate
                                                             |
  +----------+     +-----------+     +------------+     +----v--------+
  |          |     |           |     |            |     |             |
  |RETIREMENT|<----+ MONITORING|<----+ DEPLOYMENT |<----+   TESTING   |
  |          |     |           |     |            |     |             |
  +----------+     +-----------+     +------------+     +-------------+
       |               |                  |                     |
   Gate 7          Gate 6             Gate 5                Gate 4
  Retirement     Monitoring Gate    Deployment Gate     Pre-Deployment
  Gate                                                      Gate
```

---

## Phase 1: Ideation

### Description

The earliest stage where an AI opportunity is identified. This may originate from customer feedback, market analysis, operational pain points, or technology scouting. The output is a brief concept description, not a full product brief.

### Key Activities

1. Capture the opportunity hypothesis in one paragraph
2. Conduct initial screening: is AI the right approach, or would a simpler solution suffice?
3. Perform preliminary risk assessment: could this use case fall into a prohibited or high-risk category?
4. Identify the product owner and potential stakeholders

### Governance Activities

| Activity | Owner | Artifact |
|----------|-------|----------|
| Initial AI vs. non-AI assessment | Product Manager | Informal memo or backlog item |
| Preliminary risk screening | Product Manager | Completed using the decision tree in this guide (see Section: Governance Intensity Decision Tree) |
| Prohibited use case check | Compliance Officer | Quick review against EU AI Act Art. 5 categories |

### ISO/IEC 42001 Alignment

**Plan** -- Identify the AI opportunity and initial risk context.

### Gate 0: Screening Gate

| Criterion | Evidence | Fast-Track Eligible? |
|-----------|----------|---------------------|
| Opportunity is not in a prohibited AI category (EU AI Act Art. 5) | Compliance officer sign-off or self-certification for minimal-risk | Yes -- self-certification |
| AI approach is justified over non-AI alternatives | Brief rationale documented | Yes |
| Product owner assigned | Named individual | Yes |
| Preliminary risk tier estimated | Initial classification (may change in Discovery) | Yes |

**Approval authority:** Product Manager (all tiers at this early stage).

---

## Phase 2: Discovery

### Description

Deep exploration of the problem, users, data landscape, and technical feasibility. This is where the [Responsible Product Brief](../templates/responsible-product-brief.md) is authored. The output is a comprehensive, governance-enriched product brief ready for the Discovery Gate.

### Key Activities

1. Author the [Responsible Product Brief](../templates/responsible-product-brief.md) with all governance sections
2. Complete the [EU AI Act Risk Classification Checklist](../checklists/eu-ai-act-risk-classification.yaml)
3. Conduct stakeholder analysis and ethical impact assessment
4. Define acceptance criteria using the [Defining Acceptance Criteria](../evaluations/defining-acceptance-criteria.md) guide
5. Draft the evaluation strategy using the [Evaluation Strategy Template](../evaluations/evaluation-strategy-template.yaml)
6. Assess data availability, quality, and governance requirements
7. Determine human oversight model (HITL/HOTL/HOTA)

### Role Responsibilities (RACI)

| Activity | PM | Eng | DS | Compliance | Risk | Ethics |
|----------|----|----|-----|-----------|------|--------|
| Responsible Product Brief | A | C | C | C | C | C |
| Risk classification | R | C | C | A | C | I |
| Ethical impact assessment | R | I | C | C | C | A |
| Acceptance criteria | A | R | R | C | I | I |
| Evaluation strategy | A | R | R | C | I | I |
| Data governance assessment | C | C | R | A | C | I |

> A=Accountable, R=Responsible, C=Consulted, I=Informed

### ISO/IEC 42001 Alignment

**Plan** -- Determine requirements, risks, objectives, and planning for the AI system.

### Gate 1: Discovery Gate

> *Full gate criteria are defined in the [Discovery Governance README](../README.md#the-discovery-gate).*

| Criterion | Evidence Required | Minimal Risk | Limited Risk | High Risk |
|-----------|-------------------|-------------|-------------|-----------|
| Risk classification completed | Completed [checklist](../checklists/eu-ai-act-risk-classification.yaml) | Required | Required | Required |
| Not in prohibited category | Classification confirms no Art. 5 violation | Required | Required | Required |
| Responsible Product Brief complete | All sections of [template](../templates/responsible-product-brief.md) filled | Summary OK | Full | Full |
| Acceptance criteria defined | [Acceptance criteria](../evaluations/defining-acceptance-criteria.md) with thresholds | Required | Required | Required |
| Evaluation strategy documented | Completed [strategy template](../evaluations/evaluation-strategy-template.yaml) | Required | Required | Required |
| Ethical impact assessment | Section 5 of Product Brief | Optional | Required | Required |
| Stakeholder value map | Section 2.3 of Product Brief | Optional | Required | Required |
| DPIA initiated | DPIA document started | If personal data | If personal data | Required |
| Governance Committee approval | Meeting minutes with decision | Not required | Required | Required |

**Approval authority:**
- Minimal: Product Manager + Team Lead
- Limited: AI Governance Committee
- High: AI Governance Committee + Board-level sponsor

---

## Phase 3: Definition

### Description

Translate the approved product brief into detailed technical specifications, architecture decisions, and sprint plans. This is where governance requirements become engineering requirements: eval suites are specified, guardrail configurations are drafted, and monitoring requirements are defined.

### Key Activities

1. Translate acceptance criteria into testable eval cases
2. Design system architecture with governance controls embedded
3. Specify data pipeline requirements including lineage tracking
4. Define guardrail and safety rail specifications for runtime
5. Create sprint backlog with governance tasks explicitly included
6. Estimate governance overhead and incorporate into capacity planning

### Role Responsibilities (RACI)

| Activity | PM | Eng | DS | Compliance | Risk | Ethics |
|----------|----|----|-----|-----------|------|--------|
| Technical specification | C | A | R | C | I | I |
| Eval suite specification | A | R | R | C | I | I |
| Architecture with governance | C | A | C | C | R | I |
| Sprint planning with governance | A | R | C | I | I | I |
| Guardrail specification | C | R | C | C | A | C |

### ISO/IEC 42001 Alignment

**Plan** -- Finalize requirements and controls specification.

### Gate 2: Definition Gate

| Criterion | Evidence Required | Minimal Risk | Limited Risk | High Risk |
|-----------|-------------------|-------------|-------------|-----------|
| Eval suite specified | Eval case list with pass/fail criteria | Required | Required | Required |
| Architecture includes governance controls | Architecture document with monitoring, logging, escalation points | Summary | Standard | Detailed |
| Sprint plan includes governance tasks | Backlog with governance items estimated | Required | Required | Required |
| Guardrail specifications drafted | Configuration spec for runtime safety | Optional | Required | Required |
| Data pipeline lineage tracking designed | Technical design for data provenance | Optional | Required | Required |

**Approval authority:** Product Manager + Tech Lead (all tiers).

---

## Phase 4: Development

### Description

Build the AI system using [eval-driven development](../../02-development-governance/evaluations/eval-driven-development.md). Every feature is built alongside its evaluation. Governance artifacts (model cards, data sheets, bias audit scripts) are created as development progresses, not bolted on afterward.

### Key Activities

1. Implement model training and inference pipeline
2. Build eval suite in parallel with model development -- following [eval-driven development](../../02-development-governance/evaluations/eval-driven-development.md)
3. Conduct iterative bias and fairness testing throughout development
4. Create model card and data sheet
5. Implement logging and audit trail infrastructure
6. Build human override and escalation mechanisms
7. Implement guardrails and safety rails per specification

### Role Responsibilities (RACI)

| Activity | PM | Eng | DS | Compliance | Risk | Ethics |
|----------|----|----|-----|-----------|------|--------|
| Model development | I | R | A | I | I | I |
| Eval suite implementation | C | A | R | I | I | I |
| Bias and fairness testing | C | R | R | C | C | A |
| Model card creation | C | R | A | C | I | C |
| Guardrail implementation | C | A | C | C | R | I |

### ISO/IEC 42001 Alignment

**Do** -- Implement the AI system and its controls per the plan.

### Gate 3: Development Gate

| Criterion | Evidence Required | Minimal Risk | Limited Risk | High Risk |
|-----------|-------------------|-------------|-------------|-----------|
| Eval suite implemented and passing | Eval results with all thresholds met | Required | Required | Required |
| Bias testing completed | Fairness metrics across protected groups | Optional | Required | Required |
| Model card drafted | Model card document | Optional | Required | Required |
| Logging and audit trail functional | Demonstration of decision logging | Summary | Required | Required |
| Guardrails implemented | Configuration and unit tests | Optional | Required | Required |

**Approval authority:** Tech Lead + Product Manager (Minimal); + Compliance (Limited/High).

---

## Phase 5: Testing

### Description

Comprehensive pre-deployment testing including functional testing, adversarial testing (red-teaming), integration testing of governance controls, and user acceptance testing. This is the final verification before production.

### Key Activities

1. Execute the full eval suite against production-candidate model
2. Conduct red-team testing for adversarial robustness and prompt injection (for LLM-based systems)
3. Test human escalation and override flows end-to-end
4. Validate guardrail behavior under edge cases
5. Perform integration testing of monitoring and alerting pipelines
6. Run user acceptance testing with representative user groups
7. Complete the [Pre-Deployment Gate Checklist](../../02-development-governance/checklists/pre-deployment-gate.yaml)

### Role Responsibilities (RACI)

| Activity | PM | Eng | DS | Compliance | Risk | Ethics |
|----------|----|----|-----|-----------|------|--------|
| Full eval suite execution | C | R | A | I | I | I |
| Red-team testing | I | R | R | C | A | C |
| Escalation flow testing | A | R | C | C | C | I |
| Pre-deployment gate checklist | A | R | R | A | C | C |
| User acceptance testing | A | R | C | I | I | I |

### ISO/IEC 42001 Alignment

**Check** -- Verify that the AI system meets all planned requirements and controls.

### Gate 4: Pre-Deployment Gate

> *Full gate criteria are defined in the [Pre-Deployment Gate Checklist](../../02-development-governance/checklists/pre-deployment-gate.yaml).*

| Criterion | Evidence Required | Minimal Risk | Limited Risk | High Risk |
|-----------|-------------------|-------------|-------------|-----------|
| All eval suite thresholds met | Eval results report | Required | Required | Required |
| Red-team testing completed | Red-team report with findings and remediations | Optional | Required | Required |
| Fairness thresholds met across protected groups | Bias audit report | Optional | Required | Required |
| Human escalation tested end-to-end | Test execution records | Optional | Required | Required |
| Guardrails tested under adversarial conditions | Test results for edge cases and attacks | Optional | Required | Required |
| Model card finalized | Published model card | Optional | Required | Required |
| DPIA completed (if applicable) | DPIA document signed by DPO | If personal data | If personal data | Required |
| Pre-deployment checklist signed off | Completed [checklist](../../02-development-governance/checklists/pre-deployment-gate.yaml) | Required | Required | Required |

**Approval authority:**
- Minimal: Tech Lead + Product Manager
- Limited: AI Governance Committee
- High: AI Governance Committee + CISO + DPO (if personal data)

---

## Phase 6: Deployment

### Description

Release the AI system to production. This includes staged rollout (canary or blue-green deployment), activation of monitoring and alerting, confirmation that rollback procedures work, and establishment of the production baseline for continuous evaluation.

### Key Activities

1. Execute staged rollout plan (canary deployment recommended for High-risk)
2. Activate production monitoring dashboards and alerting rules
3. Confirm rollback procedures are tested and functional
4. Establish production baseline metrics for [continuous online evaluation](../../03-runtime-governance/evaluations/continuous-online-evaluation.md)
5. Enable audit trail logging in production
6. Communicate deployment to relevant stakeholders
7. Publish user-facing transparency disclosures (for Limited and High-risk)

### ISO/IEC 42001 Alignment

**Do** -- Operate the AI system under managed conditions.

### Gate 5: Deployment Gate

| Criterion | Evidence Required | Minimal Risk | Limited Risk | High Risk |
|-----------|-------------------|-------------|-------------|-----------|
| Staged rollout plan documented | Deployment plan with rollback procedure | Optional | Required | Required |
| Monitoring and alerting active | Dashboard screenshots or monitoring system configuration | Required | Required | Required |
| Rollback tested successfully | Test execution record | Optional | Required | Required |
| Transparency disclosures published | Published notice or documentation | N/A | Required | Required |
| Incident response procedures ready | Runbook linked to [Operational Governance](../../04-operational-governance/) | Summary | Required | Required |

**Approval authority:** Tech Lead + Product Manager (all tiers). Compliance notified for Limited/High.

---

## Phase 7: Monitoring

### Description

Ongoing production operations including continuous evaluation, drift detection, incident response, periodic audits, and stakeholder reporting. This is the longest phase -- lasting from deployment until retirement.

### Key Activities

1. Monitor continuous evaluation metrics against thresholds per [continuous online evaluation](../../03-runtime-governance/evaluations/continuous-online-evaluation.md)
2. Detect and respond to data drift and model performance degradation
3. Execute incident response procedures when anomalies are detected
4. Conduct periodic bias re-audits at the cadence determined by risk tier
5. Produce compliance reports for regulators and internal governance committees
6. Gather user feedback and incorporate into product iterations
7. Reassess risk classification when scope or context changes materially

### Role Responsibilities (RACI)

| Activity | PM | Eng | DS | Compliance | Risk | Ethics |
|----------|----|----|-----|-----------|------|--------|
| Continuous evaluation monitoring | I | A | R | I | I | I |
| Drift detection and response | C | R | A | I | C | I |
| Incident response | C | R | C | C | A | I |
| Periodic bias re-audit | C | C | R | C | C | A |
| Compliance reporting | C | C | C | A | C | I |
| Risk re-classification | A | C | C | R | R | C |

### ISO/IEC 42001 Alignment

**Check + Act** -- Monitor performance, identify nonconformities, take corrective action.

### Gate 6: Monitoring Gate (Periodic)

This gate is evaluated periodically, not just once. Cadence depends on risk tier:

| Risk Tier | Full Review Cadence | Abbreviated Check Cadence |
|-----------|--------------------|-----------------------------|
| Minimal | Annually | Quarterly |
| Limited | Semi-annually | Monthly |
| High | Quarterly | Weekly |

| Criterion | Evidence Required |
|-----------|-------------------|
| All continuous evaluation metrics within thresholds | Monitoring dashboard export or report |
| No unresolved critical or high-severity incidents | Incident log review |
| Bias re-audit completed on schedule | Bias audit report |
| Risk classification still accurate | Risk review document |
| Compliance reports delivered on schedule | Report delivery records |
| Stakeholder feedback reviewed and actioned | Feedback log and product backlog items |

**Approval authority:** Product Manager + Compliance Officer.

---

## Phase 8: Retirement

### Description

Controlled decommissioning of an AI system. Retirement may be triggered by replacement with a newer system, business decision to discontinue, regulatory change making the system non-compliant, or persistent performance degradation that cannot be remediated.

### Key Activities

1. Notify all stakeholders (internal and external) of retirement timeline
2. Migrate dependent systems to alternatives or manual processes
3. Archive all governance artifacts (model cards, eval results, audit reports, incident logs)
4. Ensure data retention obligations are met for archived data
5. Deactivate monitoring and alerting (after confirming system is fully offline)
6. Conduct post-mortem / lessons learned review
7. Update the AI system inventory

### ISO/IEC 42001 Alignment

**Act** -- Take action to address end-of-life considerations and preserve organizational learning.

### Gate 7: Retirement Gate

| Criterion | Evidence Required | All Risk Tiers |
|-----------|-------------------|---------------|
| Stakeholders notified | Communication records | Required |
| Dependent systems migrated | Migration verification | Required |
| Governance artifacts archived | Archive location documented | Required |
| Data retention obligations verified | DPO sign-off | Required |
| Post-mortem completed | Lessons learned document | Required (High), Optional (others) |
| AI system inventory updated | Updated registry | Required |

**Approval authority:** Product Manager + Compliance Officer.

---

## Governance Intensity Decision Tree

Use this decision tree at the Ideation phase (Gate 0) to determine the governance intensity that will apply throughout the lifecycle. The determination may be refined at the Discovery phase (Gate 1) after full risk classification.

```
START: Is this system an AI system as defined by EU AI Act Article 3(1)?
  |
  +-- NO --> Standard product governance (outside this framework's scope)
  |
  +-- YES --> Does it fall into a prohibited category (Art. 5)?
       |
       +-- YES --> STOP. Do not proceed. Escalate to Compliance.
       |
       +-- NO --> Is it listed in Annex III (high-risk categories)?
            |
            +-- YES --> Is it a safety component of a regulated product?
            |    |
            |    +-- YES --> HIGH-RISK: Full governance at every gate.
            |    |
            |    +-- NO --> Does it make decisions about natural persons
            |         |     in areas listed in Annex III (credit, employment,
            |         |     law enforcement, migration, etc.)?
            |         |
            |         +-- YES --> HIGH-RISK: Full governance at every gate.
            |         |
            |         +-- NO --> LIMITED or MINIMAL. Proceed to full
            |                    classification at Discovery Gate.
            |
            +-- NO --> Does it interact with natural persons?
                 |     (chatbot, emotion recognition, biometric
                 |      categorization, deep fake generation)
                 |
                 +-- YES --> LIMITED: Standard governance with
                 |           transparency obligations.
                 |
                 +-- NO --> MINIMAL: Streamlined governance.
                            Fast-track gates permitted.
```

### Fast-Track Path (Minimal Risk)

For AI systems classified as Minimal-risk, the following fast-track rules apply:

| Gate | Fast-Track Allowance |
|------|---------------------|
| Gate 0 (Screening) | Self-certification by Product Manager |
| Gate 1 (Discovery) | Abbreviated product brief; PM + Tech Lead approval (no committee) |
| Gate 2 (Definition) | Standard process (no fast-track) |
| Gate 3 (Development) | Core eval suite only; no mandatory bias audit |
| Gate 4 (Pre-Deployment) | Abbreviated checklist; no red-team requirement |
| Gate 5 (Deployment) | Standard deployment; monitoring required but alerting scope reduced |
| Gate 6 (Monitoring) | Annual full review; quarterly abbreviated check |
| Gate 7 (Retirement) | Standard process (no fast-track) |

### Full Governance Path (High Risk)

For AI systems classified as High-risk, all gates must be passed in full. No fast-track allowances. Additional requirements include:

- AI Governance Committee approval at Gates 1, 4, and 6
- Board-level sponsor at Gate 1
- CISO and DPO involvement at Gate 4
- Quarterly full monitoring reviews (Gate 6)
- Mandatory post-mortem at Gate 7

---

## ISO/IEC 42001 AIMS PDCA Mapping Summary

| PDCA Phase | Lifecycle Phases | Key Activities |
|------------|-----------------|----------------|
| **Plan** | Ideation, Discovery, Definition | Establish AI policy, assess risks, determine requirements, plan controls |
| **Do** | Development, Deployment | Implement the AI system and its management controls |
| **Check** | Testing, Monitoring | Verify system meets requirements, monitor performance, audit compliance |
| **Act** | Monitoring, Retirement | Correct nonconformities, improve processes, apply lessons learned, decommission |

---

## Cross-References to Framework Artifacts

| Lifecycle Phase | Key Artifacts | Location |
|----------------|---------------|----------|
| Ideation | Governance intensity decision tree | This document (above) |
| Discovery | Responsible Product Brief template | [templates/responsible-product-brief.md](../templates/responsible-product-brief.md) |
| Discovery | EU AI Act Risk Classification | [checklists/eu-ai-act-risk-classification.yaml](../checklists/eu-ai-act-risk-classification.yaml) |
| Discovery | Acceptance Criteria Guide | [evaluations/defining-acceptance-criteria.md](../evaluations/defining-acceptance-criteria.md) |
| Discovery | Evaluation Strategy Template | [evaluations/evaluation-strategy-template.yaml](../evaluations/evaluation-strategy-template.yaml) |
| Discovery | PRD Governance Add-on | [governance-extensions/prd-governance-addon.md](../governance-extensions/prd-governance-addon.md) |
| Discovery | MVP Governance Add-on | [governance-extensions/mvp-governance-addon.md](../governance-extensions/mvp-governance-addon.md) |
| Development | Eval-Driven Development | [eval-driven-development.md](../../02-development-governance/evaluations/eval-driven-development.md) |
| Development | Eval Gate Integration | [eval-gate-integration.md](../../02-development-governance/evaluations/eval-gate-integration.md) |
| Testing | Pre-Deployment Gate Checklist | [pre-deployment-gate.yaml](../../02-development-governance/checklists/pre-deployment-gate.yaml) |
| Monitoring | Continuous Online Evaluation | [continuous-online-evaluation.md](../../03-runtime-governance/evaluations/continuous-online-evaluation.md) |
| All phases | AI Quality Metrics Catalog | [ai-quality-metrics-catalog.md](../evaluations/ai-quality-metrics-catalog.md) |
| All phases | Governance in Agile Sprints | [governance-in-agile-sprints.md](../../07-enterprise-implementation/process-integration/governance-in-agile-sprints.md) |
| All phases | SAFEST Compliance Tracker | [safest-compliance-tracker.yaml](../../04-operational-governance/regulatory/safest-compliance-tracker.yaml) |

---

*Last updated: 2026-02-28*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
*Framework: [Product Governance for Agentic AI Workflows](../../README.md)*
