# Three Lines of Defense for AI Governance

> **Purpose:** Detailed guide for applying the three-lines-of-defense (3LoD) model to AI governance in regulated FinTechs, mapping specific AI responsibilities to each line and connecting them to the SAFEST Accountability pillar.
>
> **Regulatory Basis:** DNB Good Practice for AI in the Financial Sector; SAFEST item A-02; Wft Section 3:17 (sound business operations); EU AI Act Articles 14, 17, 72-73.
>
> **SAFEST Reference:** A-02 (Three-lines-of-defense model for AI)

---

## Why 3LoD Matters for AI

DNB expects every licensed financial institution to operate a clear three-lines-of-defense model. For AI-intensive FinTechs, this is not a box-ticking exercise -- it is the structural backbone that determines whether your governance is real or performative.

The 3LoD model ensures:
- **Separation of duties** -- the people who build AI do not validate it, and the people who validate it do not audit it.
- **Escalation paths** -- problems detected at any level have a defined route upward.
- **Independent assurance** -- the board receives an opinion on AI governance effectiveness from a party that has no stake in the AI system's success.

Without a functioning 3LoD model, DNB will not consider your governance framework credible, regardless of how complete your checklists are.

---

## The Three Lines at a Glance

```
+=====================================================================+
|                         BOARD / MANAGEMENT                          |
|    Ultimate accountability for AI governance (A-01)                 |
|    Sets risk appetite | Approves AI strategy | Reviews reports      |
+=====================================================================+
         |                    |                    |
         v                    v                    v
+-------------------+  +-------------------+  +-------------------+
|   1ST LINE        |  |   2ND LINE        |  |   3RD LINE        |
|   OF DEFENSE      |  |   OF DEFENSE      |  |   OF DEFENSE      |
|                   |  |                   |  |                   |
|  OWNS + MANAGES   |  |  OVERSEES +       |  |  INDEPENDENTLY    |
|  THE RISK         |  |  CHALLENGES       |  |  ASSURES          |
|                   |  |                   |  |                   |
|  Product Teams    |  |  AI Risk          |  |  Internal Audit   |
|  AI Engineers     |  |  Compliance       |  |  (or outsourced   |
|  ML Engineers     |  |  Model Validation |  |   audit function)  |
|  Data Engineers   |  |  DPO              |  |                   |
|  DevOps/MLOps     |  |  Legal            |  |                   |
+-------------------+  +-------------------+  +-------------------+
   Build, Test,           Set Policy,           Independent
   Operate, Monitor       Challenge, Advise     Assessment
```

---

## First Line of Defense: Product Teams and AI Engineers

### Role

The first line **owns and manages** the AI risk. They build, test, deploy, operate, and monitor AI systems. They are closest to the technology and bear primary responsibility for ensuring each AI system meets governance requirements.

### Key Responsibilities

| Responsibility | SAFEST Items | Governance Pillar |
|---------------|-------------|-------------------|
| Maintain AI system inventory with risk classifications | S-01 | Discovery |
| Document algorithm selection rationale and trade-offs | S-02 | Discovery |
| Define and measure model performance metrics against acceptance thresholds | S-03 | Development |
| Perform edge case analysis and stress testing | S-04, S-05 | Development |
| Implement and document fallback procedures | S-13 | Runtime |
| Maintain model rollback capability | S-16 | Runtime |
| Conduct pre-deployment bias testing | F-03 | Development |
| Implement production fairness monitoring | F-11 | Runtime |
| Create and maintain model cards | T-12 | Development |
| Implement explainability methods per model | T-01 | Development |
| Log all AI-assisted decisions (audit trail) | A-11 | Runtime |
| Maintain model change log | A-12 | Operational |
| Implement data drift detection | S-12 | Runtime |
| Execute AI incident response procedures | A-15 | Runtime |
| Produce monitoring dashboards | T-17 | Runtime |

### First Line Deliverables

For each AI system, the first line must produce and maintain:

