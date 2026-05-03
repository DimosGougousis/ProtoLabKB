# Stage 2 Implementation Plan: STRUCTURE

> **Date:** 2026-05-03
> **Scope:** JTBD stratification, resistance mapping, stakeholder journey
> **Target Files:**
> - `~/.claude/skills/pl-funnel-intake/SKILL.md` (v1.2.0)
> - `~/.claude/skills/agentic-tpm/SKILL.md` (v2.1.0)
> **Prerequisite:** Stage 1 complete (Decision Gate, tiered self-check, version bump)

---

## Task Dependency Graph

```
Task 2.1 (Box 1 JTBD Stratification)
    ├── Adds JTBD workstream to Knowledge Sources
    ├── Restructures Box 1 with 1.1–1.6 subsections
    └── Outputs: Functional + Emotional + Social JTBDs + Opportunity Scores + Anti-JTBDs
         │
         ▼
Task 2.2 (Box 7 JTBD → Resistance Mapping)
    ├── Consumes Emotional/Social JTBDs from Box 1
    ├── Adds Box 7.0 before existing 7.1
    └── Outputs: Targeted mitigations linked to threatened jobs
         │
         ▼
Task 2.3 (Box 2 Stakeholder Journey Map)
    ├── Consumes stakeholder list from Box 2 RACI
    ├── Adds Box 2.G (v1.1) / Box 2.H (v2.0)
    └── Outputs: Sentiment trajectory Intake → Pilot → GA → Scale
         │
         ▼
Task 2.4 (Self-Check Updates)
    ├── Activates P1 checks that reference Stage 2 features
    └── Updates Required Behaviors section
```

---

## Task 2.1: Box 1 JTBD Stratification

### Objective
Replace the flat JTBD generation in Box 1 with a stratified structure that surfaces Functional, Emotional, and Social jobs — plus Opportunity Scoring and Anti-JTBDs.

### Why This Matters
- **Functional jobs** drive feature requirements (what the solution must do)
- **Emotional jobs** drive adoption and resistance (how stakeholders feel) — these feed directly into Box 7
- **Social jobs** drive champion behavior and political support (how stakeholders want to be perceived) — these feed into Box 2
- **Anti-JTBDs** prevent scope creep by stating jobs the solution must actively NOT solve
- **Opportunity Scoring** (`Importance × (5 − Satisfaction)`) provides an objective prioritization method

### Changes Required

#### A. Add JTBD Workstream to Knowledge Sources

**In both skills**, add after the change management framework reference:

```markdown
6. **JTBD reference**: `C:\Users\dimos\ProtoLab\ai-implementation-workstreams\00-JTBD-and-problem-statements\README.md` — functional, emotional, social job stratification, problem statements by priority, OKRs
```

#### B. Replace Box 1 Content

**In `pl-funnel-intake`:**

Replace:
```markdown
#### Box 1 — Problem & JTBD
- Current-state pain (quantified where possible)
- 2–3 JTBDs in "When I'm X doing Y, I want Z, so I can W" form
- Top JTBD ranked with rationale
```

With:
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

**1.6 Anti-JTBDs (Jobs We Must Not Solve)**
Explicitly state jobs that, if solved, would undermine the use case or create new risks.

| Anti-JTBD | Why Excluded | Risk if Included |
|-----------|-------------|------------------|
| "When I'm an engineer, I want AI to handle all client communication, so I can focus on technical work" | Would eliminate the advisory role transformation | Identity threat becomes critical; adoption collapses; Box 7 resistance score → Critical |
| "When I'm a customer, I want fully automated ordering with zero human review, so I can get instant quotes" | Would violate quality gatekeeper JTBD and compliance requirements | Liability risk; engineer resistance; EU AI Act high-risk classification |

**Rule:** Every use case must have at least 1 Anti-JTBD. If none are obvious, flag: "⚠️ No Anti-JTBDs identified — scope creep risk."
```

**In `agentic-tpm`:**

Replace:
```markdown
#### Box 1 — Problem & JTBD

- Current-state pain (quantified where possible)
- 2–3 JTBDs in "When I'm X doing Y, I want Z, so I can W" form
- Top JTBD ranked with rationale
- **Inversion question** (Munger): "What would have to be true for this NOT to work?" — one sentence
```

With the same structure as above, but preserve the Inversion Question as **1.7** (shifted down).

### Verification
- [ ] Box 1 has 6–7 subsections (1.1–1.6 + 1.7 inversion in v2.0)
- [ ] JTBD workstream added to Knowledge Sources
- [ ] Emotional and Social JTBDs are required fields
- [ ] Opportunity Score formula is explicit
- [ ] Anti-JTBDs have at least 2 default examples
- [ ] Self-check P1 item 8 references Box 1 stratification

---

## Task 2.2: Box 7 JTBD → Resistance Mapping

### Objective
Add a new subsection (Box 7.0) that maps each resistance type to the threatened JTBD from Box 1, making mitigations targeted rather than generic.

### Why This Matters
The change management framework already identifies resistance types (Identity Threat, Skill Anxiety, etc.) but treats them as isolated phenomena. In reality, each resistance type is a reaction to a threatened job:
- **Identity Threat** = "I want to feel confident in my professional identity" is threatened
- **Skill Anxiety** = "I want to feel competent in my role" is threatened
- **Economic Fear** = "I want to ensure my economic security" is threatened

By mapping resistance → threatened JTBD → targeted mitigation, the skill produces actionable change management plans instead of generic "training and communication" recommendations.

### Changes Required

**In both skills**, insert before Box 7.1:

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

### Verification
- [ ] Box 7.0 exists in both skills
- [ ] All 6 resistance types have JTBD mapping columns
- [ ] Mitigation strategies are job-specific, not generic
- [ ] Self-check P0 item 3 updated to mention "+ JTBD mapping"

---

## Task 2.3: Box 2 Stakeholder Journey Map

### Objective
Add a dynamic view of how stakeholder sentiment and influence change over the use-case lifecycle (Intake → Pilot → GA → Scale).

### Why This Matters
RACI is static. In practice:
- A champion identified at Intake may lose credibility during Pilot if quality SLAs are missed
- A skeptic may become an advocate if their concerns are addressed
- A blocker may soften if given an advisory role in the transformation

The journey map surfaces these trajectories and defines trigger events for re-evaluation.

### Changes Required

**In `pl-funnel-intake`:**

Add after Box 2 RACI:

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

**In `agentic-tpm`:**

Add after Box 2.G ICP / Beachhead / Anti-ICP as **Box 2.H**:

```markdown
#### Box 2.H — Stakeholder Journey Map

