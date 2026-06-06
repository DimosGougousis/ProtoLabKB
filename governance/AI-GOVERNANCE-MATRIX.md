# ProtoLabs AI Governance Matrix

> **Document Type:** Cross-Reference Governance Matrix
> **Version:** 1.0
> **Effective Date:** 2026-05-29
> **Owner:** Chief AI Officer (CAIO)
> **Approved By:** AI Governance Council
> **Review Cycle:** Quarterly, or upon new agent deployment
> **Next Review:** 2026-08-29
> **Classification:** Internal — Board Distribution

---

## 1. Purpose

This matrix provides a **single-pane-of-glass** cross-reference of every ProtoLabs AI system against all applicable governance controls, regulatory frameworks, risk classifications, and accountability assignments. It is the authoritative reference for:

- **AI Governance Council** — deployment approval decisions
- **Engineering Teams** — control implementation requirements
- **Compliance & Audit** — evidence collection and certification readiness
- **Board of Directors** — risk exposure and regulatory posture

---

## 2. Agent Fleet Registry & Risk Classification

### 2.1 Current Agent Fleet

| Agent ID | Agent Name | Tier | Autonomy Level | Lifecycle Stage | Status | Policy Owner | Technical Owner |
|----------|-----------|:----:|---------------|----------------|:------:|-------------|----------------|
| `dfm-router` | DFM Router | 1 | Advisory | Discovery & Intake | ✅ Production | VP Product | ML Engineering Lead |
| `cnc-machining` | CNC Machining Agent | 1 | Advisory | DFM Analysis | ✅ Production | VP Engineering | CNC ML Engineer |
| `injection-molding` | Injection Molding Agent | 1 | Advisory | DFM Analysis | ✅ Production | VP Engineering | IM ML Engineer |
| `sheet-metal` | Sheet Metal Agent | 1 | Advisory | DFM Analysis | ✅ Production | VP Engineering | SM ML Engineer |
| `3d-printing` | 3D Printing Agent | 1 | Advisory | DFM Analysis | ✅ Production | VP Engineering | 3DP ML Engineer |
| `materials-selection` | Materials Selection Agent | 1 | Advisory | Quote & Proposal | ✅ Production | VP Engineering | Materials ML Engineer |
| `quote-bot` | Quote Generation Bot | 2 | Conditional | Quote & Proposal | 🔶 In Development | VP Sales | Pricing ML Engineer |
| `production-scheduler` | Production Scheduler | 2 | Conditional | Order & Production | 🔶 In Development | VP Manufacturing | Scheduling ML Engineer |
| `quality-agent` | Quality Inspection Agent | 2 | Conditional | Manufacturing | 🔶 In Development | VP Manufacturing | Quality ML Engineer |
| `param-optimizer` | Parameter Optimizer | 3 | High Autonomy | Manufacturing | 🔴 Planned | VP Manufacturing | Optimization ML Engineer |

### 2.2 Tier Classification Criteria

| Criterion | Tier 1 — Advisory | Tier 2 — Conditional | Tier 3 — High Autonomy |
|-----------|:-----------------:|:--------------------:|:----------------------:|
| **Human-in-the-loop** | Human decides always | Human approves exceptions | Human oversees by exception |
| **Tool/API access** | Read-only | Read/Write (bounded) | Read/Write (bounded + validated) |
| **Physical actuation** | None | None | Indirect (via PLC/CNC) |
| **Financial impact** | None | Direct (pricing, scheduling) | Direct (production parameters) |
| **Safety impact** | None | Indirect (schedule conflicts) | Direct (machine parameters) |
| **Kill switch required** | No | Yes (<30s) | Yes (<5s + auto safe-state) |
| **Safety Agent required** | No | Yes | Yes (mandatory Governor) |
| **EU AI Act mapping** | Limited-risk | Limited-to-High (re-assess) | High-risk (assumed) |
| **Approval authority** | Technical Owner + Security | Governance Council | Council + Board |

---

## 3. Control Requirements Matrix

