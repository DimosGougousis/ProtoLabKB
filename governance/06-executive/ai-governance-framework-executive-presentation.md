# ProtoLabs AI Governance Framework
## Executive Overview — Architecture & Readiness

> **Presentation Date:** April 28, 2026
> **Version:** 2.0 (updated to reflect enforcement architecture + PaC assessment)
> **Presented by:** Chief AI Officer, ProtoLabs AI Governance Office
> **Classification:** Board Confidential
> **Duration:** 30 minutes + 15 minutes Q&A
> **Source Document:** `docs/governance-framework-architecture.md`

---

## Slide 1: Title

# ProtoLabs AI Governance Framework
## Depth, Breadth, and Certification Readiness

**A Comprehensive View of Enterprise AI Governance**
**23 Artifacts · 7 Pillars · 4 Frameworks · 1 Unified System**

*April 28, 2026 | ProtoLabs Executive Leadership*

---

## Slide 2: The Governance Stack — One Visual

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                                                                                 │
│                        PROTOLABS AI GOVERNANCE STACK                            │
│                                                                                 │
│  ┌───────────────────────────────────────────────────────────────────────────┐  │
│  │                        REGULATORY FRAMEWORKS                               │  │
│  │                                                                           │  │
│  │   ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  │  │
│  │   │ EU AI    │  │ NIST AI  │  │ ISO/IEC  │  │ GDPR +   │  │ Sector   │  │  │
│  │   │ Act      │  │ RMF 1.0  │  │ 42001    │  │ Privacy  │  │ Standards│  │  │
│  │   │          │  │          │  │          │  │          │  │          │  │  │
│  │   │ Risk-    │  │ GOVERN   │  │ Certif-  │  │ Data     │  │ AS9100D  │  │  │
│  │   │ based    │  │ MAP      │  │ iable    │  │ Protect  │  │ ISO 13485│  │  │
│  │   │ tiers    │  │ MEASURE  │  │ AIMS     │  │          │  │ IATF     │  │  │
│  │   │          │  │ MANAGE   │  │          │  │          │  │ 16949    │  │  │
│  │   └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘  │  │
│  │        └──────────────┴──────────────┴──────────────┴──────────────┘        │  │
│  └───────────────────────────────────────────────────────────────────────────┘  │
│                                      │                                          │
│                                      ▼                                          │
│  ┌───────────────────────────────────────────────────────────────────────────┐  │
│  │                        GOVERNANCE POLICY LAYER                             │  │
│  │                                                                           │  │
│  │   ┌─────────────────────────────────────────────────────────────────┐    │  │
│  │   │              AI GOVERNANCE POLICY (Entry Point)                  │    │  │
│  │   │                                                                  │    │  │
│  │   │  1. Policy Statement  5. Control Requirements                    │    │  │
│  │   │  2. Definitions       6. Monitoring & Incidents                  │    │  │
│  │   │  3. Governance Bodies 7. Third-Party Controls                    │    │  │
│  │   │  4. Risk Classification 8. Review & Updates                      │    │  │
│  │   └─────────────────────────────────────────────────────────────────┘    │  │
│  └───────────────────────────────────────────────────────────────────────────┘  │
│                                      │                                          │
│                                      ▼                                          │
│  ┌───────────────────────────────────────────────────────────────────────────┐  │
│  │                        OPERATIONAL PILLARS                                 │  │
│  │                                                                           │  │
│  │   ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐          │  │
│  │   │DISCOVERY│ │DEVELOP- │ │RUNTIME  │ │OPERATIO-│ │CROSS-   │          │  │
│  │   │         │ │MENT     │ │         │ │NAL      │ │CUTTING  │          │  │
│  │   │ Risk    │ │ Eval-   │ │ Safety  │ │ Monitor │ │ RACI    │          │  │
│  │   │ Intake  │ │ Driven  │ │ Agents  │ │ Audit   │ │ Vendor  │          │  │
│  │   │ Oppor-  │ │ Model   │ │ Kill    │ │ Incident│ │ Reten-  │          │  │
│  │   │ tunity  │ │ Cards   │ │ Switch  │ │ Retire  │ │ tion    │          │  │
│  │   │ Register│ │ Prompts │ │ Guard-  │ │ Improve │ │ Comms   │          │  │
│  │   │         │ │         │ │ rails   │ │         │ │         │          │  │
│  │   └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘          │  │
│  │        └───────────┴───────────┴───────────┴───────────┘                │  │
│  └───────────────────────────────────────────────────────────────────────────┘  │
│                                      │                                          │
│                                      ▼                                          │
│  ┌───────────────────────────────────────────────────────────────────────────┐  │
│  │                        EXECUTIVE OVERSIGHT                                 │  │
│  │                                                                           │  │
│  │   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                   │  │
│  │   │ AI Governance│  │ Quarterly    │  │ Board of     │                   │  │
│  │   │ Council      │  │ Governance   │  │ Directors    │                   │  │
│  │   │              │  │ Report       │  │              │                   │  │
│  │   │ 7 members    │  │ KPI Dashboard│  │ Tier 3       │                   │  │
│  │   │ Monthly      │  │ Trend Analysis│ │ Approval     │                   │  │
│  │   │ Quorum: 5/7  │  │ Incident Stats│ │ Risk Appetite│                   │  │
│  │   └──────────────┘  └──────────────┘  └──────────────┘                   │  │
│  └───────────────────────────────────────────────────────────────────────────┘  │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## Slide 3: The Full Artifact Tree — 23 Documents

