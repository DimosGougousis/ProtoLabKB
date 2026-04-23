# Governance in Quarterly Planning

## Purpose

Define the quarterly AI governance review cadence that connects sprint-level governance execution to board-level strategic oversight. Quarterly planning ensures the AI portfolio is assessed holistically, governance resources are allocated proportionally, and the CAIO delivers structured reporting to the board. Without this cadence, governance becomes reactive -- problems are discovered at audit time rather than managed proactively.

## When to Use

- At the start of each fiscal quarter during portfolio planning
- When the CAIO prepares the quarterly governance report for the board
- When new AI initiatives require risk classification and governance budget allocation
- When reviewing AI risk register entries accumulated during the prior quarter
- During annual budget planning to justify governance investment

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **CAIO** | **Responsible** -- prepares and presents the quarterly AI governance review |
| **Board / CEO** | **Accountable** -- reviews and acts on quarterly governance findings |
| **AI Governance Committee** | **Consulted** -- pre-reviews quarterly materials before board submission |
| **Product Managers** | **Consulted** -- provide AI initiative roadmaps and resource requirements |
| **Compliance Officer** | **Consulted** -- provides regulatory developments and compliance status |
| **Internal Audit** | **Informed** -- uses quarterly outputs as input for audit planning |

## Regulatory Basis

- **SAFEST item K-02** -- board-level AI governance reporting
- **SAFEST item A-01** -- AI strategy aligned with business objectives
- **SAFEST item S-01** -- AI system inventory maintenance and review
- **DNB Good Practice for AI** -- periodic review of AI risk and governance effectiveness
- **EU AI Act Article 9(2)** -- continuous risk management system with regular systematic review
- **DORA Article 5(2)** -- ICT risk management framework must be reviewed at least yearly and upon major incidents
- **Wft Section 3:17** -- sound and controlled business operations require periodic oversight

---

## 1. Quarterly AI Portfolio Review

### 1.1 Review Scope

Each quarter, the CAIO conducts a portfolio-level review covering all AI systems in the inventory. This is not a deep-dive into individual models -- that happens at the team level. This is a strategic view of the AI portfolio's risk posture, governance health, and alignment with business objectives.

### 1.2 Review Agenda Template

| # | Agenda Item | Time | Owner | Input Documents |
|---|------------|------|-------|----------------|
| 1 | **Portfolio overview** -- total AI systems by risk tier, new additions, retirements since last quarter | 10 min | CAIO | AI system inventory |
| 2 | **Governance health dashboard** -- gate pass rates, overdue reviews, open exceptions, incident count | 15 min | CAIO | Governance KPI dashboard |
| 3 | **AI risk register review** -- top 5 risks, movement since last quarter, new risks identified | 15 min | CAIO + Risk Manager | AI risk register |
| 4 | **New AI initiatives** -- risk classification of proposed initiatives, governance requirements, resource needs | 20 min | Product Managers | Initiative proposals |
| 5 | **Regulatory developments** -- new regulations, guidance updates, supervisory actions affecting AI | 10 min | Compliance Officer | Regulatory tracker |
| 6 | **Governance resource allocation** -- staffing, tooling, training budgets for next quarter | 15 min | CAIO | Budget tracker |
| 7 | **Escalations and decisions** -- items requiring Committee or Board attention | 10 min | CAIO | Escalation log |
| 8 | **Actions and next steps** -- documented actions with owners and deadlines | 5 min | CAIO | Action tracker |

**Total meeting duration: 100 minutes**

---

## 2. AI Risk Register Review

### 2.1 Risk Register Structure

The AI risk register is the living document that tracks identified AI-specific risks across the portfolio. It is reviewed in full each quarter by the CAIO and AI Governance Committee.

| Field | Description |
|-------|------------|
| **Risk ID** | Unique identifier (e.g., AIR-2026-015) |
| **Risk description** | What could go wrong and what would be the impact |
| **Affected AI system(s)** | Which systems from the inventory are exposed |
| **Risk tier** | High / Medium / Low |
| **Likelihood** | Rare / Unlikely / Possible / Likely / Almost Certain |
| **Impact** | Negligible / Minor / Moderate / Major / Critical |
| **Inherent risk score** | Likelihood x Impact |
| **Controls in place** | Existing mitigations (governance gates, monitoring, guardrails) |
| **Residual risk score** | Risk after controls |
| **Risk owner** | Named individual |
| **Status** | Open / Mitigating / Accepted / Closed |
| **Trend** | Increasing / Stable / Decreasing (vs. prior quarter) |

