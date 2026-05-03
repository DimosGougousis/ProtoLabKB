# Implementation Plan: `pl-funnel-intake` Skill Enhancements

> **Plan Date:** 2026-05-03
> **Target Files:**
> - `~/.claude/skills/pl-funnel-intake/SKILL.md` (v1.2.0 → v1.3.0)
> - `~/.claude/skills/agentic-tpm/SKILL.md` (v2.1.0 → v2.2.0)
> - `~/.claude/skills/shared/glossary-procedure.md` (new)
> - `ai-implementation-workstreams/00-JTBD-and-problem-statements/jtbd-evaluation-framework.md` (new)
> **Estimated Duration:** 3–4 days (staged)
> **Review Basis:** `docs/pl-funnel-intake-critical-review.md`

---

## Plan Architecture

```
Stage 1: UNBLOCK  (P0 fixes — skill executes correctly)
    ├── Task 1.1: Create glossary-procedure.md
    └── Task 1.2: Add Decision Gate to both skills

Stage 2: STRUCTURE (P1 enhancements — JTBD quality + stakeholder clarity)
    ├── Task 2.1: Restructure Box 1 with JTBD stratification
    ├── Task 2.2: Add JTBD → Resistance mapping to Box 7
    ├── Task 2.3: Collapse 28-item self-check to 10 tiered checks
    └── Task 2.4: Add stakeholder journey mapping to Box 2

Stage 3: POLISH   (P2 enhancements — output quality + friction reduction)
    ├── Task 3.1: Add stakeholder-specific digest views
    ├── Task 3.2: Add Anti-JTBDs
    └── Task 3.3: Add unified readiness cost to executive summary

Stage 4: VALIDATE (Verification — test the enhanced skill)
    ├── Task 4.1: Run skill against 3 canonical use cases
    ├── Task 4.2: Review output with stakeholder proxies
    └── Task 4.3: Version bump + changelog
```

---

## Stage 1: UNBLOCK (Day 1 — Morning)

**Goal:** Fix the two hard blockers so the skill executes correctly and stops bad bets.

---

### Task 1.1: Create `~/.claude/skills/shared/glossary-procedure.md`

**Why:** Both v1.1 and v2.0 reference this file. It does not exist. Without it, Step 1.5 fails silently.

**File to create:** `~/.claude/skills/shared/glossary-procedure.md`

**Content template:**
```markdown
---
name: glossary-procedure
preamble-tier: 2
description: |
  Shared glossary generation procedure for ProtoLabs skills. Extracts domain-specific
  terms from PM input, looks up definitions via cascade, and emits a confidence-rated
  term table. Used by pl-funnel-intake and agentic-tpm.
---

# Glossary Generation Procedure

## Purpose

Ensure all stakeholders share the same definitions before proceeding with use-case
analysis. Ambiguous terms are the #1 source of stakeholder misalignment.

## Procedure

### Step 1 — Term Extraction

Extract domain-specific terms from the use-case description. Broadest scope:
- Manufacturing terms (CNC, injection molding, DFM, tolerances)
- AI/ML terms (model, inference, fine-tuning, prompt)
- Governance terms (EU AI Act, NIST RMF, ISO 42001, ITAR, GDPR)
- Business terms (ROI, TTV, CAC, GM, NSM)
- Compliance terms (conformity assessment, DPIA, post-market monitoring)

### Step 2 — Definition Lookup Cascade

For each term, attempt lookup in this order:
1. **Seed glossary** (inline below)
2. **Governance glossary** — `C:\Users\dimos\ProtoLab\governance\docs\glossary.md` (if exists)
3. **KB search** — search `knowledge/` folder for term definitions
4. **Web search** — only for terms not found in local sources
5. **Mark ambiguous** — if no authoritative source found

### Step 3 — Confidence Rating

| Rating | Meaning | Action |
|--------|---------|--------|
| 🟢 | Definition from authoritative source (governance doc, KB article) | Use as-is |
| 🟡 | Definition inferred from context or web source | Note uncertainty |
| 🔴 | Definition ambiguous or contested | Ask PM to clarify (1 question max) |

### Step 4 — Output Format

Emit before the canvas:

```markdown
## Glossary of Assumed Definitions

