# AI Governance Maturity Roadmap

## Purpose

Define a 12-month journey from ad-hoc AI governance to an optimized, measurable, and continuously improving governance program. This roadmap provides five maturity levels with concrete assessment criteria, month-by-month milestones, quick wins per quarter, and common pitfalls. It complements the [Adoption Playbook](adoption-playbook.md) by providing the maturity assessment framework that measures progress.

## When to Use

- During initial governance program planning to set realistic expectations and milestones
- At semi-annual maturity assessments to measure progress (see [Supervisory Reporting Calendar](../process-integration/supervisory-reporting-calendar.md))
- When reporting governance maturity to the Board as part of the quarterly governance report
- When DNB asks "how mature is your AI governance?" during SREP or licensing
- When justifying governance investment by demonstrating measurable maturity improvement

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **CAIO** | **Responsible** -- drives maturity progression, conducts assessments, reports to Board |
| **Board** | **Accountable** -- approves maturity targets and resources |
| **AI Governance Committee** | **Consulted** -- reviews maturity assessments and approves remediation plans |
| **Product Teams** | **Consulted** -- provide evidence of governance execution for maturity scoring |
| **Internal Audit** | **Consulted** -- validates maturity assessment accuracy independently |

## Regulatory Basis

- **DNB Good Practice for AI** -- expects progressive maturity in AI governance; "good practice" implies a journey, not a binary state
- **SAFEST all pillars** -- maturity levels map to progressive completion of SAFEST items
- **EU AI Act Article 9(2)** -- risk management as a continuous iterative process implies growing maturity
- **ISO/IEC 42001 Section 10** -- continual improvement of the AI management system
- **DORA Article 5** -- ICT risk management framework subject to continuous improvement

---

## 1. Five Maturity Levels

### 1.1 Level Definitions

| Level | Name | Description | FinTech Reality |
|-------|------|------------|-----------------|
| **0** | **Reactive** | No AI governance. AI incidents are handled ad-hoc when they occur. No proactive measures. Organization reacts to problems rather than preventing them. | "We deal with AI problems when customers complain or regulators ask." |
| **1** | **Ad-Hoc** | Informal AI governance. AI systems exist but governance is individual-dependent, undocumented, and inconsistent. No CAIO, no committee, no standards. | "We have models in production but nobody can list them all." |
| **2** | **Managed** | Basic governance structure exists. AI inventory started, model owners assigned, CAIO mandate established. Governance happens but is largely manual and reactive. | "We know what AI we have and who owns it, but governance is still a checklist exercise." |
| **3** | **Defined** | Governance policies, standards, and processes are documented and enforced. Evaluation pipelines exist. Federated governance model operational. Governance is integrated into development workflows. | "Governance is part of how we build, not something we bolt on afterward." |
| **4** | **Measured** | Governance effectiveness is quantified with KPIs. Exception register is active. Quarterly reporting is data-driven. Continuous monitoring produces actionable insights. Governance decisions are evidence-based. | "We can prove our governance works with data, not just documents." |
| **5** | **Optimized** | Continuous improvement based on metrics and feedback. Proactive regulatory engagement. Industry benchmarking. Governance automation reduces manual effort. Innovation in governance practice. | "Our governance improves every quarter and adapts to new AI capabilities before regulators require it." |

**Note:** Level 0 (Reactive) is added from the research paper to acknowledge organizations with no proactive governance. Most regulated FinTechs should aim for Level 2+ immediately.

### 1.2 Assessment Criteria per Level

#### Level 1: Ad-Hoc

| Criterion | Status |
|-----------|--------|
| AI systems exist in production | Yes |
| Complete AI system inventory exists | No |
| Named model owners for all systems | No |
| CAIO or equivalent mandate | No |
| Documented governance policies | No |
| Evaluation pipelines | No |
| Incident response process for AI | No |

#### Level 2: Managed

