---
type: use-case-explorer
domain: customer-edge (RFQ)
portfolio_anchor: memoized-questing-sphinx.md §7–8, Tier 1 table — "Multimodal RFQ portal" + "Engineer copilot" + "Confidence-aware quoting"
reference_intake: _example-funnel-intake-secure-design-to-order.md
generated: 2026-04-27
---

# /pl-use-case-explorer — RFQ Domain

## Step 1 — Parse Domain

The worked example (Secure Design-to-Order Sandbox) centers on the **RFQ (Request for Quote)** interaction surface — the moment a customer submits a design and Protolabs responds with a quote + ETA. Mapping to the portfolio:

- **Domain:** "customer-edge" → **Bucket 1 (Edge Solutions for Clients)**
- **Cross-cuts:** Bucket 3 (Pricing & Quotes) for the quoting engine, Layer 2 (DFM) for the analysis substrate
- **Portfolio anchor:** `memoized-questing-sphinx.md` §7, Tier 1 table — "Multimodal RFQ portal" + "Engineer copilot" + "Confidence-aware quoting"

---

## Step 1.5 — Glossary of Assumed Definitions

_I extracted the following domain-specific terms from the RFQ/SDTO context. Review and correct any that don't match your intent._

| Term | Assumed Meaning | Confidence | Source |
|------|-----------------|------------|--------|
| RFQ | Request for Quote — customer submission of CAD + specs requesting price + lead time | 🟢 | CLAUDE.md routing keywords |
| Order Object | Normalized JSON contract: geometry pointer + material + tolerance + qty + intent + provenance | 🟢 | memoized-questing-sphinx.md §2 |
| Confidence routing | Pattern of routing AI output to auto-process / quick-review / full-review / refuse based on calibrated thresholds | 🟢 | memoized-questing-sphinx.md §2 |
| HITL (Human-in-the-Loop) | Control pattern where a human reviews/approves AI output before downstream action | 🟢 | governance/05-cross-cutting/glossary.md |
| DFM | Design for Manufacturability — evaluation of whether a part can be economically produced by a given process | 🟢 | CLAUDE.md + AI-CAD-DESIGN-FEATURES-CATALOGUE.md |
| Working-with-Machines (WwM) | Protolabs autonomy framework: Tool → Augmentation → Collaboration → Automation | 🟢 | memoized-questing-sphinx.md §4 |
| ProDesk | Protolabs' existing AI-enabled manufacturing platform with real-time quoting + DFM | 🟢 | CLAUDE.md |
| SDTO | Secure Design-to-Order — sandboxed CAD environment where Save ≡ Order trigger | 🟡 | solutions-discovery/cad-design-to-order-aws-appstream.md |
| Multimodal RFQ | RFQ intake accepting CAD, photos, sketches, PDFs — not just STEP files | 🟡 | memoized-questing-sphinx.md §7 |
| EU AI Act risk class | Limited / High / Unacceptable risk tiers under Regulation (EU) 2024/1689 | 🟢 | governance/01-discovery-governance/checklists/eu-ai-act-risk-classification.yaml |

_No 🔴🔴 entries — proceeding without clarification._

---

## Step 2 — Generate Candidate List

From `memoized-questing-sphinx.md` §7–8, extracting 5 candidates that map to the RFQ / customer-edge domain:

---

### Candidate 1: Multimodal RFQ Portal

**1-line description:** Customer drops CAD, photo, sketch, or PDF spec; AI converts to a structured Order Object and routes to the quoting pipeline.

| Axis | Score | Justification |
|------|-------|---------------|
| Impact | 5 | Unlocks the long-tail of customers who don't have clean STEP files; directly expands TAM and reduces intake friction |
| Feasibility | 4 | LLM + VLM commodity tech; Layer 1 ingestion already partially exists in ProDesk; 4 engineers can ship a pilot in 90 days |
| Data Readiness | 4 | Historical quote data + existing Order Object schema provide training signal; multimodal parsing is commodity |
| Strategic Fit | 5 | Directly delivers on "speed and certainty" promise; differentiator vs. Xometry/Fictiv who still require structured uploads |

