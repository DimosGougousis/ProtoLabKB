# Governance in Agile Sprints

> **Purpose:** Define how AI governance checkpoints integrate into Agile/Scrum ceremonies, so that governance is a natural part of the engineering workflow rather than a separate bureaucratic process.
>
> **Regulatory Basis:** SAFEST items A-04 (RACI matrix for AI lifecycle), A-11 (decision audit trail), A-12 (model change log); DNB expectation that governance is operationalized, not theoretical.
>
> **Key Principle:** Governance should be invisible when things are going well and loud when things go wrong. If governance feels like a separate activity, it is not integrated -- it is appended.

---

## 1. Governance Across Scrum Ceremonies

### 1.1 Sprint Planning

**When:** Start of each sprint.

**Governance integration points:**

| Activity | Who | What | SAFEST Ref |
|----------|-----|------|-----------|
| Assign risk tier to new AI features | Product Owner + 2nd Line | Every new AI feature story gets a risk tier label (minimal/limited/high) from the [Risk Tiering Model](../risk-based-adoption/risk-tiering-model.md) | S-01 |
| Include governance tasks in sprint | Product Owner | Governance tasks are sized and added to the sprint backlog, not a separate backlog | A-04 |
| Estimate governance effort | Team | Governance work is estimated like any other work; it counts against velocity | A-04 |
| Flag governance blockers | Scrum Master | Identify any governance dependencies (e.g., 2nd line review needed, Committee approval pending) | A-04 |
| Check: does this sprint include an AI deployment? | Product Owner | If yes, ensure deployment approval checklist items are in the sprint | A-03 |

**Sprint Planning Template Addition:**

For each AI-related user story, ask:

```
1. What is the risk tier of this AI feature? [Minimal / Limited / High]
2. What governance deliverables does this tier require?
   (See risk-tiering-model.md Section 2.2)
3. Are the governance deliverables in this sprint's backlog?
4. Are there governance dependencies outside the team?
   (2nd line review, Committee approval, external validation)
5. Is this sprint deploying an AI system to production?
   If yes: is the deployment approval package ready?
```

### 1.2 Daily Standup

**When:** Daily, 15 minutes.

**Governance integration points:**

Governance blockers are treated like any other blocker. No separate "governance standup" is needed.

| Signal | Action | Who Owns |
|--------|--------|----------|
| "Blocked on model validation review" | Scrum Master escalates to 2nd line lead | Scrum Master |
| "Bias testing surfaced an issue" | Team investigates; may need to re-scope the sprint | Model Owner + 2nd Line |
| "Evaluation results below threshold" | Block deployment until root cause identified | Model Owner |
| "Data drift alert fired overnight" | Investigate; assess if sprint scope needs to change | On-call engineer |
| "Governance Committee rejected our deployment request" | Product Owner negotiates or adjusts scope | Product Owner |

**Anti-pattern:** Creating a separate "governance standup" or "compliance check-in." If governance is separate from the daily standup, it is not integrated.

### 1.3 Sprint Review (Demo)

**When:** End of each sprint.

**Governance integration points:**

| Activity | Who Presents | What to Demonstrate | SAFEST Ref |
|----------|-------------|-------------------|-----------|
| Demo AI feature functionality | AI Engineer | What the model does, how it works | T-01 |
| Show evaluation results | AI Engineer | Pre-deployment eval results against acceptance criteria | S-03 |
| Present bias/fairness test results (if applicable) | AI Engineer or 2nd Line | Fairness metrics for this sprint's AI work | F-03 |
| Demonstrate fallback behavior | DevOps/MLOps | What happens when the AI fails; live demo if possible | S-13 |
| Show model card updates | Model Owner | New or updated sections of the model card | T-12 |
| Present governance compliance status | Model Owner | Which governance items are complete vs. outstanding | A-04 |

**Sprint Review Governance Slide Template:**

```
Sprint [N] -- AI Governance Summary
====================================

AI Feature: [Feature name]
Risk Tier: [Minimal / Limited / High]

Evaluation Results:
  Metric 1: [name] = [value] vs threshold [threshold] [PASS/FAIL]
  Metric 2: [name] = [value] vs threshold [threshold] [PASS/FAIL]
  Metric 3: [name] = [value] vs threshold [threshold] [PASS/FAIL]

Fairness Check: [Completed / Not required / In progress]
  Result: [summary or "N/A"]

Deployment Readiness:
  [ ] Model card updated
  [ ] Evaluations passing
  [ ] Fallback documented and tested
  [ ] Logging configured
  [ ] Approval obtained: [Team lead / Committee / Board]

Outstanding Items:
  - [List any incomplete governance items with target dates]
```

