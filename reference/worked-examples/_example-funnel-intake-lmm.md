---
type: funnel-intake
use_case_name: Protolabs Large Manufacturing Model (PL-LMM)
domain: manufacturing-ai-foundation-model
process_hint: cnc-machining, injection-molding, sheet-metal, 3d-printing
vertical: cross-process
compliance_keywords: eu-ai-act, nist-ai-rmf, iso-42001, itar, ear, gdpr
data_keywords: historical-data, self-learning, data-flywheel, proprietary-model
---

# PL-LMM — Protolabs Large Manufacturing Model

> Golden test case for `/pl-funnel-intake`. This use case triggers Appendix E (Historical Data & Proprietary Model Strategy) because it involves historical data as a competitive asset, model fine-tuning, self-learning loops, and data flywheel mechanics.

## Use Case Description

Build a foundation-class Large Manufacturing Model (LMM) trained on Protolabs' 20-year archive of CAD geometry, quotes, DFM annotations, toolpaths, mold designs, machine routings, defect/yield records, and post-quote outcomes (won/lost, lead-time-actual, scrap, rework) across CNC, injection molding, sheet metal, and 3D printing. The LMM ingests CAD plus intent and emits price, lead time, DFM risk, process recommendation, and routing — becoming the engine behind the RFQ process.

### Strategic Context

Protolabs holds a **closed-loop manufacturing dataset**: geometry → price → process → outcome — all under one roof, all owned. The asset is structurally unique: nobody else holds geometry + price + manufactured-outcome ground truth at this scale across multiple processes. The window to convert that asset into a model is roughly 24 months before competitors close the closed-loop gap through partnerships with contract manufacturers.

### Architecture (3 Layers)

**Layer 1 — PL-LMM-Core (foundation model)**
- Inputs: B-rep + STEP, optional 2D drawings + GD&T, material/tolerance intent, target quantity
- Output: feature-tokenized embedding consumed by all downstream heads
- Pretraining: masked-feature reconstruction, geometry↔price contrastive, geometry↔process contrastive, masked-tolerance prediction

**Layer 2 — Quoting heads (specialized fine-tunes)**
- Price head — per process, per region, per quantity break, with prediction interval
- Lead-time head — with confidence intervals from historical actuals
- Process-recommendation head — CNC vs. IM vs. SM vs. 3DP with rationale and counterfactual cost
- Yield/scrap-risk head — closed-loop labels from manufactured outcomes
- DFM-risk head — replaces hand-coded rule library; produces calibrated probabilities

**Layer 3 — Generative DFM copilot**
- Conditional CAD-edit suggestions for DFM fixes
- VQ-CAD-style diffusion conditioned on PL-LMM-Core embeddings
- Material/process co-suggestion

### Phased Roadmap (24 months)

**Phase 0 — Foundation (months 0–4):** Data unification across CNC/IM/SM/3DP, outcome-label backfill, customer-IP/NDA legal classification, governance scaffold, team standup (10–15 ML engineers + academic partnership)

**Phase 1 — PL-LMM v0 (months 4–10):** Train Layer-1 encoder, ship Price-Head v1 as shadow model, internal A/B vs. rule-based quoter, decision gate on WAPE improvement

**Phase 2 — PL-LMM v1 production (months 10–16):** Replace pricing for non-regulated CNC/3DP, deploy DFM-risk head, lead-time and yield-risk heads in ProDesk, bifurcated deployment for regulated verticals

**Phase 3 — Generative copilot (months 16–24):** Conditional CAD-edit suggestions, quote→counter-design→re-quote loop in <30s, selective expansion to regulated verticals, open API tier

### Data Inventory (Conservative)

- Millions of B-rep CAD parts with priced quotes
- Tens of millions of quote line-items with feature-level pricing
- Hundreds of millions of DFM rule firings with engineer overrides
- Manufactured-order outcomes: actual vs. quoted cycle time, scrap rate, returns
- Tooling/mold libraries, material substitutions, shop routings

### Build vs. Partner (Encoder)

| Option | Trade-off |
|---|---|
| Build encoder from scratch | Full IP control. 18+ mo to v1. Highest cost. |
| Partner with academic lab (Stanford SVL, MIT CSAIL, ETH) | Fast access to talent; publish-friendly; Protolabs keeps cost/outcome head IP. **Recommended.** |
| License a commercial encoder (Autodesk, etc.) | Fastest. Cedes substrate IP and creates platform-risk dependency. |

**Recommendation:** Hybrid — partner-built or open-source-warm-started encoder, fully proprietary cost/outcome/DFM heads. The moat is the heads, not the encoder.

### Compliance & Governance (Day-One)

- **EU AI Act:** Limited-risk for general quoting, high-risk when autonomously pricing/routing regulated parts (medical implants, flight-critical aerospace). Bifurcated deployment.
- **NIST AI RMF:** Govern / Map / Measure / Manage applied per head, per deployment tier.
- **ITAR / EAR:** Training corpus must exclude or red-team-segregate controlled technical data; on-prem/sovereign-cloud variant for defense customers.
- **Customer IP:** Training must respect NDAs — opt-in for new contracts, anonymization + feature-level aggregation for legacy.

### Key Risks

| Risk | Severity | Mitigation |
|---|---|---|
| Customer IP / NDA exposure in training data | High | Legal-led data classification, differential privacy, opt-in tiering |
| EU AI Act high-risk classification stalls launch | High | Bifurcated model + early conformity assessment; ship limited-risk path first |
| Internal silos block data unification | High | Treat unification as P0; executive sponsor |
| B-rep encoder underperforms on long-tail geometry | Medium | Hierarchical feature-tokenization; mesh-based co-encoder fallback |
| Foundation-model talent scarcity | Medium | Academic partnership for encoder; keep cost/outcome heads in-house |
| Closed-loop dataset replicated by competitor partnership | Medium-High | 24-month window pressure; move now |

### Success Criteria at Month 24

- Pricing accuracy (WAPE) on non-regulated CNC + 3DP improved materially vs. 2026 baseline
- DFM false-positive rate cut substantially (engineer time reclaimed)
- Generative DFM-fix accepted by customers on a meaningful fraction of flagged parts
- Public, governed API: any AI design tool's output flows through PL-LMM for instant pricing and routing — making Protolabs the **default procurement-phase backend** for AI-generated CAD

## Expected Funnel Intake Outputs

Running `/pl-funnel-intake intake/_example-funnel-intake-lmm.md` should produce:

1. **Glossary** — terms like LMM, B-rep, WAPE, DFM, HITL, ITAR, EAR, EU AI Act, NIST AI RMF, ISO 42001, data flywheel, etc.
2. **6-Box Canvas** — all 6 boxes populated with PM voice, JTBDs, RACI, metrics, risks, compliance triad, solution sketch
3. **Appendix A** — component diagram (encoder, heads, generative layer, MLOps), build-vs-buy table, compliance architecture with specific NIST sub-IDs and ISO 42001 clauses, confidence-routing thresholds, liability allocation per component
4. **Appendix B** — engineer-weeks per phase, cloud costs, milestones at T+30/T+90/T+180, kill criteria, headcount asks
5. **Appendix C** — hypothesis (shadow model WAPE beats rules by ≥X%), pilot scope, success/kill criteria, duration
6. **Appendix D** — Xometry and Fictiv competitive scan with verifiable URLs, Protolabs differentiation thesis
7. **Appendix E** — **MUST be populated** (this use case explicitly involves historical data, proprietary model, self-learning loop, data flywheel)