### 3.1 Governance Controls by Tier

| Control ID | Control Name | Description | Tier 1 | Tier 2 | Tier 3 | Evidence Artifact |
|:----------:|-------------|-------------|:------:|:------:|:------:|-------------------|
| **GC-01** | Model Card | Documentation of model purpose, training data, limitations, performance | ✅ Required | ✅ Required | ✅ Required + External Audit | `model-card.md` |
| **GC-02** | Eval Suite | Accuracy, safety, fairness evaluation against golden dataset | ✅ Required | ✅ Required | ✅ Required + Red Team | `*-eval-results.yaml` |
| **GC-03** | Input Sanitization | Validate, sanitize, and secure all inputs before processing | ✅ Required | ✅ Required | ✅ Required | `input-sanitization.md` |
| **GC-04** | Human Oversight Plan | Defined human review/approval process | Advisory (override) | Mandatory (approval gate) | Mandatory (exception review) | `human-oversight-plan.md` |
| **GC-05** | Kill Switch | Emergency stop mechanism | ❌ Not Required | ✅ Required (<30s) | ✅ Required (<5s + safe-state) | `kill-switch-specification.md` |
| **GC-06** | Source Citation / Audit Trail | Every output traces to source KB + original URL | ✅ Required | ✅ Required | ✅ Required | `audit-record-schema.yaml` |
| **GC-07** | Bias & Fairness Assessment | Evaluate for discriminatory outcomes | If demographic data | ✅ Required | ✅ Required + 3rd Party | `bias-and-fairness-evals.md` |
| **GC-08** | Incident Response Plan | Defined escalation, containment, recovery procedures | ✅ Required | ✅ Required | ✅ Required + Board Notification | `ai-incident-report.md` |
| **GC-09** | Pre-Deployment Gate | Approval before production release | Automated CI/CD | Council Review | Board Approval | Gate approval records |
| **GC-10** | Post-Deployment Monitoring | Ongoing performance and drift tracking | Performance KPIs | Performance + Drift + Misuse | Full Spectrum + Continuous Eval | Grafana dashboards |
| **GC-11** | Legal Review | Legal counsel review of AI outputs | ❌ Not Required | If customer-facing | ✅ Required | Legal sign-off |
| **GC-12** | PE Validation | Professional Engineer validation of structural outputs | ❌ N/A | If structural output | ✅ Required | PE sign-off |
| **GC-13** | Safety Agent Integration | Independent Governor agent validates actions | ❌ Not Required | ✅ Required | ✅ Required (Mandatory) | `safety-agent-config.yaml` |
| **GC-14** | Tool-Use Risk Model | Documented risk assessment for every tool/API the agent can invoke | ❌ Not Required | ✅ Required | ✅ Required | `tool-use-risk-model.yaml` |
| **GC-15** | Hard Guardrails | Parametric, temporal, functional, spatial boundaries | Output bounded | Financial + Safety bounds | Physical + Safety bounds | `hard-guardrails-config.yaml` |
| **GC-16** | Explainability Module | Decision explanation available to users/operators | Confidence score | Full rationale | Full rationale + counterfactuals | `explainability-module.md` |
| **GC-17** | Data Governance | Data handling, retention, access control policies | ✅ Required | ✅ Required | ✅ Required | `data-governance-plan.md` |
| **GC-18** | Multi-Tenant Isolation | Client data isolation and cross-tenant protection | ✅ Required | ✅ Required | ✅ Required | `tenant-isolation-config.yaml` |
| **GC-19** | Drift Detection | Model performance degradation monitoring | ❌ Not Required | ✅ Required | ✅ Required | `drift-detection-runbook.md` |
| **GC-20** | Red Team Exercise | Adversarial testing by independent team | ❌ Not Required | If customer-facing | ✅ Required | `red-team-report-*.pdf` |

### 3.2 Control Coverage Summary

