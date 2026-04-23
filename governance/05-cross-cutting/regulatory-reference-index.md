# Regulatory Reference Index

> Master index of every regulation, standard, and guideline referenced across the **Protolabs AI Governance Framework**. Adapted from the upstream FinTech-oriented index: DORA, Wft, PSD2, MiCAR removed; ITAR, EAR, FDA 21 CFR 820, AS9100D, ISO 9001/13485, IATF 16949, NADCAP, RoHS, REACH, and NIST CSF added.

**Version:** 2.0 (Protolabs adaptation)
**Last Updated:** 2026-04-23
**Owner:** ProtoLabs AI Governance Office
**Review Cycle:** Quarterly, or upon significant regulatory change

---

## Purpose

Single source of truth for every regulation that touches the ProtoLab agent system. For each entry this index records:

1. A brief description and relevance to the DFM agent fleet.
2. Key articles, clauses, or sub-categories that bear on agentic AI.
3. Where each requirement is addressed within this governance framework.
4. A link to the underlying compliance knowledge-base article in `../../knowledge/` when one exists (governance files **link**, never duplicate).

Use this index when you need to answer: *"Where in our governance framework do we satisfy requirement X of regulation Y?"*

**Scope note.** This index is organised in three bands:
- **Band A — Core to all agents** (EU AI Act, GDPR, NIST CSF 2.0, ISO/IEC 42001, SOC 2).
- **Band B — Activated when manufacturing compliance keywords fire** (ITAR, EAR, FDA 21 CFR 820, AS9100D, ISO 13485, IATF 16949, NADCAP, RoHS, REACH, ISO 9001).
- **Band C — US state and jurisdiction-specific** (HIPAA, Colorado AI Act, PCI DSS).
- **Archived — Not applicable to Protolabs** (DORA, Wft, PSD2, MiCAR — see `_archive/`).

The `{{#regulated}}` template pattern in `../../templates/*.md` and `../protolabs/manufacturing-compliance-routing.md` govern when Band B is loaded.

---

## Band A — Core (apply to every DFM agent)

### A.1 EU AI Act (Regulation (EU) 2024/1689)

**Overview.** A harmonised, risk-based legal framework for AI within the EU. Classifies AI systems into unacceptable, high, limited, and minimal risk tiers and imposes proportional obligations.

**Protolabs applicability.** The DFM agents (CNC, injection molding, sheet metal, 3D printing, materials) are **Limited-risk** when used as advisory design-review tools. They would move to **High-risk** if autonomy ever extended to binding quote decisions affecting price, lead-time, or customer commitments (EU AI Act Annex III is not directly triggered, but a future autonomous-quoting mode must be re-classified).

| Article | Title | Core Requirement | Governance Section |
|---------|-------|------------------|--------------------|
| Art 6 | Classification of High-Risk AI | Determine risk tier for every agent | `../01-discovery-governance/checklists/eu-ai-act-risk-classification.yaml`, `../protolabs/agent-risk-registry.yaml` |
| Art 9 | Risk Management System | Continuous risk management | `../01-discovery-governance/templates/risk-management-plan.md`, `../04-operational-governance/templates/drift-detection-runbook.md` |
| Art 10 | Data & Data Governance | Training/validation/test data quality & bias | `../02-development-governance/evaluations/bias-and-fairness-evals.md`, `../protolabs/source-grounding-data-contract.yaml` |
| Art 11 | Technical Documentation | Maintain up-to-date tech docs | `../02-development-governance/templates/model-card.md` |
| Art 13 | Transparency & Info | Users must know they are interacting with AI | `../03-runtime-governance/transparency-controls.md` |
| Art 14 | Human Oversight | Design for humans to oversee, interrupt, override | `../03-runtime-governance/human-oversight-protocol.md`, `../protolabs/agents/*/KILLSWITCH.md` |
| Art 15 | Accuracy, Robustness, Cybersecurity | Accuracy & resilience | `../04-operational-governance/guides/red-teaming-ai-systems.md`, `../protolabs/dfm-accuracy-eval-suite.yaml` |
| Art 52 | Transparency for Certain AI | Notify persons interacting with AI | `../03-runtime-governance/transparency-controls.md` |