```
governance/
│
├── ai-governance-policy.md .............................. ★ ENTRY POINT
│   └── 8 sections: Policy → Scope → Bodies → RACI → Risk → Controls
│                                                    → Monitoring → Review
│
├── ai-policy-client-summary.md .......................... Client-facing summary
│
├── 01-discovery-governance/
│   └── ai-opportunity-register.md ....................... ISO 42001 Cl. 6.1
│       5 opportunities tracked, scored by value × feasibility
│
├── 02-development-governance/
│   ├── checklists/
│   │   └── model-card-completeness-checklist.yaml ....... 32 validation items
│   │       Critical/High/Medium gates per risk tier
│   │
│   └── prompt-registry.md ............................... Centralized prompt
│       version tracking across all 10 agents
│
├── 03-runtime-governance/
│   └── agentic-workflows/
│       └── safety-agent-architecture.md ................. Governor spec
│           Monitoring · Interception · Kill Switch · Fail-closed design
│
├── 04-operational-governance/
│   ├── incident-severity-classification.md .............. ★ Sev1-Sev4
│   │   Decision tree · Response SLAs · Escalation paths
│   │
│   ├── aims-internal-audit-plan.md ...................... ISO 42001 Cl. 9.2
│   │   Annual calendar · Clause-by-clause criteria
│   │
│   ├── aims-corrective-action-template.md ............... 8D RCA template
│   ├── aims-management-review-agenda.md ................. ISO 42001 Cl. 9.3
│   ├── aims-improvement-register.md ..................... ISO 42001 Cl. 10.2
│   ├── aims-evaluation-repository-index.md .............. Fleet eval results
│   ├── model-retirement-procedure.md .................... Lifecycle closure
│   └── regulatory-change-monitor.md ..................... Ongoing compliance
│
├── 05-cross-cutting/
│   ├── ai-governance-council-charter.md ................. ★ Council ops
│   │   Composition · Authority · Decision process · Dissent rights
│   │
│   ├── approval-thresholds-by-tier.md ................... ★ Decision rules
│   │   Tier 1: Tech+Sec · Tier 2: Council · Tier 3: Board
│   │
│   ├── third-party-ai-vendor-controls.md ................ Vendor governance
│   │   Assessment checklist · DPA · Provenance registry · Exit strategy
│   │
│   ├── aims-signing-authority-matrix.md ................. Who signs what
│   ├── aims-competence-matrix.md ........................ Role → skills map
│   ├── aims-communication-plan.md ....................... Internal + external
│   ├── aims-document-retention-schedule.md .............. 7-year retention
│   └── governance-framework-changelog.md ................ Version history
│
└── 06-executive/
    └── aims-objectives-and-kpis.md ...................... 10 SMART objectives
        Fleet accuracy · Incident count · Gate pass rate · Training
```

---

