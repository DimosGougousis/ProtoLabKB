# Product Governance for Agentic AI Workflows

**A unified governance framework bridging Responsible AI, AI Product Management, and LLMOps guardrails for enterprise agentic systems.**

---

## The Problem

Organizations deploying AI agents face a fragmented governance landscape. Responsible AI frameworks address ethics but ignore production operations. MLOps tooling handles deployment but lacks product-level risk assessment. Compliance checklists satisfy regulators but fail to prevent the real-world harms that emerge when autonomous agents interact with customers, make decisions, and delegate tasks to other agents.

No single framework today unifies these three concerns:

1. **Responsible AI** -- ethical principles, fairness, transparency, accountability
2. **AI Product Management** -- discovery, validation, evaluation, lifecycle management
3. **LLMOps Guardrails** -- runtime safety, prompt security, output filtering, observability

This repository fills that gap. It provides a comprehensive, actionable governance framework designed specifically for **business AI agents**: customer-facing chatbots, autonomous decision-makers, multi-agent orchestration systems, and any AI product that acts on behalf of an organization.

---

## The Four Governance Pillars

Governance is not a single checkpoint. It spans the entire lifecycle of an AI product, from the first idea to decommissioning. This framework organizes governance into four pillars, each addressing a distinct phase and set of concerns:

```
+---------------------------+---------------------------+
|                           |                           |
|  1. DISCOVERY GOVERNANCE  |  2. DEVELOPMENT           |
|                           |     GOVERNANCE             |
|  What should we build?    |  How do we build it        |
|  Is it ethical?           |  safely?                   |
|  Is it the right problem? |  Is it biased or unfair?   |
|                           |                           |
|  - Problem validation     |  - Eval-driven development |
|  - EU AI Act risk tiers   |  - Bias & fairness testing |
|  - Stakeholder analysis   |  - Red-teaming protocols   |
|  - Ethical review boards  |  - Model cards & data      |
|  - Go/no-go gates         |    sheets                  |
|                           |  - Quality gates           |
+---------------------------+---------------------------+
|                           |                           |
|  3. RUNTIME GOVERNANCE    |  4. OPERATIONAL            |
|                           |     GOVERNANCE             |
|  How do we control it     |  How do we secure and      |
|  in real-time?            |  monitor it?               |
|                           |                           |
|  - Guardrails & safety    |  - Incident response       |
|    rails                  |  - Audit trails            |
|  - Prompt injection       |  - Drift detection         |
|    defense                |  - Compliance reporting    |
|  - Output filtering       |  - Cost governance         |
|  - Human escalation       |  - Decommissioning         |
|  - Permission boundaries  |    procedures              |
|                           |                           |
+---------------------------+---------------------------+
```

| Pillar | Core Question | Key Artifacts | Directory |
|--------|--------------|---------------|-----------|
| **Discovery** | What should we build? Is it ethical? | Risk assessments, ethical reviews, opportunity canvases | `01-discovery-governance/` |
| **Development** | How do we build it safely? Is it biased? | Eval suites, bias audits, model cards, quality gates | `02-development-governance/` |
| **Runtime** | How do we control it in production? | Guardrail configs, escalation policies, safety rails | `03-runtime-governance/` |
| **Operational** | How do we secure and monitor it long-term? | Incident playbooks, audit templates, drift dashboards | `04-operational-governance/` |

---

## Key Differentiators

### Governance for Agentic AI, Not Just Models

Traditional AI governance treats a model as a static artifact to be tested and deployed. Agentic AI is different. Agents make decisions, take actions, delegate to sub-agents, and interact with real users in unpredictable ways. This framework addresses:

- **Delegation chains** -- Who is accountable when Agent A delegates to Agent B, which calls Tool C?
- **Permission boundaries** -- What is an agent allowed to do? What requires human approval?
- **Multi-agent orchestration** -- How do you govern a system of cooperating agents?
- **Autonomous decision-making** -- When should an agent act autonomously vs. escalate to a human?
- **Machine Identity (NHI)** -- Treating agents as first-class IAM citizens with least-privilege scopes and credential lifecycle management
- **Human oversight models** -- HITL (Human-in-the-Loop), HOTL (Human-on-the-Loop), and HOTA (Human-out-of-the-Loop Autonomy) scaled by risk tier
- **Agent Fleet Operations** -- Fleet-wide visibility into agent health, KPIs/SLAs, cost governance, and MLOps lifecycle

### Eval-Driven Development (Shift-Left Testing for AI)

Evaluations are not an afterthought. They are a first-class concern woven into every pillar:

- **Discovery**: Define acceptance criteria and evaluation strategy before writing a single line of code
- **Development**: Build eval suites alongside features; no merge without passing evals
- **Runtime**: Continuous evaluation of live agent behavior against safety and quality thresholds
- **Operational**: Periodic re-evaluation to detect drift, degradation, and emerging failure modes