| Criterion | Required | Evidence |
|-----------|----------|----------|
| AI system inventory covers >90% of production systems | Yes | Inventory document/database |
| Every system has a named model owner | Yes | Inventory with owner column |
| CAIO mandate formally assigned | Yes | Board resolution or job description |
| AI Governance Committee established | Yes | Approved charter |
| MVG applied to all minimal-risk systems | Yes | Completed MVG checklists |
| Basic model cards exist for high-risk systems | Yes | Model card documents |
| AI risk register started | Yes | Risk register with at least top 5 risks |
| Board has been briefed on AI governance | Yes | Board meeting minutes |

#### Level 3: Defined

| Criterion | Required | Evidence |
|-----------|----------|----------|
| All Level 2 criteria sustained | Yes | Periodic verification |
| Governance policies documented and approved by Committee | Yes | Policy documents |
| Risk tiering model applied to all systems | Yes | Risk tier assigned in inventory |
| Evaluation pipelines operational for high and limited-risk systems | Yes | Pipeline configurations and results |
| Bias testing conducted for all customer-facing AI | Yes | Bias evaluation reports |
| Governance integrated into CI/CD pipelines | Yes | Pipeline gate configurations |
| Governance integrated into sprint ceremonies | Yes | DoD with governance criteria |
| Federated governance model operational (CoE + AI Stewards) | Yes | CoE charter, steward assignments |
| Training program launched | Yes | Training materials and completion records |
| Fallback and kill switch procedures documented and tested | Yes | Test results |

#### Level 4: Measured

| Criterion | Required | Evidence |
|-----------|----------|----------|
| All Level 3 criteria sustained | Yes | Periodic verification |
| Governance KPIs defined and tracked (see quarterly planning) | Yes | KPI dashboard |
| Quarterly governance report delivered to Board | Yes | Board reports |
| Exception register active with quarterly review | Yes | Exception register |
| Independent model validation completed for all high-risk systems | Yes | Validation reports |
| Continuous monitoring operational with automated alerting | Yes | Monitoring dashboard + alert history |
| Incident response process tested with drill | Yes | Drill results |
| Internal audit completed for AI governance | Yes | Audit report |
| Governance cycle time measured and improving | Yes | Cycle time metrics |
| SAFEST self-assessment completed | Yes | Self-assessment scorecard |

#### Level 5: Optimized

| Criterion | Required | Evidence |
|-----------|----------|----------|
| All Level 4 criteria sustained | Yes | Periodic verification |
| Governance KPIs show improving trends for 2+ consecutive quarters | Yes | Trend analysis |
| Automated compliance checks reduce manual governance effort by >50% | Yes | Automation metrics |
| Proactive regulatory engagement (sharing practices, participating in industry groups) | Yes | Meeting records |
| Governance processes updated based on incident learnings and audit findings | Yes | Process change log |
| Champion-challenger governance applied (comparing governance approaches) | Yes | Comparison results |
| Governance innovation documented (new tools, new approaches, new metrics) | Yes | Innovation log |
| External benchmark against industry peers | Yes | Benchmark report |
| **Cost governance operational** | **Yes** | **Cost attribution dashboard, budget variance <5%** |
| **Multi-tenancy governance implemented** | **Yes** | **6-layer isolation validated, cross-tenant audit clean** |

**New Criteria (Research Paper Addition):**

**Cost Governance:**
- Hierarchical budget architecture operational (Org → Team → Agent → Skill → Run)
- Cost attribution dashboard deployed with real-time visibility
- Budget variance tracking with <5% variance from forecast
- Model routing by complexity/cost optimized
- ROI per agent/skill tracked and reported

**Multi-Tenancy Governance:**
- 6-layer isolation model implemented and validated
- Cross-tenant attack pattern detection operational
- Per-tenant audit isolation with separate encryption keys
- Tenant-scoped SPIFFE trust domains operational
- Annual cross-tenant isolation penetration testing completed

