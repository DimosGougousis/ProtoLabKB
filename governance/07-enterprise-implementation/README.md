# Enterprise Implementation Guide

> **Phase 2 -- Organizational Adoption of AI Governance for Regulated FinTechs**

---

## Why This Section Exists

Checklists alone do not produce compliant organizations. A FinTech can have perfect model cards, thorough bias evaluations, and a complete SAFEST checklist -- and still fail a DNB licensing interview if no one in the room can explain who is responsible for the AI, how governance decisions are made, or how governance fits into the engineering workflow.

**Organizational structure must precede checklists.** Before you fill in a single compliance item, you need to answer:

- Who owns AI governance decisions?
- How do governance activities flow through your development process?
- Which AI systems require which level of governance intensity?
- What tooling enforces governance automatically rather than relying on human memory?

This section answers those questions.

---

## The Four Enterprise Dimensions

Enterprise AI governance adoption rests on four interdependent dimensions. Each dimension must be addressed; skipping any one creates a structural gap that regulators will identify.

```
+---------------------------+       +---------------------------+
|   1. ORGANIZATIONAL       |       |   2. PROCESS              |
|      MODEL                |       |      INTEGRATION          |
|                           |       |                           |
|  - Three Lines of Defense |       |  - Agile Sprint           |
|  - AI Governance          |       |    Integration            |
|    Committee              |       |  - Definition of Done     |
|  - Board Accountability   |       |  - Governance User        |
|  - RACI Matrices          |       |    Stories                |
+---------------------------+       +---------------------------+
             |                                   |
             v                                   v
+---------------------------+       +---------------------------+
|   3. RISK-BASED           |       |   4. TOOLING              |
|      ADOPTION             |       |      INTEGRATION          |
|                           |       |                           |
|  - Risk Tiering Model     |       |  - Eval Pipelines         |
|  - Minimum Viable         |       |  - Compliance-as-Code     |
|    Governance             |       |  - Monitoring Dashboards  |
|  - Adoption Playbook      |       |  - Audit Trail Systems    |
+---------------------------+       +---------------------------+
```

### Dimension 1: Organizational Model

Defines **who** is responsible for AI governance and **how authority flows**.

| File | Purpose |
|------|---------|
| [Three Lines of Defense for AI](organizational-model/three-lines-of-defense-for-ai.md) | Maps the classic 3LoD model to AI-specific responsibilities |
| [AI Governance Committee Charter](organizational-model/ai-governance-committee-charter.md) | Template for establishing the central AI governance decision-making body |
| [Board-Level AI Accountability](organizational-model/board-level-ai-accountability.md) | Guide for satisfying DNB board accountability expectations (A-01, K-01 through K-04) |

### Dimension 2: Process Integration

Defines **when** governance activities happen within existing engineering workflows.

| File | Purpose |
|------|---------|
| [Governance in Agile Sprints](process-integration/governance-in-agile-sprints.md) | How governance checkpoints inject into Scrum ceremonies and the Definition of Done |

### Dimension 3: Risk-Based Adoption

Defines **how much** governance to apply, proportional to risk.

| File | Purpose |
|------|---------|
| [Risk Tiering Model](risk-based-adoption/risk-tiering-model.md) | Maps EU AI Act risk classifications to governance intensity levels |
| [Minimum Viable Governance](risk-based-adoption/minimum-viable-governance.md) | The lightest governance profile for minimal/limited-risk AI |
| [Adoption Playbook](risk-based-adoption/adoption-playbook.md) | 12-month phased rollout guide from assessment to regulatory readiness |

### Dimension 4: Tooling Integration

Defines **what systems** enforce governance automatically. *(Content in `tooling-integration/` -- covered in a future phase.)*

---

## Target Audience

This section is written for **FinTechs seeking DNB/ECB licensing** as Payment Service Providers (PSPs), Electronic Money Institutions (EMIs), or Crypto-Asset Service Providers (CASPs) under MiCAR. Specifically:

| Role | What to read first |
|------|--------------------|
| **CEO / Founder** | Board-Level AI Accountability, Adoption Playbook |
| **CTO / VP Engineering** | Three Lines of Defense, Governance in Agile Sprints |
| **Head of Compliance / MLRO** | Risk Tiering Model, AI Governance Committee Charter |
| **Head of Product** | Minimum Viable Governance, Governance in Agile Sprints |
| **Internal Audit** | Three Lines of Defense, Risk Tiering Model |

---

## How This Section Connects to the Four Governance Pillars

The repository is organized around four governance pillars that cover the AI product lifecycle:

| Pillar | Directory | Enterprise Implementation Touchpoints |
|--------|-----------|--------------------------------------|
| **Discovery Governance** | `01-discovery-governance/` | Risk tiering at ideation; ethical use case review in committee |
| **Development Governance** | `02-development-governance/` | Sprint integration; Definition of Done; eval pipelines |
| **Runtime Governance** | `03-runtime-governance/` | Monitoring responsibilities per line of defense; incident escalation |
| **Operational Governance** | `04-operational-governance/` | Board reporting; audit trail retention; regulatory readiness |

Each enterprise implementation file explicitly references the SAFEST checklist items it supports (e.g., A-01, S-13, K-04) so you can trace from organizational structure back to specific regulatory evidence.

---

## Mapping to SAFEST Pillars

| Enterprise Dimension | Primary SAFEST Pillars | Key Items |
|---------------------|----------------------|-----------|
| Organizational Model | Accountability (A), Skills (K) | A-01 through A-05, K-01 through K-04 |
| Process Integration | Soundness (S), Accountability (A) | S-19 through S-22, A-04, A-11, A-12 |
| Risk-Based Adoption | All pillars | Risk-proportional application of all items |
| Tooling Integration | Soundness (S), Transparency (T) | S-12, T-15 through T-17 |

---

## Prerequisites

Before implementing this section, ensure you have:

1. **Read the SAFEST checklist** -- see `docs/06-licensing-preparation/safest-checklist-dnb-pre-application.md` in the parent AIGovernance repository for the full regulatory context.
2. **An AI system inventory** (even a draft) -- you cannot assign governance to systems you have not catalogued (SAFEST item S-01).
3. **Board commitment** -- enterprise governance adoption requires executive sponsorship. Without it, governance becomes a paper exercise that DNB will see through.

---

## Reading Order

For a FinTech starting from scratch, follow this sequence:

1. **Risk Tiering Model** -- understand how much governance each AI system needs
2. **Minimum Viable Governance** -- establish baseline governance for all AI systems immediately
3. **Three Lines of Defense** -- assign organizational responsibilities
4. **AI Governance Committee Charter** -- establish the decision-making body
5. **Board-Level AI Accountability** -- ensure board-level oversight is in place
6. **Governance in Agile Sprints** -- embed governance into engineering workflows
7. **Adoption Playbook** -- execute the 12-month rollout plan

---

*Last updated: 2026-02-28*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
