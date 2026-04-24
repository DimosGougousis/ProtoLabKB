# Governance by Stage — Client Journey & Agentic Workflow

> **Purpose:** Maps every stage of the ProtoLabs client journey to mandatory governance requirements across NIST AI RMF, Agentic Governance 2026, Singapore MGF, and ISO/IEC 42001 (AI Management System). Defines risk controls, RACI accountability, and PDCA integration for each stage.

**Version:** 1.1  
**Last Updated:** 2026-04-24  
**Owner:** ProtoLabs AI Governance Office  
**Review Cycle:** Quarterly  
**ISO 42001 Certification Target:** Q1 2027  

---

## Executive Summary

Every client journey stage has **mandatory governance gates** that must be satisfied before progression. This document provides:

1. **Framework Mapping** — Which NIST AI RMF Functions, Agentic Governance tiers, Singapore MGF principles, and ISO 42001 clauses apply
2. **Risk Register** — Specific threats, likelihood, impact, and mitigations per stage
3. **RACI Matrix** — Clear accountability for every governance action
4. **Evidence Requirements** — What artifacts must exist to pass each gate
5. **ISO 42001 PDCA Thread** — How each stage maps to Plan-Do-Check-Act for certification

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    GOVERNANCE ARCHITECTURE OVERVIEW                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐ │
│   │   NIST AI   │    │  AGENTIC    │    │  SINGAPORE  │    │   PROTOCOL  │ │
│   │   RMF 1.0   │    │ GOVERNANCE  │    │    MGF      │    │   LABS RACI │ │
│   │             │    │    2026     │    │             │    │             │ │
│   │ • GOVERN    │    │ • Tier      │    │ • Hard      │    │ • Policy    │ │
│   │ • MAP       │    │   Classification│  Guardrails  │    │   Owner     │ │
│   │ • MEASURE   │    │ • Tool-Use  │    │ • Meaningful │    │ • Technical │ │
│   │ • MANAGE    │    │   Risk Model│    │   Human      │    │   Owner     │ │
│   │ • 7 Charact.│    │ • Safety    │    │   Accountability│  • Operational│ │
│   │             │    │   Agent     │    │ • Multi-Agent│    │   Owner     │ │
│   │             │    │             │    │   Coordination│   • Safety    │ │
│   │             │    │             │    │              │    │   Officer   │ │
│   └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘ │
│          │                  │                  │                  │          │
│          └──────────────────┴──────────────────┴──────────────────┘          │
│                                    │                                         │
│                         ┌──────────┴──────────┐                             │
│                         │   ISO/IEC 42001      │                             │
│                         │   AI MANAGEMENT      │                             │
│                         │      SYSTEM          │                             │
│                         │  ┌────┐┌────┐┌────┐┌────┐                         │
│                         │  │Plan││ Do ││Check││Act │                         │
│                         │  └────┘└────┘└────┘└────┘                         │
│                         │   (Certifiable — Q1 2027)                         │
│                         └─────────────────────────┘                         │
│                                    │                                         │
│                         ┌──────────┴──────────┐                             │
│                         │   GOVERNANCE GATES    │                             │
│                         │  (Discovery → Dev →   │                             │
│                         │   Deploy → Periodic)  │                             │
│                         └───────────────────────┘                             │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Stage 1: Discovery & Intake

### Stage Overview

| Attribute | Value |
|-----------|-------|
| **Primary Agents** | `{{dfm-router}}` (Tier 1 — Advisory) |
| **Human Touchpoints** | Client uploads CAD, describes part |
| **System Touchpoints** | Intake sanitization, risk classification |
| **Governance Gate** | **Discovery Gate** — Must pass before DFM analysis |

---

### 1.1 AI Framework Mapping

#### NIST AI RMF Functions

| Function | Category | Requirement | Evidence |
|----------|----------|-------------|----------|
| **GOVERN** | GV-1.1 | AI risk management policies established | `governance-charter.md` exists |
| **GOVERN** | GV-2.1 | Organizational roles defined | RACI matrix published |
| **GOVERN** | GV-3.1 | Workforce AI literacy | Training certificates on file |
| **MAP** | MP-1.1 | Context of use defined | `ml-lifecycle-canvas.md` completed |
| **MAP** | MP-2.1 | AI system categorized | Agent tier classification: **Tier 1** (Advisory) |
| **MAP** | MP-3.1 | Individual-level impacts assessed | Client data handling DPIA |
| **MAP** | MP-4.1 | Societal impacts considered | No high-risk societal impact (B2B manufacturing) |
| **MEASURE** | MS-1.1 | Evaluation methods selected | Input sanitization eval criteria defined |
| **MANAGE** | MG-1.1 | Risk response strategies defined | Escalation path for suspicious uploads |

#### NIST AI RMF — Seven Characteristics

| Characteristic | Assessment | Evidence Required |
|----------------|------------|-------------------|
| **Valid & Reliable** | Router accuracy >95% on process classification | `dfm-router-eval-results.yaml` |
| **Safe** | No physical actuation at this stage | N/A — advisory only |
| **Secure & Resilient** | Input sanitization active (WP01) | `input-sanitization.md` |
| **Accountable & Transparent** | Client notified AI is classifying their upload | `transparency-controls.md` |
| **Explainable & Interpretable** | Router decision logged with confidence score | `router-decision-log-schema.yaml` |
| **Privacy-Enhanced** | CAD file encrypted at rest, access logged | `customer-cad-ip-protection-guardrail.md` |
| **Fair** | No demographic data processed at intake | Bias assessment: N/A |

#### Agentic Governance 2026

| Element | Requirement | Evidence |
|---------|-------------|----------|
| **Autonomy Tier** | Tier 1 — Advisory (read-only, no actions) | `agent-tier-classification.yaml` |
| **Tool-Use Risk** | No tools invoked — classification only | Tool registry: empty |
| **Safety Agent** | Not required for Tier 1 | N/A |
| **Kill Switch** | Not required (no physical risk) | N/A |

#### Singapore MGF

| Principle | Implementation | Evidence |
|-----------|----------------|----------|
| **Hard Guardrails** | Input validation: file type, size, encoding | `input-validation-schema.json` |
| **Meaningful Human Accountability** | Policy owner: VP of Product | `policy-ownership-registry.yaml` |
| **Multi-Agent Coordination** | Single agent at this stage — no coordination needed | N/A |

#### ISO/IEC 42001 — PDCA Thread

| PDCA Phase | Clause | Application in Stage 1 | Evidence |
|------------|--------|------------------------|----------|
| **PLAN** | 4.1, 4.2, 6.1 | Establish intake context, identify interested parties (clients, regulators), assess intake risks | `ml-lifecycle-canvas.md`, `risk-management-plan.md` |
| **DO** | 8.1, 8.2 | Implement intake processes, apply input sanitization controls | `input-sanitization.md`, `input-validation-schema.json` |
| **CHECK** | 9.1 | Monitor router accuracy, intake error rates, client complaints | `dfm-router-eval-results.yaml`, incident logs |
| **ACT** | 10.2 | Improve intake based on feedback, update validation patterns | KB freshness updates, pattern library revisions |

**ISO 42001 Certification Note:** Stage 1 demonstrates **Clause 4 (Context)** and **Clause 6.1 (Risk Assessment)** evidence. The intake process is the first operational process auditors will examine.

