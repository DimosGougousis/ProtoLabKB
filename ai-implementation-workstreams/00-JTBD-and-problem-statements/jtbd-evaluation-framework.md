# JTBD Evaluation Framework

> **Purpose:** Single source of truth for evaluating, prioritizing, and validating Jobs to be Done before they enter the funnel intake. This document answers: *"What jobs matter, how much, and what does done look like?"*
> **Scope:** All ProtoLabs AI governance and manufacturing intelligence JTBDs
> **Owner:** AI Product + Governance Committee
> **Review Cadence:** Monthly or after every major discovery sprint

---

## How to Use This Document

1. **Product Strategy** — Use Section 1 (RICE + Opportunity Scoring) to rank jobs and allocate roadmap capacity.
2. **Funnel Intake** — Use Section 2 (MoSCoW) to scope use cases: a use case that activates only "Could" jobs is a weak bet.
3. **Executive Decisions** — Use Section 3 (Cost of Not Doing) to justify investment or explain deferral.
4. **Sequencing** — Use Section 4 (Dependencies) to identify blockers and parallelization opportunities.
5. **Eval-Driven Development** — Use Section 5 (Acceptance Criteria Library) to define "done" before building.
6. **Confidence Calibration** — Use Section 6 (Evidence Quality) to flag jobs that need discovery before build commitment.

---

## 1. Job Scoring: RICE + Opportunity Score

### Scoring Methodology

| Dimension | Formula | Source |
|-----------|---------|--------|
| **RICE** | (Reach × Impact × Confidence) / Effort | Intercom framework |
| **Opportunity Score** | Importance × (5 − Current Satisfaction) | Ulwick / Christensen |
| **Composite Rank** | 60% RICE rank + 40% Opportunity Score rank | ProtoLabs weighted |

### Scoring Definitions

| Dimension | Scale | How to Estimate |
|-----------|-------|-----------------|
| **Reach** | Users or events per quarter | Usage analytics, CRM data, support ticket volume |
| **Impact** | 1–5 (0.25 = minimal, 1 = low, 2 = medium, 3 = high, 4 = massive) | Revenue at stake, compliance risk, strategic fit |
| **Confidence** | % (20% = moonshot, 50% = low, 80% = medium, 100% = high) | Evidence quality (see Section 6) |
| **Effort** | Engineer-weeks | Engineering lead estimate, ranged |
| **Importance** | 1–5 (1 = nice-to-have, 5 = existential) | Stakeholder interviews, win/loss analysis |
| **Current Satisfaction** | 1–5 (1 = deeply unsatisfied, 5 = fully satisfied) | Survey, NPS verbatims, support ticket sentiment |

### Evaluated Jobs

#### Functional Jobs

| JTBD ID | Job Statement | Reach (qtr) | Impact | Confidence | Effort (wks) | **RICE** | Importance | Satisfaction | **Opp Score** | **Composite Rank** |
|---------|--------------|-------------|--------|------------|--------------|----------|------------|--------------|---------------|--------------------|
| F1 | Secure AI Input Processing | 10,000 queries | 5 | 90% | 4 | **1,125** | 5 | 1 | **20** | **1** |
| F2 | Defend Against Adversarial Attacks | 10,000 queries | 5 | 85% | 8 | **531** | 5 | 2 | **15** | **2** |
| F3 | Monitor System Behavior | All AI services | 4 | 80% | 6 | **427** | 4 | 2 | **12** | **4** |
| F4 | Maintain Audit Compliance | All audits + DSRs | 5 | 90% | 6 | **338** | 5 | 2 | **15** | **3** |
| CAD-CORE | Evaluate CAD Files for Manufacturability | 5,000 uploads | 4 | 70% | 12 | **117** | 4 | 2 | **12** | **5** |
| CAD-VLM | Visual Understanding of Manufacturing Complexity | 3,000 uploads | 3 | 60% | 10 | **54** | 3 | 3 | **6** | **8** |
| CAD-HIST | Learn from Previous Projects | 5,000 uploads | 3 | 50% | 16 | **47** | 3 | 2 | **9** | **6** |
| SD-1 | LMM Buy/Build Strategy Decision | 1 (strategic) | 5 | 40% | 8 | **100** | 5 | 1 | **20** | **1** |
| SD-2 | Historical Data Loading & Curation Pipeline | Internal only | 4 | 30% | 20 | **24** | 4 | 1 | **16** | **7** |
| SD-3 | Governance Gap Resolution | Internal only | 4 | 30% | 12 | **40** | 4 | 1 | **16** | **7** |