Map how key stakeholders are expected to move through the transformation.
This surfaces political risks early and defines trigger points for re-evaluation.

| Stakeholder | Current State | Intake Sentiment | Pilot Target | GA Target | Scale Target | Re-evaluation Trigger |
|-------------|--------------|------------------|--------------|-----------|--------------|----------------------|
| [Role] | [Context] | [Advocate/Neutral/Skeptic/Blocker] | [Target] | [Target] | [Target] | [Trigger event] |

**Sentiment definitions:**
- **Advocate:** Actively promotes; volunteers for pilot
- **Neutral:** Willing to participate; no strong opinion
- **Skeptic:** Has concerns; requires evidence
- **Blocker:** Actively opposes; can veto or stall

**Rule:** If any stakeholder is Blocker at Intake, flag in executive summary and require mitigation plan before PROCEED.
```

### Verification
- [ ] Journey map exists in both skills
- [ ] Table includes 5 phases (Current, Intake, Pilot, GA, Scale)
- [ ] Re-evaluation triggers are specific events
- [ ] Self-check updated to reference stakeholder journey mapping

---

## Task 2.4: Self-Check & Required Behaviors Updates

### Objective
Activate the P1 checks that reference Stage 2 features, and update Required Behaviors to enforce new patterns.

### Changes Required

**In both skills**, update the P1 self-check items that were staged in Stage 1:

The P1 items already reference Stage 2 features (e.g., "Box 1 JTBDs are stratified"). These were added in Stage 1 but the underlying content did not yet exist. After Tasks 2.1–2.3, these checks become valid.

**No structural change needed** — the self-checks were pre-positioned in Stage 1.

**Add to Required Behaviors in both skills:**

```markdown
- Box 1 JTBDs must be stratified into Functional, Emotional, and Social jobs with stakeholder mapping.
- Box 1 must include at least 1 Anti-JTBD with explicit risk justification.
- Box 7 resistance mitigations must map to threatened JTBDs from Box 1 — generic mitigations are not acceptable.
- Box 2 must include a Stakeholder Journey Map showing sentiment trajectory from Intake to Scale.
```

### Verification
- [ ] Required Behaviors section includes JTBD stratification rule
- [ ] Required Behaviors section includes Anti-JTBD rule
- [ ] Required Behaviors section includes JTBD → Resistance mapping rule
- [ ] Required Behaviors section includes Stakeholder Journey Map rule

---

## Implementation Order

```
Step 1: Task 2.1A — Add JTBD workstream to Knowledge Sources (both skills)
Step 2: Task 2.1B — Replace Box 1 content (both skills)
Step 3: Task 2.2 — Insert Box 7.0 before 7.1 (both skills)
Step 4: Task 2.3 — Add Stakeholder Journey Map (both skills)
Step 5: Task 2.4 — Update Required Behaviors (both skills)
Step 6: Verification — Run diff against originals, check all insertion points
```

**Parallelization opportunity:** Steps 1–4 can be done in parallel across the two skills (4 independent edits). Step 5 (Required Behaviors) must wait for Steps 1–4 to complete.

---

## Rollback Strategy

If any edit corrupts the skill file:

1. Restore from `SKILL.md.bak.20260503` (created during Stage 1)
2. Re-apply Stage 1 changes (version bump, Decision Gate, self-check)
3. Re-apply Stage 2 changes incrementally, verifying after each task

---

## Success Criteria

- [ ] Both skills reference the JTBD workstream in Knowledge Sources
- [ ] Box 1 in both skills has Functional + Emotional + Social JTBDs with Opportunity Scoring
- [ ] Box 1 in both skills has Anti-JTBDs with risk justification
- [ ] Box 7 in both skills has JTBD → Resistance mapping (Box 7.0)
- [ ] Box 2 in both skills has Stakeholder Journey Map
- [ ] Required Behaviors enforces all Stage 2 patterns
- [ ] Self-check P1 items validate Stage 2 features
- [ ] No syntax errors or broken references in either skill file

---

## Time Estimate

| Task | Effort |
|------|--------|
| 2.1A — Knowledge Sources update | 10 min |
| 2.1B — Box 1 restructure | 45 min |
| 2.2 — Box 7.0 insertion | 20 min |
| 2.3 — Journey map addition | 20 min |
| 2.4 — Required Behaviors update | 15 min |
| Verification | 20 min |
| **Total** | **~2.5 hours** |

---

*End of Stage 2 Implementation Plan.*
