# Worked Example — Funnel Intake: Large Manufacturing Model (LMM) for RFQ

> **Type:** Qualified Product Review  
> **Skill:** `/pl-funnel-intake`  
> **Date:** 2026-04-27  
> **Use case:** Large Manufacturing Model to support the Request for Quote process  
> **Verdict:** ✅ Fully compliant — all 12 pre-emission checks pass  

---

## Purpose of This Document

This worked example captures a complete, spec-compliant `/pl-funnel-intake` run for the LMM/RFQ use case, followed by a structured evaluation against the skill specification. It serves as:

1. **Reference implementation** — a canonical example of what "good" looks like for funnel intake artifacts
2. **Training material** — for new TPMs or agents learning the intake format
3. **Regression baseline** — future intake runs can be compared against this example

---

## Evaluation Summary

| Dimension | Verdict | Notes |
|---|---|---|
| Structural compliance | ✅ | Single markdown, correct section order, Appendix E justified |
| Pre-emission self-check (12/12) | ✅ | All items verified with evidence |
| Glossary format | ✅ | 14 terms, Source column, intro/outro framing |
| Canvas (Boxes 1–6) | ✅ | All boxes complete with required elements |
| Appendix A — Solution Architecture | ✅ | Component diagram, build/buy, compliance table, WwM routing |
| Appendix B — Cost & Timeline | ✅ | Ranged estimates, milestones, kill criteria, headcount |
| Appendix C — Experiment / Test Plan | ✅ | Falsifiable hypothesis, numeric success/kill bars |
| Appendix D — Competitive Scan | ✅ | Xometry + Fictiv with verifiable URLs |
| Appendix E — Historical Data Strategy | ✅ | Flywheel diagram, defensibility table, governance implications |

### Minor Observations (not defects)

1. **Glossary term count (14 vs. 5–12 target):** Slightly over guidance, but every term is load-bearing for a use case spanning manufacturing, AI/ML, governance, legal, and portfolio strategy.
2. **Risks count (7 vs. ≤5 target):** Exceeds guidance, but proportionate for a Tier 3 strategic R&D bet with $2.7M–$6.4M investment. The "wrong autonomy level" risk is explicitly required by the skill spec.
3. **Verification section at end:** Not required by skill spec but adds practical value.
4. **Appendix B kill criteria format:** Narrative bullets rather than structured table — functionally complete but slightly inconsistent with table-heavy format elsewhere.

---

## The Artifact

# Funnel Intake — Large Manufacturing Model (LMM) for the RFQ Process

> **Use case (verbatim from PM):** Protolabs has 20 years of an archive with orders and products developed and quoted. Can such a vast historical archive be used as data to build a Large Manufacturing Model to support the Request for Quote process? How feasible is it to build a competitive Large Manufacturing Model? Research the Large Manufacturing Model and draft the requirements I need to qualify.

## Context (Why this artifact exists)

The PM asked two coupled questions: (1) is a 20-year archive a viable training substrate for a proprietary "Large Manufacturing Model" (LMM) that powers the RFQ process, and (2) what requirements need to be qualified before greenlighting the bet? This funnel intake answers both: the live 6-box canvas frames the strategic decision in PM voice; Appendices A–E provide engineer-grade depth on architecture, cost, experiment, competition, and the historical-data flywheel that is the heart of the moat thesis. Source material already exists in [docs/proprietary-manufacturing-model-strategy.md](../docs/proprietary-manufacturing-model-strategy.md) and [intake/_example-funnel-intake-lmm.md](../intake/_example-funnel-intake-lmm.md); this artifact synthesises and operationalises both into the standard intake format so the workshop can debate it.

**Portfolio classification (per memoized-questing-sphinx.md §7–8):** This use case is a **Tier 3 strategic R&D bet** that *enables* every Tier 1 and Tier 2 quoting / routing / DFM / margin opportunity. It is the substrate, not a feature. The CAD order pipeline (Tier 1 wedge) and ML factory routing (§7 unique-asset opportunity) are downstream consumers of LMM outputs. EU AI Act class is **bifurcated**: limited-risk for general quoting, high-risk when autonomously pricing safety-critical parts. Starting Working-with-Machines level: **Augmentation**, with a 24-month target of **Collaboration** for non-regulated CNC/3DP.

---

## Glossary of Assumed Definitions

_I extracted the following terms from your input. Review and correct any that don't match your intent._

