# Quarterly AI Governance Report -- Template

> **Purpose:** Standardized template for quarterly AI governance reporting to the board, CAIO, and regulators. Ensures consistent, comprehensive, and evidence-based governance communication aligned with DNB supervisory expectations.
>
> **When to Use:** At the end of each calendar quarter (Q1: Jan-Mar, Q2: Apr-Jun, Q3: Jul-Sep, Q4: Oct-Dec). The report should be finalized within 15 business days of quarter-end and presented at the next board meeting.
>
> **Who Is Responsible:**
> - **Author:** CAIO (or AI Governance PM if CAIO not yet appointed)
> - **Reviewers:** Head of Compliance, Head of Internal Audit
> - **Approver:** Board-level AI accountable member (see [Board-Level AI Accountability](../07-enterprise-implementation/organizational-model/board-level-ai-accountability.md))
> - **Distribution:** Board, AI Ethics Board, Head of Compliance, DNB (on request)
>
> **Regulatory Basis:** SAFEST items A-01 (board-level accountability), T-17 (monitoring dashboards), A-15 (incident management); DNB Good Practice for AI; DORA Article 13(6) (ICT risk management reporting to management body); EU AI Act Article 72 (post-market monitoring obligations for high-risk systems).

---

## Report Metadata

| Field | Value |
|-------|-------|
| **Report Title** | Quarterly AI Governance Report |
| **Reporting Period** | [FILL IN: e.g., Q1 2026 (January -- March 2026)] |
| **Report Date** | [FILL IN: e.g., 2026-04-15] |
| **Author** | [FILL IN: Name, Title] |
| **Reviewed By** | [FILL IN: Name, Title -- Head of Compliance] |
| **Approved By** | [FILL IN: Name, Title -- Board Member with AI Accountability] |
| **Classification** | Confidential -- Board Distribution |
| **Version** | [FILL IN: e.g., 1.0] |
| **Distribution List** | [FILL IN: Board members, CAIO, AI Ethics Board, Head of Compliance, Internal Audit] |
| **Previous Report Date** | [FILL IN: Date of last quarterly report, or "N/A -- First Report"] |

---

## 1. Executive Summary

*Provide a 200-word maximum summary covering: overall governance health, most significant change since last quarter, top risk, and single most important action item for the board.*

[FILL IN]

**Overall Governance Health:** [Green / Amber / Red]

**Key Highlights This Quarter:**
- [FILL IN: 3-5 bullet points of the most important developments]

**Board Action Required:**
- [FILL IN: Specific decisions or approvals needed from the board this quarter]

---

## 2. AI Portfolio Overview

### 2.1 Portfolio Summary

| Metric | Previous Quarter | Current Quarter | Change |
|--------|-----------------|-----------------|--------|
| Total AI systems in production | [FILL IN] | [FILL IN] | [+/- N] |
| AI systems in development/pipeline | [FILL IN] | [FILL IN] | [+/- N] |
| AI systems decommissioned this quarter | -- | [FILL IN] | -- |
| Total autonomous agent systems | [FILL IN] | [FILL IN] | [+/- N] |

### 2.2 Risk Tier Distribution

| Risk Tier | Count | % of Portfolio | Change from Previous Quarter |
|-----------|-------|---------------|------------------------------|
| High Risk (EU AI Act Annex III) | [FILL IN] | [FILL IN]% | [FILL IN] |
| Limited Risk (transparency obligations) | [FILL IN] | [FILL IN]% | [FILL IN] |
| Minimal Risk | [FILL IN] | [FILL IN]% | [FILL IN] |
| Pending Classification | [FILL IN] | [FILL IN]% | [FILL IN] |

### 2.3 New Deployments This Quarter

| System Name | Risk Tier | Business Function | Oversight Model | Deployment Date | Governance Gate Outcome |
|-------------|-----------|-------------------|-----------------|-----------------|------------------------|
| [FILL IN] | [High/Limited/Minimal] | [FILL IN] | [HITL/HOTL/HOTA] | [FILL IN] | [Approved/Conditional] |

### 2.4 Human Oversight Model Distribution