## Slide 4: Risk Tier Architecture

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                                                                                 │
│                    RISK TIER ARCHITECTURE — 3 TIERS                             │
│                                                                                 │
│  ┌─────────────────────────────────────────────────────────────────────────┐   │
│  │  TIER 1 — ADVISORY                                                      │   │
│  │  ─────────────────                                                      │   │
│  │  Autonomy: Read-only recommendations                                    │   │
│  │  Examples: DFM Router, CNC Agent, Injection Molding Agent,              │   │
│  │            Sheet Metal Agent, 3D Printing Agent, Materials Agent         │   │
│  │  Approval: Technical Owner + Security Lead                              │   │
│  │  Gate: Automated CI/CD                                                  │   │
│  │  Safety Agent: Not required                                             │   │
│  │  Kill Switch: Not required                                              │   │
│  │  EU AI Act: Limited-risk                                                │   │
│  │                                                                         │   │
│  │  Required Artifacts:                                                    │   │
│  │  ✓ Model Card  ✓ Eval Suite  ✓ Input Sanitization                      │   │
│  │  ✓ Tier Classification  ✓ Source Grounding                             │   │
│  └─────────────────────────────────────────────────────────────────────────┘   │
│                                      │                                          │
│                                      ▼                                          │
│  ┌─────────────────────────────────────────────────────────────────────────┐   │
│  │  TIER 2 — CONDITIONAL AUTONOMY                                          │   │
│  │  ────────────────────────────                                           │   │
│  │  Autonomy: Tool/API invocation; human approval for exceptions           │   │
│  │  Examples: Quote Generation, Production Scheduling, Quality Inspection  │   │
│  │  Approval: Governance Council (7 members, quorum 5/7)                   │   │
│  │  Gate: Council review meeting                                           │   │
│  │  Safety Agent: Required                                                 │   │
│  │  Kill Switch: Required (<30s activation)                                │   │
│  │  EU AI Act: Limited-to-High risk (re-assess per Annex III)              │   │
│  │                                                                         │   │
│  │  Required Artifacts (all Tier 1, plus):                                 │   │
│  │  ✓ Risk Assessment  ✓ Human Oversight Plan  ✓ Kill Switch Test          │   │
│  │  ✓ Legal Review (if customer-facing)  ✓ Incident Response Plan          │   │
│  │  ✓ Bias Assessment                                                      │   │
│  └─────────────────────────────────────────────────────────────────────────┘   │
│                                      │                                          │
│                                      ▼                                          │
│  ┌─────────────────────────────────────────────────────────────────────────┐   │
│  │  TIER 3 — HIGH AUTONOMY                                                 │   │
│  │  ──────────────────────                                                 │   │
│  │  Autonomy: Independent action within boundaries; exception-based review │   │
│  │  Examples: Parameter Optimizer, Autonomous Quality Control              │   │
│  │  Approval: Governance Council → Board of Directors                      │   │
│  │  Gate: Board session                                                    │   │
│  │  Safety Agent: Required (independent infrastructure)                    │   │
│  │  Kill Switch: Required (3 redundant paths)                              │   │
│  │  EU AI Act: High-risk (assumed until proven otherwise)                  │   │
│  │                                                                         │   │
│  │  Required Artifacts (all Tier 2, plus):                                 │   │
│  │  ✓ Red Team Exercise  ✓ PE Validation (if structural)                   │   │
│  │  ✓ Board Incident Response  ✓ Continuous Monitoring Spec                │   │
│  │  ✓ Autonomous Decision Governance  ✓ Vendor Lock-In Plan                │   │
│  └─────────────────────────────────────────────────────────────────────────┘   │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## Slide 5: Governance Council — Decision Authority

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                                                                                 │
│                    AI GOVERNANCE COUNCIL — COMPOSITION                          │
│                                                                                 │
│                         ┌─────────────────┐                                     │
│                         │   CAIO (Chair)  │                                     │
│                         │   Board-delegated│                                    │
│                         │   authority      │                                    │
│                         └────────┬────────┘                                     │
│                                  │                                              │
│            ┌─────────────────────┼─────────────────────┐                        │
│            │                     │                     │                        │
│   ┌────────▼────────┐  ┌────────▼────────┐  ┌────────▼────────┐               │
│   │ Head of         │  │ Data Protection │  │ Legal Counsel   │               │
│   │ Engineering     │  │ Officer         │  │                 │               │
│   │                 │  │                 │  │                 │               │
│   │ Technical       │  │ GDPR, Privacy,  │  │ Regulatory,     │               │
│   │ feasibility     │  │ Data handling   │  │ Contracts       │               │
│   └─────────────────┘  └─────────────────┘  └─────────────────┘               │
│                                                                                 │
│   ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐               │
│   │ Head of         │  │ Security Lead   │  │ VP Product      │               │
│   │ Internal Audit  │  │                 │  │                 │               │
│   │                 │  │ Cybersecurity,  │  │ Business        │               │
│   │ Audit readiness,│  │ Adversarial     │  │ objectives,     │               │
│   │ Evidence quality│  │ resilience      │  │ Client impact   │               │
│   └─────────────────┘  └─────────────────┘  └─────────────────┘               │
│                                                                                 │
│  ┌───────────────────────────────────────────────────────────────────────────┐  │
│  │                                                                           │  │
│  │   AUTHORITY MATRIX                                                        │  │
│  │                                                                           │  │
│  │   ┌──────────────────────┬──────────────────┬──────────────────────┐     │  │
│  │   │ Decision             │ Authority        │ Escalation           │     │  │
│  │   ├──────────────────────┼──────────────────┼──────────────────────┤     │  │
│  │   │ Tier 1 deployment    │ Approve          │ None (notify)        │     │  │
│  │   │ Tier 2 deployment    │ Approve          │ Board (if critical)  │     │  │
│  │   │ Tier 3 deployment    │ Recommend        │ Board (final)        │     │  │
│  │   │ Risk tier disputes   │ Final decision   │ —                    │     │  │
│  │   │ Policy amendments    │ Approve (majority)│ Board (if major)    │     │  │
│  │   │ Vendor integration   │ Approve          │ Board (if customer)  │     │  │
│  │   │ Incident RCA         │ Approve          │ Board (Sev1)         │     │  │
│  │   │ Agent retirement     │ Approve          │ Board (Tier 3)       │     │  │
│  │   └──────────────────────┴──────────────────┴──────────────────────┘     │  │
│  │                                                                           │  │
│  │   Meeting Cadence: Monthly (90 min) · Emergency: <24 hours               │  │
│  │   Quorum: 5 of 7 · Dissent rights: Any member may force Board escalation │  │
│  │                                                                           │  │
│  └───────────────────────────────────────────────────────────────────────────┘  │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## Slide 6: Incident Response Architecture

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                                                                                 │
│                    INCIDENT RESPONSE — 4 SEVERITY LEVELS                        │
│                                                                                 │
│  ┌─────────────────────────────────────────────────────────────────────────┐   │
│  │  SEV1 — CRITICAL                                                        │   │
│  │  ────────────────                                                       │   │
│  │  Trigger: Safety harm · Data breach · Regulatory violation              │   │
│  │  Response: 15 min · Containment: 1 hour · RCA: 48 hours                │   │
│  │  Escalation: CAIO + Board (within 2 hours)                             │   │
│  │  Containment: Kill switch · Quarantine · Customer notification          │   │
│  │  Target: 0 per quarter                                                  │   │
│  └─────────────────────────────────────────────────────────────────────────┘   │
│                                                                                 │
│  ┌─────────────────────────────────────────────────────────────────────────┐   │
│  │  SEV2 — HIGH                                                            │   │
│  │  ──────────                                                             │   │
│  │  Trigger: Accuracy >10% degradation · Kill switch failure               │   │
│  │  Response: 2 hours · Containment: 4 hours · RCA: 5 days                │   │
│  │  Escalation: Governance Council (within 4 hours)                        │   │
│  │  Containment: Safe mode · Rollback · Enhanced monitoring                │   │
│  └─────────────────────────────────────────────────────────────────────────┘   │
│                                                                                 │
│  ┌─────────────────────────────────────────────────────────────────────────┐   │
│  │  SEV3 — MEDIUM                                                          │   │
│  │  ────────────                                                           │   │
│  │  Trigger: Drift beyond tolerance · Audit trail gaps                     │   │
│  │  Response: 24 hours · Containment: 48 hours · RCA: 10 days             │   │
│  │  Escalation: Technical Owner → Policy Owner                             │   │
│  └─────────────────────────────────────────────────────────────────────────┘   │
│                                                                                 │
│  ┌─────────────────────────────────────────────────────────────────────────┐   │
│  │  SEV4 — LOW                                                             │   │
│  │  ─────────                                                              │   │
│  │  Trigger: Cosmetic issues · Logging noise                               │   │
│  │  Response: 1 week · Fix in next sprint                                  │   │
│  └─────────────────────────────────────────────────────────────────────────┘   │
│                                                                                 │
│  ┌───────────────────────────────────────────────────────────────────────────┐  │
│  │                                                                           │  │
│  │   LIFECYCLE:  DETECT → CLASSIFY → CONTAIN → INVESTIGATE →               │  │
│  │               REMEDIATE → REVIEW → CLOSE                                 │  │
│  │                                                                           │  │
│  │   REGULATORY: EU AI Act Art. 26(5) · GDPR Art. 33 · ITAR §127.12       │  │
│  │                                                                           │  │
│  └───────────────────────────────────────────────────────────────────────────┘  │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## Slide 7: ISO 42001 Readiness — Current State

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                                                                                 │
│                    ISO/IEC 42001 READINESS SCORECARD                            │
│                                                                                 │
│   Clause 4 — Context of the Organisation        ████████████░░░░  80%          │
│                                                                                 │
│   Clause 5 — Leadership                          █████████████████░  85%        │
│                                                                                 │
│   Clause 6 — Planning                            ██████████████████░  90%        │
│                                                                                 │
│   Clause 7 — Support                             █████████████████░  85%        │
│                                                                                 │
│   Clause 8 — Operation                           ████████████████░░  80%        │
│                                                                                 │
│   Clause 9 — Performance Evaluation              ██████████████████░  90%        │
│                                                                                 │
│   Clause 10 — Improvement                        █████████████████░  85%        │
│                                                                                 │
│   Annex A — AI Controls                          █████████████████░  85%        │
│                                                                                 │
│   Annex B — Implementation Guidance              █████████████████░  85%        │
│                                                                                 │
│   ─────────────────────────────────────────────────────────────────────────    │
│   OVERALL READINESS                              █████████████████░░  87%       │
│                                                                                 │
│   ┌─────────────────────────────────────────────────────────────────────────┐   │
│   │  REMAINING 13% TO CERTIFICATION:                                        │   │
│   │  • Execution evidence (real data in artifacts) — 8 weeks team effort    │   │
│   │  • External audit engagement (TÜV SÜD or BSI) — Procurement             │   │
│   │  • Board resolution adopting ISO 42001 — Board approval                 │   │
│   │  TARGET: Q1 2027                                                         │   │
│   └─────────────────────────────────────────────────────────────────────────┘   │
│                                                                                 │
│   Full analysis: docs/iso-42001-gap-analysis.md                                │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## Slide 8: Framework Integration Map

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                                                                                 │
│                    HOW THE 4 FRAMEWORKS INTEGRATE                               │
│                                                                                 │
│   ┌─────────────────────────────────────────────────────────────────────────┐   │
│   │                                                                         │   │
│   │    EU AI ACT                    NIST AI RMF 1.0                         │   │
│   │    ────────                     ───────────────                         │   │
│   │    Risk tiers:                  Functions:                              │   │
│   │    • Unacceptable    ──────►   • GOVERN  (policy, roles, culture)      │   │
│   │    • High            ──────►   • MAP     (context, categorization)     │   │
│   │    • Limited         ──────►   • MEASURE (evals, metrics)              │   │
│   │    • Minimal         ──────►   • MANAGE (response, monitoring)         │   │
│   │                                                                         │   │
│   │    Articles 9-15, 26, 72       7 Characteristics:                       │   │
│   │    map to governance           Valid, Safe, Secure, Accountable,        │   │
│   │    controls per tier           Explainable, Private, Fair               │   │
│   │                                                                         │   │
│   └─────────────────────────────────────────────────────────────────────────┘   │
│                                      │                                          │
│                                      ▼                                          │
│   ┌─────────────────────────────────────────────────────────────────────────┐   │
│   │                                                                         │   │
│   │    ISO/IEC 42001               SINGAPORE MGF                           │   │
│   │    ─────────────               ─────────────                            │   │
│   │    PDCA Cycle:                 Principles:                              │   │
│   │    • PLAN  (Cl. 4-6)  ──────► • Hard Guardrails                        │   │
│   │    • DO    (Cl. 7-8)  ──────► • Meaningful Human Accountability        │   │
│   │    • CHECK (Cl. 9)    ──────► • Multi-Agent Coordination               │   │
│   │    • ACT   (Cl. 10)                                                    │   │
│   │                                                                         │   │
│   │    Certifiable by              Agentic-specific:                        │   │
│   │    external auditor            • Tier classification                    │   │
│   │    (TÜV SÜD / BSI)            • Tool-use risk modeling                  │   │
│   │                                • Safety agent architecture              │   │
│   │                                                                         │   │
│   └─────────────────────────────────────────────────────────────────────────┘   │
│                                      │                                          │
│                                      ▼                                          │
│   ┌─────────────────────────────────────────────────────────────────────────┐   │
│   │                                                                         │   │
│   │    PROTOLABS GOVERNANCE LAYER (What We Built)                           │   │
│   │                                                                         │   │
│   │    Maps all 4 frameworks into:                                          │   │
│   │    • 23 governance artifacts (policy, charters, checklists, templates)  │   │
│   │    • 7 operational pillars (discovery → development → runtime → ops)    │   │
│   │    • 3 risk tiers with explicit approval thresholds                     │   │
│   │    • 10 AI agents governed across the full lifecycle                    │   │
│   │                                                                         │   │
│   └─────────────────────────────────────────────────────────────────────────┘   │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## Slide 9: Agent Fleet — Governance Coverage

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                                                                                 │
│                    AGENT FLEET — GOVERNANCE COVERAGE                            │
│                                                                                 │
│  ┌───────────────────────────────────────────────────────────────────────────┐  │
│  │                                                                           │  │
│  │   AGENT                    TIER    MODEL CARD   EVAL    SAFETY   STATUS  │  │
│  │   ─────────────────────    ────    ──────────   ────    ──────   ──────  │  │
│  │                                                                           │  │
│  │   DFM Router               T1      ✓            ✓       —       ✅       │  │
│  │   CNC Machining            T1      ✓            ✓       —       ✅       │  │
│  │   Injection Molding        T1      ✓            ✓       —       ✅       │  │
│  │   Sheet Metal              T1      ✓            ✓       —       ✅       │  │
│  │   3D Printing              T1      ✓            ✓       —       ✅       │  │
│  │   Materials Selection      T1      ✓            ✓       —       ✅       │  │
│  │   Vertical — Aerospace     T1      ✓            ✓       —       ✅       │  │
│  │   Vertical — Medical       T1      ✓            ✓       —       ✅       │  │
│  │   Vertical — Automotive    T1      ✓            ✓       —       ✅       │  │
│  │   Trends & Strategy        T1      ✓            ✓       —       ✅       │  │
│  │                                                                           │  │
│  │   ─────────────────────────────────────────────────────────────────────   │  │
│  │   FLEET TOTAL: 10 agents    All Tier 1 (Advisory)    100% governed       │  │
│  │                                                                           │  │
│  └───────────────────────────────────────────────────────────────────────────┘  │
│                                                                                 │
│  ┌───────────────────────────────────────────────────────────────────────────┐  │
│  │                                                                           │  │
│  │   PLANNED ADDITIONS (Roadmap)                                             │  │
│  │                                                                           │  │
│  │   Quote Generation Bot      T2      Planned Q3 2026   Council approval   │  │
│  │   Production Scheduler      T2      Planned Q4 2026   Council approval   │  │
│  │   Parameter Optimizer       T3      Planned 2027      Board approval     │  │
│  │                                                                           │  │
│  └───────────────────────────────────────────────────────────────────────────┘  │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## Slide 10: Enforcement Architecture — What Protects Us

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                                                                                 │
│              7-LAYER GOVERNANCE ENFORCEMENT PIPELINE                            │
│                    (Fail-Closed: Block Unless Pass)                             │
│                                                                                 │
│  Every agent execution passes through 7 layers. Total overhead: <25ms.         │
│                                                                                 │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    │
│  │   LAYER 1   │───►│   LAYER 2   │───►│   LAYER 3   │───►│   LAYER 4   │    │
│  │ COMPLIANCE  │    │   BUDGET    │    │    RBAC     │    │    HITL     │    │
│  │             │    │             │    │             │    │    GATE     │    │
│  │ Jurisdiction│    │ Tenant cap  │    │ SPIFFE ID   │    │ Confidence  │    │
│  │ Regulatory  │    │ User cap    │    │ Permissions │    │ Authority   │    │
│  │ Data class  │    │ Agent cap   │    │ Delegation  │    │ routing     │    │
│  └──────┬──────┘    └──────┬──────┘    └──────┬──────┘    └──────┬──────┘    │
│         ▼                  ▼                  ▼                  ▼            │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐                       │
│  │   LAYER 5   │───►│   LAYER 6   │───►│   LAYER 7   │                       │
│  │   CIRCUIT   │    │    AUDIT    │    │  EXECUTION  │                       │
│  │   BREAKER   │    │    LOG      │    │   WRAPPER   │                       │
│  │             │    │             │    │             │                       │
│  │ Error rate  │    │ SHA-256     │    │ Sandbox     │                       │
│  │ Loop detect │    │ integrity   │    │ Tool inter- │                       │
│  │ Dependency  │    │ chain       │    │ ception     │                       │
│  └─────────────┘    └─────────────┘    └─────────────┘                       │
│                                                                                 │
│  + Safety Agent (Governor) — independent monitoring & kill-switch              │
│  + Multi-Tenant Isolation — 6-layer client boundary enforcement                │
│  + Policy Engine — OPA/Cedar compiled policies (implementation in progress)    │
│                                                                                 │
│  STATUS: Architecture complete ✅  Implementation: 60% (Gap 1 remediation)    │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## Slide 11: Policy-as-Code — Honest Assessment

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                                                                                 │
│                    POLICY-AS-CODE STATE ASSESSMENT                              │
│                                                                                 │
│  An external evaluation claimed 10 gaps. Internal review found:                 │
│                                                                                 │
│  ┌─────────────────────────────────────────────────────────────────────────┐   │
│  │  4 "GAPS" ALREADY ADDRESSED BY EXISTING ARCHITECTURE                    │   │
│  │                                                                         │   │
│  │  ✅ Policy Engine        → 7-Layer Pipeline with OPA/Cedar (L1-L7)     │   │
│  │  ✅ Runtime Compliance   → Safety Agent + continuous L1 checks          │   │
│  │  ✅ Client-Specific      → 6-Layer Multi-Tenant Isolation              │   │
│  │  ✅ Provenance Chain     → L6 Audit Log with SHA-256 integrity         │   │
│  └─────────────────────────────────────────────────────────────────────────┘   │
│                                                                                 │
│  ┌─────────────────────────────────────────────────────────────────────────┐   │
│  │  6 REAL GAPS — REMEDIATION PLAN                                         │   │
│  │                                                                         │   │
│  │  Gap 1: Checklists → Executable Guardrails    6.5 sprints  P0          │   │
│  │  Gap 5: Policy Tree with Inheritance          6   sprints  P1          │   │
│  │  Gap 7: Adversarial Testing Framework         7.5 sprints  P1          │   │
│  │  Gap 4: Multi-Modal CAD Guardrails            6   sprints  P1          │   │
│  │  Gap 10: Control Tax Analysis                 5.5 sprints  P2          │   │
│  │  Gap 3: Formal Verification (Tier 3)          10.5 sprints P2          │   │
│  │                                                                         │   │
│  │  TOTAL: 42 sprints · ~$600K · 18 sprints at avg 3.3 engineers          │   │
│  └─────────────────────────────────────────────────────────────────────────┘   │
│                                                                                 │
│  Full plan: docs/policy-as-code-remediation-plan.md                            │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## Slide 12: The Ask

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                                                                                 │
│                              THE ASK                                            │
│                                                                                 │
│  ┌─────────────────────────────────────────────────────────────────────────┐   │
│   1. APPROVE governance framework as enterprise standard                     │
│      • 23 artifacts operational                                              │
│      • 7-layer enforcement pipeline architected                              │
│      • ISO 42001 readiness: 87%                                              │
│      • Certification target: Q1 2027                                         │
│  └─────────────────────────────────────────────────────────────────────────┘   │
│                                                                                 │
│  ┌─────────────────────────────────────────────────────────────────────────┐   │
│   2. APPROVE board resolution adopting ISO 42001                             │
│      • Formal commitment to AI management system certification               │
│      • Budget allocation for certification body engagement                   │
│      • CAIO authorized to execute certification roadmap                      │
│  └─────────────────────────────────────────────────────────────────────────┘   │
│                                                                                 │
│  ┌─────────────────────────────────────────────────────────────────────────┐   │
│   3. AUTHORIZE Policy-as-Code remediation budget ($600K)                     │
│      • Phase 1 (Foundation): $180K — executable checklists + policy tree    │
│      • Phase 2 (Production): $240K — CAD guardrails + adversarial testing   │
│      • Phase 3 (Advanced): $180K — formal verification + control tax        │
│      • Timeline: 18 sprints (approx. 6 months)                              │
│  └─────────────────────────────────────────────────────────────────────────┘   │
│                                                                                 │
│  ┌─────────────────────────────────────────────────────────────────────────┐   │
│   4. DIRECT teams to populate execution evidence                             │
│      • Model cards with real performance data                               │
│      • Eval results from production agents                                  │
│      • Training records and competence evidence                             │
│      • Timeline: 8 weeks to evidence-ready state                            │
│  └─────────────────────────────────────────────────────────────────────────┘   │
│                                                                                 │
│  ┌─────────────────────────────────────────────────────────────────────────┐   │
│   5. AUTHORIZE certification body engagement                                 │
│      • TÜV SÜD or BSI (recommended for manufacturing AI)                    │
│      • Pre-assessment: Q4 2026                                              │
│      • Certification audit: Q1 2027                                         │
│  └─────────────────────────────────────────────────────────────────────────┘   │
│                                                                                 │
│  ┌─────────────────────────────────────────────────────────────────────────┐   │
│  │                                                                         │   │
│  │   THE BOTTOM LINE                                                       │   │
│  │                                                                         │   │
│  │   ProtoLabs has built the most comprehensive AI governance framework    │   │
│  │   in the manufacturing sector. 23 artifacts. 4 integrated frameworks.  │   │
│  │   7-layer enforcement pipeline. 87% ISO 42001 readiness.               │   │
│  │                                                                         │   │
│  │   The architecture is complete. The remaining work is implementation    │   │
│  │   and evidence population — not design.                                 │   │
│  │                                                                         │   │
│  │   With board approval, we certify in Q1 2027 and become the first      │   │
│  │   ISO 42001-certified AI manufacturing company.                         │   │
│  │                                                                         │   │
│  └─────────────────────────────────────────────────────────────────────────┘   │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## Appendix A: Artifact Cross-Reference Map