#### Emotional Jobs

| JTBD ID | Job Statement | Reach (qtr) | Impact | Confidence | Effort (wks) | **RICE** | Importance | Satisfaction | **Opp Score** | **Composite Rank** |
|---------|--------------|-------------|--------|------------|--------------|----------|------------|--------------|---------------|--------------------|
| E1 | Confidence in Security | 500 engineers | 4 | 70% | 6 | **233** | 5 | 2 | **15** | **3** |
| E2 | Trust in Compliance | 50 compliance staff | 3 | 60% | 4 | **225** | 4 | 2 | **12** | **4** |
| E3 | Control Over Risk | 200 managers | 3 | 50% | 4 | **188** | 4 | 3 | **8** | **6** |

#### Social Jobs

| JTBD ID | Job Statement | Reach (qtr) | Impact | Confidence | Effort (wks) | **RICE** | Importance | Satisfaction | **Opp Score** | **Composite Rank** |
|---------|--------------|-------------|--------|------------|--------------|----------|------------|--------------|---------------|--------------------|
| S1 | Industry Leadership | All customers | 3 | 50% | 8 | **94** | 3 | 3 | **6** | **8** |
| S2 | Responsible Innovation | Industry peers | 2 | 40% | 6 | **53** | 3 | 3 | **6** | **8** |

### Priority Tiers (from Composite Rank)

| Tier | Composite Rank | Action |
|------|----------------|--------|
| **P0 — Must Build** | 1–3 | Fund immediately; block release if not done |
| **P1 — Should Build** | 4–6 | Fund in next quarter; negotiate scope if constrained |
| **P2 — Could Build** | 7–8 | Backlog; fund only if P0/P1 complete and capacity exists |
| **P3 — Won't Build (Now)** | >8 | Explicitly deprioritize; revisit quarterly |

---

## 2. MoSCoW Classification

### Classification Rules

| Classification | Definition | Funnel Intake Rule |
|----------------|------------|-------------------|
| **Must** | Regulatory requirement, security hard blocker, or existential business risk | Use case MUST activate at least one Must job to proceed |
| **Should** | High business value, drives adoption, or unblocks strategic bets | Use case SHOULD activate ≥1 Should job; if only Must, flag as "compliance-only" |
| **Could** | Nice-to-have, competitive differentiation, or future-proofing | Use case CAN include Could jobs but cannot be justified by them alone |
| **Won't** | Out of scope, conflicts with strategy, or cost exceeds value | Use case MUST NOT activate Won't jobs; if it does, flag scope conflict |

### MoSCoW by JTBD

| JTBD ID | Job | MoSCoW | Rationale |
|---------|-----|--------|-----------|
| F1 | Secure AI Input Processing | **Must** | EU AI Act Art. 15 (accuracy); GDPR Art. 32 (security); zero tolerance for breach |
| F2 | Defend Against Adversarial Attacks | **Must** | Defense-in-depth requirement; F1 ineffective without F2 |
| F3 | Monitor System Behavior | **Must** | ISO 27001 A.12.4 (monitoring); NIST AI RMF Measure function |
| F4 | Maintain Audit Compliance | **Must** | GDPR Art. 30 (records); SOX 404 (controls); ISO 27001 A.12.4 |
| CAD-CORE | Evaluate CAD Files for Manufacturability | **Should** | Core revenue driver; not legally required but strategically critical |
| CAD-VLM | Visual Understanding of Manufacturing Complexity | **Could** | Differentiator; rules-based system covers 70% of cases |
| CAD-HIST | Learn from Previous Projects | **Could** | Moat builder; requires data flywheel that doesn't exist yet |
| SD-1 | LMM Buy/Build Strategy Decision | **Must** | Gates all downstream model work; governance gaps persist until decided |
| SD-2 | Historical Data Loading & Curation Pipeline | **Should** | Enables Phase 2 fine-tuning; not needed for Phase 1 (buy API) |
| SD-3 | Governance Gap Resolution | **Should** | Required for ISO 42001 certification; can draft during Phase 1 |
| E1 | Confidence in Security | **Should** | Drives adoption; not legally required but failure = attrition |
| E2 | Trust in Compliance | **Should** | Enables audit cooperation; failure = audit friction |
| E3 | Control Over Risk | **Could** | Management comfort; can be addressed with reporting |
| S1 | Industry Leadership | **Could** | Marketing value; no direct revenue impact |
| S2 | Responsible Innovation | **Won't** | Influencer play; defer until core security jobs complete |