| Tier | Required Controls | Optional Controls | Total |
|:----:|:-----------------:|:-----------------:|:-----:|
| **Tier 1** | 10 | 3 | 13 |
| **Tier 2** | 18 | 2 | 20 |
| **Tier 3** | 20 | 0 | 20 |

---

## 4. Regulatory Framework Cross-Reference

### 4.1 Framework Mapping Matrix

| Control ID | NIST AI RMF | EU AI Act | ISO/IEC 42001 | Singapore MGF | Agentic 2026 |
|:----------:|-------------|-----------|---------------|---------------|--------------|
| GC-01 | GV-7.1 | Art. 11 (Technical Documentation) | 7.5 (Documented Information) | — | — |
| GC-02 | MS-1.1, MS-2.1 | Art. 15 (Accuracy, Robustness) | 8.4 (AI System Development) | — | — |
| GC-03 | MAP-1.1, MS-1.1 | Art. 9 (Risk Management) | 8.2 (Risk Treatment) | Hard Guardrails (Input) | — |
| GC-04 | MG-1.1 | Art. 14 (Human Oversight) | 8.1 (Operational Planning) | Meaningful Human Accountability | — |
| GC-05 | MG-2.4 | Art. 14.4(d) (Override Capability) | 8.3 (Risk Treatment) | Hard Guardrails (Emergency) | Safety Agent |
| GC-06 | GV-7.2, CHAR-4 | Art. 13 (Transparency) | 9.1 (Monitoring) | Auditability | — |
| GC-07 | CHAR-6 | Art. 10 (Data Governance) | 6.1 (Risk Assessment) | — | — |
| GC-08 | MG-2.1, MS-4.2 | Art. 62 (Incident Reporting) | 10.1 (Nonconformity) | — | — |
| GC-09 | MG-1.1 | Art. 43 (Conformity Assessment) | 9.2 (Internal Audit) | Operational Readiness | Deployment Gate |
| GC-10 | MS-3.1, MG-3.1 | Art. 72 (Post-Market Monitoring) | 9.1 (Performance Evaluation) | — | — |
| GC-11 | GV-1.1 | Art. 5 (Prohibited Practices) | 6.1.3 (Legal Requirements) | — | — |
| GC-12 | CHAR-1 | Art. 9 (Risk Management) | 8.4 (Verification) | — | — |
| GC-13 | — | Art. 14 (Human Oversight) | 8.3 (Risk Treatment) | Safety Agent Architecture | Safety Agent |
| GC-14 | MAP-2.1 | Art. 9 (Risk Management) | 6.1 (Risk Assessment) | — | Tool-Use Risk Model |
| GC-15 | MG-2.4 | Art. 9.5 (Risk Mitigation) | 8.2 (Risk Treatment) | Hard Guardrails | — |
| GC-16 | CHAR-5 | Art. 13.4(f) (Explanation) | 7.4 (Communication) | Explainability | — |
| GC-17 | GV-6.1 | Art. 10 (Data Governance) | 7.5 (Documented Information) | — | — |
| GC-18 | CHAR-7 | Art. 10.5 (Data Separation) | 8.1 (Operational Planning) | — | — |
| GC-19 | MS-3.2 | Art. 72 (Post-Market Monitoring) | 9.1 (Performance Evaluation) | — | — |
| GC-20 | MS-2.1, CHAR-2, CHAR-3 | Art. 55 (Codes of Conduct) | 9.2 (Internal Audit) | Red Teaming | Safety Agent Validation |

### 4.2 NIST AI RMF Function Coverage

| NIST Function | Controls Mapped | Coverage Status |
|---------------|:--------------:|:--------------:|
| **GOVERN** (GV) | GC-01, GC-06, GC-07, GC-08, GC-11, GC-17 | ✅ Complete |
| **MAP** (MP) | GC-03, GC-14, GC-17, GC-18 | ✅ Complete |
| **MEASURE** (MS) | GC-02, GC-03, GC-06, GC-10, GC-19, GC-20 | ✅ Complete |
| **MANAGE** (MG) | GC-04, GC-05, GC-08, GC-09, GC-10, GC-15 | ✅ Complete |

