# AI Governance Adoption Playbook

> **Purpose:** A phased, step-by-step rollout guide for adopting AI governance across a regulated FinTech over 12 months, from initial assessment to regulatory readiness.
>
> **Regulatory Basis:** All SAFEST pillars; EU AI Act implementation timeline; DORA; DNB Good Practice for AI in the Financial Sector.
>
> **Target Audience:** CEO, CTO, Head of Compliance, and anyone responsible for planning and executing the AI governance adoption program.
>
> **Key Principle:** Governance adoption is a change management program, not a documentation project. If you only produce documents without changing how people work, you have not adopted governance -- you have created a compliance archive.

---

## Rollout Overview

```
Month  1-2          3-4             5-6            7-9            10-12
+------------+ +------------+ +------------+ +------------+ +------------+
|            | |            | |            | |            | |            |
|   ASSESS   | | FOUNDATION | |   EMBED    | |   MATURE   | |  OPTIMIZE  |
|            | |            | |            | |            | |            |
| Inventory  | | Committee  | | Agile      | | Full gov   | | Continuous |
| Classify   | | MVG for    | | integration| | for high   | | improvement|
| Identify   | | all AI     | | Eval       | | risk       | | Internal   |
| owners     | | Board      | | pipelines  | | Automated  | | audit      |
|            | | mandate    | | Train teams| | compliance | | Regulatory |
|            | |            | |            | |            | | readiness  |
+------------+ +------------+ +------------+ +------------+ +------------+
```

---

## Phase 1: ASSESS (Month 1-2)

### Objective

Understand what AI you have, how risky it is, and who is responsible for it. You cannot govern what you have not catalogued.

### Key Actions

| # | Action | Owner | Deliverable | SAFEST Ref |
|---|--------|-------|-------------|-----------|
| 1.1 | **Inventory all AI systems** -- every model, API, algorithm, and ML pipeline in use, including third-party AI services | CTO / Head of AI | AI system inventory (spreadsheet or database) | S-01 |
| 1.2 | **Classify each system by risk tier** using the [Risk Tiering Model](risk-tiering-model.md) decision tree | Model owners + Compliance | Risk tier assigned per system | S-01 |
| 1.3 | **Identify model owners** -- assign a named individual accountable for each AI system | CTO | Owner column in AI system inventory | A-05 |
| 1.4 | **Map current state** -- for each system, document what governance (if any) already exists | Model owners | Current-state assessment | -- |
| 1.5 | **Identify quick wins** -- systems where governance is nearly complete vs. systems with major gaps | Project lead | Gap analysis report | -- |
| 1.6 | **Assess organizational readiness** -- do you have the right skills, tools, and culture for governance? | Head of HR / CTO | Readiness assessment | K-05, K-07 |
| 1.7 | **Secure executive sponsorship** -- brief the board on the governance adoption plan and secure commitment | CEO / CTO | Board briefing minutes | A-01 |

### AI System Inventory Template

| # | System Name | Description | Business Function | Risk Tier | Model Owner | Current Governance State | Gap Priority |
|---|-------------|-------------|-------------------|-----------|-------------|------------------------|-------------|
| 1 | [name] | [what it does] | [fraud, AML, KYC, etc.] | [High/Limited/Minimal] | [name] | [None/Partial/Complete] | [High/Med/Low] |

### Success Criteria

| Criterion | Measurement |
|-----------|-------------|
| All AI systems inventoried | Inventory covers 100% of known AI/ML systems |
| All systems risk-classified | Every system has a risk tier assigned |
| All systems have an owner | Every system has a named model owner |
| Board briefing completed | Board minutes record sponsorship commitment |
| Gap analysis produced | Written report identifying top priority gaps |

### Common Pitfalls

| Pitfall | How to Avoid |
|---------|-------------|
| Missing third-party AI services (vendor APIs, cloud ML) | Ask engineering: "What APIs do we call that have ML behind them?" (K-13) |
| Classifying everything as "minimal" to reduce work | Have 2nd line review all classifications; use decision tree, not intuition |
| No one wants to be the model owner | Make model ownership a recognized responsibility, not a punishment; include in role descriptions |
| Board sees this as a compliance checkbox | Frame governance as competitive advantage for licensing; show DNB expectations |

---

## Phase 2: FOUNDATION (Month 3-4)

### Objective

Establish the organizational governance structure and deploy minimum viable governance across all AI systems.

### Key Actions