---

## 2. Month-by-Month Milestones

### 2.1 Months 1-3: Foundation (Target: Level 1 to Level 2)

| Month | Milestone | Key Deliverable | Owner |
|-------|-----------|----------------|-------|
| **1** | Complete AI system inventory | Inventory with >90% of production systems | CTO |
| **1** | Assign model owners for all inventoried systems | Owner column populated in inventory | CTO |
| **1** | Secure Board commitment and appoint CAIO | Board resolution | CEO |
| **2** | Classify all systems by risk tier | Risk tier assigned per system | CAIO + Compliance |
| **2** | Establish AI Governance Committee | Approved charter | CAIO |
| **2** | Start AI risk register | Top 10 risks identified and scored | CAIO |
| **3** | Apply MVG to all minimal-risk systems | Completed MVG checklists (10 items per system) | Model Owners |
| **3** | Create model cards for high-risk systems | Draft model cards | Data Scientists |
| **3** | Board AI governance briefing | Board presentation delivered | CAIO |

### 2.2 Months 4-6: Integration (Target: Level 2 to Level 3)

| Month | Milestone | Key Deliverable | Owner |
|-------|-----------|----------------|-------|
| **4** | Document governance policies and standards | Policy document approved by Committee | CAIO |
| **4** | Launch evaluation pipelines for high-risk systems | Eval pipelines running in CI/CD | ML Engineers |
| **4** | Establish CoE with core team | CoE charter, team hired/assigned | CAIO |
| **5** | Integrate governance into sprint ceremonies | Updated Definition of Done for all AI squads | Scrum Masters |
| **5** | Conduct first bias evaluations for customer-facing AI | Bias evaluation reports | Data Scientists |
| **5** | Assign AI Stewards to product squads | Steward roles filled | CAIO |
| **6** | Implement governance gates in CI/CD pipelines | Gate configurations blocking non-compliant deployments | ML Engineers |
| **6** | Launch AI literacy training program | Training materials delivered, first cohort completed | CAIO + HR |
| **6** | Test fallback and kill switch procedures | Test results documented | ML Engineers |

### 2.3 Months 7-9: Measurement (Target: Level 3 to Level 4)

| Month | Milestone | Key Deliverable | Owner |
|-------|-----------|----------------|-------|
| **7** | Define and deploy governance KPI dashboard | Dashboard operational | CAIO |
| **7** | Deliver first quarterly governance report to Board | Q1 board report | CAIO |
| **7** | Complete independent validation for all high-risk systems | Validation reports | AI Risk Analyst |
| **8** | Activate continuous monitoring with automated alerting | Monitoring system operational | ML Engineers |
| **8** | Establish exception register | Exception register with review process | CAIO |
| **8** | Conduct AI incident response drill | Drill results and learnings | CAIO |
| **9** | Complete SAFEST self-assessment | Self-assessment scorecard | CAIO |
| **9** | Commission first internal audit of AI governance | Audit scope and schedule agreed | Internal Audit |
| **9** | Measure governance cycle time baseline | Baseline metrics | CAIO |

### 2.4 Months 10-12: Optimization (Target: Level 4 to Level 5)

| Month | Milestone | Key Deliverable | Owner |
|-------|-----------|----------------|-------|
| **10** | Internal audit completed with findings addressed | Audit report + remediation plan | Internal Audit + CAIO |
| **10** | Implement automated compliance checks for repeatable governance items | Automation configurations | ML Engineers |
| **10** | Governance KPIs showing improving trends | Trend analysis | CAIO |
| **11** | Proactive regulatory engagement initiated | Meeting with DNB / industry group participation | CAIO |
| **11** | Process improvements implemented based on audit findings | Updated processes | CAIO |
| **11** | Champion-challenger approach tested for one governance process | Comparison results | CAIO |
| **12** | Annual governance effectiveness review | Annual report | CAIO |
| **12** | External maturity benchmark (if available) | Benchmark results | CAIO |
| **12** | Next-year governance plan approved | Annual plan | Board |