> Terms extracted from use-case description. All stakeholders should confirm these
> definitions before proceeding. 🔴 terms require clarification.

| Term | Definition | Source | Confidence |
|------|-----------|--------|------------|
| [term] | [definition] | [file path or "inferred"] | 🟢/🟡/🔴 |
```

### Seed Glossary (Inline Definitions)

| Term | Definition | Source |
|------|-----------|--------|
| DFM | Design for Manufacturing — the practice of designing parts to optimize manufacturability | ProtoLabs KB |
| JTBD | Jobs to be Done — a framework for understanding user needs through the lens of the progress they seek | Christensen Institute |
| EU AI Act | European Union Artificial Intelligence Act — regulation classifying AI systems by risk level | governance/eu-ai-act-compliance-mapping.md |
| NIST AI RMF | National Institute of Standards and Technology AI Risk Management Framework | governance/nist-ai-rmf-compliance-mapping.md |
| ISO 42001 | International standard for AI management systems | governance/iso-42001-gap-analysis.md |
| ITAR | International Traffic in Arms Regulations — US export control for defense-related technical data | governance/compliance/itar.md |
| HITL | Human-in-the-Loop — a design pattern where human judgment is required at critical decision points | Inferred |
| TTV | Time to Value — the duration from project start to first measurable business outcome | Inferred |
| NSM | North Star Metric — the single metric that best captures the core value delivered to customers | Inferred |
| Working-with-Machines | ProtoLabs autonomy framework: Tool → Augmentation → Collaboration → Automation | governance/working-with-machines.md |

### Post-Glossary Gate

- If any 🔴 terms remain: Ask PM 1 clarifying question. Do not proceed until resolved.
- If all terms are 🟢 or 🟡: Proceed to canvas generation.
```

**Verification:**
- [ ] File exists at `~/.claude/skills/shared/glossary-procedure.md`
- [ ] File has valid YAML frontmatter
- [ ] Seed glossary includes at least 10 manufacturing/AI/governance terms
- [ ] Output format specifies Source column (required by self-check)

**Owner:** Technical Writer / Skill Maintainer
**Estimated effort:** 45 minutes

---

### Task 1.2: Add Decision Gate to Both Skills

**Why:** The skill currently generates a full canvas + 5 appendices even for use cases that should be killed or deferred. This wastes stakeholder time and creates false momentum.

**Files to edit:**
- `~/.claude/skills/pl-funnel-intake/SKILL.md`
- `~/.claude/skills/agentic-tpm/SKILL.md`

**Insertion point:** After Box 8 (Data Readiness), before Appendix A generation.

**Content to add (identical in both skills):**
```markdown
### Step 2.5 — Decision Gate (Hard Stop)

Before generating appendices, calculate the verdict. This is a **binding** gate —
if the verdict is KILL, DEFER, or REDESIGN, emit only the executive summary
(or equivalent header) with rationale and stop. Do not generate appendices.

**Calculations:**
- **Adjusted ROI** = Business Value (Box 3 ROI lower bound) − Technical Cost (Box 6 estimate) − Change Cost (Box 7.3 Total) − Data Engineering Cost (Box 8.8 weighted score < 3.0 adds $50k–$200k penalty)
- **Total Readiness Score** = min(Data Readiness Score, 6 − (Change Resistance Risk / 10))  [maps 6–45 risk to 1.5–5.4 scale, then clips to 1–5]
- **Evidence Gate** = (v2.0 only) If Box 1.5 shows 🔴 INSUFFICIENT EVIDENCE, verdict = RAT-FIRST

**Verdict Rules:**

| Condition | Verdict | Output |
|-----------|---------|--------|
| Adjusted ROI < 0 | **KILL** | Executive summary only + "Why this use case does not clear the ROI bar" |
| Total Readiness Score < 2.0 | **DEFER** | Executive summary + readiness gap analysis (which dimension is blocking) |
| Resistance Risk = Critical (46+) | **REDESIGN** | Box 7 only + 3 redesign prompts to reduce human impact |
| Evidence Gate = 🔴 (v2.0) | **RAT-FIRST** | Appendix C (Experiment Plan) only + discovery sprint recommendation |
| Tier 1/2 + RAT not yet run | **RAT-FIRST** | Appendix C only + "Run RAT before build commitment" |
| All clear | **PROCEED** | Full canvas + all appendices |

**Emission rule for non-PROCEED verdicts:**
```markdown
## Verdict: [VERDICT]