**Anti-pattern:** Skipping governance items in the sprint review because "the stakeholders do not care." If governance is not demonstrated, it is not verified.

### 1.4 Sprint Retrospective

**When:** End of each sprint, after Sprint Review.

**Governance integration points:**

Add these governance-specific retrospective questions to your standard format:

| Question | Purpose | Possible Actions |
|----------|---------|-----------------|
| "Did governance tasks take longer than estimated?" | Calibrate governance effort estimation | Adjust planning; create reusable templates; automate where possible |
| "Did any governance blocker slow us down?" | Identify process bottlenecks | Improve 2nd line response times; pre-schedule reviews |
| "Did we discover a governance gap this sprint?" | Continuous improvement | Add to governance improvement backlog; update checklists |
| "Did we skip any governance steps? If so, why?" | Detect governance erosion | Address root cause: time pressure, unclear requirements, tooling gaps |
| "Is the risk tier still correct for the AI system we worked on?" | Ongoing risk assessment | Reclassify if needed; adjust governance intensity |

**Retrospective Output:** Governance improvement items go into the team's backlog, not a separate governance backlog. They are prioritized alongside feature work.

### 1.5 Backlog Grooming (Refinement)

**When:** Mid-sprint or as scheduled.

**Governance integration points:**

| Activity | Who | What | SAFEST Ref |
|----------|-----|------|-----------|
| Add governance stories for new AI features | Product Owner + Model Owner | Every new AI feature in the backlog gets companion governance stories | A-04 |
| Size governance stories | Team | Governance work is estimated like feature work | A-04 |
| Review risk tier of upcoming features | 2nd Line (if attending) or PO | Upcoming AI features are pre-classified so governance requirements are known before sprint planning | S-01 |
| Identify 2nd line dependencies | Scrum Master | Flag stories that need model validation, Committee approval, or external review | S-19, A-03 |

---

## 2. Definition of Done Extension for AI Features

Extend the team's existing Definition of Done (DoD) with AI governance requirements. The extension is tiered by risk level.

### 2.1 DoD Extension: All AI Features (All Risk Tiers)

A user story involving AI is not "done" unless:

| # | Criterion | SAFEST Ref |
|---|-----------|-----------|
| 1 | AI system is registered in the AI system inventory (or entry updated) | S-01 |
| 2 | Model card exists and is current | T-12 |
| 3 | Acceptance criteria are defined, evaluated, and passing | S-03 |
| 4 | Fallback behavior is documented | S-13 |
| 5 | Logging is configured and verified | A-11 |
| 6 | Model change log is updated | A-12 |
| 7 | Named model owner is assigned | A-05 |

### 2.2 DoD Extension: Limited-Risk AI Features (Additional)

| # | Criterion | SAFEST Ref |
|---|-----------|-----------|
| 8 | Customer-facing AI disclosure implemented (if applicable) | T-06 |
| 9 | Override / escalation to human implemented (if applicable) | A-07 |
| 10 | Basic fairness check completed | F-03 |
| 11 | Kill switch implemented and documented | A-09 |
| 12 | AI Governance Committee approval obtained | A-03 |

### 2.3 DoD Extension: High-Risk AI Features (Additional)

| # | Criterion | SAFEST Ref |
|---|-----------|-----------|
| 13 | Independent model validation completed by 2nd line | S-19 |
| 14 | Full bias testing across protected groups completed | F-03 |
| 15 | Stress testing completed with documented results | S-05 |
| 16 | Human-in-the-loop design documented and implemented | A-06 |
| 17 | Customer decision explanation mechanism implemented | T-07 |
| 18 | Explainability method documented and tested | T-01 |
| 19 | FRIA completed (from Aug 2026) | E-12 |
| 20 | Board approval obtained | A-01 |

---

## 3. Governance User Story Templates

Use these templates to create governance stories in your backlog. They follow the standard user story format and can be pointed, estimated, and tracked like any other story.

### Template 1: Model Card

```
As a [model owner / regulator / auditor],
I want a current model card for [AI system name],
So that anyone can understand what this system does,
  what data it uses, and what its limitations are.

Acceptance Criteria:
- Model card follows the organization's template
  (see minimum-viable-governance.md Section 3)
- All sections are filled in with current information
- Model card is stored in the model's repository
- Model card is linked from the AI system inventory

Risk Tier: [All tiers]
SAFEST Reference: T-12
Estimated Effort: [X] story points
```

### Template 2: Pre-Deployment Evaluation

