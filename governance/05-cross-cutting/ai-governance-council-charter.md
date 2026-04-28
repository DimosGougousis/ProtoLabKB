# AI Governance Council Charter

> **Document Type:** Governance Body Charter
> **Version:** 1.0
> **Effective Date:** 2026-04-28
> **Owner:** Chief AI Officer (CAIO)
> **Approved By:** Board of Directors
> **Review Cycle:** Annual
> **Next Review:** 2027-04-28

---

## Purpose

This charter establishes the AI Governance Council as the authoritative body for enterprise AI risk decisions at ProtoLabs. The Council ensures that AI systems are designed, deployed, and operated in compliance with the [AI Governance Policy](ai-governance-policy.md), applicable regulations (EU AI Act, GDPR, ITAR/EAR, NIST AI RMF, ISO/IEC 42001), and ProtoLabs' risk appetite.

## When to Use

- When a new AI system requires governance review or deployment approval
- When an existing AI system changes risk tier, vendor, or autonomy level
- When a Sev1 or Sev2 AI incident occurs
- When regulatory changes require governance framework updates
- When quarterly governance reporting is due

## Who Is Responsible

The Council is collectively responsible for AI governance decisions. Individual members have specific accountabilities defined in Section 3.

## Regulatory Basis

- **EU AI Act Article 26(2)** — Providers of high-risk AI systems shall ensure human oversight by natural persons with appropriate competence
- **ISO/IEC 42001 Clause 5.1** — Leadership and commitment to the AI Management System
- **ISO/IEC 42001 Clause 5.3** — Organizational roles, responsibilities, and authorities
- **ISO/IEC 42001 Clause 9.3** — Management review
- **NIST AI RMF GV-1.2** — Accountability structures defined, with roles and responsibilities documented
- **NIST AI RMF GV-2.1** — Risk-aware culture established within the AI development team

---

## 1. Council Composition

### 1.1 Standing Members

| Role | Responsibility | Voting | Required for Quorum |
|------|---------------|--------|---------------------|
| **CAIO** (Chair) | Sets agenda, breaks ties, owns final decision on policy interpretation | Yes | Yes |
| **Head of Engineering** | Represents technical feasibility, infrastructure constraints, and implementation risk | Yes | Yes |
| **Data Protection Officer (DPO)** | Represents GDPR, data privacy, and customer data handling compliance | Yes | Yes |
| **Legal Counsel** | Represents regulatory compliance, contractual obligations, and liability | Yes | Yes |
| **Head of Internal Audit** | Represents audit readiness, evidence quality, and control effectiveness | Yes | Yes |
| **Security Lead** | Represents cybersecurity, adversarial resilience, and infrastructure security | Yes | Yes |
| **VP Product** | Represents business objectives, customer impact, and product strategy | Yes | Yes |

### 1.2 Advisory (Non-Voting) Attendees

| Role | When Invited |
|------|-------------|
| **Safety Officer** | Tier 2/3 reviews, incident reviews, kill-switch design reviews |
| **Professional Engineer (PE)** | Any agent producing structural design outputs |
| **Domain Specialist** | Process-specific reviews (e.g., CNC engineer for machining agents) |
| **External Auditor** | ISO 42001 preparation, regulatory examination |
| **Client Representative** | Upon request for client-facing agent reviews |

### 1.3 Succession and Delegation

- Each standing member must designate a **named delegate** who can attend and vote in their absence.
- Delegation must be documented in writing to the CAIO before the meeting.
- The Chair may designate a Vice-Chair to preside in their absence; the Vice-Chair has tie-breaking authority.

---

## 2. Meeting Cadence and Quorum

### 2.1 Regular Meetings

| Meeting Type | Cadence | Duration | Agenda Source |
|-------------|---------|----------|---------------|
| **Monthly Governance Review** | First Tuesday of each month | 90 minutes | Standing agenda (Section 5) + deployment queue |
| **Quarterly Board Report Prep** | Last week of each quarter | 120 minutes | [Quarterly Governance Report](../06-executive/quarterly-governance-report.md) review |
| **Annual Policy Review** | April (aligned with policy anniversary) | Half-day | Full policy review, charter review, maturity assessment |

### 2.2 Emergency Meetings

- **Trigger:** Sev1 incident, regulatory enforcement action, or Board directive.
- **Convening:** Any standing member may request; CAIO must convene within **24 hours**.
- **Quorum:** Minimum **3 members** (reduced from standard quorum for urgency).
- **Decisions:** Binding; ratified at next regular meeting.

### 2.3 Quorum Rules

- **Standard quorum:** 5 of 7 standing members must be present (in person or video).
- **Proxy votes** are not permitted. A member must be present to vote.
- **Decisions without quorum:** Advisory only; must be ratified at next quorate meeting.

---

## 3. Authority and Decision Rights

### 3.1 What the Council Can Approve

| Decision | Authority Level |
|----------|----------------|
| Tier 1 agent deployment | **Approve** (or delegate to Technical Owner per approval thresholds) |
| Tier 2 agent deployment | **Approve** |
| Tier 3 agent deployment | **Recommend to Board** (Board has final approval) |
| Risk tier classification disputes | **Final decision** |
| Governance policy amendments | **Approve** (majority vote) |
| Vendor AI integration (customer data) | **Approve** |
| Incident root cause acceptance | **Approve** |
| Agent retirement | **Approve** |
| Governance framework exceptions | **Approve** (with documented justification) |