### Rationale
[2–3 sentences explaining which condition triggered the verdict]

### Required Action
[Specific next step: e.g., "Run 6 customer interviews and re-run intake"]

### Re-evaluation Criteria
[What must change for this use case to be reconsidered]
```

Do not emit appendices. Do not emit the full canvas. Stop here.
```

**Verification:**
- [ ] Decision Gate appears after Box 8 in both skills
- [ ] Verdict rules include all 5 cases (KILL, DEFER, REDESIGN, RAT-FIRST, PROCEED)
- [ ] Non-PROCEED verdicts truncate output (no appendices)
- [ ] Adjusted ROI formula references Box 3, Box 6, Box 7.3, Box 8.8
- [ ] Self-check updated to include "Decision Gate verdict emitted" as P0 check

**Owner:** Skill Maintainer
**Estimated effort:** 1 hour

---

## Stage 2: STRUCTURE (Day 1 — Afternoon + Day 2 — Morning)

**Goal:** Improve JTBD quality, stakeholder clarity, and change management actionability.

---

### Task 2.1: Restructure Box 1 with JTBD Stratification

**Why:** Current Box 1 generates generic JTBDs. The JTBD workstream already has Functional, Emotional, and Social jobs stratified. The skill should reference them and generate stakeholder-specific variants.

**Files to edit:**
- `~/.claude/skills/pl-funnel-intake/SKILL.md`
- `~/.claude/skills/agentic-tpm/SKILL.md`

**Knowledge source to add:**
```markdown
6. **JTBD reference**: `C:\Users\dimos\ProtoLab\ai-implementation-workstreams\00-JTBD-and-problem-statements\README.md` — functional, emotional, social job stratification
```

**Replace Box 1 content with:**
```markdown
#### Box 1 — Problem & JTBDs

**1.1 Current-State Pain (quantified where possible)**
[Existing content preserved]

**1.2 Functional JTBDs (what users need to accomplish)**
Generate 2–3 functional JTBDs in "When I'm [situation], I want [motivation], so I can [outcome]" form.
Reference the JTBD workstream for domain-specific functional jobs.

| JTBD | Primary Stakeholder | Evidence Source | Priority |
|------|--------------------:|-----------------|----------|
| | | [Interview / Support ticket / Win-loss / Inferred] | [P0/P1/P2] |

**1.3 Emotional JTBDs (how users want to feel)**
Generate 1–2 emotional JTBDs. These drive adoption and resistance. If missing, default to:
- "I want to feel confident that [AI system / process] is [secure / accurate / fair]"
- "I want to feel in control of [decisions / outcomes / risk]"

| JTBD | Primary Stakeholder | Threatened By | Priority |
|------|--------------------:|---------------|----------|
| | | [AI automation / Compliance gap / Uncertainty] | [P0/P1/P2] |

**1.4 Social JTBDs (how users want to be perceived)**
Generate 1 social JTBD. These drive champion behavior and political support.

| JTBD | Primary Stakeholder | Political Implication | Priority |
|------|--------------------:|----------------------|----------|
| | | [Champion / Blocker / Neutral lever] | [P0/P1/P2] |

**1.5 JTBD Priority Matrix**
Score each JTBD using the Opportunity Score (Ulwick): Importance × (5 − Current Satisfaction).

| JTBD | Importance (1-5) | Satisfaction (1-5) | Opportunity Score | Top Priority? |
|------|-----------------:|-------------------:|------------------:|:-------------:|
| | | | | |

**Priority rule:** Opportunity Score ≥ 15 = P0, 8–14 = P1, < 8 = P2.

**1.6 Inversion Question (Munger)**
"What would have to be true for this NOT to work?" — one sentence.
[v2.0 already has this; preserve]
```