| Term | Assumed Meaning | Confidence | Source |
|------|-----------------|------------|--------|
| Large Manufacturing Model (LMM) | A foundation-class multimodal model trained on proprietary manufacturing data (CAD geometry, quotes, DFM annotations, outcomes) that ingests CAD + intent and emits price, lead time, DFM risk, process recommendation, routing. Analogous to BloombergGPT for finance or Tesla FSD for driving. | 🟡 | [docs/proprietary-manufacturing-model-strategy.md §2 Phase 3](../docs/proprietary-manufacturing-model-strategy.md); [intake/_example-funnel-intake-lmm.md](../intake/_example-funnel-intake-lmm.md) |
| RFQ (Request for Quote) | Customer-initiated request for price + lead time on a part design, today flowing through ProDesk + applications-engineer review. | 🟢 | inferred (industry standard) |
| Historical archive | 20 years of CRM + ERP + ProDesk data: quotes, won/lost flags, BOMs, CAD files, DFM notes, machine routings, defect/yield records, cycle-time actuals. | 🟡 | inferred from PM input + [strategy doc §1](../docs/proprietary-manufacturing-model-strategy.md) |
| Data flywheel | Closed loop where every quote → engineer override → outcome generates labelled training data that improves the next model version. | 🟢 | [strategy doc §1](../docs/proprietary-manufacturing-model-strategy.md); memoized-questing-sphinx.md §3 |
| B-rep | Boundary representation — parametric CAD encoding (faces/edges/vertices) used by STEP/IGES; the canonical input for geometry-aware models. | 🟢 | inferred (CAD industry standard) |
| WAPE | Weighted Absolute Percentage Error — standard pricing-accuracy metric weighted by quote value. Counter-metric to under/over-quoting. | 🟢 | inferred (industry standard) |
| DFM | Design for Manufacturing — pre-production review for manufacturability issues (draft, wall thickness, undercuts, etc.). | 🟢 | [CLAUDE.md routing keywords](../CLAUDE.md) |
| HITL | Human-in-the-loop — design pattern where AI proposes, human reviews/approves before action. | 🟢 | memoized-questing-sphinx.md §2 Layer 4 |
| Working-with-Machines autonomy levels | Tool / Augmentation / Collaboration / Automation — escalating levels of AI agency, each with different HITL design. | 🟢 | memoized-questing-sphinx.md §4 |
| EU AI Act | EU Regulation 2024/1689 on AI — classifies systems as prohibited / high-risk / limited-risk / minimal; imposes Article 9, 15, 72 obligations on high-risk. | 🟢 | [governance/04-operational-governance/regulatory/eu-ai-act-compliance-mapping.md](../governance/04-operational-governance/regulatory/eu-ai-act-compliance-mapping.md) |
| NIST AI RMF | NIST AI Risk Management Framework — Govern / Map / Measure / Manage functions for trustworthy AI. | 🟢 | [governance/05-cross-cutting/nist-ai-rmf-compliance-mapping.md](../governance/05-cross-cutting/nist-ai-rmf-compliance-mapping.md) |
| ISO/IEC 42001 | International standard for AI Management Systems — Clauses 4–10 covering context, leadership, planning, support, operation, evaluation, improvement. | 🟢 | inferred (ISO published standard) |
| ITAR / EAR | US export-control regimes (defense / dual-use). Constrain who can train on, see, or deploy models exposed to controlled technical data. | 🟢 | [CLAUDE.md compliance keywords](../CLAUDE.md) |
| Closed-loop dataset | Dataset that links input (CAD) → decision (quote/process) → outcome (manufactured cost / yield / lead-time-actual) under one operator. The structurally rare asset. | 🟡 | [intake/_example-funnel-intake-lmm.md](../intake/_example-funnel-intake-lmm.md) |
| Competitive LMM | Model whose price/lead-time/DFM accuracy on Protolabs-style RFQs measurably beats GPT-4-class general models AND beats the existing rule-based ProDesk quoter on WAPE / false-positive rate. | 🟡 | inferred from PM intent ("competitive") |

_No 🔴🔴 entries — proceeding without clarification. PM may correct any 🟡 above._

---

## Live Canvas (Layer 1) — for transcribing to printed canvas

### Box 1 — Problem & JTBD

**Current-state pain (quantified where possible):**
- ProDesk + engineer-reviewed quoting today is rule-based and labour-bounded; complex / multi-process / novel-geometry RFQs require senior engineer hours that don't scale
- Pricing accuracy drift on long-tail geometries causes either margin leak (underpricing) or lost deals (overpricing); magnitude is internally known, externally inferred to be 5–15% WAPE on edge cases
- 20 years of closed-loop data sits in CRM/ERP/ProDesk silos — it's an asset on the balance sheet that produces zero ML leverage today
- Generic LLMs (Claude/GPT-4V) commodify *extraction* but cannot price/route Protolabs parts because they lack the closed-loop ground truth — so the moat narrows every quarter we don't capture it
- 24-month strategic window before competitors close the closed-loop gap via contract-manufacturer partnerships

**JTBDs (top 3):**
1. **When I'm a Protolabs applications engineer drowning in standard quotes, I want the model to handle the 60–80% confident band so I can spend my hours on novel geometry, customer DFM consulting, and edge cases that protect margin.**
2. When I'm a customer submitting an RFQ, I want a credible price + lead time + DFM signal in seconds (not hours) so my engineering cycle doesn't stall waiting on a vendor.
3. When I'm a Protolabs exec, I want a defensible AI moat that compounds with every quote shipped, so that we are structurally harder to displace 12 months from now than today.

**Top JTBD:** #1 — it's the one that funds the others. Engineer leverage is the immediate ROI; customer speed and exec moat are downstream consequences.

### Box 2 — Users, Stakeholders, RACI

**Primary user:** Senior applications engineer reviewing AI-proposed quotes (the human in the confidence-routing loop).

**Secondary users:** RFQ-submitting customer (multi-modal input); pricing/margin manager (model output consumer); operations engineer (factory routing consumer); compliance officer (audit trail consumer).

**RACI:**

| Role | Person/Function | RACI |
|---|---|---|
| Head of AI Product (TPM) | Owns the bet end-to-end | **A** |
| AI/Data Engineering lead | Owns model architecture, training, MLOps | **R** |
| Applications Engineering lead | Owns override-UX, quality gates, override taxonomy | **R** |
| Pricing/Margin lead | Validates pricing-head accuracy & business KPIs | **C** |
| Legal & Compliance | EU AI Act conformity, GDPR DPIA, ITAR/EAR scoping, customer NDA review | **C** |
| Operations / Hubs Network | Routing-head consumer, capacity feedback | **C** |
| CISO / Security | Private endpoint, data residency, model-weight protection | **C** |
| Exec sponsor (CEO/CPO) | Funding, 24-month commitment, public commitment "no headcount cut" | **A** |
| Sales & Marketing | Informed on Phase 2 GA timing | **I** |
| Customer Support | Informed on autonomy-level changes, escalation paths | **I** |

### Box 3 — Metrics & ROI Hypothesis

