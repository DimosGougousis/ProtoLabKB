# Critical Review: `pl-funnel-intake` Skill (v1.1) & `agentic-tpm` (v2.0)

> **Reviewer:** Technical Writer — Documentation Quality & Stakeholder Friction Analysis
> **Date:** 2026-05-03
> **Scope:** Skill definition, procedure, output format, and stakeholder friction points
> **Files Reviewed:**
> - `~/.claude/skills/pl-funnel-intake/SKILL.md` (v1.1.0)
> - `~/.claude/skills/agentic-tpm/SKILL.md` (v2.0.0)
> - `ai-implementation-workstreams/00-JTBD-and-problem-statements/README.md`
> - `governance/07-enterprise-implementation/process-integration/change-management-for-ai.md`

---

## 1. Executive Summary

| Dimension | Score | Verdict |
|-----------|-------|---------|
| **Completeness** | 8/10 | Excellent coverage of governance, compliance, change management, and data readiness |
| **Stakeholder Clarity** | 5/10 | RACI is present but static; no journey mapping; JTBDs are generated, not elicited |
| **Friction Reduction** | 4/10 | High cognitive load (28-item self-check); broken file reference; no go/no-go gate |
| **JTBD Quality** | 5/10 | Format is correct (When/I want/So I can) but lacks functional/emotional/social stratification and stakeholder-specific variants |
| **Actionability** | 6/10 | Output is comprehensive but may overwhelm; no clear "next step" artifact for each stakeholder |

**Bottom line:** The skill produces *defensible governance artifacts* but does not sufficiently reduce friction between stakeholders. The JTBD classification is structurally sound but semantically shallow — it treats all jobs as functional and fails to surface the emotional and social jobs that drive resistance (Box 7) and adoption (Box 9). The v2.0 `agentic-tpm` skill addresses many of these gaps but introduces new complexity without resolving the core friction problem.

---

## 2. Critical Findings (Ranked by Severity)

### 🔴 P0 — Broken File Reference (Hard Blocker)

**Issue:** Both v1.1 and v2.0 reference `~/.claude/skills/shared/glossary-procedure.md` in Step 1.5. This file does not exist in the workspace.

**Impact:** The skill cannot execute its glossary generation step. This breaks the "shared vocabulary" gate that is meant to prevent misalignment between stakeholders.

**Evidence:**
```markdown
# From SKILL.md Step 1.5
Load the shared glossary procedure: `~/.claude/skills/shared/glossary-procedure.md`
```

**Fix:** Either create the missing file or remove the dependency and inline a minimal glossary procedure.

---

### 🔴 P0 — No Go/No-Go Decision Gate

**Issue:** The skill generates artifacts (canvas + appendices) but never forces a binary decision. The Pre-Emission Self-Check is a quality gate, not a decision gate. There is no explicit "PROCEED / RAT-FIRST / REDESIGN / KILL / DEFER" recommendation that is binding.

**Impact:** Stakeholders leave the intake with a thick document and no clear verdict. The v2.0 executive summary header includes a "Recommendation" field, but the skill does not enforce that this field drive a hard stop.

**Evidence:**
- v1.1: No recommendation field at all.
- v2.0: Recommendation field exists but is not tied to a hard gate (e.g., "If KILL, stop here and emit only the executive summary").

**Fix:** Add a **Decision Gate** step after Box 7 + Box 8. If Change Cost > ROI lower bound OR Data Readiness < 2.0 OR Resistance Risk = Critical, the skill must emit a truncated output with a clear verdict and stop.

---

### 🟡 P1 — JTBDs Are Generated, Not Elicited

**Issue:** Box 1 instructs the skill to "produce 2–3 JTBDs" from the use-case description. This treats JTBDs as a creative writing exercise rather than a research output. The JTBD workstream (`00-JTBD-and-problem-statements/README.md`) contains a well-structured set of functional, emotional, and social jobs, but the skill does not reference it.

**Impact:**
- Stakeholders see generic JTBDs that do not reflect actual user struggles.
- The emotional jobs (e.g., "I want to feel confident that my IP is secure") that drive resistance in Box 7 are never surfaced in Box 1.
- The social jobs (e.g., "I want to be perceived as a security leader") that influence champion identification in Box 2 are missing.