**Verification:**
- [ ] Box 1 has 6 subsections (1.1–1.6)
- [ ] JTBD workstream added to Knowledge Sources
- [ ] Emotional and Social JTBDs are required fields (not optional)
- [ ] Opportunity Score formula is explicit
- [ ] Self-check updated: "Box 1 JTBDs stratified with stakeholder mapping"

**Owner:** Skill Maintainer
**Estimated effort:** 1.5 hours

---

### Task 2.2: Add JTBD → Resistance Mapping to Box 7

**Why:** Box 7 scores resistance but does not trace it back to the threatened jobs from Box 1. This makes mitigations generic instead of targeted.

**Files to edit:**
- `~/.claude/skills/pl-funnel-intake/SKILL.md`
- `~/.claude/skills/agentic-tpm/SKILL.md`

**Insert before Box 7.1:**
```markdown
**7.0 JTBD → Resistance Mapping**

For each resistance type, identify the threatened JTBD from Box 1 and the targeted mitigation.
This connects change management to the actual jobs at stake.

| Resistance Type | Threatened JTBD (from Box 1) | Root Cause | Targeted Mitigation |
|----------------|------------------------------|------------|---------------------|
| Identity Threat | [E1: "I want to feel confident in my expertise"] | AI replaces core design work | Reframe role; preserve quality sign-off; celebrate advisory wins |
| Skill Anxiety | [E2: "I want to feel competent in my role"] | New skills required (consultative selling) | Safe-to-fail training; peer mentoring; early wins |
| Economic Fear | [F4: "I want to ensure my economic security"] | Fear of layoff or pay cut | Written Transformation Guarantee; compensation floor |
| Quality Gatekeeper | [F2: "I want to ensure output quality"] | Liability for AI-generated errors | Engineer retains final sign-off; AI error transparency; override logging |
| Change Fatigue | [E3: "I want to feel my organization is stable"] | History of failed initiatives | Small wins first; no big-bang rollouts; acknowledge past failures |
| Comfort Zone | [E1 or E2] | Loss aversion; preference for known competence | Compelling personal benefit narrative; opt-in pilot option |

**Rule:** If a resistance type has no mapped JTBD, flag: "⚠️ No JTBD mapped — mitigation may be generic."
```

**Verification:**
- [ ] Box 7.0 exists in both skills
- [ ] All 6 resistance types have JTBD mapping columns
- [ ] Mitigation strategies are job-specific, not generic
- [ ] Self-check updated: "Box 7 includes JTBD → Resistance mapping"

**Owner:** Skill Maintainer
**Estimated effort:** 45 minutes

---

### Task 2.3: Collapse 28-Item Self-Check to 10 Tiered Checks

**Why:** 28 items = cognitive overload = skipped. 10 tiered items = actionable.

**Files to edit:**
- `~/.claude/skills/pl-funnel-intake/SKILL.md`
- `~/.claude/skills/agentic-tpm/SKILL.md`