**Leading indicators (weekly):**
- Engineer override rate per confidence band (target: declining 5% week-over-week post Phase-1 GA)
- Median time-to-quote for the pilot segment (target: 60s for high-confidence band by Month 6)

**Lagging indicators (quarterly):**
- WAPE on pilot segment (target: ≤5% on non-regulated CNC by Month 12; ≤3% by Month 18)
- Quote-to-order conversion delta vs. control (target: +3–8 percentage points by Month 12)

**Counter-metric (must NOT degrade):**
- Customer-reported quote dispute rate / firm-quote vs. indicative-quote delta — bad quotes in front of strategic accounts kill the bet faster than slow quotes

**ROI hypothesis (numeric range with assumptions):**
- Inputs: $200K–$400K Phase 1; $500K–$1M Phase 2; $2M–$5M Phase 3 (per strategy doc §6)
- Returns by Month 24: (a) 30–60% engineer-hour reclaim on pilot segments → $X redirected to high-margin DFM consulting; (b) 1–3% gross-margin uplift from pricing accuracy on production-volume orders; (c) 3–8pp conversion uplift from sub-minute quote SLA
- Assumption that breaks the ROI: if labelled-pair curation can't reach 500 pairs by Month 6, Phase 2 slips and the flywheel doesn't ignite

### Box 4 — Knowns / Unknowns / Risks

**Knowns:**
- Closed-loop dataset exists across CNC / IM / SM / 3DP under one operator — structurally rare
- ProDesk + Hubs Network give a working baseline + supplier-routing data
- LLM extraction layer is commodity; the moat is the geometry/pricing/outcome heads
- Engineer override = labelled training data — the people-strategy IS the data strategy
- Bifurcated EU AI Act path is feasible (limited-risk first, high-risk later)

**Unknowns (testable):**
- Q1: How much of the 20-year archive is **legally usable** for training (NDA / customer-IP / ITAR scoping)?
- Q2: What's the **WAPE delta** between a fine-tuned domain model and GPT-4V on a 500-pair held-out set?
- Q3: Does the B-rep encoder need to be **built, partnered, or licensed** — and what's the talent gap between options?
- Q4: How fast does the **override flywheel actually accelerate** — i.e., does 1,000 overrides/month produce measurable accuracy gains or do we need 10,000?
- Q5: Will customers **accept AI-generated quotes** as binding (vs. indicative) — and at what confidence threshold?

**Risks (probability × impact × mitigation owner):**

| Risk | P | I | Mitigation | Owner |
|---|---|---|---|---|
| Customer-IP / NDA exposure in training data | High | High | Legal-led classification, opt-in tiering, differential privacy, anonymisation | Legal & Compliance |
| EU AI Act high-risk class triggers stall launch | Med | High | Bifurcated deployment — ship limited-risk path first; early conformity prep | Compliance + AI Eng |
| **Wrong autonomy level** — auto-quote a part we should have routed to engineer | Med | High | Confidence-routing thresholds set conservatively; HITL by default; kill-switch | Apps Eng lead |
| Internal data silos block unification | High | Med-High | Treat unification as P0; named exec sponsor; quarterly OKR | Head of AI Product |
| Foundation-model talent scarcity | Med | High | Academic partnership for encoder; keep heads in-house; budget for 2 senior hires | AI Eng lead |
| Closed-loop dataset replicated by Xometry/Fictiv partnership | Med | Med-High | 24-month window pressure; ship Phase 1 inside 6 months | Head of AI Product |
| Engineer team treats project as headcount threat | Med | High | Public no-cut commitment; co-design rule; "AI Engineering Liaison" role | Apps Eng lead + CEO |

### Box 5 — Data Reqs & Compliance

**Data we have / need / blocked:**

| Status | Asset | Owner |
|---|---|---|
| ✅ Have | Historical RFQ corpus (100K–1M+ quotes) | Sales Ops |
| ✅ Have | DFM issue → outcome mapping (10K–50K issues) | Apps Engineering |
| ✅ Have | Process-specific pricing signals (ProDesk) | Pricing |
| ✅ Have | Customer conversion data (50K–200K interactions) | Sales Ops + CRM |
| 🟡 Need | Labelled input → Order-Object pairs (target 500–2,000) | AI Eng + Apps Eng |
| 🟡 Need | Structured engineer-override taxonomy (1,000+ events) | Apps Eng (UI instrumentation) |
| 🟡 Need | Quote → firm-quote delta tracking | Sales Ops + ERP |
| 🔴 Blocked | Customer NDA opt-in for legacy data — needs legal review per contract class | Legal |
| 🔴 Blocked | ITAR/EAR-segregated training corpus — needs export-control classification on every CAD asset | Legal + CISO |

**Governance triad (all three required):**

- **EU AI Act risk class:** **Bifurcated** — *limited-risk* for general quoting (Article 50 transparency only), *high-risk* when the model autonomously prices/routes safety-critical parts (medical implants, flight-critical aerospace) per Annex III §1. Justification: pricing of safety-critical components is a "decision affecting access to essential services" in the indirect sense and ProtoLabs' own risk appetite should treat it as high-risk by design even if Annex III doesn't strictly bind.
- **NIST AI RMF mapping:** **Govern** — model governance committee + policy, **Map** — context of use per head/per deployment tier, **Measure** — WAPE / FPR / drift continuously, **Manage** — kill-switch + rollback + post-market monitoring per governance/05-cross-cutting/nist-ai-rmf-compliance-mapping.md.
- **ISO/IEC 42001 control reference:** Clause 6.1 (risk assessment) for the bifurcated tier model; Clause 7.5 (input data) for training-corpus classification; Clause 8.4 (performance monitoring) for the drift dashboard; Clause 9.1 (evaluation) for retraining cadence; Clause 10.1 (incident response) for the rollback playbook. (See governance/ repo content.)

**Legal & Compliance posture:**