### 3.2 What Must Go to the Board

| Decision | Escalation Trigger |
|----------|-------------------|
| Tier 3 deployment | Always |
| Any deployment with residual risk rated "Critical" | Always |
| Policy changes affecting risk appetite | Always |
| Regulatory enforcement response | Always |
| Budget requests exceeding CAIO authority | Per financial governance |

### 3.3 What Can Be Delegated

| Decision | Delegate To | Conditions |
|----------|------------|------------|
| Tier 1 deployment approval | Technical Owner + Security Lead | Per [Approval Thresholds](approval-thresholds-by-tier.md); Council notified |
| Routine monitoring review | Operational Owner | Monthly report submitted to Council |
| Vendor risk assessment (non-customer-data) | Security Lead | Assessment documented; Council notified |

---

## 4. Decision Process

### 4.1 Standard Decision Flow

```
Proposal submitted (by Policy Owner or Technical Owner)
        |
        v
  +---------------------------+
  | PRE-REVIEW (5 business    |
  | days before meeting)      |
  |                           |
  | Council members review    |
  | proposal + supporting     |
  | artifacts (model card,    |
  | eval results, risk        |
  | assessment)               |
  +---------------------------+
        |
        v
  +---------------------------+
  | COUNCIL MEETING           |
  |                           |
  | 1. Presenter summary      |
  |    (10 min)               |
  | 2. Q&A by council         |
  |    (20 min)               |
  | 3. Closed deliberation    |
  |    (15 min)               |
  | 4. Decision: Approve /    |
  |    Conditionally Approve /|
  |    Reject / Escalate      |
  +---------------------------+
        |
        v
  Decision recorded in meeting minutes
  with conditions, dissenting views,
  and required follow-up actions
```

### 4.2 Decision Outcomes

| Outcome | Definition | Required Action |
|---------|-----------|-----------------|
| **Approved** | All requirements met; deployment authorized | Technical Owner proceeds to deployment |
| **Conditionally Approved** | Requirements met with conditions | Technical Owner must satisfy conditions before deployment; Council verifies |
| **Rejected** | Requirements not met | Technical Owner addresses gaps; re-submit at next meeting |
| **Escalated to Board** | Decision exceeds Council authority | CAIO presents to Board at next session |

### 4.3 Dissent and Minority Views

- Any member may register a **dissenting vote** with written rationale.
- Dissenting views are recorded in the meeting minutes and included in Board reporting.
- A dissenting member may request **escalation to the Board** if they believe the decision creates unacceptable risk. The CAIO must honor this request.

---

## 5. Standing Agenda (Monthly)

| Item | Duration | Owner |
|------|----------|-------|
| 1. Previous action items review | 10 min | CAIO |
| 2. Deployment queue review (new + in-progress) | 20 min | VP Product |
| 3. Tier 2/3 deployment decisions (if any) | 20 min | Presenting team |
| 4. Incident review (Sev1/Sev2 since last meeting) | 15 min | Safety Officer |
| 5. Regulatory update scan | 10 min | Legal Counsel |
| 6. Monitoring dashboard review (drift, accuracy, safety KPIs) | 10 min | Head of Engineering |
| 7. Open items and escalations | 5 min | CAIO |

---

## 6. Record Keeping

### 6.1 Meeting Minutes

Every Council meeting must produce minutes containing:
- Date, time, attendees (including delegates), and quorum confirmation
- Agenda items discussed
- Decisions made (with vote counts and dissenting views)
- Action items (with owners and deadlines)
- Escalations to Board

Minutes are stored in `governance/05-cross-cutting/council-minutes/` and retained for **7 years** per [Document Retention Schedule](aims-document-retention-schedule.md).

### 6.2 Decision Log

A running decision log is maintained at `governance/05-cross-cutting/council-decision-log.yaml`:

```yaml
- decision_id: "DEC-2026-001"
  date: "2026-05-06"
  subject: "DFM Router v2 deployment approval"
  risk_tier: "Tier 1"
  outcome: "approved"
  conditions: []
  votes_for: 7
  votes_against: 0
  dissenting_views: []
  action_items:
    - owner: "Technical Owner"
      deadline: "2026-05-13"
      description: "Deploy to production"
```

---

## 7. Charter Amendments

- This charter may be amended by **majority vote** of the Council.
- Amendments affecting Council authority, composition, or Board escalation rights require **Board approval**.
- All amendments are version-controlled and logged in the document header.

---

## Cross-References

| Document | Relationship |
|----------|-------------|
| [AI Governance Policy](ai-governance-policy.md) | Parent policy; this charter implements Section 3 |
| [Approval Thresholds by Tier](approval-thresholds-by-tier.md) | Defines per-tier approval rules the Council enforces |
| [Governance Roles & RACI](governance-roles-raci.md) | Detailed RACI for all governance roles |
| [Quarterly Governance Report](../06-executive/quarterly-governance-report.md) | Council prepares quarterly Board report |
| [AI Risk Appetite Framework](../06-executive/ai-risk-appetite-framework.md) | Council enforces Board-defined risk appetite |
| [Incident Severity Classification](../04-operational-governance/incident-severity-classification.md) | Council reviews Sev1/Sev2 incidents |
| [ISO 42001 Gap Analysis](../../docs/iso-42001-gap-analysis.md) | Council oversees certification roadmap |

---

*This charter is version-controlled and auditable. Unauthorized modifications void governance compliance claims.*