### 4.3 NIST Seven Characteristics Coverage

| Characteristic | Controls Mapped | Assessment |
|---------------|:--------------:|------------|
| **Valid & Reliable** | GC-02, GC-12, GC-19 | Eval suites + drift detection ensure ongoing validity |
| **Safe** | GC-04, GC-05, GC-13, GC-15 | Kill switches + Safety Agent + hard guardrails |
| **Secure & Resilient** | GC-03, GC-18, GC-20 | Input sanitization + tenant isolation + red teaming |
| **Accountable & Transparent** | GC-01, GC-06, GC-16 | Model cards + audit trails + explainability |
| **Explainable & Interpretable** | GC-16 | Decision explanations at all tiers |
| **Privacy-Enhanced** | GC-17, GC-18 | Data governance + multi-tenant isolation |
| **Fair** | GC-07 | Bias and fairness evaluations |

---

## 5. Client Journey Stage × Governance Gate Matrix

### 5.1 Stage-Gate Cross-Reference

| Client Journey Stage | Primary Agents | Tier | Governance Gate | Required Controls | Gate Approver |
|---------------------|---------------|:----:|----------------|-------------------|:-------------:|
| **1. Discovery & Intake** | `dfm-router` | 1 | Discovery Gate | GC-01, GC-02, GC-03, GC-06, GC-17, GC-18 | Technical Owner + Security |
| **2. DFM Analysis** | `cnc-machining`, `injection-molding`, `sheet-metal`, `3d-printing` | 1 | Development Gate | GC-01, GC-02, GC-03, GC-06, GC-07, GC-16, GC-17 | Technical Owner + Security |
| **3. Quote & Proposal** | `materials-selection`, `quote-bot` | 1/2 | Quote Approval Gate | GC-01–GC-18 (Tier 2 full set) | Governance Council |
| **4. Order & Production** | `production-scheduler` | 2 | Production Release Gate | GC-01–GC-18 + GC-15 (safety bounds) | Governance Council |
| **5. Manufacturing & Quality** | `quality-agent`, `param-optimizer` | 2/3 | Continuous Monitoring | GC-01–GC-20 (full set for Tier 3) | Council + Board (Tier 3) |

### 5.2 Gate Evidence Requirements

| Gate | Minimum Evidence | Pass Criteria | Fail Action |
|------|-----------------|---------------|-------------|
| **Discovery Gate** | Tier classification, input sanitization active, router eval >95% | All checklist items ✅ | Block DFM analysis; remediate |
| **Development Gate** | Model cards, eval >90%, adversarial testing, citation enforcement | All checklist items ✅ | Block quote generation; remediate |
| **Quote Approval Gate** | Tier 2 classification, Safety Agent, kill switch tested, financial guardrails | All checklist items ✅ | Block client proposal; remediate |
| **Production Release Gate** | Safety validation, hard guardrails, MES integration tested, kill switch <30s | All checklist items ✅ | Block shop floor; remediate |
| **Continuous Monitoring** | Real-time telemetry, drift detection, Safety Agent active, kill switch <5s (Tier 3) | Ongoing compliance | Auto-hold production; escalate |

---

## 6. Work Package × Governance Framework Matrix

### 6.1 P0 Critical Work Packages

| Work Package | NIST AI RMF Functions | Agentic 2026 Elements | Singapore MGF Principles | ISO 42001 Clauses | Safety Agent |
|-------------|----------------------|----------------------|-------------------------|-------------------|:------------:|
| **WP01: Input Sanitization** | MAP, MANAGE | Tier Classification | Hard Guardrails (Input) | 6.1, 8.1, 8.2, 9.1 | Validates Input |
| **WP02: Adversarial Defense** | MEASURE, MANAGE | Tool-Use Risk, Safety Agent | Hard Guardrails (Defense-in-Depth) | 8.2, 8.3, 9.1, 9.2 | Validates Actions |
| **WP03: Runtime Monitoring** | MEASURE | Multi-Agent Coordination | Multi-Agent Coordination | 9.1, 9.2 | Telemetry Feed |
| **WP04: Audit & Compliance** | GOVERN, MANAGE | Meaningful Human Accountability | Auditability | 7.5, 9.1, 9.2, 10.1 | — |

