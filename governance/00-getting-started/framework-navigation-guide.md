# Framework Navigation Guide — ProtoLabs Agentic DFM

## Purpose

This guide maps common scenarios to specific framework artifacts for the ProtoLabs Product Office AI agent system. Use it when you know what you need to accomplish but are not sure where to find the relevant guidance, checklist, or template for governing DFM (Design for Manufacturing) agents in regulated manufacturing verticals.

## When to Use

Anytime you have a specific governance question or task and want to find the right artifact quickly. This is your "I need to..." reference.

## Who Is Responsible

All team members. This guide is a navigation aid, not a governance artifact itself.

## Regulatory Basis

Best practice -- efficient navigation reduces governance friction and increases adoption. This guide is tailored for the ProtoLabs manufacturing domain (CNC machining, injection molding, sheet metal, 3D printing, materials selection, and regulated verticals: aerospace, medical, automotive).

---

## Decision Tree: "I need to..."

### Starting a New AI Product

| I need to... | Go to... | Pillar |
|-------------|----------|--------|
| Scope an AI product from scratch | [`00-getting-started/ml-lifecycle-canvas.md`](ml-lifecycle-canvas.md) | Getting Started |
| Classify my AI system's risk level under the EU AI Act | `01-discovery-governance/eu-ai-act-risk-classification.yaml` | Discovery |
| Conduct an ethical risk assessment | `01-discovery-governance/ethical-risk-assessment.yaml` | Discovery |
| Decide whether to build this AI product at all (go/no-go) | `01-discovery-governance/discovery-gate-checklist.yaml` | Discovery |
| Identify stakeholders and their concerns | `01-discovery-governance/stakeholder-analysis.md` | Discovery |
| Understand what governance intensity my product requires | [`00-getting-started/ml-lifecycle-canvas.md`](ml-lifecycle-canvas.md) (Section 5) | Getting Started |
| Define my AI product's governance profile | `01-discovery-governance/governance-profile-template.md` | Discovery |

### Building and Testing an AI Product

| I need to... | Go to... | Pillar |
|-------------|----------|--------|
| Set up automated evals for my AI product | `02-development-governance/eval-driven-development.md` | Development |
| Test my AI system for bias and fairness | `02-development-governance/bias-fairness-testing.md` | Development |
| Red-team my AI agent for safety vulnerabilities | `02-development-governance/red-teaming-protocol.md` | Development |
| Create a model card for my AI system | `02-development-governance/model-card-template.md` | Development |
| Document my training data governance | `02-development-governance/data-sheet-template.md` | Development |
| Define quality gates for my development pipeline | `02-development-governance/quality-gate-checklist.yaml` | Development |
| Validate that my product meets acceptance criteria before deployment | `02-development-governance/deployment-readiness-checklist.yaml` | Development |

### Deploying and Running an AI Product

| I need to... | Go to... | Pillar |
|-------------|----------|--------|
| Configure guardrails for my AI agent | `03-runtime-governance/guardrail-configuration.md` | Runtime |
| Defend against prompt injection attacks | `03-runtime-governance/prompt-security.md` | Runtime |
| Set up output filtering and safety rails | `03-runtime-governance/safety-rail-framework.md` | Runtime |
| Define when my agent should escalate to a human | `03-runtime-governance/human-escalation-policy.md` | Runtime |
| Govern a customer-facing chatbot | `03-runtime-governance/multi-agent-governance-framework.md` | Runtime |
| Set permission boundaries for agent actions | `03-runtime-governance/permission-boundary-model.md` | Runtime |
| Govern a multi-agent orchestration system | `03-runtime-governance/multi-agent-governance-framework.md` | Runtime |
| Define the delegation chain for my agent system | `03-runtime-governance/delegation-chain-governance.md` | Runtime |

### Operating and Maintaining an AI Product

| I need to... | Go to... | Pillar |
|-------------|----------|--------|
| Set up monitoring for my AI product in production | `04-operational-governance/monitoring-framework.md` | Operational |
| Respond to an AI incident | `04-operational-governance/incident-response-playbook.md` | Operational |
| Conduct a post-incident review | `04-operational-governance/post-incident-review-template.md` | Operational |
| Detect model drift or performance degradation | `04-operational-governance/drift-detection.md` | Operational |
| Prepare for a governance audit | `04-operational-governance/audit-trail-template.md` | Operational |
| Generate a compliance report | `04-operational-governance/compliance-reporting-template.md` | Operational |
| Govern AI system costs | `04-operational-governance/cost-governance.md` | Operational |
| Decommission an AI system safely | `04-operational-governance/decommissioning-checklist.yaml` | Operational |
| Conduct a periodic governance review | `04-operational-governance/periodic-review-checklist.yaml` | Operational |

### Cross-Cutting and Organizational Concerns

