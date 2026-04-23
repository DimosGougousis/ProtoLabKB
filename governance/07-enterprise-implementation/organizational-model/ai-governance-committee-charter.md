# AI Governance Committee Charter -- Template

> **Purpose:** Provide a ready-to-adopt template for establishing an AI Governance Committee in a regulated FinTech, satisfying DNB expectations for structured AI governance decision-making.
>
> **Regulatory Basis:** DNB Good Practice for AI in the Financial Sector; Wft Section 3:17 (sound business operations); EU AI Act Article 72 (post-market monitoring); SAFEST items A-01 through A-04.
>
> **Instructions:** Copy this template, replace `[COMPANY NAME]` with your legal entity name, adapt membership to your organizational structure, and obtain board approval. Items marked `[ADAPT]` require company-specific input.

---

## 1. Purpose and Mandate

### 1.1 Purpose

The AI Governance Committee ("the Committee") is the principal decision-making body for AI governance at `[COMPANY NAME]`. It ensures that all AI and machine learning systems developed, deployed, or procured by `[COMPANY NAME]` comply with applicable regulations, internal policies, and ethical standards.

### 1.2 Mandate

The Committee is authorized by the Board of Directors to:

1. **Govern** -- set policies, standards, and principles for AI development and deployment.
2. **Approve** -- authorize the deployment of new AI systems and material changes to existing systems, proportional to risk tier.
3. **Oversee** -- monitor AI system performance, risk, fairness, and compliance on an ongoing basis.
4. **Escalate** -- raise AI-related risks and incidents to the board when they exceed defined thresholds.
5. **Report** -- provide the board with quarterly reporting on AI governance status.

### 1.3 Scope

The Committee's scope covers:

- All AI/ML systems in the AI system inventory (SAFEST item S-01), including internally developed models, fine-tuned models, third-party AI APIs, and agentic AI workflows.
- All stages of the AI lifecycle: discovery, development, deployment, runtime monitoring, and retirement.
- All SAFEST pillars: Soundness, Accountability, Fairness, Ethics, Skills, and Transparency.

### 1.4 Authority Limits

| Decision | Committee Authority | Escalation Required |
|----------|-------------------|-------------------|
| Deploy minimal-risk AI system | Approve | -- |
| Deploy limited-risk AI system | Approve | -- |
| Deploy high-risk AI system | Recommend | Board approval required |
| Retire any AI system | Approve | Inform board |
| Approve AI governance policies | Approve | Board ratification for major policies |
| Approve new AI use case (ethical review) | Approve (minimal/limited risk) | Board approval for high-risk or novel use cases |
| Activate kill switch on AI system | Inform (after the fact) | 1st/2nd line authorized to act immediately (A-09) |
| Approve third-party AI vendor | Approve (standard risk) | Board approval if critical/important function under DORA |
| Set AI risk appetite parameters | Recommend | Board approval required |
| Approve AI-related budget allocation | Recommend | CFO/Board approval per financial authority matrix |

---

## 2. Membership

### 2.1 Standing Members

| Role | Name | Line of Defense | Voting |
|------|------|----------------|--------|
| **Chair:** Chief Technology Officer (CTO) or VP Engineering | `[NAME]` | 1st Line leadership | Yes |
| **Vice-Chair:** Chief Risk Officer (CRO) or Head of Risk | `[NAME]` | 2nd Line leadership | Yes |
| Chief Information Security Officer (CISO) | `[NAME]` | 2nd Line | Yes |
| Head of Compliance / MLRO | `[NAME]` | 2nd Line | Yes |
| Head of Product | `[NAME]` | 1st Line | Yes |
| Data Protection Officer (DPO) | `[NAME]` | 2nd Line (advisory) | Yes |
| Head of AI/ML Engineering | `[NAME]` | 1st Line | Yes |
| Head of Model Validation (if separate) | `[NAME]` | 2nd Line | Yes |

### 2.2 Non-Voting Attendees

| Role | Purpose |
|------|---------|
| Internal Audit representative | 3rd line observer; attends to inform audit planning, does not vote to preserve independence |
| Legal Counsel | Advises on regulatory and contractual matters |
| Committee Secretary | Records minutes, tracks actions, manages agenda |

### 2.3 Ad Hoc Invitees

The Chair may invite additional participants as needed:
- Individual model owners presenting deployment proposals
- External advisors (e.g., regulatory counsel, AI ethics consultants)
- Representatives from business units affected by AI governance decisions

### 2.4 Chair Responsibilities