### 2.2 Quarterly Risk Review Actions

| If... | Then... |
|-------|---------|
| Residual risk exceeds risk appetite | Escalate to Board with remediation plan and timeline |
| New risk tier = High | Assign to next AI Governance Committee meeting within 2 weeks |
| Risk trend is increasing for 2+ quarters | Trigger root cause analysis; consider additional controls |
| Control effectiveness is unverified | Schedule control testing before next quarterly review |
| Risk is accepted | Document acceptance rationale, accepting authority, and review date |

---

## 3. New AI Initiative Risk Classification

### 3.1 Quarterly Intake Process

All new AI initiatives proposed for the next quarter must be risk-classified before receiving governance and development resources.

| Step | Action | Owner | Timeline |
|------|--------|-------|----------|
| 1 | Product team submits AI initiative proposal using the [Responsible Product Brief](../../01-discovery-governance/templates/responsible-product-brief.md) | Product Manager | 2 weeks before quarterly review |
| 2 | CoE pre-screens using the [Risk Tiering Model](../risk-based-adoption/risk-tiering-model.md) decision tree | AI Risk Analyst | 1 week before quarterly review |
| 3 | CAIO presents classified initiatives at quarterly review with recommended governance profiles | CAIO | During quarterly review |
| 4 | Committee approves, modifies, or rejects proposed initiatives | AI Governance Committee | During quarterly review |
| 5 | Approved initiatives receive governance resource allocation | CAIO | Within 1 week of quarterly review |

### 3.2 FinTech Example: Q2 Initiative Intake

| Initiative | Proposed Use | Pre-Screen Risk Tier | Governance Profile | Estimated Governance Effort |
|-----------|-------------|---------------------|-------------------|---------------------------|
| AI-powered transaction monitoring enhancement | Upgrade existing AML detection model with LLM-based alert triage | High | Full governance | 160 hours |
| Customer onboarding chatbot | Conversational agent guiding KYC document submission | Limited | Standard governance | 80 hours |
| Internal expense categorization | Auto-classify employee expense receipts | Minimal | MVG | 16 hours |

---

## 4. Governance Resource Allocation

### 4.1 Budget Categories

| Category | Description | Typical Allocation |
|----------|-----------|-------------------|
| **Staffing** | CoE team, AI Stewards, external specialists | 50-60% |
| **Tooling** | Evaluation platforms, monitoring tools, GRC systems | 20-25% |
| **Training** | AI literacy programs, certification courses, workshops | 10-15% |
| **External services** | Independent validation, external audit, legal advisory | 10-15% |

### 4.2 Resource Allocation by Risk Tier

Governance resources are allocated proportional to risk, not proportional to the number of AI systems.

| Risk Tier | Systems (typical) | Governance Effort (typical) | Rationale |
|-----------|------------------|-----------------------------|-----------|
| High | 20% of portfolio | 60% of governance budget | Full lifecycle governance, independent validation, board reporting |
| Limited | 50% of portfolio | 30% of governance budget | Standard governance with evaluation pipelines and monitoring |
| Minimal | 30% of portfolio | 10% of governance budget | MVG only -- inventory, basic model card, annual review |

---

## 5. CAIO Quarterly Report Template

The CAIO delivers this report to the Board quarterly. It should be concise (3-5 pages), evidence-based, and focused on decisions the Board needs to make.

### 5.1 Report Structure

```markdown
# AI Governance Quarterly Report -- Q[X] [YEAR]

## 1. Executive Summary (1 paragraph)
[Key message: are we in control of our AI risk? What decisions does the Board need to make?]

## 2. Portfolio Snapshot
| Metric | This Quarter | Last Quarter | Trend |
|--------|-------------|-------------|-------|
| Total AI systems in inventory | | | |
| High-risk systems | | | |
| Limited-risk systems | | | |
| Minimal-risk systems | | | |
| Systems deployed this quarter | | | |
| Systems retired this quarter | | | |

## 3. Governance Health KPIs
| KPI | Target | Actual | Status |
|-----|--------|--------|--------|
| AI inventory completeness | 100% | | [G/A/R] |
| Governance gate first-pass rate | >85% | | [G/A/R] |
| Mean time to governance approval | <5 days | | [G/A/R] |
| Open governance exceptions | <5 | | [G/A/R] |
| AI incidents (Sev 1-2) | 0 | | [G/A/R] |
| AI literacy training completion | >95% | | [G/A/R] |
| Overdue model reviews | 0 | | [G/A/R] |

## 4. Top 5 AI Risks
[Risk ID, description, trend, controls, residual risk, Board action required]

## 5. Regulatory Developments
[New regulations, guidance changes, supervisory actions relevant to AI]

## 6. Next Quarter Outlook
[Planned AI deployments, governance resource needs, key milestones]

## 7. Decisions Required
[Specific decisions the Board needs to make with options and CAIO recommendation]
```

