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

## Live Canvas (Layer 1) — for transcribing to printed canvas

### Box 1 — Problem & JTBD

**Current-state pain (quantified where possible):**
- Regulated buyers (defense, aerospace, medical-implant, IP-sensitive industrial) currently cannot use Protolabs' self-serve quoting flow because uploading a STEP file to a non-compliant cloud is a deemed-export event under ITAR §120.17 and a CMMC-violation under DFARS 252.204-7012.
- Inferred deflection rate: a meaningful share of regulated RFQs (estimate 10–20% of inbound from these verticals) is lost to CMs with classified networks before Protolabs ever sees the file. Exact number is an Unknown — see Box 4.
- Manual workaround today: phone + secure-FTP + offline DFM = 3–10 day quote SLA vs. ProDesk's <1 hour, eroding the speed-and-certainty promise on exactly the customers with the highest gross margin.

**JTBDs (When I'm X doing Y, I want Z, so I can W):**
1. *(Top JTBD)* When I'm a defense-prime buyer doing routine prototype sourcing, I want to share controlled CAD with Protolabs without my export-control officer having to issue a TAA, so I can get a quote in minutes and stay inside an order pipeline I trust.
2. When I'm an aerospace design engineer iterating on a part, I want my "Save" inside CAD to be the order action, so I never produce a copy of the file on my laptop and never have to re-justify export-control compliance to legal for each upload.
3. When I'm a Protolabs applications engineer, I want to review controlled customer geometry inside an audited workspace with full provenance, so my review action itself is evidence for an AS9100 / ITAR / CMMC audit.

**Top JTBD ranked with rationale:** #1 wins because it removes the single largest friction in the regulated-vertical sales motion (the export-control review per upload). #2 and #3 are downstream UX wins that follow once #1 is solved.

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

## Pre-Emission Self-Check

| # | Check | ✓ |
|---|---|---|
| 1 | Glossary has `Source` column with file path or "inferred" for every term | ✓ |
| 2 | Glossary has intro/outro framing text per glossary-procedure.md | ✓ |
| 3 | Box 5 includes all three governance frameworks (EU AI Act + NIST AI RMF + ISO 42001) | ✓ |
| 4 | Box 5 includes Working-with-Machines placement with autonomy level + 12-month target + HITL design | ✓ |
| 5 | Appendix A compliance table maps controls to specific components | ✓ |
| 6 | Appendix A compliance table includes ISO 42001 clause-level mapping (not just "lifecycle management") | ✓ (clauses 6.1.2, 7.5, 8.2, 8.4, 9.1, 10.1) |
| 7 | Appendix A compliance table includes liability allocation per component (vendor / Protolabs / customer) | ✓ |
| 8 | Appendix A includes Working-with-Machines sub-section with confidence-routing thresholds (numeric) | ✓ (≥0.85 / 0.6–0.85 / <0.6) |
| 9 | Appendix A non-functional reqs include security posture detail (auth, network, audit, pen-test) | ✓ |
| 10 | Appendix D covers all activated tiers (1A/1B/2/3) with verifiable URLs or explicit "no public evidence found" for every claim | ✓ |
| 11 | Portfolio tier cites memoized-questing-sphinx.md §7–8 explicitly | ✓ (Tier 1 — frontmatter + reuses §7 substrate logic) |
| 12 | All four strategic dimensions surfaced: Working-with-Machines, Governance, Market Competition, Legal & Compliance | ✓ |

---

## Final Destination & Verification

**Final destination of this artifact (post-approval):** `solutions-discovery/funnel-intake-secure-design-to-order-sandbox.md` — sits alongside the existing technical brief `solutions-discovery/cad-design-to-order-aws-appstream.md` (which it cites and compresses).

**Verification:**
1. Confirm the artifact reads cleanly to a TPM unfamiliar with the project (no jargon without glossary entry)
2. Confirm every Appendix-A compliance row maps to a concrete component
3. Confirm the Pre-Emission Self-Check table is fully ticked
4. Confirm all 12 dimensions of `pl-funnel-intake/SKILL.md` Step-7 self-check are satisfied
5. (At workshop time) Run `/pl-rehearse "Secure Design-to-Order Sandbox"` to stress-test against a skeptical Protolabs engineer before the actual review