---

### 1.2 Risk Register

| Risk ID | Threat | Likelihood | Impact | Mitigation | Owner |
|---------|--------|------------|--------|------------|-------|
| R-1.1 | Malicious CAD file (malware embedded) | Medium | High | WP01 input sanitization + sandboxed parsing | Security Engineer |
| R-1.2 | Prompt injection in part description | Medium | Medium | WP02 Layer 0-4 defense, output validation | AI Safety Engineer |
| R-1.3 | IP theft (CAD exfiltration) | Low | Critical | Encryption at rest, access logging, DLP | Data Protection Officer |
| R-1.4 | Incorrect process classification | Medium | Medium | Router eval >95%, human override available | ML Engineer |
| R-1.5 | Data retention violation | Low | High | Auto-deletion after 7 years, audit logs | Compliance Officer |

---

### 1.3 RACI Matrix — Discovery & Intake

| Activity | Policy Owner | Technical Owner | Operational Owner | Safety Officer | Client |
|----------|:----------:|:---------------:|:-----------------:|:------------:|:------:|
| Define intake policies | **A** | R | C | C | I |
| Implement input sanitization | C | **A** | I | R | I |
| Classify process & vertical | I | **A** | C | C | I |
| Assess risk tier | C | R | C | **A** | I |
| Approve Discovery Gate | **A** | R | C | R | I |
| Handle client data | I | R | **A** | C | C |
| Respond to incidents | **A** | R | R | R | I |

**Legend:** R = Responsible, A = Accountable, C = Consulted, I = Informed

---

### 1.4 Evidence Checklist — Discovery Gate

- [ ] `agent-tier-classification.yaml` — Tier 1 confirmed
- [ ] `input-sanitization.md` — WP01 active
- [ ] `dfm-router-eval-results.yaml` — >95% accuracy
- [ ] `transparency-controls.md` — AI disclosure active
- [ ] `customer-cad-ip-protection-guardrail.md` — CAD handling verified
- [ ] `policy-ownership-registry.yaml` — MHA assigned
- [ ] Incident response playbook — escalation path defined

---

## Stage 2: AI-Powered DFM Analysis

### Stage Overview

| Attribute | Value |
|-----------|-------|
| **Primary Agents** | `{{cnc-machining}}`, `{{injection-molding}}`, `{{sheet-metal}}`, `{{3d-printing}}` (Tier 1 — Advisory) |
| **Human Touchpoints** | PE review for complex parts, exception handling |
| **System Touchpoints** | DFM eval suite, KB article loader, citation enforcer |
| **Governance Gate** | **Development Gate** — Must pass before quote generation |

---

### 2.1 AI Framework Mapping

#### NIST AI RMF Functions

| Function | Category | Requirement | Evidence |
|----------|----------|-------------|----------|
| **GOVERN** | GV-4.1 | Risk tolerance defined | `ai-risk-appetite-framework.md` |
| **GOVERN** | GV-5.1 | Ongoing monitoring planned | `continuous-monitoring-plan.md` |
| **GOVERN** | GV-6.1 | Third-party resources identified | KB article sources documented |
| **GOVERN** | GV-7.1 | Model documentation complete | `model-card.md` per agent |
| **MAP** | MP-1.2 | Categorized as Tier 1 (Advisory) | `agent-tier-classification.yaml` |
| **MAP** | MP-2.2 | Risk tolerance for DFM accuracy | >90% accuracy required |
| **MEASURE** | MS-1.1 | Evaluation methods: golden dataset | `dfm-accuracy-eval-suite.yaml` |
| **MEASURE** | MS-2.1 | Pre-deployment evaluation | Eval results on file |
| **MEASURE** | MS-2.2 | Evaluation covers validity & reliability | Statistical variance report |
| **MEASURE** | MS-3.1 | Performance tracking active | Grafana dashboard configured |
| **MEASURE** | MS-4.1 | Output validation methods | Citation enforcement active |
| **MANAGE** | MG-2.1 | Incident response playbook | `ai-incident-report.md` template |
| **MANAGE** | MG-3.1 | Regular review cadence | Quarterly eval schedule |

#### NIST AI RMF — Seven Characteristics

| Characteristic | Assessment | Evidence Required |
|----------------|------------|-------------------|
| **Valid & Reliable** | DFM accuracy >90% on golden dataset | `dfm-accuracy-eval-suite.yaml` |
| **Safe** | Harm scenarios documented (wrong DFM → bad part) | `risk-management-plan.md` |
| **Secure & Resilient** | Adversarial testing passed (WP02) | `red-teaming-ai-systems.md` |
| **Accountable & Transparent** | Source citation enforced (KB + source_url) | `source-grounding-data-contract.yaml` |
| **Explainable & Interpretable** | RAG context displayed, decision traced | `transparency-controls.md` |
| **Privacy-Enhanced** | Customer CAD not used for model training | `data-governance-plan.md` |
| **Fair** | No bias in material recommendations | `bias-and-fairness-evals.md` |

#### Agentic Governance 2026

| Element | Requirement | Evidence |
|---------|-------------|----------|
| **Autonomy Tier** | Tier 1 — Advisory (recommendations only, no actions) | `agent-tier-classification.yaml` |
| **Tool-Use Risk** | Read-only KB access, no API calls | Tool registry: read-only |
| **Safety Agent** | Not required for Tier 1 | N/A |
| **Kill Switch** | Not required (no physical risk) | N/A |

#### Singapore MGF

| Principle | Implementation | Evidence |
|-----------|----------------|----------|
| **Hard Guardrails** | Output bounded to ProtoLabs capabilities only | `capability-boundary-config.yaml` |
| **Meaningful Human Accountability** | PE owns DFM policy correctness | `policy-ownership-registry.yaml` |
| **Multi-Agent Coordination** | Router → Specialist agent handoff logged | `delegation-chain-audit.md` |

#### ISO/IEC 42001 — PDCA Thread

| PDCA Phase | Clause | Application in Stage 2 | Evidence |
|------------|--------|------------------------|----------|
| **PLAN** | 6.2, 8.4 | Set DFM accuracy objectives (>90%), plan eval suite design, plan model documentation | `aims-objectives-and-kpis.md`, `eval-driven-development.md` |
| **DO** | 8.1, 8.4 | Develop specialist agents, run eval suites, enforce citations, build model cards | `model-card.md`, `dfm-accuracy-eval-suite.yaml`, `test-plan-for-ai.md` |
| **CHECK** | 9.1, 9.2 | Evaluate agent accuracy, conduct internal audit of model documentation, review eval results | `dfm-accuracy-eval-suite.yaml`, internal audit records |
| **ACT** | 10.1, 10.2 | Correct accuracy gaps, retrain models, update KB articles, improve eval coverage | Retraining pipeline, KB freshness updates |

**ISO 42001 Certification Note:** Stage 2 is the **core evidence zone** for auditors. `model-card.md` (Clause 7.5), `test-plan-for-ai.md` (Clause 8.4), and `dfm-accuracy-eval-suite.yaml` (Clause 9.1) are primary audit artifacts.

---

### 2.2 Risk Register