```
As a [model owner],
I want to run pre-deployment evaluations for [AI system name],
So that I have evidence the model meets its acceptance criteria
  before it serves customers.

Acceptance Criteria:
- [N] acceptance criteria are defined with measurable thresholds
- Evaluation pipeline is automated and reproducible
- All criteria are passing (or failing criteria are documented
  with a remediation plan approved by the governance committee)
- Results are stored alongside the model card

Risk Tier: [All tiers]
SAFEST Reference: S-03
Estimated Effort: [X] story points
```

### Template 3: Bias/Fairness Testing

```
As a [model owner / compliance officer],
I want to complete bias testing for [AI system name],
So that we have evidence the model does not discriminate
  across protected characteristics.

Acceptance Criteria:
- Protected characteristics relevant to this use case identified (F-01)
- Proxy variable analysis completed (F-02)
- Fairness metrics selected and justified (F-04)
- Testing executed across all relevant subgroups
- Results documented with pass/fail against defined thresholds
- Results reviewed by 2nd line

Risk Tier: [Limited, High]
SAFEST Reference: F-03, F-04
Estimated Effort: [X] story points
```

### Template 4: Fallback Procedure

```
As a [DevOps engineer / on-call responder],
I want a documented and tested fallback procedure for [AI system name],
So that service continues if the AI system fails.

Acceptance Criteria:
- Fallback procedure documented (what happens, who is notified,
  what manual process takes over)
- Fallback tested in staging environment
- Recovery time measured and documented (S-14)
- Kill switch (if applicable) tested and documented (A-09)

Risk Tier: [All tiers]
SAFEST Reference: S-13, S-14, A-09
Estimated Effort: [X] story points
```

### Template 5: Governance Committee Deployment Package

```
As a [model owner],
I want to prepare the deployment approval package for [AI system name],
So that the AI Governance Committee can make an informed
  approval decision.

Acceptance Criteria:
- Model card complete and current (T-12)
- Risk tier classification documented (S-01)
- Pre-deployment evaluation results attached (S-03)
- Bias/fairness testing results attached (F-03, if applicable)
- Independent validation report attached (S-19, if high-risk)
- Fallback procedure documented (S-13)
- DPIA attached (if personal data)
- FRIA attached (if high-risk, from Aug 2026)
- Package submitted 5 business days before Committee meeting

Risk Tier: [Limited, High]
SAFEST Reference: A-03
Estimated Effort: [X] story points
```

### Template 6: AI Incident Retrospective

```
As a [incident responder / model owner],
I want to complete a root cause analysis for AI incident [ID],
So that we can prevent recurrence and improve our AI governance.

Acceptance Criteria:
- Incident timeline reconstructed from logs (A-11)
- Root cause identified (A-18)
- Immediate remediation completed and verified
- Long-term prevention actions identified and added to backlog
- Lessons learned documented
- Incident report submitted to AI Governance Committee

Risk Tier: [All tiers -- triggered by incident]
SAFEST Reference: A-15, A-18
Estimated Effort: [X] story points
```

---

## 4. Sprint Governance by Risk Tier

How governance affects sprint capacity depends on the risk tier of the AI system being developed.

### Estimated Governance Overhead by Tier

| Risk Tier | Governance Overhead (% of Sprint Capacity) | Typical Activities |
|-----------|-------------------------------------------|-------------------|
| Minimal | 5-10% | Model card, 3 evals, logging, annual review |
| Limited | 15-25% | Above + fairness check, transparency, Committee package |
| High | 25-40% | Above + independent validation, full bias testing, FRIA, board package |

**Note:** These percentages decrease over time as governance becomes habitual and tooling automates repetitive steps. In the first 2-3 sprints with governance, expect the higher end of the range. After 6 months, expect the lower end.

### Sprint Capacity Planning Example

```
Team velocity: 40 story points per sprint
Sprint contains: 1 high-risk AI feature + 2 non-AI features

Governance allocation:
  High-risk AI governance stories: ~12 points (30% of 40)
  Feature work (AI): ~12 points
  Feature work (non-AI): ~16 points
  Total: 40 points

Governance stories in this sprint:
  - Update model card (2 pts)
  - Run pre-deployment evaluations (3 pts)
  - Complete bias testing (3 pts)
  - Prepare Committee deployment package (2 pts)
  - Implement customer explanation mechanism (2 pts)
  Total governance: 12 points
```

---

## 5. Anti-Patterns: What NOT to Do

### Anti-Pattern 1: Governance as Afterthought

**Symptom:** Governance tasks are added at the end of the sprint or after the feature is "done."

**Why it fails:** Governance requirements may change the design. Discovering at deployment time that you need human-in-the-loop review means rework.

**Fix:** Governance stories are added during backlog grooming and sprint planning, not sprint review.

### Anti-Pattern 2: Governance as Separate Sprint

**Symptom:** "We do a governance sprint every quarter to catch up."