**Linked compliance KB:** `../../knowledge/cnc-machining/eu-ai-act-governance.md`

---

### A.2 GDPR (Regulation (EU) 2016/679)

**Overview.** Governs the processing of personal data within the EU. Relevant to Protolabs agents when customer submissions contain engineer names, account information, or anything that identifies the submitter or beneficiary of the design.

**Protolabs applicability.** Customer CAD files and intake descriptions can include personal data embedded in filenames, metadata, or free-text fields. The CAD/IP protection guardrail (`../protolabs/customer-cad-ip-protection-guardrail.md`) implements GDPR-compliant handling.

| Article | Title | Core Requirement | Governance Section |
|---------|-------|------------------|--------------------|
| Art 5 | Principles | Lawfulness, fairness, transparency, minimisation | `../01-discovery-governance/templates/data-governance-plan.md` |
| Art 13-14 | Information to be provided | Transparent processing info including automated decision-making | `../03-runtime-governance/transparency-controls.md` |
| Art 22 | Automated Individual Decision-Making | Right to human review | `../03-runtime-governance/human-oversight-protocol.md` |
| Art 25 | Data Protection by Design | Technical & organisational measures | `../protolabs/customer-cad-ip-protection-guardrail.md` |
| Art 35 | DPIA | Data Protection Impact Assessment for high-risk processing | `../01-discovery-governance/templates/dpia-template.md` |

---

### A.3 NIST Cybersecurity Framework 2.0 (NIST CSF 2.0)

**Overview.** Voluntary cybersecurity framework organised around six Functions: Govern, Identify, Protect, Detect, Respond, Recover.

**Protolabs applicability.** The agent system stores cached KB content, intake descriptions, and (future) customer CAD files. NIST CSF 2.0 provides the reference architecture for securing the whole pipeline and especially the intake boundary.

| Function | Category (examples) | Governance Section |
|----------|---------------------|--------------------|
| Govern (GV) | Organisational cybersecurity strategy, roles, policy | `../01-discovery-governance/templates/governance-charter.md`, `../05-cross-cutting/governance-roles-raci.md` |
| Identify (ID) | Asset management, risk assessment | `../protolabs/agent-risk-registry.yaml`, `../05-cross-cutting/machine-identity-nhi.md` |
| Protect (PR) | Access control, data security | `../protolabs/customer-cad-ip-protection-guardrail.md` |
| Detect (DE) | Continuous monitoring, anomaly detection | `../04-operational-governance/templates/drift-detection-runbook.md` |
| Respond (RS) | Incident response | `../04-operational-governance/templates/ai-incident-report.md`, `../protolabs/agents/*/KILLSWITCH.md` |
| Recover (RC) | Recovery planning, improvements | `../04-operational-governance/incident-response-plan.md` |

**Linked compliance KB:** `../../knowledge/cnc-machining/nist-cybersecurity-framework.md`

---

### A.4 ISO/IEC 42001 — AI Management System (AIMS)

**Overview.** Requirements for establishing, maintaining, and improving an AI Management System. Uses the Annex SL high-level structure.

| Clause | Title | Governance Section |
|--------|-------|--------------------|
| 4 | Context of the Organisation | `../01-discovery-governance/templates/governance-charter.md` |
| 5 | Leadership | `../05-cross-cutting/governance-roles-raci.md` |
| 6 | Planning | `../01-discovery-governance/templates/risk-management-plan.md` |
| 7 | Support | `../07-enterprise-implementation/training-and-awareness-plan.md` |
| 8 | Operation | `../03-runtime-governance/` (all guides) |
| 9 | Performance Evaluation | `../04-operational-governance/continuous-monitoring-plan.md` |
| 10 | Improvement | `../04-operational-governance/incident-response-plan.md` |
| Annex A | AI Controls | Mapped across the entire framework |
| Annex B | Implementation Guidance | `../03-runtime-governance/guides/`, `../04-operational-governance/guides/` |

