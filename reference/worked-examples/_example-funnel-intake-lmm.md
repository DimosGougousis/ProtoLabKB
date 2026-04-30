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
- Inputs: B-rep + STEP (DFS-reserialized for autoregressive compatibility), optional 2D drawings + GD&T, material/tolerance intent, target quantity
- Output: feature-tokenized embedding consumed by all downstream heads
- Pretraining: masked-feature reconstruction, geometry↔price contrastive, geometry↔process contrastive, masked-tolerance prediction
- **STEP preprocessing pipeline** (validated by STEP-LLM, Jan 2026): depth-first search reserialization linearizes graph-structured STEP cross-references while preserving locality; Chain-of-Thought structural annotations guide global coherence
- **RAG module** for grounding predictions against similar historical geometries — substantially enhances completeness and renderability
- **RL refinement** with Chamfer Distance-based geometric reward to reduce geometric discrepancy during generation

**Layer 2 — Quoting heads (specialized fine-tunes)**
- Price head — per process, per region, per quantity break, with prediction interval
- Lead-time head — with confidence intervals from historical actuals
- Process-recommendation head — CNC vs. IM vs. SM vs. 3DP with rationale and counterfactual cost
- Yield/scrap-risk head — closed-loop labels from manufactured outcomes
- DFM-risk head — trained on annotated DFM-CODE corpus (entity/relation-annotated rules, CODE-ACCORD approach); produces calibrated probabilities

**Layer 3 — Generative DFM copilot**
- Conditional CAD-edit suggestions for DFM fixes
- VQ-CAD-style diffusion conditioned on PL-LMM-Core embeddings
- Material/process co-suggestion
- **Topological validation gates** (Euler characteristic, sphericity, mean curvature) to ensure generated edits are manufacturable (CADmium approach)

### Phased Roadmap (24 months)

**Phase 0 — Foundation (months 0–4):** Data unification across CNC/IM/SM/3DP, outcome-label backfill, customer-IP/NDA legal classification, governance scaffold, team standup (10–15 ML engineers + academic partnership). **New:** Build DFM-CODE annotation corpus (entity/relation-annotated DFM rules); build CADBench-equivalent evaluation suite with 5-level cognition framework.

**Phase 1 — PL-LMM v0 (months 4–10):** Train Layer-1 encoder with DFS-reserialized STEP pipeline, ship Price-Head v1 as shadow model, internal A/B vs. rule-based quoter, decision gate on WAPE improvement. **New:** Implement self-improvement training loop (iterative generate→evaluate→filter→retrain); integrate RAG module for CAD grounding; establish scaling curves across model sizes.

**Phase 2 — PL-LMM v1 production (months 10–16):** Replace pricing for non-regulated CNC/3DP, deploy DFM-risk head (trained on DFM-CODE corpus), lead-time and yield-risk heads in ProDesk, bifurcated deployment for regulated verticals. **New:** Add RL refinement with Chamfer Distance reward; deploy topological validation gates for generative outputs.

**Phase 3 — Generative copilot (months 16–24):** Conditional CAD-edit suggestions with topological validation, quote→counter-design→re-quote loop in <30s, selective expansion to regulated verticals, open API tier. **New:** Extend DFM-CODE corpus to ITAR/EAR compliance rules for automated export control screening.

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

| Risk | Severity | Mitigation | Source |
|---|---|---|---|
| Customer IP / NDA exposure in training data | High | Legal-led data classification, differential privacy, opt-in tiering | Internal |
| EU AI Act high-risk classification stalls launch | High | Bifurcated model + early conformity assessment; ship limited-risk path first | Internal |
| Internal silos block data unification | High | Treat unification as P0; executive sponsor | Internal |
| B-rep encoder underperforms on long-tail geometry | Medium | DFS-based STEP reserialization + hierarchical feature-tokenization; mesh-based co-encoder fallback | STEP-LLM (2026) |
| Foundation-model talent scarcity | Medium | Academic partnership for encoder; keep cost/outcome heads in-house | Internal |
| Closed-loop dataset replicated by competitor partnership | Medium-High | 24-month window pressure; move now | Internal |
| STEP graph structure breaks autoregressive generation | High | DFS reserialization + CoT structural annotations | STEP-LLM (2026) |
| DFM rule generalization fails on novel geometries | Medium | Annotated DFM-CODE corpus + RAG grounding | CODE-ACCORD (2024) |
| Generative copilot produces topologically invalid edits | Medium | Euler characteristic + sphericity validation gates | CADmium (2025) |
| Single-shot fine-tuning underperforms on CAD tasks | Medium | Iterative self-improvement loop (generate→evaluate→filter→retrain) | BlenderLLM (2024) |
| Evaluation metrics don't capture manufacturing relevance | Medium | 5-level cognition framework + Chamfer Distance + topological metrics | AECBench (2025), CADmium (2025) |