1. **Model Card** (T-12) -- standardized documentation including purpose, data, performance, limitations, fairness assessment
2. **Evaluation Results** -- pre-deployment and ongoing eval results against defined acceptance criteria (S-03)
3. **Fallback Documentation** (S-13) -- what happens when the AI fails
4. **Bias Testing Report** (F-03) -- pre-deployment and periodic fairness testing results
5. **Incident Response Runbook** (A-15) -- system-specific incident procedures
6. **Change Log** (A-12) -- complete record of all model changes with approval records

### First Line Anti-Patterns

- Building AI systems without notifying the second line until deployment is imminent
- Treating governance documentation as a post-hoc exercise done after launch
- Conflating model validation (2nd line) with model testing (1st line)
- Skipping bias testing because "we do not collect protected characteristics"

---

## Second Line of Defense: AI Risk, Compliance, and Model Validation

### Role

The second line **oversees, challenges, and advises** the first line. They set policies, define standards, independently validate models, and ensure the first line is managing risk effectively. They do NOT build or operate AI systems.

### Key Responsibilities

| Responsibility | SAFEST Items | Governance Pillar |
|---------------|-------------|-------------------|
| Define AI governance policies and standards | A-03, E-01 | Cross-cutting |
| Perform independent model validation | S-19 | Development |
| Set validation frequency and trigger criteria | S-20 | Operational |
| Review and challenge bias testing methodology | F-03, F-04 | Development |
| Conduct proxy variable analysis | F-02 | Discovery |
| Review ethical use case proposals | E-02 | Discovery |
| Maintain prohibited AI uses list | E-03 | Discovery |
| Ensure GDPR compliance (DPIAs, Art. 22 procedures) | T-10 | Cross-cutting |
| Review customer-facing AI disclosures and explanations | T-06, T-07 | Runtime |
| Ensure DORA ICT risk management alignment for AI | S-18 | Operational |
| Monitor regulatory developments and update policies | All | Operational |
| Advise first line on governance requirements per risk tier | A-04 | Cross-cutting |
| Review and approve AI incident classifications | A-15, A-16 | Runtime |
| Produce board-level AI risk reporting | K-02, A-10 | Operational |

### Second Line Deliverables

1. **AI Governance Policy** -- board-approved document defining standards, risk appetite, and requirements (A-03, E-01)
2. **Independent Validation Reports** (S-19) -- for each high-risk model, a validation report covering conceptual soundness, data integrity, discriminatory power, calibration, and stability
3. **Fairness Metrics Framework** (F-04) -- which metrics apply to which use cases, with justified thresholds
4. **AI Risk Dashboard** -- aggregated view of AI risk across all systems for management and board (K-02)
5. **Regulatory Compliance Map** -- tracking EU AI Act, DORA, GDPR, Wwft, and sector-specific requirements to internal controls
6. **FRIA Reports** (E-12) -- Fundamental Rights Impact Assessments for high-risk AI systems

### Second Line Anti-Patterns

- Rubber-stamping first line work without genuine challenge
- Performing validation using the same data and methods as the first line
- Setting policies that are theoretically sound but operationally impossible
- Acting as a gatekeeper that slows everything down without adding risk insight

---

## Third Line of Defense: Internal Audit

### Role

The third line provides **independent assurance** to the board and senior management that the first and second lines are operating effectively. Internal audit does not build, operate, or set policy for AI systems. They assess whether governance controls are designed adequately and operating as intended.

### Key Responsibilities

| Responsibility | SAFEST Items | Governance Pillar |
|---------------|-------------|-------------------|
| Assess adequacy of the AI governance framework design | A-01, A-02, A-03 | Cross-cutting |
| Test operating effectiveness of AI governance controls | A-04 | Cross-cutting |
| Verify independence of second-line model validation | S-19 | Development |
| Assess completeness and accuracy of AI system inventory | S-01 | Discovery |
| Test audit trail completeness and integrity | A-11, A-13 | Runtime |
| Assess incident response readiness through simulation | A-15 | Runtime |
| Verify board AI competency and reporting adequacy | K-01, K-02 | Operational |
| Evaluate training program effectiveness | K-09, K-11 | Operational |
| Assess third-party AI risk management | K-13, K-14, K-15 | Operational |
| Report findings directly to the board/audit committee | A-01 | Cross-cutting |

### Third Line Deliverables

