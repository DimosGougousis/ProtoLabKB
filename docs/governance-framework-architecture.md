# ProtoLabs AI Governance Framework — Architecture Document

> **Document Type:** Board-Level Governance Architecture Reference
> **Version:** 2.0
> **Date:** 2026-04-28
> **Owner:** Chief AI Officer (CAIO)
> **Approved By:** Board of Directors
> **Classification:** Board Confidential
> **Review Cycle:** Semi-annual, or upon material regulatory or architectural change
> **Next Review:** 2026-10-28

---

## 1. Executive Summary

ProtoLabs operates AI systems that influence manufacturing decisions — from DFM analysis to pricing to production scheduling. This document defines the **complete governance architecture** that ensures these systems are safe, compliant, auditable, and trustworthy.

The architecture integrates **4 regulatory frameworks** (EU AI Act, NIST AI RMF 1.0, ISO/IEC 42001, Singapore MGF) into a **unified operational system** spanning the full AI lifecycle: discovery, development, deployment, monitoring, and retirement.

### Current State

| Metric | Value |
|--------|-------|
| **Governance artifacts** | 23 documents across 7 pillars |
| **AI agents governed** | 10 (all Tier 1 — Advisory) |
| **ISO 42001 readiness** | 87% (target: Q1 2027 certification) |
| **Policy-as-Code maturity** | Architecture complete, implementation in progress |
| **Regulatory frameworks integrated** | 4 (EU AI Act, NIST AI RMF, ISO 42001, Singapore MGF) |

### What This Document Covers

1. **Architecture Overview** — The 4-layer governance stack
2. **Regulatory Framework Integration** — How 4 frameworks map to ProtoLabs controls
3. **Risk Classification** — 3-tier system with explicit control requirements
4. **Enforcement Architecture** — 7-layer pipeline with policy-as-code
5. **Safety Architecture** — Safety Agents, kill-switches, fail-closed design
6. **Multi-Tenant Isolation** — 6-layer isolation for client-specific governance
7. **Agent Fleet Governance** — Current fleet and roadmap
8. **Policy-as-Code Roadmap** — Remediation plan for 6 identified gaps
9. **Certification Roadmap** — ISO 42001 timeline
10. **Board Governance** — Decision authority, escalation, reporting

---

## 2. Architecture Overview — The 4-Layer Stack

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│                    PROTOLABS AI GOVERNANCE ARCHITECTURE                      │
│                                                                             │
│  LAYER 1: REGULATORY FRAMEWORKS                                             │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │  EU AI Act  │  NIST AI RMF 1.0  │  ISO/IEC 42001  │  Singapore MGF  │  │
│  │  Risk tiers │  GOVERN/MAP/      │  Certifiable    │  Hard guardrails│  │
│  │  Art. 9-50  │  MEASURE/MANAGE   │  AIMS (PDCA)    │  Safety agents  │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                      │                                      │
│                                      ▼                                      │
│  LAYER 2: GOVERNANCE POLICY                                                 │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                                                                       │  │
│  │  AI Governance Policy (Entry Point)                                   │  │
│  │  ├── Policy Statement & Scope                                         │  │
│  │  ├── Governance Bodies & Roles (Council, CAIO, RACI)                  │  │
│  │  ├── Risk Classification (3 Tiers)                                    │  │
│  │  ├── Control Requirements by Tier                                     │  │
│  │  ├── Monitoring & Incident Response                                   │  │
│  │  ├── Third-Party Vendor Controls                                      │  │
│  │  └── Review & Update Cadence                                          │  │
│  │                                                                       │  │
│  │  Supporting: 22 artifacts across 7 operational pillars                │  │
│  │                                                                       │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                      │                                      │
│                                      ▼                                      │
│  LAYER 3: ENFORCEMENT ARCHITECTURE                                          │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                                                                       │  │
│  │  7-Layer Governance Enforcement Pipeline (Fail-Closed)                │  │
│  │                                                                       │  │
│  │  L1: Compliance ──► L2: Budget ──► L3: RBAC ──► L4: HITL Gate        │  │
│  │                              │                                        │  │
│  │  L5: Circuit Breaker ◄──────┘                                        │  │
│  │       │                                                                │  │
│  │       ▼                                                                │  │
│  │  L6: Audit Log (SHA-256 integrity chain) ──► L7: Execution Wrapper    │  │
│  │                                                                       │  │
│  │  + Safety Agent (Governor) — independent monitoring & kill-switch     │  │
│  │  + Multi-Tenant Isolation — 6-layer tenant boundary enforcement       │  │
│  │  + Policy-as-Code Engine — OPA/Cedar compiled policies                │  │
│  │                                                                       │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                      │                                      │
│                                      ▼                                      │
│  LAYER 4: EXECUTIVE OVERSIGHT                                               │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                                                                       │  │
│  │  AI Governance Council    Quarterly Report    Board of Directors      │  │
│  │  7 members, monthly       KPI dashboard       Tier 3 approval         │  │
│  │  Quorum: 5/7              Trend analysis      Risk appetite           │  │
│  │  Authority: Tier 1-2      Incident stats      Strategic direction     │  │
│  │                                                                       │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Regulatory Framework Integration

