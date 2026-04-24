# Board Resolution — Adoption of ISO/IEC 42001 AI Management System

> **Purpose:** Formal board resolution establishing ProtoLabs' commitment to ISO/IEC 42001:2023 certification and authorizing the AI Management System (AIMS).

**Resolution Number:** BR-2026-0424-AI  
**Date:** 2026-04-24  
**Meeting:** Board of Directors — Special Session on AI Governance  
**Classification:** Confidential — Board Distribution  

---

## Resolution

**WHEREAS**, ProtoLabs operates AI-powered agents that provide Design for Manufacturing (DFM) analysis, materials selection, production scheduling, and quality control services to clients in aerospace, medical device, automotive, and general manufacturing sectors;

**WHEREAS**, clients in regulated industries increasingly require evidence of systematic AI governance as a procurement qualification, with ISO/IEC 42001:2023 recognized as the international standard for AI Management Systems;

**WHEREAS**, the Board of Directors recognizes that certifiable AI governance provides competitive advantage, regulatory compliance assurance, and risk mitigation for ProtoLabs and its clients;

**WHEREAS**, the ProtoLabs AI Governance Office has conducted a gap analysis against ISO/IEC 42001:2023 and established a certification roadmap targeting Q1 2027;

**NOW, THEREFORE, BE IT RESOLVED THAT:**

### 1. Adoption of ISO/IEC 42001:2023

The Board formally adopts ISO/IEC 42001:2023 — Artificial Intelligence Management System as the governing framework for all AI system lifecycle processes at ProtoLabs, effective immediately.

### 2. Scope of the AI Management System

The AIMS scope encompasses:
- All AI agents in the ProtoLabs agent fleet (`{{dfm-router}}`, `{{cnc-machining}}`, `{{injection-molding}}`, `{{sheet-metal}}`, `{{3d-printing}}`, `{{materials-selection}}`, `{{production-scheduler}}`, `{{quality-agent}}`)
- All stages of the AI system lifecycle: discovery, development, deployment, operation, monitoring, and retirement
- All client-facing and internal AI-powered manufacturing decision support systems

**Explicitly excluded from scope:** Third-party AI tools not integrated into the ProtoLabs agent fleet (e.g., generic LLM APIs used for non-agentic tasks).

### 3. Authorization of Resources

The Board authorizes:
- **Budget allocation:** $180,000 for ISO 42001 certification activities (FY2026-2027)
- **Personnel allocation:** 0.5 FTE AI Governance Office, 0.25 FTE Internal Audit
- **External services:** Certification body engagement (TÜV SÜD or BSI), consultant support as needed
- **Timeline:** Certification target Q1 2027

### 4. Appointment of AIMS Leadership

| Role | Appointee | Responsibility |
|------|-----------|----------------|
| **AI Management System Owner** | Chief AI Officer (CAIO) | Overall accountability for AIMS implementation and certification |
| **AI Policy Owner** | VP of Product | Accountability for AI policy correctness and business alignment |
| **Technical Owner** | VP of Engineering | Accountability for AIMS technical implementation |
| **Safety Officer** | Director of Manufacturing Safety | Accountability for Safety Agent and physical safety validation |
| **Compliance Officer** | General Counsel / DPO | Accountability for regulatory compliance and audit readiness |

### 5. Policy Commitments

The Board commits that ProtoLabs AI systems will:
- Be **valid and reliable** — achieving >90% accuracy on DFM recommendations, >95% schedule feasibility, >98% quality detection
- Be **safe** — with zero tolerance for realized harm scenarios; all Tier 2/3 agents validated by Safety Agent
- Be **secure and resilient** — with <1% adversarial attack success rate, 99.9% system availability
- Be **accountable and transparent** — with complete audit trails, source citations, and clear RACI accountability
- Be **explainable** — with decision rationale available for all high-stakes AI outputs
- Be **privacy-enhanced** — with client CAD/IP data encrypted, access-controlled, and never used for model training without consent
- Be **fair** — with no discriminatory outcomes; bias testing conducted for all recommendation agents

### 6. Risk Appetite Statement

The Board approves the AI Risk Appetite Framework (`governance/06-executive/ai-risk-appetite-framework.md`) with the following non-negotiables:
- **Zero appetite** for unacceptable risk AI systems (EU AI Act Article 5)
- **Zero appetite** for discriminatory outcomes without mitigation
- **Zero appetite** for safety-critical failures without human oversight
- **Zero appetite** for regulatory violations in ITAR/EAR-controlled contexts

### 7. Certification Target

The Board sets **Q1 2027** as the target date for achieving ISO/IEC 42001:2023 certification, with the following milestones:
- Q2 2026: Gap closure complete, internal audit program operational
- Q3 2026: First internal audit conducted, findings closed
- Q4 2026: Stage 1 and Stage 2 certification audits completed
- Q1 2027: Certification awarded

### 8. Review Cadence

The Board will review AIMS performance and certification progress **quarterly** through the existing Quarterly Governance Report (`governance/06-executive/quarterly-governance-report.md`), with ISO 42001-specific agenda items added to the management review process.

---

## Voting Record

| Director | Vote | Date |
|----------|------|------|
| [Chairperson Name] | ✅ Approve | 2026-04-24 |
| [Director 2 Name] | ✅ Approve | 2026-04-24 |
| [Director 3 Name] | ✅ Approve | 2026-04-24 |
| [Director 4 Name] | ✅ Approve | 2026-04-24 |
| [Director 5 Name] | ✅ Approve | 2026-04-24 |

**Resolution passed unanimously.**

---

## Signatures

```
_________________________________
[Chairperson Name]
Chairperson, Board of Directors
Date: 2026-04-24

_________________________________
[CEO Name]
Chief Executive Officer
Date: 2026-04-24

_________________________________
[CAIO Name]
Chief AI Officer, AIMS Owner
Date: 2026-04-24
```

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-24 | ProtoLabs AI Governance Office | Initial board resolution |

---

## See Also

- `governance/06-executive/ai-risk-appetite-framework.md` — AI Risk Appetite Framework
- `docs/iso-42001-gap-analysis.md` — ISO 42001 Gap Analysis and Certification Roadmap
- `governance/07-enterprise-implementation/iso-42001-certification/aims-objectives-and-kpis.md` — AIMS Objectives and KPIs
