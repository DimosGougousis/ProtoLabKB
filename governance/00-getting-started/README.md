# Getting Started with Product Governance for Agentic AI

## Purpose

This guide helps you adopt the governance framework incrementally. You do not need to implement everything at once. Start where you are, with the problems you face today, and expand as your governance maturity grows.

## The Core Principle: Governance Intensity Matches Risk

Not every AI product needs the same level of governance. A low-risk internal summarization tool requires lighter governance than a customer-facing autonomous financial advisor. This framework scales with your risk profile.

The key insight: **governance is not overhead -- it is the mechanism by which you ship AI products with confidence.** Teams that invest in governance ship faster in the long run because they spend less time in crisis response, regulatory remediation, and trust recovery.

---

## Prerequisites

Before diving in, ensure your team has a basic understanding of:

1. **EU AI Act risk classification** -- The EU AI Act categorizes AI systems into four risk tiers (Unacceptable, High, Limited, Minimal). Your governance obligations depend on which tier your system falls into. If you are unsure, start with the risk classification checklist in `01-discovery-governance/`.

2. **Your AI product's scope** -- Who are the users? What decisions does the AI make? Can it act autonomously? Does it interact with customers? The answers shape which governance artifacts matter most.

3. **Your organization's current governance baseline** -- What processes do you already have? This framework integrates with existing quality management, risk management, and compliance processes rather than replacing them.

---

## Three Adoption Paths

Choose the path that matches your current situation. Each path is a valid starting point and all paths converge toward full governance maturity.

### Path A: Risk Assessment First

**Best for:** Organizations under regulatory pressure, teams deploying in regulated industries, compliance-driven adoption.

**Start with:**
1. Complete the EU AI Act risk classification for your AI system (`01-discovery-governance/eu-ai-act-risk-classification.yaml`)
2. Based on the risk tier, determine your governance intensity level
3. Conduct the ethical risk assessment (`01-discovery-governance/ethical-risk-assessment.yaml`)
4. Implement the governance checkpoints required for your risk tier
5. Expand into Development and Runtime Governance as you build

**Timeline:** 2-4 weeks to initial risk assessment, then ongoing governance integration.

**You will know it is working when:** You can articulate your AI system's risk tier, the specific governance obligations that apply, and who is accountable for each obligation.

### Path B: Eval-First (Shift-Left Testing)

**Best for:** Engineering-led teams, organizations that already have AI in production but lack systematic evaluation, teams that want to improve quality before formalizing governance.

**Start with:**
1. Read the eval-driven development guide (`02-development-governance/eval-driven-development.md`)
2. Define acceptance criteria for your AI product's core behaviors
3. Build an initial eval suite that tests for quality, safety, and fairness
4. Integrate evals into your CI/CD pipeline as mandatory gates
5. Use eval results to identify governance gaps and expand into other pillars

**Timeline:** 1-2 weeks to first eval suite, then iterative expansion.

**You will know it is working when:** No AI model change reaches production without passing an automated eval suite, and the team treats eval failures with the same urgency as test failures in traditional software.

### Path C: Full Governance (Comprehensive Adoption)

**Best for:** New AI product initiatives starting from scratch, organizations building their first customer-facing AI agent, teams with executive mandate for AI governance.

**Start with:**
1. Fill out the ML Lifecycle Canvas (`00-getting-started/ml-lifecycle-canvas.md`) for your AI product
2. Work through each pillar sequentially: Discovery, Development, Runtime, Operational
3. For each pillar, complete the core checklists and establish the required processes
4. Set up the cross-cutting concerns (RACI, glossary, templates)
5. Establish the executive reporting cadence (`06-executive/`)

**Timeline:** 4-8 weeks for initial framework deployment, then continuous improvement.

**You will know it is working when:** Every AI product has a governance profile, governance checkpoints are embedded in the development lifecycle, and there is a clear audit trail from discovery through operations.

---

## How the Four Pillars Connect

The pillars are not independent silos. They form a continuous governance chain:

```
  DISCOVERY          DEVELOPMENT          RUNTIME           OPERATIONAL
  GOVERNANCE    -->  GOVERNANCE     -->   GOVERNANCE   -->  GOVERNANCE
                                                                |
  "Should we          "Is it safe         "Is it behaving      "Is it still
   build this?"        to ship?"           correctly?"          safe over time?"
                                                                |
       ^                                                        |
       +------- Feedback loop: Operational insights inform -----+
                future Discovery decisions
```

**Key handoff points:**

| From | To | What Transfers |
|------|----|---------------|
| Discovery | Development | Risk tier, acceptance criteria, ethical boundaries, eval strategy |
| Development | Runtime | Trained/configured model, eval suite, guardrail specifications, quality bar |
| Runtime | Operational | Live system, monitoring configuration, escalation policies, SLA definitions |
| Operational | Discovery | Incident learnings, drift reports, user feedback, re-evaluation triggers |

Each pillar's artifacts reference artifacts in adjacent pillars. Follow the cross-references to see how governance decisions flow through the lifecycle.

---

## Start Here: Recommendations by Role

### Product Manager
1. Fill out the [ML Lifecycle Canvas](ml-lifecycle-canvas.md)
2. Complete the risk classification in `01-discovery-governance/`
3. Define acceptance criteria and evaluation strategy
4. Establish go/no-go gate criteria for your product

### Engineer / ML Engineer
1. Read the [eval-driven development guide](../02-development-governance/eval-driven-development.md)
2. Build your first eval suite before building features
3. Understand the guardrail architecture in `03-runtime-governance/`
4. Set up monitoring hooks as part of your deployment

### Compliance Officer / Risk Manager
1. Start with the [EU AI Act risk classification](../01-discovery-governance/eu-ai-act-risk-classification.yaml)
2. Map existing compliance processes to the four pillars
3. Identify gaps between current controls and framework requirements
4. Establish the audit trail and evidence requirements

### Executive / Board Member
1. Read the executive summaries in `06-executive/`
2. Understand the governance investment framework
3. Review the risk dashboard template
4. Establish the governance reporting cadence

### Security Engineer
1. Focus on `03-runtime-governance/` for prompt injection defense and safety rails
2. Review the incident response playbooks in `04-operational-governance/`
3. Understand the permission boundary model for agent delegation
4. Integrate security monitoring with governance observability

---

## Framework Navigation

Not sure where to go next? Use the [Framework Navigation Guide](framework-navigation-guide.md) -- a decision-tree style reference that maps common scenarios to specific framework artifacts.

---

## What Success Looks Like

A mature governance implementation has these characteristics:

1. **Every AI product has a governance profile** -- risk tier, governance intensity, accountable roles, and a living set of governance artifacts
2. **Governance is embedded, not bolted on** -- checkpoints are part of the development workflow, not separate approval processes
3. **Evaluations run continuously** -- from development through production, with clear thresholds and automatic escalation
4. **Audit trails are complete** -- any decision can be traced from business rationale through risk assessment to production behavior
5. **Incidents trigger improvement** -- operational learnings feed back into governance refinement, not just incident closure
6. **Teams understand why** -- governance is seen as enabling fast, confident delivery rather than bureaucratic overhead

---

*Next step: Fill out the [ML Lifecycle Canvas](ml-lifecycle-canvas.md) for your AI product, or use the [Framework Navigation Guide](framework-navigation-guide.md) to find exactly what you need.*