### 6.2 P1 High Priority Initiatives

| Initiative | NIST AI RMF | Agentic 2026 | Singapore MGF | ISO 42001 | Budget | Timeline |
|-----------|-------------|--------------|---------------|-----------|--------|----------|
| **Zero-Trust Architecture** | CHAR-3 (Secure) | Safety Agent Infrastructure | Hard Guardrails (Network) | 8.1, 8.3 | $500K–$1M | 90 days |
| **Adversarial Defense Commercial** | MS-2.1, CHAR-2, CHAR-3 | Safety Agent Validation | Red Teaming | 8.4, 9.2 | $300K–$500K | 60 days |
| **Insider Threat Program** | MS-3.1, MS-3.2 | Behavioral Analysis | Behavioral Guardrails | 9.1, 9.2 | $200K–$300K | 120 days |
| **Nation-State Countermeasures** | CHAR-3, MG-2.1 | — | — | 6.1, 8.3 | $500K–$2M | 180 days |

---

## 7. ISO/IEC 42001 Readiness Matrix

### 7.1 Clause Readiness by Agent Tier

| ISO 42001 Clause | Tier 1 Readiness | Tier 2 Readiness | Tier 3 Readiness | Gap |
|------------------|:----------------:|:----------------:|:----------------:|-----|
| **4.1 Context** | ✅ 90% | ✅ 85% | 🔶 60% | Tier 3 needs OT/ICS context |
| **4.2 Interested Parties** | ✅ 85% | ✅ 80% | 🔶 55% | Need client procurement mapping |
| **5.1 Leadership** | ✅ 80% | ✅ 75% | 🔶 50% | Board engagement for Tier 3 |
| **5.2 Policy** | ✅ 95% | ✅ 90% | ✅ 85% | Policy covers all tiers |
| **6.1 Risk Assessment** | ✅ 90% | ✅ 85% | 🔶 65% | Tier 3 needs OT risk assessment |
| **6.2 Objectives** | ✅ 85% | ✅ 80% | 🔶 60% | Tier 3 KPIs not yet defined |
| **7.1 Resources** | ✅ 80% | 🔶 65% | 🔴 40% | Tier 3 needs specialized OT resources |
| **7.2 Competence** | ✅ 75% | 🔶 60% | 🔴 35% | Tier 3 needs OT/ICS training |
| **7.3 Awareness** | ✅ 80% | 🔶 65% | 🔴 40% | Tier 3 awareness program needed |
| **7.4 Communication** | ✅ 75% | 🔶 60% | 🔴 35% | Tier 3 stakeholder comms plan |
| **7.5 Documented Info** | ✅ 90% | ✅ 85% | 🔶 65% | Tier 3 needs OT documentation |
| **8.1 Operational Planning** | ✅ 85% | ✅ 80% | 🔶 55% | Tier 3 operational procedures |
| **8.2 Risk Treatment** | ✅ 85% | ✅ 80% | 🔶 55% | Tier 3 physical risk treatment |
| **8.3 AI System Lifecycle** | ✅ 80% | 🔶 70% | 🔴 45% | Tier 3 lifecycle not defined |
| **8.4 AI System Requirements** | ✅ 85% | ✅ 75% | 🔶 50% | Tier 3 requirements incomplete |
| **9.1 Monitoring** | ✅ 85% | ✅ 80% | 🔶 60% | Tier 3 needs OT monitoring |
| **9.2 Internal Audit** | ✅ 75% | 🔶 65% | 🔴 40% | Tier 3 audit procedures needed |
| **9.3 Management Review** | ✅ 80% | 🔶 70% | 🔴 45% | Tier 3 review cadence needed |
| **10.1 Nonconformity** | ✅ 80% | 🔶 70% | 🔶 55% | Tier 3 corrective actions |
| **10.2 Continual Improvement** | ✅ 75% | 🔶 65% | 🔴 40% | Tier 3 improvement process |