| # | Action | Owner | Deliverable | SAFEST Ref |
|---|--------|-------|-------------|-----------|
| 2.1 | **Establish AI Governance Committee** using the [Charter template](../organizational-model/ai-governance-committee-charter.md) | CEO / CTO | Signed Committee charter; first meeting scheduled | A-03 |
| 2.2 | **Assign board-level AI accountability** per the [Board Accountability guide](../organizational-model/board-level-ai-accountability.md) | Board | Board mandate updated with AI accountability clause | A-01 |
| 2.3 | **Define 3 Lines of Defense** per the [3LoD guide](../organizational-model/three-lines-of-defense-for-ai.md) | CRO / CTO | 3LoD documentation; reporting lines documented | A-02 |
| 2.4 | **Deploy MVG for all AI systems** -- every system completes the [10-item MVG checklist](minimum-viable-governance.md) | Model owners | MVG checklist completed per system | S-01, T-12, S-03, S-13, A-11 |
| 2.5 | **Adopt AI governance policies** -- AI ethics principles, prohibited AI uses, model lifecycle policy | Head of Compliance | Board-approved policy documents | E-01, E-03 |
| 2.6 | **Create RACI matrix** for the AI lifecycle (discovery through retirement) | CTO + CRO | RACI matrix document | A-04 |
| 2.7 | **Establish governance improvement backlog** -- all known gaps become tracked items | Project lead | Backlog in issue tracker | -- |

### MVG Deployment Tracker

| System Name | Risk Tier | MVG Item 1: Inventory | MVG Item 2: Owner | MVG Item 3: Model Card | MVG Item 4: Algorithm Doc | MVG Item 5: Criteria Defined | MVG Item 6: Criteria Passing | MVG Item 7: Fallback | MVG Item 8: Logging | MVG Item 9: Training | MVG Item 10: Review Date | Status |
|-------------|-----------|----------------------|-------------------|----------------------|--------------------------|------------------------------|-----------------------------|--------------------|--------------------|--------------------|-------------------------|--------|
| [system] | [tier] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [% done] |

### Success Criteria

| Criterion | Measurement |
|-----------|-------------|
| AI Governance Committee operational | First meeting held; minutes produced |
| Board accountability assigned | Board mandate updated; name documented |
| 3LoD model defined | Documentation complete; no independence conflicts |
| MVG deployed for all systems | 100% of AI systems have all 10 MVG items completed |
| Core policies adopted | AI ethics principles and prohibited uses list board-approved |
| RACI matrix completed | Covers full AI lifecycle; reviewed by all line leads |

### Common Pitfalls

| Pitfall | How to Avoid |
|---------|-------------|
| Committee charter too ambitious for current maturity | Start with monthly meetings and basic agenda; expand as governance matures |
| MVG treated as one-time exercise | MVG establishes ongoing obligations (annual review, logging); it is not done after the checklist |
| 3LoD conflicts with flat organizational structure | You can implement 3LoD in a 20-person company; it is about separation of duties, not headcount |
| Policies written by lawyers without engineering input | Policies must be operationally feasible; involve 1st line in drafting |

---

## Phase 3: EMBED (Month 5-6)

### Objective

Inject governance into daily engineering workflows, establish evaluation pipelines, and train the organization.

### Key Actions

| # | Action | Owner | Deliverable | SAFEST Ref |
|---|--------|-------|-------------|-----------|
| 3.1 | **Integrate governance into Agile sprints** per the [Sprint Integration guide](../process-integration/governance-in-agile-sprints.md) | Scrum Masters / Engineering leads | Extended Definition of Done; governance user story templates in team library | A-04 |
| 3.2 | **Set up evaluation pipelines** -- automated evaluation runs on model changes | ML Engineers | CI/CD pipeline running evaluations; results stored | S-03 |
| 3.3 | **Implement production monitoring** for high-risk and limited-risk systems | ML Engineers / DevOps | Monitoring dashboards; alert thresholds configured | S-12, T-17, F-11 |
| 3.4 | **Launch AI literacy training program** covering all employees who interact with AI | Head of HR / Learning | Training program launched; tracking system in place | K-09 |
| 3.5 | **Conduct role-specific training** for board, compliance, operations, and developers | Head of HR / Learning | Role-specific modules delivered | K-10 |
| 3.6 | **Pilot governance in one sprint team** before rolling out to all teams | 1 sprint team + project lead | Pilot retrospective with lessons learned | -- |
| 3.7 | **Establish incident response procedures** for AI-specific incidents | CISO / CRO | AI incident response plan documented and communicated | A-15 |
| 3.8 | **Upgrade limited-risk systems** from MVG to standard governance (22 items) | Model owners | Standard governance checklist completed for all limited-risk systems | -- |