| Artifact | ISO 42001 | NIST AI RMF | EU AI Act | Singapore MGF |
|----------|-----------|-------------|-----------|---------------|
| AI Governance Policy | Cl. 5.2 | GV-1.1 | Art. 9 | MHA |
| Council Charter | Cl. 5.3 | GV-1.2 | Art. 26(2) | MHA |
| Approval Thresholds | Cl. 8.1 | MG-1.1 | Art. 9(2) | Hard Guardrails |
| Incident Severity | Cl. 10.1 | MG-2.1 | Art. 72 | Hard Guardrails |
| Model Card Checklist | Cl. 7.5 | GV-7.1 | Art. 11 | Transparency |
| Prompt Registry | Cl. 7.5 | GV-7.1 | Art. 11(2)(b) | Transparency |
| Vendor Controls | Cl. 8.1 | GV-6.1 | Art. 25, 28 | Hard Guardrails |
| Safety Agent Arch. | Cl. 8.1 | MS-3.1 | Art. 14(3)(b) | Safety Agent |
| Internal Audit Plan | Cl. 9.2 | GV-5.1 | Art. 72 | Accountability |
| Retirement Procedure | Cl. 8.4 | MG-3.1 | Art. 72(2) | — |
| Competence Matrix | Cl. 7.2 | GV-3.1 | Art. 4 | Accountability |
| Communication Plan | Cl. 7.4 | GV-1.1 | Art. 13 | Transparency |
| Retention Schedule | Cl. 7.5 | — | Art. 18 | — |
| Objectives & KPIs | Cl. 6.2 | GV-5.1 | — | Accountability |
| Corrective Action | Cl. 10.1 | MG-2.1 | — | Accountability |
| Management Review | Cl. 9.3 | GV-5.1 | — | Accountability |
| Opportunity Register | Cl. 6.1 | GV-4.1 | — | — |
| Signing Authority | Cl. 5.3 | GV-1.2 | Art. 26(2) | MHA |
| Changelog | Cl. 7.5 | — | — | — |
| Regulatory Monitor | Cl. 4.1 | GV-1.1 | — | — |
| Improvement Register | Cl. 10.2 | GV-5.1 | — | Accountability |
| Eval Repository | Cl. 9.1 | MS-2.1 | Art. 15 | Hard Guardrails |
| Client Policy Summary | Cl. 5.2 | GV-1.1 | Art. 13, 52 | Transparency |

