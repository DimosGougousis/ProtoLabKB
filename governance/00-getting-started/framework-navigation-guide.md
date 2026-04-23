# Framework Navigation Guide

## Purpose

This guide maps common scenarios to specific framework artifacts. Use it when you know what you need to accomplish but are not sure where to find the relevant guidance, checklist, or template.

## When to Use

Anytime you have a specific governance question or task and want to find the right artifact quickly. This is your "I need to..." reference.

## Who Is Responsible

All team members. This guide is a navigation aid, not a governance artifact itself.

## Regulatory Basis

Best practice -- efficient navigation reduces governance friction and increases adoption.

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

---

## Still Lost?

If you cannot find what you need:

1. Check the [Glossary](../05-cross-cutting/glossary.md) -- you may be using different terminology
2. Browse the pillar READMEs -- each pillar directory has a README.md that serves as its table of contents
3. Review the [root README](../README.md) for the high-level framework overview

---

*This guide will be updated as new governance artifacts are added to the framework. If you identify a gap (a common scenario that is not covered), open an issue or contribute the missing artifact.*
