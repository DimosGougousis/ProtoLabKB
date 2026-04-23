# Technical Product Manager's Guide
## Using the Strategy Agent as Your Copilot

**Version:** 1.0  
**Last Updated:** April 23, 2026  
**For:** Technical Product Managers at ProtoLabs

---

## Table of Contents

1. [Introduction](#introduction)
2. [Quick Start](#quick-start)
3. [The Strategy Agent: Your Strategic Copilot](#the-strategy-agent-your-strategic-copilot)
4. [Use Case Library](#use-case-library)
5. [Workflow Patterns](#workflow-patterns)
6. [Command Reference](#command-reference)
7. [Best Practices](#best-practices)
8. [Troubleshooting](#troubleshooting)

---

## Introduction

As a Technical Product Manager (TPM), you constantly evaluate new ideas, assess market opportunities, and guide product development. The **Strategy Agent** (`trends-strategy`) is your AI copilot for strategic analysis, leveraging MIT Sloan's five lenses to provide structured, evidence-based guidance.

### What This Guide Covers

- How to invoke the Strategy Agent for different scenarios
- Real-world use cases with example prompts
- Multi-agent workflows that combine strategy with manufacturing analysis
- Best practices for getting the most valuable insights

### Who Should Use This

- **Technical Product Managers** evaluating new product ideas
- **Engineering Managers** assessing technology adoption
- **Innovation Leaders** exploring market opportunities
- **Strategy Teams** conducting competitive analysis

---

## Quick Start

### 1. Basic Invocation

```
/pl-ask "[Your strategic question]"
```

The router automatically detects strategic keywords and routes to the Strategy Agent.

### 2. Strategic Keywords

The following keywords trigger the Strategy Agent:

| Category | Keywords |
|----------|----------|
| **Trends** | trend, innovation, industry 4.0, digital transformation |
| **Strategy** | strategy, competitive advantage, market positioning |
| **MIT Frameworks** | delta model, platform leadership, dynamic capabilities, transient advantage |
| **Analysis** | evaluate, assess, compare, recommend, should we |

### 3. Example Quick Prompts

```
/pl-ask "What are the latest trends in additive manufacturing for 2026?"
/pl-ask "Apply the Delta Model to our CNC machining services"
/pl-ask "Should we build AI capabilities in-house or partner?"
/pl-ask "Analyze our competitive position using Platform Leadership"
```

---

## The Strategy Agent: Your Strategic Copilot

### What Makes It Different

Unlike generic AI assistants, the Strategy Agent is **grounded in MIT Sloan's strategic frameworks** and **ProtoLabs manufacturing expertise**. It doesn't just give opinions—it applies proven strategic lenses to your specific situation.

### The Five Lenses

| Lens | Core Question | When to Use |
|------|---------------|-------------|
| **Delta Model** | How do we bond with customers? | Customer strategy, positioning, differentiation |
| **Platform Leadership** | How do we orchestrate ecosystems? | Partnership strategy, API/platform decisions |
| **Dynamic Capabilities** | How do we adapt to change? | Technology adoption, organizational agility |
| **Simple Rules** | What guides our decisions? | Operational strategy, decision frameworks |
| **Transient Advantage** | How do we compete when advantages are temporary? | Innovation strategy, market timing |

### How It Works

```
Your Question
     │
     ▼
┌─────────────────────────┐
│  Strategy Agent Loads   │
│  MIT Sloan KB Articles  │
│  + Manufacturing Trends │
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────────┐
│  Applies Relevant Lens    │
│  (Delta, Platform, etc.)│
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────────┐
│  Synthesizes Analysis   │
│  with Source Citations  │
└──────────┬──────────────┘
           │
           ▼
    Strategic Recommendation
```

---

## Use Case Library

### Use Case 1: New Product Introduction (NPI)

**Scenario:** You're launching a new manufacturing service and need strategic guidance.

**Prompt:**
```
/pl-ask "We're considering launching a metal 3D printing service for aerospace 
components. Use the Delta Model to analyze how we should position this offering 
and what customer bonding strategies would be most effective."
```

**What the Agent Does:**
1. Loads aerospace and 3D printing trend articles
2. Applies Delta Model (Best Product, Total Solutions, System Lock-in)
3. Analyzes competitive positioning
4. Recommends customer bonding strategy

**Expected Output:**
- Strategic positioning recommendation
- Customer segmentation analysis
- Competitive differentiation strategy
- Implementation roadmap

---

### Use Case 2: Technology Adoption Decision

**Scenario:** You're deciding whether to adopt AI for quoting.

**Prompt:**
```
/pl-ask "Should we build an AI-powered quoting system in-house or partner with 
a vendor? Apply the Build/Buy/Partner framework and Dynamic Capabilities lens 
from MIT Sloan."
```

**What the Agent Does:**
1. Loads AI implementation risks and governance articles
2. Applies Build/Buy/Partner framework
3. Uses Dynamic Capabilities (sensing, seizing, transforming)
4. Evaluates strategic fit

**Expected Output:**
- Build/Buy/Partner recommendation
- Risk assessment
- Capability gap analysis
- Implementation timeline

---

### Use Case 3: Competitive Analysis

**Scenario:** You're analyzing competitive threats.

**Prompt:**
```
/pl-ask "A new competitor has entered the market with a digital manufacturing 
platform that connects customers to a network of suppliers. Apply Platform 
Leadership analysis to understand their strategy and how we should respond."
```

**What the Agent Does:**
1. Loads platform leadership and industry 4.0 articles
2. Applies Platform Leadership four levers
3. Analyzes ecosystem dynamics
4. Recommends competitive response

**Expected Output:**
- Platform strategy analysis
- Ecosystem threat assessment
- Response options (scope, technology, relationships, organization)
- Strategic recommendations

---

### Use Case 4: Innovation Portfolio

**Scenario:** You're prioritizing innovation initiatives.

**Prompt:**
```
/pl-ask "We have three innovation initiatives: (1) AI-powered design 
recommendations, (2) blockchain supply chain tracking, (3) AR/VR customer 
visualization. Use the Transient Advantage framework to prioritize these 
initiatives."
```

**What the Agent Does:**
1. Loads innovation trends and AI governance articles
2. Applies Transient Advantage framework
3. Evaluates each initiative on competitive sustainability
4. Prioritizes based on strategic fit

**Expected Output:**
- Initiative scoring
- Priority ranking
- Resource allocation recommendations
- Timeline suggestions

---

### Use Case 5: Multi-Agent Workflow (Full NPI)

**Scenario:** Complete new product introduction with CAD file.

**Prompt:**
```
/pl-cad-review bracket.step --vertical aerospace
```

**What Happens:**
1. **CAD Parser Agent** parses STEP file
2. **2D Generator** creates orthographic views
3. **3D Generator** creates interactive viewer
4. **Feature Detector** identifies holes, pockets, etc.
5. **DFM Pre-Checker** flags issues
6. **Router** directs to CNC + Aerospace agents
7. **Combined Report** with images + analysis

---

## Command Reference

### Strategy-Only Commands

```bash
# General strategic question
/pl-ask "What are the key trends in additive manufacturing for 2026?"

# Apply specific MIT framework
/pl-ask "Apply the Delta Model to our CNC machining services positioning"

# Technology adoption decision
/pl-ask "Should we build AI capabilities in-house or partner?"

# Competitive analysis
/pl-ask "Analyze [competitor] using Platform Leadership framework"

# Innovation prioritization
/pl-ask "Prioritize our innovation initiatives using Transient Advantage"
```

### CAD + Strategy Commands

```bash
# Parse CAD and get strategic analysis
/pl-cad-review part.step

# Parse with process hint
/pl-cad-review part.step --process cnc

# Parse with vertical for compliance
/pl-cad-review part.step --vertical aerospace

# Parse with material
/pl-cad-review part.step --material aluminum-6061

# Full options
/pl-cad-review part.step \
  --process cnc-machining \
  --vertical aerospace \
  --material titanium \
  --output ./reports/
```

### Multi-Agent Workflows

```bash
# Strategy + Manufacturing analysis
/pl-ask "We're considering entering the medical device market. 
What does the Delta Model say about our positioning, and what 
manufacturing capabilities do we need?"

# Strategy + CAD + Manufacturing
/pl-cad-review implant.step --vertical medical
"Also analyze our competitive position in medical using 
Platform Leadership framework"
```

---

## Best Practices

### 1. Be Specific

**❌ Vague:**
```
/pl-ask "What should we do?"
```

**✅ Specific:**
```
/pl-ask "Should we build an AI quoting system in-house or partner? 
Apply the Build/Buy/Partner framework."
```

### 2. Provide Context

**❌ No Context:**
```
/pl-ask "Analyze our strategy"
```

**✅ With Context:**
```
/pl-ask "We're a $50M manufacturing services company with strengths 
in CNC and 3D printing. A competitor just raised $100M for an 
AI-powered manufacturing platform. Apply Platform Leadership to 
analyze their strategy and our response options."
```

### 3. Request Specific Frameworks

**❌ Generic:**
```
/pl-ask "How do we compete?"
```

**✅ Framework-Specific:**
```
/pl-ask "How do we compete? Apply the Delta Model to analyze 
our customer bonding options: Best Product, Total Customer 
Solutions, or System Lock-in."
```

### 4. Chain Multiple Agents

```
# Step 1: Strategy
/pl-ask "Should we enter the aerospace market? Apply Dynamic 
Capabilities to assess if we can adapt."

# Step 2: CAD Analysis (if you have a part)
/pl-cad-review bracket.step --vertical aerospace

# Step 3: Manufacturing Q&A
/pl-ask "What AS9100 requirements apply to CNC machined 
aerospace brackets?"
```

### 5. Iterate and Refine

**First attempt:**
```
/pl-ask "Analyze our strategy"
```

**Refined:**
```
/pl-ask "Analyze our competitive position in on-demand manufacturing 
using the Delta Model. We're considering three strategic options: 
(1) compete on price, (2) compete on speed/quality, (3) build a 
platform ecosystem. Evaluate each option."
```

---

## Troubleshooting

### Issue: "Strategy Agent not invoked"

**Symptoms:** Your strategic question is routed to a different agent.

**Solution:**
- Include explicit strategic keywords: "strategy", "Delta Model", "Platform Leadership"
- Use `/pl-ask` not `/pl-dfm-review` for strategic questions
- Be explicit: "Apply the [framework] to analyze..."

### Issue: "CAD file not recognized"

**Symptoms:** CAD file upload fails or is treated as text.

**Solution:**
- Use `/pl-cad-review` command specifically
- Ensure file has correct extension: `.step`, `.stp`, `.stl`, `.obj`
- Check file size (max 100MB)
- Verify file is not corrupted

### Issue: "Analysis seems generic"

**Symptoms:** Response lacks specific insights or actionable recommendations.

**Solution:**
- Provide more context about your business situation
- Specify which MIT Sloan lens to apply
- Ask follow-up questions to drill deeper
- Request specific recommendations, not just analysis

### Issue: "Want to combine strategy + manufacturing"

**Symptoms:** Need both strategic and manufacturing analysis.

**Solution:**
```
# Option 1: Sequential
/pl-ask "Strategic question..."
/pl-cad-review part.step

# Option 2: In one prompt (router will coordinate)
/pl-ask "Strategic question about [part]..." 
# Then provide CAD file in follow-up

# Option 3: Explicit multi-agent
/pl-ask "As a strategic analysis using Platform Leadership, 
should we build a manufacturing platform? Then analyze this 
part for manufacturability: [CAD file]"
```

---

## Appendix: MIT Sloan Framework Quick Reference

### Delta Model

**Core Question:** How do we bond with customers?

| Position | Strategy | When to Use |
|----------|----------|-------------|
| **Best Product** | Compete on features, price, performance | Commodity markets, clear differentiators |
| **Total Customer Solutions** | Deep customer relationships, customization | Complex needs, high switching costs |
| **System Lock-in** | Ecosystem dominance, network effects | Platform businesses, two-sided markets |

**Example Prompt:**
```
/pl-ask "Apply the Delta Model to our CNC machining business. 
Should we position as Best Product (speed/quality), Total 
Customer Solutions (DFM expertise), or System Lock-in 
(digital platform)?"
```

### Platform Leadership

**Core Question:** How do we orchestrate ecosystems?

| Lever | Decision | Key Considerations |
|-------|----------|-------------------|
| **Scope** | What belongs on platform vs. outside? | Core vs. complementary |
| **Product Technology** | How do complements interface? | APIs, standards, tools |
| **External Relationships** | How to manage ecosystem? | Incentives, governance |
| **Internal Organization** | How to structure for platform success? | Teams, metrics, culture |

**Example Prompt:**
```
/pl-ask "We're building a manufacturing services platform. 
Apply Platform Leadership to analyze: (1) What capabilities 
should be on-platform vs. off-platform? (2) What APIs do 
we need? (3) How do we incentivize suppliers?"
```

### Dynamic Capabilities

**Core Question:** How do we adapt to change?

| Capability | Activities | Manufacturing Application |
|------------|------------|---------------------------|
| **Sensing** | Scan, learn, interpret | Monitor new technologies, customer trends |
| **Seizing** | Invest, innovate, execute | Adopt new processes, launch services |
| **Transforming** | Reconfigure, integrate, divest | Restructure for new capabilities |

**Example Prompt:**
```
/pl-ask "AI is disrupting manufacturing. Apply Dynamic 
Capabilities to assess: (1) How well do we sense AI 
opportunities? (2) Can we seize them? (3) What 
transformation is needed?"
```

### Simple Rules

**Core Question:** What guides our decisions?

| Rule Type | Purpose | Example |
|-----------|---------|---------|
| **Boundary** | Which opportunities to pursue | "Only enter markets where we can be top 3" |
| **Prioritizing** | Rank competing opportunities | "Prioritize speed over cost for prototypes" |
| **Timing** | When to act | "Launch when 3 customers commit" |
| **Exit** | When to stop | "Exit if ROI < 15% after 2 years" |

**Example Prompt:**
```
/pl-ask "We need simple rules for deciding which new 
manufacturing technologies to adopt. What boundary, 
prioritizing, timing, and exit rules should we use?"
```

### Transient Advantage

**Core Question:** How do we compete when advantages are temporary?

| Strategy | When to Use | Tactics |
|----------|-------------|---------|
| **Continuous Innovation** | Fast-moving markets | Rapid iteration, experimentation |
| **Strategic Pivoting** | Market shifts | Reallocate resources quickly |
| **Portfolio Approach** | Uncertain outcomes | Multiple bets, stage-gates |

**Example Prompt:**
```
/pl-ask "The manufacturing services market is evolving 
rapidly. Apply Transient Advantage to develop our 
competitive strategy for a world where advantages are 
temporary."
```

---

## Summary

The Strategy Agent is your copilot for:

✅ **Strategic Analysis** — Apply MIT Sloan frameworks to real problems  
✅ **Decision Support** — Get structured recommendations with trade-offs  
✅ **Trend Monitoring** — Stay current on manufacturing innovations  
✅ **Multi-Agent Workflows** — Combine strategy with CAD + DFM analysis  

**Remember:** The agent is most effective when you:
- Provide specific context about your situation
- Explicitly request specific frameworks
- Ask follow-up questions to drill deeper
- Combine with other agents for comprehensive analysis

---

*Happy strategizing! 🎯*