| Risk ID | Threat | Likelihood | Impact | Mitigation | Owner |
|---------|--------|------------|--------|------------|-------|
| R-2.1 | Hallucinated DFM recommendation | Medium | High | Golden dataset eval >90%, human PE review | ML Engineer |
| R-2.2 | Outdated KB article cited | Medium | Medium | KB freshness SLA (quarterly refresh) | Knowledge Manager |
| R-2.3 | Missing source citation | Medium | Medium | Automated citation enforcement | AI Engineer |
| R-2.4 | Bias in material recommendation | Low | Medium | Fairness eval, diverse test cases | AI Ethics Lead |
| R-2.5 | Adversarial prompt injection | Medium | High | WP02 5-layer defense active | Security Engineer |
| R-2.6 | Model drift over time | Medium | High | Quarterly revalidation, drift detection | MLOps Engineer |

---

### 2.3 RACI Matrix — DFM Analysis

| Activity | Policy Owner | Technical Owner | Operational Owner | Safety Officer | Client |
|----------|:----------:|:---------------:|:-----------------:|:------------:|:------:|
| Define DFM accuracy standards | **A** | R | C | C | I |
| Build eval suite (golden dataset) | C | **A** | I | C | I |
| Run pre-deployment evaluation | I | **A** | C | C | I |
| Approve Development Gate | **A** | R | C | R | I |
| Maintain KB articles | C | R | **A** | I | I |
| Handle DFM accuracy incidents | **A** | R | R | R | I |
| Conduct quarterly revalidation | C | **A** | C | C | I |

---

### 2.4 Evidence Checklist — Development Gate

- [ ] `model-card.md` — Complete for each specialist agent
- [ ] `dfm-accuracy-eval-suite.yaml` — >90% accuracy demonstrated
- [ ] `red-teaming-ai-systems.md` — Adversarial testing passed
- [ ] `source-grounding-data-contract.yaml` — Citation enforcement active
- [ ] `transparency-controls.md` — Explainability features live
- [ ] `risk-management-plan.md` — Harm scenarios documented
- [ ] `bias-and-fairness-evals.md` — No significant bias detected
- [ ] `continuous-monitoring-plan.md` — Drift detection configured

---

## Stage 3: Quote & Proposal

### Stage Overview

| Attribute | Value |
|-----------|-------|
| **Primary Agents** | `{{materials-selection}}` (Tier 1), Quote Bot (Tier 2 — Conditional) |
| **Human Touchpoints** | Account Manager validation, Pricing Team escalation |
| **System Touchpoints** | Financial guardrails, margin checks, approval tiers |
| **Governance Gate** | **Quote Approval Gate** — Must pass before client proposal |

---

### 3.1 AI Framework Mapping

#### NIST AI RMF Functions

| Function | Category | Requirement | Evidence |
|----------|----------|-------------|----------|
| **GOVERN** | GV-1.2 | Accountability structures for financial decisions | `governance-roles-raci.md` |
| **GOVERN** | GV-4.2 | Risk tolerance for pricing errors | Pricing variance threshold defined |
| **MAP** | MP-2.1 | Quote bot classified as **Tier 2** (Conditional Autonomy) | `agent-tier-classification.yaml` |
| **MAP** | MP-3.2 | Financial impact of incorrect quote | Business impact assessment |
| **MEASURE** | MS-1.2 | Pricing accuracy metrics | Quote variance <5% vs actual |
| **MEASURE** | MS-3.2 | Drift detection for pricing model | Monthly pricing accuracy review |
| **MEASURE** | MS-4.2 | Incident reporting for pricing errors | `ai-incident-report.md` |
| **MANAGE** | MG-1.2 | Risk treatment for pricing errors | Human approval for quotes >$X |
| **MANAGE** | MG-2.2 | Incident response for pricing errors | Escalation to Pricing Team |
| **MANAGE** | MG-2.4 | Kill switch for quote bot (30-second SLA) | `kill-switch-specification.md` |

#### NIST AI RMF — Seven Characteristics

| Characteristic | Assessment | Evidence Required |
|----------------|------------|-------------------|
| **Valid & Reliable** | Quote accuracy within 5% of actual cost | `quote-accuracy-eval.yaml` |
| **Safe** | No safety impact (financial only) | N/A |
| **Secure & Resilient** | Pricing data protected, tamper-evident | `audit-record-schema.yaml` |
| **Accountable & Transparent** | Quote breakdown shows AI vs human components | `transparency-controls.md` |
| **Explainable & Interpretable** | Quote logic explainable to client | `quote-explanation-template.md` |
| **Privacy-Enhanced** | Client pricing history access-controlled | `skill-manifest.yaml` RBAC |
| **Fair** | No discriminatory pricing | `bias-and-fairness-evals.md` |

#### Agentic Governance 2026

| Element | Requirement | Evidence |
|---------|-------------|----------|
| **Autonomy Tier** | Tier 2 — Conditional Autonomy (API calls to ERP, human approval for exceptions) | `agent-tier-classification.yaml` |
| **Tool-Use Risk** | ERP API read/write, bounded by financial guardrails | `tool-use-risk-model.yaml` |
| **Safety Agent** | Required — validates all Tier 2 actions | `safety-agent-config.yaml` |
| **Kill Switch** | Required — 30-second activation | `kill-switch-specification.md` |

#### Singapore MGF

| Principle | Implementation | Evidence |
|-----------|----------------|----------|
| **Hard Guardrails** | Parametric: quote cannot exceed margin bounds | `financial-guardrails-config.yaml` |
| **Hard Guardrails** | Functional: cannot modify pricing tables | `erp-access-control-policy.yaml` |
| **Meaningful Human Accountability** | VP of Sales owns pricing policy | `policy-ownership-registry.yaml` |
| **Multi-Agent Coordination** | Materials agent → Quote bot handoff validated | `delegation-chain-audit.md` |

#### ISO/IEC 42001 — PDCA Thread

| PDCA Phase | Clause | Application in Stage 3 | Evidence |
|------------|--------|------------------------|----------|
| **PLAN** | 6.1, 6.2 | Assess financial risks of automated quoting, set pricing accuracy objectives, define approval thresholds | `risk-management-plan.md`, `aims-objectives-and-kpis.md` |
| **DO** | 8.1, 8.2 | Implement quote bot with financial guardrails, integrate Safety Agent, configure kill switch, establish audit logging | `financial-guardrails-config.yaml`, `safety-agent-config.yaml`, `kill-switch-specification.md` |
| **CHECK** | 9.1, 9.2 | Monitor quote accuracy, audit financial guardrail effectiveness, review Tier 2 classification | `quote-accuracy-eval.yaml`, internal audit records |
| **ACT** | 10.1, 10.2 | Adjust guardrail thresholds, refine approval tiers, improve quote explanations based on disputes | `quote-explanation-template.md`, dispute resolution records |

**ISO 42001 Certification Note:** Stage 3 introduces **Tier 2 agent evidence** (Clause 8.2 risk treatment). The `tool-use-risk-model.yaml` and `safety-agent-config.yaml` demonstrate controlled AI system operation. Kill switch testing records are critical audit evidence.

---

### 3.2 Risk Register