---

## 3. Quick Wins per Quarter

### Q1 Quick Wins (Months 1-3)

1. **Inventory the obvious** -- list all AI systems your team knows about in a shared spreadsheet. Do not wait for perfection.
2. **Name the owners** -- assign every AI system a model owner by the end of week 2. An imperfect assignment is better than none.
3. **Apply MVG to 3 systems** -- pick your 3 lowest-risk AI systems and complete MVG checklists. Prove the process works.
4. **Hold one Committee meeting** -- even if the charter is still draft, hold the first governance committee meeting to establish the cadence.

### Q2 Quick Wins (Months 4-6)

1. **Add one governance gate to CI/CD** -- start with a model card completeness check. Automate the simplest governance requirement first.
2. **Run one bias evaluation** -- pick your highest-risk customer-facing system and run a fairness evaluation. Document results even if imperfect.
3. **Add governance to one team's DoD** -- pilot governance integration with a single squad before rolling out to all teams.
4. **Train one cohort** -- deliver AI governance training to the team building your highest-risk AI system.

### Q3 Quick Wins (Months 7-9)

1. **Build a 3-metric dashboard** -- start with inventory completeness, gate pass rate, and overdue reviews. Three metrics are better than no dashboard.
2. **Run one incident drill** -- simulate a model producing harmful outputs. Test your response without a real incident.
3. **Complete one validation** -- have your AI Risk Analyst independently validate your highest-risk model. Learn from the first validation.
4. **Deliver one board report** -- use the CAIO quarterly report template. A brief report is better than no report.

### Q4 Quick Wins (Months 10-12)

1. **Automate one check** -- identify the most tedious manual governance check and automate it. Prove automation value.
2. **Close one audit finding** -- address the most impactful finding from internal audit quickly. Demonstrate responsiveness.
3. **Show trend improvement** -- present at least one KPI that has improved over the last two quarters to the Board.
4. **Plan next year** -- use the maturity assessment to set realistic targets for the next 12 months.

---

## 4. Resource Requirements

### 4.1 Resource Requirements by Maturity Transition

| Transition | Duration | FTE Required | Budget (EUR, approximate) | Key Roles |
|-----------|----------|-------------|--------------------------|-----------|
| Level 1 to 2 | 3 months | 2.0 FTE | 50K-100K (primarily staffing) | CAIO (0.5), Compliance (0.5), CTO (0.5), Admin (0.5) |
| Level 2 to 3 | 3 months | 4.0 FTE | 150K-250K (staffing + tooling) | CAIO (1.0), ML Engineer (1.0), AI Risk Analyst (0.5), Stewards (1.0), Training (0.5) |
| Level 3 to 4 | 3 months | 4.5 FTE | 100K-200K (primarily tooling + validation) | CAIO (1.0), ML Engineer (1.0), AI Risk Analyst (1.0), Internal Audit (0.5), Dashboard (1.0) |
| Level 4 to 5 | 3 months | 3.0 FTE | 75K-150K (optimization + automation) | CAIO (1.0), ML Engineer (1.0), Governance Lead (0.5), External engagement (0.5) |

### 4.2 Total 12-Month Investment

| Category | Year 1 Estimate (EUR) |
|----------|----------------------|
| Staffing (CoE team) | 300K-500K |
| Tooling (evaluation, monitoring, GRC) | 75K-150K |
| Training (programs, certifications) | 25K-50K |
| External services (validation, audit, legal) | 50K-100K |
| **Total** | **450K-800K** |

---

## 5. Common Pitfalls