### 3.1 How the 4 Frameworks Map Together

| Framework | Role in ProtoLabs Architecture | Certifiable? |
|-----------|-------------------------------|--------------|
| **EU AI Act** | Risk classification (Tier 1/2/3), mandatory controls per risk level, regulatory compliance | No (regulation, not standard) |
| **NIST AI RMF 1.0** | Lifecycle functions (GOVERN/MAP/MEASURE/MANAGE), 7 trustworthiness characteristics | No (voluntary framework) |
| **ISO/IEC 42001** | Management system structure (PDCA cycle), certifiable AIMS, audit-ready evidence | **Yes** — target Q1 2027 |
| **Singapore MGF** | Agentic-specific principles (hard guardrails, meaningful human accountability, multi-agent coordination) | No (voluntary framework) |

### 3.2 Cross-Framework Control Mapping

Every ProtoLabs governance control satisfies multiple frameworks simultaneously:

| Control | EU AI Act | NIST AI RMF | ISO 42001 | Singapore MGF |
|---------|-----------|-------------|-----------|---------------|
| Risk Classification | Art. 9(2) | MAP-2.1 | Cl. 6.1 | — |
| Model Card | Art. 11 | GV-7.1 | Cl. 7.5 | Transparency |
| Eval Suite | Art. 9(3) | MS-2.1 | Cl. 9.1 | Hard Guardrails |
| Human Oversight Plan | Art. 14 | MG-1.1 | Cl. 8.1 | Meaningful Human Accountability |
| Kill Switch | Art. 14(4)(a) | MG-1.1 | Cl. 8.1 | Hard Guardrails |
| Audit Trail | Art. 12 | GV-7.2 | Cl. 7.5 | Accountability |
| Incident Response | Art. 26(5) | MG-2.1 | Cl. 10.1 | Hard Guardrails |
| Safety Agent | Art. 14(3)(b) | MS-3.1 | Cl. 8.1 | Safety Agent |
| Vendor Controls | Art. 25, 28 | GV-6.1 | Cl. 8.1 | Hard Guardrails |
| Bias Assessment | Art. 9(2)(b) | MS-1.1 | Cl. 6.1 | Fairness |

### 3.3 Sector-Specific Compliance Layers

In addition to the 4 AI governance frameworks, ProtoLabs agents must comply with sector-specific standards based on client vertical:

| Vertical | Standard | AI Governance Implication |
|----------|----------|--------------------------|
| **Aerospace** | AS9100D, AS9102, FAA | Flight-critical parts require Tier 3 controls + formal verification |
| **Medical** | ISO 13485, FDA 510(k), MDR | Implant/surgical tool DFM requires biocompatibility validation + audit trail |
| **Automotive** | IATF 16949, PPAP | Production part quotes require PPAP-compliant documentation |
| **Defense** | ITAR, EAR | Technical data controls override explainability requirements |
| **General** | GDPR, CCPA | Client data handling, right to explanation |

---

## 4. Risk Classification — 3-Tier System