| Oversight Model | Definition | Count | % |
|-----------------|-----------|-------|---|
| **HITL** (Human-in-the-Loop) | Human approves every decision | [FILL IN] | [FILL IN]% |
| **HOTL** (Human-on-the-Loop) | Human monitors, can intervene | [FILL IN] | [FILL IN]% |
| **HOTA** (Human-over-the-Loop) | Human sets policy, agent executes autonomously | [FILL IN] | [FILL IN]% |
| **Fully Autonomous** | No human oversight (minimal risk only) | [FILL IN] | [FILL IN]% |

---

## 3. Governance Maturity Progress

### 3.1 Current Maturity Assessment

| Maturity Dimension | Target Level (12-month) | Current Level | On Track? |
|-------------------|------------------------|---------------|-----------|
| Organizational Model | [FILL IN] | [FILL IN] | [Yes/At Risk/No] |
| Process Integration | [FILL IN] | [FILL IN] | [Yes/At Risk/No] |
| Risk-Based Adoption | [FILL IN] | [FILL IN] | [Yes/At Risk/No] |
| Tooling & Automation | [FILL IN] | [FILL IN] | [Yes/At Risk/No] |

*For maturity level definitions, see [Governance Maturity Roadmap](../07-enterprise-implementation/risk-based-adoption/governance-maturity-roadmap.md).*

### 3.2 Milestones Achieved This Quarter

| Milestone | Target Date | Actual Date | Status |
|-----------|-------------|-------------|--------|
| [FILL IN: e.g., "AI Ethics Board established"] | [FILL IN] | [FILL IN] | [Completed/In Progress/Delayed] |

### 3.3 Milestones at Risk