The Chair:
- Sets the agenda in consultation with the Vice-Chair
- Facilitates Committee discussions and ensures all perspectives are heard
- Holds the casting vote in the event of a tie
- Ensures Committee decisions are communicated and implemented
- Presents quarterly AI governance reports to the board

`[ADAPT]` **Note on Chair selection:** Some organizations prefer the CRO as Chair to emphasize risk oversight. The choice between CTO-as-Chair and CRO-as-Chair signals the organization's governance philosophy. DNB does not prescribe either approach but will assess whether the chosen structure provides effective oversight. If the CTO chairs, the CRO must be empowered to challenge and escalate independently.

---

## 3. Meeting Cadence and Quorum

### 3.1 Regular Meetings

| Meeting Type | Frequency | Duration | Purpose |
|-------------|-----------|----------|---------|
| Full Committee Meeting | Monthly | 90 minutes | Review AI risk dashboard, approve deployments, address escalations |
| Emergency Meeting | As needed (within 24 hours of trigger) | 60 minutes | Address critical AI incidents or urgent regulatory matters |
| Annual Strategy Session | Annually (Q1) | Half day | Review AI governance strategy, update risk appetite, plan annual audit |

### 3.2 Quorum

- **Quorum for decisions:** Minimum 5 voting members present, including at least 1 first-line representative and 1 second-line representative.
- **Chair or Vice-Chair** must be present for quorum.
- **Written resolutions:** Decisions may be taken by written resolution circulated to all voting members, requiring unanimous approval of respondents with minimum 5 responses within 48 hours.

### 3.3 Decision Making

- Decisions are made by **simple majority** of voting members present.
- The Chair holds the **casting vote** in case of a tie.
- **Dissenting opinions** must be recorded in the minutes. Any member may request their dissent be escalated to the board.
- Decisions requiring board approval are recorded as **recommendations** and presented at the next board meeting (or sooner if urgency requires).

---

## 4. Standing Agenda Items

Each monthly Committee meeting follows this standard agenda:

### Standard Monthly Agenda

| # | Item | Owner | Duration | SAFEST Link |
|---|------|-------|----------|------------|
| 1 | **Approval of previous minutes and action tracker review** | Secretary | 10 min | -- |
| 2 | **AI Risk Dashboard review** -- model performance, drift alerts, fairness metrics, incident summary | CRO / Head of AI Risk | 15 min | S-03, S-12, F-11 |
| 3 | **Incident review** -- AI incidents since last meeting, root cause analyses, lessons learned | Head of Compliance | 10 min | A-15, A-16, A-18 |
| 4 | **Deployment proposals** -- new AI systems or material changes requiring Committee approval | Model Owner (presenting) | 20 min | S-01, S-02, F-03, T-12 |
| 5 | **Policy and standards updates** -- new or revised governance policies, regulatory changes | Head of Compliance / DPO | 10 min | E-01, T-06 |
| 6 | **Ethical review** -- new AI use case proposals, ethical concerns raised | DPO / Ethics representative | 10 min | E-02, E-03 |
| 7 | **Third-party AI review** -- vendor risk updates, new vendor assessments | CISO / Head of Procurement | 5 min | K-13, K-14, S-18 |
| 8 | **Training and skills update** -- training completion, competency gaps | Head of HR / Learning | 5 min | K-09, K-11 |
| 9 | **Any other business and action items** | Chair | 5 min | -- |

### Deployment Proposal Package

For agenda item 4, model owners must submit the following at least 5 business days before the meeting:

| Document | Required For | SAFEST Item |
|----------|-------------|------------|
| Model Card | All risk tiers | T-12 |
| Risk tier classification with justification | All risk tiers | S-01 |
| Pre-deployment evaluation results | All risk tiers | S-03 |
| Bias/fairness testing results | Limited and High risk | F-03 |
| Independent validation report | High risk only | S-19 |
| Fallback procedure documentation | All risk tiers | S-13 |
| DPIA (if personal data involved) | Where GDPR requires | T-10 |
| FRIA (if high-risk under EU AI Act) | High risk only | E-12 |

---

## 5. Escalation Paths

### 5.1 Escalation to the Board

The Committee must escalate to the board when:

| Trigger | Timeframe | Mechanism |
|---------|-----------|-----------|
| Critical AI incident causing customer harm or regulatory breach | Within 24 hours | Emergency board notification by Chair |
| Bias or discrimination detected in production AI system affecting customers | Within 48 hours | Written notification to board member with AI accountability |
| Material model performance degradation affecting core business processes | Within 1 week | Included in next board reporting cycle or emergency session |
| Regulatory finding or enforcement action related to AI | Immediately | Direct communication to board |
| Committee unable to reach consensus on high-risk deployment | Next board meeting | Recommendation with dissenting opinions presented |
| AI risk appetite breach | Within 48 hours | Written notification to board |