**Replace the entire Pre-Emission Self-Check section with:**
```markdown
### Pre-Emission Self-Check (Tiered)

#### P0 — Must Pass (Hard Blockers)
Emitting output with any unchecked P0 item is a skill failure.

| # | Check | ✓ |
|---|-------|---|
| 1 | Glossary emitted with Source column for every term | ☐ |
| 2 | Box 5 includes all three governance frameworks (EU AI Act + NIST AI RMF + ISO 42001) | ☐ |
| 3 | Box 7 includes Resistance Risk Score + threshold classification + JTBD mapping | ☐ |
| 4 | Box 8 includes Data Readiness Score (1-5) with threshold classification | ☐ |
| 5 | Decision Gate verdict emitted (PROCEED / RAT-FIRST / REDESIGN / KILL / DEFER) | ☐ |

#### P1 — Should Pass (Quality Gates)
These distinguish a good intake from a great one.

| # | Check | ✓ |
|---|-------|---|
| 6 | Appendix A compliance table maps controls to specific components with liability allocation | ☐ |
| 7 | Appendix D cites verifiable URLs or states "no public evidence found" for every claim | ☐ |
| 8 | Box 1 JTBDs are stratified (Functional / Emotional / Social) with stakeholder mapping + Opportunity Scores | ☐ |
| 9 | Box 7 includes Change Cost Estimation compared to Box 3 ROI | ☐ |
| 10 | Executive summary (or equivalent header) includes Adjusted ROI and Total Readiness Score | ☐ |

**Auto-check guidance:** Where the skill can verify a condition programmatically
(e.g., "Glossary has Source column"), auto-check and only surface failures.
```

**Verification:**
- [ ] Self-check has exactly 10 items (5 P0 + 5 P1)
- [ ] P0 items are all hard blockers (output should not emit if unchecked)
- [ ] P1 items are quality differentiators
- [ ] No P2 "nice to have" items (moved to skill documentation, not self-check)

**Owner:** Skill Maintainer
**Estimated effort:** 30 minutes

---

### Task 2.4: Add Stakeholder Journey Mapping to Box 2

**Why:** RACI is static. Stakeholders change sentiment and influence over time. The skill should surface this trajectory.

**Files to edit:**
- `~/.claude/skills/pl-funnel-intake/SKILL.md`
- `~/.claude/skills/agentic-tpm/SKILL.md`

**Add to Box 2 (after RACI in v1.1, after 2.G ICP in v2.0):**
```markdown
#### Box 2.G — Stakeholder Journey Map

Map how key stakeholders are expected to move through the transformation.
This surfaces political risks early and defines trigger points for re-evaluation.

| Stakeholder | Current State | Intake Sentiment | Pilot Target | GA Target | Scale Target | Re-evaluation Trigger |
|-------------|--------------|------------------|--------------|-----------|--------------|----------------------|
| [Role, e.g., Engineering Director] | [1-sentence context] | [Advocate / Neutral / Skeptic / Blocker] | [Target sentiment] | [Target sentiment] | [Target sentiment] | [Event that triggers reassessment, e.g., "Pilot misses quality SLA"] |
| [Role, e.g., Senior Engineer] | | | | | | |
| [Role, e.g., Compliance Officer] | | | | | | |

**Sentiment definitions:**
- **Advocate:** Actively promotes the use case; volunteers for pilot
- **Neutral:** Willing to participate; no strong opinion
- **Skeptic:** Has concerns; requires evidence to move forward
- **Blocker:** Actively opposes; can veto or stall the use case

**Rule:** If any stakeholder is Blocker at Intake, flag in executive summary and require mitigation plan before PROCEED.
```

**Verification:**
- [ ] Box 2.G exists in both skills
- [ ] Table includes 5 phases (Current, Intake, Pilot, GA, Scale)
- [ ] Re-evaluation triggers are specific events, not vague conditions
- [ ] Self-check updated: "Box 2 includes stakeholder journey mapping"

**Owner:** Skill Maintainer
**Estimated effort:** 45 minutes

---

## Stage 3: POLISH (Day 2 — Afternoon)

**Goal:** Reduce per-stakeholder cognitive load and prevent scope creep.

---

### Task 3.1: Add Stakeholder-Specific Digest Views

**Why:** The full canvas is written for the PM. Other stakeholders need role-specific summaries. Without this, they must hunt through 10+ pages for their relevant sections.

**Files to edit:**
- `~/.claude/skills/pl-funnel-intake/SKILL.md`
- `~/.claude/skills/agentic-tpm/SKILL.md`