| Milestone | Target Date | Risk Description | Mitigation Plan |
|-----------|-------------|-----------------|-----------------|
| [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |

---

## 4. Key Metrics Dashboard Summary

*Data sourced from the [AI Governance Dashboard](governance-dashboard-spec.md).*

### 4.1 Pillar Health Summary

| Pillar | Health Status | Key Metric | Value | Trend |
|--------|-------------|------------|-------|-------|
| Discovery | [Green/Amber/Red] | Ethics review backlog | [FILL IN] | [Improving/Stable/Worsening] |
| Development | [Green/Amber/Red] | Eval suite pass rate | [FILL IN]% | [Improving/Stable/Worsening] |
| Runtime | [Green/Amber/Red] | Guardrail trigger rate | [FILL IN]% | [Improving/Stable/Worsening] |
| Operational | [Green/Amber/Red] | Open incidents | [FILL IN] | [Improving/Stable/Worsening] |

### 4.2 Autonomous Decision Statistics

| Metric | Value | Benchmark/Target |
|--------|-------|-----------------|
| Total autonomous agent decisions this quarter | [FILL IN] | -- |
| Decisions escalated to human oversight | [FILL IN] ([FILL IN]%) | <[FILL IN]% |
| Agent boundary violations | [FILL IN] | 0 |
| Autonomous decision error rate | [FILL IN]% | <0.1% |
| Mean time from escalation to human response | [FILL IN] min | <[FILL IN] min |

---

## 5. Incidents and Near-Misses

### 5.1 Incident Summary

| Severity | Count This Quarter | Previous Quarter | Change | All Resolved? |
|----------|-------------------|------------------|--------|---------------|
| Critical (P1) | [FILL IN] | [FILL IN] | [+/- N] | [Yes/No] |
| High (P2) | [FILL IN] | [FILL IN] | [+/- N] | [Yes/No] |
| Medium (P3) | [FILL IN] | [FILL IN] | [+/- N] | [Yes/No] |
| Low (P4) | [FILL IN] | [FILL IN] | [+/- N] | [Yes/No] |
| **Total** | **[FILL IN]** | **[FILL IN]** | **[+/- N]** | -- |

### 5.2 Material Incidents Detail

*Report all Critical and High severity incidents. Reference the incident response playbook in [04-operational-governance/](../04-operational-governance/).*

| Incident ID | Date | System Affected | Severity | Description | Root Cause | Resolution | Lessons Learned |
|-------------|------|-----------------|----------|-------------|-----------|------------|-----------------|
| [FILL IN] | [FILL IN] | [FILL IN] | [P1/P2] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |

### 5.3 Near-Misses

| ID | Date | System | Description | Why It Was Caught | Preventive Action Taken |
|----|------|--------|-------------|-------------------|------------------------|
| [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |

---

## 6. Compliance Status

### 6.1 EU AI Act Compliance

| Obligation | Applicable Systems | Status | Deadline | Notes |
|-----------|-------------------|--------|----------|-------|
| High-risk system registration | [FILL IN] | [Complete/In Progress/Not Started] | [FILL IN] | [FILL IN] |
| Conformity assessment | [FILL IN] | [Complete/In Progress/Not Started] | [FILL IN] | [FILL IN] |
| Transparency obligations (Art. 50) | [FILL IN] | [Complete/In Progress/Not Started] | [FILL IN] | [FILL IN] |
| AI literacy requirements (Art. 4) | All staff | [Complete/In Progress/Not Started] | [FILL IN] | [FILL IN] |

### 6.2 DORA Compliance (AI-Specific)

| Requirement | Status | Evidence | Notes |
|-------------|--------|----------|-------|
| AI systems included in ICT risk management framework | [Complete/In Progress/Not Started] | [FILL IN] | [FILL IN] |
| Third-party AI provider risk assessment | [Complete/In Progress/Not Started] | [FILL IN] | [FILL IN] |
| AI incident reporting procedures aligned with DORA | [Complete/In Progress/Not Started] | [FILL IN] | [FILL IN] |
| AI operational resilience testing | [Complete/In Progress/Not Started] | [FILL IN] | [FILL IN] |

### 6.3 DNB SAFEST Progress

| SAFEST Pillar | Total Items | Completed | % Complete | Previous Quarter % | Target % (Year-End) |
|---------------|-------------|-----------|-----------|-------------------|---------------------|
| **S** -- Security & Soundness | [FILL IN] | [FILL IN] | [FILL IN]% | [FILL IN]% | [FILL IN]% |
| **A** -- Accountability | [FILL IN] | [FILL IN] | [FILL IN]% | [FILL IN]% | [FILL IN]% |
| **F** -- Fairness | [FILL IN] | [FILL IN] | [FILL IN]% | [FILL IN]% | [FILL IN]% |
| **E** -- Ethics | [FILL IN] | [FILL IN] | [FILL IN]% | [FILL IN]% | [FILL IN]% |
| **S** -- Sustainability | [FILL IN] | [FILL IN] | [FILL IN]% | [FILL IN]% | [FILL IN]% |
| **T** -- Transparency | [FILL IN] | [FILL IN] | [FILL IN]% | [FILL IN]% | [FILL IN]% |
| **Overall** | **[FILL IN]** | **[FILL IN]** | **[FILL IN]%** | **[FILL IN]%** | **[FILL IN]%** |

*Detailed SAFEST item status available in the [AI Governance Dashboard](governance-dashboard-spec.md).*

---

## 7. Risk Register Updates

### 7.1 Top AI Risks

| Risk ID | Risk Description | Likelihood | Impact | Risk Score | Mitigation Status | Owner | Change Since Last Quarter |
|---------|-----------------|-----------|--------|-----------|-------------------|-------|--------------------------|
| [FILL IN] | [FILL IN] | [1-5] | [1-5] | [L x I] | [Open/Mitigating/Closed] | [FILL IN] | [New/Increased/Stable/Decreased/Closed] |

### 7.2 Emerging Risks

*New risks identified this quarter that were not on the previous risk register.*

| Risk Description | Source of Identification | Preliminary Assessment | Proposed Response |
|-----------------|------------------------|----------------------|-------------------|
| [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |

---

## 8. Audit Findings and Remediation

| Finding ID | Source | Severity | Description | Remediation Plan | Target Date | Status |
|-----------|--------|----------|-------------|-----------------|-------------|--------|
| [FILL IN] | [Internal Audit / External Audit / DNB] | [Critical/High/Medium/Low] | [FILL IN] | [FILL IN] | [FILL IN] | [Open/In Progress/Closed] |

**Summary:** [FILL IN: Total open findings, any overdue, overall trajectory]

---

## 9. Upcoming Regulatory Deadlines

| Deadline | Regulation | Description | Owner | Status | Days Remaining |
|----------|-----------|-------------|-------|--------|---------------|
| [FILL IN] | [EU AI Act / DORA / DNB] | [FILL IN] | [FILL IN] | [On Track/At Risk/Overdue] | [FILL IN] |

---

## 10. Resource and Budget

### 10.1 Governance Program Budget

| Category | Budget (Quarter) | Actual Spend | Variance | Notes |
|----------|-----------------|-------------|----------|-------|
| Personnel (FTE) | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |
| Tooling & Platforms | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |
| External Audit / Advisory | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |
| Training & Upskilling | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |
| **Total** | **[FILL IN]** | **[FILL IN]** | **[FILL IN]** | -- |

### 10.2 Resource Allocation

| Role | FTE Allocated | FTE Utilized | Gap |
|------|--------------|-------------|-----|
| CAIO / AI Governance Lead | [FILL IN] | [FILL IN] | [FILL IN] |
| AI Ethics Board members (part-time) | [FILL IN] | [FILL IN] | [FILL IN] |
| AI Stewards (embedded in teams) | [FILL IN] | [FILL IN] | [FILL IN] |
| Compliance / 2nd Line | [FILL IN] | [FILL IN] | [FILL IN] |
| Internal Audit / 3rd Line | [FILL IN] | [FILL IN] | [FILL IN] |

---

## 11. Recommendations and Action Items

### 11.1 Board Decisions Requested

| # | Decision Required | Rationale | Recommended Action | Deadline |
|---|------------------|-----------|-------------------|----------|
| 1 | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |

### 11.2 Action Items from This Report

| # | Action | Owner | Priority | Deadline | Status |
|---|--------|-------|----------|----------|--------|
| 1 | [FILL IN] | [FILL IN] | [Critical/High/Medium] | [FILL IN] | [New] |

### 11.3 Outstanding Actions from Previous Quarter

| # | Action | Owner | Original Deadline | Current Status | Revised Deadline |
|---|--------|-------|-------------------|----------------|-----------------|
| 1 | [FILL IN] | [FILL IN] | [FILL IN] | [Open/In Progress/Closed/Overdue] | [FILL IN] |

---

## 12. Appendices

### Appendix A: Glossary

See the unified [Glossary](../05-cross-cutting/glossary.md) for definitions of terms used in this report.

### Appendix B: ISO/IEC 42001 PDCA Alignment

| PDCA Phase | Report Sections |
|-----------|-----------------|
| **Plan** | Sections 3 (Maturity targets), 9 (Deadlines), 10 (Budget) |
| **Do** | Sections 2 (Deployments), 4 (Metrics) |
| **Check** | Sections 4 (Metrics), 5 (Incidents), 6 (Compliance), 8 (Audit) |
| **Act** | Sections 7 (Risk updates), 11 (Recommendations) |

---

## Cross-References

| Related Artifact | Location | Relationship |
|-----------------|----------|-------------|
| AI Governance Dashboard Specification | [06-executive/governance-dashboard-spec.md](governance-dashboard-spec.md) | Dashboard is the data source for Section 4 |
| Board-Level AI Accountability | [07-enterprise/board-level-ai-accountability.md](../07-enterprise-implementation/organizational-model/board-level-ai-accountability.md) | Defines the approver role for this report |
| Governance Maturity Roadmap | [07-enterprise/governance-maturity-roadmap.md](../07-enterprise-implementation/risk-based-adoption/governance-maturity-roadmap.md) | Section 3 references maturity levels and milestones |
| Three Lines of Defense | [07-enterprise/three-lines-of-defense-for-ai.md](../07-enterprise-implementation/organizational-model/three-lines-of-defense-for-ai.md) | Report distribution follows 3LoD model |
| Risk Tiering Model | [07-enterprise/risk-tiering-model.md](../07-enterprise-implementation/risk-based-adoption/risk-tiering-model.md) | Section 2.2 uses risk tier definitions |
| SAFEST Checklists | Various YAML files across pillar directories | Section 6.3 aggregates SAFEST completion data |
| Incident Response Playbooks | [04-operational-governance/](../04-operational-governance/) | Section 5 references incident handling procedures |

---

*Template Version: 1.0*
*Last updated: 2026-02-28*
*Classification: Confidential -- Board Distribution*