### 5.2 Escalation from the First Line

First-line teams can escalate to the Committee through:

1. **Scheduled agenda items** -- submit a topic for the next monthly meeting
2. **Ad hoc request to Chair** -- for matters requiring attention before the next meeting
3. **Emergency escalation** -- for Severity 1 incidents, follow the incident response plan (A-15) which triggers an emergency Committee meeting

### 5.3 Regulatory Escalation

| Event | Reporting Obligation | Committee Role |
|-------|---------------------|----------------|
| DORA major ICT incident involving AI | DNB notification within 4 hours (initial) | Classify, coordinate, approve notification |
| EU AI Act serious incident (from Aug 2026) | Market surveillance authority within 15 days | Review, approve notification content |
| GDPR personal data breach involving AI | AP notification within 72 hours | Review AI-specific aspects, coordinate with DPO |

---

## 6. Reporting to the Board

### 6.1 Quarterly Board Report

The Committee produces a quarterly AI governance report for the board containing:

| Section | Content | SAFEST Items |
|---------|---------|-------------|
| **Executive Summary** | Key risks, material decisions, overall governance health | -- |
| **AI System Inventory Update** | New systems, retired systems, changes in risk classification | S-01 |
| **Performance and Risk** | Aggregated model performance against thresholds, drift trends | S-03, S-12 |
| **Fairness and Ethics** | Bias monitoring results, ethical concerns raised and resolved | F-11, E-02 |
| **Incidents** | AI incidents since last report, root causes, remediation status | A-15, A-18 |
| **Compliance** | Regulatory developments, compliance status, open findings | All |
| **Skills and Training** | Training completion rates, competency gaps, succession risks | K-09, K-11, K-08 |
| **Third-Party AI** | Vendor risk status, new vendor onboarding, concentration risk | K-13, S-18 |
| **Recommendations** | Items requiring board decision or awareness | -- |

### 6.2 Annual Governance Effectiveness Report

Once per year, the Committee produces a self-assessment of governance effectiveness:
- Governance maturity against target state
- Progress on audit findings
- Regulatory readiness assessment
- Governance improvement plan for the next year

---

## 7. Committee Effectiveness

### 7.1 Annual Self-Assessment

The Committee conducts an annual self-assessment covering:

- Are all required roles represented?
- Is attendance consistent (>80% for all standing members)?
- Are decisions made in a timely manner?
- Is the escalation process working?
- Are board reports providing useful information?
- Is the Committee adding value or creating unnecessary bureaucracy?

### 7.2 Continuous Improvement

The Committee maintains a governance improvement backlog and reviews it quarterly. Improvement items may come from:
- Committee self-assessment
- Internal audit findings
- Regulatory feedback
- Incident post-mortems
- Team feedback

---

## 8. Record Keeping

| Record | Retention Period | SAFEST Item |
|--------|-----------------|------------|
| Committee minutes | Minimum 5 years (Wwft) or 10 years (EU AI Act) | A-13 |
| Deployment approval records | Life of the AI system + 5 years | A-11 |
| Escalation records | 5 years | A-10 |
| Board reports | 10 years | K-02 |
| Policy versions | All versions retained indefinitely | E-01 |

---

## 9. Charter Review

This charter is reviewed and approved by the Board of Directors annually, or sooner if material changes are required. The next review is scheduled for `[DATE]`.

| Version | Date | Approved By | Changes |
|---------|------|------------|---------|
| 1.0 | `[DATE]` | Board of Directors | Initial charter |

---

## Cross-References

- **Three Lines of Defense:** [three-lines-of-defense-for-ai.md](three-lines-of-defense-for-ai.md) -- defines the roles that populate this Committee
- **Board-Level AI Accountability:** [board-level-ai-accountability.md](board-level-ai-accountability.md) -- details the board oversight that this Committee reports into
- **Risk Tiering Model:** [../risk-based-adoption/risk-tiering-model.md](../risk-based-adoption/risk-tiering-model.md) -- determines which deployments require Committee vs. board approval
- **Governance in Agile Sprints:** [../process-integration/governance-in-agile-sprints.md](../process-integration/governance-in-agile-sprints.md) -- how sprint-level governance feeds into Committee reporting
- **SAFEST Checklist:** See the parent AIGovernance repository at `docs/06-licensing-preparation/safest-checklist-dnb-pre-application.md`

---

*Last updated: 2026-02-28*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