### Success Criteria at Month 24

- Pricing accuracy (WAPE) on non-regulated CNC + 3DP improved materially vs. 2026 baseline
- DFM false-positive rate cut substantially (engineer time reclaimed)
- Generative DFM-fix accepted by customers on a meaningful fraction of flagged parts
- Public, governed API: any AI design tool's output flows through PL-LMM for instant pricing and routing — making Protolabs the **default procurement-phase backend** for AI-generated CAD

## Research-Backed Enhancements Summary

| Enhancement | Research Source | Phase | Impact |
|---|---|---|---|
| DFS-based STEP reserialization | STEP-LLM (Shi et al., Jan 2026) | Phase 0-1 | Critical — mitigates encoder long-tail geometry risk |
| RAG module for CAD grounding | STEP-LLM (Shi et al., Jan 2026) | Phase 1 | High — substantially improves completeness and renderability |
| RL with Chamfer Distance reward | STEP-LLM (Shi et al., Jan 2026) | Phase 2 | High — reduces geometric discrepancy in generation |
| Self-improvement training loop | BlenderLLM (Du et al., Dec 2024) | Phase 1 | High — more data-efficient than one-shot fine-tuning |
| DFM-CODE annotation corpus | CODE-ACCORD (Hettiarachchi et al., Mar 2024) | Phase 0 | Critical — enables trainable DFM rule generalization |
| 5-level cognition evaluation | AECBench (Liang et al., Sep 2025) | Phase 0-1 | High — sets realistic performance expectations per task type |
| Topological validation metrics | CADmium (Govindarajan et al., Jul 2025) | Phase 2 | Medium — validates generative copilot output quality |
| Scaling law validation | Architext (Galanos et al., Mar 2023) | Phase 1 | Medium — informs model size decisions |
| LLM-as-Judge evaluation | AECBench (Liang et al., Sep 2025) | Phase 1 | Medium — scalable evaluation of complex DFM outputs |

## Jobs To Be Done (JTBD)

### JTBD Category 1: Data Foundation & Corpus Construction

| JTBD ID | Job Statement | Acceptance Criteria | Phase | Priority | Risks Addressed |
|---|---|---|---|---|---|
| JTBD-DATA-001 | When building the training corpus, I want to unify CNC/IM/SM/3DP data into a single schema so that the LMM can learn cross-process patterns | Unified schema covers all 4 processes; >90% of historical quotes mapped; data quality score >85% | Phase 0 | P0 | Internal silos block data unification |
| JTBD-DATA-002 | When preparing STEP files for training, I want DFS-reserialized representations so that the encoder can process graph-structured geometry without losing cross-reference locality | All STEP files pass through DFS reserialization pipeline; CoT structural annotations generated; locality preservation validated on 1000-sample test set | Phase 0-1 | P0 | STEP graph structure breaks autoregressive generation; B-rep encoder underperforms |
| JTBD-DATA-003 | When codifying DFM rules, I want an entity/relation-annotated DFM-CODE corpus so that the DFM-risk head can generalize beyond hand-coded rules | 500+ DFM rules annotated with entities (features, materials, processes) and relations (constraints, thresholds); inter-annotator agreement >80%; corpus covers all 4 processes | Phase 0 | P0 | DFM rule generalization fails on novel geometries |
| JTBD-DATA-004 | When handling customer data, I want automated NDA classification and opt-in tiering so that training respects IP boundaries | 100% of training data classified (opt-in/anonymized/excluded); differential privacy applied to legacy data; legal sign-off on classification methodology | Phase 0 | P0 | Customer IP / NDA exposure |
| JTBD-DATA-005 | When backfilling outcome labels, I want actual-vs-quoted deltas for every manufactured order so that the model learns from ground truth | >80% of manufactured orders have actual cycle time, scrap rate, and cost linked to original quote; data completeness dashboard live | Phase 0 | P1 | Evaluation metrics don't capture manufacturing relevance |
| JTBD-DATA-006 | When building the evaluation suite, I want a CADBench-equivalent benchmark with 5-level cognition tasks so that we can measure progress across memorization, understanding, reasoning, calculation, and application | Benchmark covers 20+ tasks across 5 cognitive levels; >4000 questions/evaluations; LLM-as-Judge rubrics validated by domain experts | Phase 0-1 | P0 | Evaluation metrics don't capture manufacturing relevance |

