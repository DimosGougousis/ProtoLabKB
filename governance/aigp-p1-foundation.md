# AIGP-P1: Foundation — Governance Operating System

> **Pillar 1 of 6** | AI Governance Pillars (AIGP)  
> **Scope:** Governance infrastructure, roles, RACI, policy lifecycle, and baseline controls that every subsequent pillar depends upon.

---

## 1. Purpose

Establish the **minimum viable governance operating system** (MV-GOS) required before any AI system is designed, procured, or deployed at ProtoLabs. This pillar answers: *Who decides, who is accountable, what policies apply, and how do we know they are followed?*

---

## 2. Governance Architecture

### 2.1 Three-Line Model (Adapted for AI)

| Line | Function | Accountability |
|------|----------|----------------|
| **1st** | Product & Engineering | Build right (controls in code, DFM agents, data pipelines) |
| **2nd** | AI Governance Office | Set policy, monitor compliance, report to board |
| **3rd** | Internal Audit / Ethics Review | Independent assurance, red-team exercises, external audit liaison |

### 2.2 RACI for Key Decisions

| Decision | Product | Engineering | Legal | AI Gov Office | Board |
|----------|:-------:|:-----------:|:-----:|:-------------:|:-----:|
| Deploy high-risk AI (EU AI Act Art. 6) | C | R | C | A | I |
| Approve training-data sourcing | C | R | A | C | I |
| Set acceptable-error budget for DFM agent | A | R | C | C | I |
| Incident response (bias drift, hallucination) | C | R | C | A | I |
| Annual policy refresh | C | C | C | R | A |

> **Legend:** R = Responsible, A = Accountable, C = Consulted, I = Informed

---

## 3. Policy Lifecycle

```
Draft → Stakeholder Review → Legal Sign-off → AI Gov Office Approval → Board Ratification → Publish → Train → Monitor → Refresh (annual, or trigger-based)
```

### 3.1 Trigger-Based Refresh Events
- New regulation (EU AI Act, state AI laws, NIST updates)
- Material incident (customer complaint, regulatory inquiry, bias finding)
- New process vertical (e.g., adding medical-device DFM)
- Model architecture change (LLM upgrade, new modality)

---

## 4. Baseline Controls (Universal)

Every AI system at ProtoLabs MUST implement:

| Control ID | Control | Verification |
|------------|---------|------------|
| BLC-01 | Documented purpose statement & success criteria | Review in PR |
| BLC-02 | Defined human-in-the-loop (HITL) level | `governance/hitl-levels.md` |
| BLC-03 | Risk classification (minimal / limited / high / unacceptable) | EU AI Act mapping |
| BLC-04 | Data provenance log | See AIGP-P4 (Lineage) |
| BLC-05 | Model card with performance bounds | See AIGP-P5 (MCP) |
| BLC-06 | Incident response playbook | 24-hr escalation path defined |
| BLC-07 | Retraining / drift detection schedule | See AIGP-P2 (Telemetry) |

---

## 5. Documentation Registry

| Document | Owner | Location | Refresh Cycle |
|----------|-------|----------|---------------|
| AI Governance Policy | AI Gov Office | `governance/ai-governance-policy.md` | Annual |
| Risk Classification Matrix | AI Gov Office | `governance/risk-matrix.md` | Trigger |
| HITL Level Definitions | Product | `governance/hitl-levels.md` | Annual |
| Incident Response Playbook | Security | `governance/incident-response.md` | Semi-annual |
| Vendor AI Assessment | Procurement | `governance/vendor-ai-checklist.md` | Per vendor |

---

## 6. Compliance Mapping

| Regulation / Standard | How P1 Satisfies |
|-----------------------|------------------|
| EU AI Act Art. 9 (Risk Management) | Risk classification + refresh triggers |
| EU AI Act Art. 10 (Data Governance) | BLC-04 + P4 lineage |
| EU AI Act Art. 14 (Human Oversight) | BLC-02 + HITL definitions |
| ISO 42001 Cl. 4 (Context) | Governance architecture + RACI |
| ISO 42001 Cl. 5 (Leadership) | Board ratification + 3-line model |
| NIST AI RMF GOVERN 1.1 | Policy lifecycle + baseline controls |

---

## 7. Acceptance Criteria

- [ ] RACI matrix published and acknowledged by all named roles
- [ ] At least one policy has completed full lifecycle (draft → ratification)
- [ ] All active AI projects have BLC-01 through BLC-07 documented
- [ ] AI Gov Office has quarterly board-reporting cadence established

---

*Next: [AIGP-P2: Observe & Telemetry](aigp-p2-observe-telemetry.md)*
