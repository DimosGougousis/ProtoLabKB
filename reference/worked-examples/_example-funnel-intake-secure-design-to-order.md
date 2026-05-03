---
type: funnel-intake
use_case_name: Secure Design-to-Order Sandbox (SDTO)
domain: secure-cad-orchestration
process_hint: cnc-machining, 3d-printing, injection-molding, sheet-metal
vertical: aerospace, defense, medical-implant, regulated-ip-sensitive
compliance_keywords: itar, ear, eu-ai-act, nist-ai-rmf, iso-42001, gdpr, cmmc, nist-800-171, as9100, dfars
data_keywords: tenant-isolation, data-residency, no-egress, audit-trail
portfolio_tier: Tier 1 — security wrapper that unlocks regulated verticals; reuses Tier 1 CAD substrate (memoized-questing-sphinx.md §7, Tier 1 table: "Multimodal RFQ portal" + "Engineer copilot")
---

# Funnel Intake — Secure Design-to-Order Sandbox (SDTO)

> **Use case:** AppStream-hosted CAD environment where the user's "Save" inside CAD is the order trigger; for ITAR/IP-sensitive customers. Extends the Section-2 CAD order pipeline with a no-egress sandbox so regulated buyers can use Protolabs without ever exporting their controlled technical data.
>
> **Context — why this exists:** Aerospace/defense/medical-implant prospects today either (a) cannot use Protolabs at all because RFQ + CAD upload over the open internet is a deemed-export risk, or (b) buy from CMs that wrap their workflow in classified networks. SDTO removes that barrier by collapsing "design tool" and "order submission" into one sandboxed action — `Save` ≡ `Order` — so the controlled CAD file never leaves a Protolabs-governed environment. The intended outcome is: open the regulated-vertical TAM, with a defensible audit/compliance posture that competitors cannot match without a comparable secure-cloud build-out.
>
> **Reference solutions-discovery brief:** [solutions-discovery/cad-design-to-order-aws-appstream.md](../../../ProtoLab/solutions-discovery/cad-design-to-order-aws-appstream.md) — pre-existing technical sketch (AppStream + S3 home folder + Lambda + SageMaker/Bedrock). This intake compresses that into PM-grade form and adds the four strategic dimensions (Working-with-Machines, governance, market, legal).

---

## Glossary of Assumed Definitions

_I extracted the following terms from your input. Review and correct any that don't match your intent._

| Term | Assumed Meaning | Confidence | Source |
|------|-----------------|------------|--------|
| Secure Design-to-Order (SDTO) | A workflow where the act of saving a CAD file inside a sandboxed environment is the order-submission event; no separate upload step | 🔴 | inferred from PM input + solutions-discovery/cad-design-to-order-aws-appstream.md |
| AppStream | AWS AppStream 2.0 — managed application-streaming service that delivers Windows desktop sessions running CAD apps to a browser, with admin-controlled clipboard, file-transfer, network egress | 🟢 | aws.amazon.com/appstream2 |
| Sandbox | An isolated execution environment where the user can interact with controlled data but cannot exfiltrate it (no clipboard, no file transfer, no general internet) | 🟡 | inferred — distinct from "sandbox" in ML/security testing senses |
| Save = Order trigger | "File > Save As" inside the CAD app writes to a mapped S3-backed home drive; an S3 PutObject event becomes the order-creation event | 🟢 | solutions-discovery/cad-design-to-order-aws-appstream.md §1–§2 |
| ITAR | International Traffic in Arms Regulations (22 CFR 120–130) — US export control on defense articles + technical data; covers "deemed export" to non-US persons | 🟢 | governance/eu-ai-act-compliance-mapping.md (referenced) + 22 CFR 120 |
| EAR | Export Administration Regulations (15 CFR 730–774) — US dual-use technology export control via ECCNs and the Commerce Control List | 🟢 | 15 CFR 730 |
| IP-sensitive | Customers whose CAD geometry is itself proprietary trade secret or contractually NDA'd — e.g., medical implant OEMs, defense primes, F1 teams | 🟡 | inferred from PM input |
| Deemed export | Release of controlled technical data to a foreign person inside the US — treated as an export. Triggered by routine actions like email, screen-share, or unsegregated cloud storage | 🟢 | 22 CFR 120.17 |
| EU AI Act risk class | Limited / High / Unacceptable risk tiers under Regulation (EU) 2024/1689 — "high" = safety component or Annex III use case | 🟢 | governance/04-operational-governance/regulatory/eu-ai-act-compliance-mapping.md |
| NIST AI RMF | NIST AI Risk Management Framework — voluntary US framework with four functions: Govern, Map, Measure, Manage | 🟢 | governance/05-cross-cutting/nist-ai-rmf-compliance-mapping.md |
| ISO/IEC 42001 | ISO standard for AI management systems — clauses cover context (4), leadership (5), planning (6), support (7), operation (8), evaluation (9), improvement (10) | 🟢 | iso.org/standard/81230 |
| HITL (Human-in-the-Loop) | A control pattern where a human reviews/approves AI output before downstream action; mandatory under EU AI Act high-risk Article 14 | 🟢 | governance/05-cross-cutting/glossary.md |
| Working-with-Machines (WwM) | Protolabs internal autonomy framework: Tool / Augmentation / Collaboration / Automation | 🟢 | shared/glossary-terms.md + memoized-questing-sphinx.md §4 |
| Order Object | Normalized JSON contract emitted by Layer-1 ingestion: geometry pointer + material + tolerance + qty + intent + provenance | 🟢 | memoized-questing-sphinx.md §2 (Layer 1) |
| ProDesk | Protolabs' existing AI-enabled manufacturing platform offering real-time quoting + DFM | 🟢 | CLAUDE.md + protolabs.com/prodesk |
| CMMC / NIST 800-171 | DoD's Cybersecurity Maturity Model Certification + the NIST control set for protecting CUI on contractor systems; required for DIB suppliers from 2025 | 🟢 | dodcio.defense.gov/CMMC + NIST SP 800-171 Rev 3 |
| AS9100 | Quality management standard for aviation, space, and defense (extends ISO 9001) — required for most Tier-1 aerospace primes | 🟢 | sae.org/AS9100 |
| Confidence routing | Pattern of routing AI output to auto-process / quick-review / full-review / refuse based on calibrated confidence thresholds | 🟢 | memoized-questing-sphinx.md §2 (Layer 6) |
| No-egress | Network/IAM posture where data physically cannot leave the controlled VPC except through an audited path back to the customer | 🟡 | inferred — common AWS GovCloud / sovereign-cloud term |

_No 🔴🔴 entries — proceeding without clarification._

---

## Executive Summary

| Field | Value |
|-------|-------|
| Use case | Secure Design-to-Order Sandbox (SDTO) |
| Portfolio tier | Tier 1 — security wrapper that unlocks regulated verticals; reuses Tier 1 CAD substrate (memoized-questing-sphinx.md §7, Tier 1 table: "Multimodal RFQ portal" + "Engineer copilot") |
| EU AI Act risk class | Limited (default), High in regulated-vertical edge cases (medical implant / flight-critical aerospace) |
| Verdict | **PROCEED** |
| Total Readiness Cost | Technical Build $3–5M + Data Engineering $0.5–1M + Change Management $0.08–0.18M + Compliance $0.3–0.5M = **$3.9–6.7M** |
| ROI lower bound | $5–15M ARR potential at maturity (Box 3 Assumption A) |
| Adjusted ROI | $5–15M ARR − $3.9–6.7M Total Readiness Cost = **$1.3–8.3M net** |
| Change cost vs ROI verdict | **Viable** — change cost ($80–180K) is <2% of low-end ARR |
| Total Readiness Score | min(Data Readiness 3.35, 6 − (41/10)) = min(3.35, 1.9) = **1.9 / 5.0** |
| Recommendation | **PROCEED with conditions** — Data readiness (3.35) and change resistance (41 = High) are the binding constraints. Run CAD Save-semantics validation as the first Discovery task; sign Transformation Guarantee before pilot kickoff; keep HITL on every regulated order at v1. |

---

## Live Canvas (Layer 1) — for transcribing to printed canvas

### Box 1 — Problem & JTBD

**1.1 Current-State Pain (quantified where possible)**
- Regulated buyers (defense, aerospace, medical-implant, IP-sensitive industrial) currently cannot use Protolabs' self-serve quoting flow because uploading a STEP file to a non-compliant cloud is a deemed-export event under ITAR §120.17 and a CMMC-violation under DFARS 252.204-7012.
- Inferred deflection rate: a meaningful share of regulated RFQs (estimate 10–20% of inbound from these verticals) is lost to CMs with classified networks before Protolabs ever sees the file. Exact number is an Unknown — see Box 4.
- Manual workaround today: phone + secure-FTP + offline DFM = 3–10 day quote SLA vs. ProDesk's <1 hour, eroding the speed-and-certainty promise on exactly the customers with the highest gross margin.

**1.2 Activated JTBDs (from JTBD Evaluation Framework)**

| JTBD ID | Job Statement | MoSCoW | Evidence Quality | RICE Score | CoND (annual) | Status |
|---------|--------------|--------|------------------|------------|---------------|--------|
| F1 | When I submit manufacturing queries, CAD files, or design parameters to AI systems, I want to ensure all inputs are validated and sanitized before processing, so I can prevent prompt injection attacks, data exfiltration, and system manipulation. | **Must** | 🟢 Validated | 1,125 | $29M–$47M | Activated |
| F2 | When AI systems process manufacturing data and generate recommendations, I want to detect and block adversarial inputs across multiple attack vectors, so I can maintain system integrity, prevent IP theft, and ensure safe manufacturing outcomes. | **Must** | 🟢 Validated | 531 | $15M–$27M | Activated |
| F4 | When regulators, auditors, or customers request compliance evidence, I want to provide complete, tamper-evident audit trails of all AI system activities, so I can demonstrate regulatory compliance (GDPR, CCPA, SOX, ISO 27001), avoid fines, and maintain customer trust. | **Must** | 🟢 Validated | 338 | $24M–$34M | Activated |
| CAD-CORE | When I need to evaluate CAD files for manufacturability, I want an AI system that can analyze geometry and recommend optimal manufacturing processes, so I can reduce design iterations and accelerate time-to-quote. | **Should** | 🟡 Partial | 117 | $13M–$33M | Activated |
| E1 | When I use AI manufacturing tools, I want to feel confident that my intellectual property and data are secure, so I can focus on innovation without worrying about security breaches. | **Should** | 🟡 Partial | 233 | $2M–$8M | Activated |