### JTBD Category 2: Model Architecture & Training

| JTBD ID | Job Statement | Acceptance Criteria | Phase | Priority | Risks Addressed |
|---|---|---|---|---|---|
| JTBD-MODEL-001 | When training the foundation encoder, I want to start from an open-source-warm-started or partner-built base so that we reach v1 in <10 months while keeping cost/outcome IP proprietary | Encoder trained and validated; WAPE on held-out test set meets baseline; partner IP agreement signed | Phase 1 | P0 | Foundation-model talent scarcity |
| JTBD-MODEL-002 | When fine-tuning CAD-specific behavior, I want an iterative self-improvement loop so that the model improves beyond what one-shot supervised fine-tuning achieves | 3+ self-improvement iterations completed; each iteration shows measurable improvement on CADBench; filtered training set quality >90% | Phase 1 | P0 | Single-shot fine-tuning underperforms |
| JTBD-MODEL-003 | When the encoder processes STEP geometry, I want a RAG module that retrieves similar historical parts so that predictions are grounded in actual manufacturing precedent | RAG retrieval latency <200ms; top-5 retrieval accuracy >80%; downstream head accuracy improves >5% with RAG vs. without | Phase 1 | P1 | B-rep encoder underperforms on long-tail geometry |
| JTBD-MODEL-004 | When training the DFM-risk head, I want it trained on the DFM-CODE corpus so that it produces calibrated probabilities rather than binary rules | DFM-risk head AUC >0.85 on held-out test set; calibration error <5%; covers all 4 manufacturing processes | Phase 2 | P0 | DFM rule generalization fails on novel geometries |
| JTBD-MODEL-005 | When refining generated geometries, I want RL with Chamfer Distance reward so that outputs have lower geometric discrepancy | Chamfer Distance improves >15% vs. non-RL baseline; visual quality validated by manufacturing engineers on 500-sample set | Phase 2 | P1 | Generative copilot produces topologically invalid edits |
| JTBD-MODEL-006 | When validating generative DFM copilot outputs, I want topological correctness gates (Euler characteristic, sphericity) so that suggested edits are always manufacturable | 100% of generated edits pass Euler characteristic validation; sphericity within tolerance of original; zero topologically invalid outputs in production | Phase 2-3 | P1 | Generative copilot produces topologically invalid edits |
| JTBD-MODEL-007 | When selecting model size, I want scaling curves established for manufacturing-specific tasks so that we right-size the encoder without over/under-provisioning | Scaling curves plotted for 3+ model sizes on CADBench; optimal size identified for cost/accuracy trade-off; results documented | Phase 1 | P2 | Foundation-model talent scarcity |

### JTBD Category 3: Compliance & Governance

| JTBD ID | Job Statement | Acceptance Criteria | Phase | Priority | Risks Addressed |
|---|---|---|---|---|---|
| JTBD-GOV-001 | When deploying for regulated verticals, I want bifurcated model architecture (limited-risk vs. high-risk) so that EU AI Act compliance doesn't block non-regulated launch | Two deployment tiers operational; limited-risk tier passes conformity assessment; high-risk tier has documented risk management system per EU AI Act Art. 9 | Phase 1-2 | P0 | EU AI Act high-risk classification stalls launch |
| JTBD-GOV-002 | When training on potentially controlled data, I want automated ITAR/EAR screening so that no controlled technical data enters the general training corpus | Screening pipeline flags 100% of ITAR/EAR-controlled data; red-team-segregated corpus for defense variant; on-prem deployment option validated | Phase 0 | P0 | ITAR/EAR compliance violation |
| JTBD-GOV-003 | When the DFM-risk head flags issues, I want NIST AI RMF traceability (Govern/Map/Measure/Manage) per head per deployment tier so that every model decision is auditable | NIST AI RMF mapping documented for each head; Measure metrics defined and instrumented; Manage procedures tested via tabletop exercise | Phase 1 | P1 | Regulatory audit failure |
| JTBD-GOV-004 | When extending DFM rules to compliance domains, I want an ITAR/EAR compliance corpus (entity/relation-annotated) so that the model can screen export-controlled designs automatically | 200+ ITAR/EAR rules annotated; automated screening achieves >95% recall on test set; false-positive rate <10% | Phase 3 | P1 | ITAR/EAR compliance violation |
| JTBD-GOV-005 | When customers use the public API, I want per-customer data isolation and audit trails so that no customer's data improves another customer's predictions | Data isolation validated by penetration test; audit trail covers 100% of API calls; customer can request data deletion within 30 days (GDPR Art. 17) | Phase 3 | P1 | Customer IP / NDA exposure |