### Evaluation Pipeline Architecture

```
Code Change (model, data, features)
    |
    v
CI/CD Pipeline Trigger
    |
    +-- Run unit tests (standard)
    |
    +-- Run acceptance criteria evaluations (S-03)
    |       |
    |       +-- Metric 1: [name] vs threshold
    |       +-- Metric 2: [name] vs threshold
    |       +-- Metric 3+: [name] vs threshold
    |
    +-- Run bias/fairness checks (F-03, if limited/high risk)
    |       |
    |       +-- Demographic parity check
    |       +-- Disparate impact ratio
    |
    +-- Generate evaluation report
    |
    +-- Store results alongside model artifacts
    |
    v
Pipeline PASSES: merge allowed
Pipeline FAILS: merge blocked; model owner investigates
```

### Success Criteria

| Criterion | Measurement |
|-----------|-------------|
| Governance in Agile sprints adopted | All sprint teams using extended DoD and governance stories |
| Eval pipelines operational | Automated evaluations running on every model change |
| Production monitoring live | Dashboards operational for all high-risk and limited-risk systems |
| AI literacy training launched | >80% of target audience enrolled |
| Limited-risk systems at standard governance | All limited-risk systems meeting 22-item checklist |
| Incident response plan in place | Plan documented, communicated, and tabletop-tested |

### Common Pitfalls

| Pitfall | How to Avoid |
|---------|-------------|
| Engineering teams resist governance in sprints | Start with pilot team; show it works without destroying velocity; address concerns in retrospectives |
| Evaluation pipelines produce results no one looks at | Integrate eval results into sprint review; make them part of deployment decisions |
| Training is generic "AI awareness" with no practical value | Tailor training to roles; use your own AI systems as examples, not abstract case studies |
| Monitoring dashboards created but not reviewed | Assign dashboard review to a specific person/ceremony (weekly 2nd line review) |

---

## Phase 4: MATURE (Month 7-9)

### Objective

Achieve full governance for all high-risk AI systems, automate compliance checks, and build organizational governance muscle.

### Key Actions

| # | Action | Owner | Deliverable | SAFEST Ref |
|---|--------|-------|-------------|-----------|
| 4.1 | **Complete full governance for all high-risk AI systems** (40+ items per [Risk Tiering Model](risk-tiering-model.md)) | Model owners + 2nd Line | Full governance checklist completed per high-risk system | All |
| 4.2 | **Conduct independent model validation** for all high-risk systems | 2nd Line (Model Validation) | Validation reports per system | S-19 |
| 4.3 | **Complete comprehensive bias testing** for all high-risk and limited-risk systems | Model owners + 2nd Line | Bias testing reports with fairness metrics | F-03, F-04 |
| 4.4 | **Implement automated compliance checks** -- governance status tracked programmatically | ML Engineers / DevOps | Compliance dashboard showing governance completeness per system | -- |
| 4.5 | **Conduct AI incident tabletop exercise** -- simulate a high-severity AI incident | CISO / CRO | Exercise report; identified gaps added to backlog | A-15 |
| 4.6 | **Board AI competency development** -- deep-dive workshops, DNB interview rehearsal | Head of HR / External advisor | Training records; mock interview results | K-01, K-03 |
| 4.7 | **Prepare EU AI Act technical documentation** for high-risk systems (Annex IV) | Model owners + Legal | Technical documentation drafts | T-11 |
| 4.8 | **Complete FRIA** for all high-risk systems | 2nd Line (DPO / Compliance) | FRIA reports | E-12 |
| 4.9 | **Implement champion-challenger framework** for high-risk models | ML Engineers | A/B testing infrastructure for model comparison | S-22 |

### Automated Compliance Dashboard

Track governance completeness programmatically:

```
AI Governance Compliance Dashboard
=====================================

System: Fraud Detection v3.2     Risk Tier: HIGH
Overall Compliance: 38/42 items (90%)

  Documentation:     8/8  [========] 100%
  Evaluations:       7/8  [======= ] 88%  <-- Missing: adversarial testing
  Runtime Monitoring: 6/6  [========] 100%
  Human Oversight:    4/4  [========] 100%
  Transparency:       5/6  [=====  ] 83%  <-- Missing: FRIA (due Aug 2026)
  Skills:             4/4  [========] 100%
  Approval:           4/6  [====   ] 67%  <-- Missing: Board approval, validation

Action Items:
  1. Complete adversarial testing (S-06) -- Due: Month 8
  2. Schedule board approval session -- Due: Month 8
  3. Commission independent validation (S-19) -- Due: Month 9
  4. Draft FRIA (E-12) -- Due: Month 9
```