1. **Annual AI Governance Audit Plan** -- risk-based plan covering key governance areas
2. **Audit Reports** -- findings, risk ratings, and recommendations for each audit
3. **Findings Tracker** -- status of open findings with remediation deadlines
4. **Board Assurance Letter** -- annual opinion on the overall effectiveness of AI governance

### Third Line Considerations for FinTechs

Many early-stage FinTechs do not have a dedicated internal audit function. DNB recognizes this but still expects independent assurance. Options:

| Approach | When Appropriate | Considerations |
|----------|-----------------|----------------|
| **Outsourced internal audit** | Pre-license or <50 employees | Must have contractual independence; cannot be the same firm providing 2nd line services |
| **Co-sourced internal audit** | 50-200 employees | Internal audit lead with external specialist support for AI-specific audits |
| **In-house internal audit** | >200 employees or DNB requires it | Full-time internal audit team with AI audit capability |

Regardless of approach, the third line must:
- Report directly to the board or audit committee (not to the CTO or CRO)
- Have unrestricted access to all AI-related documentation, code, and data
- Be free from management influence on scope, findings, or recommendations

---

## Responsibilities Matrix: 3LoD Across Governance Pillars

| Activity | 1st Line | 2nd Line | 3rd Line |
|----------|----------|----------|----------|
| **DISCOVERY GOVERNANCE** | | | |
| Propose new AI use cases | Responsible | Consulted (ethical review) | -- |
| Classify AI system risk tier | Responsible | Accountable (approves) | Audits classification |
| Conduct FRIA for high-risk AI | Supports | Responsible | Audits completeness |
| | | | |
| **DEVELOPMENT GOVERNANCE** | | | |
| Build and test AI models | Responsible | -- | -- |
| Define acceptance criteria | Responsible | Approves thresholds | -- |
| Conduct pre-deployment bias testing | Responsible | Reviews methodology | Audits execution |
| Perform independent model validation | -- | Responsible | Audits independence |
| Create model cards | Responsible | Reviews completeness | Audits accuracy |
| | | | |
| **RUNTIME GOVERNANCE** | | | |
| Monitor model performance in production | Responsible | Monitors dashboards | -- |
| Detect and respond to data drift | Responsible | Sets thresholds, escalates | -- |
| Handle AI incidents | Responsible (execute) | Responsible (classify, report) | Reviews post-incident |
| Maintain fallback procedures | Responsible | Reviews adequacy | Tests through simulation |
| Log AI decisions (audit trail) | Responsible | Reviews completeness | Audits integrity |
| | | | |
| **OPERATIONAL GOVERNANCE** | | | |
| Produce board AI reports | Supports (data) | Responsible (report) | Audits accuracy |
| Maintain regulatory compliance | Supports (implementation) | Responsible (mapping) | Audits coverage |
| Manage third-party AI risk | Responsible (due diligence) | Responsible (oversight) | Audits framework |
| Conduct AI training programs | Supports (technical content) | Responsible (program design) | Audits effectiveness |
| Maintain AI system retirement process | Responsible (execute) | Approves | Audits completeness |

---

## Interaction Model: How Lines Communicate and Escalate

### Regular Communication Channels

| Channel | Frequency | Participants | Purpose |
|---------|-----------|-------------|---------|
| AI Governance Committee | Monthly | 1st line leads, 2nd line leads, 3rd line observer | Review AI risk, approve deployments, escalate issues |
| Model Validation Review | Per model deployment + quarterly | 1st line model owner, 2nd line validator | Challenge model performance and methodology |
| AI Risk Dashboard Review | Weekly | 2nd line risk, 1st line on-call | Review production monitoring alerts |
| Audit Planning Session | Annually + quarterly updates | 3rd line, 2nd line | Agree audit scope and timing |
| Board AI Reporting | Quarterly | 2nd line, 3rd line | Present AI governance status and audit findings |

### Escalation Triggers and Paths