### 4.1 Tier Definitions

| Tier | Autonomy | Description | Examples | Approval |
|------|----------|-------------|----------|----------|
| **Tier 1** | Advisory | Read-only recommendations; no actions; human decides | DFM Router, CNC Agent, Injection Molding Agent, Sheet Metal Agent, 3D Printing Agent, Materials Agent, Vertical Agents, Trends Agent | Technical Owner + Security |
| **Tier 2** | Conditional | Can invoke tools/APIs; human approval for exceptions | Quote Generation, Production Scheduling, Quality Inspection | Governance Council |
| **Tier 3** | High | Acts independently within boundaries; exception-based review | Parameter Optimization, Autonomous Quality Control | Council + Board |

### 4.2 EU AI Act Mapping

| ProtoLabs Tier | EU AI Act Risk Level | Regulatory Obligation |
|----------------|---------------------|----------------------|
| Tier 1 | Limited-risk | Transparency obligations (Art. 50) |
| Tier 2 | Limited-to-High (re-assess per Annex III) | Risk management + human oversight (Art. 9, 14) |
| Tier 3 | High-risk (assumed until proven otherwise) | Full compliance (Art. 9-15, 26, 72) |

### 4.3 Control Requirements by Tier

| Control | Tier 1 | Tier 2 | Tier 3 |
|---------|--------|--------|--------|
| Model Card | ✓ Required | ✓ Required | ✓ + external audit |
| Eval Suite | ✓ Required | ✓ Required | ✓ + red-team exercise |
| Input Sanitization | ✓ Required | ✓ Required | ✓ Required |
| Human Oversight | Advisory (override available) | Mandatory (approval gate) | Mandatory (exception-based) |
| Kill Switch | Not required | ✓ <30s activation | ✓ <30s, 3 redundant paths |
| Audit Trail | ✓ Required | ✓ Required | ✓ Required |
| Bias Assessment | If demographic data | ✓ Required | ✓ + third-party review |
| Incident Response | ✓ Required | ✓ Required | ✓ + board notification |
| Pre-Deployment Gate | Automated CI/CD | Council review | Board approval |
| Post-Deployment Monitoring | Performance KPIs | Performance + drift + misuse | Full spectrum + continuous eval |
| Safety Agent | Not required | ✓ Required | ✓ Independent infrastructure |
| Formal Verification | Not required | Not required | ✓ Required (deterministic outputs) |
| Legal Review | Not required | If customer-facing | ✓ Required |
| PE Validation (structural) | N/A | If structural output | ✓ Required |

---

## 5. Enforcement Architecture — 7-Layer Pipeline

### 5.1 Pipeline Overview

Every agent execution passes through a 7-layer governance enforcement pipeline. The pipeline operates on a **fail-closed** principle: execution is blocked unless all checks explicitly pass.

```
User Request
     │
     ▼
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   LAYER 1   │───►│   LAYER 2   │───►│   LAYER 3   │───►│   LAYER 4   │
│ COMPLIANCE  │    │   BUDGET    │    │    RBAC     │    │    HITL     │
│    CHECK    │    │    CHECK    │    │    CHECK    │    │    GATE     │
│             │    │             │    │             │    │             │
│ • Jurisdiction│  │ • Tenant cap│    │ • SPIFFE ID │    │ • Confidence│
│ • Regulatory │  │ • User cap  │    │ • Permissions│   │ • Threshold │
│ • Data class │  │ • Agent cap │    │ • Delegation │   │ • Authority │
│ • Time rules │  │ • Run cap   │    │ • TTL/Scope  │   │   routing   │
└──────┬──────┘    └──────┬──────┘    └──────┬──────┘    └──────┬──────┘
       │                  │                  │                  │
       ▼                  ▼                  ▼                  ▼
   [BLOCK/PASS]       [BLOCK/PASS]       [BLOCK/PASS]       [BLOCK/PASS]
                                                     │
                                                     ▼
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   LAYER 5   │───►│   LAYER 6   │───►│   LAYER 7   │
│   CIRCUIT   │    │    AUDIT    │    │  EXECUTION  │
│   BREAKER   │    │    LOG      │    │   WRAPPER   │
│             │    │             │    │             │
│ • Error rate│    │ • Immutable │    │ • Sandbox   │
│ • Latency   │    │ • SHA-256   │    │ • Resource  │
│ • Loop det. │    │   chain     │    │   limits    │
│ • Dependency│    │ • Policy    │    │ • Tool inter│
│             │    │   decisions │    │ • Output val│
└──────┬──────┘    └──────┬──────┘    └──────┬──────┘
       │                  │                  │
       ▼                  ▼                  ▼
   [THROTTLE/         [APPEND]          [AGENT
    PAUSE/STOP]                         EXECUTES]
```