**Tier:** 1 — ship in 6–9 months
**Autonomy:** Start: Augmentation (AI extracts, human confirms) → Y1: Collaboration (AI extracts + validates, human samples)
**EU AI Act:** Limited risk (transparency obligations only; no safety-critical decision)
**Xometry/Fictiv gap:** Leapfrog opportunity — neither offers true multimodal intake

#### Acceptance Criteria

| # | Acceptance Criterion | Test Type | Kill-if-fails |
|---|----------------------|-----------|---------------|
| 1 | AI extracts material, quantity, tolerance, and finish from an unstructured email+PDF combo with ≥90% field accuracy on a 50-sample test set | Integration (extraction accuracy) | <80% field accuracy |
| 2 | Order Object created from a hand-drawn sketch passes downstream DFM validation without manual field correction in ≥85% of cases | End-to-end integration | <70% pass-through rate |
| 3 | End-to-end latency from file drop to structured Order Object ≤15s p95 for files ≤50MB | Latency | >30s p95 |
| 4 | System correctly refuses ambiguous input (e.g., corrupted file, non-manufacturing document) with a human-readable error in ≥95% of negative test cases | Security/compliance (refusal) | <85% correct refusal |

---

### Candidate 2: Confidence-Aware DFM + Quote Engine

**1-line description:** Every quote carries a calibrated confidence band; high-confidence quotes auto-issue, medium routes to engineer review, low refuses with clarification request.

| Axis | Score | Justification |
|------|-------|---------------|
| Impact | 5 | Core revenue engine — quote accuracy × speed = conversion × margin; 1% accuracy improvement at scale = significant $ |
| Feasibility | 3 | Requires calibrated confidence model + engineer-validator UX + integration with existing pricing/ETA layers; non-trivial |
| Data Readiness | 5 | Rich historical quote-to-actual-cost data; every quote has a known outcome — supervised learning on a silver platter |
| Strategic Fit | 5 | THE defining feature of the Section-2 architecture; the compounding moat that makes Protolabs harder to displace each quarter |

**Tier:** 1 — ship in 6–9 months (the wedge)
**Autonomy:** Start: Augmentation (AI proposes, human approves every quote) → Y1: Collaboration (AI auto-quotes high-confidence band, human samples + audits)
**EU AI Act:** Limited risk for commercial; High risk when touching safety-critical (medical/aerospace) — requires Article 14 HITL
**Xometry/Fictiv gap:** Leader — neither publishes confidence bands or routes by calibrated uncertainty

#### Acceptance Criteria

| # | Acceptance Criterion | Test Type | Kill-if-fails |
|---|----------------------|-----------|---------------|
| 1 | Confidence scores are calibrated: quotes with confidence ≥0.85 have actual-cost deviation ≤10% in ≥90% of cases on a 200-quote holdout set | Statistical calibration | <80% calibration |
| 2 | High-confidence auto-quotes achieve quote-to-order conversion rate ≥ parity with human-issued quotes on the same segment | A/B conversion test | >5pp below human baseline |
| 3 | Engineer-review SLA: ≥90% of medium-confidence quotes reviewed within 4 hours during business hours | Latency / UX time-trial | <70% within 4h |
| 4 | Zero high-confidence auto-quotes issued for parts flagged as flight-critical or medical-implant (kill-switch verified) | Security/compliance | Any violation = kill |

---

### Candidate 3: Engineer Copilot for Quote Drafting

**1-line description:** LLM drafts the customer-facing quote narrative (DFM summary, recommendations, pricing rationale); engineer edits in seconds instead of writing from scratch.