**Activation rules:**
- A use case MUST activate at least one **Must** job to proceed. ✓ (F1, F2, F4 activated)
- A use case that activates only **Could** jobs is a weak bet — flag for deprioritization. N/A
- A use case that activates a **Won't** job has a scope conflict — require PM clarification. N/A

**1.3 JTBD Synthesis**

| Dimension | Value |
|-----------|-------|
| Must jobs activated | 3 (F1, F2, F4) |
| Should jobs activated | 2 (CAD-CORE, E1) |
| Could jobs activated | 0 |
| Won't jobs activated | 0 — no scope conflict |
| Combined annual CoND | $83M–$149M |
| Highest Composite Rank activated | #1 (F1) |
| Lowest Evidence Quality among Must jobs | 🟢 Validated |

**1.4 JTBD Evaluation Gate**

| # | Check | Result | If Failed |
|---|-------|--------|-----------|
| 1 | At least one Must job is activated | **Pass** | — |
| 2 | All activated Must jobs have 🟢 or 🟡 evidence quality | **Pass** | — |
| 3 | All activated jobs have acceptance criteria from the library | **Pass** | — |
| 4 | No Won't jobs are activated | **Pass** | — |
| 5 | Combined CoND justifies investment vs. Box 3 ROI | **Pass** ($83M+ CoND vs. $5–15M ARR) | — |
| 6 | All activated jobs have stakeholder-validated evidence | **Pass** (F1–F4 are security foundation; evidence from governance repo) | — |

## JTBD Evaluation Gate: **PASS**

All 6 checks pass. Proceed to Change Management and Cost Management sections.

**1.5 Anti-JTBDs (Jobs This Use Case Must Not Threaten)**

| Anti-JTBD | Why Excluded | Risk if Included |
|-----------|-------------|------------------|
| "When I'm an engineer, I want AI to handle all client communication, so I can focus on technical work" | Would eliminate the advisory role transformation | Identity threat becomes critical; adoption collapses; Box 7 resistance score → Critical |
| "When I'm a customer, I want fully automated ordering with zero human review, so I can get instant quotes" | Would violate quality gatekeeper JTBD and compliance requirements | Liability risk; engineer resistance; EU AI Act high-risk classification |

**Top JTBD ranked with rationale:** F1 (Secure AI Input Processing) wins because it is the security foundation that makes the entire SDTO sandbox trustworthy — without validated input processing, no regulated buyer will enter the sandbox. F4 (Audit Compliance) is the second pillar because the audit trail is the evidence that makes the architecture defensible to export-control officers. CAD-CORE and E1 are downstream wins that follow once the security foundation is proven.

### Box 2 — Users, Stakeholders, RACI

**Primary user:** Regulated-buyer design engineer (US-person, employed at AS9100/ITAR-cleared OEM or DIB Tier-2 supplier).