### 5.2 Layer Specifications

| Layer | Purpose | Key Checks | Failure Action | Target Latency |
|-------|---------|------------|----------------|----------------|
| **L1: Compliance** | Regulatory conformance | Jurisdiction, regulatory status, data classification, time rules | Block with compliance error | <5ms |
| **L2: Budget** | Cost control | Tenant/user/agent/skill/run budget caps | Block with budget error | <2ms |
| **L3: RBAC** | Authorization | SPIFFE identity, permissions, delegation chain, TTL, scope | Block with auth error | <5ms |
| **L4: HITL Gate** | Human oversight | Confidence score, threshold band, authority level, queue | Route to human or auto-approve | <10ms |
| **L5: Circuit Breaker** | System stability | Error rate, latency, loop detection, dependency health | Throttle → Pause → Stop | <1ms |
| **L6: Audit Log** | Accountability | Immutable record, integrity chain, policy decisions | Block if logging fails (fail-closed) | Async |
| **L7: Execution** | Safe execution | Sandbox, resource limits, tool interception, output validation | Agent executes with monitoring | — |
| **TOTAL** | | | | **<25ms target, <100ms max** |

### 5.3 Policy Engine Integration

The pipeline uses **OPA (Open Policy Agent)** or **Cedar** as the policy decision point:

```rego
package agent.execution

import future.keywords.if
import future.keywords.in

default allow := false

allow if {
    input.compliance.jurisdiction in input.agent.authorized_jurisdictions
    input.budget.remaining > input.request.estimated_cost
    input.rbac.permissions[_] == input.request.action
    input.circuit_breaker.state == "CLOSED"
}
```

**Policy-as-Code Status:**
- Architecture: ✅ Complete
- OPA/Cedar integration spec: ✅ Complete
- Checklist compilation to Rego: 🔴 In progress (Gap 1 remediation)
- CI/CD integration: 🔴 In progress

---

## 6. Safety Architecture

### 6.1 Safety Agent (Governor) Design

Every Tier 2+ agent has an independent Safety Agent that monitors, intercepts, and — when necessary — shuts down the primary agent.

```
User Input ──► ┌──────────────┐    ┌──────────────┐
               │  PRIMARY     │    │  SAFETY      │
               │  AGENT       │◄──►│  AGENT       │
               │              │    │  (Governor)  │
               │  - Processes │    │              │
               │  - Generates │    │  - Monitors  │
               │  - Acts      │    │  - Intercepts│
               │              │    │  - Shuts down│
               └──────┬───────┘    └──────┬───────┘
                      │                   │
                      v                   v
               ┌──────────────┐    ┌──────────────┐
               │  OUTPUT      │    │  ALERT       │
               │  GATE        │    │  ENGINE      │
               │              │    │              │
               │  - Validates │    │  - Logs      │
               │  - Releases  │    │  - Escalates │
               │  - Blocks    │    │  - Notifies  │
               └──────────────┘    └──────────────┘
```

### 6.2 Design Principles

| Principle | Implementation |
|-----------|---------------|
| **Separation of concerns** | Safety Agent is a separate process — not embedded in the primary agent |
| **Fail-closed** | If Safety Agent fails, primary agent is blocked by default |
| **Independent monitoring** | Safety Agent has its own logging, alerting, and health check |
| **Minimal surface** | Safety Agent has read-only access to primary agent outputs |
| **Defense in depth** | Safety Agent is one layer; it does not replace human oversight, evals, or input sanitization |