| Axis | Score | Justification |
|------|-------|---------------|
| Impact | 3 | Direct hours-saved for applications engineers; improves consistency of customer communication; moderate revenue impact |
| Feasibility | 5 | Managed LLM + RAG over KB = weeks of work, not quarters; lowest-risk build in the portfolio |
| Data Readiness | 4 | Historical quote narratives + KB articles provide training/retrieval corpus; some curation needed |
| Strategic Fit | 3 | Supports the people strategy (engineers see immediate benefit) but not a standalone differentiator |

**Tier:** 1 — ship in 6–9 months
**Autonomy:** Start: Tool (engineer drafts with AI suggestions) → Y1: Augmentation (AI drafts, engineer edits)
**EU AI Act:** Limited risk (transparency; no autonomous decision)
**Xometry/Fictiv gap:** Parity — both could bolt on an LLM; the moat is in the KB quality, not the model

#### Acceptance Criteria

| # | Acceptance Criterion | Test Type | Kill-if-fails |
|---|----------------------|-----------|---------------|
| 1 | Engineer edits ≤30% of AI-drafted quote text (measured by edit-distance) in ≥80% of quotes on a 50-quote pilot | UX time-trial | >50% edit rate in >40% of quotes |
| 2 | AI-drafted quotes contain zero factual errors about material properties, tolerances, or process capabilities in a 100-quote audit | Accuracy / compliance | ≥2 factual errors |
| 3 | Draft generation latency ≤5s p95 for quotes with ≤10 line items | Latency | >10s p95 |
| 4 | Engineer can escalate to full-human-draft with one click and the AI draft is discarded (no leakage into customer communication) | Integration / compliance | Escalation fails or draft leaks |

---

### Candidate 4: Secure Design-to-Order Sandbox (SDTO)

**1-line description:** AppStream-hosted CAD environment where Save ≡ Order trigger; for ITAR/IP-sensitive customers who cannot upload files over the open internet.

| Axis | Score | Justification |
|------|-------|---------------|
| Impact | 5 | Opens regulated-vertical TAM ($5–15M ARR potential); only solution where the file never leaves the boundary |
| Feasibility | 2 | Heavy infra build (AppStream + S3 + KMS + GovCloud); legal opinion required; 6–12 month timeline minimum; needs +2 FTE |
| Data Readiness | 3 | Existing Order Object schema + ProDesk integration points exist; but per-tenant isolation + audit trail are net-new data infra |
| Strategic Fit | 4 | Strong alignment with "speed + certainty" for regulated buyers; but cross-domain (security + manufacturing) penalized per skill rules |

**Tier:** 2 — build over 9–18 months (high impact, more engineering depth)
**Autonomy:** Start: Augmentation (AppEng reviews every regulated order) → Y1: Collaboration for non-flight-critical; stay at Augmentation for flight-critical/implant
**EU AI Act:** Limited default; High for medical-implant / flight-critical slice (Article 14 HITL mandatory)
**Xometry/Fictiv gap:** Leapfrog opportunity — neither has a hosted-CAD sandbox or GovCloud-aligned workflow

#### Acceptance Criteria

| # | Acceptance Criterion | Test Type | Kill-if-fails |
|---|----------------------|-----------|---------------|
| 1 | Save→Order Object success rate ≥95% across SolidWorks, NX, and Fusion 360 in a 50-save-per-product test | Integration | <80% success rate |
| 2 | Zero confirmed data-egress events from the sandbox in a 12-week pilot (verified by SIEM + pen-test) | Security/compliance | Any confirmed egress = kill |
| 3 | AppStream interactive latency ≤100ms p95 for input echo on assemblies ≤500MB | Latency | >200ms p95 |
| 4 | AppEng-review SLA: ≥80% of regulated orders cleared within 4 hours | UX time-trial | <60% within 4h |

---

### Candidate 5: Network Partner Match Optimizer

**1-line description:** ML routes orders to the optimal manufacturing partner by capability × capacity × quality history × geography × compliance — replacing rules-based matching.