**Evidence:**
```markdown
# From SKILL.md Box 1
- 2–3 JTBDs in "When I'm X doing Y, I want Z, so I can W" form
- Top JTBD ranked with rationale
```

Compare to the JTBD workstream, which has:
- Functional Jobs (F1–F4): Secure AI Input Processing, Defend Against Adversarial Attacks, etc.
- Emotional Jobs (E1–E3): Confidence in Security, Trust in Compliance, Control Over Risk
- Social Jobs (S1–S2): Industry Leadership, Responsible Innovation

**Fix:**
1. Reference the JTBD workstream as a knowledge source.
2. Stratify JTBDs into Functional / Emotional / Social in Box 1.
3. Map each JTBD to the stakeholder(s) who hold it (engineer, customer, compliance officer, etc.).
4. Add a "JTBD Elicitation Checklist" — if no interview evidence exists, flag the JTBD as "inferred — validation required."

---

### 🟡 P1 — Box 7 (Change Readiness) Is Isolated from Box 1 (JTBDs)

**Issue:** The change readiness assessment evaluates resistance but does not trace that resistance back to the unmet or threatened jobs of the affected stakeholders. The "Identity Threat" resistance type is fundamentally an emotional job being threatened — but this connection is never made explicit.

**Impact:** Mitigation strategies in Box 7 are generic ("training," "compensation") rather than job-specific ("reframe the engineer's job from 'drafter' to 'advisor'").

**Evidence:**
```markdown
# From change-management-for-ai.md
"The core psychological threat: 'If AI does the design, what am I?'"
```

This is an emotional job (E1: Confidence in professional identity) being threatened. The skill should surface this in Box 1 and reference it in Box 7.

**Fix:** Add a **JTBD → Resistance Mapping** table in Box 7:

| Resistance Type | Threatened JTBD | Mitigation Strategy |
|----------------|-----------------|---------------------|
| Identity Threat | E1: "I want to feel confident in my professional identity" | Reframe role from drafter to advisor; preserve quality sign-off authority |
| Skill Anxiety | E2: "I want to feel competent in my role" | Structured skill-building with safe-to-fail practice |
| Economic Fear | F4: "I want to ensure my economic security" | Transformation Guarantee with written compensation floor |

---

### 🟡 P1 — 28-Item Pre-Emission Self-Check Is Cognitive Overload

**Issue:** The self-check table has 28 items. In practice, this will be skimmed or skipped. It is a "wall of checkboxes" with no prioritization.

**Impact:** Quality gaps slip through. The skill emits incomplete outputs because the self-check is too burdensome to execute rigorously.

**Evidence:**
```markdown
# From SKILL.md — 28 rows, all equally weighted
| 1 | Glossary has Source column... | ☐ |
| 2 | Glossary has intro/outro framing... | ☐ |
... (through row 28)
```

**Fix:**
1. **Tier the checks:** P0 (must pass), P1 (should pass), P2 (nice to have).
2. **Auto-check where possible:** If the skill can verify a condition programmatically (e.g., "Glossary has Source column"), it should auto-check and only flag failures.
3. **Collapse related checks:** Items 5–8 (Appendix A compliance) could be a single "Compliance Architecture Complete" check with sub-items.
4. **Reduce to 10–12 high-signal checks.**

---

### 🟡 P1 — No Stakeholder Journey Mapping

**Issue:** Box 2 provides a static RACI table. It does not show how a stakeholder's role, sentiment, or influence changes over the lifecycle of the use case (intake → pilot → GA → scale).

**Impact:**
- Champions identified in Box 2 may lose influence during pilot.
- Saboteurs in Box 2 (v2.0) may become neutral if their concerns are addressed — but the skill has no mechanism to track this.
- The "Pre-Mortem Call Sheet" (v2.0) is a snapshot, not a trajectory.

**Fix:** Add a **Stakeholder Journey Map** — a simple table showing sentiment and influence at each phase:

| Stakeholder | Intake | Pilot | GA | Scale | Trigger for Re-evaluation |
|-------------|--------|-------|-----|-------|---------------------------|
| Engineering Director | Neutral | Cautious | Supportive | Champion | If pilot misses quality SLA |
| Senior Engineer (Skeptical Expert) | Skeptic | Observer | Neutral | Advocate | If identity threat is addressed |

---

### 🟢 P2 — Data Readiness (Box 8) and Change Readiness (Box 7) Do Not Intersect

**Issue:** Box 8.10 has an integration checklist with Box 7, but it is optional and shallow. The data engineering backlog (Box 8.7) and the change cost (Box 7.3) are never summed into a single "Total Cost of Readiness."

**Impact:** Decision-makers see two separate cost piles and must mentally integrate them. This increases the risk of underestimating total readiness cost.

**Fix:** Add a **Unified Readiness Cost** row in the executive summary:

```
| Total Readiness Cost | Technical Build + Data Engineering + Change Management + Compliance |
```

---

### 🟢 P2 — No "Anti-JTBD" or Non-Goal JTBDs

**Issue:** v2.0 adds Non-Goals / Anti-Scope (Box 6.X), but this is framed as feature exclusion. It does not capture the *jobs the solution must not do* — which is a powerful JTBD technique for preventing scope creep.

**Impact:** Stakeholders agree on what is in scope but disagree on what outcomes the solution must actively avoid.

**Fix:** Add an **Anti-JTBD** section:

| Anti-JTBD | Why We Must Not Solve This | Risk if We Do |
|-----------|---------------------------|---------------|
| "When I'm an engineer, I want AI to handle all client communication, so I can focus on technical work" | This would eliminate the advisory role transformation | Identity threat becomes critical; adoption collapses |

---

## 3. Stakeholder Friction Analysis

### Friction Matrix

| Stakeholder | Where They Engage | Friction Point | Severity |
|-------------|-------------------|----------------|----------|
| **Product Manager (user of skill)** | Input prompt | Must write a perfect use-case description upfront; no iterative clarification | High |
| **Engineering Lead** | Appendix A | Compliance architecture table is dense and liability-heavy; no "starter template" | Medium |
| **Compliance Officer** | Box 5, Appendix A | Must manually map EU AI Act + NIST + ISO 42001 for every use case; no reusable template | High |
| **Change Management Lead** | Box 7 | Resistance scoring is subjective; no calibration examples | Medium |
| **Executive Sponsor** | Executive Summary (v2.0 only) | v1.1 has no exec summary; v2.0 summary is 10 lines but not actionable without reading full doc | High |
| **Data Engineer** | Box 8 | Data quality assessment requires manual scoring; no automated guidance | Medium |
| **Sales Director** | Box 2, Box 9 (v2.0) | Buying center mapping is customer-facing only; internal sales impact is missing | Low |

### Key Insight: The Skill Serves the PM, Not the Stakeholder Ecosystem

The skill is optimized for the PM who runs `/pl-funnel-intake` to produce a canvas. It is not optimized for the *consumers* of that canvas. Each stakeholder receives a document formatted for the PM's workflow, not for their decision-making needs.

**Example:** A Compliance Officer needs to know:
- Which controls are *new* vs. *already implemented* for this use case?
- What is the *compliance cost* (audit, documentation, legal review)?
- What is the *regulatory timeline* (e.g., EU AI Act conformity assessment deadline)?

The current output buries this information in a dense table within Appendix A.

---

## 4. JTBD Classification: Specific Issues

### 4.1 Missing Stratification

The JTBD workstream (`00-JTBD-and-problem-statements/README.md`) correctly stratifies jobs into Functional, Emotional, and Social. The skill does not. This means:

- **Functional jobs** drive feature requirements (what the solution must do).
- **Emotional jobs** drive adoption and resistance (how stakeholders feel).
- **Social jobs** drive champion identification and political support (how stakeholders want to be perceived).

Without stratification, the canvas treats all jobs as functional, leading to feature-heavy, emotion-light product bets.

### 4.2 Missing Stakeholder-Specific JTBDs

The same use case has different jobs for different stakeholders:

| Stakeholder | Functional Job | Emotional Job | Social Job |
|-------------|---------------|---------------|------------|
| **Engineer** | "I want to review AI-generated designs quickly" | "I want to feel my expertise is still valued" | "I want to be seen as a quality guardian, not a bottleneck" |
| **Customer** | "I want to get accurate quotes faster" | "I want to feel confident in the manufacturing outcome" | "I want my procurement team to see me as innovative" |
| **Compliance Officer** | "I want to demonstrate audit compliance" | "I want to feel we are ahead of regulatory risk" | "I want to be recognized as a governance leader" |
| **Sales Director** | "I want to close deals faster" | "I want to feel in control of the sales process" | "I want to be seen as driving revenue innovation" |

The skill should generate stakeholder-specific JTBDs, not a single generic set.

### 4.3 Missing "Job Importance vs. Satisfaction" Scoring

The JTBD framework (Ulwick, Christensen) uses an importance × satisfaction matrix to prioritize jobs. The skill ranks JTBDs with "rationale" but does not score them.

**Fix:** Add a simple 1–5 scoring:

| JTBD | Importance (1-5) | Current Satisfaction (1-5) | Opportunity Score (I × (5-S)) | Priority |
|------|-----------------|---------------------------|------------------------------|----------|
| F1: Secure AI Input Processing | 5 | 1 | 20 | P0 |
| E1: Confidence in Security | 5 | 2 | 15 | P0 |
| S1: Industry Leadership | 3 | 3 | 6 | P2 |

---

## 5. Recommended Enhancements

### Enhancement 1: Fix the Broken Glossary Reference (P0)

**Action:** Create `~/.claude/skills/shared/glossary-procedure.md` or inline a minimal glossary step.

**Minimal inline procedure:**
```markdown
### Step 1.5 — Glossary Generation (Inline)

1. Extract domain-specific terms from the use-case description.
2. For each term, provide: Term | Definition | Source (file path or "inferred").
3. If a term is ambiguous, mark it 🔴 and ask the PM to clarify (1 question max).
4. Emit the glossary table before the canvas.
```

---

### Enhancement 2: Add a Hard Decision Gate (P0)

**Action:** Insert a new step between Box 8 and Appendix generation.

```markdown
### Step 2.5 — Decision Gate

Calculate:
- **Adjusted ROI** = Business Value (Box 3) - Technical Cost (Appendix B) - Change Cost (Box 7.3) - Data Engineering Cost (Box 8.8)
- **Total Readiness Score** = min(Data Readiness Score, Change Readiness Score)

**Verdict Rules:**
- If Adjusted ROI < 0 → **KILL** — emit executive summary only, with rationale.
- If Total Readiness Score < 2.0 → **DEFER** — emit readiness gap analysis, not full canvas.
- If Resistance Risk = Critical (46+) → **REDESIGN** — emit Box 7 only, with redesign prompts.
- If RAT not yet run AND Tier = 1/2 → **RAT-FIRST** — emit RAT plan (Appendix C), not full build commitment.
- Otherwise → **PROCEED** — emit full canvas + appendices.
```

---

### Enhancement 3: Stratify JTBDs and Add Stakeholder-Specific Variants (P1)

**Action:** Restructure Box 1 as follows:

```markdown
#### Box 1 — Problem & JTBDs

**1.1 Current-State Pain (quantified)**

**1.2 Functional JTBDs (what users need to accomplish)**
| JTBD | Stakeholder(s) | Evidence Source | Priority |
|------|---------------|-----------------|----------|
| "When I'm [X], I want [Z], so I can [W]" | [Primary user] | [Interview / ticket / inferred] | [P0/P1/P2] |

**1.3 Emotional JTBDs (how users want to feel)**
| JTBD | Stakeholder(s) | Threatened By | Priority |
|------|---------------|---------------|----------|
| "I want to feel confident that..." | [Role] | [AI automation / compliance gap / etc.] | [P0/P1/P2] |

**1.4 Social JTBDs (how users want to be perceived)**
| JTBD | Stakeholder(s) | Political Implication | Priority |
|------|---------------|----------------------|----------|
| "I want to be seen as..." | [Role] | [Champion / blocker / neutral] | [P0/P1/P2] |

**1.5 JTBD Priority Matrix**
| JTBD | Importance | Satisfaction | Opportunity Score | Top Priority? |
|------|-----------|------------|------------------|---------------|
```