---

### A.5 SOC 2 (Trust Services Criteria)

**Overview.** AICPA auditing standard for security, availability, processing integrity, confidentiality, and privacy. Relevant if Protolabs AI outputs are consumed by enterprise customers who expect a SOC 2 Type II report.

| TSC | Category | Governance Section |
|-----|----------|--------------------|
| CC6.1 | Logical access controls | `../protolabs/agents/*/skill-manifest.yaml` |
| CC6.2 | Access removal | `../03-runtime-governance/templates/agent-registry-entry.yaml` |
| CC7.2 | System monitoring | `../04-operational-governance/monitoring-dashboard.md` |
| CC7.3 | Incident detection | `../03-runtime-governance/templates/kill-switch-specification.md` |
| PI1.3 | Complete processing | `../03-runtime-governance/agentic-workflows/delegation-chain-audit.md` |
| C1.1 | Confidential information | `../protolabs/customer-cad-ip-protection-guardrail.md` |

---

## Band B — Manufacturing Compliance (activated by `{{#regulated}}` keywords)

### B.1 ITAR — International Traffic in Arms Regulations (22 CFR Parts 120-130)

**Overview.** US State Department (DDTC) regulations controlling defense articles and services on the USML. Applies to many aerospace, defense, and high-performance parts.

**Protolabs applicability.** Triggered when the `dfm-router` detects ITAR/USML/defense keywords. Activates the CAD/IP protection guardrail in "ITAR-controlled" mode and escalates to HITL oversight.

| Requirement | Governance Section |
|-------------|--------------------|
| Deemed-export controls | `../protolabs/customer-cad-ip-protection-guardrail.md` |
| Jurisdiction & classification determination | `../protolabs/manufacturing-compliance-routing.md` |
| Recordkeeping | `../04-operational-governance/templates/audit-record-schema.yaml` |
| Authorised foreign nationals | `../05-cross-cutting/machine-identity-nhi.md` (agent authorisation) |

**Linked compliance KB:** `../../knowledge/cnc-machining/itar-ear-compliance.md`, `../../knowledge/3d-printing/additive-export-controls.md`

---

### B.2 EAR — Export Administration Regulations (15 CFR Parts 730-774)

**Overview.** US Commerce Department (BIS) regulations controlling dual-use items and "dual-use" software/technology. Covers more parts than ITAR but generally with less restriction.

**Protolabs applicability.** Triggered for commercial-grade dual-use items (e.g., certain aerospace materials, specific 3D-printed metals, semiconductor tooling components). Same runtime routing as ITAR but with different classification tables (ECCN vs. USML).

| Requirement | Governance Section |
|-------------|--------------------|
| ECCN determination | `../protolabs/manufacturing-compliance-routing.md` |
| License exceptions | `../../knowledge/cnc-machining/itar-ear-compliance.md` (linked) |
| End-use / end-user screening | `../03-runtime-governance/agentic-workflows/customer-facing-agent-safety.md` |

**Linked compliance KB:** `../../knowledge/cnc-machining/itar-ear-compliance.md`

---

### B.3 FDA 21 CFR Part 820 — Quality System Regulation for Medical Devices

**Overview.** FDA's Quality System Regulation for manufacturers of finished medical devices. Covers design controls, production & process controls, corrective & preventive action (CAPA), and records.

**Protolabs applicability.** Triggered when `vertical-medical` keywords fire (medical device, biocompatibility, implantable, catheter, FDA clearance, Class I/II/III). The DFM output must include explicit FDA-readiness caveats.

| Subpart | Requirement | Governance Section |
|---------|-------------|--------------------|
| C (Design Controls) | Design validation & verification | `../02-development-governance/templates/test-plan-for-ai.md` |
| G (Production & Process Controls) | Validated manufacturing processes | `../03-runtime-governance/guides/` |
| H (Acceptance Activities) | Acceptance criteria | `../01-discovery-governance/evaluations/defining-acceptance-criteria.md` |
| I (Nonconforming Product) | CAPA | `../04-operational-governance/templates/ai-incident-report.md` |
| M (Records) | DMR, DHR, DHF | `../04-operational-governance/templates/audit-record-schema.yaml` |