| I need to... | Go to... | Pillar |
|-------------|----------|--------|
| Look up a governance or AI term | [`05-cross-cutting/glossary.md`](../05-cross-cutting/glossary.md) | Cross-cutting |
| Define roles and responsibilities for governance | `05-cross-cutting/raci-matrix-template.md` | Cross-cutting |
| Understand the three lines of defense model | `05-cross-cutting/three-lines-of-defense.md` | Cross-cutting |
| Find a reusable template | `05-cross-cutting/` (browse directory) | Cross-cutting |

### Executive and Strategic

| I need to... | Go to... | Pillar |
|-------------|----------|--------|
| Brief the board on AI governance | `06-executive/board-summary-template.md` | Executive |
| Build a business case for governance investment | `06-executive/governance-investment-framework.md` | Executive |
| Review the AI portfolio risk dashboard | `06-executive/risk-dashboard-template.md` | Executive |
| Understand governance maturity levels | `06-executive/governance-maturity-model.md` | Executive |

### Enterprise Implementation

| I need to... | Go to... | Pillar |
|-------------|----------|--------|
| Roll out governance across the organization | `07-enterprise-implementation/rollout-playbook.md` | Enterprise |
| Manage organizational change for AI governance | `07-enterprise-implementation/change-management.md` | Enterprise |
| Select and configure governance tooling | `07-enterprise-implementation/tooling-guide.md` | Enterprise |
| Train teams on governance practices | `07-enterprise-implementation/training-curriculum.md` | Enterprise |

### ProtoLab-Specific Governance

| I need to... | Go to... | Pillar |
|-------------|----------|--------|
| Understand the risk profile of our 10 DFM agents | `../protolabs/agent-risk-registry.yaml` | ProtoLab |
| Check SAFEST compliance coverage for an agent | `../protolabs/safest-coverage-matrix.md` | ProtoLab |
| Protect customer CAD files and IP | `../protolabs/customer-cad-ip-protection-guardrail.md` | ProtoLab |
| Validate DFM accuracy against the golden fixture | `../protolabs/dfm-accuracy-eval-suite.yaml` | ProtoLab |
| Enforce source citation for every agent claim | `../protolabs/source-grounding-data-contract.yaml` | ProtoLab |
| Check when a compliance KB should be loaded | `../protolabs/manufacturing-compliance-routing.md` | ProtoLab |
| Run adversarial tests on DFM agents | `../protolabs/red-team-playbook-dfm-agents.md` | ProtoLab |
| Verify KB article freshness | `../protolabs/kb-freshness-provenance-contract.md` | ProtoLab |
| Find the KILLSWITCH for a specific agent | `../protolabs/agents/<agent-id>/KILLSWITCH.md` | ProtoLab |
| Review an agent's skill manifest | `../protolabs/agents/<agent-id>/skill-manifest.yaml` | ProtoLab |
| Check board-level AI risk dashboard | `../dashboards/board.html` | Executive |

---

## Common Scenarios (End-to-End)

These scenarios span multiple pillars. Follow the sequence for a complete governance approach.

### Scenario 1: "We are launching a new customer-facing AI chatbot"

1. Fill out the [ML Lifecycle Canvas](ml-lifecycle-canvas.md) to scope the product
2. Classify the risk tier: `01-discovery-governance/eu-ai-act-risk-classification.yaml`
3. Conduct the ethical risk assessment: `01-discovery-governance/ethical-risk-assessment.yaml`
4. Pass the Discovery Gate: `01-discovery-governance/discovery-gate-checklist.yaml`
5. Define the eval strategy: `02-development-governance/eval-driven-development.md`
6. Red-team the chatbot: `02-development-governance/red-teaming-protocol.md`
7. Configure guardrails: `03-runtime-governance/guardrail-configuration.md`
8. Set up human escalation: `03-runtime-governance/human-escalation-policy.md`
9. Define permission boundaries: `03-runtime-governance/permission-boundary-model.md`
10. Deploy with monitoring: `04-operational-governance/monitoring-framework.md`
11. Prepare incident response: `04-operational-governance/incident-response-playbook.md`

### Scenario 2: "We have AI in production but no governance framework"

1. Start with an inventory: list all AI systems currently in production
2. For each system, fill out the [ML Lifecycle Canvas](ml-lifecycle-canvas.md)
3. Classify risk tiers: `01-discovery-governance/eu-ai-act-risk-classification.yaml`
4. Prioritize: address highest-risk systems first
5. Build eval suites: `02-development-governance/eval-driven-development.md`
6. Retrofit monitoring: `04-operational-governance/monitoring-framework.md`
7. Establish incident response: `04-operational-governance/incident-response-playbook.md`
8. Schedule periodic reviews: `04-operational-governance/periodic-review-checklist.yaml`

### Scenario 3: "We are preparing for an EU AI Act compliance audit"

1. Classify all AI systems by risk tier: `01-discovery-governance/eu-ai-act-risk-classification.yaml`
2. For high-risk systems, verify all Article 9-15 requirements are met
3. Gather evidence using the audit trail template: `04-operational-governance/audit-trail-template.md`
4. Verify model cards and data sheets exist: `02-development-governance/model-card-template.md`
5. Verify monitoring and incident response are in place: `04-operational-governance/`
6. Generate compliance report: `04-operational-governance/compliance-reporting-template.md`
7. Prepare board briefing: `06-executive/board-summary-template.md`