---

### Enhancement 4: Add JTBD → Resistance Mapping in Box 7 (P1)

**Action:** Replace the generic resistance scoring with a job-threat mapping.

```markdown
#### Box 7 — Change Readiness & Human Impact

**7.0 JTBD → Resistance Mapping**

For each resistance type, identify the threatened JTBD and the mitigation:

| Resistance Type | Threatened JTBD (from Box 1) | Root Cause | Mitigation Strategy |
|----------------|------------------------------|------------|---------------------|
| Identity Threat | E1: "I want to feel confident in my expertise" | AI replaces core design work | Reframe role; preserve quality sign-off; celebrate advisory wins |
| Skill Anxiety | E2: "I want to feel competent" | New skills (consultative selling) required | Safe-to-fail training; peer mentoring; early wins |
| Economic Fear | F4: "I want economic security" | Fear of layoff or pay cut | Written Transformation Guarantee; compensation floor |
| Quality Gatekeeper | F2: "I want to ensure output quality" | Liability for AI-generated errors | Engineer retains final sign-off; AI error transparency |
```

---

### Enhancement 5: Collapse the Pre-Emission Self-Check (P1)

**Action:** Replace 28 items with 10 tiered checks.

```markdown
### Pre-Emission Self-Check (Tiered)

#### P0 — Must Pass (Hard Blockers)
| # | Check | ✓ |
|---|-------|---|
| 1 | Glossary emitted with Source column | ☐ |
| 2 | Box 5 includes all three governance frameworks (EU AI Act + NIST + ISO 42001) | ☐ |
| 3 | Box 7 includes Resistance Risk Score + threshold classification | ☐ |
| 4 | Box 8 includes Data Readiness Score (1-5) | ☐ |
| 5 | Decision Gate verdict emitted (PROCEED / RAT-FIRST / REDESIGN / KILL / DEFER) | ☐ |

#### P1 — Should Pass (Quality Gates)
| # | Check | ✓ |
|---|-------|---|
| 6 | Appendix A compliance table maps controls to specific components with liability allocation | ☐ |
| 7 | Appendix D cites verifiable URLs or states "no public evidence found" | ☐ |
| 8 | Box 1 JTBDs are stratified (Functional / Emotional / Social) with stakeholder mapping | ☐ |
| 9 | Box 7 includes JTBD → Resistance mapping | ☐ |
| 10 | Executive summary includes Adjusted ROI and Total Readiness Score | ☐ |
```

---

### Enhancement 6: Add Stakeholder Journey Mapping (P1)

**Action:** Add a new subsection to Box 2.

```markdown
#### Box 2.G — Stakeholder Journey Map

| Stakeholder | Current State | Intake Sentiment | Pilot Target | GA Target | Scale Target | Trigger for Re-evaluation |
|-------------|--------------|------------------|--------------|-----------|--------------|---------------------------|
| [Role] | [Description] | [Advocate/Neutral/Skeptic/Blocker] | [Target sentiment] | [Target sentiment] | [Target sentiment] | [Event that triggers reassessment] |
```

---

### Enhancement 7: Add Stakeholder-Specific Output Views (P2)

**Action:** After generating the full canvas, emit a "Stakeholder Digest" — a 1-page summary tailored to each major stakeholder.

```markdown
### Stakeholder Digests (Auto-generated from canvas)

#### For Executive Sponsor
- Verdict: [PROCEED / etc.]
- Adjusted ROI: [$X–$Y]
- Top 3 risks: [List]
- Decision required: [What they must approve]

#### For Engineering Lead
- Technical build time: [N weeks]
- Key integration points: [List]
- Compliance components: [List]
- Kill criteria: [List]

#### For Compliance Officer
- EU AI Act risk class: [Limited / High]
- New controls required: [List]
- Audit timeline: [Dates]
- Documentation gaps: [List]

#### For Change Management Lead
- Resistance risk score: [N]
- Affected headcount: [N]
- Top 3 mitigation strategies: [List]
- Phase 0 activities required: [Yes / No]
```

---

### Enhancement 8: Add Anti-JTBDs (P2)

**Action:** Add to Box 1 or Box 6.X.