### Dependency Rule

> A **Must** job cannot depend on a **Could** or **Won't** job. If a Must job's prerequisite is classified Could/Won't, escalate the prerequisite to **Should** or **Must**.

---

## 3. Cost of Not Doing (CoND)

### Methodology

For each P0/P1 job, estimate the annual cost of deferral or non-delivery. This is not the cost to build — it is the cost of *not* building.

| Cost Category | How to Estimate | Source |
|---------------|-----------------|--------|
| **Regulatory penalty** | Max fine × probability of enforcement action | Legal + compliance risk register |
| **Revenue at risk** | Affected pipeline × win-rate degradation | CRM + win/loss analysis |
| **Competitive loss** | Market share shift × customer LTV | Competitive intelligence |
| **Operational inefficiency** | Manual effort × hourly cost × frequency | Time-motion studies |
| **Reputational damage** | NPS drop × churn increase × LTV | Customer success data |
| **Talent attrition** | Replacement cost × turnover increase | HR data |

### Cost of Not Doing by JTBD

| JTBD ID | Job | Regulatory Penalty | Revenue at Risk | Competitive Loss | OpEx Inefficiency | Reputational Damage | Talent Attrition | **Total Annual CoND** |
|---------|-----|-------------------|-----------------|------------------|-------------------|---------------------|------------------|----------------------|
| F1 | Secure AI Input Processing | €20M (GDPR 4%) | $5M–$15M (IP theft) | $2M–$8M | $500K (manual review) | $1M–$3M | $200K | **$29M–$47M** |
| F2 | Defend Against Adversarial Attacks | €10M (GDPR 2%) | $3M–$10M | $1M–$5M | $300K | $500K–$2M | $100K | **$15M–$27M** |
| F3 | Monitor System Behavior | €5M (GDPR 2%) | $1M–$3M | $500K–$2M | $200K (manual monitoring) | $200K–$1M | $50K | **$7M–$11M** |
| F4 | Maintain Audit Compliance | €20M (GDPR 4%) | $2M–$5M (audit failure → contract loss) | $1M–$3M | $400K (manual reporting) | $500K–$1M | $100K | **$24M–$34M** |
| CAD-CORE | Evaluate CAD Files | $0 | $8M–$20M (quote velocity) | $3M–$10M | $2M (engineer time) | $200K–$1M | $300K | **$13M–$33M** |
| SD-1 | LMM Buy/Build Decision | $0 | $5M–$15M (wrong bet) | $2M–$8M | $100K (analysis paralysis) | $0 | $0 | **$7M–$23M** |
| E1 | Confidence in Security | $0 | $1M–$3M (adoption drag) | $500K–$2M | $0 | $200K–$1M | $500K–$1.5M | **$2M–$8M** |

### CoND Thresholds

| Total Annual CoND | Action |
|-------------------|--------|
| >$20M | Must build — executive escalation if deferred |
| $10M–$20M | Should build — fund in next quarter |
| $5M–$10M | Could build — evaluate against other opportunities |
| <$5M | Won't build unless strategic alignment |

---

## 4. Dependency Mapping

### Dependency Rules

1. **Must jobs cannot be blocked by Could jobs.** If a Must job depends on a Could job, escalate the dependency.
2. **Emotional jobs (E) often depend on Functional jobs (F).** E1 (Confidence) requires F1 (Secure Input) to be demonstrably working.
3. **Social jobs (S) depend on both F and E.** S1 (Industry Leadership) requires F1–F4 + E1–E2 to be operational and evidenced.
4. **Strategic decisions (SD) are upstream of most jobs.** SD-1 (LMM Strategy) gates SD-2, SD-3, CAD-HIST, and CAD-VLM.

### Dependency Graph

```
SD-1 (LMM Strategy) ──┬──► SD-2 (Historical Data Pipeline)
                      │       └──► CAD-HIST (Learn from History)
                      │       └──► Drift Detection Baselines
                      │       └──► Golden Eval Sets
                      ├──► SD-3 (Governance Gap Resolution)
                      │       └──► ISO 42001 Certification
                      │       └──► EU AI Act Art. 10 Compliance
                      └──► CAD-VLM (Visual Understanding)
                              └──► Fine-tuned vision model

F1 (Secure Input) ────┬──► F2 (Adversarial Defense)
                      │       └──► F3 (Runtime Monitoring)
                      │               └──► F4 (Audit & Compliance)
                      └──► E1 (Confidence in Security)
                              └──► S1 (Industry Leadership)

F4 (Audit Compliance) ──► E2 (Trust in Compliance)
                              └──► S2 (Responsible Innovation)

CAD-CORE (DFM Evaluation) ──► CAD-VLM (Visual Understanding)
                                    └──► CAD-HIST (Historical Learning)
```