### JTBD Category 4: Evaluation & Quality Assurance

| JTBD ID | Job Statement | Acceptance Criteria | Phase | Priority | Risks Addressed |
|---|---|---|---|---|---|
| JTBD-EVAL-001 | When evaluating the Price-Head, I want WAPE improvement measured against the 2026 rule-based baseline so that we have a clear go/no-go gate for production deployment | WAPE improves ≥X% on held-out non-regulated CNC+3DP test set; improvement statistically significant (p<0.05); results reviewed by pricing team | Phase 1 | P0 | Internal — production readiness gate |
| JTBD-EVAL-002 | When evaluating DFM outputs, I want LLM-as-Judge with expert-derived rubrics so that we can scale evaluation of complex, long-form DFM explanations | Rubrics cover 10+ DFM output types; inter-rater reliability >0.8 (Cohen's kappa); LLM-as-Judge agreement with human experts >85% | Phase 1-2 | P1 | Evaluation metrics don't capture manufacturing relevance |
| JTBD-EVAL-003 | When evaluating generative copilot outputs, I want topological metrics (Euler characteristic, sphericity, mean curvature) so that we catch geometric quality issues that simple metrics miss | Topological metrics computed for 100% of generated outputs; threshold violations trigger automatic rejection; metrics dashboard live | Phase 2 | P1 | Generative copilot produces topologically invalid edits |
| JTBD-EVAL-004 | When the model is in production, I want continuous monitoring of prediction drift so that model degradation is detected before it impacts customers | Drift detection alerts fire within 24 hours of degradation; automated retraining triggered on drift threshold; customer-facing accuracy dashboard updated weekly | Phase 2-3 | P1 | Model degradation in production |

### JTBD Category 5: Competitive & Strategic

| JTBD ID | Job Statement | Acceptance Criteria | Phase | Priority | Risks Addressed |
|---|---|---|---|---|---|
| JTBD-STRAT-001 | When competitors partner with contract manufacturers, I want the LMM v1 shipped within the 24-month window so that Protolabs' closed-loop data advantage is converted to a model moat | LMM v1 in production for non-regulated CNC+3DP by month 16; competitive gap analysis updated quarterly; 24-month deadline has executive visibility | Phase 0-2 | P0 | Closed-loop dataset replicated by competitor partnership |
| JTBD-STRAT-002 | When AI design tools generate CAD, I want PL-LMM as the default procurement-phase backend so that any AI-generated design flows through Protolabs for instant pricing and routing | Public API live; 3+ AI design tool integrations; API latency <5s for indicative quote; developer documentation published | Phase 3 | P1 | Strategic — market positioning |
| JTBD-STRAT-003 | When presenting to the board, I want a clear build-vs-partner decision framework for the encoder so that investment is justified against alternatives | Build/partner/license options scored on cost, time-to-v1, IP control, talent access; recommendation documented with executive sign-off | Phase 0 | P1 | Foundation-model talent scarcity |

## Expected Funnel Intake Outputs

Running `/pl-funnel-intake intake/_example-funnel-intake-lmm.md` should produce:

1. **Glossary** — terms like LMM, B-rep, WAPE, DFM, HITL, ITAR, EAR, EU AI Act, NIST AI RMF, ISO 42001, data flywheel, DFS reserialization, RAG, Chamfer Distance, DFM-CODE, self-improvement loop, topological validation, etc.
2. **6-Box Canvas** — all 6 boxes populated with PM voice, JTBDs, RACI, metrics, risks, compliance triad, solution sketch
3. **Appendix A** — component diagram (encoder with DFS reserialization, RAG module, heads, generative layer with topological gates, MLOps), build-vs-buy table, compliance architecture with specific NIST sub-IDs and ISO 42001 clauses, confidence-routing thresholds, liability allocation per component
4. **Appendix B** — engineer-weeks per phase, cloud costs, milestones at T+30/T+90/T+180, kill criteria, headcount asks
5. **Appendix C** — hypothesis (shadow model WAPE beats rules by ≥X%), pilot scope, success/kill criteria, duration
6. **Appendix D** — Xometry and Fictiv competitive scan with verifiable URLs, Protolabs differentiation thesis
7. **Appendix E** — **MUST be populated** (this use case explicitly involves historical data, proprietary model, self-learning loop, data flywheel)
8. **Appendix F** — Research evidence base: STEP-LLM, BlenderLLM, CODE-ACCORD, AECBench, CADmium, Architext with links and key findings