### 7.2 Certification Readiness Summary

| Tier | Current Readiness | Target | Gap to Close | Priority Actions |
|:----:|:-----------------:|:------:|:------------:|-----------------|
| **Tier 1** | 83% | 95% | 12% | Complete documentation, run internal audit |
| **Tier 2** | 74% | 90% | 16% | Safety Agent integration, kill switch testing, internal audit |
| **Tier 3** | 49% | 85% | 36% | OT risk assessment, training program, lifecycle definition |

---

## 8. RACI Master Matrix

### 8.1 Governance Activity RACI

| Activity | CAIO | Policy Owner | Technical Owner | Operational Owner | Safety Officer | DPO | Legal | Board |
|----------|:----:|:----------:|:--------------:|:-----------------:|:------------:|:---:|:-----:|:-----:|
| Set AI risk appetite | **A** | C | C | I | C | C | C | R |
| Classify agent tier | C | **A** | R | C | R | I | I | I |
| Approve Tier 1 deployment | I | **A** | R | C | C | I | I | I |
| Approve Tier 2 deployment | **A** | R | R | C | R | C | C | I |
| Approve Tier 3 deployment | R | C | R | C | R | C | C | **A** |
| Conduct risk assessment | C | **A** | R | C | R | C | C | I |
| Implement controls | I | C | **A** | R | C | I | I | I |
| Monitor performance | I | C | R | **A** | C | I | I | I |
| Activate kill switch | I | I | R | R | **A** | I | I | I |
| Handle incidents | **A** | R | R | R | R | C | C | I (Sev1) |
| Report to board | **A** | C | C | I | C | C | C | I |
| Conduct internal audit | I | C | C | C | C | **A** | C | I |
| Manage third-party AI | C | **A** | R | C | C | R | R | I |
| Update governance policy | **A** | R | C | C | C | C | C | R |

**Legend:** R = Responsible, A = Accountable, C = Consulted, I = Informed

---

## 9. Incident Severity & Escalation Matrix

### 9.1 Severity Classification

| Severity | Definition | Examples | Response Time | Escalation |
|:--------:|-----------|----------|:-------------:|------------|
| **Sev1 — Critical** | Safety risk, data breach, production halt | Unsafe machine parameter, client IP exfiltration, Tier 3 kill switch failure | <15 minutes | CAIO → Board (24h) |
| **Sev2 — Major** | Significant accuracy degradation, unauthorized access | DFM accuracy <80%, unauthorized API access, Safety Agent failure | <1 hour | CAIO → Governance Council (48h) |
| **Sev3 — Moderate** | Performance degradation, minor policy violation | Drift >5%, missing citation, guardrail boundary breach | <4 hours | Policy Owner → CAIO (weekly) |
| **Sev4 — Low** | Cosmetic issues, minor anomalies | UI display error, log formatting issue, minor latency spike | <24 hours | Operational Owner → Policy Owner (monthly) |

### 9.2 Escalation Path