| Risk ID | Threat | Likelihood | Impact | Mitigation | Owner |
|---------|--------|------------|--------|------------|-------|
| R-3.1 | Incorrect quote (underpricing) | Medium | High | Financial guardrails, human approval >threshold | Pricing Manager |
| R-3.2 | Incorrect quote (overpricing) | Medium | Medium | Margin checks, competitive benchmark | Pricing Manager |
| R-3.3 | Unauthorized pricing table modification | Low | Critical | RBAC, Safety Agent validation, audit logs | Security Engineer |
| R-3.4 | Quote bot API abuse | Low | High | Rate limiting, anomaly detection | Security Engineer |
| R-3.5 | Discriminatory pricing | Low | High | Fairness eval, pricing audit | Compliance Officer |

---

### 3.3 RACI Matrix — Quote & Proposal

| Activity | Policy Owner | Technical Owner | Operational Owner | Safety Officer | Client |
|----------|:----------:|:---------------:|:-----------------:|:------------:|:------:|
| Define pricing policy | **A** | C | R | C | I |
| Set financial guardrails | **A** | R | C | C | I |
| Implement quote bot | C | **A** | I | R | I |
| Validate Tier 2 classification | C | R | C | **A** | I |
| Configure Safety Agent | I | **A** | I | R | I |
| Approve Quote Approval Gate | **A** | R | R | R | I |
| Handle pricing disputes | **A** | I | R | I | C |
| Activate kill switch (if needed) | I | R | R | **A** | I |

---

### 3.4 Evidence Checklist — Quote Approval Gate

- [ ] `agent-tier-classification.yaml` — Tier 2 confirmed
- [ ] `tool-use-risk-model.yaml` — ERP API calls bounded
- [ ] `safety-agent-config.yaml` — Safety Agent integrated
- [ ] `kill-switch-specification.md` — 30-second kill switch tested
- [ ] `financial-guardrails-config.yaml` — Margin checks active
- [ ] `quote-accuracy-eval.yaml` — <5% variance demonstrated
- [ ] `audit-record-schema.yaml` — All quotes logged tamper-evidently
- [ ] `policy-ownership-registry.yaml` — VP of Sales MHA assigned

---

## Stage 4: Order Confirmation & Production

### Stage Overview

| Attribute | Value |
|-----------|-------|
| **Primary Agents** | `{{production-scheduler}}` (Tier 2 — Conditional) |
| **Human Touchpoints** | Production Manager approval, maintenance team |
| **System Touchpoints** | MES/ERP integration, hard guardrails, Safety Agent |
| **Governance Gate** | **Production Release Gate** — Must pass before shop floor |

---

### 4.1 AI Framework Mapping

#### NIST AI RMF Functions

| Function | Category | Requirement | Evidence |
|----------|----------|-------------|----------|
| **GOVERN** | GV-4.1 | Risk tolerance for production scheduling | Maintenance window policy |
| **GOVERN** | GV-5.2 | Supply chain risk management | Supplier risk assessment |
| **MAP** | MP-1.1 | Production context defined | `ml-lifecycle-canvas.md` — Production edition |
| **MAP** | MP-2.1 | Scheduler classified as **Tier 2** (Conditional) | `agent-tier-classification.yaml` |
| **MAP** | MP-3.1 | Worker safety impact assessed | ISO 10218 compliance check |
| **MEASURE** | MS-1.1 | Schedule optimization metrics | OEE improvement target |
| **MEASURE** | MS-2.1 | Safety validation before deployment | `safety-validation-report.md` |
| **MEASURE** | MS-3.1 | Real-time schedule monitoring | MES dashboard active |
| **MANAGE** | MG-1.1 | Risk response for schedule conflicts | Conflict resolution playbook |
| **MANAGE** | MG-2.1 | Incident response for production errors | `ai-incident-report.md` |
| **MANAGE** | MG-2.4 | Kill switch for scheduler (30-second SLA) | `kill-switch-specification.md` |

#### NIST AI RMF — Seven Characteristics

| Characteristic | Assessment | Evidence Required |
|----------------|------------|-------------------|
| **Valid & Reliable** | Schedule feasibility >95% (no conflicts) | `scheduler-eval-results.yaml` |
| **Safe** | No scheduling during maintenance windows | `safety-validation-report.md` |
| **Secure & Resilient** | MES API access controlled, encrypted | `nist-cybersecurity-framework.md` |
| **Accountable & Transparent** | Schedule changes logged with reason | `audit-record-schema.yaml` |
| **Explainable & Interpretable** | Schedule rationale available to operators | `schedule-explanation-module.md` |
| **Privacy-Enhanced** | No personal data in production scheduling | DPIA: N/A |
| **Fair** | No worker discrimination in shift scheduling | `bias-and-fairness-evals.md` |

#### Agentic Governance 2026

| Element | Requirement | Evidence |
|---------|-------------|----------|
| **Autonomy Tier** | Tier 2 — Conditional Autonomy (MES API writes, human approval for exceptions) | `agent-tier-classification.yaml` |
| **Tool-Use Risk** | MES API read/write, bounded by safety constraints | `tool-use-risk-model.yaml` |
| **Safety Agent** | Required — validates all schedule changes against ISO 10218 / IEC 62443 | `safety-agent-config.yaml` |
| **Kill Switch** | Required — 30-second activation | `kill-switch-specification.md` |

#### Singapore MGF

| Principle | Implementation | Evidence |
|-----------|----------------|----------|
| **Hard Guardrails** | Temporal: no production during maintenance (02:00-06:00) | `hard-guardrails-config.yaml` |
| **Hard Guardrails** | Dependency: material confirmation required before scheduling | `inventory-confirmation-api.yaml` |
| **Hard Guardrails** | Functional: cannot modify safety PLC logic | `safety-plc-readonly-policy.yaml` |
| **Meaningful Human Accountability** | VP of Manufacturing owns production policy | `policy-ownership-registry.yaml` |
| **Multi-Agent Coordination** | Supply Chain Agent → Production Agent → Quality Agent | `orchestration-agent-config.yaml` |

#### ISO/IEC 42001 — PDCA Thread

| PDCA Phase | Clause | Application in Stage 4 | Evidence |
|------------|--------|------------------------|----------|
| **PLAN** | 6.1, 6.2, 8.2 | Assess production scheduling risks (safety, supply chain), set schedule feasibility objectives, plan hard guardrails | `risk-management-plan.md`, `aims-objectives-and-kpis.md`, `hard-guardrails-config.yaml` |
| **DO** | 8.1, 8.2, 8.3 | Deploy scheduler with MES integration, activate Safety Agent, enforce hard guardrails, implement kill switch | `safety-agent-config.yaml`, `kill-switch-specification.md`, `orchestration-agent-config.yaml` |
| **CHECK** | 9.1, 9.2 | Monitor schedule feasibility, audit guardrail effectiveness, verify Safety Agent validation logs, conduct internal audit | `scheduler-eval-results.yaml`, Safety Agent logs, internal audit records |
| **ACT** | 10.1, 10.2 | Adjust maintenance windows, refine inventory confirmation thresholds, improve orchestration based on incident analysis | Incident post-mortems, guardrail updates |

**ISO 42001 Certification Note:** Stage 4 is the **safety-critical evidence zone**. `hard-guardrails-config.yaml` (Clause 8.2), `safety-agent-config.yaml` (Clause 8.3), and `safety-validation-report.md` (Clause 9.1) are mandatory audit artifacts. The auditor will verify that hard guardrails are **technically enforced**, not just documented.