- **GDPR:** EU private endpoint (no data leaves VPC); DPIA covering training-as-purpose; right-to-erasure with data lineage; Article 22 human-review path for any automated decision; purpose-limited training (Art 5(1)(b))
- **ITAR / EAR:** Export-controlled CAD must be red-team-segregated from training corpus OR processed only by US-person-cleared infrastructure; on-prem / sovereign-cloud variant for defense customers
- **Customer IP:** NDAs honoured — opt-in for new contracts via T&C update; legacy data anonymised + feature-level aggregated (no full-CAD reproduction); customer right-to-exclude with audit trail
- **Liability allocation:** Indicative quote = ProtoLabs liability bounded by T&C; firm quote (binding) = ProtoLabs full liability — gated by HITL until model demonstrates calibrated confidence

**Working-with-Machines placement:**

- **Current autonomy level (Phase 0/1):** **Tool → Augmentation** — engineer drives, AI suggests
- **12-month target:** **Augmentation → Collaboration** for non-regulated CNC/3DP high-confidence band (auto-quote with sampling audit); **Augmentation** held for everything else
- **24-month target:** **Collaboration** for non-regulated CNC/3DP/SM; **Augmentation** for IM (mold-flow complexity); **Augmentation** held for regulated verticals (medical/aerospace/defense)
- **HITL design (where + why):** Confidence-routing in the orchestration layer — high-confidence auto-respond with sampled audit, medium-confidence engineer-quick-review, low-confidence full-engineer-review. Why: regulatory requirement (EU AI Act + ProtoLabs risk appetite) AND business requirement (one bad strategic-account quote kills trust faster than slow quotes save it).

### Box 6 — Solution Sketch + Backlog + Decisions

**Solution sketch (3 lines):**
A 3-layer system — (1) PL-LMM-Core foundation encoder trained on 20-year B-rep + outcome data; (2) specialised heads for price / lead-time / DFM-risk / process-recommendation / yield; (3) generative DFM copilot. Wraps the existing ProDesk + Hubs Network + applications-engineering workflow with confidence-routing and full audit trail. See **Appendix A** for component depth.

**Discovery stream:**
- Legal classification of 20-year archive: NDA tiers, ITAR/EAR scoping, GDPR purpose mapping
- Pilot-segment selection: 1 process × 1 customer-segment × 1 geography (likely non-regulated CNC aluminium, EU)
- Encoder build-vs-partner-vs-license decision (recommend: academic partnership, see Appendix A)
- Override-UX co-design with 2 senior applications engineers (voting members)
- Baseline WAPE measurement on current rule-based ProDesk quoter

**Build stream:**
- Phase 1 — Provenance tracker + override-logging UI + 500-pair labelled corpus + GPT-4V extraction baseline
- Phase 2 — Fine-tune Llama-3 / Mistral domain-adapted model + vector DB for similarity search + EU private endpoint
- Phase 3 — Train PL-LMM-Core encoder + specialised heads + self-learning pipeline + generative DFM copilot

**Enablement stream:**
- "AI Engineering Liaison" role — promote a respected senior applications engineer
- Public no-headcount-cut commitment in writing
- Weekly office-hours pairing (AI engineers ↔ applications engineers)
- Override-impact dashboard ("engineer X improved next-month accuracy by Y bps")
- AI Governance Board (Legal + CISO + AI Eng + Apps Eng + Compliance)

**Parked decisions:**

| Decision | Proposed owner | Trigger to revisit |
|---|---|---|
| Build vs. partner vs. license the B-rep encoder | AI Eng lead | Month 3 (after talent scan + academic-partner LOIs) |
| Open governed API tier (third-party AI-CAD tools route through PL-LMM) | Head of AI Product | Month 18 (after Phase 2 production proven) |
| Acquire vs. partner for closed-loop data on processes ProtoLabs doesn't own (e.g., casting) | CEO + Head of AI Product | Month 12 |
| Bind firm quotes (vs. indicative) at what confidence threshold | Legal + Pricing | Month 9 (after WAPE calibration) |
| Reveal LMM as a product story (marketing) vs. keep as silent moat | CMO + CEO | Month 15 |

---

## Appendix A — Solution Architecture

### Component diagram (text)

```
     ┌─────────────────────────────────────────────────────────────┐
     │                  Customer Interaction Layer                  │
     │   (multimodal RFQ portal, AI app-eng chat, quote-slider)    │
     └──────────────────────────┬──────────────────────────────────┘
                                │
     ┌──────────────────────────▼──────────────────────────────────┐
     │           Ingestion & Normalization (Layer 1, BUY)          │
     │   CAD parsing (Open Cascade) │ LLM extraction (Claude/GPT)  │
     │            → Order Object (canonical contract)              │
     └──────────────────────────┬──────────────────────────────────┘
                                │
     ┌──────────────────────────▼──────────────────────────────────┐
     │             PL-LMM-Core encoder (BUILD/PARTNER)             │
     │  B-rep tokenizer → multimodal foundation embedding (THE MOAT)│
     └──────┬──────────────┬─────────────┬──────────────┬──────────┘
            │              │             │              │
     ┌──────▼─────┐ ┌──────▼────┐ ┌──────▼──────┐ ┌─────▼──────┐
     │ Price head │ │ Lead-time │ │  DFM-risk   │ │ Process-   │
     │ (BUILD)    │ │ head      │ │ head        │ │ rec head   │
     │            │ │ (BUILD)   │ │ (BUILD)     │ │ (BUILD)    │
     └──────┬─────┘ └──────┬────┘ └──────┬──────┘ └─────┬──────┘
            │              │             │              │
     ┌──────▼──────────────▼─────────────▼──────────────▼──────┐
     │         Decision Orchestration (Layer 4, BUILD)          │
     │  Confidence routing → auto / quick-review / full-review  │
     │                  + Engineer override UI                  │
     └──────────────────────────┬──────────────────────────────┘
                                │
     ┌──────────────────────────▼──────────────────────────────┐
     │      MLOps & Governance (Layer 6, BUY+BUILD)            │
     │   Drift │ Audit trail │ Retraining │ Kill-switch        │
     │   Private EU endpoint │ Data lineage │ Model versioning │
     └─────────────────────────────────────────────────────────┘
                                │
     ┌──────────────────────────▼──────────────────────────────┐
     │          Generative DFM Copilot (Phase 3, BUILD)         │
     │  Conditional CAD-edit suggestions (VQ-CAD / diffusion)   │
     └─────────────────────────────────────────────────────────┘
```