---

## Appendix B: Certification Timeline

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                                                                                 │
│                    ISO 42001 CERTIFICATION ROADMAP                              │
│                                                                                 │
│   Q2 2026          Q3 2026          Q4 2026          Q1 2027                   │
│   ────────         ────────         ────────         ────────                   │
│                                                                                 │
│   ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐                │
│   │ FRAMEWORK│    │ EVIDENCE │    │ PRE-     │    │CERTIFICA-│                │
│   │ COMPLETE │    │ POPULATE │    │ ASSESS   │    │ TION     │                │
│   │          │    │          │    │          │    │          │                │
│   │ 23 docs  │    │ Real data│    │ TÜV SÜD │    │ Audit    │                │
│   │ created  │    │ in all   │    │ or BSI   │    │ & Cert   │                │
│   │ ✓ DONE   │    │ artifacts│    │ pre-audit│    │          │                │
│   │          │    │          │    │          │    │ ★ TARGET │                │
│   └──────────┘    └──────────┘    └──────────┘    └──────────┘                │
│        │                │               │               │                      │
│        ▼                ▼               ▼               ▼                      │
│   Board reso-      Internal audit   Gap closure     ISO 42001                 │
│   lution adopts    (full scope)     verification    certificate               │
│   ISO 42001        + management                   issued                      │
│                    review                                                     │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## Appendix C: Key Reference Documents