### Success Criteria

| Criterion | Measurement |
|-----------|-------------|
| All high-risk systems at full governance | 100% of high-risk systems meeting 40+ item checklist |
| Independent validation completed | Validation report exists for every high-risk system |
| Comprehensive bias testing done | Bias testing report exists for all high-risk and limited-risk systems |
| Compliance dashboard operational | Programmatic tracking of governance completeness |
| Incident tabletop exercise completed | Exercise report produced; gaps identified and tracked |
| Board AI competency demonstrated | Training records; mock interview feedback positive |

### Common Pitfalls

| Pitfall | How to Avoid |
|---------|-------------|
| Full governance for high-risk systems takes longer than expected | Start with the most critical system; use it as a template for others |
| Independent validation is a bottleneck (limited 2nd line capacity) | Plan validation scheduling early; consider co-sourcing with external validator |
| Compliance dashboard becomes a vanity metric | Link dashboard to deployment gates: if governance is incomplete, deployment is blocked |
| Board training is "too busy" to attend | Frame as DNB interview preparation; board members who cannot pass the interview put the license at risk |

---

## Phase 5: OPTIMIZE (Month 10-12)

### Objective

Continuous improvement, independent assurance, and demonstrated regulatory readiness.

### Key Actions

| # | Action | Owner | Deliverable | SAFEST Ref |
|---|--------|-------|-------------|-----------|
| 5.1 | **Commission internal audit of AI governance** (first AI-specific audit) | Head of Internal Audit (or outsourced) | Audit report with findings and recommendations | A-02 |
| 5.2 | **Conduct governance maturity assessment** against target state | CRO / Project lead | Maturity assessment report | -- |
| 5.3 | **Address audit findings** -- remediate all critical and high findings | Responsible parties per finding | Finding closure evidence | -- |
| 5.4 | **Prepare regulatory readiness package** -- assemble all evidence for DNB pre-application | Head of Compliance | Regulatory readiness binder (per SAFEST checklist) | All |
| 5.5 | **Conduct DNB pre-application meeting rehearsal** -- internal simulation | External advisor / CEO / CTO | Rehearsal notes; identified weaknesses addressed | K-03 |
| 5.6 | **Produce annual AI governance report** for the board | AI Governance Committee | Annual governance report | K-02 |
| 5.7 | **Review and update all governance documentation** -- policies, checklists, templates | Compliance + Model owners | Updated documentation | All |
| 5.8 | **Establish continuous improvement cadence** -- governance improvement backlog reviewed quarterly | AI Governance Committee | Quarterly improvement cycle in place | -- |
| 5.9 | **Document lessons learned** from the 12-month adoption | Project lead | Lessons learned report | -- |

### Regulatory Readiness Assessment

Use this checklist to assess readiness for a DNB pre-application meeting. Map to the SAFEST checklist readiness scoring (see `safest-checklist-dnb-pre-application.md`).

| SAFEST Pillar | Critical Items Total | Items Complete | % Complete | Status |
|--------------|---------------------|----------------|-----------|--------|
| Soundness (S) | [count] | [count] | [%] | [Ready/Not Ready] |
| Accountability (A) | [count] | [count] | [%] | [Ready/Not Ready] |
| Fairness (F) | [count] | [count] | [%] | [Ready/Not Ready] |
| Ethics (E) | [count] | [count] | [%] | [Ready/Not Ready] |
| Skills (K) | [count] | [count] | [%] | [Ready/Not Ready] |
| Transparency (T) | [count] | [count] | [%] | [Ready/Not Ready] |
| **Overall** | | | | **[Ready / Nearly Ready / Not Ready]** |

Readiness thresholds (from SAFEST checklist):
- **Ready** (>=80% of critical items complete): Schedule the DNB meeting.
- **Nearly Ready** (60-79%): Schedule in 4-8 weeks; close gaps.
- **Not Yet Ready** (<60%): Defer meeting; address gaps first.

### Success Criteria

| Criterion | Measurement |
|-----------|-------------|
| Internal audit completed | Audit report issued with findings rated |
| Critical audit findings remediated | All critical findings closed |
| Regulatory readiness assessed | Readiness assessment completed; score >= 80% of critical items |
| DNB rehearsal completed | Rehearsal conducted; weaknesses addressed |
| Annual governance report produced | Report presented to board |
| Continuous improvement cadence established | Quarterly review cycle operational |