**Add to Output Format section (after appendices, before Pre-Emission Self-Check):**
```markdown
### Stakeholder Digests (Auto-Generated)

After the full canvas and appendices, emit a 1-page digest for each major stakeholder.
These are extracted from the canvas — no new content, just role-specific curation.

#### Executive Sponsor Digest
```markdown
## Digest for Executive Sponsor

| Field | Value |
|-------|-------|
| Verdict | [PROCEED / etc.] |
| Adjusted ROI | [$X–$Y] |
| Total Bet Cost | [Technical + Data + Change + Compliance] |
| Top 3 Risks | [From Box 4] |
| Change Cost vs. ROI | [Viable / Marginal / Inverted] |
| Decision Required | [What they must approve to proceed] |
| Timeline to First Value | [T+N weeks] |
| Kill Criteria | [From Appendix B] |
```

#### Engineering Lead Digest
```markdown
## Digest for Engineering Lead

| Field | Value |
|-------|-------|
| Technical Build Time | [N weeks] |
| Key Integration Points | [From Appendix A] |
| Compliance Components | [From Appendix A compliance table] |
| Non-Functional Requirements | [Latency, scale, availability, security] |
| Build vs. Buy Recommendations | [From Appendix A] |
| Kill Criteria | [From Appendix B] |
| Working-with-Machines Placement | [Current → Target autonomy level] |
```

#### Compliance Officer Digest
```markdown
## Digest for Compliance Officer

| Field | Value |
|-------|-------|
| EU AI Act Risk Class | [Limited / High] |
| NIST AI RMF Functions | [Govern / Map / Measure / Manage — which components] |
| ISO 42001 Clauses | [Specific clauses mapped to components] |
| New Controls Required | [Not already implemented] |
| Audit Timeline | [Key dates / milestones] |
| Documentation Gaps | [What must be created for conformity] |
| Liability Allocation | [Vendor / Protolabs / Customer per component] |
```

#### Change Management Lead Digest
```markdown
## Digest for Change Management Lead

| Field | Value |
|-------|-------|
| Resistance Risk Score | [N] / Threshold: [Low/Med/High/Critical] |
| Affected Headcount | [By role type] |
| Identity Threat Level | [None/Low/Med/High/Critical] |
| Top 3 Mitigation Strategies | [From Box 7] |
| Phase 0 Activities Required | [Yes / No] |
| Transformation Guarantee Required | [Yes / No] |
| Adjusted Time to Value | [Technical Build + Change Adoption] |
```

**Rule:** If a stakeholder type is not relevant to the use case (e.g., no customer-facing element → no Sales Director digest), state "N/A — [reason]" and omit the digest.
```

**Verification:**
- [ ] 4 digests defined (Executive, Engineering, Compliance, Change Management)
- [ ] Each digest has ≤ 8 fields
- [ ] Fields are extracted from canvas, not invented
- [ ] Output format section updated to include digests

**Owner:** Skill Maintainer
**Estimated effort:** 1.5 hours

---

### Task 3.2: Add Anti-JTBDs

**Why:** Scope creep often comes from solving jobs that should not be solved. Anti-JTBDs make these explicit.

**Files to edit:**
- `~/.claude/skills/pl-funnel-intake/SKILL.md`
- `~/.claude/skills/agentic-tpm/SKILL.md`

**Add to Box 1 (as 1.6, shifting Inversion Question to 1.7):**
```markdown
**1.6 Anti-JTBDs (Jobs We Must Not Solve)**

Explicitly state jobs that, if solved, would undermine the use case or create new risks.
These are the mirror of Non-Goals (Box 6.X) but framed from the user's perspective.

| Anti-JTBD | Why Excluded | Risk if Included |
|-----------|-------------|------------------|
| "When I'm an engineer, I want AI to handle all client communication, so I can focus on technical work" | Would eliminate the advisory role transformation | Identity threat becomes critical; adoption collapses; Box 7 resistance score → Critical |
| "When I'm a customer, I want fully automated ordering with zero human review, so I can get instant quotes" | Would violate quality gatekeeper JTBD and compliance requirements | Liability risk; engineer resistance; EU AI Act high-risk classification |

**Rule:** Every use case must have at least 1 Anti-JTBD. If none are obvious, flag: "⚠️ No Anti-JTBDs identified — scope creep risk."
```

