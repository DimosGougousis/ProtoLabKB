# ProtoLab Product Manager Workflow Guide

> How to navigate a new AI/ML project from idea to implementation using the ProtoLab system.

---

## The PM Journey at a Glance

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  1. DISCOVER │ → │  2. INTAKE  │ → │ 3. FEASIBILITY│ → │ 4. REHEARSE │ → │ 5. DELIVER  │
│   (Explore)  │    │  (Canvas)   │    │   (Probe)    │    │  (Stress-test)│   (Implement)│
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
      │                  │                  │                  │                  │
   /pl-use-case      /pl-funnel-       /pl-feasibility    /pl-rehearse      Work packages
   -explorer         intake or         -probe                                + Governance
                     /pl-agentic                                              + DFM review
                     -tpm
```

**Total time investment**: 2–4 hours of structured work → a decision-ready product bet.

---

## Stage 1: Discover — "What should we build?"

**Goal**: Generate and rank candidate AI use cases for your domain.

**When to use**: You have a vague problem space but no crisp use-case definition. Or you want to validate that your idea is the *best* use of resources.

**Command**:
```
/pl-use-case-explorer <domain>
```

**Examples**:
```
/pl-use-case-explorer "customer-edge"
/pl-use-case-explorer "manufacturability"
/pl-use-case-explorer "quoting"
/pl-use-case-explorer "operations"
/pl-use-case-explorer                    # Full landscape scan
```

**What you get**:
| Output | Purpose |
|--------|---------|
| Scored candidate table (3–5 use cases) | Prioritized by impact, feasibility, data readiness, strategic fit |
| Portfolio tier mapping (1/2/3/4) | Tells you if this is a 6-month ship, 18-month build, or partner play |
| EU AI Act risk class | Early compliance signal |
| Competitive gap analysis | Why us vs. Xometry, Fictiv, etc. |
| Autonomy level recommendation | Tool → Augmentation → Collaboration → Autonomy |

**Decision gate**: Pick the top-ranked candidate. If none score above a 7/10, stop. The domain isn't ready.

**Time**: 15–30 minutes.

---

## Stage 2: Intake — "What does this use case actually look like?"

**Goal**: Produce a structured, decision-ready canvas that captures the full product bet — not just the tech.

**When to use**: You have a use-case description and need to turn it into a defensible, shareable artifact.

**Two options**:

### Option A: Standard Funnel Intake (v1.2)
For most use cases. Produces the 6-box canvas + Box 7 (Change Readiness) + 4 appendices.

```
/pl-funnel-intake "<use-case-description>"
```

**Example**:
```
/pl-funnel-intake "Secure Design-to-Order Sandbox: AppStream-hosted CAD environment where Save = order trigger; for ITAR / IP-sensitive customers."
```

### Option B: Agentic TPM (v2.1) — Recommended
For strategic bets, board presentations, or when you need to win political support. Produces a 12-section canvas with customer discovery evidence, business model, PR-FAQ, and YAML companion.

```
/pl-agentic-tpm "<use-case-description>"
```

**Example**:
```
/pl-agentic-tpm "Manufacturability Copilot for Customers: real-time DFM feedback during design in-browser."
```

**What you get** (Agentic TPM — superset of Funnel Intake):

| Box | Content | Why It Matters |
|-----|---------|----------------|
| **Executive Summary** | 10-line C-suite snapshot | Gets you the 60-second meeting |
| **Box 1 — Problem & JTBDs** | Functional, emotional, social jobs | Validates you're solving a real problem |
| **Box 1.5 — Discovery Evidence** | Customer truth gate | Separates real pain from assumed pain |
| **Box 2 — Stakeholders** | Power map, champions, saboteurs | Wins politically before you build |
| **Box 3 — Value & Metrics** | North Star Metric, OKRs, theory of change | Ties the bet to business outcomes |
| **Box 3.6 — Business Model** | Value capture, pricing, TCO | Shows how we make money |
| **Box 4 — Solution Sketch** | High-level capability description | Sets scope without over-specifying |
| **Box 5 — Data & AI Readiness** | Data availability, model options, cold-start | Surfaces the hardest problem early |
| **Box 5.5 — Trust Calibration** | Human-AI trust, behavioral design | Predicts adoption or rejection |
| **Box 6 — Risks & Mitigations** | Pre-mortem, non-goals, sunset criteria | Shows you've thought about failure |
| **Box 7 — Change Readiness** | Workforce transformation cost | Prevents "great product, no adoption" |
| **Box 9 — GTM & Adoption** | Launch plan, adoption funnel | Bridges build → usage |
| **Appendix A — Solution Architecture** | 6-layer architecture sketch | Engineering conversation starter |
| **Appendix B — Governance Triad** | EU AI Act, NIST AI RMF, ISO 42001 | Compliance pre-check |
| **Appendix C — Data & MLOps** | Data prerequisites, monitoring, retraining | Data engineering contract |
| **Appendix D — Effort & Timeline** | T-shirt sizing, dependency map | Resource planning |
| **Appendix E — Riskiest Assumption Test** | RAT design, pass/fail criteria | De-risks before build |
| **Appendix F — PR-FAQ** | Working-backwards press release | Forces customer-centric thinking |
| **Appendix G — YAML Companion** | Structured machine-readable output | Feeds into Jira, Confluence, etc. |

**Decision gate**: Does the Adjusted ROI (Business Value − Total Readiness Cost) justify proceeding? Does the recommendation say PROCEED, RAT-FIRST, or KILL?

**Time**: 30–60 minutes.

---

## Stage 3: Feasibility — "Can we actually build this?"

**Goal**: Sharpen Appendix A (Solution Architecture) into an engineering-facing artifact with build-vs-buy decisions, integration points, and effort estimates.

**When to use**: The canvas says PROCEED or RAT-FIRST, and you need to validate technical feasibility before committing resources.

**Command**:
```
/pl-feasibility-probe "<use-case-description>"
```

**Example**:
```
/pl-feasibility-probe "Secure Design-to-Order Sandbox: AppStream-hosted CAD environment where Save = order trigger; for ITAR / IP-sensitive customers."
```

**What you get**:

| Section | Output |
|---------|--------|
| Architecture Sketch | Boxes-and-arrows mapped to 6-layer Teresa architecture |
| Model Class Options | Classical ML / Deep Learning / Generative / Hybrid with tradeoffs |
| Build vs Buy Table | Per-component recommendation with "buy commodity, build moat" framing |
| Integration Points | ProDesk hooks, ERP/CRM, partner APIs, cloud services |
| Data Prerequisites | Training data volume, labels, source; eval data; production flow |
| MLOps Requirements | Latency SLO, monitoring, retraining cadence, cost envelope |
| Governance Triad Mapping | EU AI Act risk class + NIST AI RMF functions + ISO 42001 controls |

**Decision gate**: Can engineering commit to the architecture? Is the cost envelope acceptable? Are data prerequisites achievable?

**Time**: 20–30 minutes.

---

## Stage 4: Rehearse — "Will this survive a skeptical engineer?"

**Goal**: Stress-test your canvas and feasibility probe before the real workshop. Simulate a senior Protolabs engineer with 15+ years of experience who is *not* enthusiastic about AI.

**When to use**: Before any workshop, board presentation, or engineering review. This is your dry run.

**Command**:
```
/pl-rehearse "<use-case-name>"
```

**Example**:
```
/pl-rehearse "Secure Design-to-Order Sandbox"
```

**What happens**:
1. The system loads your funnel intake artifact (if you provide it)
2. A simulated senior engineer asks you **one question at a time** across five dimensions:
   - **Semantic Precision** — "You defined 'real-time' as <5s — where did that number come from?"
   - **Working-with-Machines** — "Why are you placing this at Augmentation, not Tool?"
   - **Governance** — "Where's our EU AI Act conformity assessment for this?"
   - **Market/Competition** — "Xometry already does this — why us?"
   - **Legal/Liability** — "When the AI quotes an ITAR-controlled part wrong, who eats the liability?"
   - **Cost/ROI** — "Show me the math, not the slide."

3. You answer each question. The engineer pushes back on weak answers.
4. After 6–10 questions, you get a scorecard:
   - Clarity (1–5)
   - Empathy (1–5)
   - Technical Depth (1–5)
   - Prioritization (1–5)
   - Change-Management Instinct (1–5)

**Decision gate**: Did you sustain the probes without the artifact falling apart? If the weakest dimension is below 3, sharpen it before the real workshop.

**Time**: 20–40 minutes.

---

## Stage 5: Deliver — "Let's build it (safely)."

**Goal**: Move from artifact to implementation with governance guardrails.

### 5.1 Design Review (if building a physical part)
```
/pl-dfm-review "<part-description>"
```
Routes to CNC, injection molding, sheet metal, or 3D printing agent. Returns DFM evaluation with source citations.

### 5.2 Governance Assessment
```
/pl-governance <assessment-type> [scope]
```
Assesses compliance with AI governance framework. Use before any production deployment.

### 5.3 Comprehensive Assessment
```
/pl-assess <target> [criteria]
```
Combined DFM + governance evaluation. Use for final sign-off.

### 5.4 Implementation Workstreams
If the canvas and feasibility probe pass, file the work in the appropriate track:

| Track | Owner | Status | Description |
|-------|-------|--------|-------------|
| **WP-CAD** | Engineering + PM | 🟡 Planning | CAD AI Evaluation — $600K strategic initiative |
| **WP01 — Input Sanitization** | Security | 🔴 Blocked | Unprotected AI inputs (prompt injection) |
| **WP02 — Adversarial Defense** | Security | 🔴 Blocked | Multi-layer defense against attacks |
| **WP03 — Runtime Monitoring** | SRE | 🔴 Blocked | Real-time AI behavior visibility |
| **WP04 — Audit & Compliance** | Compliance | 🔴 Blocked | Tamper-evident audit trails |

**Decision gate**: All P0 work packages must be resolved before production deployment of any customer-facing AI feature.

---

## Quick Reference: Command Cheat Sheet

| Stage | Command | Input | Output |
|-------|---------|-------|--------|
| **Discover** | `/pl-use-case-explorer` | Domain name or empty | Scored candidate table |
| **Intake** | `/pl-funnel-intake` | Use-case description | 6-box canvas + 4 appendices |
| **Intake+** | `/pl-agentic-tpm` | Use-case description | 12-section canvas + 7 appendices + YAML |
| **Feasibility** | `/pl-feasibility-probe` | Use-case description | Architecture sketch + build-vs-buy |
| **Rehearse** | `/pl-rehearse` | Use-case name | Turn-based engineer simulation + scorecard |
| **DFM Review** | `/pl-dfm-review` | Part description or file | DFM evaluation report |
| **Q&A** | `/pl-ask` | Manufacturing question | Answer with source citations |
| **Strategy** | `/pl-strategy` | Topic or question | Strategic analysis |
| **Governance** | `/pl-governance` | Assessment type + scope | Compliance assessment |
| **Assess** | `/pl-assess` | Target + criteria | Combined DFM + governance |
| **Refresh KB** | `/pl-refresh-kb` | Folder (optional) | Updated cached articles |

---

## Decision Framework: Which Command When?

```
"I have a problem space but no crisp use case"
    └──► /pl-use-case-explorer