**Linked compliance KB:** `../../knowledge/3d-printing/fda-biocompatibility.md`, `../../knowledge/verticals/medical-devices-compliance.md` (if present)

---

### B.4 AS9100D — Aerospace Quality Management System

**Overview.** Aerospace-specific extension of ISO 9001 adding requirements for configuration management, first-article inspection, counterfeit parts prevention, and product safety. Published by SAE / IAQG.

**Protolabs applicability.** Triggered by `vertical-aerospace` keywords (aerospace, aircraft, flight-critical, AS9100, NADCAP). DFM output must explicitly mention configuration control and first-article inspection implications.

| Clause (relative to ISO 9001) | Add-on Requirement | Governance Section |
|-------------------------------|---------------------|--------------------|
| 8.1.1 | Operational risk management | `../01-discovery-governance/templates/risk-management-plan.md` |
| 8.1.4 | Prevention of counterfeit parts | `../../knowledge/verticals/aerospace-compliance.md` (linked) |
| 8.3.4 | Configuration management | `../02-development-governance/templates/model-card.md` |
| 8.5.1.3 | Production process verification (first-article inspection) | `../02-development-governance/templates/test-plan-for-ai.md` |

---

### B.5 ISO 13485:2016 — Medical Device Quality Management

**Overview.** Standalone QMS standard for medical devices. Often used by manufacturers who are not FDA-regulated (e.g., EU MDR scope).

**Protolabs applicability.** Complement to FDA 21 CFR 820 for medical vertical. Same runtime triggers.

Governance cross-references: same as FDA 21 CFR 820 above.

---

### B.6 IATF 16949:2016 — Automotive Quality Management

**Overview.** Automotive-sector-specific QMS built on ISO 9001, adding requirements for APQP, PPAP, control plans, and customer-specific requirements.

**Protolabs applicability.** Triggered by `vertical-automotive-ev` keywords. Particularly relevant for production-volume CNC and injection-molded parts destined for automotive tier-1/tier-2 suppliers.

| Element | Governance Section |
|---------|--------------------|
| APQP (Advanced Product Quality Planning) | `../01-discovery-governance/templates/risk-management-plan.md` |
| PPAP (Production Part Approval Process) | `../02-development-governance/templates/test-plan-for-ai.md` |
| Control Plan | `../03-runtime-governance/templates/agent-registry-entry.yaml` |
| Customer-specific requirements | `../protolabs/manufacturing-compliance-routing.md` |

---

### B.7 NADCAP — National Aerospace and Defense Contractors Accreditation Program

**Overview.** PRI-administered accreditation for special processes in aerospace (heat treating, non-destructive testing, welding, coating, chemical processing).

**Protolabs applicability.** Referenced for aerospace-vertical DFM advice that touches special processes. Not directly a Protolabs compliance obligation — but the agent must flag when a customer's design implies a NADCAP special process so the human loop can confirm supplier qualification.

---

### B.8 RoHS Directive (2011/65/EU) and REACH Regulation (EC) 1907/2006

**Overview.** EU regulations restricting hazardous substances (RoHS) and governing chemical substances including SVHCs (REACH). Relevant for materials selection advice and for end-of-life/disposal guidance.

**Protolabs applicability.** Triggered when `materials-selection` agent advises on plastics or metals destined for the EU market. The agent must flag restricted substances and SVHC candidate-list status.

| Requirement | Governance Section |
|-------------|--------------------|
| Restricted substance declarations | `../../knowledge/materials/` (linked) |
| Candidate list monitoring | `../protolabs/kb-freshness-provenance-contract.md` (90-day refresh) |

---

### B.9 ISO 9001:2015 — General QMS

**Overview.** Baseline ISO QMS standard. Underpins AS9100D, ISO 13485, IATF 16949. Referenced directly for general manufacturing compliance claims.