### Sequencing Recommendation

| Phase | Jobs | Rationale |
|-------|------|-----------|
| **Phase 0 (Now)** | SD-1 decision + F1 + F2 + F3 + F4 | Security foundation + strategic direction |
| **Phase 1 (Months 1–6)** | SD-2 pipeline + SD-3 governance + CAD-CORE | Build data flywheel + close governance gaps + core revenue feature |
| **Phase 2 (Months 6–18)** | CAD-VLM + CAD-HIST + E1 (measured) | Differentiation + moat + adoption validation |
| **Phase 3 (Months 18+)** | S1 + S2 + E2 + E3 | Market positioning + compliance culture + risk maturity |

---

## 5. Acceptance Criteria Library

### Purpose

Reusable, measurable "done" definitions for each job type. The funnel intake references these rather than generating acceptance criteria from scratch.

### Criteria by Job Type

#### Security Jobs (F1, F2)

| Criterion | Threshold | Measurement Method | Eval Dataset | Owner |
|-----------|-----------|-------------------|--------------|-------|
| Coverage | >99.9% of inputs sanitized/defended | Automated regression test | Production traffic sample | Security Eng |
| Latency | p99 <10ms (F1); p99 <15ms per layer (F2) | Load test | Production-like traffic | Platform Eng |
| Detection rate | >98% adversarial detection | Red-teaming suite | 10,000 adversarial examples | Security Eng |
| False positive rate | <1% legitimate requests blocked | Production telemetry | 30-day production sample | Product Manager |
| Explainability | 100% of blocked inputs have reason code | Audit log review | Random sample of 1,000 blocks | Compliance |
| Zero successful attacks | Zero confirmed breaches | Incident review | All security incidents | CISO |

#### Monitoring Jobs (F3)

| Criterion | Threshold | Measurement Method | Eval Dataset | Owner |
|-----------|-----------|-------------------|--------------|-------|
| Coverage | 100% of AI services monitored | Infrastructure audit | All service endpoints | SRE |
| Alert latency | <30 seconds from anomaly to alert | Chaos engineering | Injected anomalies | SRE |
| Detection rate | >90% of known anomaly types detected | Labeled anomaly dataset | 5,000 labeled events | ML Engineer |
| False positive rate | <5% of alerts are false positives | Alert review | 30-day alert sample | SRE |
| Uptime | 99.9% monitoring system availability | Uptime monitoring | Continuous | SRE |

#### Compliance Jobs (F4)

| Criterion | Threshold | Measurement Method | Eval Dataset | Owner |
|-----------|-----------|-------------------|--------------|-------|
| Event capture | 100% of AI system activities logged | Log completeness audit | 30-day production logs | Compliance |
| Tamper evidence | 100% of logs have verifiable integrity hash | Cryptographic verification | Random sample of 10,000 logs | Security Eng |
| Logging latency | <100ms from event to persisted log | Performance test | High-volume event simulation | Platform Eng |
| Report accuracy | 100% of compliance reports match ground truth | Audit simulation | Quarterly audit dataset | Compliance |
| DSR response time | <30 days for data subject requests | Ticket tracking | All DSR tickets | DPO |
| Retention | 7-year retention with automated lifecycle | Policy audit | Retention policy review | Legal |

#### CAD AI Jobs (CAD-CORE, CAD-VLM, CAD-HIST)

| Criterion | Threshold | Measurement Method | Eval Dataset | Owner |
|-----------|-----------|-------------------|--------------|-------|
| Analysis time | <60 seconds end-to-end | Benchmark | 1,000 typical parts | ML Engineer |
| Feature precision | >95% vs. expert engineer review | Expert comparison | 500 labeled designs | Domain Expert |
| DFM coverage | 100% of ProtoLabs guidelines covered | Ruleset audit | All DFM guidelines | Domain Expert |
| Design iteration reduction | 40% fewer iterations | A/B test | Pilot cohort vs. control | Product Manager |
| User satisfaction | >4.0/5.0 for explanations | Survey | All pilot users | UX Research |
| VLM accuracy | >90% visual DFM assessment | Expert review | 500 visual cases | Domain Expert |
| Similarity search | <100ms top-5 retrieval | Benchmark | 10,000 design index | ML Engineer |
| Historical improvement | 20% accuracy lift with historical data | A/B test | Historical vs. baseline model | ML Engineer |