### Build vs Buy per component

| Component | Build / Buy / Partner | Rationale |
|---|---|---|
| CAD parsing (STEP/IGES/STL) | **Buy / OSS** (Open Cascade) | Commodity; engineer hours wasted here |
| LLM extraction (Phase 1) | **Buy** (Claude / GPT-4V private endpoint) | Commodity; replace in Phase 2 |
| Domain-adapted LLM (Phase 2) | **Build** (fine-tune Llama-3 / Mistral) | Lower inference cost + accuracy + EU residency |
| Vector DB / similarity search | **Buy** (pgvector / Pinecone / Weaviate) | Commodity infra |
| **PL-LMM-Core encoder** | **Partner** (academic — Stanford SVL / MIT CSAIL / ETH) **+** in-house ownership of weights | Talent scarce; partnership accelerates v1; ProtoLabs keeps IP |
| **Specialised heads** (price / lead-time / DFM / process / yield) | **Build** | THE MOAT — proprietary outcome data only ProtoLabs has |
| Confidence-routing orchestrator | **Build** | Workflow IP + integrates with ProDesk |
| Engineer override UI | **Build** | Co-designed with applications engineering |
| MLOps tooling | **Buy** (MLflow / Weights & Biases / Vertex / SageMaker) | Commodity |
| Audit trail / data lineage | **Buy + Build** | Buy log infra, build domain-specific lineage schema |
| Generative DFM copilot | **Build** (Phase 3) | Frontier R&D; differentiation |

### Integration points

- **ProDesk** — LMM heads expose REST APIs consumed by ProDesk quote engine; existing rule-based quoter runs in shadow mode for 6 months pre-cutover
- **ERP** — outcome backfill (manufactured cost, lead-time-actual, scrap rate) feeds training labels
- **CRM** — quote-to-order conversion + customer NDA classification flags
- **Hubs Network APIs** — routing-head consumes partner capacity, quality history, geo
- **Cloud:** EU private endpoint (likely AWS eu-west / GCP europe-west); on-prem variant for defense
- **Identity & access:** SSO + RBAC; engineer-override actions logged with user ID for training-data provenance

### Maps to the 6-layer Teresa narrative

| Teresa narrative layer | LMM component |
|---|---|
| Layer 1 — Ingestion & Normalization | CAD parsing + LLM extraction |
| Layer 2 — Geometric & Manufacturability Analysis | **PL-LMM-Core encoder + DFM-risk head** (the moat) |
| Layer 3 — Pricing & ETA Engine | **Price head + Lead-time head + Process-rec head + Yield head** |
| Layer 4 — Decision Orchestration | Confidence-routing + engineer override UI |
| Layer 5 — Customer Interaction | Multimodal portal + chat + quote-slider |
| Layer 6 — MLOps & Governance | Drift / audit / retraining / kill-switch / model versioning |

### Non-functional requirements

- **Latency SLO:** Quote-end-to-end ≤60s for high-confidence band; ≤180s for medium; full-review path async with 4-hour SLA
- **Scale:** Design for 10× current RFQ volume by Month 24; 100× by Month 36
- **Availability:** 99.5% Phase 1; 99.9% Phase 2 GA; degradation = fallback to rule-based ProDesk (kill-switch)
- **Security posture:** SSO + MFA + RBAC; private VPC peering — customer CAD never traverses public internet; encrypted-at-rest (AES-256) + encrypted-in-transit (TLS 1.3); model-weight access logged + signed; quarterly third-party pen-test; SOC 2 Type II within 18 months; supply-chain SBOM; secret-rotation 90 days

### Compliance Architecture sub-section

**Per-component compliance + liability allocation table:**

| Compliance control | Component | Liability holder |
|---|---|---|
| EU AI Act Art 9 — risk-management system | MLOps & Governance layer (risk register, retraining gates) | ProtoLabs |
| EU AI Act Art 11 — technical documentation | MLOps (model cards per head + version) | ProtoLabs |
| EU AI Act Art 14 — human oversight | Decision Orchestration (confidence-routing + engineer override) | ProtoLabs |
| EU AI Act Art 15 — accuracy / robustness / cybersecurity | All heads (continuous WAPE/FPR monitoring) | ProtoLabs |
| EU AI Act Art 50 — transparency to user | Customer Interaction layer (AI-disclosure banner + provenance citations) | ProtoLabs |
| EU AI Act Art 72 — post-market monitoring | MLOps drift dashboard + incident review | ProtoLabs |
| NIST AI RMF GV-1.1 — policies & procedures | AI Governance Board charter + policy docs | ProtoLabs |
| NIST AI RMF MP-3.1 — context of use mapped | Model card per head per deployment tier | ProtoLabs |
| NIST AI RMF MS-1.1 — quantitative measures defined | WAPE / FPR / override rate dashboards | ProtoLabs |
| NIST AI RMF MG-1.1 — risk-response plan | Kill-switch + rollback playbook | ProtoLabs |
| ISO/IEC 42001 Cl. 6.1 — risk assessment | Bifurcated tier-classification doc | ProtoLabs |
| ISO/IEC 42001 Cl. 7.5 — input data | Training-corpus classification + lineage tracking | ProtoLabs |
| ISO/IEC 42001 Cl. 8.4 — performance monitoring | MLOps drift dashboard | ProtoLabs |
| ISO/IEC 42001 Cl. 9.1 — evaluation | Quarterly model evaluation report | ProtoLabs |
| ISO/IEC 42001 Cl. 10.1 — incident response | On-call + rollback playbook | ProtoLabs |
| GDPR Art 22 — automated-decision human review | Decision Orchestration HITL gate | ProtoLabs |
| GDPR Art 17 — right to erasure | Data lineage + selective re-training | ProtoLabs |
| ITAR/EAR — controlled technical data | Segregated training corpus + on-prem variant | ProtoLabs (US) + Customer (data classification) |
| Customer NDA — IP protection | Opt-in tiering + anonymisation pipeline | ProtoLabs (process) + Customer (consent) |
| Encoder partnership IP | Academic partner contract — weights to ProtoLabs | ProtoLabs (with academic partner co-author license) |
| LLM API (Phase 1) | Vendor SLA + DPA (Anthropic / OpenAI) | **Vendor** for infra + **ProtoLabs** for use |
| Cloud provider (EU endpoint) | DPA + EU data-residency clause | **Vendor** for infra + **ProtoLabs** for config |