---

## 6. Board-Level KPI Review

### 6.1 KPI Definitions and Thresholds

| KPI | Definition | Green | Amber | Red |
|-----|-----------|-------|-------|-----|
| **AI inventory completeness** | % of production AI systems registered in inventory | 100% | 90-99% | <90% |
| **Governance gate first-pass rate** | % of deployments passing all governance gates on first attempt | >85% | 70-85% | <70% |
| **Mean governance approval time** | Average business days from deployment package submission to approval | <5 days | 5-10 days | >10 days |
| **Open governance exceptions** | Number of active exceptions to governance standards | <5 | 5-10 | >10 |
| **AI incidents (Severity 1-2)** | Count of high-severity AI incidents in the quarter | 0 | 1-2 | >2 |
| **AI literacy completion** | % of relevant staff completing required AI training | >95% | 80-95% | <80% |
| **Overdue model reviews** | Number of AI systems past their scheduled review date | 0 | 1-3 | >3 |
| **Regulatory findings (AI)** | Count of AI-related regulatory findings open | 0 | 1-2 minor | Any major |
| **Bias testing coverage** | % of customer-facing AI systems with current bias test results | 100% | 80-99% | <80% |

### 6.2 KPI Escalation Protocol

| KPI Status | Action | Timeline |
|-----------|--------|----------|
| All Green | Information only; no Board action required | Quarterly report |
| Any Amber | CAIO presents remediation plan at next Committee meeting | Within 2 weeks |
| Any Red | CAIO presents to Board with immediate remediation plan | Within 1 week |
| Red for 2+ consecutive quarters | Board reviews CAIO effectiveness and governance program adequacy | At next Board meeting |

---

## 7. Annual Governance Planning Cycle

Quarterly reviews feed into the annual governance planning cycle.

| Quarter | Focus | Key Deliverable |
|---------|-------|----------------|
| **Q1** | Annual governance plan approval; budget allocation; regulatory horizon scan | Annual governance plan document |
| **Q2** | Mid-year progress review; adjust plan based on regulatory developments | Mid-year governance report |
| **Q3** | Pre-audit preparation; gap assessment; remediation planning | Audit readiness assessment |
| **Q4** | Annual governance effectiveness review; next-year planning; maturity assessment | Annual governance report; next-year plan draft |

---

## Cross-References

- **CAIO Role and KPIs:** [../../05-cross-cutting/governance-roles-raci.md](../../05-cross-cutting/governance-roles-raci.md) -- CAIO success metrics that feed quarterly reporting
- **AI Governance Committee Charter:** [../organizational-model/ai-governance-committee-charter.md](../organizational-model/ai-governance-committee-charter.md) -- the body that pre-reviews quarterly materials
- **Board-Level AI Accountability:** [../organizational-model/board-level-ai-accountability.md](../organizational-model/board-level-ai-accountability.md) -- board oversight obligations this cadence supports
- **Risk Tiering Model:** [../risk-based-adoption/risk-tiering-model.md](../risk-based-adoption/risk-tiering-model.md) -- risk classification for new initiatives
- **Adoption Playbook:** [../risk-based-adoption/adoption-playbook.md](../risk-based-adoption/adoption-playbook.md) -- 12-month plan that quarterly reviews track
- **Supervisory Reporting Calendar:** [supervisory-reporting-calendar.md](supervisory-reporting-calendar.md) -- external reporting deadlines that quarterly reviews must align with
- **Executive Dashboard Spec:** [../../06-executive/governance-dashboard-spec.md](../../06-executive/governance-dashboard-spec.md) -- visualization of KPIs reviewed quarterly
- **Quarterly Governance Report:** [../../06-executive/quarterly-governance-report.md](../../06-executive/quarterly-governance-report.md) -- companion executive report format

---

*Last updated: 2026-03-01*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