### Common Pitfalls

| Pitfall | How to Avoid |
|---------|-------------|
| Audit commissioned too late -- findings cannot be remediated before DNB meeting | Start audit in Month 10 at the latest; earlier if possible |
| Regulatory readiness package is a document collection, not a coherent narrative | Assign one person to synthesize the package into a clear story for DNB |
| "We are done" mentality after 12 months | Governance is continuous; the 12-month plan is the beginning, not the end |
| Lessons learned report never written | Schedule it; it is the foundation for Year 2 improvement |

---

## Summary Timeline

| Month | Phase | Key Milestone | Key Deliverable |
|-------|-------|--------------|-----------------|
| 1 | Assess | AI system inventory complete | Inventory + risk classifications |
| 2 | Assess | Gap analysis and board briefing | Gap analysis report; board commitment |
| 3 | Foundation | AI Governance Committee established | Signed charter; first meeting held |
| 4 | Foundation | MVG deployed for all systems | MVG checklists complete for all systems |
| 5 | Embed | Governance in Agile sprints piloted | Pilot team retrospective |
| 6 | Embed | Eval pipelines and monitoring live | Automated evaluations running; dashboards operational |
| 7 | Mature | Full governance for first high-risk system | Complete governance package for 1 system |
| 8 | Mature | Independent validation underway | Validation scheduled for all high-risk systems |
| 9 | Mature | All high-risk systems at full governance | Complete governance for all high-risk systems |
| 10 | Optimize | Internal audit commissioned | Audit fieldwork begins |
| 11 | Optimize | Audit findings remediated | Critical findings closed |
| 12 | Optimize | Regulatory readiness confirmed | DNB pre-application readiness package complete |

---

## Resource Requirements

### Estimated Effort by Phase

| Phase | Duration | Key Roles Required | Estimated FTE Equivalent |
|-------|----------|-------------------|-------------------------|
| Assess | 2 months | CTO, model owners, compliance lead | 0.5 FTE total |
| Foundation | 2 months | CTO, CRO, compliance lead, model owners | 1.0 FTE total |
| Embed | 2 months | Scrum masters, ML engineers, HR/Learning, model owners | 1.5 FTE total |
| Mature | 3 months | Model owners, 2nd line validators, compliance, legal | 2.0 FTE total |
| Optimize | 3 months | Internal audit, compliance, CTO, project lead | 1.0 FTE total |

**Notes:**
- FTE estimates are cumulative across all involved roles, not a single person working full-time.
- The "Mature" phase is the most resource-intensive because full governance for high-risk systems requires sustained effort.
- After the 12-month program, ongoing governance maintenance is estimated at 0.5-1.0 FTE depending on the number of AI systems and their risk tiers.

### Budget Considerations

| Cost Category | Typical Range | Notes |
|--------------|---------------|-------|
| External model validation | EUR 10,000-30,000 per model | For high-risk systems requiring independent validation |
| Outsourced internal audit | EUR 15,000-40,000 per audit | Depends on scope and complexity |
| AI literacy training platform | EUR 5,000-15,000/year | Or build internally using existing LMS |
| External governance advisory | EUR 20,000-60,000 | For framework design and DNB preparation |
| Tooling (monitoring, dashboards) | EUR 5,000-20,000/year | May leverage existing infrastructure |

---

## Cross-References

- **Risk Tiering Model:** [risk-tiering-model.md](risk-tiering-model.md) -- used in Phase 1 for classification; determines governance intensity throughout
- **Minimum Viable Governance:** [minimum-viable-governance.md](minimum-viable-governance.md) -- deployed in Phase 2 as the governance floor
- **Three Lines of Defense:** [../organizational-model/three-lines-of-defense-for-ai.md](../organizational-model/three-lines-of-defense-for-ai.md) -- established in Phase 2
- **AI Governance Committee Charter:** [../organizational-model/ai-governance-committee-charter.md](../organizational-model/ai-governance-committee-charter.md) -- adopted in Phase 2
- **Board-Level AI Accountability:** [../organizational-model/board-level-ai-accountability.md](../organizational-model/board-level-ai-accountability.md) -- established in Phase 2
- **Governance in Agile Sprints:** [../process-integration/governance-in-agile-sprints.md](../process-integration/governance-in-agile-sprints.md) -- embedded in Phase 3
- **SAFEST Checklist:** See the parent AIGovernance repository at `docs/06-licensing-preparation/safest-checklist-dnb-pre-application.md`

---

*Last updated: 2026-02-28*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