---

### 4.2 Risk Register

| Risk ID | Threat | Likelihood | Impact | Mitigation | Owner |
|---------|--------|------------|--------|------------|-------|
| R-4.1 | Schedule conflict with maintenance | Medium | High | Hard guardrail: maintenance window lock | Production Manager |
| R-4.2 | Unsafe production parameters | Low | Critical | Safety Agent validates against ISO 10218 | Safety Officer |
| R-4.3 | Material shortage causing delay | Medium | Medium | Dependency guardrail: inventory confirmation | Supply Chain Manager |
| R-4.4 | MES API unauthorized access | Low | Critical | RBAC, network segmentation, audit logs | Security Engineer |
| R-4.5 | Cascading failure (multi-agent) | Low | Critical | Orchestration Agent monitors dependencies | AI Safety Engineer |
| R-4.6 | OT network traversal | Low | Critical | Air gap, firewall, Safety Agent validation | Security Engineer |

---

### 4.3 RACI Matrix — Order Confirmation & Production

| Activity | Policy Owner | Technical Owner | Operational Owner | Safety Officer | Client |
|----------|:----------:|:---------------:|:-----------------:|:------------:|:------:|
| Define production safety policy | **A** | C | R | R | I |
| Implement scheduler agent | C | **A** | I | R | I |
| Configure hard guardrails | C | **A** | C | R | I |
| Validate Safety Agent integration | I | R | I | **A** | I |
| Approve Production Release Gate | **A** | R | R | R | I |
| Monitor production schedule | I | C | **A** | C | I |
| Handle production incidents | **A** | R | R | R | I |
| Activate emergency stop | I | R | R | **A** | I |

---

### 4.4 Evidence Checklist — Production Release Gate

- [ ] `agent-tier-classification.yaml` — Tier 2 confirmed
- [ ] `tool-use-risk-model.yaml` — MES API calls bounded
- [ ] `safety-agent-config.yaml` — Validates against ISO 10218 / IEC 62443
- [ ] `kill-switch-specification.md` — 30-second kill switch tested
- [ ] `hard-guardrails-config.yaml` — Temporal, parametric, functional guardrails active
- [ ] `scheduler-eval-results.yaml` — >95% schedule feasibility
- [ ] `safety-validation-report.md` — Safety testing passed
- [ ] `orchestration-agent-config.yaml` — Multi-agent coordination monitored
- [ ] `policy-ownership-registry.yaml` — VP of Manufacturing MHA assigned

---

## Stage 5: Manufacturing & Quality

### Stage Overview

| Attribute | Value |
|-----------|-------|
| **Primary Agents** | `{{quality-agent}}` (Tier 2 — Conditional), Real-time parameter optimizer (Tier 3 — High Autonomy) |
| **Human Touchpoints** | Machine operator, quality engineer, maintenance technician |
| **System Touchpoints** | IoT sensors, SCADA/MES, anomaly detection, kill switch |
| **Governance Gate** | **Continuous Monitoring** — No single gate; real-time oversight |

---

### 5.1 AI Framework Mapping

#### NIST AI RMF Functions

| Function | Category | Requirement | Evidence |
|----------|----------|-------------|----------|
| **GOVERN** | GV-4.1 | Risk tolerance for real-time adjustments | Parameter bounds policy |
| **GOVERN** | GV-5.1 | Continuous monitoring mandated | `continuous-monitoring-plan.md` |
| **MAP** | MP-1.1 | Manufacturing context defined | `ml-lifecycle-canvas.md` — Manufacturing edition |
| **MAP** | MP-2.1 | Quality agent: Tier 2; Parameter optimizer: **Tier 3** | `agent-tier-classification.yaml` |
| **MAP** | MP-3.1 | Worker safety impact — **Critical** | ISO 10218, ISO/TS 15066 assessment |
| **MEASURE** | MS-1.1 | Quality metrics: dimensional accuracy | CMM measurement data |
| **MEASURE** | MS-2.1 | Safety validation for Tier 3 | `safety-validation-report.md` — Tier 3 edition |
| **MEASURE** | MS-3.1 | Real-time telemetry monitoring | IoT sensor dashboard |
| **MEASURE** | MS-3.2 | Drift detection (>5% triggers alert) | `drift-detection-runbook.md` |
| **MANAGE** | MG-1.1 | Risk response for quality failures | Rework/scrap procedures |
| **MANAGE** | MG-2.1 | Incident response for safety events | `ai-incident-report.md` — Safety edition |
| **MANAGE** | MG-2.4 | Kill switch: 30-second (Tier 2), **5-second (Tier 3)** | `kill-switch-specification.md` |

#### NIST AI RMF — Seven Characteristics

| Characteristic | Assessment | Evidence Required |
|----------------|------------|-------------------|
| **Valid & Reliable** | Quality detection accuracy >98% | `quality-agent-eval-results.yaml` |
| **Safe** | Parameter optimizer bounded by safety limits | `safety-validation-report.md` |
| **Secure & Resilient** | ICS network segmented, encrypted | `nist-cybersecurity-framework.md` |
| **Accountable & Transparent** | All parameter changes logged | `audit-record-schema.yaml` |
| **Explainable & Interpretable** | Anomaly explanation to operator | `anomaly-explanation-module.md` |
| **Privacy-Enhanced** | No personal data on shop floor | DPIA: N/A |
| **Fair** | No worker monitoring bias | `bias-and-fairness-evals.md` |

#### Agentic Governance 2026

| Element | Requirement | Evidence |
|---------|-------------|----------|
| **Autonomy Tier** | Quality Agent: Tier 2; Parameter Optimizer: **Tier 3** (High Autonomy) | `agent-tier-classification.yaml` |
| **Tool-Use Risk** | Tier 3: SCPI commands to CNC, bounded by parametric guardrails | `tool-use-risk-model.yaml` |
| **Safety Agent** | **Mandatory for Tier 3** — Governor validates all SCPI commands | `safety-agent-config.yaml` |
| **Kill Switch** | Tier 2: 30-second; **Tier 3: 5-second + automatic safe-state** | `kill-switch-specification.md` |

#### Singapore MGF

| Principle | Implementation | Evidence |
|-----------|----------------|----------|
| **Hard Guardrails** | Parametric: feed rate 10%-120% nominal | `hard-guardrails-config.yaml` |
| **Hard Guardrails** | Spatial: robot zones enforced (ISO 10218) | `robot-safety-zones.yaml` |
| **Hard Guardrails** | Functional: cannot modify safety PLC | `safety-plc-readonly-policy.yaml` |
| **Meaningful Human Accountability** | VP of Manufacturing owns safety policy | `policy-ownership-registry.yaml` |
| **Multi-Agent Coordination** | Production Agent ↔ Quality Agent ↔ Safety Agent | `orchestration-agent-config.yaml` |

#### ISO/IEC 42001 — PDCA Thread