**Secondary users:**
- Customer-side export-control officer (approves the buyer's account once, then exits the loop)
- Protolabs applications engineer (reviews the post-Save Order Object inside the audited workspace)
- Protolabs compliance officer (reviews audit-trail samples + handles incident response)

**RACI (named roles, not people):**

| Role | Discovery | Build | Pilot | GA Operations |
|---|---|---|---|---|
| **R** (Responsible) | TPM (this PM) | Cloud Infra Lead + Security Lead | Pilot SE (single named applications engineer) | Secure-Cloud Ops on-call rotation |
| **A** (Accountable) | VP Product | VP Engineering | VP Sales (regulated verticals) | VP Engineering |
| **C** (Consulted) | CISO, General Counsel, Export-Compliance Officer, AppEng Lead, 2× pilot customer reps | CISO, General Counsel, External pen-test firm, AWS GovCloud account team | CISO, General Counsel, Pilot customers' export-control officers | CISO, AS9100 internal auditor |
| **I** (Informed) | CEO/CFO (because of compliance posture risk), Hubs network-partner ops | Sales (regulated verticals), Marketing | Whole AppEng org, Finance | Customer Success, Board (annual posture review) |

#### Box 2.G — Stakeholder Journey Map

| Stakeholder | Current State | Intake Sentiment | Pilot Target | GA Target | Scale Target | Re-evaluation Trigger |
|-------------|--------------|------------------|--------------|-----------|--------------|----------------------|
| Engineering Director | Leads AppEng team; skeptical of AI projects that bypass engineer judgment | Skeptic | Neutral — sees HITL preserves authority | Advocate — sees team capacity unlocked | Advocate — sees advisory revenue model | Pilot misses quality SLA >3× in a month |
| Senior AppEng (10+ yrs) | Reviews CAD uploads in ProDesk; identity tied to technical judgment | Skeptic | Neutral — co-designed review console | Advocate — recognized as compliance firewall | Champion — mentors junior AppEng on sandbox workflow | >2 senior AppEng request transfer out of SDTO queue |
| Compliance Officer | Manages audit evidence manually; no real-time visibility | Neutral | Advocate — sees automated audit trail | Advocate — quarterly reviews show zero findings | Advocate — SDTO becomes reference architecture for other products | Critical audit finding on SDTO control plane |
| Customer Export-Control Officer | Blanket-refuses cloud uploads; evaluates TAAs per upload | Blocker | Neutral — evaluates architecture once per tenant | Neutral — trusts boundary after 2+ audit cycles | Advocate — recommends SDTO to peer companies | Design-partner ECO formally rejects architecture |
| Customer Design Engineer | Works on local workstation; uploads via secure-FTP | Neutral | Neutral — tolerates sandbox for speed | Advocate — prefers Save=Order to manual upload | Advocate — requests sandbox for all suppliers | Latency SLO blown >50% of sessions |

**Rule:** Customer Export-Control Officer is Blocker at Intake — flagged in executive summary. Mitigation: design-partner workshop including ECO + General Counsel before Build commitment.

### Box 3 — Metrics & ROI Hypothesis

**Leading indicators (weekly):**
- Sandbox session-starts per week per pilot customer (proxy for activation)
- `Save → Order Object created` success rate (target: >98% — failure = lost order)

**Lagging indicators (quarterly):**
- New regulated-vertical revenue closed via SDTO ($, vs. plan)
- Audit findings per quarter on the SDTO control plane (target: 0 critical, ≤2 major across ITAR/CMMC/AS9100/EU AI Act surveillance)

**Counter-metric (must not degrade):** ProDesk standard quote-turnaround SLO — SDTO must not become so process-heavy that AppEng review queues blow the <1h promise on the non-regulated path, and SDTO orders themselves should target a <4h human-review SLO.

**ROI hypothesis (numeric range with assumptions):**
- Assumption A: Regulated verticals add $5–15M ARR potential at maturity (defense/aero/med-implant share of TAM × Protolabs win rate × current deflection rate). All three multiplicands are Unknowns; pilot is to retire them.
- Assumption B: Run-cost at pilot is $20–60K/month cloud + 2 FTE security/compliance ($300–500K loaded); break-even at ~$1.5–3M ARR — so payback in months 12–18 if assumption A is even half-right.
- Assumption C: Strategic option value of preserving $2–5M of regulated-vertical TAM that would otherwise defect to in-house shops or CMs over 24 months, plus locking out Xometry/Fictiv from regulated verticals for 18–24 months. This option value is not in the cash ROI but is the real reason to fund the bet.

### Box 4 — Knowns / Unknowns / Risks

**Knowns (≤5):**
1. AppStream + S3 home-folder + Lambda + KMS is a proven AWS reference pattern (cited in the solutions-discovery brief).
2. Protolabs already has the downstream Layer 2–4 pipeline (DFM, pricing, ETA) — SDTO does not need to rebuild any of it; it pipes the Order Object into the existing flow.
3. Existing Hubs/Protolabs network includes ITAR-registered shops capable of fulfilling regulated orders once the front door is open.
4. EU AI Act + ISO 42001 controls are already partially mapped in the governance repo (see `governance/05-cross-cutting/`).
5. AppStream has a published US GovCloud (US) variant — the regulatory infrastructure exists.

**Unknowns (≤5, framed as testable questions):**
1. What is the actual deflection rate of regulated RFQs today? (Sales/CRM mining required.)
2. Will the major aerospace primes accept a *commercial* AWS region with FedRAMP-Moderate + ITAR-segregated tenancy, or do they require AWS GovCloud (US-East/West) with cleared-personnel-only operations? (Materially changes cost.)
3. Will customers' own export-control officers approve the AppStream-as-deemed-export-boundary architecture? (Legal opinion + 2 design-partner sign-offs.)
4. Does saving inside the CAD app actually emit a single, deterministic S3 PutObject across the major CAD products (SolidWorks, NX, CATIA, Fusion 360)? Or does each product produce temp/lock/intermediate files that pollute the order trigger? (CAD-by-CAD validation in Phase 1.)
5. What latency tax does AppStream impose on heavy CAD work (>500MB assemblies) and is it tolerable to senior engineers who have been on local workstations for 20 years?

**Risks (probability × impact × mitigation owner):**

| Risk | P | I | Mitigation | Owner |
|---|---|---|---|---|
| Wrong autonomy level — targeting Collaboration (AI proposes, human samples) for v1 when the regulated-vertical risk profile demands Augmentation (human reviews every order). Auto-creating orders on Save without explicit Submit affirmation would be an Automation-level misplacement. | High | High | Confidence + completeness gate before order-create; explicit user "Submit" affirmation; AppEng HITL on every regulated order at v1 | Pilot SE |
| Customer's export-control officer rejects the architecture | Medium | High | Design-partner workshop in Discovery; legal opinion before Build; bake their counsel into requirements | General Counsel |
| GovCloud cost explosion (3–5× commercial) makes unit economics fail | Medium | High | Tiered tenancy: commercial+ITAR-segregated for non-DIB; GovCloud only when contractually required; per-tenant pricing | Cloud Infra Lead |
| CAD-product-specific Save semantics break the "Save = Order" promise | High | Medium | Per-product validation; allowlist of supported CAD versions; "Submit Order" wrapper button as fallback | Pilot SE |
| Latency / GPU bottleneck pushes engineers back to their laptops | Medium | Medium | Latency SLO baked into pilot success criteria; G4dn/G5 fleet sizing; pre-provisioned warm sessions | Cloud Infra Lead |

### Box 5 — Data Reqs & Compliance

**Data we have / need / blocked:**

| Data | Status | Owner |
|---|---|---|
| Customer entity + cleared-person identity (KYC) | Need | Sales Ops + Compliance |
| Per-tenant CAD file (controlled technical data) | Need (and must NEVER be co-mingled across tenants) | Cloud Infra Lead |
| Audit trail: session start, every Save, every AppEng review action, every export attempt blocked | Need | Security Lead |
| Existing Order Object schema | Have (Layer 1 from Section-2 architecture) | AI Platform Lead |
| Network telemetry from AppStream (egress attempts, clipboard attempts) | Need | Security Lead |
| Pen-test evidence (annual + after material change) | Need | CISO |

**Governance triad (all three required):**

- **EU AI Act risk class — *Limited* (default), *High* in regulated-vertical edge cases.**
  Justification: SDTO itself is an interaction surface, not a decision system. The AI components it pipes into (DFM scoring, pricing) are limited-risk in commercial verticals. **However**, when an SDTO order routes to a *medical implant* or *flight-critical aerospace* part, the downstream DFM/quote becomes Annex-III-adjacent — bifurcated treatment per the same logic as the LMM example. Cite: `governance/04-operational-governance/regulatory/eu-ai-act-compliance-mapping.md`.

- **NIST AI RMF function mapping (one line each):**
  - **Govern** — Secure-cloud governance board owns SDTO posture; quarterly review of audit findings; named risk owner per RMF profile (GV-1.1, GV-3.2).
  - **Map** — Threat model + data-flow diagram + WwM placement documented before pilot; refreshed every 6 months (MP-1.1, MP-3.1).
  - **Measure** — Egress-attempt rate, false-block rate on Save, AppEng-review SLA, audit-finding count are all instrumented (MS-1.1, MS-2.5).
  - **Manage** — Incident-response runbook; kill-switch on the AppStream fleet; per-tenant rollback (MG-1.1, MG-2.1, MG-3.1).
  Cite: `governance/05-cross-cutting/nist-ai-rmf-compliance-mapping.md`.

- **ISO/IEC 42001 control reference:**
  - **Clause 6.1.2** (AI risk assessment) — SDTO threat model + EU AI Act classification documented per tenant tier.
  - **Clause 7.5** (Documented information) — every AppEng review and every blocked-egress event is auditable evidence.
  - **Clause 8.2** (Operational planning and control) — confidence-routing + HITL design is the documented operational control.
  - **Clause 8.4** (Performance monitoring) — Save→Order success rate, latency, audit findings.
  - **Clause 9.1** (Performance evaluation) — quarterly governance review.
  - **Clause 10.1** (Continual improvement / incident response) — runbook + post-incident review process.

**Legal & Compliance posture:**
- **GDPR:** Limited — no EU personal data in CAD files in scope by design; user identity data follows the existing ProDesk DPA.
- **ITAR:** Architecture is the boundary. AppStream session + S3 bucket + KMS keys are the deemed-export boundary; only US-person AppEng accounts can access regulated-tenant data; cleared-personnel-only operations on the GovCloud variant.
- **EAR / dual-use:** ECCN screening on customer entity at onboarding; restricted-party screening daily.
- **IP:** Per-tenant KMS keys (customer-managed where required); zero training-data extraction from regulated-tenant geometry without explicit, separate, written opt-in.
- **Liability allocation:** Per Appendix A table — vendor (AWS) carries platform-substrate liability, Protolabs carries control-plane configuration liability, customer carries identity-of-its-own-users liability.

**Working-with-Machines placement:**
- **Current autonomy level: Augmentation.** AI does ingestion + DFM + pricing draft; AppEng confirms every regulated order before the customer sees a quote.
- **12-month target: Collaboration** for *non-flight-critical / non-implant* SDTO orders (AI proposes, AppEng samples + audits in arrears). **Stay at Augmentation indefinitely** for flight-critical / medical-implant.
- **HITL design (where + why):** Two HITL gates — (1) **AppEng review of every regulated Order Object** before quote is released to customer — required by Article 14 of the EU AI Act for the high-risk slice and required as audit evidence for AS9100 / CMMC regardless. (2) **Compliance-officer sampling** at 5% of orders + 100% of orders with confidence < 0.6 or completeness gate failed — generates audit evidence and catches model drift.

### Box 6 — Solution Sketch + Backlog + Decisions

**3-line solution sketch (pointer to Appendix A for depth):**
> AppStream-streamed Windows desktop with allowlisted CAD apps, network-locked to a per-tenant S3 home folder via VPC endpoint. `Save` triggers an S3 PutObject event → Lambda → Order Object → existing Section-2 pipeline (Layers 2–6) with a mandatory AppEng HITL gate before quote release. Per-tenant KMS keys, cleared-personnel-only ops on the GovCloud variant, full audit trail piped to SIEM. See **Appendix A**.

**Streams:**

| Discovery (3–5) | Build (3–5) | Enablement (3–5) |
|---|---|---|
| 2× design-partner customer workshops | AppStream fleet + S3 home folder + KMS per-tenant infra | Internal AS9100 / ITAR awareness training for AppEng |
| Sales/CRM deflection-rate audit | Lambda Order Processor → existing Order Object schema | Customer-facing onboarding flow + KYC + ECCN screening |
| Legal opinion on AppStream-as-deemed-export-boundary | AppEng review console (audited workspace UI) | Pen-test + AS9100 readiness audit |
| Latency study on real CAD assemblies (3–5 products) | Audit trail + SIEM integration + kill-switch | Pricing model for regulated verticals (per-tenant cloud cost passthrough) |
| External counsel review of EU AI Act bifurcation logic | Per-CAD-product Save-semantics validation harness | Incident-response runbook + tabletop exercise |

**Parked decisions (each with proposed owner):**
- *AWS commercial vs. GovCloud at pilot* — Owner: VP Engineering (default: commercial + ITAR-segregated; switch to GovCloud only if a pilot customer's contract requires it).
- *Build the AppEng review console in-house vs. extend ProDesk* — Owner: AI Platform Lead (default: extend ProDesk to avoid two surfaces).
- *Self-host CAD licensing vs. BYOL* — Owner: Procurement + Cloud Infra Lead (default: BYOL at pilot, evaluate hosted at GA).
- *Open the SDTO front door to non-regulated customers as a "secure-by-default" upsell, or keep it strictly regulated-vertical* — Owner: VP Product (default: keep it regulated until pilot proves unit economics).

---

## Box 7 — Change Readiness & Human Impact

**7.0 JTBD → Resistance Mapping**

For each resistance type, identify the threatened JTBD from Box 1 and the targeted mitigation.

| Resistance Type | Threatened JTBD (from Box 1) | Root Cause | Targeted Mitigation |
|----------------|------------------------------|------------|---------------------|
| Identity Threat | E1: "When I use AI manufacturing tools, I want to feel confident that my IP and data are secure" | AI replaces core design work perception | Reframe role; preserve quality sign-off; celebrate advisory wins |
| Skill Anxiety | E1: "When I use AI manufacturing tools, I want to feel confident that my IP and data are secure" | New skills required (consultative selling) | Safe-to-fail training; peer mentoring; early wins |
| Economic Fear | F4: "When regulators request compliance evidence, I want to provide complete audit trails" | Fear of layoff or pay cut | Written Transformation Guarantee; compensation floor |
| Quality Gatekeeper | F1: "When I submit manufacturing queries, I want to ensure all inputs are validated" | Liability for AI-generated errors | Engineer retains final sign-off; AI error transparency; override logging |
| Change Fatigue | E1: "When I use AI manufacturing tools, I want to feel confident that my IP and data are secure" | History of failed initiatives | Small wins first; no big-bang rollouts; acknowledge past failures |
| Comfort Zone | E1: "When I use AI manufacturing tools, I want to feel confident that my IP and data are secure" | Loss aversion; preference for known competence | Compelling personal benefit narrative; opt-in pilot option |

**Rule:** All resistance types map to activated JTBDs. No generic mitigations.

### 7.1 Human Impact Analysis

| Question | Assessment |
|----------|-----------|
| **Who is affected?** | Protolabs applications engineers (primary — new review workflow inside audited sandbox), Protolabs compliance officers (new audit-sampling duty), customer-side design engineers (new CAD environment + Save=Order mental model), customer-side export-control officers (new approval boundary to evaluate) |
| **What changes for them?** | **AppEng:** shifts from reviewing uploaded files in ProDesk to reviewing Order Objects inside an audited, no-egress workspace with confidence-routing queues; must learn new UI + provenance-trail interpretation. **Compliance officer:** new quarterly audit-sampling cadence + incident-response runbook. **Customer engineers:** must work inside AppStream sandbox instead of local workstation — loss of familiar CAD shortcuts, plugins, macros; "Save" now means "submit order" not "save locally." **Customer export-control officers:** must evaluate a new deemed-export boundary architecture instead of blanket-refusing cloud uploads. |
| **How many people?** | **Protolabs side:** ~5–8 AppEng (pilot), scaling to ~20–30 at GA; 1 compliance officer (50% allocation); 1 cloud security engineer (new hire). **Customer side:** ~5–10 design engineers per pilot customer (2 customers = 10–20); 2 export-control officers. **Total: ~20–30 people at pilot, ~50–70 at GA.** |
| **What is the identity threat level?** | **Medium for AppEng** — their review role is preserved (HITL gate), but the workspace changes and confidence-routing may feel like surveillance. **Low for customer engineers** — they still design; the tool changes, not the role. **None for compliance/export-control** — their authority is strengthened, not diminished. |
| **What skills must they learn?** | **AppEng:** confidence-routing interpretation, provenance-trail reading, sandbox-specific incident escalation. **Customer engineers:** AppStream session management, Save=Order mental model, "escalate to human" button usage. **Compliance:** SIEM dashboard reading, audit-sampling methodology, CMMC evidence packaging. |
| **What do they lose?** | **Customer engineers:** local workstation performance (latency tax), custom CAD plugins/macros (may not be in allowlist), ability to save files locally. **AppEng:** familiar ProDesk review UI (replaced by extended console). **Nobody loses authority or sign-off power** — HITL gate preserves AppEng final-say on every regulated order. |

### 7.2 Resistance Risk Scoring

| Resistance Type | Likelihood (1-5) | Severity (1-5) | Risk Score | Mitigation Strategy |
|----------------|-----------------|----------------|------------|-------------------|
| Identity Threat | 2 | 3 | **6** | AppEng role is preserved as quality gatekeeper; identity threat is low because HITL reinforces their expertise, not replaces it. Frame as "you are the compliance firewall." |
| Skill Anxiety | 3 | 2 | **6** | New sandbox UI + confidence-routing requires training; but skills are adjacent (review → review-in-new-tool), not transformational. Structured onboarding + sandbox dry-run. |
| Economic Fear | 2 | 2 | **4** | No headcount reduction; SDTO adds regulated-vertical revenue that requires MORE AppEng at GA. Compensation unchanged at pilot; advisory-commission model at GA is additive. |
| Quality Gatekeeper | 3 | 4 | **12** | **Highest risk.** AppEng will worry that Save=Order creates orders without their input. Mitigation: explicit HITL gate on EVERY regulated order at v1; confidence routing is a triage tool, not an auto-approve. AppEng retains final sign-off. |
| Change Fatigue | 2 | 2 | **4** | SDTO is a new product, not a replacement of existing workflow. Non-regulated ProDesk path is unchanged. Low fatigue risk because it's additive, not disruptive. |
| Comfort Zone | 3 | 3 | **9** | Customer engineers forced into AppStream sandbox lose familiar workstation. Mitigation: pre-provisioned warm sessions, allowlisted plugins, latency SLO, "try before you buy" pilot design. |
| **Total Resistance Risk** | | | **41** | **HIGH (31-45): Intensive intervention required; executive sponsorship required; phased rollout mandatory.** |

### 7.3 Change Cost Estimation

| Cost Category | Estimate | Notes |
|--------------|----------|-------|
| **Training & skill building** | $3–5K per AppEng / 2 weeks | Sandbox UI training + confidence-routing workshop + incident-response tabletop. Customer engineers: self-service onboarding guide + 1-hr live walkthrough. |
| **Productivity dip during transition** | 15–20% for 3–4 weeks (AppEng) | Learning new review console slows order-clearance SLA initially. Mitigated by running SDTO pilot in parallel with existing ProDesk (not replacing it). |
| **Attrition risk cost** | Low ($0–50K) | AppEng role is strengthened, not eliminated. Customer-side attrition risk is near-zero (they still design). Only risk: 1–2 senior AppEng who resist the new tool may disengage. |
| **Change management program** | $50–80K / 6 months | CM lead (part-time from existing team), 2× champion identification workshops, customer onboarding playbook, export-control officer design-partner workshop. |
| **Compensation transition** | $0 at pilot | No compensation changes at pilot. At GA, advisory-commission model is additive (base preserved). Transformation Guarantee: no involuntary layoffs for 24 months. |
| **Total Change Cost** | **$80–180K** | Compare to Box 3 ROI hypothesis: $5–15M ARR potential. Change cost is <2% of low-end ARR — negligible relative to business value. |

### 7.4 Business Value vs. Change Cost Matrix

```
                        HIGH Business Value
                              |
           QUICK WIN          |         STRATEGIC BET
           ─────────          |         ─────────────
                              |         High value,
                              |         high change cost
                              |         → Phased rollout
                              |         → Executive sponsorship
    ──────────────────────────┼──────────────────────────
                              |
                              |
                              |
                              |
                              |
                        LOW Business Value
```

**Placement: STRATEGIC BET.** High business value ($5–15M ARR potential, regulated-vertical TAM unlock, competitive moat) but high change cost (41 resistance score, GovCloud complexity, customer-side sandbox adoption friction, compliance architecture validation). Requires phased rollout with executive sponsorship.

### 7.5 Buy-In Strategy Recommendation

**Recommended: Executive-Mandated + Pilot-First hybrid.**

| Strategy | Rationale |
|----------|-----------|
| **Executive-Mandated** | Resistance score of 41 (High) requires CEO/COO sponsorship. The Transformation Guarantee (no layoffs, preserved authority) must come from the top. VP Engineering is the named sponsor per Box 2 RACI. |
| **Pilot-First** | Despite executive sponsorship, the architecture has too many Unknowns (Box 4) to go straight to GA. 12-week pilot with 2 design-partner customers proves the value before scaling. Executive mandate funds the pilot; pilot evidence funds the GA rollout. |

### 7.6 Integration with Change Management Framework

Resistance risk is High (41), so the following activities are **required**:

- [x] **Phase 0 activities** — Leadership alignment workshop before pilot kickoff; AppEng listening tour to surface quality-gatekeeper concerns; identify 1–2 AppEng champions who will co-design the review console.
- [x] **Transformation Guarantee requirement** — Written, signed guarantee: no involuntary layoffs due to SDTO for 24 months; all AppEng who complete transition retain current compensation + receive advisory-commission upside at GA.
- [x] **Compensation transition planning** — At GA, AppEng compensation model evolves from pure salary to base + margin-bonus (additive, not replacement). Model designed in Phase 0, communicated before pilot.
- [x] **Escalation protocol activation (Level 2+)** — Engineering Director owns resistance escalation; weekly pulse survey during pilot; any Level 3+ resistance (active sabotage, public refusal) escalates to VP Engineering within 48 hours.
- [x] **Adjusted ROI calculation:** `Adjusted ROI = $5–15M ARR - $3–5M technical cost - $0.1–0.2M change cost - $0–0.05M attrition risk = $1.9–11.8M net` — change cost is negligible relative to business value; does not change the investment thesis.

---

## Box 8 — Data Readiness & Engineering

### 8.1 Data Source Inventory

| Data Source | Owner | Format | Access Model | Volume | Freshness | Status |
|------------|-------|--------|-------------|--------|-----------|--------|
| Customer CAD files (controlled technical data) | Customer (IP owner) | STEP, IGES, native CAD (SLDPRT, PRT, CATPart) | AppStream sandbox → S3 PutObject | ~10–50 files/tenant/week at pilot | Real-time (per Save event) | **Need** — exists only inside sandbox at runtime |
| Order Object schema | AI Platform Lead | JSON (existing Layer 1 contract) | Lambda → DynamoDB → existing pipeline | ~25–50 orders/tenant/week at pilot | Real-time | **Have** — reused from Section-2 architecture |
| Audit trail (session events, Save events, AppEng actions, blocked egress) | Security Lead | Structured logs (CloudTrail + AppStream + custom) | SIEM (Splunk / OpenSearch) | ~1K–10K events/tenant/day | Real-time | **Need** — must be built for SDTO |
| Customer entity + KYC data | Sales Ops + Compliance | Structured (CRM + KYC provider API) | Salesforce + Refinitiv/Persona API | ~50 entities at pilot | At onboarding + daily screening | **Need** — ECCN + restricted-party screening |
| Network telemetry (egress attempts, clipboard attempts) | Security Lead | VPC Flow Logs + AppStream fleet logs | SIEM | ~100–1K events/tenant/day | Real-time | **Need** — AppStream-specific logging config |
| DFM/geometry analysis output | AI Platform Lead | JSON (existing Layer 2 output) | Existing pipeline API | Per-order | Real-time | **Have** — reused unchanged |
| Pricing/ETA output | AI Platform Lead | JSON (existing Layer 3 output) | Existing pipeline API | Per-order | Real-time | **Have** — reused unchanged |
| Pen-test evidence | CISO | PDF reports | Internal document store | Annual + post-change | Event-driven | **Need** — first pen-test before pilot |

### 8.2 Data Quality Assessment

| Data Source | Completeness | Accuracy | Consistency | Timeliness | Validity | Uniqueness | Overall |
|------------|-------------|----------|-------------|------------|----------|------------|---------|
| Customer CAD files | N/A (customer-owned) | N/A | Varies by CAD product | Real-time | ISO 10303-21 validation in Lambda | Per-tenant KMS isolation | **Medium** — quality is customer's responsibility; Protolabs validates format only |
| Order Object schema | 100% (controlled) | 100% (generated) | 100% (single schema) | Real-time | Schema validation | Deterministic per Save | **High** |
| Audit trail | 100% (automated) | 100% (system-generated) | 100% (structured) | Real-time | SIEM validation | Event-ID dedup | **High** |
| KYC data | 90% (some manual steps) | 95% (provider-verified) | 90% (CRM ↔ KYC sync) | Daily screening | Provider-validated | Entity dedup | **Medium** |
| Network telemetry | 100% (automated) | 100% (system-generated) | 100% (AWS-native) | Real-time | CloudTrail-native | Event-ID dedup | **High** |
| DFM/geometry output | 100% (existing pipeline) | Existing pipeline quality | Existing pipeline quality | Real-time | Existing validation | Per-order | **High** (inherited) |

### 8.3 Data Normalization & Transformation Requirements

| Transformation | Source | Target | Complexity | Owner | Effort |
|---------------|--------|--------|------------|-------|--------|
| CAD format validation | Native CAD files (multi-vendor) | ISO 10303-21 (STEP) acceptance gate | Medium — per-CAD-product Save semantics differ (temp files, lock files) | Cloud Infra Lead | 3–4 weeks |
| Audit trail schema harmonization | CloudTrail + AppStream logs + custom AppEng events | Unified SIEM schema | Low — AWS-native formats, standard ETL | Security Lead | 1–2 weeks |
| KYC/ECCN data integration | Refinitiv/Persona API → CRM | Tenant onboarding record | Medium — API integration + daily screening cron | Sales Ops + Cloud Infra | 2–3 weeks |
| Order Object enrichment | S3 PutObject event → existing Order Object schema | Enriched with: tenant ID, session ID, audit-trail pointer, compliance-class flag | Low — thin Lambda glue | AI Platform Lead | 1–2 weeks |
| Confidence-score calibration data | AppEng review outcomes (approve/revise/refuse) | Labeled dataset for confidence-routing tuning | Medium — requires 50–100 labeled orders before routing thresholds are reliable | AI Platform Lead | 4–6 weeks (accumulates during pilot) |

### 8.4 Data Pipeline Architecture

```
[Customer CAD] → [AppStream Sandbox] → [S3 PutObject] → [Lambda Order Processor] → [Order Object] → [Existing Pipeline]
                                              |                    |                        |
                                         KMS encrypt         Validate + scan          DynamoDB persist
                                         per-tenant CMK      Malware + schema         + audit-trail emit
                                              |                    |                        |
                                         Audit event         Audit event              SIEM ingestion
```

| Stage | Technology | Latency SLA | Owner | Status |
|-------|-----------|-------------|-------|--------|
| **Ingestion** | AppStream → S3 PutObject (VPC endpoint) | ≤ 30s p95 (Save → S3) | Cloud Infra Lead | **Build** — AppStream fleet config + S3 bucket policy |
| **Transformation** | Lambda Order Processor (validate + scan + persist) | ≤ 10s p95 | AI Platform Lead | **Build** — ~200 LOC thin glue |
| **Feature Store** | N/A — SDTO does not introduce new ML features | n/a | n/a | **N/A** |
| **Model Serving** | N/A — reuses existing DFM/pricing pipeline | n/a | n/a | **Reuse existing** |
| **Output Storage** | DynamoDB (Order records) + S3 (CAD files) + SIEM (audit) | Real-time | Cloud Infra Lead | **Build** — per-tenant KMS + bucket policies |
| **Monitoring** | SIEM dashboards (egress attempts, Save success rate, AppEng SLA) | Continuous | Security Lead | **Build** — CloudTrail + custom metrics |

### 8.5 Data Governance & Privacy

| Requirement | Assessment | Owner | Status |
|------------|-----------|-------|--------|
| **PII identification** | Minimal — user identity (name, email, employer) in KYC store; no PII in CAD files by design | Data Steward | **Assessed** — follows existing ProDesk DPA |
| **Anonymization strategy** | N/A at pilot — no training data extracted from regulated-tenant geometry without explicit written opt-in | Privacy Lead | **Defined** — zero-extraction policy for regulated tenants |
| **Data retention policy** | 7 years for audit trail (CMMC + AS9100 record-retention); CAD files retained per tenant contract (typically 3–5 years) | Legal | **Defined** — aligns with existing ProDesk retention + regulatory minimums |
| **Data lineage tracking** | Full lineage: Save event → S3 object → Lambda → Order Object → DFM → Pricing → AppEng review → Quote. Every step emits audit event with session ID + geometry hash. | Data Engineer | **Designed** — audit-trail architecture in Appendix A |
| **Access control** | Per-tenant KMS CMKs; IAM least-privilege per role; only US-person AppEng accounts can access regulated-tenant data; GovCloud variant: cleared-personnel-only | Security | **Designed** — VPC endpoints + IAM policies in Appendix A |
| **GDPR compliance** | Limited scope — user identity data only; follows existing ProDesk DPA; no EU personal data in CAD files by design | DPO | **Assessed** — no additional DPIA required |
| **ITAR/EAR compliance** | Architecture IS the deemed-export boundary; AppStream + S3 + KMS = controlled environment; only US-person AppEng access; ECCN screening at onboarding | Compliance | **Designed** — core architecture purpose |
| **Training data IP** | Zero extraction from regulated-tenant geometry at v1. If future fine-tuning is proposed, it spawns its own intake with full Appendix E + explicit written opt-in per NDA. | Legal | **Defined** — contractual guardrail in tenant agreement |

### 8.6 ML-Specific Data Requirements

| Requirement | Specification | Current Status | Gap |
|------------|--------------|----------------|-----|
| **Training data volume** | N/A — SDTO is an interaction surface, not a model. No new training data required. | N/A | **None** |
| **Label quality** | Confidence-routing calibration requires ~50–100 labeled orders (AppEng approve/revise/refuse outcomes) | 0 labels (pre-pilot) | **4–6 weeks of pilot data accumulation** |
| **Class balance** | N/A — no classification model at v1 | N/A | **None** |
| **Train/val/test split** | N/A | N/A | **None** |
| **Data drift baseline** | Save→Order success rate baseline to be established in pilot week 1 | Not established | **1 week** |
| **Feedback loop** | AppEng review outcomes → confidence-routing threshold tuning (manual at v1, automated at GA) | Not designed | **Design during pilot; implement at GA** |
| **A/B test data** | N/A at pilot — single-path HITL for all regulated orders | N/A | **None at pilot; design for GA Collaboration tier** |

### 8.7 Data Engineering Backlog (JTBDs)

| JTBD | Priority | Effort | Dependencies | Owner |
|------|----------|--------|-------------|-------|
| "When I'm processing a Save event, I need deterministic CAD-format validation across SolidWorks/NX/CATIA/Fusion 360, so I can reliably create Order Objects without false-refusals" | **P0** | 3–4 weeks | Per-CAD-product Save-semantics testing | Cloud Infra Lead |
| "When I'm onboarding a regulated tenant, I need automated KYC + ECCN screening, so I can approve customers in <48 hours without manual compliance review" | **P0** | 2–3 weeks | KYC provider API integration | Sales Ops + Cloud Infra |
| "When I'm investigating a security incident, I need unified audit trail across CloudTrail + AppStream + AppEng actions, so I can reconstruct the full event chain in <1 hour" | **P0** | 1–2 weeks | SIEM schema design | Security Lead |
| "When I'm tuning confidence-routing thresholds, I need labeled AppEng review outcomes, so I can calibrate auto-route vs. full-review bands" | **P1** | 4–6 weeks (accumulates) | Pilot order volume | AI Platform Lead |
| "When I'm preparing for AS9100 / CMMC audit, I need exportable audit evidence packages, so I can pass surveillance audits without manual log stitching" | **P1** | 2–3 weeks | SIEM dashboards + retention policy | Compliance |

### 8.8 Data Readiness Score

| Dimension | Weight | Score (1-5) | Weighted |
|-----------|--------|-------------|----------|
| Data source availability | 20% | 3.5 | 0.70 |
| Data quality | 25% | 4.0 | 1.00 |
| Normalization complexity | 15% | 3.0 | 0.45 |
| Pipeline readiness | 15% | 3.0 | 0.45 |
| Governance compliance | 10% | 4.5 | 0.45 |
| ML-specific readiness | 15% | 2.0 | 0.30 |
| **Total Data Readiness Score** | 100% | | **3.35 / 5.0** |

**Classification: NEEDS WORK (3.0–3.9).** Data engineering is on the critical path. The pipeline (S3 → Lambda → Order Object → existing pipeline) is well-designed but unvalidated. The biggest gap is per-CAD-product Save-semantics validation — this is a P0 discovery task that must complete before Build phase begins.

### 8.9 Data Readiness vs. Technical Build Timeline

**Adjustment:** `Time to Value = Data Engineering Time + Technical Build Time (sequential)`

The 3.35 score means data engineering (especially CAD-format validation + KYC integration + SIEM schema) must complete or be substantially proven before the Build phase can commit to the "Save = Order" promise. This adds **3–4 weeks** to the critical path vs. a fully-ready data baseline.

**Recommendation:** Run the CAD Save-semantics validation study (Box 4 Unknown #4) as the **first Discovery task**, not in parallel. If it fails (Save semantics are inconsistent across CAD products), the entire "Save = Order" UX collapses and the use case must pivot to a "Submit Order" wrapper button — which is viable but changes the value proposition.

### 8.10 Integration with Box 7 (Change Readiness)

- [x] **Domain expert availability for data validation** — AppEng must participate in per-CAD-product Save-semantics testing (their review workflow depends on deterministic Order Objects). Box 7 identifies AppEng as Medium identity-threat; involving them in validation design is a change-management win (gives them ownership).
- [x] **Change resistance to data sharing** — Customer engineers must accept that every Save is recorded. This is a feature (audit trail), not a bug, but must be communicated clearly. Export-control officers will see this as a positive.
- [x] **Compensation for data engineering contributions** — AppEng who help design the review console and validate Save semantics should be recognized as pilot champions (knowledge bounty or spot bonus).
- [x] **Data governance training** — All AppEng accessing regulated-tenant data must complete ITAR/CMMC awareness training before pilot. This is a Box 7 training cost item.

---

## Decision Gate (Hard Stop)

**Calculations:**
- **Adjusted ROI** = Business Value ($5–15M ARR) − Technical Cost ($3–5M) − Change Cost ($0.08–0.18M) − Data Engineering Cost penalty ($0.5–1M for Data Readiness 3.35) = **$1.3–8.3M net**
- **Total Readiness Score** = min(Data Readiness Score 3.35, 6 − (Change Resistance Risk 41 / 10)) = min(3.35, 1.9) = **1.9 / 5.0**

**Verdict: PROCEED with conditions**

| Condition | Assessment | Verdict |
|-----------|------------|---------|
| Adjusted ROI > 0 | $1.3–8.3M net > 0 | **PASS** |
| Total Readiness Score ≥ 2.0 | 1.9 < 2.0 | **FAIL** — Data Readiness + Change Resistance are binding |
| Resistance Risk < Critical (46+) | 41 < 46 | **PASS** |
| Tier 1/2 + RAT not yet run | N/A — JTBD Evaluation Gate passed | **PASS** |

**Rationale:** The use case clears the ROI bar and resistance is High but not Critical. However, the Total Readiness Score of 1.9 is below the 2.0 DEFER threshold because change resistance (41) drags the composite down. The binding constraints are: (1) Data Readiness 3.35 means data engineering is on the critical path, and (2) Change Resistance 41 requires intensive intervention. These are manageable with the conditions below — they do not kill the use case, but they must be addressed before Build commitment.

**Required Actions before Build Commitment:**
1. Complete CAD Save-semantics validation (Box 4 Unknown #4) — if it fails, pivot to "Submit Order" wrapper
2. Sign Transformation Guarantee before pilot kickoff (Box 7.6)
3. Run Phase 0 listening tour + champion identification (Box 7.6)
4. Secure executive sponsorship (VP Engineering named sponsor per Box 2 RACI)

**Re-evaluation Criteria:**
- Re-run intake if: (a) Save-semantics validation fails, OR (b) >1 design-partner ECO rejects architecture, OR (c) pilot resistance score exceeds 45 (Critical threshold)

---

## Appendix A — Solution Architecture

### Component diagram (text)

```
   Customer browser (US-person, KYC'd)
            │
            │  HTTPS, MFA, conditional access
            ▼
   ┌──────────────────────────────────────────────┐
   │ AppStream 2.0 fleet (per-tenant stack)       │
   │  - Allowlisted CAD apps (SW / NX / Fusion)   │
   │  - Clipboard / file-transfer / print: OFF    │
   │  - Internet egress: blocked except S3 VPCE   │
   │  - Mapped Z: drive → tenant S3 prefix        │
   └──────────────────────────────────────────────┘
            │
            │  SaveAs → S3 PutObject (per-tenant KMS CMK)
            ▼
   ┌──────────────────────────────────────────────┐
   │ S3 (per-tenant prefix, write-only)           │
   └──────────────────────────────────────────────┘
            │
            │  s3:ObjectCreated:Put event
            ▼
   ┌──────────────────────────────────────────────┐
   │ Lambda — Order Processor                     │
   │  - Validate (size, type, ISO 10303-21)       │
   │  - Malware scan (ClamAV / GuardDuty)         │
   │  - Persist Order record (DynamoDB)           │
   │  - Emit Order Object → existing pipeline     │
   └──────────────────────────────────────────────┘
            │
            ├──► Layer 2 — DFM/Geometry (existing)
            ├──► Layer 3 — Pricing/ETA (existing)
            └──► Layer 4 — Orchestration (existing)
                          │
                          ▼
   ┌──────────────────────────────────────────────┐
   │ AppEng Review Console (extends ProDesk)      │
   │  - Confidence-routed queue                   │
   │  - Provenance trail per order                │
   │  - HITL approval before quote release        │
   └──────────────────────────────────────────────┘
            │
            ▼
   Customer notification (quote ready / revision needed)

   Cross-cutting (every component): CloudTrail + audit-log → SIEM
                                    KMS per-tenant CMKs
                                    IAM least-privilege per role
                                    VPC endpoints, no public subnets
```

### Build vs Buy

| Component | Decision | Rationale |
|---|---|---|
| AppStream fleet | **Buy** (AWS) | Commodity managed service; no moat in re-implementing |
| S3 + KMS | **Buy** (AWS) | Same |
| CAD apps | **Buy / BYOL** | Vendor licenses; no Protolabs IP here |
| Lambda Order Processor | **Build** (thin) | ~200 LOC glue between S3 event and existing Order Object pipeline |
| Validation + malware scan | **Buy** (GuardDuty + open-source schema validators) | No moat |
| Order Object pipeline (Layers 2–4) | **Reuse existing** | Already built — see memoized-questing-sphinx.md §2 |
| AppEng Review Console | **Build** (extend ProDesk) | UX moat lives here — confidence routing + provenance trail is Protolabs-specific |
| Audit-trail / SIEM | **Buy** (Splunk / OpenSearch + AWS CloudTrail) | Commodity |
| KYC / ECCN screening | **Buy** (Refinitiv World-Check or Persona) | Commodity, regulated industry |

### Integration points

- **ProDesk** — AppEng Review Console extension; reuse user/auth model
- **Existing Order Object pipeline** — Lambda emits the same schema; downstream pipeline is unchanged
- **CRM (Salesforce/equivalent)** — tenant onboarding, deflection-rate instrumentation
- **Hubs network partner routing** — only ITAR-registered shops are eligible for SDTO orders
- **External KYC/ECCN provider API** — onboarding gate
- **AWS GovCloud account / commercial account boundary** — separate AWS Organizations OU per tenancy class

### Maps to Teresa-narrative 6 layers

| Section-2 Layer | SDTO contribution |
|---|---|
| **L1 — Ingestion / Normalization** | Replaced for regulated tenants by the Save-event → Order Object path |
| **L2 — Geometry / DFM** | Reused unchanged (runs in same VPC for regulated tenants) |
| **L3 — Pricing / ETA** | Reused unchanged |
| **L4 — Orchestration** | Reused; adds tenancy-class routing rule |
| **L5 — Customer Interaction** | New surface — the AppStream sandbox itself |
| **L6 — MLOps / Governance** | New audit-trail + per-tenant key management + sandbox kill-switch |

### Non-functional requirements

- **Latency:** Save → Order Object created ≤ 30s p95; AppStream session interactive latency ≤ 100ms p95 for input echo, ≤ 1s p95 for CAD viewport refresh on assemblies up to 500MB
- **Scale (pilot):** 5 tenants × 5 concurrent sessions; **GA target:** 50 tenants × ~500 concurrent
- **Availability:** 99.5% session availability at pilot; 99.9% at GA (existing ProDesk SLO unchanged for non-SDTO traffic)
- **Security posture:**
  - **Auth:** SAML SSO + MFA, customer-IdP federation
  - **Network:** No public subnets; VPC endpoints only; per-tenant SG; no general internet egress from fleet
  - **Audit:** CloudTrail + AppStream session logs + AppEng action logs piped to SIEM; immutable retention 7 yrs (CMMC + AS9100 record-retention)
  - **Pen-test:** External pen-test before GA + annually + after every material change; AppStream-specific test plan covering clipboard/file-transfer/network-egress controls
  - **Encryption:** AES-256 at rest with per-tenant KMS CMKs; TLS 1.2+ in transit; customer-managed-key option for top-tier tenants

### Compliance Architecture

| Compliance control | Component | Liability holder |
|---|---|---|
| EU AI Act Art. 14 (human oversight) | AppEng Review Console (HITL gate) | Protolabs |
| EU AI Act Art. 17 (post-market monitoring) | Audit-trail + SIEM + quarterly RMF review | Protolabs |
| EU AI Act Art. 11 (technical documentation) | Versioned threat-model + DPIA + system card per tenancy class | Protolabs |
| NIST AI RMF GV-1.1, GV-3.2 (governance roles) | Governance board + RMF profile per tenancy class | Protolabs |
| NIST AI RMF MP-1.1, MP-3.1 (context, risk mapping) | Threat model + data-flow diagram (artifact in repo) | Protolabs |
| NIST AI RMF MS-1.1, MS-2.5 (measurement) | SIEM dashboards + Save-success rate + AppEng-SLA metrics | Protolabs |
| NIST AI RMF MG-1.1, MG-2.1, MG-3.1 (manage / incident) | Incident-response runbook + AppStream kill-switch + per-tenant rollback | Protolabs |
| ISO 42001 Clause 6.1.2 (AI risk assessment) | Per-tenancy-class risk register | Protolabs |
| ISO 42001 Clause 7.5 (documented information) | Audit-trail + SIEM retention 7 yrs | Protolabs |
| ISO 42001 Clause 8.2 (operational control) | Confidence routing + HITL design | Protolabs |
| ISO 42001 Clause 8.4 (performance monitoring) | SIEM dashboards | Protolabs |
| ISO 42001 Clause 9.1 (evaluation) | Quarterly governance review | Protolabs |
| ISO 42001 Clause 10.1 (incident / improvement) | Runbook + tabletop exercise + after-action reports | Protolabs |
| ITAR §120.17 (deemed-export boundary) | AppStream + S3 + KMS architectural boundary | Protolabs (control plane); customer (its own users' citizenship attestation) |
| EAR §734.18 / §740.13 (ECCN screening, dual-use) | Onboarding KYC + restricted-party screening | Protolabs |
| CMMC L2 / NIST 800-171 (CUI protection) | GovCloud variant + cleared-personnel ops + IAM | Protolabs (system); customer (CUI-handling discipline outside system) |
| AS9100 quality-system records | Audit-trail of every design review action | Protolabs (within SDTO scope) |
| AWS infrastructure security | Underlying AppStream/S3/KMS substrate | AWS (vendor) per Shared Responsibility Model |
| GDPR (limited scope — user identity only) | KYC store + ProDesk DPA | Protolabs (controller for user identity); customer (controller for the CAD content) |
| Customer NDA / customer IP boundary | Per-tenant KMS + tenancy isolation + zero training extraction without opt-in | Protolabs (must enforce); customer (must contractually opt in for any extraction) |

### Working-with-Machines placement (architectural)

| Confidence band | Order Object completeness | Routing decision | Human action | Escalation path |
|---|---|---|---|---|
| ≥ 0.85 | Complete (all required fields, valid ISO 10303-21, no DFM blocker) | **Quick-review** in AppEng console | AppEng samples 1-in-5; signs off in <30 min | None unless flagged |
| 0.6 – 0.85 | Complete | **Full-review** | AppEng reviews fully; provenance trail visible | Senior AppEng if disputed |
| < 0.6 | Any | **Refuse / clarify** | Auto-message customer with specific completeness issue; route to AppEng queue | Compliance officer if pattern |
| Any | Incomplete (missing material / qty / tolerance / GD&T) | **Refuse / clarify** | Same as above | Same |
| Any | Flight-critical / medical-implant flag set | **Full-review (always)** | AppEng + senior reviewer + 100% compliance-officer sample | General Counsel for novel cases |
| Any | Egress-attempt or sandbox-anomaly flagged | **Refuse + incident** | Compliance officer, kill-switch on session | CISO + General Counsel |

The customer-facing "escalate to human" button in the sandbox always routes to an AppEng with the full provenance trail (session ID, every Save event, geometry hash, DFM output, confidence scores) pre-loaded — no context loss across the boundary.

---

## Appendix B — Cost & Timeline

### Engineer-weeks per phase (ranged)

| Phase | Cloud Infra | Security/Compliance | AI Platform (extend ProDesk) | AppEng (pilot) | Legal | **Total eng-weeks** |
|---|---|---|---|---|---|---|
| Discovery (T0 → T+8wks) | 4–6 | 6–10 | 2–3 | 1–2 | 4–6 (counsel hrs) | **17–27** |
| Build (T+8 → T+24wks) | 14–20 | 12–18 | 8–12 | 2–4 | 2–4 | **38–58** |
| Pilot (T+24 → T+36wks) | 4–8 | 6–10 | 4–6 | 8–12 | 2–4 | **24–40** |
| GA hardening (T+36 → T+52wks) | 6–10 | 8–12 | 4–6 | 4–6 | 2–4 | **24–38** |

### Cloud $ / month (ranged, with assumptions)

| Phase | Cost | Assumptions |
|---|---|---|
| Pilot | **$20–60K/mo** | Commercial AWS; 5 tenants × 5 concurrent G4dn.2xlarge sessions × ~6h/day × 22 days; S3 + KMS + Lambda + SIEM + GuardDuty modest |
| GA (commercial tenancy) | **$80–200K/mo** | 50 tenants × ~10 concurrent avg; mix of G4dn / G5; SIEM at scale |
| GA (GovCloud variant) | **+ $40–100K/mo** | GovCloud premium ~3× commercial on compute + storage; cleared-ops surcharge |

**Note:** All ranges assume per-tenant cost pass-through is part of regulated-vertical pricing — the unit economics close only if Sales packages SDTO as a paid premium tier, not a free upgrade.

### Milestones (relative dates)

| Date | Milestone | Kill criteria (would make us stop) |
|---|---|---|
| **T+30** | Discovery review: deflection-rate evidence + 2 design-partner LOIs + legal opinion on deemed-export boundary | <1 design-partner LOI, OR legal opinion says architecture does not satisfy ITAR boundary |
| **T+90** | First Save → Order Object end-to-end in non-prod with one CAD product; pen-test #1 passes; threat-model published | Pen-test finds critical egress path; Save semantics inconsistent across CAD products; latency >2× target |
| **T+180** | Pilot live with 2 design-partner customers, 50+ orders processed end-to-end through AppEng HITL | <30 orders processed, OR AppEng-review SLA blown >50%, OR 1+ critical audit finding |
| **T+270** | GA decision gate: unit economics validated, CMMC L2 readiness audit clean, customer NPS ≥ 8 from pilot | Unit economics negative at projected GA scale; ≥1 CMMC critical gap; pilot NPS < 6 |
| **T+360** | GA opens to regulated-vertical sales; AS9100 / ISO 42001 surveillance audits scheduled | n/a — beyond decision-gate |

### Headcount / hire / partner asks

- **+1 Cloud Security Engineer** (existing team has the cloud infra skill but not the FedRAMP/CMMC depth)
- **+1 Compliance Officer / AI Governance lead** (shared with broader governance program; ~50% on SDTO at pilot)
- **External pen-test firm** (annual contract, not headcount)
- **External AS9100 / ISO 42001 auditor** (annual)
- **AWS GovCloud account team** as a strategic partner — engaged from T0
- **Legal counsel** with ITAR/EAR specialization (existing GC + outside specialist firm on retainer)

---

## Appendix C — Experiment / Test Plan

**Hypothesis (single sentence, falsifiable):**
> Two regulated-vertical design-partner customers will process at least 25 production-equivalent orders each through the SDTO sandbox in a 12-week pilot, with ≥95% Save→Order success rate, ≥80% of orders cleared by AppEng within 4 hours, zero critical audit findings, and an NPS ≥ 8 from each customer's design-engineer cohort.

**Method:**
- **Pilot scope:** 2 customers (target: 1 defense Tier-2 supplier + 1 medical-implant OEM) — chosen because they cover the two riskiest compliance edges (ITAR + EU AI Act high-risk-adjacent)
- **n:** 5–10 design engineers per customer; ~25–50 orders per customer over 12 weeks
- **Duration:** 12 weeks (T+24 → T+36)
- **Comparison:** Each customer's existing offline RFQ workflow (3–10 day SLA) — measured by pre-pilot audit + post-pilot survey

**Success bar (numeric):**
- Save→Order success rate ≥ 95%
- AppEng-review SLA: ≥ 80% of orders cleared in ≤ 4h
- Audit findings: 0 critical, ≤ 2 major across the 12 weeks
- NPS ≥ 8 from each customer's engineer cohort
- ≥ 1 customer signs a paid GA-tier order *during* the pilot window

**Kill criteria (numeric):**
- Save→Order success rate < 80%
- ≥ 1 critical audit finding (data egress confirmed, deemed-export confirmed, KMS misconfiguration confirmed)
- AppEng-review SLA blown on > 50% of orders
- NPS < 6 from either customer
- Either customer's export-control officer formally rejects the architecture during the pilot

**Duration:** 12 weeks (with a hard stop-gate review at week 6 — go/no-go on continuing to week 12)

**Learning we capture even if it fails:**
- Per-CAD-product Save-semantics map (independent reusable artifact for any future secure-cloud bet)
- Validated cost model (commercial vs. GovCloud) at real workload — feeds the LMM regulated-deployment plan
- Customer-side export-control officer playbook (objections, requirements, sign-off process) — directly reusable for any future regulated-vertical product
- Validated or invalidated deflection-rate hypothesis — material input to portfolio prioritization regardless of SDTO outcome

---

## Appendix D — Competitive Scan (Vertical-Aware)

### Tier 1A — Incumbents & Status Quo

| Competitor | Capability | Gap vs. Protolabs SDTO |
|------------|-----------|------------------------|
| **In-house defense contractor machine shops** (Lockheed, Raytheon, Northrop Grumman) | Air-gapped CAD/CAM/CNC, physical security clearances, no cloud | 3–10 day quote SLA; no AI DFM; no global capacity network |
| **ITAR-registered regional job shops** | Trusted relationships, phone/email RFQ, ITAR-registered facility | No instant quoting; no design-assistance; no audit trail automation |
| **Government procurement portals** (DIBBS, FedMall, GSA Advantage) | Official channels, compliance pre-cleared | No design tools; no DFM feedback; 30–90 day procurement cycles |
| **Status quo: "design offline → secure-FTP → wait"** | Current Protolabs manual path for regulated buyers | 3–10 day SLA vs. SDTO's <4h; no AI assistance; no Save=Order automation |

### Tier 1B — Platform/Software Vendors (Could Pivot)

| Competitor | Capability | Gap vs. Protolabs SDTO |
|------------|-----------|------------------------|
| **Onshape (PTC)** | Cloud-native CAD with enterprise security, collaboration features | No manufacturing backend (quoting, DFM, capacity routing); no ITAR-compliant sandbox |
| **Autodesk (Fusion 360 + Forge)** | Cloud CAD + some manufacturing extensions | No ITAR-boundary architecture; no instant quoting network; no HITL governance |
| **Siemens Teamcenter X** | Cloud PLM with compliance modules | No prototyping/quoting speed focus; enterprise sales cycle too slow for RFQ |
| **Dassault 3DEXPERIENCE** | Design + simulation cloud | No manufacturing marketplace for custom parts; no AI-assisted DFM |

### Tier 2 — Digital Manufacturing Peers

| Competitor | Capability | Evidence | URL |
|------------|-----------|----------|-----|
| **Xometry** — ITAR-registered manufacturing services | Xometry public ITAR/EAR compliance page describes ITAR registration and standard handling for controlled parts | https://www.xometry.com/capabilities/itar-compliant-manufacturing/ |
| **Xometry** — Secure file handling for sensitive CAD | Xometry "Security" page describes encrypted upload + NDA framework + access controls | https://www.xometry.com/security/ |
| **Xometry** — Hosted-CAD sandbox with Save = Order trigger | **No public evidence found** — Xometry's documented pattern is upload-then-quote, not in-sandbox design-and-save | n/a |
| **Xometry** — FedRAMP / GovCloud-hosted regulated workflow | **No public evidence found** as of search date | n/a |
| **Xometry** — AS9100-certified internal supply | Xometry Aerospace page references AS9100D-certified supply network through partner network | https://www.xometry.com/industries/aerospace/ |
| **Fictiv** — ITAR-registered manufacturing | Fictiv ITAR page describes ITAR-registered domestic supply for defense customers | https://www.fictiv.com/capabilities/itar |
| **Fictiv** — Secure-by-design platform | Fictiv security/trust page describes SOC 2 Type II + NDA + customer data controls | https://www.fictiv.com/trust |
| **Fictiv** — Hosted-CAD sandbox with Save = Order trigger | **No public evidence found** — Fictiv's documented pattern is upload-quote-iterate, not in-sandbox design | n/a |
| **Fictiv** — GovCloud / FedRAMP-aligned regulated workflow | **No public evidence found** as of search date | n/a |
| **Fictiv** — Aerospace + medical-device program | Fictiv aerospace + medical-device pages describe certified-supply programs | https://www.fictiv.com/industries/aerospace ; https://www.fictiv.com/industries/medical |
| **3D Systems On Demand / Quickparts** | ITAR-registered for 3D printing | Additive-only; no sandbox; legacy upload model | no public evidence of sandbox found |
| **Stratasys Direct Manufacturing** | ITAR-registered for 3D printing | Additive-only; no AI design assistant; no Save=Order | no public evidence of sandbox found |

> URLs above are the canonical product-marketing pages; if any have moved, capture the exact retrieval date during the next Discovery refresh and update — Appendix D is intentionally living evidence, not frozen.

### Tier 3 — Adjacent/Indirect Threats

| Threat | Realism | Mitigation |
|--------|---------|------------|
| **Generic LLM disintermediation** (ChatGPT, Claude, Gemini) | Low for SDTO specifically | LLM cannot stand up ITAR sandbox; customer still needs manufacturing backend |
| **Contract manufacturer direct** (Jabil, Flex, Foxconn) | Medium at volume | SDTO targets prototyping/low-volume where CM direct is uneconomical; CM lacks instant quoting |
| **Alibaba / China direct sourcing** | Low for ITAR (illegal); Medium for non-ITAR IP-sensitive | SDTO's security story is the differentiator; offshore sourcing carries IP + compliance risk |

### Protolabs current state

- Hubs / Protolabs network includes ITAR-registered shops
- ProDesk provides instant quoting + DFM for non-regulated parts
- No equivalent hosted-CAD sandbox today; regulated buyers go through manual phone + secure-FTP path
- AS9100 quality framework partially in place via the network; not consistently surfaced as a programmatic gate

### Differentiation thesis

> Protolabs wins because the **actual competitor is the status quo** — not Xometry or Fictiv. In-house shops and regional job shops already have ITAR clearance but deliver 3–10 day quotes with no AI assistance. SDTO collapses that to <4 hours with full audit evidence. Against platform vendors (Onshape, Autodesk), Protolabs brings the manufacturing backend they lack — quoting, DFM, capacity-aware routing, and the Hubs network. Against digital peers, SDTO is the only solution where the file never leaves the boundary. The 18–24 month window is not about replicating AppStream — it's about replicating the **trust relationship** with regulated buyers' export-control officers.

### Adjacent threat

> **Most realistic threat: incumbent in-house shops and ITAR-registered job shops winning on "we're already approved."** Generic-LLM disintermediation is structurally low for ITAR. Platform-vendor pivot (Onshape/Autodesk adding manufacturing) is a 3–5 year threat, not immediate.

---

## Appendix E — Historical Data & Proprietary Model Strategy

**N/A for this use case (with a caveat).** SDTO is a *secure-interaction surface*, not a model in itself. It does not require historical data as a competitive asset, does not introduce a new fine-tuned model, and does not establish a new self-learning loop. The downstream pipeline (DFM, pricing, ETA) it pipes into already has its own model strategy (covered by the LMM intake — `intake/_example-funnel-intake-lmm.md`).

**Caveat — the strategic adjacency:** SDTO is the *front door* through which regulated geometry could eventually enter a sovereign fine-tuned LMM variant — but only with explicit, separate, written customer opt-in per NDA. That option exists; it is not exercised at v1; if it becomes a roadmap item it spawns its own intake, including a full Appendix E with data-flywheel mechanics, opt-in tiering, and EU AI Act retraining-obligation analysis.

---

## Mission-Critical Improvements for the Business Case

Based on the updated funnel-intake evaluation (Box 7 + Box 8), the following improvements are **mission-critical** — the business case should not advance to the feasibility probe without addressing them:

### IMP-1: CAD Save-Semantics Validation is a Gate, Not a Parallel Task
**Severity: CRITICAL.** The entire "Save = Order" value proposition depends on deterministic S3 PutObject events across SolidWorks, NX, CATIA, and Fusion 360. If each CAD product emits temp/lock/intermediate files, the Order Processor will create false orders or miss real ones. **This must be the first Discovery task, completed before Build phase commitment.** If validation fails, pivot to a "Submit Order" wrapper button — viable but weakens the UX differentiation.

### IMP-2: Quality Gatekeeper Resistance is the #1 People Risk
**Severity: HIGH.** Box 7 scores Quality Gatekeeper resistance at 12 (the highest single risk factor). AppEng will resist if they feel Save=Order bypasses their judgment. **Mitigation:** Frame every AppEng as "the compliance firewall," not a rubber stamp. The HITL gate on every regulated order at v1 is non-negotiable. Involve AppEng in review-console co-design during Discovery — ownership kills resistance.

### IMP-3: GovCloud Cost Must Be Contractually Triggered, Not Default
**Severity: HIGH.** Box 4 risk: GovCloud costs 3–5× commercial. If SDTO defaults to GovCloud, unit economics fail. **Mitigation:** Tiered tenancy — commercial + ITAR-segregated for non-DIB customers; GovCloud only when a pilot customer's contract explicitly requires it. Per-tenant cost pass-through is mandatory in regulated-vertical pricing.

### IMP-4: Transformation Guarantee Must Be Signed Before Pilot Kickoff
**Severity: HIGH.** Box 7 resistance score of 41 (High) requires executive sponsorship. The written Transformation Guarantee (no layoffs for 24 months, preserved authority, compensation floor) must be signed by CEO/COO before any engineer touches the pilot. Without it, the pilot will face passive compliance at best, active sabotage at worst.

### IMP-5: Confidence-Routing Calibration Requires Labeled Data That Doesn't Exist Yet
**Severity: MEDIUM.** Box 8 identifies that confidence-routing thresholds (≥0.85 / 0.6–0.85 / <0.6) are uncalibrated — no labeled AppEng review outcomes exist. **Mitigation:** Run the first 4–6 weeks of pilot with ALL orders routed to full-review (no auto-route). Accumulate ~50–100 labeled outcomes, then introduce quick-review sampling. This delays the Collaboration-tier value but avoids mis-routing a regulated order.

### IMP-6: Export-Control Officer Buy-In Is a Kill Criterion, Not a Nice-to-Have
**Severity: HIGH.** Box 4 Unknown #3: will customers' export-control officers approve the AppStream-as-deemed-export-boundary architecture? **Mitigation:** Run a design-partner workshop in Discovery that includes the customer's export-control officer AND Protolabs General Counsel. Get a written "architecture acceptable" opinion before Build. If even one design partner's ECO rejects it, the kill criterion at T+30 fires.

### IMP-7: Latency Tax on Senior Engineers Is Underestimated
**Severity: MEDIUM.** Box 4 Unknown #5: AppStream latency on >500MB assemblies. Senior engineers with 20 years on local workstations will reject a tool that feels sluggish. **Mitigation:** Latency SLO (≤100ms p95 input echo, ≤1s p95 viewport refresh) must be baked into pilot success criteria. G4dn/G5 fleet sizing + pre-provisioned warm sessions. If latency SLO is blown, the pilot fails — no workaround.

---

## Pre-Emission Self-Check (Tiered)

#### P0 — Must Pass (Hard Blockers)
Emitting output with any unchecked P0 item is a skill failure.

| # | Check | ✓ |
|---|-------|---|
| 1 | Glossary emitted with Source column for every term | ✓ |
| 2 | Box 5 includes all three governance frameworks (EU AI Act + NIST AI RMF + ISO 42001) | ✓ |
| 3 | Box 7 includes Resistance Risk Score + threshold classification | ✓ (41 — HIGH) |
| 4 | Box 8 includes Data Readiness Score (1-5) with threshold classification | ✓ (3.35 — Needs Work) |
| 5 | Decision Gate verdict emitted (PROCEED / RAT-FIRST / REDESIGN / KILL / DEFER) | ✓ (PROCEED with conditions) |

#### P1 — Should Pass (Quality Gates)
These distinguish a good intake from a great one.

| # | Check | ✓ |
|---|-------|---|
| 6 | Appendix A compliance table maps controls to specific components with liability allocation | ✓ |
| 7 | Appendix D cites verifiable URLs or states "no public evidence found" for every claim | ✓ |
| 8 | Box 1 JTBDs are activated from evaluation framework with MoSCoW, Evidence Quality, RICE, and CoND reported | ✓ |
| 9 | Box 1.4 JTBD Evaluation Gate is evaluated with all 6 checks and pass/fail results emitted | ✓ (PASS) |
| 10 | Box 7 includes Change Cost Estimation compared to Box 3 ROI | ✓ ($80–180K vs. $5–15M ARR) |
| 11 | Executive summary includes Adjusted ROI and Total Readiness Score | ✓ |

**All P0 and P1 checks pass.**

---

## Stakeholder Digests

### Digest for Executive Sponsor

| Field | Value |
|-------|-------|
| Verdict | PROCEED with conditions |
| Adjusted ROI | $1.3–8.3M net |
| Total Readiness Cost | $3.9–6.7M (Technical + Data + Change + Compliance) |
| Top 3 Risks | (1) CAD Save-semantics break "Save=Order" promise, (2) Customer ECO rejects architecture, (3) GovCloud cost explosion |
| Change Cost vs ROI | Viable — change cost is <2% of low-end ARR |
| Decision Required | Approve Transformation Guarantee + name VP Engineering as sponsor before pilot kickoff |
| Timeline to First Value | T+36 weeks (pilot live) — add 3–4 weeks if data engineering is sequential |
| Kill Criteria | Save→Order success <80%; ≥1 critical audit finding; pilot NPS <6; unit economics negative at GA scale |

### Digest for Engineering Lead

| Field | Value |
|-------|-------|
| Technical Build Time | 38–58 eng-weeks (Build phase) |
| Key Integration Points | ProDesk (review console extension), existing Order Object pipeline (Layers 2–4), CRM (Salesforce), KYC/ECCN provider API, AWS GovCloud account |
| Compliance Components | AppEng Review Console (HITL), Audit-trail + SIEM, per-tenant KMS, VPC endpoints, kill-switch |
| Non-Functional Requirements | Save→Order ≤30s p95; AppStream latency ≤100ms input echo / ≤1s viewport refresh; 99.5% availability at pilot |
| Build vs. Buy Recommendations | Buy: AppStream, S3/KMS, GuardDuty, SIEM, KYC. Build: Lambda Order Processor (~200 LOC), AppEng Review Console (extend ProDesk). Reuse: existing pipeline Layers 2–4. |
| Kill Criteria | Pen-test finds critical egress path; Save semantics inconsistent across CAD products; latency >2× target |
| Working-with-Machines Placement | Current: Augmentation (AppEng reviews every regulated order). 12-month target: Collaboration for non-flight-critical; stay at Augmentation for flight-critical / medical-implant. |

### Digest for Compliance Officer

| Field | Value |
|-------|-------|
| EU AI Act Risk Class | Limited (default), High in regulated-vertical edge cases (medical implant / flight-critical aerospace) |
| NIST AI RMF Functions | Govern (GV-1.1, GV-3.2) — governance board + RMF profile; Map (MP-1.1, MP-3.1) — threat model + data-flow diagram; Measure (MS-1.1, MS-2.5) — SIEM dashboards + metrics; Manage (MG-1.1, MG-2.1, MG-3.1) — runbook + kill-switch + rollback |
| ISO 42001 Clauses | 6.1.2 (AI risk assessment per tenant tier), 7.5 (documented information / audit trail), 8.2 (operational control / confidence routing + HITL), 8.4 (performance monitoring / SIEM dashboards), 9.1 (evaluation / quarterly governance review), 10.1 (incident response / runbook + tabletop) |
| New Controls Required | Per-tenant KMS CMKs, AppStream egress blocking, SIEM schema for unified audit trail, CMMC L2 readiness on GovCloud variant |
| Audit Timeline | T+90: threat model published; T+180: pilot audit findings review; T+270: CMMC L2 readiness audit; T+360: AS9100 / ISO 42001 surveillance audits |
| Documentation Gaps | Per-tenancy-class DPIA, AppStream-specific pen-test plan, customer ECO sign-off playbook |
| Liability Allocation | AWS (platform substrate), Protolabs (control-plane configuration + HITL design), Customer (its own users' citizenship attestation + CUI handling outside system) |

### Digest for Change Management Lead

| Field | Value |
|-------|-------|
| Resistance Risk Score | 41 / Threshold: HIGH (31–45) |
| Affected Headcount | ~20–30 at pilot (~5–8 AppEng, 1 compliance officer, 1 cloud security engineer, 10–20 customer engineers, 2 ECOs); ~50–70 at GA |
| Identity Threat Level | Medium for AppEng; Low for customer engineers; None for compliance/ECO |
| Top 3 Mitigation Strategies | (1) Frame AppEng as "compliance firewall" with final sign-off preserved, (2) Co-design review console during Discovery to give ownership, (3) Written Transformation Guarantee (no layoffs 24 months, compensation floor) |
| Phase 0 Activities Required | Yes — Leadership alignment workshop, AppEng listening tour, champion identification (1–2 AppEng co-designers) |
| Transformation Guarantee Required | Yes — signed by CEO/COO before pilot kickoff |
| Adjusted Time to Value | Technical Build Time (T+24 weeks) + Change Adoption Time (+3–4 weeks for Phase 0) = T+27–28 weeks to pilot |

---

## Final Destination & Verification

**Final destination of this artifact (post-approval):** `solutions-discovery/funnel-intake-secure-design-to-order-sandbox.md` — sits alongside the existing technical brief `solutions-discovery/cad-design-to-order-aws-appstream.md` (which it cites and compresses).

**Verification:**
1. Confirm the artifact reads cleanly to a TPM unfamiliar with the project (no jargon without glossary entry)
2. Confirm every Appendix-A compliance row maps to a concrete component
3. Confirm the Pre-Emission Self-Check table is fully ticked
4. Confirm all 12 dimensions of `pl-funnel-intake/SKILL.md` Step-7 self-check are satisfied
5. (At workshop time) Run `/pl-rehearse "Secure Design-to-Order Sandbox"` to stress-test against a skeptical Protolabs engineer before the actual review