| Document | Location | Purpose |
|----------|----------|---------|
| **Governance Framework Architecture** | `docs/governance-framework-architecture.md` | Comprehensive board-level architecture reference (this presentation's source) |
| **Policy-as-Code Remediation Plan** | `docs/policy-as-code-remediation-plan.md` | Detailed plan for 6 identified gaps with sprint-level tasks |
| **ISO 42001 Gap Analysis** | `docs/iso-42001-gap-analysis.md` | Clause-by-clause readiness assessment |
| **Governance by Stage Framework** | `docs/governance-by-stage-framework.md` | Client journey → governance mapping |
| **AI Governance Policy** | `governance/ai-governance-policy.md` | Entry point policy (23 artifacts) |
| **7-Layer Enforcement Pipeline** | `governance/03-runtime-governance/agentic-workflows/governance-enforcement-pipeline.md` | OPA/Cedar pipeline specification |
| **Safety Agent Architecture** | `governance/03-runtime-governance/agentic-workflows/safety-agent-architecture.md` | Governor spec with kill-switch |
| **Multi-Tenant Isolation** | `governance/03-runtime-governance/agentic-workflows/multi-tenant-isolation.md` | 6-layer client isolation model |

---

*This presentation is derived from the ProtoLabs AI Governance Framework Architecture Document (v2.0). All artifacts referenced are version-controlled and auditable. For the complete architecture, see `docs/governance-framework-architecture.md`.*