```
Severity 1 (Critical):                  Severity 2 (High):
AI system causing customer harm          Model performance below threshold
or regulatory breach                     Bias detected in production

1st Line detects                         1st Line detects
    |                                        |
    v                                        v
Immediate: Activate kill switch (A-09)   1st Line investigates (24h)
    |                                        |
    v                                        v
1st Line notifies 2nd Line (<1 hour)     1st Line notifies 2nd Line (<24h)
    |                                        |
    v                                        v
2nd Line classifies incident (A-15)      2nd Line reviews and challenges
    |                                        |
    v                                        v
2nd Line notifies board member (A-01)    AI Governance Committee (next meeting)
    |                                        |
    v                                        v
DORA reporting if applicable (A-16)      Board informed in quarterly report
4h initial / 72h intermediate / 1m final
```

```
Severity 3 (Medium):                    Severity 4 (Low):
Drift detected, no immediate impact      Documentation gap identified

1st Line investigates and remediates     1st Line creates backlog item
    |                                        |
    v                                        v
2nd Line informed at next dashboard      Tracked in governance backlog
review                                       |
    |                                        v
    v                                    Addressed in next sprint
AI Governance Committee if pattern
emerges
```

---

## Staffing the Three Lines in a FinTech Context

### Minimum Viable Staffing (Pre-License, 10-30 Employees)

| Line | Minimum Staffing | Notes |
|------|-----------------|-------|
| 1st Line | AI/ML engineers on product team (existing) | Governance responsibilities added to existing roles |
| 2nd Line | 1 dedicated AI Risk/Compliance person + external model validation | Cannot be someone who also builds models |
| 3rd Line | Outsourced to audit firm | Must be independent from 2nd line provider |

### Growth Staffing (Post-License, 30-100 Employees)

| Line | Staffing | Notes |
|------|---------|-------|
| 1st Line | Product squads with designated governance leads per squad | Each squad has one person who owns governance deliverables |
| 2nd Line | AI Risk team (2-3 people): Head of AI Risk, Model Validator, AI Compliance Analyst | Head of AI Risk reports to CRO, not CTO |
| 3rd Line | Co-sourced: 1 internal audit coordinator + external AI audit specialist | Internal coordinator builds institutional knowledge |

### Key Principle: Independence

DNB will test independence during the licensing process. The following arrangements are NOT acceptable:

| Arrangement | Why It Fails |
|-------------|-------------|
| CTO oversees both 1st and 2nd line AI functions | No separation of duties |
| Same person builds models and validates them | Self-review threat |
| 2nd line model validator reports to the AI engineering lead | Reporting line compromises independence |
| Audit firm providing both 2nd line advisory and 3rd line audit | Independence conflict |
| Board member with AI accountability has no AI understanding | Cannot exercise meaningful oversight (K-01) |

---

## Implementation Checklist

Use this checklist to verify your 3LoD model is in place:

| # | Item | Status |
|---|------|--------|
| 1 | 1st, 2nd, and 3rd line responsibilities documented and assigned to named individuals | [ ] |
| 2 | Reporting lines ensure 2nd line independence from 1st line | [ ] |
| 3 | 3rd line reports directly to board/audit committee | [ ] |
| 4 | Escalation triggers and paths defined for all severity levels | [ ] |
| 5 | Communication channels established (governance committee, dashboard reviews) | [ ] |
| 6 | Each AI system has a named 1st line model owner (A-05) | [ ] |
| 7 | Independent model validation assigned and resourced (S-19) | [ ] |
| 8 | Audit plan includes AI governance scope | [ ] |
| 9 | Board member with AI accountability identified (A-01) | [ ] |
| 10 | RACI matrix completed for AI lifecycle (A-04) | [ ] |

---

## Cross-References

- **AI Governance Committee Charter:** [ai-governance-committee-charter.md](ai-governance-committee-charter.md) -- establishes the body where the three lines interact
- **Board-Level AI Accountability:** [board-level-ai-accountability.md](board-level-ai-accountability.md) -- details board oversight that sits above all three lines
- **Risk Tiering Model:** [../risk-based-adoption/risk-tiering-model.md](../risk-based-adoption/risk-tiering-model.md) -- determines governance intensity per line
- **Governance in Agile Sprints:** [../process-integration/governance-in-agile-sprints.md](../process-integration/governance-in-agile-sprints.md) -- how 1st line governance integrates into sprint workflows
- **SAFEST Checklist:** See the parent AIGovernance repository at `docs/06-licensing-preparation/safest-checklist-dnb-pre-application.md`

---

*Last updated: 2026-02-28*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