| PDCA Phase | Clause | Application in Stage 5 | Evidence |
|------------|--------|------------------------|----------|
| **PLAN** | 6.1, 6.2, 8.2 | Assess Tier 3 risks (physical harm, OT security), set quality detection objectives (>98%), plan 5-second kill switch + auto safe-state | `risk-management-plan.md`, `aims-objectives-and-kpis.md`, `kill-switch-specification.md` |
| **DO** | 8.1, 8.2, 8.3 | Deploy Tier 3 parameter optimizer with SCPI command validation, activate Safety Agent governor, implement real-time telemetry, enforce parametric/spatial guardrails | `safety-agent-config.yaml`, `tool-use-risk-model.yaml`, IoT sensor integration |
| **CHECK** | 9.1, 9.2 | Monitor quality metrics in real-time, audit Safety Agent validation logs, conduct monthly kill switch tests, perform internal audit of Tier 3 controls | `quality-agent-eval-results.yaml`, kill switch test logs, Safety Agent audit trail |
| **ACT** | 10.1, 10.2 | Respond to anomalies (auto-hold, alert, rework), update safety bounds based on incident analysis, improve anomaly detection thresholds | `ai-incident-report.md`, `drift-detection-runbook.md`, safety bound updates |

**ISO 42001 Certification Note:** Stage 5 is the **highest-risk evidence zone**. The auditor will focus on:
- **Clause 8.3 (Risk Treatment):** Is the Safety Agent actually validating every Tier 3 action?
- **Clause 9.1 (Monitoring):** Are kill switch tests performed and documented monthly?
- **Clause 10.1 (Nonconformity):** Are safety incidents investigated with root cause analysis?

The `kill-switch-specification.md` with monthly test records is **mandatory** for certification.

---

### 5.2 Risk Register

| Risk ID | Threat | Likelihood | Impact | Mitigation | Owner |
|---------|--------|------------|--------|------------|-------|
| R-5.1 | Parameter optimizer exceeds safe bounds | Low | **Critical** | Safety Agent validates all SCPI commands | Safety Officer |
| R-5.2 | Quality agent misses defect | Medium | High | Human operator backup, >98% accuracy target | Quality Manager |
| R-5.3 | IoT sensor failure (false negative) | Medium | Medium | Sensor redundancy, anomaly detection | Maintenance Engineer |
| R-5.4 | Kill switch failure | Low | **Critical** | Monthly kill switch test, automatic safe-state | Safety Officer |
| R-5.5 | OT cyberattack (ransomware) | Low | **Critical** | Network segmentation, IEC 62443, backups | Security Engineer |
| R-5.6 | Multi-agent cascade failure | Low | **Critical** | Orchestration Agent + Safety Agent | AI Safety Engineer |
| R-5.7 | Emergency stop bypass | Low | **Critical** | Safety PLC independent of AI, physical E-stop | Safety Officer |

---

### 5.3 RACI Matrix — Manufacturing & Quality

| Activity | Policy Owner | Technical Owner | Operational Owner | Safety Officer | Client |
|----------|:----------:|:---------------:|:-----------------:|:------------:|:------:|
| Define safety bounds policy | **A** | C | C | R | I |
| Implement parameter optimizer | C | **A** | I | R | I |
| Configure Tier 3 Safety Agent | I | R | I | **A** | I |
| Test kill switch (monthly) | I | R | C | **A** | I |
| Monitor real-time quality | I | C | **A** | C | I |
| Respond to anomaly alert | I | C | **A** | R | I |
| Activate emergency stop | I | C | R | **A** | I |
| Investigate safety incident | **A** | R | R | R | I |

---

### 5.4 Evidence Checklist — Continuous Monitoring

- [ ] `agent-tier-classification.yaml` — Tier 3 confirmed for parameter optimizer
- [ ] `tool-use-risk-model.yaml` — SCPI commands bounded
- [ ] `safety-agent-config.yaml` — Governor validates all Tier 3 actions
- [ ] `kill-switch-specification.md` — 5-second kill switch + auto safe-state tested
- [ ] `hard-guardrails-config.yaml` — Parametric, spatial, functional guardrails active
- [ ] `quality-agent-eval-results.yaml` — >98% defect detection accuracy
- [ ] `drift-detection-runbook.md` — >5% drift triggers alert
- [ ] `nist-cybersecurity-framework.md` — ICS segmentation verified
- [ ] Monthly kill switch test log — Last 3 months passing

---

## Stage 6: Delivery & Feedback

### Stage Overview

| Attribute | Value |
|-----------|-------|
| **Primary Agents** | Feedback analysis agent (Tier 1 — Advisory) |
| **Human Touchpoints** | Client feedback, Customer Success Manager |
| **System Touchpoints** | Feedback collection, KB freshness SLA, retraining pipeline |
| **Governance Gate** | **Post-Market Review Gate** — Quarterly board review |

---

### 6.1 AI Framework Mapping

#### NIST AI RMF Functions

| Function | Category | Requirement | Evidence |
|----------|----------|-------------|----------|
| **GOVERN** | GV-5.1 | Post-market monitoring established | `continuous-monitoring-plan.md` |
| **GOVERN** | GV-5.2 | Feedback loop into governance | `feedback-to-governance-process.md` |
| **MAP** | MP-1.1 | Post-deployment context defined | `post-market-context.md` |
| **MAP** | MP-2.1 | Feedback agent: Tier 1 (Advisory) | `agent-tier-classification.yaml` |
| **MEASURE** | MS-3.1 | Customer satisfaction metrics | NPS, CSAT tracking |
| **MEASURE** | MS-3.2 | Model drift detection from feedback | Feedback sentiment drift alert |
| **MEASURE** | MS-4.2 | Incident reporting from field | `ai-incident-report.md` |
| **MANAGE** | MG-3.1 | Regular review cadence | Quarterly governance review |
| **MANAGE** | MG-3.2 | Model update procedures | `model-update-procedure.md` |
| **MANAGE** | MG-4.1 | Stakeholder communication | Quarterly board report |

#### NIST AI RMF — Seven Characteristics

| Characteristic | Assessment | Evidence Required |
|----------------|------------|-------------------|
| **Valid & Reliable** | Feedback analysis accuracy >90% | `feedback-analysis-eval.yaml` |
| **Safe** | No safety impact at delivery stage | N/A |
| **Secure & Resilient** | Feedback data encrypted, anonymized | `data-governance-plan.md` |
| **Accountable & Transparent** | Feedback drives model improvement | `feedback-to-governance-process.md` |
| **Explainable & Interpretable** | Feedback trends explained to product team | `feedback-dashboard.md` |
| **Privacy-Enhanced** | Client feedback anonymized | `dpia-template.md` |
| **Fair** | No bias in feedback interpretation | `bias-and-fairness-evals.md` |

#### Agentic Governance 2026

| Element | Requirement | Evidence |
|---------|-------------|----------|
| **Autonomy Tier** | Tier 1 — Advisory (feedback analysis only) | `agent-tier-classification.yaml` |
| **Tool-Use Risk** | Read-only feedback analysis | Tool registry: read-only |
| **Safety Agent** | Not required for Tier 1 | N/A |
| **Kill Switch** | Not required | N/A |

#### Singapore MGF

| Principle | Implementation | Evidence |
|-----------|----------------|----------|
| **Hard Guardrails** | Feedback cannot trigger automatic model deployment | `model-update-procedure.md` |
| **Meaningful Human Accountability** | VP of Product owns feedback policy | `policy-ownership-registry.yaml` |
| **Multi-Agent Coordination** | Feedback agent → Model retraining pipeline | `retraining-pipeline-config.yaml` |