```markdown
#### Box 1.6 — Anti-JTBDs (Jobs We Must Not Solve)

| Anti-JTBD | Why Excluded | Risk if Included |
|-----------|-------------|------------------|
| "When I'm an engineer, I want AI to handle all client communication..." | Would eliminate advisory role transformation | Identity threat → critical; adoption collapse |
| "When I'm a customer, I want fully automated ordering with zero human review..." | Would violate quality gatekeeper JTBD | Liability risk; engineer resistance |
```

---

## 6. Best Practices to Adopt

### 6.1 From JTBD Theory (Christensen / Ulwick)

1. **Elicit, don't invent.** JTBDs should come from interviews, support tickets, and win/loss data — not from the skill's imagination. The v2.0 "Discovery Evidence" box (Box 1.5) is a good start but should gate JTBD generation, not just canvas advancement.
2. **Score importance × satisfaction.** Use the Opportunity Score to prioritize jobs, not just the PM's intuition.
3. **Segment by stakeholder.** The same use case has different jobs for engineers, customers, compliance officers, and sales leaders.

### 6.2 From Change Management (Prosci / Kotter)

1. **Map resistance to threatened jobs.** The change management framework already does this implicitly ("Identity Threat" = threatened emotional job). Make it explicit in the skill.
2. **Use the ADKAR model as a checklist.** For each stakeholder, check: Awareness → Desire → Knowledge → Ability → Reinforcement. The skill currently skips Desire and Reinforcement.
3. **Co-create the canvas with affected stakeholders.** The skill generates the canvas in one shot. In practice, the PM should share drafts with engineers and incorporate feedback before the workshop.

### 6.3 From Documentation Design (Divio System)

1. **Separate tutorials from reference.** The current output mixes tutorial (how to think about the use case) with reference (compliance mappings, data schemas). Consider splitting into:
   - **Tutorial:** "How to evaluate a use case" (for new PMs)
   - **How-to:** "How to run `/pl-funnel-intake`" (for experienced PMs)
   - **Reference:** "Compliance mapping templates" (for compliance officers)
   - **Explanation:** "Why change readiness matters" (for executives)
2. **Provide a quick-start path.** New users should be able to get a "lite" canvas (Boxes 1–4 only) in 5 minutes, then deepen as needed.

### 6.4 From Decision Science (Kahneman / Duke)

1. **Use pre-mortems, not just post-mortems.** v2.0 adds a pre-mortem (Box 4). Extend this to stakeholders: "If this fails, what will each stakeholder say?"
2. **Calibrate estimates.** The skill uses ranged estimates (good), but does not provide calibration guidance. Add: "If you are 90% confident the range is correct, make it 50% wider."
3. **Force a kill criterion for every milestone.** Appendix B has kill criteria, but they are often vague ("pilot fails"). Make them numeric: "If <3 of 5 pilot customers achieve <20% time savings by Week 12, kill."

---

## 7. Summary of Recommended Changes

| Priority | Enhancement | Effort | Impact |
|----------|-------------|--------|--------|
| P0 | Fix broken glossary reference | 30 min | Unblocks skill execution |
| P0 | Add hard Decision Gate | 1 hour | Prevents bad bets from advancing |
| P1 | Stratify JTBDs + stakeholder variants | 2 hours | Reduces stakeholder friction |
| P1 | Add JTBD → Resistance mapping | 1 hour | Makes change management actionable |
| P1 | Collapse self-check to 10 items | 30 min | Increases quality gate adherence |
| P1 | Add stakeholder journey mapping | 1 hour | Surfaces political dynamics |
| P2 | Add stakeholder-specific digests | 2 hours | Reduces cognitive load per stakeholder |
| P2 | Add Anti-JTBDs | 30 min | Prevents scope creep |

**Total estimated effort:** ~8 hours of skill editing.

**Expected outcome:**
- Stakeholder friction reduced by surfacing emotional/social jobs early.
- Bad bets stopped at intake, not after 6 months of build.
- Compliance officers, engineering leads, and change management leads receive actionable, role-specific outputs.
- The canvas becomes a *decision tool*, not just a *documentation artifact*.

---

*End of review.*