```
┌─────────────────────────────────────────────────────────────────┐
│                    INCIDENT ESCALATION PATH                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Detection ──► Triage ──► Containment ──► Resolution ──► Review  │
│                                                                  │
│  Sev1: Safety Officer ──► CAIO ──► Board (24h notification)     │
│  Sev2: Technical Owner ──► Policy Owner ──► CAIO ──► Council    │
│  Sev3: Operational Owner ──► Policy Owner ──► CAIO              │
│  Sev4: Operational Owner ──► Policy Owner                       │
│                                                                  │
│  KILL SWITCH: Safety Officer can activate independently          │
│  at any severity level without approval                          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 10. Monitoring & KPI Dashboard Matrix

### 10.1 KPIs by Tier

| KPI | Tier 1 Target | Tier 2 Target | Tier 3 Target | Measurement |
|-----|:-------------:|:-------------:|:-------------:|-------------|
| **Accuracy** | >95% | >93% | >98% | Golden dataset eval |
| **Latency** | <500ms | <200ms | <100ms | P95 response time |
| **False Positive Rate** | <2% | <1% | <0.5% | Confusion matrix |
| **Uptime** | 99.5% | 99.9% | 99.99% | Health check probes |
| **Kill Switch Activation** | N/A | <30s | <5s | Monthly drill |
| **Drift Alert** | N/A | >5% degradation | >3% degradation | Weekly eval |
| **Citation Coverage** | 100% | 100% | 100% | Automated check |
| **Incident Response** | <24h | <4h | <15m | Time to containment |

### 10.2 Dashboard Requirements

| Dashboard | Audience | Refresh Rate | Key Panels |
|-----------|----------|:------------:|------------|
| **Executive Risk Dashboard** | Board, CAIO | Daily | Risk posture, incident count, compliance score |
| **Operational Dashboard** | Engineering, Ops | Real-time | Latency, errors, throughput, kill switch status |
| **Compliance Dashboard** | DPO, Legal, Audit | Weekly | Control coverage, evidence status, audit findings |
| **Safety Dashboard** | Safety Officer | Real-time | Safety Agent status, guardrail breaches, kill switch drills |

---

## 11. Third-Party AI Vendor Matrix

| Vendor / Model | Use Case | Tier | Risk Level | Controls Required | Review Cadence |
|---------------|----------|:----:|:----------:|-------------------|:--------------:|
| Anthropic Claude | DFM analysis backbone | 1 | Medium | GC-01, GC-02, GC-03, GC-06, GC-17 | Quarterly |
| OpenAI GPT-4V | CAD image analysis | 1 | Medium | GC-01, GC-02, GC-03, GC-06, GC-17 | Quarterly |
| Azure OpenAI | Quote generation support | 2 | High | GC-01–GC-18 (full Tier 2) | Monthly |
| Custom ML Models | Parameter optimization | 3 | Critical | GC-01–GC-20 (full set) | Continuous |

**Vendor Assessment Criteria:**
- [ ] Data processing agreement (DPA) signed
- [ ] SOC 2 Type II or equivalent certification
- [ ] Data residency requirements met (EU/US)
- [ ] Model card and safety documentation available
- [ ] Incident notification SLA defined (<24h)
- [ ] Exit strategy and data portability documented

---

## 12. Document Cross-Reference

| Document | Location | Purpose | Review Cycle |
|----------|----------|---------|:------------:|
| AI Governance Policy | `governance/ai-governance-policy.md` | Enterprise policy entry point | Annual |
| Governance Framework Architecture | `docs/governance-framework-architecture.md` | Board-level architecture reference | Semi-annual |
| Governance by Stage Framework | `docs/governance-by-stage-framework.md` | Client journey governance gates | Quarterly |
| ISO 42001 Gap Analysis | `docs/iso-42001-gap-analysis.md` | Certification readiness | Quarterly |
| Governance Framework Mapping | `ai-implementation-workstreams/GOVERNANCE-FRAMEWORK-MAPPING.md` | WP-to-framework alignment | Per release |
| Implementation Guide | `governance/AI-GOVERNANCE-IMPLEMENTATION-GUIDE.md` | Practical implementation roadmap | Quarterly |
| Policy-as-Code Remediation Plan | `docs/policy-as-code-remediation-plan.md` | PaC gap closure | Monthly |

---

## Appendix A: Glossary

| Term | Definition |
|------|------------|
| **AIMS** | AI Management System (per ISO/IEC 42001) |
| **CAIO** | Chief AI Officer |
| **DPA** | Data Processing Agreement |
| **DPIA** | Data Protection Impact Assessment |
| **DPO** | Data Protection Officer |
| **GC** | Governance Control (this matrix) |
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
| 1.0 | 2026-05-29 | AI Governance Office | Initial release — consolidated from policy, architecture, and stage framework |