### Scenario 4: "Our AI agent made a bad decision and we need to respond"

1. Activate incident response: `04-operational-governance/incident-response-playbook.md`
2. Assess severity and scope
3. If needed, trigger rollback per the deployment strategy in the Lifecycle Canvas
4. Conduct post-incident review: `04-operational-governance/post-incident-review-template.md`
5. Update eval suite to cover the failure mode: `02-development-governance/eval-driven-development.md`
6. Update guardrails if a runtime control was missing: `03-runtime-governance/guardrail-configuration.md`
7. Update risk assessment if a new harm scenario was discovered: `01-discovery-governance/ethical-risk-assessment.yaml`

### Scenario 5: "A customer wants a DFM review of a complex machined part"

1. Determine process: Use `../CLAUDE.md` routing keywords → CNC Machining Agent
2. Check regulatory mode: Does the part description include ITAR/EAR/aerospace/medical keywords?
3. Fill out the ML Lifecycle Canvas for this specific review session
4. Load the CNC Machining agent skill manifest from `../protolabs/agents/cnc-machining/`
5. Verify KB freshness: Is the CNC machining KB within the 90-day SLA?
6. Execute DFM review with source citation per `../protolabs/source-grounding-data-contract.yaml`
7. If regulated mode activated, include compliance KB citations (ITAR, AS9100D, etc.)
8. Log the review for audit trail

### Scenario 6: "A customer uploaded a CAD file with ITAR-controlled features"

1. The `{{#regulated}}` pattern detects ITAR keywords in the part description
2. The CAD/IP protection guardrail activates: `../protolabs/customer-cad-ip-protection-guardrail.md`
3. Compliance KBs load: `../knowledge/cnc-machining/itar-ear-compliance.md`
4. Agent output is flagged for human review before any response to customer
5. Incident logged per `04-operational-governance/templates/ai-incident-report.md`
6. Post-incident review determines if the upload should have been blocked earlier in the intake flow
7. Update intake guardrails if a control gap was identified

### Scenario 7: "The materials-selection agent recommended a non-compliant material"

1. Activate incident response: `04-operational-governance/incident-response-playbook.md`
2. Check the agent's skill manifest: Was the compliance KB loaded? (`../protolabs/agents/materials-selection/skill-manifest.yaml`)
3. Review the KB freshness contract: Was the material data stale? (`../protolabs/kb-freshness-provenance-contract.md`)
4. Check the source-grounding contract: Did the agent cite the correct KB article?
5. Update the materials-selection agent's capability boundaries to forbid recommendations without compliance validation
6. Add a new eval case for material compliance checking (`../protolabs/dfm-accuracy-eval-suite.yaml`)
7. Refresh the relevant KB articles and verify with golden fixture

---

## Agent Selection Guide

Not sure which agent to use? Follow this decision tree:

```
Customer asks about...
│
├─→ "Can you make this part?" / "DFM review" / "manufacturability"
│   └─→ What manufacturing process?
│       ├─→ CNC machining → CNC Machining Agent (`agents/cnc-machining.agent.md`)
│       ├─→ Injection molding → Injection Molding Agent (`agents/injection-molding.agent.md`)
│       ├─→ Sheet metal → Sheet Metal Agent (`agents/sheet-metal.agent.md`)
│       ├─→ 3D printing → 3D Printing Agent (`agents/3d-printing.agent.md`)
│       └─→ Not sure → DFM Router Agent (`agents/dfm-router.agent.md`) classifies intent
│
├─→ "What material should I use?" / "material properties" / "alternative material"
│   └─→ Materials Selection Agent (`agents/materials-selection.agent.md`)
│
├─→ "Aerospace requirements" / "AS9100" / "flight critical"
│   └─→ Vertical Aerospace Agent (`agents/vertical-aerospace.agent.md`)
│
├─→ "Medical device" / "biocompatible" / "FDA" / "ISO 13485"
│   └─→ Vertical Medical Agent (`agents/vertical-medical.agent.md`)
│
├─→ "Automotive" / "EV" / "lightweighting" / "powertrain"
│   └─→ Vertical Automotive/EV Agent (`agents/vertical-automotive-ev.agent.md`)
│
└─→ "Industry trends" / "Industry 4.0" / "market forecast"
    └─→ Trends & Strategy Agent (`agents/trends-strategy.agent.md`)
```

Each agent loads only the KB articles specified in its `loads:` frontmatter. The router agent ensures the right specialist is invoked and the right compliance KBs are loaded when regulated keywords are detected.

---

## Still Lost?

If you cannot find what you need:

1. Check the [Glossary](../05-cross-cutting/glossary.md) -- you may be using different terminology
2. Browse the pillar READMEs -- each pillar directory has a README.md that serves as its table of contents
3. Review the [root README](../README.md) for the high-level framework overview

---

*This guide will be updated as new governance artifacts are added to the framework. If you identify a gap (a common scenario that is not covered), open an issue or contribute the missing artifact.*