**Why it fails:** Governance is decoupled from development. Models deploy without governance and governance is retrofitted. DNB will see this as a paper exercise.

**Fix:** Governance is part of every sprint that includes AI work. It is never deferred.

### Anti-Pattern 3: Governance Owned by Compliance

**Symptom:** The compliance team writes all governance documentation; engineering team does not engage.

**Why it fails:** Compliance cannot write accurate model cards or meaningful evaluation criteria. The documentation will be generic and fail under regulatory scrutiny.

**Fix:** 1st line (engineering) creates governance deliverables. 2nd line (compliance) reviews and challenges them. See [Three Lines of Defense](../organizational-model/three-lines-of-defense-for-ai.md).

### Anti-Pattern 4: Governance Blocking Everything

**Symptom:** Every AI change requires Committee approval, causing multi-week delays.

**Why it fails:** Teams bypass governance or stop innovating. Governance becomes the enemy.

**Fix:** Use risk tiering. Minimal-risk AI needs team lead sign-off, not Committee approval. Only limited and high-risk changes go to Committee. See [Risk Tiering Model](../risk-based-adoption/risk-tiering-model.md).

### Anti-Pattern 5: Governance Theater

**Symptom:** All checklists are filled in, but no one can explain what the evaluations actually test or what the model card means.

**Why it fails:** DNB will interview your people. If the model owner cannot explain the model card they signed off on, governance is performative.

**Fix:** The person who creates the governance deliverable must be able to explain it. If they cannot, the deliverable is not done.

### Anti-Pattern 6: Copy-Paste Governance

**Symptom:** Every model card looks identical. Every evaluation uses the same 3 metrics regardless of the model.

**Why it fails:** Generic governance does not capture system-specific risks. A fraud detection model and a log analyzer have fundamentally different risk profiles.

**Fix:** Governance deliverables must be specific to the AI system. Templates provide structure; content must be bespoke.

---

## 6. Tooling Recommendations

Governance integration works best when supported by tooling. These are recommendations, not requirements.

| Need | Tooling Approach | Benefit |
|------|-----------------|---------|
| Model card management | Version-controlled markdown in model repository | Tracks changes; part of code review |
| Evaluation pipeline | CI/CD integration (e.g., GitHub Actions, GitLab CI) | Evaluations run automatically on model changes |
| Governance checklist tracking | Issue tracker labels/tags (e.g., Jira, Linear, GitHub Issues) | Governance stories visible alongside feature work |
| Audit trail | Structured logging to centralized system | Automated evidence collection (A-11) |
| Risk tier labels | Custom labels in issue tracker | At-a-glance risk tier visibility in backlog |
| Committee package assembly | Template in document management system | Consistent, complete deployment packages |

---

## 7. Implementation Checklist

| # | Item | Status |
|---|------|--------|
| 1 | Definition of Done extended with AI governance criteria (per risk tier) | [ ] |
| 2 | Sprint Planning includes governance task identification for AI features | [ ] |
| 3 | Daily Standup treats governance blockers like any other blocker | [ ] |
| 4 | Sprint Review includes governance compliance demonstration | [ ] |
| 5 | Sprint Retrospective includes governance-specific questions | [ ] |
| 6 | Backlog Grooming adds governance stories for upcoming AI features | [ ] |
| 7 | Governance user story templates available in the team's template library | [ ] |
| 8 | Risk tier labels configured in issue tracker | [ ] |
| 9 | Sprint review governance slide template available | [ ] |
| 10 | Team trained on governance integration approach | [ ] |

---

## Cross-References

- **Risk Tiering Model:** [../risk-based-adoption/risk-tiering-model.md](../risk-based-adoption/risk-tiering-model.md) -- determines governance intensity per sprint
- **Minimum Viable Governance:** [../risk-based-adoption/minimum-viable-governance.md](../risk-based-adoption/minimum-viable-governance.md) -- the lightest governance profile for sprint work on minimal-risk AI
- **Three Lines of Defense:** [../organizational-model/three-lines-of-defense-for-ai.md](../organizational-model/three-lines-of-defense-for-ai.md) -- who does what in sprint governance
- **AI Governance Committee Charter:** [../organizational-model/ai-governance-committee-charter.md](../organizational-model/ai-governance-committee-charter.md) -- deployment approval authority and meeting cadence
- **Adoption Playbook:** [../risk-based-adoption/adoption-playbook.md](../risk-based-adoption/adoption-playbook.md) -- when sprint integration happens in the rollout timeline
- **SAFEST Checklist:** See the parent AIGovernance repository at `docs/06-licensing-preparation/safest-checklist-dnb-pre-application.md`

---

*Last updated: 2026-02-28*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