### Working-with-Machines placement (architectural) — confidence routing

| Confidence | Order Object completeness | Routing decision | Human action | Escalation |
|---|---|---|---|---|
| > 0.85 | Complete (no missing fields) | **Auto-respond** (Phase 2+ only, non-regulated only) | None per quote; sampled audit (10%) | Customer "talk to engineer" button → engineer queue with full provenance |
| 0.60 – 0.85 | Complete or 1 ambiguous field | **Quick-review** (engineer 1-click approve / edit) | ≤2 min review | Same |
| < 0.60 | Multiple missing/ambiguous fields | **Full-review** (AI as decision support, engineer drives) | Full review | Same |
| Any (regulated vertical) | — | **Full-review by default** | Full review | Same + compliance log |
| Any (novel geometry / strategic account) | — | **Full-review** | Full review + customer-facing engineer call | Same |

Provenance trail attached to every quote: input span → extraction → confidence → engineer overrides → outcome.

---

## Appendix B — Cost & Timeline

| Phase | Window | Engineer-weeks | Cloud $/mo (pilot → scale) | Headcount asks | Milestones | Kill criteria |
|---|---|---|---|---|---|---|
| Discovery | T+0 to T+30 days | 8–12 ew | $5K → $5K | 0 (existing team) | Legal classification of archive complete; pilot segment selected; baseline WAPE measured | Legal blocks > 70% of archive from training |
| Phase 1 — Augment | T+30 to T+180 days | 80–120 ew | $15K → $40K | +1 senior MLE; +1 data eng | 500-pair labelled corpus; provenance tracker live; override-UI live; GPT-4V extraction in shadow | <500 pairs by Month 6 OR override rate > 50% |
| Phase 2 — Fine-Tune | T+180 to T+540 days | 200–350 ew | $50K → $150K | +2 senior MLE; +1 MLOps; encoder partnership LOI signed | Domain-adapted model beats GPT-4V on held-out set; vector DB live; EU private endpoint; replace pricing for non-regulated CNC/3DP | Fine-tuned WAPE not better than baseline OR encoder partner falls through with no Plan B |
| Phase 3 — LMM | T+540 to T+1080 days | 400–700 ew | $200K → $500K | +2 senior MLE; +1 generative-AI specialist; budget for compute bursts | PL-LMM-Core trained; self-learning loop measurably improving WAPE month-over-month; generative DFM copilot accepted by customers | Self-learning loop produces no measurable accuracy improvement after 2 retraining cycles |

**Total 24–36mo investment (per strategy doc §6):** $2.7M–$6.4M. Assumes EU private cloud (not on-prem); excludes data-center / on-prem variant for defense which adds ~$500K–$1M.

---

## Appendix C — Experiment / Test Plan

**Hypothesis (single sentence, falsifiable):**
A domain-adapted model fine-tuned on 500–2,000 ProtoLabs (input → corrected Order Object) pairs will achieve ≥3 percentage-point lower WAPE on a held-out 200-quote test set in non-regulated CNC aluminium, compared to GPT-4V baseline, within 6 months of Phase 1 start.

**Method:**
- Pilot scope: non-regulated CNC aluminium, EU customers, single-process orders
- N: 200-quote held-out test set (stratified by complexity tier)
- Duration: 12 weeks of corpus curation + 4 weeks of training + 2 weeks of evaluation = 18 weeks
- Comparators: (a) current rule-based ProDesk quoter, (b) GPT-4V zero-shot, (c) GPT-4V few-shot, (d) fine-tuned domain model

**Success bar (numeric):**
- Fine-tuned model WAPE ≥3pp lower than GPT-4V baseline AND ≥2pp lower than current rule-based ProDesk
- Override rate on engineer-validator UI <30% on the high-confidence band
- Median time-to-quote for high-confidence band ≤60s

**Kill criteria (numeric):**
- Fine-tuned model WAPE within ±1pp of GPT-4V (no domain advantage) → kill Phase 2 fine-tune; revisit corpus quality
- Override rate >50% → kill auto-quote ambition; remain in Augmentation
- Three or more strategic-account quote disputes traced to model error → halt + post-mortem

**Duration:** 18 weeks total

**Learning we capture even if it fails:**
- Empirical mapping of which Order-Object fields are hardest for AI (informs roadmap)
- Override taxonomy with reason codes (informs Phase 2/3 corpus targeting)
- Calibrated baseline of GPT-4V capability on Protolabs RFQs (informs build-vs-buy on every adjacent use case)
- Customer trust signal: do they use the indicative quote as a budgeting input even when wrong?