"I have a use case and need to turn it into an artifact"
    ├──► /pl-funnel-intake          (standard, fast)
    └──► /pl-agentic-tpm            (strategic, board-ready)

"The canvas says PROCEED — can we build it?"
    └──► /pl-feasibility-probe

"I need to stress-test before the real workshop"
    └──► /pl-rehearse

"We're building a physical part — is it manufacturable?"
    └──► /pl-dfm-review

"I have a manufacturing question"
    └──► /pl-ask

"I need to check compliance before shipping"
    └──► /pl-governance

"I need the full picture — DFM + governance"
    └──► /pl-assess
```

---

## Example: End-to-End Workflow

**Scenario**: You want to explore AI-powered manufacturability feedback for customers.

### Step 1 — Discover
```
/pl-use-case-explorer "customer-edge"
```
*Output*: "Manufacturability Copilot for Customers" ranks #2 with high impact, medium feasibility, Tier 1 (6–9 months).

### Step 2 — Intake
```
/pl-agentic-tpm "Manufacturability Copilot for Customers: real-time DFM feedback during design in-browser."
```
*Output*: 12-section canvas. Verdict: **PROCEED**. Adjusted ROI positive. Change cost: medium (engineers fear replacement).

### Step 3 — Feasibility
```
/pl-feasibility-probe "Manufacturability Copilot for Customers: real-time DFM feedback during design in-browser."
```
*Output*: Architecture maps to Layer 2 (Geometric & Manufacturability Analysis). Build the DFM engine, buy the CAD viewer. Data prerequisite: 10K+ annotated CAD files.

### Step 4 — Rehearse
```
/pl-rehearse "Manufacturability Copilot for Customers"
```
*Output*: Scorecard — Clarity 4, Empathy 3, Technical Depth 4, Prioritization 5, Change-Management 3. Weakness: Change-Management. Sharpen Box 7 before workshop.

### Step 5 — Deliver
- File under **WP-CAD** (strategic initiative)
- Run `/pl-governance` for EU AI Act conformity assessment
- Schedule engineering review with sharpened Box 7

---

## Governance Checkpoints

Every project must pass these gates before advancing:

| Gate | Stage | Check | Artifact |
|------|-------|-------|----------|
| **G1 — Problem Validation** | Intake | Do we have customer discovery evidence? | Box 1.5 (Agentic TPM) |
| **G2 — Value Justification** | Intake | Is Adjusted ROI > 0? | Executive Summary |
| **G3 — Technical Feasibility** | Feasibility | Can engineering commit to architecture? | Feasibility Probe output |
| **G4 — Compliance Pre-Check** | Feasibility | What's the EU AI Act risk class? | Appendix B |
| **G5 — Stakeholder Alignment** | Rehearse | Can we survive skeptical engineer pushback? | Rehearse scorecard |
| **G6 — Change Readiness** | Intake | Is workforce transformation cost acceptable? | Box 7 |
| **G7 — Governance Sign-Off** | Deliver | Has `/pl-governance` been run? | Compliance assessment |

---

## Tips for PMs

1. **Start with `/pl-use-case-explorer`** even if you think you know the answer. The ranking often surfaces better opportunities.

2. **Use `/pl-agentic-tpm` for anything that goes to the board or cross-functional leadership.** The PR-FAQ (Appendix F) alone is worth the extra time.

3. **Never skip `/pl-rehearse`.** The weakest dimension in the scorecard is almost always what kills you in the real meeting.

4. **Box 7 (Change Readiness) is not optional.** The best technical solution fails if the workforce rejects it.

5. **The YAML companion (Appendix G) feeds directly into Jira/Confluence.** Use it to bridge the gap between PM artifact and engineering backlog.

6. **If the feasibility probe says "data prerequisite: 10K+ labeled examples,"** stop and validate data availability before proceeding. This is the #1 reason AI projects fail.

7. **Governance is not a checkbox.** Run `/pl-governance` early — if you're High-risk under EU AI Act, the compliance timeline may be longer than the build timeline.

---

*Document version: 1.0 | Last updated: 2026-05-03*