### 6.3 Kill Switch Architecture

| Activation Path | Target Latency | Scope |
|----------------|---------------|-------|
| Automated (Safety Agent detects violation) | <5 seconds | Single agent |
| Manual (operator dashboard) | <15 seconds | Single agent or fleet |
| Emergency (Governance Council) | <30 seconds | All Tier 2+ agents |

**Kill Switch States:**
```
NORMAL → THROTTLED → PAUSED → STOPPED → QUARANTINED
         (reduced    (no new   (all      (isolated
          capacity)   requests) stopped)  for RCA)
```

---

## 7. Multi-Tenant Isolation

### 7.1 Six-Layer Isolation Model

Each client (tenant) operates within isolated boundaries across 6 layers:

```
LAYER 6: AUDIT ISOLATION
  Per-tenant audit trails, separate encryption keys, integrity chain
                              ▲
LAYER 5: REASONING ISOLATION
  Isolated reasoning traces, chain-of-thought separation
                              ▲
LAYER 4: CONTEXT ISOLATION
  Separate RAG indices, vector stores, conversation history per tenant
                              ▲
LAYER 3: NETWORK ISOLATION
  VPC per tenant, micro-segmentation, encrypted inter-service comms
                              ▲
LAYER 2: STORAGE ISOLATION
  Separate databases, object stores, encryption keys per tenant
                              ▲
LAYER 1: COMPUTE ISOLATION
  Dedicated containers/VMs, resource quotas, sandbox boundaries
```

### 7.2 Per-Client Policy Enforcement

Each client order carries contractual and regulatory obligations that are compiled into guardrails per order:

| Client Type | Policy Sources | Enforcement |
|-------------|---------------|-------------|
| Aerospace (AS9100D) | ITAR controls + AS9102 FAI requirements + Tier 3 controls | Compiled into OPA policies per order |
| Medical (ISO 13485) | FDA 510(k) + biocompatibility + audit trail requirements | Compiled into OPA policies per order |
| Automotive (IATF 16949) | PPAP documentation + SPC requirements | Compiled into OPA policies per order |
| General | GDPR + standard DFM controls | Default policy set |

**Status:** Architecture complete. Per-order compilation in progress (Gap 5 remediation).

---

## 8. Agent Fleet — Current State & Roadmap

### 8.1 Current Fleet (10 Agents — All Tier 1)

| Agent | Tier | Model Card | Eval Suite | Safety Agent | Status |
|-------|------|-----------|------------|--------------|--------|
| DFM Router | T1 | ✓ | ✓ | — | ✅ Production |
| CNC Machining | T1 | ✓ | ✓ | — | ✅ Production |
| Injection Molding | T1 | ✓ | ✓ | — | ✅ Production |
| Sheet Metal | T1 | ✓ | ✓ | — | ✅ Production |
| 3D Printing | T1 | ✓ | ✓ | — | ✅ Production |
| Materials Selection | T1 | ✓ | ✓ | — | ✅ Production |
| Vertical — Aerospace | T1 | ✓ | ✓ | — | ✅ Production |
| Vertical — Medical | T1 | ✓ | ✓ | — | ✅ Production |
| Vertical — Automotive | T1 | ✓ | ✓ | — | ✅ Production |
| Trends & Strategy | T1 | ✓ | ✓ | — | ✅ Production |

### 8.2 Planned Additions

| Agent | Tier | Timeline | Approval Required | Governance Gate |
|-------|------|----------|-------------------|-----------------|
| Quote Generation Bot | T2 | Q3 2026 | Governance Council | Council review + Safety Agent |
| Production Scheduler | T2 | Q4 2026 | Governance Council | Council review + Safety Agent |
| Parameter Optimizer | T3 | 2027 | Council + Board | Board session + formal verification |
| Autonomous QC | T3 | 2027 | Council + Board | Board session + formal verification |

### 8.3 CAD AI Evaluation System (WP-CAD)

A new strategic initiative for AI-powered CAD evaluation:

| Attribute | Value |
|-----------|-------|
| **Priority** | P0 Strategic |
| **Timeline** | 12 weeks |
| **Budget** | $600K |
| **Scope** | Multi-format CAD parsing, feature recognition, VLM analysis, DFM rule engine |
| **Governance** | Tier 1 (advisory) with Tier 2 upgrade path for autonomous recommendations |
| **Key Risk** | Multi-modal CAD guardrails (Gap 4 remediation required before production) |

---

## 9. Policy-as-Code Roadmap

### 9.1 Gap Summary

A comprehensive assessment against state-of-the-art Policy-as-Code research identified **6 genuine gaps** (4 claimed gaps were already addressed by existing architecture):

| Gap | Status | Impact | Effort |
|-----|--------|--------|--------|
| **Gap 1:** Checklists not executable | Architecture exists, needs implementation | Blocks automated enforcement | 6.5 sprints |
| **Gap 3:** No formal verification | No architecture exists | Blocks Tier 3 safety-critical | 10.5 sprints |
| **Gap 4:** No multi-modal CAD guardrails | No architecture exists | Blocks CAD system deployment | 6 sprints |
| **Gap 5:** No policy tree with inheritance | Architecture exists, needs extension | Blocks cross-framework compliance | 6 sprints |
| **Gap 7:** No adversarial testing framework | Partial architecture exists | Blocks Tier 2+ deployment | 7.5 sprints |
| **Gap 10:** No control tax analysis | No architecture exists | Limits optimization | 5.5 sprints |
| **TOTAL** | | | **42 sprints** |

### 9.2 What Already Exists (Correcting Misconceptions)

| Claimed Gap | Actual State |
|-------------|-------------|
| No Policy Engine | ✅ 7-Layer Pipeline with OPA/Cedar, fail-closed, <25ms |
| No Runtime Compliance | ✅ Safety Agent + continuous compliance in L1 |
| No Client-Specific Enforcement | ✅ 6-Layer Multi-Tenant Isolation + per-tenant budgets |
| No Provenance Chain | ✅ L6 Audit Log with SHA-256 integrity chain |

### 9.3 Implementation Phases

```
PHASE 1 (Sprints 1-6): Foundation — $180K
├── Gap 1: Executable Checklists (compile YAML → OPA Rego)
├── Gap 5: Policy Tree (hierarchical policies with conflict resolution)
└── Gap 7: Adversarial Testing (OWASP LLM Top 10 + agentic attacks)

PHASE 2 (Sprints 7-12): Production Readiness — $240K
├── Gap 4: Multi-Modal CAD Guardrails (geometry-level input validation)
├── Gap 7: Adversarial Testing (complete CI/CD integration)
└── Gap 10: Control Tax (cost/benefit analysis per control)

PHASE 3 (Sprints 13-18): Advanced Capabilities — $180K
├── Gap 3: Formal Verification (Lean 4 for Tier 3 deterministic outputs)
└── Gap 10: Control Tax optimization (ongoing)

TOTAL: 18 sprints, ~$600K, avg 3.3 engineers
```

Detailed remediation plan: [Policy-as-Code Remediation Plan](policy-as-code-remediation-plan.md)

---

## 10. ISO 42001 Certification Roadmap

### 10.1 Current Readiness

```
Clause 4 — Context of the Organisation        ████████████░░░░  80%
Clause 5 — Leadership                         █████████████████░  85%
Clause 6 — Planning                           ██████████████████░  90%
Clause 7 — Support                            █████████████████░  85%
Clause 8 — Operation                          ████████████████░░  80%
Clause 9 — Performance Evaluation             ██████████████████░  90%
Clause 10 — Improvement                       █████████████████░  85%
Annex A — AI Controls                         █████████████████░  85%
Annex B — Implementation Guidance             █████████████████░  85%

OVERALL READINESS                             █████████████████░░  87%
```

### 10.2 Certification Timeline

| Phase | Timeline | Activities |
|-------|----------|------------|
| **Framework Complete** | Q2 2026 ✅ | 23 artifacts created, 87% readiness |
| **Evidence Populate** | Q3 2026 | Real data in all artifacts, internal audit |
| **Pre-Assessment** | Q4 2026 | TÜV SÜD or BSI pre-audit, gap closure |
| **Certification** | Q1 2027 | Formal audit, certificate issued |

