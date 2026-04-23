# Pillar 3: Runtime Governance

## Purpose

Runtime Governance ensures that AI systems behave correctly, safely, and fairly **while they are serving real users in production**. This is where guardrails are enforced, safety policies are applied, agent permissions are controlled, and continuous evaluation detects problems before they escalate.

Discovery Governance asks "should we build this?" Development Governance asks "did we build it safely?" Runtime Governance asks: **"Is it behaving correctly right now?"**

This pillar is particularly critical for agentic AI systems, where autonomous agents make decisions, take actions, delegate to sub-agents, and interact with customers in ways that are difficult to fully predict during development.

## When to Use

Apply Runtime Governance to every AI system that is live in production:

- When deploying an AI system for the first time
- When operating any customer-facing AI agent or chatbot
- When running multi-agent systems with autonomous decision-making capabilities
- When monitoring AI system behavior against acceptance criteria
- When responding to alerts or anomalies in AI system behavior
- When evaluating whether to roll back, adjust, or escalate

**Trigger:** Runtime Governance is always active. It is not a phase -- it is a continuous operational concern from the moment an AI system enters production until it is decommissioned.

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **MLOps / Platform Engineer** | **Responsible** -- operates the monitoring infrastructure, guardrail enforcement, alert routing |
| **Model Owner** | **Accountable** -- responds to alerts, makes decisions about interventions, owns the system's production behavior |
| **On-Call Engineer** | **Responsible** -- first responder for production alerts and anomalies |
| **Compliance Officer (2nd Line)** | **Reviewer** -- monitors continuous evaluation dashboards, escalates concerns |
| **AI Governance Committee** | **Approver** -- approves changes to guardrail configurations and permission boundaries for limited/high-risk systems |

## Regulatory Basis

- **EU AI Act Article 9(3)** -- Risk management system must address risks from foreseeable use and misuse
- **EU AI Act Article 14** -- Human oversight measures, including ability to interrupt or shut down
- **EU AI Act Article 72** -- Post-market monitoring system for high-risk systems
- **GDPR Article 22** -- Right not to be subject to solely automated decision-making
- **SAFEST items S-12** (drift detection), **S-13** (fallback procedures), **A-06** (human-in-the-loop), **A-07** (override), **A-09** (kill switch), **A-11** (audit trail), **F-11** (fairness monitoring)
- **DORA Article 11** -- ICT incident management procedures

---

## What This Pillar Contains

### Evaluations

| File | Description | When to Use |
|------|-------------|-------------|
| [evaluations/continuous-online-evaluation.md](evaluations/continuous-online-evaluation.md) | Guide for evaluating AI systems continuously in production: shadow mode, canary deployments, real-time monitoring, user feedback loops, alerting, and A/B testing | When setting up or reviewing production monitoring for any AI system |

### Agentic Workflows

| File | Description | When to Use |
|------|-------------|-------------|
| [agentic-workflows/multi-agent-governance-framework.md](agentic-workflows/multi-agent-governance-framework.md) | **Key differentiator** -- governance framework for multi-agent systems: permission boundaries, delegation chains, accountability, human-in-the-loop decision points, inter-agent protocols, and customer transparency | When designing, deploying, or governing any agentic AI system (single agent or multi-agent) |

---

## The Runtime Governance Layer

```
                           RUNTIME GOVERNANCE LAYER
  +-----------------------------------------------------------------+
  |                                                                 |
  |   +------------------+   +------------------+   +------------+  |
  |   | INPUT GUARDRAILS |   | AI SYSTEM        |   | OUTPUT     |  |
  |   |                  |   | (model, agent,   |   | GUARDRAILS |  |
  |   | - Prompt filter  |-->| LLM, workflow)   |-->| - Safety   |  |
  |   | - Input validate |   |                  |   |   filter   |  |
  |   | - Injection      |   | Operates within  |   | - PII      |  |
  |   |   defense        |   | permission       |   |   scrubber |  |
  |   | - Rate limiting  |   | boundaries       |   | - Format   |  |
  |   |                  |   |                  |   |   validate |  |
  |   +------------------+   +------------------+   +------------+  |
  |          |                       |                     |        |
  |          v                       v                     v        |
  |   +----------------------------------------------------------+  |
  |   | MONITORING AND CONTINUOUS EVALUATION                     |  |
  |   |                                                          |  |
  |   | - Real-time metric tracking against acceptance criteria  |  |
  |   | - Data drift detection                                   |  |
  |   | - Fairness monitoring across protected groups            |  |
  |   | - User feedback collection and analysis                  |  |
  |   | - Alert routing and escalation                           |  |
  |   +----------------------------------------------------------+  |
  |          |                       |                     |        |
  |          v                       v                     v        |
  |   +----------------------------------------------------------+  |
  |   | CONTROL MECHANISMS                                       |  |
  |   |                                                          |  |
  |   | - Kill switch / circuit breaker                          |  |
  |   | - Automatic rollback triggers                            |  |
  |   | - Human escalation routing                               |  |
  |   | - Traffic shifting (canary control)                      |  |
  |   | - Audit trail logging                                    |  |
  |   +----------------------------------------------------------+  |
  |                                                                 |
  +-----------------------------------------------------------------+
```