#### ISO/IEC 42001 — PDCA Thread

| PDCA Phase | Clause | Application in Stage 6 | Evidence |
|------------|--------|------------------------|----------|
| **PLAN** | 6.2, 9.3 | Set post-market monitoring objectives, plan management review agenda, define feedback-to-improvement process | `aims-objectives-and-kpis.md`, `aims-management-review-agenda.md` |
| **DO** | 8.1, 8.4 | Collect client feedback, run feedback analysis, execute retraining pipeline with human validation, produce quarterly board report | `feedback-to-governance-process.md`, `model-update-procedure.md`, `quarterly-board-report.md` |
| **CHECK** | 9.1, 9.2, 9.3 | Evaluate feedback analysis accuracy, conduct management review of AIMS performance, audit post-market monitoring effectiveness | `feedback-analysis-eval.yaml`, management review minutes, internal audit records |
| **ACT** | 10.1, 10.2 | Implement model improvements from feedback, update KB articles, refine governance policies, close nonconformities | `aims-improvement-register.md`, KB freshness updates, policy revisions |

**ISO 42001 Certification Note:** Stage 6 is the **management system closure loop**. The auditor will verify:
- **Clause 9.3 (Management Review):** Are quarterly reviews conducted with documented minutes?
- **Clause 10.2 (Continual Improvement):** Does feedback actually drive improvement actions?
- **Clause 7.5 (Documented Information):** Are all governance artifacts version-controlled and retained?

The `quarterly-board-report.md` and `aims-management-review-minutes-template.md` are **mandatory** for demonstrating management commitment.

---

### 6.2 Risk Register

| Risk ID | Threat | Likelihood | Impact | Mitigation | Owner |
|---------|--------|------------|--------|------------|-------|
| R-6.1 | Negative feedback ignored | Medium | High | KB freshness SLA, quarterly review | Knowledge Manager |
| R-6.2 | Feedback data breach | Low | Medium | Encryption, access control | Data Protection Officer |
| R-6.3 | Model retraining from bad feedback | Low | High | Human validation before retraining | ML Engineer |
| R-6.4 | Regulatory reporting failure | Low | High | Automated compliance reporting | Compliance Officer |

---

### 6.3 RACI Matrix — Delivery & Feedback

| Activity | Policy Owner | Technical Owner | Operational Owner | Safety Officer | Client |
|----------|:----------:|:---------------:|:-----------------:|:------------:|:------:|
| Define feedback policy | **A** | C | R | I | C |
| Collect client feedback | I | C | **A** | I | R |
| Analyze feedback trends | I | **A** | C | I | I |
| Drive KB updates | C | R | **A** | I | I |
| Approve Post-Market Review Gate | **A** | R | R | C | I |
| Quarterly board reporting | **A** | R | R | R | I |
| Trigger model retraining | C | **A** | C | I | I |

---

### 6.4 Evidence Checklist — Post-Market Review Gate

- [ ] `feedback-analysis-eval.yaml` — >90% sentiment accuracy
- [ ] `continuous-monitoring-plan.md` — Post-market monitoring active
- [ ] `feedback-to-governance-process.md` — Feedback loop documented
- [ ] `model-update-procedure.md` — Human validation before retraining
- [ ] Quarterly governance review minutes — Last 4 quarters
- [ ] `quarterly-board-report.md` — Board governance report delivered
- [ ] KB freshness SLA — <90 days since last refresh

---

## Continuous Monitoring Layer

### Overview

The monitoring layer operates **across all stages** and provides real-time visibility into agent behavior, risk posture, and compliance status.

---

### Monitoring Governance Mapping

| Monitor | NIST AI RMF | Agentic 2026 | Singapore MGF | RACI |
|---------|-------------|--------------|---------------|------|
| **WP03: Runtime Monitoring** | MS-3.1, MS-3.2 | Safety Agent (Governor) | Multi-Agent Coordination | Technical Owner: **A** |
| **WP04: Audit & Compliance** | GV-7.2, MS-4.2 | Meaningful Human Accountability | Auditability | Compliance Officer: **A** |
| **Safety Agent (Governor)** | MG-2.4 | Safety Agent Architecture | Hard Guardrails | Safety Officer: **A** |
| **Orchestration Agent** | MG-1.1 | Multi-Agent Coordination | Multi-Agent Coordination | AI Safety Engineer: **A** |
| **Grafana Dashboard** | MS-3.1 | — | — | Technical Owner: **A** |
| **Quarterly Board Report** | GV-1.1, MG-4.1 | — | Meaningful Human Accountability | Policy Owner: **A** |

---

### Monitoring Risk Register

| Risk ID | Threat | Likelihood | Impact | Mitigation | Owner |
|---------|--------|------------|--------|------------|-------|
| R-M.1 | Monitoring system failure (blind spot) | Low | Critical | Redundant monitoring, heartbeat checks | Technical Owner |
| R-M.2 | Alert fatigue causing ignored warnings | Medium | High | Tiered alerting, escalation policies | Operational Owner |
| R-M.3 | Audit log tampering | Low | Critical | Tamper-evident logging, blockchain hash | Security Engineer |
| R-M.4 | Safety Agent failure | Low | **Critical** | Safety Agent redundancy, fallback to human | Safety Officer |
| R-M.5 | Orchestration Agent cascade miss | Low | **Critical** | Cross-agent dependency checks | AI Safety Engineer |

---

## Cross-Stage Governance Summary

### Governance Gate Summary

| Gate | Stage | NIST Functions | ISO 42001 PDCA | Key Characteristics | Agentic Tier | Kill Switch | Approver |
|------|-------|----------------|----------------|---------------------|--------------|-------------|----------|
| **Discovery Gate** | 1 | GOVERN, MAP | **PLAN** — Context, risk assessment | Secure, Transparent, Privacy | Tier 1 | N/A | Policy Owner |
| **Development Gate** | 2 | GOVERN, MEASURE | **PLAN/DO** — Objectives, development, testing | Valid, Safe, Explainable | Tier 1 | N/A | Policy Owner |
| **Quote Approval Gate** | 3 | MAP, MANAGE | **DO/CHECK** — Tier 2 deployment, monitoring | Valid, Accountable, Fair | Tier 2 | 30-second | Policy Owner |
| **Production Release Gate** | 4 | MAP, MEASURE, MANAGE | **DO/CHECK** — Safety validation, guardrail audit | Safe, Secure, Explainable | Tier 2 | 30-second | Policy Owner |
| **Continuous Monitoring** | 5 | MEASURE, MANAGE | **CHECK/ACT** — Real-time monitoring, incident response | Safe, Secure, Valid | Tier 2/3 | 5-second (Tier 3) | Safety Officer |
| **Post-Market Review Gate** | 6 | GOVERN, MANAGE | **ACT** — Management review, continual improvement | Valid, Accountable, Fair | Tier 1 | N/A | Policy Owner |

### RACI Summary by Role