**Verification:**
- [ ] Box 1.6 exists in both skills
- [ ] At least 2 example Anti-JTBDs provided as defaults
- [ ] Risk column connects to Box 7 resistance or Box 5 compliance
- [ ] Self-check updated: "Box 1 includes Anti-JTBDs with risk justification"

**Owner:** Skill Maintainer
**Estimated effort:** 30 minutes

---

### Task 3.3: Add Unified Readiness Cost to Executive Summary

**Why:** Decision-makers currently see technical cost, data cost, and change cost in separate boxes. They need a single figure.

**Files to edit:**
- `~/.claude/skills/pl-funnel-intake/SKILL.md` (add to Output Format header)
- `~/.claude/skills/agentic-tpm/SKILL.md` (add to Executive Summary Header)

**For v1.1 (add to top of output):**
```markdown
## Executive Summary

| Field | Value |
|-------|-------|
| Use case | [name] |
| Portfolio tier | [1/2/3/4] |
| EU AI Act risk class | [limited/high] |
| Verdict | [PROCEED / RAT-FIRST / REDESIGN / KILL / DEFER] |
| Total Readiness Cost | [Technical Build + Data Engineering + Change Management + Compliance] |
| ROI lower bound | [from Box 3] |
| Adjusted ROI | [Business Value − Total Readiness Cost] |
| Change cost vs. ROI verdict | [viable / marginal / inverted] |
| Total Readiness Score | [min(Data Readiness, Change Readiness)] |
| Recommendation | [PROCEED / etc. with 1-sentence rationale] |
```

**For v2.0 (extend existing executive summary):**
Add two rows to the existing table:
```markdown
| Total Readiness Cost | [Technical + Data + Change + Compliance] |
| Total Readiness Score | [min(Data Readiness, Change Readiness) / 5.0] |
```

**Verification:**
- [ ] Executive summary includes unified cost and readiness score
- [ ] Adjusted ROI is explicit (not just "ROI lower bound")
- [ ] Self-check updated: "Executive summary includes Adjusted ROI and Total Readiness Score"

**Owner:** Skill Maintainer
**Estimated effort:** 30 minutes

---

## Stage 4: VALIDATE (Day 3)

**Goal:** Verify the enhanced skill works correctly and produces better output.

---

### Task 4.1: Run Skill Against 3 Canonical Use Cases

**Test cases:**
1. **"Secure Design-to-Order Sandbox"** (ITAR-sensitive, high compliance, medium change)
2. **"Multimodal RFQ"** (customer-facing, high data readiness, low change)
3. **"Manufacturability Copilot"** (engineer-facing, high identity threat, high resistance)

**For each test case, verify:**
- [ ] Glossary emitted with Source column
- [ ] Box 1 has Functional + Emotional + Social JTBDs with Opportunity Scores
- [ ] Box 7 has JTBD → Resistance mapping
- [ ] Decision Gate emits a verdict before appendices
- [ ] If verdict = PROCEED, all appendices generated
- [ ] If verdict = KILL/DEFER/REDESIGN, output truncated correctly
- [ ] Stakeholder digests emitted at end
- [ ] Self-check has 10 items (not 28)

**Owner:** Skill Maintainer + PM Proxy
**Estimated effort:** 2 hours

---

### Task 4.2: Review Output with Stakeholder Proxies

**Reviewers:**
- Engineering Lead proxy: Check Appendix A digest for actionability
- Compliance Officer proxy: Check compliance digest for completeness
- Change Management Lead proxy: Check Box 7 and CM digest for usability

**For each proxy, collect:**
- Can you find your relevant information in < 2 minutes?
- Is the JTBD → Resistance mapping accurate for your domain?
- Does the verdict (PROCEED/KILL/etc.) feel justified by the data?
- What is still missing or confusing?