### 10.3 Remaining 13% to Certification

| Gap | Action | Timeline |
|-----|--------|----------|
| Execution evidence | Populate artifacts with real production data | 8 weeks |
| External audit engagement | Procure TÜV SÜD or BSI | 4 weeks |
| Board resolution | Formal adoption of ISO 42001 | 1 board meeting |

---

## 11. Board Governance

### 11.1 Decision Authority

| Decision | Authority | Escalation |
|----------|-----------|------------|
| Tier 1 deployment | Technical Owner + Security | None (notify Council) |
| Tier 2 deployment | Governance Council | Board (if critical) |
| Tier 3 deployment | Council recommends → Board approves | — |
| Risk tier disputes | Council (final) | — |
| Policy amendments | Council (majority) | Board (if major) |
| Vendor integration | Council | Board (if customer-facing) |
| Incident RCA (Sev1) | Council | Board notification |
| Agent retirement | Council | Board (Tier 3) |

### 11.2 Governance Council

| Attribute | Detail |
|-----------|--------|
| **Composition** | CAIO (Chair), Head of Engineering, DPO, Legal Counsel, Head of Internal Audit, Security Lead, VP Product |
| **Quorum** | 5 of 7 members |
| **Cadence** | Monthly (90 min); emergency <24 hours |
| **Dissent Rights** | Any member may force Board escalation |

### 11.3 Reporting to Board

| Report | Frequency | Content |
|--------|-----------|---------|
| Quarterly Governance Report | Quarterly | KPI dashboard, incident stats, risk posture, certification progress |
| Sev1 Incident Report | Within 2 hours of incident | Root cause, containment, remediation |
| ISO 42001 Progress | Quarterly | Readiness scorecard, audit findings |
| Policy-as-Code Progress | Quarterly | Gap remediation status, automation metrics |

### 11.4 KPIs Reported to Board

| KPI | Target | Current |
|-----|--------|---------|
| DFM Accuracy (fleet) | >90% | TBD (eval in progress) |
| Sev1 Incidents per quarter | 0 | 0 |
| Governance Gate Pass Rate (first attempt) | >85% | TBD |
| Audit Trail Completeness | 100% | TBD |
| Kill Switch Activation Time | <30s | TBD |
| ISO 42001 Readiness | 100% by Q1 2027 | 87% |
| AI Literacy Training Completion | >95% | TBD |

---

## 12. Artifact Map