---

## Appendix D — Competitive Scan (Xometry + Fictiv)

### Xometry

| Capability | Evidence description | URL |
|---|---|---|
| Instant quoting with image / CAD recognition | Public product page: "Instant Quoting Engine" — describes ML-driven pricing | https://www.xometry.com/instant-quoting-engine/ |
| Large US manufacturing partner network | Public investor materials + product pages | https://www.xometry.com/about/ |
| Multi-process coverage (CNC, 3DP, IM, SM) | Public product pages | https://www.xometry.com/capabilities/ |
| AI/ML team + capability | LinkedIn presence; some technical blog posts | https://www.xometry.com/resources/ (product blog) |
| **Public evidence of proprietary foundation model / LMM** | **No public evidence found** | — |
| **Public evidence of self-learning loop with override-data flywheel** | **No public evidence found** | — |
| EU AI Act-native governance posture | **No public evidence found** | — |
| Bifurcated regulated/non-regulated deployment | **No public evidence found** | — |

### Fictiv

| Capability | Evidence description | URL |
|---|---|---|
| Digital quoting + CAD-centric workflow | Public product pages | https://www.fictiv.com/ |
| IP control / supplier vetting narrative | Public product / blog content | https://www.fictiv.com/why-fictiv |
| Multi-process coverage (CNC, IM, 3DP, urethane) | Public capability pages | https://www.fictiv.com/capabilities |
| **Public evidence of multimodal pre-CAD entry (photo / sketch / PDF spec)** | **No public evidence found** — Fictiv funnel-top is CAD-centric | — |
| **Public evidence of proprietary foundation model / LMM** | **No public evidence found** | — |
| **Public evidence of self-learning override-data flywheel** | **No public evidence found** | — |
| EU AI Act-native governance posture | **No public evidence found** — primarily US market | — |

> Caveat: "no public evidence found" ≠ "doesn't exist internally." Both companies could plausibly have undisclosed model strategies; competitive monitoring (patent filings, job postings for foundation-model engineers, conference talks) should be a continuous workstream.

### ProtoLabs current state