| Pitfall | Description | Prevention |
|---------|------------|-----------|
| **Paper governance** | Creating documents without changing how people work | Verify that governance artifacts are used in daily decisions, not filed and forgotten |
| **Boil the ocean** | Trying to reach Level 5 in month 1 | Follow the phased approach; celebrate Level 2 before pursuing Level 3 |
| **CAIO without authority** | Appointing a CAIO who cannot block deployments | Ensure Board delegates deployment authority explicitly |
| **Governance as punishment** | Teams perceive governance as a tax on productivity | Frame governance as quality assurance; celebrate governance wins; measure governance speed |
| **Central bottleneck** | All governance decisions flow through one person | Implement federated model early; empower AI Stewards |
| **Ignoring quick wins** | Spending months on infrastructure before delivering visible value | Ship MVG for 3 systems in month 1; demonstrate value before asking for more investment |
| **Skipping Level 2** | Jumping to eval pipelines and CI/CD gates without knowing what AI you have | Inventory first; always; no exceptions |
| **One-time effort** | Treating governance as a project that finishes | Governance is an ongoing operating expense, not a one-time project |
| **No Board engagement** | CAIO works in isolation without Board support | Brief the Board in Month 1; deliver quarterly reports from Month 7 |
| **Audit avoidance** | Delaying internal audit because "we are not ready" | An early audit at Level 3 provides course correction; waiting until Level 5 risks compounding problems |

---

## 6. Maturity Assessment Template

Use this template semi-annually to score your current maturity level.

| # | Assessment Question | Level 2 | Level 3 | Level 4 | Level 5 | Current Status |
|---|-------------------|---------|---------|---------|---------|---------------|
| 1 | Is the AI system inventory complete? | >90% | 100% | 100% + auto-validated | 100% + reconciled with prod | |
| 2 | Does every system have a named model owner? | Yes | Yes | Verified quarterly | Verified + succession plan | |
| 3 | Is the CAIO mandate formally documented? | Yes | Yes + authority matrix | Yes + success metrics | Yes + external recognition | |
| 4 | Are governance policies documented? | Draft | Approved + enforced | Measured for effectiveness | Continuously improved | |
| 5 | Are eval pipelines operational for high-risk AI? | No | Yes | Yes + automated alerts | Yes + champion-challenger | |
| 6 | Is governance integrated into CI/CD? | No | Basic gates | Comprehensive gates | Gates + automated remediation | |
| 7 | Are governance KPIs tracked? | No | No | Yes | Yes + improving trends | |
| 8 | Is independent validation completed? | No | Started | All high-risk complete | All high-risk + sample limited | |
| 9 | Has internal audit reviewed AI governance? | No | No | First audit complete | Annual audit + trend | |
| 10 | Is governance continuously improving? | No | No | Responding to findings | Proactive improvement | |

**Scoring:** Your maturity level is the highest level where ALL criteria for that level and below are met. Partial completion does not count.

---

## Cross-References

- **Adoption Playbook:** [adoption-playbook.md](adoption-playbook.md) -- the 12-month execution plan this roadmap measures
- **Risk Tiering Model:** [risk-tiering-model.md](risk-tiering-model.md) -- risk classification that drives governance intensity
- **Minimum Viable Governance:** [minimum-viable-governance.md](minimum-viable-governance.md) -- the Level 2 governance floor
- **Full Governance Profile:** [full-governance-profile.md](full-governance-profile.md) -- Level 3+ requirements for high-risk systems
- **AI Center of Excellence:** [../organizational-model/ai-center-of-excellence.md](../organizational-model/ai-center-of-excellence.md) -- CoE maturity indicators
- **Governance in Quarterly Planning:** [../process-integration/governance-in-quarterly-planning.md](../process-integration/governance-in-quarterly-planning.md) -- quarterly reviews that track maturity
- **Governance Roles and RACI:** [../../05-cross-cutting/governance-roles-raci.md](../../05-cross-cutting/governance-roles-raci.md) -- CAIO success metrics aligned with maturity levels

---

*Last updated: 2026-03-01*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
