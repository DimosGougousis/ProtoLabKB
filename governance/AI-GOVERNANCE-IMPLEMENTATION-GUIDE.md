# ProtoLabs AI Governance Implementation Guide

> **Document Type:** Practical Implementation Roadmap
> **Version:** 1.0
> **Effective Date:** 2026-05-29
> **Owner:** Chief AI Officer (CAIO)
> **Approved By:** AI Governance Council
> **Review Cycle:** Quarterly
> **Next Review:** 2026-08-29
> **Classification:** Internal — Engineering & Operations

---

## 1. Purpose & Audience

This guide translates the **AI Governance Matrix** and **Governance Framework Architecture** into **actionable implementation steps** for every role in the ProtoLabs organization. It answers: *"What do I do, when, and how?"*

| Audience | Start Here |
|----------|-----------|
| **Executives / Board** | [Section 2: Executive Decision Timeline](#2-executive-decision-timeline) |
| **Product Managers** | [Section 3: Agent Lifecycle Governance](#3-agent-lifecycle-governance) |
| **Engineers** | [Section 4: Control Implementation Playbooks](#4-control-implementation-playbooks) |
| **Compliance / Audit** | [Section 5: Evidence Collection & Certification](#5-evidence-collection--certification-roadmap) |
| **Operations** | [Section 6: Runtime Operations](#6-runtime-operations) |
| **All Teams** | [Section 7: Quick-Start Checklists](#7-quick-start-checklists) |

---

## 2. Executive Decision Timeline

### 2.1 Phase Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    IMPLEMENTATION PHASES — 39-WEEK PROGRAM                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  PHASE 0: FOUNDATION          PHASE 1: P0 DEPLOY      PHASE 2: DECISIONS   │
│  Weeks 1–3                    Weeks 4–7                 Weeks 4–14           │
│  ┌─────────────────┐          ┌─────────────────┐      ┌─────────────────┐  │
│  │ Complete code    │          │ Deploy WP01-WP04│      │ Executive       │  │
│  │ Build infra      │          │ to production   │      │ approvals for   │  │
│  │ Create tests     │          │                 │      │ P1 initiatives  │  │
│  │ Resolve overlaps │          │                 │      │                 │  │
│  └─────────────────┘          └─────────────────┘      └─────────────────┘  │
│  Budget: $150K                Budget: $200K             Budget: $50K         │
│  Resources: 4 eng × 3wk      Resources: 4 eng × 4wk   Resources: exec time │
│                                                                              │
│  PHASE 3: P1 IMPLEMENTATIONS                                                │
│  Weeks 8–30                                                                  │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │ Zero-Trust │ Adversarial Commercial │ Insider Threat │ Nation-State  │   │
│  │ $500K-$1M  │ $300K-$500K           │ $200K-$300K    │ $500K-$2M     │   │
│  │ 90 days    │ 60 days               │ 120 days       │ 180 days      │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│  Budget: $1.5M–$3.5M                                                        │
│  Resources: 10–15 FTE                                                       │
│                                                                              │
│  TOTAL PROGRAM: $1.9M–$3.9M │ 39 weeks │ 18–23 engineers                    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 Executive Decision Points

| Week | Decision | Budget | Attendees | Options | Recommendation |
|:----:|----------|--------|-----------|---------|:--------------:|
| **1** | Approve Phase 0 foundation | $150K | CTO, CFO, VP Eng | Approve / Defer | ✅ Approve |
| **4** | Zero-Trust Architecture | $500K–$1M | CTO, CISO, CFO, VP Eng | Approve / Reject / Defer | Defer to Q3 |
| **6** | Adversarial Defense Commercial | $300K–$500K | CTO, CISO, VP Eng, AI Lead | Build / Buy / Hybrid | Hybrid |
| **10** | Insider Threat Program | $200K–$300K | CEO, CTO, CISO, VP HR, Legal | Approve w/ privacy / Reject | Approve w/ safeguards |
| **14** | Nation-State Countermeasures | $500K–$2M | Board, CEO, CTO, CISO, Legal | Approve / Reject / Defer | Board decision |

### 2.3 Budget Summary

| Category | Phase 0 | Phase 1 | Phase 2 | Phase 3 | **Total** |
|----------|---------|---------|---------|---------|-----------|
| **Duration** | 3 weeks | 4 weeks | 10 weeks | 22 weeks | **39 weeks** |
| **Engineers** | 4 | 4 | 2 (analysis) | 10–15 | **18–23** |
| **Budget** | $150K | $200K | $50K | $1.5M–$3.5M | **$1.9M–$3.9M** |

---

## 3. Agent Lifecycle Governance

### 3.1 Lifecycle Stages & Gates

Every AI agent must pass through **5 governance gates** before and during production operation:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    AGENT LIFECYCLE GOVERNANCE FLOW                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌────────┐│
│  │ DISCOVERY│───►│   DEV    │───►│  DEPLOY  │───►│ OPERATE  │───►│RETIRE  ││
│  │          │    │          │    │          │    │          │    │        ││
│  │ • Intake │    │ • Build  │    │ • Gate   │    │ • Monitor│    │ • Gate ││
│  │ • Classify│   │ • Eval   │    │ • Approve│    │ • Drift  │    │ • Archive│
│  │ • Gate 1 │    │ • Gate 2 │    │ • Gate 3 │    │ • Gate 4 │    │ • Gate 5││
│  └──────────┘    └──────────┘    └──────────┘    └──────────┘    └────────┘│
│       │               │               │               │               │     │
│       ▼               ▼               ▼               ▼               ▼     │
│  Discovery       Development     Production      Continuous       End-of-  │
│  Gate            Gate            Release Gate    Monitoring       Life Gate │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3.2 Gate Requirements by Stage

#### Gate 1: Discovery Gate (Pre-Development)

| Requirement | Owner | Evidence | Timeline |
|-------------|-------|----------|:--------:|
| Agent tier classification completed | Policy Owner | `agent-tier-classification.yaml` | Day 1 |
| Context of use documented | Technical Owner | `ml-lifecycle-canvas.md` | Day 2 |
| Risk assessment initiated | Safety Officer | `risk-management-plan.md` (draft) | Day 3 |
| Policy Owner + Technical Owner assigned | CAIO | `policy-ownership-registry.yaml` | Day 1 |
| Input sanitization requirements defined | Security Engineer | `input-sanitization-requirements.md` | Day 3 |
| Data handling requirements documented | DPO | `data-governance-plan.md` (draft) | Day 5 |

**Gate Approver:** Technical Owner + Security  
**Gate SLA:** 5 business days from intake

#### Gate 2: Development Gate (Pre-Deployment)

| Requirement | Owner | Evidence | Timeline |
|-------------|-------|----------|:--------:|
| Model card completed | Technical Owner | `model-card.md` | Per agent |
| Eval suite passing (>90% accuracy) | Technical Owner | `*-eval-results.yaml` | Per agent |
| Adversarial testing completed | Security Engineer | `red-teaming-report.md` | Per agent |
| Source citation enforcement active | AI Engineer | `source-grounding-data-contract.yaml` | Per agent |
| Human oversight plan documented | Policy Owner | `human-oversight-plan.md` | Per agent |
| Bias & fairness assessment | AI Ethics Lead | `bias-and-fairness-evals.md` | Per agent |
| Safety Agent integration (Tier 2/3) | Safety Officer | `safety-agent-config.yaml` | Tier 2/3 only |
| Kill switch tested (Tier 2/3) | Safety Officer | `kill-switch-test-log.md` | Tier 2/3 only |
| Tool-use risk model documented (Tier 2/3) | Technical Owner | `tool-use-risk-model.yaml` | Tier 2/3 only |

**Gate Approver:** Technical Owner + Security (Tier 1) / Governance Council (Tier 2) / Council + Board (Tier 3)  
**Gate SLA:** 10 business days from development completion

#### Gate 3: Production Release Gate

| Requirement | Owner | Evidence | Timeline |
|-------------|-------|----------|:--------:|
| All Development Gate items ✅ | Technical Owner | Gate 2 checklist | Pre-requisite |
| CI/CD pipeline configured | DevOps | `deployment-pipeline.yaml` | Week of deploy |
| Monitoring dashboards active | Ops Engineer | Grafana dashboards | Week of deploy |
| Incident response playbook ready | Safety Officer | `ai-incident-report.md` template | Week of deploy |
| Team training completed | Policy Owner | Training certificates | Week of deploy |
| Hard guardrails configured (Tier 2/3) | Technical Owner | `hard-guardrails-config.yaml` | Tier 2/3 only |
| Kill switch drill passed (Tier 2/3) | Safety Officer | Drill results | Tier 2/3 only |

**Gate Approver:** Same as Development Gate  
**Gate SLA:** 5 business days from deployment readiness

#### Gate 4: Continuous Monitoring Gate (Ongoing)

| Requirement | Frequency | Owner | Evidence |
|-------------|:---------:|-------|----------|
| Performance KPIs within targets | Daily (automated) | Ops Engineer | Grafana alerts |
| Drift detection review | Weekly | Technical Owner | `drift-detection-report.md` |
| Kill switch drill | Monthly | Safety Officer | Drill results |
| Eval suite re-run | Quarterly | Technical Owner | `*-eval-results.yaml` |
| Bias & fairness re-assessment | Quarterly | AI Ethics Lead | `bias-and-fairness-evals.md` |
| KB freshness check | Quarterly | Knowledge Manager | KB update log |
| Internal audit | Semi-annual | DPO | Audit report |
| Governance Council review | Monthly | CAIO | Council minutes |

**Gate Action:** If any check fails → trigger incident response → escalate per severity matrix

#### Gate 5: End-of-Life Gate (Retirement)

| Requirement | Owner | Evidence |
|-------------|-------|----------|
| Retirement justification documented | Policy Owner | `retirement-justification.md` |
| Data retention/deletion plan | DPO | `data-retention-plan.md` |
| Client notification (if customer-facing) | VP Product | Notification records |
| Knowledge archival | Knowledge Manager | Archive confirmation |
| Audit trail preserved | Compliance Officer | Archive confirmation |
| Governance Council approval | CAIO | Council minutes |

---

## 4. Control Implementation Playbooks

### 4.1 GC-01: Model Card

**What:** Standardized documentation of every AI model's purpose, training data, performance, limitations, and ethical considerations.

**How to implement:**

```yaml
# model-card-template.yaml
model_card:
  agent_id: "{{agent-id}}"
  agent_name: "{{agent-name}}"
  version: "{{version}}"
  tier: 1|2|3
  
  purpose:
    description: "What this agent does and why"
    intended_use: "Primary use cases"
    out_of_scope: "What this agent should NOT be used for"
  
  training_data:
    sources:
      - name: "Knowledge base articles"
        url: "knowledge/{{folder}}/"
        last_updated: "YYYY-MM-DD"
      - name: "Golden dataset"
        records: N
        coverage: "Process types, materials, geometries"
    preprocessing: "How data was cleaned and prepared"
  
  performance:
    accuracy: "{{percentage}}%"
    eval_dataset: "{{dataset-name}}"
    eval_date: "YYYY-MM-DD"
    metrics:
      - name: "Precision"
        value: "{{value}}"
      - name: "Recall"
        value: "{{value}}"
      - name: "F1"
        value: "{{value}}"
  
  limitations:
    - "Known limitation 1"
    - "Known limitation 2"
  
  ethical_considerations:
    bias_assessment: "Completed / Not Required"
    fairness_eval: "link to eval results"
  
  owners:
    policy_owner: "{{name}}"
    technical_owner: "{{name}}"
    safety_officer: "{{name}}"
  
  review:
    last_review: "YYYY-MM-DD"
    next_review: "YYYY-MM-DD"
    review_cadence: "Quarterly"
```

**Owner:** Technical Owner  
**Timeline:** 2 days per agent  
**Evidence location:** `agents/{{agent-id}}/model-card.yaml`

---

### 4.2 GC-02: Eval Suite

**What:** Automated evaluation of agent accuracy, safety, and fairness against a golden dataset.

**How to implement:**

1. **Create golden dataset** — Minimum 100 test cases per process type covering:
   - Standard cases (happy path)
   - Edge cases (unusual geometries, rare materials)
   - Adversarial cases (injection attempts, malformed inputs)
   - Bias cases (demographic-neutral test scenarios)

2. **Define evaluation metrics:**
   - Accuracy: >90% (Tier 1), >93% (Tier 2), >98% (Tier 3)
   - Latency: <500ms (Tier 1), <200ms (Tier 2), <100ms (Tier 3)
   - False positive rate: <2% (Tier 1), <1% (Tier 2), <0.5% (Tier 3)

3. **Automate in CI/CD:**
   ```yaml
   # .github/workflows/agent-eval.yml
   name: Agent Evaluation
   on:
     pull_request:
       paths: ['agents/**']
     schedule:
       - cron: '0 6 * * 1'  # Weekly Monday 6am
   
   jobs:
     evaluate:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v4
         - name: Run eval suite
           run: python eval/run_eval.py --agent ${{ matrix.agent }} --threshold 0.90
         - name: Upload results
           uses: actions/upload-artifact@v4
           with:
             name: eval-results-${{ matrix.agent }}
             path: eval/results/
   ```

4. **Store results** in `eval/results/{{agent-id}}-{{date}}.yaml`

**Owner:** Technical Owner  
**Timeline:** 1 week per agent (initial), 1 day (re-run)  
**Evidence location:** `eval/results/`

---

### 4.3 GC-03: Input Sanitization

**What:** Validate, sanitize, and secure all inputs before AI processing.

**Implementation layers:**

| Layer | Check | Action on Failure |
|-------|-------|-------------------|
| **L0: Schema** | File type, size, encoding | Reject with error message |
| **L1: Pattern** | Regex for injection patterns | Log + reject |
| **L2: Semantic** | NLP intent analysis | Flag for human review |
| **L3: Behavioral** | User/session anomaly | Rate limit + alert |
| **L4: Output** | Response validation | Block + log |

**Owner:** Security Engineer  
**Timeline:** 1 week (deployment after Phase 0 code completion)  
**Evidence location:** `input-sanitization.md`, `input-validation-schema.json`

---

### 4.4 GC-04: Human Oversight Plan

**What:** Define exactly when and how humans review or approve AI outputs.

**Template by tier:**

| Tier | Oversight Model | Implementation |
|:----:|----------------|----------------|
| **1** | Advisory — human always decides | Display AI recommendation with confidence score; human clicks "Accept" or "Override" |
| **2** | Conditional — human approves exceptions | AI acts automatically within bounds; human approval required for: out-of-bounds values, high-value quotes, safety-adjacent decisions |
| **3** | Exception-based — human oversees by exception | AI acts autonomously within hard guardrails; human alerted only on: guardrail breach, anomaly detection, Safety Agent escalation |

**Owner:** Policy Owner  
**Timeline:** 3 days per agent  
**Evidence location:** `agents/{{agent-id}}/human-oversight-plan.md`

---

### 4.5 GC-05: Kill Switch

**What:** Emergency stop mechanism that halts all AI agent actions immediately.

**Requirements:**

| Tier | Activation Time | Scope | Auto Safe-State | Monthly Drill |
|:----:|:--------------:|-------|:---------------:|:-------------:|
| **2** | <30 seconds | Single agent | Return to last known good state | Required |
| **3** | <5 seconds | Single agent + dependent agents | Machine safe-state (stop motors, close valves) | Required |

**Implementation checklist:**
- [ ] Kill switch API endpoint defined (`POST /api/v1/agents/{id}/kill`)
- [ ] Safety Officer has independent activation authority
- [ ] Activation triggers immediate audit log entry
- [ ] Dependent agents receive cascade stop signal (Tier 3)
- [ ] Monthly drill scheduled and tracked
- [ ] Drill results documented with activation time measurement

**Owner:** Safety Officer  
**Timeline:** 2 days per agent (Tier 2/3)  
**Evidence location:** `kill-switch-specification.md`, `kill-switch-drill-log.md`

---

### 4.6 GC-13: Safety Agent Integration

**What:** Independent Governor agent that validates all Tier 2/3 actions before execution.

**Architecture:**

```
┌─────────────────────────────────────────────────────────────┐
│                    SAFETY AGENT ARCHITECTURE                  │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  User Request ──► Primary Agent ──► Safety Agent ──► Execute │
│                                      (Governor)              │
│                                         │                    │
│                                    ┌────┴────┐               │
│                                    │ VALIDATE │               │
│                                    ├─────────┤               │
│                                    │ • Bounds │               │
│                                    │ • Safety │               │
│                                    │ • Policy │               │
│                                    │ • Budget │               │
│                                    └─────────┘               │
│                                         │                    │
│                                    ┌────┴────┐               │
│                                    │ DECISION │               │
│                                    ├─────────┤               │
│                                    │ ✅ PASS  │──► Execute    │
│                                    │ ❌ FAIL  │──► Block + Log│
│                                    │ ⚠️ ESCAL │──► Human      │
│                                    └─────────┘               │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Validation checks:**
1. **Parametric bounds** — Is the action within defined limits?
2. **Safety constraints** — Does the action violate any safety rule?
3. **Policy compliance** — Does the action comply with governance policy?
4. **Budget limits** — Is the action within cost/usage bounds?
5. **Rate limits** — Has the agent exceeded action frequency?

**Owner:** Safety Officer  
**Timeline:** 1 week per Tier 2/3 agent  
**Evidence location:** `safety-agent-config.yaml`, `safety-agent-validation-logs/`

---

### 4.7 GC-15: Hard Guardrails

**What:** Non-negotiable boundaries that the AI system cannot override.

**Guardrail types:**

| Type | Description | Example |
|------|-------------|---------|
| **Parametric** | Numeric bounds on values | Feed rate: 10%–120% of nominal |
| **Temporal** | Time-based restrictions | No production scheduling during maintenance (02:00–06:00) |
| **Functional** | Actions the agent cannot perform | Cannot modify safety PLC logic |
| **Spatial** | Physical zone restrictions | Robot movement bounded by ISO 10218 zones |
| **Dependency** | Prerequisites that must be met | Material confirmation required before scheduling |
| **Financial** | Cost/pricing boundaries | Quote cannot exceed margin bounds |

**Implementation:**
```yaml
# hard-guardrails-config.yaml
guardrails:
  agent_id: "{{agent-id}}"
  tier: 2|3
  
  parametric:
    - name: "feed_rate"
      min: 0.10  # 10% of nominal
      max: 1.20  # 120% of nominal
      unit: "ratio"
      violation_action: "block_and_alert"
    
    - name: "quote_amount"
      min: 100
      max: 1000000
      unit: "USD"
      violation_action: "escalate_to_human"
  
  temporal:
    - name: "maintenance_window"
      blocked_hours: "02:00-06:00"
      timezone: "UTC"
      violation_action: "block_and_alert"
  
  functional:
    - name: "safety_plc"
      blocked_actions: ["write", "configure", "update"]
      violation_action: "block_and_alert_and_kill"
  
  financial:
    - name: "margin_bounds"
      min_margin_pct: 15
      max_discount_pct: 25
      violation_action: "escalate_to_human"
```

**Owner:** Technical Owner + Safety Officer  
**Timeline:** 3 days per agent (Tier 2/3)  
**Evidence location:** `hard-guardrails-config.yaml`

---

## 5. Evidence Collection & Certification Roadmap

### 5.1 ISO/IEC 42001 Certification Timeline

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ISO 42001 CERTIFICATION ROADMAP                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Q2 2026          Q3 2026          Q4 2026          Q1 2027                 │
│  ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐           │
│  │ GAP      │────►│ REMEDIATE│────►│ PRE-     │────►│ CERTIFY  │           │
│  │ ANALYSIS │     │          │     │ AUDIT    │     │          │           │
│  │          │     │          │     │          │     │          │           │
│  │ • Current│     │ • Close  │     │ • Mock   │     │ • Stage 1│           │
│  │   state  │     │   gaps   │     │   audit  │     │   (docs) │           │
│  │ • Target │     │ • Build  │     │ • Fix    │     │ • Stage 2│           │
│  │   state  │     │   evidence│    │   findings│    │   (ops)  │           │
│  │ • Gap    │     │ • Train  │     │ • Final  │     │ • Cert   │           │
│  │   report │     │   teams  │     │   prep   │     │   issued │           │
│  └──────────┘     └──────────┘     └──────────┘     └──────────┘           │
│  65% ready        80% ready        90% ready        95%+ ready             │
│                                                                              │
│  Certification Body: TÜV SÜD or BSI                                         │
│  Scope: AI-powered manufacturing intelligence (DFM, quoting, production)    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 5.2 Evidence Collection Schedule

| Evidence Artifact | Collection Frequency | Owner | Storage Location |
|-------------------|:-------------------:|-------|-----------------|
| Model cards | Per agent release | Technical Owner | `agents/{{id}}/model-card.yaml` |
| Eval results | Weekly (automated) | CI/CD pipeline | `eval/results/` |
| Kill switch drill logs | Monthly | Safety Officer | `ops/kill-switch-drills/` |
| Drift detection reports | Weekly | Technical Owner | `ops/drift-reports/` |
| Incident reports | Per incident | Safety Officer | `ops/incidents/` |
| Internal audit reports | Semi-annual | DPO | `governance/audits/` |
| Governance Council minutes | Monthly | CAIO | `governance/council-minutes/` |
| Bias & fairness evals | Quarterly | AI Ethics Lead | `eval/bias-fairness/` |
| KB freshness reports | Quarterly | Knowledge Manager | `knowledge/freshness/` |
| Training certificates | Per training event | HR / Policy Owner | `governance/training/` |
| Hard guardrail configs | Per change | Technical Owner | `agents/{{id}}/hard-guardrails-config.yaml` |
| Safety Agent validation logs | Continuous (automated) | Safety Agent | `ops/safety-agent-logs/` |

### 5.3 Audit Readiness Checklist

**Pre-Audit (2 weeks before):**
- [ ] All model cards up to date
- [ ] Eval results current (within 1 week)
- [ ] Kill switch drill logs current (within 1 month)
- [ ] Incident reports complete and closed
- [ ] Governance Council minutes available
- [ ] Training certificates on file
- [ ] Hard guardrail configs documented
- [ ] Safety Agent logs accessible
- [ ] RACI matrix current
- [ ] Policy review completed

**During Audit:**
- [ ] Auditor access to evidence repository
- [ ] Technical Owner available for walkthroughs
- [ ] Safety Officer available for kill switch demonstration
- [ ] Live system demonstration capability
- [ ] Interview availability for key roles

---

## 6. Runtime Operations

### 6.1 Daily Operations Checklist

| Time | Activity | Owner | Tool |
|------|----------|-------|------|
| 08:00 | Review overnight alerts | Ops Engineer | Grafana |
| 09:00 | Check agent health status | Ops Engineer | Health dashboard |
| 10:00 | Review incident queue | Safety Officer | Incident tracker |
| Ongoing | Monitor latency/error KPIs | Automated | Prometheus alerts |
| Ongoing | Safety Agent validation logs | Automated | Safety Agent dashboard |
| 17:00 | Daily ops summary | Ops Engineer | Slack #ai-ops |

### 6.2 Weekly Operations

| Day | Activity | Owner |
|-----|----------|-------|
| Monday | Drift detection review | Technical Owner |
| Tuesday | Eval suite re-run (automated) | CI/CD |
| Wednesday | Guardrail breach review | Safety Officer |
| Thursday | KB freshness spot-check | Knowledge Manager |
| Friday | Weekly ops report | Ops Engineer |

### 6.3 Monthly Operations

| Activity | Owner | Evidence |
|----------|-------|----------|
| Kill switch drill | Safety Officer | Drill results |
| Performance KPI review | Technical Owner | KPI report |
| Incident trend analysis | Safety Officer | Trend report |
| Governance Council meeting | CAIO | Council minutes |
| Guardrail effectiveness review | Technical Owner | Guardrail report |

### 6.4 Quarterly Operations

| Activity | Owner | Evidence |
|----------|-------|----------|
| Eval suite comprehensive re-run | Technical Owner | Eval results |
| Bias & fairness re-assessment | AI Ethics Lead | Bias report |
| KB freshness audit | Knowledge Manager | Freshness report |
| Model card review & update | Technical Owner | Updated model cards |
| Governance policy review | CAIO | Policy update log |
| ISO 42001 readiness assessment | DPO | Readiness scorecard |

---

## 7. Quick-Start Checklists

### 7.1 New Agent Onboarding Checklist

**Before writing any code:**
- [ ] Agent tier classification completed (`agent-tier-classification.yaml`)
- [ ] Policy Owner assigned and accepted
- [ ] Technical Owner assigned and accepted
- [ ] Context of use documented (`ml-lifecycle-canvas.md`)
- [ ] Data handling requirements documented (`data-governance-plan.md`)
- [ ] Input sanitization requirements defined

**During development:**
- [ ] Model card created (`model-card.md`)
- [ ] Eval suite created with golden dataset
- [ ] Source citation enforcement implemented
- [ ] Human oversight plan documented
- [ ] Bias & fairness assessment planned

**Before deployment (Tier 1):**
- [ ] Eval suite passing (>90% accuracy)
- [ ] Adversarial testing completed
- [ ] CI/CD pipeline configured
- [ ] Monitoring dashboard created
- [ ] Incident response playbook ready
- [ ] Team training completed
- [ ] Development Gate approved

**Before deployment (Tier 2/3 — additional):**
- [ ] Safety Agent integration tested
- [ ] Kill switch implemented and tested
- [ ] Hard guardrails configured
- [ ] Tool-use risk model documented
- [ ] Kill switch drill passed
- [ ] Governance Council approval obtained
- [ ] Board approval obtained (Tier 3 only)

### 7.2 Incident Response Checklist

**Immediate (0–15 minutes):**
- [ ] Severity classified (Sev1/2/3/4)
- [ ] Kill switch activated if safety risk (Safety Officer — no approval needed)
- [ ] Affected systems identified
- [ ] Initial containment applied

**Short-term (15 minutes – 4 hours):**
- [ ] Root cause investigation started
- [ ] Stakeholders notified per escalation matrix
- [ ] Client notification prepared (if customer-facing)
- [ ] Evidence preserved (logs, configs, state)

**Resolution (4 hours – 7 days):**
- [ ] Root cause identified
- [ ] Fix implemented and tested
- [ ] Eval suite updated with regression test
- [ ] Post-incident review completed
- [ ] Governance Council briefed (Sev1/2)

**Follow-up (7–30 days):**
- [ ] Corrective actions implemented
- [ ] Eval suite re-run to confirm fix
- [ ] Lessons learned documented
- [ ] Governance policy updated (if needed)

### 7.3 Quarterly Review Checklist

- [ ] All agent eval suites re-run — results within targets
- [ ] All kill switch drills completed — activation times within SLA
- [ ] All drift detection reports reviewed — no unaddressed drift
- [ ] All bias & fairness evals completed — no significant bias
- [ ] All model cards reviewed and updated
- [ ] All KB articles freshness checked
- [ ] All incident reports closed
- [ ] Governance Council minutes documented
- [ ] ISO 42001 readiness scorecard updated
- [ ] Risk register reviewed and updated
- [ ] Third-party vendor assessments current
- [ ] Training certificates current

---

## 8. Escalation Contacts

| Issue Type | Primary Contact | Secondary Contact | Escalation Path |
|------------|-----------------|-------------------|-----------------|
| **Technical Blockers** | VP Engineering | CTO | CEO |
| **Resource Constraints** | VP Engineering | CFO | CEO |
| **Security Incidents** | CISO | CTO | CEO + Legal |
| **Compliance Issues** | General Counsel | CISO | CEO + Board |
| **Budget Approval** | CFO | CEO | Board |
| **Vendor Issues** | Procurement | VP Engineering | CFO |
| **Privacy Concerns** | General Counsel | VP HR | CEO |
| **Safety Incidents** | Safety Officer | CAIO | Board (24h) |
| **Kill Switch Activation** | Safety Officer | CAIO | Board (24h) |

---

## 9. Tool & Platform Reference

| Tool | Purpose | Access | Owner |
|------|---------|--------|-------|
| **Grafana** | Monitoring dashboards | `grafana.protolabs.internal` | Ops Engineering |
| **Prometheus** | Metrics collection | Internal | Ops Engineering |
| **OPA/Cedar** | Policy-as-Code engine | Internal | Security Engineering |
| **GitHub Actions** | CI/CD pipeline | `github.com/protolabs` | DevOps |
| **Confluence** | Documentation | `confluence.protolabs.internal` | Knowledge Management |
| **Jira** | Issue tracking | `jira.protolabs.internal` | All teams |
| **Slack** | Communication | `protolabs.slack.com` | All teams |
| **Vault** | Secrets management | Internal | Security Engineering |

---

## 10. Document Cross-Reference

| Document | Location | Purpose |
|----------|----------|---------|
| AI Governance Matrix | `governance/AI-GOVERNANCE-MATRIX.md` | Cross-reference of all controls, agents, and frameworks |
| AI Governance Policy | `governance/ai-governance-policy.md` | Enterprise policy entry point |
| Governance Framework Architecture | `docs/governance-framework-architecture.md` | Board-level architecture reference |
| Governance by Stage Framework | `docs/governance-by-stage-framework.md` | Client journey governance gates |
| ISO 42001 Gap Analysis | `docs/iso-42001-gap-analysis.md` | Certification readiness |
| Governance Framework Mapping | `ai-implementation-workstreams/GOVERNANCE-FRAMEWORK-MAPPING.md` | WP-to-framework alignment |
| Implementation Workstreams Guide | `ai-implementation-workstreams/IMPLEMENTATION-GUIDE.md` | Work package implementation details |

---

## Appendix A: Glossary

| Term | Definition |
|------|------------|
| **AIMS** | AI Management System (per ISO/IEC 42001) |
| **CAIO** | Chief AI Officer |
| **DPA** | Data Processing Agreement |
| **DPIA** | Data Protection Impact Assessment |
| **DPO** | Data Protection Officer |
| **GC** | Governance Control |
| **MHA** | Meaningful Human Accountability |
| **MGF** | Model Governance Framework (Singapore) |
| **OT** | Operational Technology |
| **PaC** | Policy-as-Code |
| **PDCA** | Plan-Do-Check-Act |
| **PE** | Professional Engineer |
| **RACI** | Responsible, Accountable, Consulted, Informed |
| **RMF** | Risk Management Framework |
| **WP** | Work Package |

---

## Appendix B: Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-05-29 | AI Governance Office | Initial release — practical implementation companion to AI Governance Matrix |