**Owner:** Technical Writer
**Estimated effort:** 1.5 hours

---

### Task 4.3: Version Bump + Changelog

**Actions:**
- [ ] Update `pl-funnel-intake/SKILL.md` version: `1.2.0` → `1.3.0`
- [ ] Update `agentic-tpm/SKILL.md` version: `2.1.0` → `2.2.0`
- [ ] Add changelog section to both skills:

```markdown
## Changelog

### v1.3.0 / v2.2.0 (2026-05-03)
- **Added:** JTBD Evaluation Framework integration — Box 1 consumes pre-evaluated JTBDs
- **Added:** Box 1.2 Activated JTBDs with MoSCoW, Evidence Quality, RICE, CoND
- **Added:** Box 1.3 JTBD Synthesis — aggregated MoSCoW view
- **Added:** Box 1.4 JTBD Evaluation Gate — 6-check gate blocking CM/Cost if failed
- **Added:** Discovery Sprint Plan template for failed gate checks
- **Added:** `jtbd-evaluation-framework.md` as single source of truth for job evaluation
- **Changed:** Box 1 no longer generates JTBDs — activates from framework
- **Changed:** Pre-Emission Self-Check expanded to include JTBD Evaluation Gate validation

### v1.2.0 / v2.1.0 (2026-05-03)
- **Added:** Decision Gate with binding verdicts (PROCEED / RAT-FIRST / REDESIGN / KILL / DEFER)
- **Added:** JTBD stratification (Functional / Emotional / Social) with Opportunity Scoring
- **Added:** JTBD → Resistance mapping in Box 7
- **Added:** Stakeholder Journey Map in Box 2
- **Added:** Stakeholder-specific digest views (Executive, Engineering, Compliance, CM)
- **Added:** Anti-JTBDs in Box 1
- **Added:** Unified Readiness Cost and Total Readiness Score in executive summary
- **Changed:** Pre-Emission Self-Check collapsed from 28 to 10 tiered items
- **Fixed:** Broken glossary-procedure.md reference — created shared glossary skill
```

**Owner:** Skill Maintainer
**Estimated effort:** 30 minutes

---

## Rollback Plan

If any enhancement causes skill execution failures:

1. **Immediate:** Revert the changed file from git (if version-controlled) or restore from backup.
2. **Diagnostic:** Run the skill against "Secure Design-to-Order Sandbox" and capture the error.
3. **Fix:** Apply the minimal fix to resolve the error.
4. **Re-verify:** Re-run the 3 canonical test cases.

**Backup strategy:** Before editing, copy `SKILL.md` to `SKILL.md.bak.YYYYMMDD`.

---

## Success Criteria

The enhancement is complete when:

1. ✅ Both skills execute without errors on all 3 canonical use cases.
2. ✅ Decision Gate stops at least 1 of the 3 test cases (e.g., "Manufacturability Copilot" should trigger REDESIGN or RAT-FIRST due to high identity threat).
3. ✅ Stakeholder proxies can find their digest information in < 2 minutes.
4. ✅ JTBD → Resistance mapping is rated "accurate" by the Change Management proxy.
5. ✅ Self-check completes in < 30 seconds of cognitive effort (vs. previous 28-item wall).
6. ✅ Version bumped and changelog written.

---

## Appendix: File Change Summary

| File | Change Type | Stage | Task |
|------|-------------|-------|------|
| `~/.claude/skills/shared/glossary-procedure.md` | Create | 1 | 1.1 |
| `~/.claude/skills/pl-funnel-intake/SKILL.md` | Edit | 1–3 | 1.2, 2.1–2.4, 3.1–3.3 |
| `~/.claude/skills/agentic-tpm/SKILL.md` | Edit | 1–3 | 1.2, 2.1–2.4, 3.1–3.3 |

**Total files touched:** 3
**Total new files:** 1
**Estimated total effort:** 2–3 days (1 person)

---

*End of plan.*