#### Emotional Jobs (E1–E3)

| Criterion | Threshold | Measurement Method | Eval Dataset | Owner |
|-----------|-----------|-------------------|--------------|-------|
| Trust score | ≥4.0/5.0 on quarterly survey | Survey | All affected users | UX Research |
| Override rate | <5% of AI recommendations overridden | Production telemetry | First 1,000 recommendations | Product Manager |
| Support tickets | <10% reduction in security-related tickets | Ticket analysis | Quarterly comparison | Support Lead |
| Attrition rate | No increase in security-team attrition | HR data | Quarterly comparison | HR |

#### Social Jobs (S1–S2)

| Criterion | Threshold | Measurement Method | Eval Dataset | Owner |
|-----------|-----------|-------------------|--------------|-------|
| Win rate | ≥60% against Xometry on security-evaluated deals | Win/loss analysis | All competitive deals | Sales Ops |
| NPS delta | ≥+10 points vs. baseline | NPS survey | Quarterly customer survey | Customer Success |
| Industry recognition | 1+ speaking invitation or award per year | PR tracking | Annual review | Marketing |

### Pre-Deployment Evaluation Gate

No job deploys to production without passing:

- [ ] All acceptance criteria for the job type are defined (from this library)
- [ ] Eval dataset exists and is versioned
- [ ] Automated test suite passes (regression + load + red-team)
- [ ] Fairness audit passes (no protected-group bias)
- [ ] Explainability review passes (per-persona requirements met)
- [ ] Load test passes (latency SLO met at projected scale)
- [ ] Stakeholder sign-off (the person who holds the job agrees criteria are sufficient)

---

## 6. Evidence Quality Rating

### Rating System

| Rating | Meaning | Criteria | Funnel Intake Action |
|--------|---------|----------|---------------------|
| 🟢 **Validated** | High confidence; build with confidence | ≥6 customer interviews, recency ≤90 days, + quant baseline + win/loss | Consume as-is; no discovery required |
| 🟡 **Partial** | Medium confidence; some gaps | 3–5 interviews OR quant baseline only OR recency 90–180 days | Flag: "JTBD confidence medium — validate during pilot" |
| 🔴 **Inferred** | Low confidence; significant risk | <3 interviews, no quant data, OR recency >180 days | Flag: "Discovery sprint recommended before build commitment" |
| ⚫ **Assumed** | No evidence; speculative | No interviews, no data, purely theoretical | Block: "Cannot proceed without evidence — run discovery sprint" |

### Evidence Quality by JTBD

| JTBD ID | Job | Interviews (n) | Recency (days) | Quant Baseline | Win/Loss | **Rating** | **Action** |
|---------|-----|----------------|----------------|----------------|----------|------------|------------|
| F1 | Secure AI Input Processing | 8 | 45 | ✅ Security audit | ✅ Incident review | 🟢 Validated | Build |
| F2 | Defend Against Adversarial Attacks | 6 | 60 | ✅ Pen-test results | ✅ Threat intel | 🟢 Validated | Build |
| F3 | Monitor System Behavior | 4 | 90 | ✅ Uptime data | ❌ None | 🟡 Partial | Validate during pilot |
| F4 | Maintain Audit Compliance | 5 | 120 | ✅ Audit findings | ❌ None | 🟡 Partial | Validate during pilot |
| CAD-CORE | Evaluate CAD Files | 12 | 30 | ✅ Quote velocity data | ✅ Win/loss | 🟢 Validated | Build |
| CAD-VLM | Visual Understanding | 3 | 180 | ❌ None | ❌ None | 🔴 Inferred | Discovery sprint |
| CAD-HIST | Learn from History | 2 | 200 | ❌ None | ❌ None | ⚫ Assumed | Discovery sprint |
| SD-1 | LMM Buy/Build Decision | 10 | 60 | ✅ Market analysis | ✅ Vendor evals | 🟢 Validated | Decide |
| E1 | Confidence in Security | 4 | 90 | ❌ None | ❌ None | 🟡 Partial | Validate during pilot |
| E2 | Trust in Compliance | 3 | 150 | ❌ None | ❌ None | 🔴 Inferred | Discovery sprint |

### Discovery Sprint Template (for 🔴 and ⚫ jobs)

When a job is rated 🔴 or ⚫, the funnel intake emits a discovery sprint recommendation:

```markdown
### Discovery Sprint Required: [JTBD ID]

**Why:** Evidence quality is [🔴 Inferred / ⚫ Assumed]. Build commitment risks solving the wrong job or solving it poorly.

**Sprint Goal:** Validate the job statement, importance, and current satisfaction with target stakeholders.

**Activities:**
- [ ] 6 customer interviews (or internal stakeholder interviews for internal jobs)
- [ ] Quant baseline extraction (CRM, support tickets, usage analytics)
- [ ] Win/loss review (if customer-facing)
- [ ] Competitive benchmark (if differentiation job)

**Duration:** 2–3 weeks

**Success Bar:** Evidence quality improves to 🟡 or 🟢

**Kill Criterion:** No stakeholder confirms the job statement after 6 interviews
```

---

## 7. Funnel Intake Integration

### How the Funnel Intake Consumes This Framework

The funnel intake (`pl-funnel-intake` and `pl-agentic-tpm`) references this document as a knowledge source. It does NOT generate JTBDs from scratch. Instead:

1. **Parse** the use-case description for keywords that match JTBDs in this framework.
2. **Activate** the matching JTBDs — list which jobs this use case serves.
3. **Report** the pre-calculated scores (RICE, MoSCoW, CoND, Evidence Quality) for each activated job.
4. **Validate** that all activated Must jobs have 🟢 or 🟡 evidence quality.
5. **Gate** — if any activated Must job is 🔴 or ⚫, emit a discovery sprint recommendation and downgrade the verdict to RAT-FIRST or DEFER.
6. **Synthesize** — calculate the combined risk, cost, and readiness of the activated job portfolio.

### Box 1 — Problem & JTBDs (Funnel Intake Format)

```markdown
#### Box 1 — Problem & JTBDs

**1.1 Current-State Pain (use-case specific)**
[1–2 sentences quantifying the pain this use case addresses]

**1.2 Activated JTBDs (from JTBD Evaluation Framework)**

| JTBD ID | Job Statement | MoSCoW | Evidence Quality | RICE Score | CoND (annual) | Status |
|---------|--------------|--------|------------------|------------|---------------|--------|
| F1 | Secure AI Input Processing | Must | 🟢 Validated | 1,125 | $29M–$47M | Activated |
| CAD-CORE | Evaluate CAD Files for Manufacturability | Should | 🟢 Validated | 117 | $13M–$33M | Activated |
| E1 | Confidence in Security | Should | 🟡 Partial | 233 | $2M–$8M | Activated |

**1.3 JTBD Synthesis**
- **Must jobs activated:** [N] — all have 🟢/🟡 evidence quality? [Yes/No]
- **Should jobs activated:** [N]
- **Could jobs activated:** [N]
- **Combined annual CoND:** $[X]M–$[Y]M
- **Highest-risk activated job:** [JTBD ID] — [risk description]

**1.4 JTBD Evaluation Gate**

| Check | Result | Action if Failed |
|-------|--------|------------------|
| All Must jobs have 🟢 or 🟡 evidence quality | [Pass/Fail] | Downgrade verdict to RAT-FIRST; emit discovery sprint plan |
| All activated jobs have acceptance criteria from library | [Pass/Fail] | Flag: "Acceptance criteria incomplete — define before build" |
| No Won't jobs are activated | [Pass/Fail] | Flag scope conflict; require PM clarification |
| Combined CoND justifies investment vs. Box 3 ROI | [Pass/Fail] | Downgrade verdict to KILL or DEFER |

**1.5 Anti-JTBDs (Jobs This Use Case Must Not Threaten)**

| Anti-JTBD | Why Excluded | Risk if Included |
|-----------|-------------|------------------|
| "When I'm an engineer, I want AI to handle all client communication..." | Would eliminate advisory role | Identity threat → Critical resistance |

**1.6 Inversion Question (Munger)**
"What would have to be true for this NOT to work?" — one sentence.
```

---

## 8. Change Log

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-05-03 | AI Product | Initial framework: RICE, MoSCoW, CoND, Dependencies, Acceptance Criteria Library, Evidence Quality |

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Owner** | AI Product + Governance Committee |
| **Review Cadence** | Monthly or after every major discovery sprint |
| **Next Review** | 2026-06-03 |
| **Classification** | Internal Use — Strategic Planning |
| **Upstream Dependencies** | `README.md`, `jobs-to-be-done-framework.md`, `problem-statements.md` |
| **Downstream Consumers** | `pl-funnel-intake` skill, `pl-agentic-tpm` skill, roadmap planning |