**Linked compliance KB:** `../../knowledge/cnc-machining/iso-quality-standards.md`

---

## Band C — Jurisdiction-Specific (US state / sector)

### C.1 Colorado AI Act (SB 24-205)

**Overview.** Effective 2026-02-01. Regulates high-risk AI systems to prevent algorithmic discrimination.

**Protolabs applicability.** Likely **out of scope** for the current advisory DFM agents (no consequential decisions as defined in the Act). Would apply if a future quote-bot makes autonomous pricing decisions for Colorado-domiciled customers.

| Requirement | Governance Section |
|-------------|--------------------|
| Risk Assessment | `../01-discovery-governance/checklists/eu-ai-act-risk-classification.yaml` |
| Algorithmic Discrimination | `../02-development-governance/evaluations/bias-and-fairness-evals.md` |
| Notice to Consumers | `../03-runtime-governance/transparency-controls.md` |
| Human Oversight | `../03-runtime-governance/human-oversight-protocol.md` |
| Annual Review | `../07-enterprise-implementation/governance-maturity-roadmap.md` |

---

### C.2 HIPAA (Health Insurance Portability and Accountability Act)

**Overview.** US PHI protection. Security Rule (technical safeguards) + Privacy Rule (use/disclosure).

**Protolabs applicability.** Very narrow: only if the `vertical-medical` agent ever processes PHI embedded in a customer submission (e.g., a patient-specific implant reference). The CAD/IP guardrail requires PHI redaction before agent invocation.

| HIPAA Section | Requirement | Governance Section |
|---------------|-------------|--------------------|
| §164.312(a) | Access Control | `../protolabs/agents/*/skill-manifest.yaml` |
| §164.312(b) | Audit Controls | `../04-operational-governance/templates/audit-record-schema.yaml` |
| §164.312(c) | Integrity | `../03-runtime-governance/templates/kill-switch-specification.md` |
| §164.312(d) | Authentication | `../05-cross-cutting/machine-identity-nhi.md` |

---

### C.3 PCI DSS (Payment Card Industry Data Security Standard)

**Overview.** Security standards for handling cardholder data.

**Protolabs applicability.** Out of scope for advisory DFM agents. Would apply if the future quote-bot handles customer payment information.

---

## DNB SAFEST — Retained as Internal Methodology

**Note on retention.** DNB SAFEST was developed as a Dutch central bank supervisory framework. Protolabs is **not** supervised by DNB. However, SAFEST's six-pillar taxonomy (Soundness, Accountability, Fairness, Ethics, Skills, Transparency) is a well-designed organisational rubric and has been retained as **internal governance methodology** — not as external compliance. See `../protolabs/safest-coverage-matrix.md` for the ProtoLab-specific SAFEST coverage matrix.

| Pillar | Description | Governance Section |
|--------|-------------|--------------------|
| **S** — Soundness | Technically sound, validated, resilient | `../protolabs/dfm-accuracy-eval-suite.yaml`, `../04-operational-governance/guides/red-teaming-ai-systems.md` |
| **A** — Accountability | Clear ownership, roles, escalation | `../05-cross-cutting/governance-roles-raci.md` |
| **F** — Fairness | No discrimination; bias identified and mitigated | `../02-development-governance/evaluations/bias-and-fairness-evals.md` |
| **E** — Ethics | Aligned with values & societal norms | `../01-discovery-governance/templates/ethical-use-policy.md` |
| **S** — Skills | Sufficient AI literacy | `../07-enterprise-implementation/training-and-awareness-plan.md` |
| **T** — Transparency | Explainable, auditable | `../03-runtime-governance/transparency-controls.md`, `../protolabs/source-grounding-data-contract.yaml` |

---

## Archived — Not Applicable to Protolabs

The following regulations were authoritative in the upstream FinTech-oriented framework and are **not applicable** to Protolabs. They are preserved in `../_archive/` for traceability; their bindings have been removed from the cross-reference matrix below.