- **ProDesk** — AI-enabled real-time quoting + DFM analyzer, rule-based engine, in production [public product page](https://www.protolabs.com/services/digital-services/digital-platform/)
- **Hubs / Protolabs Network** — global manufacturing partner network, supplier-side scale unique among competitors
- **20-year closed-loop dataset** — geometry → quote → process → manufactured outcome under one operator (the structurally rare asset)
- **EU footprint + governance maturity** — Netherlands HQ for European ops; existing compliance scaffolding for AI Act / GDPR per governance/ repo

### Differentiation thesis

Protolabs wins this use case because the moat is the **integrated closed-loop flywheel**, not any single capability. Xometry can buy a fine-tuned LLM. Fictiv can build a similarity-search system. Neither can replicate 20 years of geometry → quote → process → manufactured-outcome data under one operator without rebuilding ProtoLabs' entire production history. Combined with a bifurcated EU AI Act-native governance posture (which a US-headquartered competitor would have to retrofit, not design-in), the Hubs Network supply realism, and the engineer-as-teacher people strategy, the LMM bet *operationalises* an asset only ProtoLabs holds. The 24-month window is the time before contract-manufacturer partnerships could let competitors approximate the closed loop — which is why "do nothing" is the highest-risk option, not "go now."

### Adjacent threat

**Generic-LLM customer disintermediation (one line):** A customer pasting CAD + spec into Claude/ChatGPT gets a plausible-sounding quote estimate but lacks capacity-aware ETAs, supplier matches, non-binding-quote legal scaffolding, and ProtoLabs-specific pricing accuracy. Threat exists, is bounded, and is exactly what this strategy operationalises against.

---

## Appendix E — Historical Data & Proprietary Model Strategy

> Required because this use case is foundationally about historical data as competitive asset, model fine-tuning, self-learning loops, and data-flywheel mechanics.

### Data flywheel diagram

```
Customer submits multimodal RFQ (CAD + intent)
           ↓
  PL-LMM heads predict {price, lead-time, DFM-risk, process, yield}
           ↓
  Confidence router decides: auto / quick-review / full-review
           ↓
  Engineer reviews → corrects / approves
           ↓ (correction event = labelled training pair)
  Quote sent → customer responds (won / lost) [conversion label]
           ↓
  Order produced → ERP records (actual cost, cycle time, scrap, returns) [outcome label]
           ↓
  All three signals (correction, conversion, outcome) → training corpus
           ↓
  Quarterly retraining → improved heads → fewer overrides → better quotes
           ↓
  → higher conversion → more orders → more outcome data → [flywheel accelerates]
```

### Phased model evolution

| Phase | Months | Approach | Why |
|---|---|---|---|
| Augment | 0–6 | **Buy** Claude/GPT-4V for extraction; **build** provenance + override logging | Ship MVP fast; capture training data |
| Fine-tune | 6–18 | **Adapt** Llama-3 / Mistral on 500–2,000 labelled pairs | Lower inference cost, EU residency, manufacturing-terminology accuracy |
| Foundation | 18–36 | **Own** PL-LMM-Core encoder + heads, trained on full 20-year archive | Multimodal manufacturing reasoning; cross-process transfer; the moat |

### Defensibility table

| Asset | Replicability | ProtoLabs advantage | Moat |
|---|---|---|---|
| LLM extraction | Low barrier | None — buy it | ❌ None |
| Provenance / citation UX | Medium | First-mover if shipped fast | 🟡 Temporary |
| Historical quote corpus (20yr) | High barrier | Unique | 🟢 Strong |
| DFM issue → outcome mapping | High barrier | Proprietary | 🟢 Strong |
| Process-specific pricing signals | Very high barrier | Machine fleet + cost data | 🟢🟢 Very strong |
| Customer conversion data | High barrier | CRM + ERP unified | 🟢 Strong |
| Fine-tuned manufacturing model | Very high barrier | Trained on the above | 🟢🟢 Very strong |
| Self-learning loop | Very high barrier | Compounds over time | 🟢🟢🟢 Dominant |

### Data requirements for next phase (Phase 2 fine-tune gating data)

| Data type | Minimum volume | Source | Current status |
|---|---|---|---|
| (RFQ input → corrected Order Object) labelled pairs | 500–2,000 | Sales Ops + Apps Eng (via override UI) | **Needs curation** — Phase 1 deliverable |
| Engineer override events with reason codes | 1,000+ | Override UI instrumentation | **Needs build** — Phase 1 deliverable |
| Quote → outcome (won/lost + final specs) | 5,000+ | CRM + ERP join | **Exists, unstructured** — Phase 1 ETL |
| DFM issue → manufacturing outcome | 200–500 | Quality + Apps Eng | **Needs curation** — Phase 1 deliverable |
| B-rep + STEP + price + outcome quadruples | 100K+ (for encoder pretraining) | ProDesk + ERP | **Exists, needs unification** — Phase 0 P0 |

### Governance implications of self-learning

| Obligation | Trigger | Implication |
|---|---|---|
| EU AI Act Art 9(3) — risk-mgmt update | Each retraining changes model behavior | Document evaluation + risk reassessment per retraining cycle |
| EU AI Act Art 15 — accuracy | Drift between retraining cycles | Continuous WAPE / FPR / calibration monitoring |
| EU AI Act Art 72 — post-market monitoring | Self-learning is "placed on market" | Drift dashboard + incident triage |
| GDPR Art 5(1)(b) — purpose limitation | Training is a separate processing purpose | DPIA must cover training-as-purpose, not just inference |
| GDPR Art 17 — right to erasure | Customer opt-out | Data lineage + selective retraining capability |
| GDPR Art 22 — automated decision-making | Auto-quote in high-confidence band | Human-review path always available |
| ITAR/EAR | Controlled CAD in training corpus | Red-team segregation OR US-person-cleared infra OR exclusion |
| IP — fine-tuned weights | Trade secret | Access-controlled weight storage; signed model artifacts; weight-exfil DLP |

### Self-learning loop diagram

```
  Engineer override event (corrected field, reason code, timestamp, user-id)
              ↓
  Outcome backfill (manufactured cost, cycle time, scrap rate)
              ↓
  Conversion outcome (quote won / lost / customer feedback)
              ↓
  Retraining corpus aggregator (with PII / IP / ITAR filters)
              ↓
  Quarterly retraining run (versioned: v1.1.0 → v1.1.1 → ...)
              ↓
  Pre-deployment evaluation gate (WAPE / FPR / calibration / fairness)
              ↓ (pass)
  Shadow deployment 2 weeks → A/B vs. previous version
              ↓ (no regression)
  Promote to production; previous version held warm for rollback (1-hour SLA)
              ↓
  Drift dashboard monitors live performance
              ↓
  [if drift detected → trigger ad-hoc retraining → loop]
```

---

## Pre-Emission Self-Check

| # | Check | ✓ |
|---|-------|---|
| 1 | Glossary has `Source` column with file path or "inferred" for every term | ✅ |
| 2 | Glossary has intro/outro framing text per glossary-procedure.md | ✅ |
| 3 | Box 5 includes all three governance frameworks (EU AI Act + NIST AI RMF + ISO 42001) | ✅ |
| 4 | Box 5 includes Working-with-Machines placement with autonomy level + 12-month target + HITL design | ✅ |
| 5 | Appendix A compliance table maps controls to specific components | ✅ |
| 6 | Appendix A compliance table includes ISO 42001 clause-level mapping (not just "lifecycle management") | ✅ (Cl. 6.1, 7.5, 8.4, 9.1, 10.1) |
| 7 | Appendix A compliance table includes liability allocation per component (vendor / Protolabs / customer) | ✅ |
| 8 | Appendix A includes Working-with-Machines sub-section with confidence-routing thresholds (numeric) | ✅ (>0.85, 0.60–0.85, <0.60) |
| 9 | Appendix A non-functional reqs include security posture detail (auth, network, audit, pen-test) | ✅ |
| 10 | Appendix D cites specific URLs for Xometry and Fictiv capability evidence, or states "no public evidence found" | ✅ |
| 11 | Portfolio tier cites memoized-questing-sphinx.md §7–8 explicitly | ✅ (Tier 3 R&D bet, substrate for Tier 1/2) |
| 12 | All four strategic dimensions surfaced: Working-with-Machines, Governance, Market Competition, Legal & Compliance | ✅ |

---

## Verification — How to use this artifact

1. **Workshop transcription**: Boxes 1–6 are designed to be transcribed onto the printed 6-box canvas in <30 minutes.
2. **Engineering review prep**: Hand Appendix A to the AI Eng lead and applications-engineering lead for line-by-line interrogation. Use `/pl-feasibility-probe` for deeper component-level pushback if needed.
3. **Skeptical-engineer rehearsal**: Run `/pl-rehearse` against this artifact to stress-test before the workshop.
4. **Cost validation**: Cross-check Appendix B engineer-week ranges with current AI/Data team capacity (4 engineers per memoized-questing-sphinx.md §1) — the LMM bet requires ≥3 incremental hires by Phase 2.
5. **Decision gate**: The five "parked decisions" in Box 6 are the first agenda items for the next AI Governance Board meeting.
6. **Live evidence**: Re-verify Xometry / Fictiv capability claims monthly — competitive landscape moves fast and "no public evidence found" is a snapshot, not a permanent state.