| # | Artifact | Location | Purpose |
|---|----------|----------|---------|
| 1 | AI Governance Policy | `governance/ai-governance-policy.md` | Entry point — scope, bodies, tiers, controls |
| 2 | Client Policy Summary | `governance/ai-policy-client-summary.md` | Client-facing governance summary |
| 3 | Council Charter | `governance/05-cross-cutting/ai-governance-council-charter.md` | Council composition, authority, process |
| 4 | Approval Thresholds | `governance/05-cross-cutting/approval-thresholds-by-tier.md` | Decision rules per tier |
| 5 | Roles & RACI | `governance/05-cross-cutting/governance-roles-raci.md` | Accountability matrix |
| 6 | Agent Tier Classification | `governance/01-discovery-governance/templates/agent-tier-classification.yaml` | Classification methodology |
| 7 | EU AI Act Risk Classification | `governance/01-discovery-governance/checklists/eu-ai-act-risk-classification.yaml` | Regulatory mapping |
| 8 | Opportunity Register | `governance/01-discovery-governance/ai-opportunity-register.md` | AI use case tracking |
| 9 | Model Card Checklist | `governance/02-development-governance/checklists/model-card-completeness-checklist.yaml` | 32 validation items |
| 10 | Pre-Deployment Gate | `governance/02-development-governance/checklists/pre-deployment-gate.yaml` | Production gate checklist |
| 11 | Prompt Registry | `governance/02-development-governance/prompt-registry.md` | Prompt version tracking |
| 12 | Safety Agent Architecture | `governance/03-runtime-governance/agentic-workflows/safety-agent-architecture.md` | Governor spec |
| 13 | Enforcement Pipeline | `governance/03-runtime-governance/agentic-workflows/governance-enforcement-pipeline.md` | 7-layer pipeline |
| 14 | Multi-Agent Governance | `governance/03-runtime-governance/agentic-workflows/multi-agent-governance-framework.md` | Agent interaction governance |
| 15 | Multi-Tenant Isolation | `governance/03-runtime-governance/agentic-workflows/multi-tenant-isolation.md` | 6-layer isolation |
| 16 | HITL Patterns | `governance/03-runtime-governance/agentic-workflows/human-in-the-loop-patterns.md` | Human oversight patterns |
| 17 | Autonomous Decision Governance | `governance/03-runtime-governance/agentic-workflows/autonomous-decision-governance.md` | Decision authority matrix |
| 18 | Incident Severity | `governance/04-operational-governance/incident-severity-classification.md` | Sev1-Sev4 definitions |
| 19 | Internal Audit Plan | `governance/04-operational-governance/aims-internal-audit-plan.md` | ISO 42001 Cl. 9.2 |
| 20 | Vendor Controls | `governance/05-cross-cutting/third-party-ai-vendor-controls.md` | Third-party governance |
| 21 | Objectives & KPIs | `governance/06-executive/aims-objectives-and-kpis.md` | 10 SMART objectives |
| 22 | Risk Appetite Framework | `governance/06-executive/ai-risk-appetite-framework.md` | Board risk tolerance |
| 23 | Quarterly Report Template | `governance/06-executive/quarterly-governance-report.md` | Board reporting |

---

## 13. The Ask — Board Actions Required

| # | Action | Rationale | Timeline |
|---|--------|-----------|----------|
| **1** | **Approve governance framework as enterprise standard** | 23 artifacts operational, 87% ISO 42001 readiness | Immediate |
| **2** | **Approve board resolution adopting ISO 42001** | Formal commitment to AIMS certification; required for TÜV SÜD/BSI engagement | Next board meeting |
| **3** | **Authorize Policy-as-Code remediation budget** | $600K over 18 sprints to close 6 gaps | Q2 2026 |
| **4** | **Direct teams to populate execution evidence** | 8-week effort to fill artifacts with real production data | Q3 2026 |
| **5** | **Authorize certification body engagement** | TÜV SÜD or BSI pre-assessment Q4 2026, certification Q1 2027 | Q3 2026 |

---

## Appendix A: Glossary

| Term | Definition |
|------|------------|
| **AIMS** | AI Management System (ISO/IEC 42001) |
| **CAIO** | Chief AI Officer |
| **HITL** | Human-in-the-Loop |
| **OPA** | Open Policy Agent |
| **PaC** | Policy-as-Code |
| **PDCA** | Plan-Do-Check-Act (ISO management cycle) |
| **RACI** | Responsible, Accountable, Consulted, Informed |
| **RBAC** | Role-Based Access Control |
| **SPIFFE** | Secure Production Identity Framework for Everyone |
| **VLM** | Vision-Language Model |

---

## Appendix B: Regulatory Reference

| Regulation | Relevance | ProtoLabs Mapping |
|------------|-----------|-------------------|
| EU AI Act (2024/1689) | Risk-based AI regulation | Tier classification, Art. 9-50 controls |
| NIST AI RMF 1.0 | Voluntary risk management framework | GOVERN/MAP/MEASURE/MANAGE functions |
| ISO/IEC 42001:2023 | Certifiable AI management system | PDCA cycle, Annex A controls |
| Singapore MGF | Agentic AI governance principles | Hard guardrails, safety agents |
| GDPR | Data protection | Client data handling, right to explanation |
| ITAR/EAR | Export controls | Technical data restrictions for defense clients |
| AS9100D | Aerospace quality | Flight-critical part governance |
| ISO 13485 | Medical device quality | Medical implant governance |
| IATF 16949 | Automotive quality | Production part governance |

---

*This document is version-controlled and auditable. Unauthorized modifications void governance compliance claims.*