---

## Key Concepts

### Guardrails vs. Safety Rails

**Guardrails** are programmatic controls that constrain AI system behavior at runtime. They operate on inputs (filtering harmful or malformed prompts), outputs (blocking harmful or non-compliant responses), and actions (preventing unauthorized operations).

**Safety rails** are a subset of guardrails specifically designed to prevent harmful, dangerous, or illegal outputs. Every safety rail is a guardrail, but not every guardrail is a safety rail.

### Permission Boundaries for Agents

Every AI agent operates within a defined permission boundary -- the set of actions it is authorized to perform. Permission boundaries follow the principle of least privilege: an agent should have only the permissions necessary for its specific task.

The [Multi-Agent Governance Framework](agentic-workflows/multi-agent-governance-framework.md) provides the comprehensive model for defining, enforcing, and auditing permission boundaries.

### Continuous Evaluation

Pre-deployment testing proves the system works on test data. Continuous evaluation proves it keeps working on real production data, with real users, under real conditions, over time. Without continuous evaluation, you discover problems from customer complaints, not from data.

See [Continuous Online Evaluation](evaluations/continuous-online-evaluation.md) for the complete methodology.

---

## How This Pillar Connects to Others

### Inputs from Development Governance

| Input | Source | Used For |
|-------|--------|----------|
| Acceptance criteria and thresholds | [Acceptance Criteria](../01-discovery-governance/evaluations/defining-acceptance-criteria.md) | Define what "good" looks like in production; monitoring thresholds |
| Eval suite | [Eval-Driven Development](../02-development-governance/evaluations/eval-driven-development.md) | Adapted for continuous production evaluation |
| Pre-deployment gate evidence | [Pre-Deployment Gate](../02-development-governance/checklists/pre-deployment-gate.yaml) | Baseline for production behavior expectations |
| Guardrail specifications | Development testing results | Define runtime safety boundaries |
| Fallback procedures | Development documentation | Activated when runtime problems occur |

### Outputs to Operational Governance

| Output | Destination | Purpose |
|--------|-------------|---------|
| Monitoring alerts | [Operational Governance](../04-operational-governance/) | Trigger incident response procedures |
| Continuous eval results | Operational dashboards | Feed drift detection and revalidation decisions |
| Audit trail data | Compliance and audit | Evidence for regulatory reporting |
| Escalation events | Incident management | Data for incident analysis and root cause investigation |
| User feedback patterns | Product improvement | Inform model retraining and feature updates |

### Feedback to Discovery Governance

| Feedback | Destination | Purpose |
|----------|-------------|---------|
| Production performance data | Discovery reassessment | Validate or revise acceptance criteria |
| Failure mode discoveries | Risk classification | May trigger reclassification to higher risk tier |
| User behavior patterns | Future product discovery | Inform new feature opportunities and risks |

---

## Getting Started

1. **Setting up production monitoring?** Start with [Continuous Online Evaluation](evaluations/continuous-online-evaluation.md) to understand what to monitor, how to alert, and how to respond.

2. **Deploying an agent system?** Read the [Multi-Agent Governance Framework](agentic-workflows/multi-agent-governance-framework.md) before going live. Define permission boundaries, escalation triggers, and audit trail requirements.

3. **Need to understand guardrail architecture?** The runtime governance layer diagram above provides the conceptual model. Each component is addressed in detail within the referenced documents.

4. **Responding to a production alert?** Follow the escalation thresholds defined in your [Evaluation Strategy](../01-discovery-governance/evaluations/evaluation-strategy-template.yaml) and the incident response procedures in [Operational Governance](../04-operational-governance/).

---

*Last updated: 2026-02-28*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