| Role | Primary Accountability | Stages Most Involved |
|------|------------------------|---------------------|
| **Policy Owner** (VP level) | Policy correctness, gate approval | All gates (1, 2, 3, 4, 6) |
| **Technical Owner** (Engineering Lead) | Implementation, eval suites, monitoring | 1, 2, 3, 4, 5, Monitoring |
| **Operational Owner** (Manager) | Day-to-day monitoring, exception handling | 3, 4, 5, 6 |
| **Safety Officer** | Safety validation, kill switch, incident response | 4, 5, Monitoring |
| **Compliance Officer** | Regulatory compliance, audit, reporting | 1, 3, 6, Monitoring |
| **Security Engineer** | Adversarial defense, access control, ICS security | 1, 2, 4, 5 |
| **Client** | Feedback, approval, transparency | 1, 3, 6 |

---

## ISO 42001 Integration Layer

### PDCA as the Horizontal Thread

ISO/IEC 42001 provides the **certifiable management system** that runs horizontally across all 6 stages. While NIST AI RMF manages risk and Singapore MGF provides guardrails, ISO 42001 ensures the entire system is **organized, audited, and continuously improving**.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ISO 42001 PDCA ACROSS ALL STAGES                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   STAGE 1          STAGE 2          STAGE 3          STAGE 4               │
│   Discovery        DFM Analysis      Quote           Production             │
│      │                  │                  │                  │              │
│      ▼                  ▼                  ▼                  ▼              │
│   ┌─────┐           ┌─────┐           ┌─────┐           ┌─────┐            │
│   │PLAN │──────────▶│ DO  │──────────▶│ DO  │──────────▶│ DO  │            │
│   │4, 6 │           │8, 8.4│          │8, 8.2│          │8, 8.3│            │
│   └─────┘           └─────┘           └─────┘           └─────┘            │
│                                                                              │
│   STAGE 5          STAGE 6                                                 │
│   Manufacturing    Delivery & Feedback                                      │
│      │                  │                                                    │
│      ▼                  ▼                                                    │
│   ┌─────┐           ┌─────┐                                                │
│   │CHECK│──────────▶│ ACT │                                                │
│   │9, 9.2│          │10, 10.2│                                             │
│   └─────┘           └─────┘                                                │
│      │                                                                       │
│      ▼                                                                       │
│   ┌─────────────────────────────────────┐                                   │
│   │  CONTINUOUS MONITORING (CHECK/ACT)   │                                   │
│   │  • 9.1 Monitoring, measurement       │                                   │
│   │  • 9.3 Management review             │                                   │
│   │  • 10.1 Nonconformity & corrective   │                                   │
│   │  • 10.2 Continual improvement        │                                   │
│   └─────────────────────────────────────┘                                   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### ISO 42001 Clause → Stage Mapping

| ISO 42001 Clause | Title | Primary Stage | Secondary Stages |
|------------------|-------|---------------|------------------|
| **Clause 4** | Context of the Organisation | 1 (Discovery) | All |
| **Clause 5** | Leadership | 6 (Post-Market Review) | All |
| **Clause 6.1** | Risk Assessment | 1 (Discovery) | 2, 3, 4, 5 |
| **Clause 6.2** | AI Objectives | 2 (Development) | 3, 4, 5 |
| **Clause 7.1** | Resources | 2 (Development) | All |
| **Clause 7.2** | Competence | 2 (Development) | 5 |
| **Clause 7.5** | Documented Information | 2 (Development) | All |
| **Clause 8.1** | Operational Planning | 3 (Quote) | 4, 5 |
| **Clause 8.2** | AI Risk Assessment | 3 (Quote) | 4, 5 |
| **Clause 8.3** | AI Risk Treatment | 4 (Production) | 5 |
| **Clause 8.4** | AI System Lifecycle | 2 (Development) | 3, 4, 5, 6 |
| **Clause 9.1** | Monitoring & Measurement | 5 (Manufacturing) | All |
| **Clause 9.2** | Internal Audit | 5 (Manufacturing) | 2, 3, 4 |
| **Clause 9.3** | Management Review | 6 (Post-Market) | All |
| **Clause 10.1** | Nonconformity | 5 (Manufacturing) | 6 |
| **Clause 10.2** | Continual Improvement | 6 (Post-Market) | All |

### Certification Audit Trail per Stage

| Audit Stage | Auditor Will Examine | Key Evidence |
|-------------|---------------------|--------------|
| **Stage 1 Audit (Documentation)** | Clauses 4-7 | `governance-charter.md`, `governance-roles-raci.md`, `risk-management-plan.md`, `aims-objectives-and-kpis.md` |
| **Stage 2 Audit (Implementation)** | Clauses 8-10 | `model-card.md`, `test-plan-for-ai.md`, `safety-agent-config.yaml`, kill switch test records, management review minutes |
| **Surveillance (Annual)** | Clause 9 + changes | Change records, incident reports, improvement register, updated eval results |

---

## Evidence Artifact Registry

| Artifact | Stage | Owner | Review Cadence | ISO 42001 Clause |
|----------|-------|-------|----------------|------------------|
| `agent-tier-classification.yaml` | All | Technical Owner | Per agent update | 4.1, 6.1 |
| `tool-use-risk-model.yaml` | 3, 4, 5 | Technical Owner | Per tool addition | 8.2 |
| `safety-agent-config.yaml` | 3, 4, 5 | Safety Officer | Quarterly | 8.3 |
| `kill-switch-specification.md` | 3, 4, 5 | Safety Officer | Quarterly test | 8.3, 9.1 |
| `hard-guardrails-config.yaml` | 3, 4, 5 | Technical Owner | Per policy change | 8.2, 8.3 |
| `policy-ownership-registry.yaml` | All | Policy Owner | Quarterly | 5.2, 5.3 |
| `audit-record-schema.yaml` | All | Compliance Officer | Annual | 7.5, 9.1 |
| `dfm-accuracy-eval-suite.yaml` | 2 | Technical Owner | Quarterly | 8.4, 9.1 |
| `nist-ai-rmf-assessment.yaml` | All | Compliance Officer | Per project | 6.1, 8.2 |
| `quarterly-board-report.md` | 6 | Policy Owner | Quarterly | 9.3 |
| `aims-objectives-and-kpis.md` | All | Policy Owner | Quarterly | 6.2, 9.1 |
| `aims-management-review-minutes-template.md` | 6 | Policy Owner | Quarterly | 9.3 |
| `aims-improvement-register.md` | 6 | Compliance Officer | Quarterly | 10.2 |
| `aims-internal-audit-checklist.md` | 5 | Internal Audit | Annual | 9.2 |

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-24 | ProtoLabs AI Governance Office | Initial release — 6-stage governance mapping |
| 1.1 | 2026-04-24 | ProtoLabs AI Governance Office | Added ISO/IEC 42001 PDCA thread, certification integration, gap analysis references |

---

## See Also

- `docs/iso-42001-gap-analysis.md` — Complete gap analysis and certification roadmap
- `governance/00-getting-started/agentic-governance-2026-framework.md` — Agentic Governance 2026 Framework
- `governance/05-cross-cutting/nist-ai-rmf-reference-guide.md` — NIST AI RMF Reference Guide
- `governance/05-cross-cutting/nist-ai-rmf-compliance-mapping.md` — Multi-framework compliance mapping (includes ISO 42001)
- `ai-implementation-workstreams/GOVERNANCE-FRAMEWORK-MAPPING.md` — WP01-WP04 Governance Mapping
- `docs/client-journey-agentic-workflow.mmd` — Client Journey Mermaid Workflow