| Axis | Score | Justification |
|------|-------|---------------|
| Impact | 4 | Directly improves on-time delivery + margin; Hubs network is the unique asset competitors can't replicate |
| Feasibility | 3 | Requires partner capacity + quality data feeds; ML routing is straightforward once data flows exist; 6–9 month build |
| Data Readiness | 3 | Partner capability data exists; real-time capacity + quality-outcome data is partially available; needs partner integration work |
| Strategic Fit | 4 | Strong alignment with "certainty" promise; but internal-ops-facing, not customer-edge — penalized per skill rules |

**Tier:** 2 — build over 9–18 months
**Autonomy:** Start: Tool (suggests top-3 partners, human picks) → Y1: Augmentation (auto-routes high-confidence, human overrides)
**EU AI Act:** Minimal risk (internal routing decision; no customer-facing AI output)
**Xometry/Fictiv gap:** Leader — Protolabs/Hubs network is larger and more global; ML routing on top is a moat

#### Acceptance Criteria

| # | Acceptance Criterion | Test Type | Kill-if-fails |
|---|----------------------|-----------|---------------|
| 1 | ML-routed orders achieve on-time delivery rate ≥3pp higher than rules-based baseline on a 500-order A/B test | A/B performance | <1pp improvement |
| 2 | Partner match latency ≤2s p95 (routing decision from Order Object to partner assignment) | Latency | >5s p95 |
| 3 | Zero orders routed to partners lacking required compliance certification (ITAR, AS9100, ISO 13485) on a 200-order audit | Compliance | Any mis-route = kill |
| 4 | Engineer override rate on ML-suggested partners ≤20% after 4-week calibration period | Adoption / UX | >40% override rate |

---

## Step 3 — Rank & Present

| Rank | Use Case | 1-line Description | Impact | Feasibility | Data Readiness | Strategic Fit | **Total** | Tier | Autonomy (start → Y1) | EU AI Act | Xometry/Fictiv gap | Rationale |
|------|----------|--------------------|--------|-------------|----------------|---------------|-----------|------|---------------------|-----------|---------------------|-----------|
| **1** | Confidence-Aware DFM + Quote Engine | Every quote carries a calibrated confidence band; routes by uncertainty | 5 | 3 | 5 | 5 | **18** | 1 | Augmentation → Collaboration | Limited (commercial) / High (safety-critical) | Leader | Highest composite score; THE compounding moat; richest data asset; directly drives conversion × margin |
| **2** | Multimodal RFQ Portal | Customer drops CAD/photo/sketch/PDF; AI → structured Order Object | 5 | 4 | 4 | 5 | **18** | 1 | Augmentation → Collaboration | Limited | Leapfrog | Tied on composite; slightly higher feasibility but less moat depth than confidence-aware quoting |
| **3** | Secure Design-to-Order Sandbox | AppStream-hosted CAD where Save ≡ Order; for ITAR/IP-sensitive buyers | 5 | 2 | 3 | 4 | **14** | 2 | Augmentation → Collaboration (non-critical) | Limited / High (implant) | Leapfrog | Highest TAM unlock but heavy infra + legal lift; Tier 2 timeline |
| **4** | Engineer Copilot for Quote Drafting | LLM drafts quote narrative; engineer edits in seconds | 3 | 5 | 4 | 3 | **15** | 1 | Tool → Augmentation | Limited | Parity | Fastest ship; strong people-strategy play; but not a standalone differentiator |
| **5** | Network Partner Match Optimizer | ML routes orders by capability × capacity × quality × compliance | 4 | 3 | 3 | 4 | **14** | 2 | Tool → Augmentation | Minimal | Leader | Unique moat via Hubs network; but internal-ops-facing, not customer-edge |

---

## Step 4 — Recommendation