| Archived regulation | Reason | Archive location |
|---------------------|--------|------------------|
| **DORA** (Digital Operational Resilience Act) | Financial sector only | `../_archive/dora-ai-requirements.md` |
| **Wft** (Dutch Financial Supervision Act) | Financial sector only | (upstream reference only; no dedicated file) |
| **PSD2** (Revised Payment Services Directive) | Payment services | (upstream reference only) |
| **MiCAR** (Markets in Crypto-Assets Regulation) | Crypto-asset services | (upstream reference only) |

---

## Cross-Reference Matrix: Regulation × Framework Pillar (Protolabs)

| Framework Pillar | EU AI Act | ISO 42001 | GDPR | NIST CSF | SOC 2 | ITAR/EAR | FDA 21 CFR 820 | AS9100D | IATF 16949 | RoHS/REACH |
|-----------------|-----------|-----------|------|----------|-------|----------|----------------|---------|------------|------------|
| **00 Getting Started** | Art 6 | Cl 4 | Art 5 | GV | — | Routing | — | — | — | — |
| **01 Discovery** | Art 6, 9, 10 | Cl 6, 8 | Art 5, 25, 35 | ID | — | Classification | Design Controls | Risk Mgmt | APQP | Material selection |
| **02 Development** | Art 10, 11, 15 | Cl 8 | Art 25 | PR | — | Deemed export | Validation | Config Mgmt | PPAP | Substance checks |
| **03 Runtime** | Art 13, 14, 15, 52 | Cl 8 | Art 13, 22 | DE, PR | CC6, CC7, PI1 | Runtime flagging | CAPA hooks | First-article | Control plans | Runtime warnings |
| **04 Operational** | Art 9, 15 | Cl 9, 10 | Art 35 | RS, RC | CC7.3, PI1.3 | Recordkeeping | DHF records | — | — | Substance logs |
| **05 Cross-cutting** | Art 10 | Cl 7 | Art 5, 25 | GV | C1.1 | Agent identity | — | — | — | — |
| **06 Executive** | — | Cl 9 | — | GV | — | — | — | — | — | — |
| **07 Enterprise Impl.** | — | Cl 5, 7 | — | GV | — | — | — | — | — | — |

---

## How to Use This Index

1. **Starting a new agent or extending an existing one.** Look up applicable regulations. Check the cross-reference matrix to identify which framework pillars require attention.
2. **Preparing for an audit, customer due-diligence questionnaire, or supervisory review.** Use the linked compliance KB files in `../../knowledge/` for regulatory content; use the governance sections in this framework for control evidence.
3. **When regulations change.** Update this index, adjust the cross-reference matrix, and propagate changes to affected sections. Log the change in the governance framework change log.
4. **During a customer DFM request that triggers `{{#regulated}}`.** Use the routing keywords in `../protolabs/manufacturing-compliance-routing.md` to determine which Band B regulation fires.

---

## Maintenance Schedule

| Activity | Frequency | Responsible |
|----------|-----------|-------------|
| Full index review | Quarterly | AI Governance Lead |
| Regulation-specific update | Within 30 days of regulatory change | Legal & Compliance |
| Cross-reference matrix validation | Semi-annually | AI Governance Lead + Legal |
| KB freshness reconciliation | Monthly | Compliance + Governance (per `../protolabs/kb-freshness-provenance-contract.md`) |

---

## Related Documents

- `../protolabs/agent-risk-registry.yaml` — ARI-scored registry of the 10 DFM agents
- `../protolabs/manufacturing-compliance-routing.md` — Keyword-to-regulation routing
- `../protolabs/customer-cad-ip-protection-guardrail.md` — CAD/IP handling policy
- `./machine-identity-nhi.md` — Non-Human Identity (NHI) management for agents
- `./governance-roles-raci.md` — RACI across the governance lifecycle
- `../00-getting-started/quick-assessment-checklist.yaml` — Initial assessment
- `../../knowledge/compliance/regulatory-framework.md` — Legacy consolidated compliance KB (in ProtoLab main tree, linked not duplicated)