This is the AI equivalent of Test-Driven Development: define what "good" looks like first, then build to meet that bar.

### Two-System Architecture

This framework implements a two-system architecture for comprehensive agent governance:

```
+================================================================+
|  AGENT FLEET COMMAND DASHBOARD                                  |
|  (Operational Visibility Layer)                                 |
|  Fleet Overview | Agent Health | KPIs & SLAs | Risk Mitigations|
|  MLOps Status | Governance Compliance | Cost Management         |
+================================================================+
         |  reads from / enforced by
         v
+================================================================+
|  AGENTIC GOVERNANCE FRAMEWORK                                   |
|  (Policy + Process + MLOps Backbone)                            |
|  Permission Boundaries | Safety Patterns | Delegation Chains   |
|  HITL/HOTL/HOTA | Inter-Agent Protocols | Eval Pipelines       |
+================================================================+
```

### Designed for Regulated Industries

This framework is built with regulated FinTech in mind -- specifically the regulatory requirements of:

- **EU AI Act** -- Risk-tiered governance obligations for AI systems
- **DNB (De Nederlandsche Bank)** guidelines -- Supervisory expectations for AI in financial services
- **DORA (Digital Operational Resilience Act)** -- ICT risk management for financial entities
- **ISO/IEC 42001** -- AI Management System standard with PDCA model

However, the framework is applicable to any enterprise deploying AI agents, whether in healthcare, insurance, legal, or other regulated or risk-sensitive domains.

---

## Quick Navigation

| Directory | Purpose |
|-----------|---------|
| [`00-getting-started/`](00-getting-started/) | Adoption guide, lifecycle canvas, framework navigation |
| [`01-discovery-governance/`](01-discovery-governance/) | Risk assessment, ethical review, opportunity validation |
| [`02-development-governance/`](02-development-governance/) | Eval-driven development, bias testing, quality gates |
| [`03-runtime-governance/`](03-runtime-governance/) | Guardrails, agent fleet operations, HITL/HOTL/HOTA, permission boundaries |
| [`04-operational-governance/`](04-operational-governance/) | Monitoring, incident response, audit, decommissioning |
| [`05-cross-cutting/`](05-cross-cutting/) | Glossary, RACI matrices, templates shared across pillars |
| [`06-executive/`](06-executive/) | Board-level summaries, dashboards, investment frameworks |
| [`07-enterprise-implementation/`](07-enterprise-implementation/) | Rollout playbooks, organizational change, tooling guides |
| [`docs/plans/`](docs/plans/) | Implementation plans and design decisions |

---

## Source Frameworks

This repository synthesizes and extends three complementary frameworks:

1. **SAFEST Framework** -- A structured approach to AI safety covering Security, Accountability, Fairness, Explainability, Sustainability, and Transparency. Provides the checklist methodology and regulatory mapping used throughout this repo.

2. **AI Product Development Toolkit** -- A practical toolkit for AI product managers covering discovery, validation, evaluation, and lifecycle management. Provides the product-centric perspective and the eval-driven development methodology.

3. **Superpowers Development Methodology** -- A rigorous software development methodology emphasizing test-driven development, systematic debugging, and verification-before-completion. Provides the engineering discipline and workflow structure.

---

## Getting Started

New to this framework? Start here:

1. **Read the adoption guide**: [`00-getting-started/README.md`](00-getting-started/README.md) -- Choose an adoption path that fits your situation
2. **Fill out the lifecycle canvas**: [`00-getting-started/ml-lifecycle-canvas.md`](00-getting-started/ml-lifecycle-canvas.md) -- Map your AI product in a single page
3. **Navigate to what you need**: [`00-getting-started/framework-navigation-guide.md`](00-getting-started/framework-navigation-guide.md) -- Find the right artifact for your current challenge
4. **Learn the language**: [`05-cross-cutting/glossary.md`](05-cross-cutting/glossary.md) -- Unified terminology across governance, AI/ML, LLM, and regulatory domains

If you are a:
- **Product Manager** -- Start with Discovery Governance (`01-discovery-governance/`)
- **Engineer** -- Start with Development Governance (`02-development-governance/`)
- **Compliance Officer** -- Start with the risk classification and regulatory mappings in Discovery Governance
- **Executive** -- Start with the executive summaries (`06-executive/`)

---

## Contributing

This is a living framework. Contributions follow the governance principles it espouses:

1. Propose changes via pull request with a clear rationale
2. New governance artifacts must include: purpose, when to use, who is responsible, and regulatory basis
3. YAML checklists follow the SAFEST template pattern (see `CLAUDE.md` for details)
4. Cross-reference related files in other pillars when adding or modifying content

---

## License

MIT License. See [LICENSE](LICENSE) for details.

Use this framework freely. Adapt it to your organization. Share improvements back.

---

*Built for teams who believe that governing AI agents is not a compliance burden but a competitive advantage.*