> **If you can only pick one for a workshop demo, pick the Confidence-Aware DFM + Quote Engine** because it is the single highest-leverage compounding asset in the portfolio. It scores 18/20 on the composite, leads Xometry/Fictiv on the quoting surface (neither publishes confidence bands or routes by calibrated uncertainty), and is the substrate that every other Tier 1 idea reuses — the multimodal RFQ portal feeds into it, the engineer copilot drafts its output, the SDTO sandbox pipes its Order Objects into it. It is achievable within the 90-day framework (narrow pilot on simple CNC aluminum, one segment, engineer-validator UX shipped first), and it has the strongest governance posture: limited-risk by default for commercial quoting, with a clear bifurcation path to high-risk Article 14 HITL for safety-critical parts. The compounding moat is real — every quote issued, every engineer override, every customer accept/reject becomes labeled training data that no competitor entering this space can replicate without the same history.

---

## Scope Boundary & TDD Contract (for recommended use case: Confidence-Aware DFM + Quote Engine)

### In Scope (v1)
- Confidence-calibrated quoting on one segment (simple CNC aluminum, single-process) — verified by AC #1
- Auto-quote issuance for confidence ≥0.85 band with audit trail — verified by AC #2
- Engineer-review console with 4h SLA for medium-confidence band — verified by AC #3
- Kill-switch preventing auto-quote for flight-critical / medical-implant flagged parts — verified by AC #4
- Confidence score exposed on every quote (internal + customer-facing transparency) — verified by AC #1
- Engineer override → labeled training data feedback loop — verified by AC #2 (conversion parity)

### Explicitly Out of Scope (v1)
- **Multimodal RFQ intake** — deferred: separate workstream (Layer 1); v1 assumes clean STEP upload
- **SDTO sandbox** — deferred: Tier 2 infra build; depends on legal opinion + GovCloud decision
- **Dynamic pricing / volume-tier optimization** — deferred: needs 6+ months of quote-to-actual learning data
- **Network partner match optimization** — deferred: partner capacity data feeds not yet integrated
- **Multi-segment expansion** (injection molding, 3D printing, sheet metal) — deferred: v1 validates the pattern on one segment before scaling
- **Customer-facing quote optimization slider** — deferred: depends on calibrated pricing model maturity

### TDD Speed Limit
- No implementation agent may write production code without a failing test first
- Each AC maps to ≥2 test assertions (one positive, one negative/edge):
  - AC #1: positive = calibration test on 200-quote holdout; negative = adversarial inputs (novel geometry, exotic material) where confidence should be low
  - AC #2: positive = A/B conversion parity test; negative = auto-quote issued for low-confidence part (should have been routed to review)
  - AC #3: positive = SLA compliance on 100-quote sample; negative = engineer unavailable scenario (fallback routing)
  - AC #4: positive = kill-switch blocks flight-critical parts; negative = non-safety-critical parts pass through normally
- If any AC cannot be tested within the pilot environment (e.g., no flight-critical test data), the use case is blocked until test infra exists
- The ACs are the contract: implementation scope is bounded by what the ACs require, nothing more

---

## Pre-Emission Self-Check

| # | Check | ✓ |
|---|---|---|
| 1 | Glossary has `Source` column with file path or "inferred" for every term | ✓ |
| 2 | Glossary has intro/outro framing text per glossary-procedure.md | ✓ |
| 3 | 3–5 candidates extracted from portfolio map (§7–8), not invented | ✓ |
| 4 | Every candidate scored on 4 axes with 1-line justification | ✓ |
| 5 | Every candidate has Tier, Autonomy (start → Y1), EU AI Act class, Xometry/Fictiv gap | ✓ |
| 6 | Every candidate has 3–4 falsifiable acceptance criteria with test type + kill-if-fails | ✓ |
| 7 | Ranked table produced with composite score | ✓ |
| 8 | Recommendation paragraph grounded in composite score + differentiation + 90-day achievability + governance | ✓ |
| 9 | Scope Boundary & TDD Contract present for recommended use case | ✓ |
| 10 | All four strategic dimensions surfaced: Working-with-Machines, Governance, Market Competition, Legal & Compliance | ✓ |
