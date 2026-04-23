# Pillar 1: Discovery Governance

## Purpose

Discovery Governance ensures that AI products are evaluated for risk, ethics, feasibility, and alignment with organizational strategy **before any development begins**. This is the "shift-left" pillar -- the place where you decide whether to build, what guardrails must exist, and how you will know if the system is working correctly.

Every AI initiative that passes through Discovery Governance exits with three things: a risk classification, a set of acceptance criteria, and an evaluation strategy. Without these, development must not begin.

## When to Use

Apply Discovery Governance at the **earliest stage** of any AI initiative:

- When a new AI product or feature is proposed
- When an existing non-AI system is being augmented with AI capabilities
- When a third-party AI system is being evaluated for procurement
- When the scope of an existing AI system changes materially (new use case, new data source, new user population)
- When regulatory changes require reclassification of an existing system

**Trigger:** Any entry in the product backlog that involves AI/ML/LLM capabilities must pass through Discovery Governance before entering a development sprint.

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **Product Manager** | **Accountable** -- owns the business case, defines the opportunity, ensures governance artifacts are completed before development begins |
| **Ethics Lead / Responsible AI Lead** | **Consulted** -- provides ethical review, identifies potential harms, challenges assumptions about fairness and transparency |
| **Compliance Officer (2nd Line)** | **Consulted** -- validates EU AI Act risk classification, identifies regulatory obligations, reviews documentation for regulatory adequacy |
| **AI/ML Engineer** | **Consulted** -- provides technical feasibility assessment, identifies data requirements, advises on evaluation approach |
| **AI Governance Committee** | **Approver** -- grants Discovery Gate approval for limited and high-risk systems |

## Regulatory Basis

- **EU AI Act Articles 5-6, 9, Annex III** -- Risk classification obligations and prohibited practices
- **EU AI Act Article 9(2)** -- Risk management system must identify and analyze known and foreseeable risks
- **GDPR Article 35** -- Data Protection Impact Assessment for high-risk processing
- **DNB Good Practice for AI** -- Expectation that AI risk assessment occurs before deployment
- **SAFEST items S-01, S-02, E-03, F-01, F-02** -- System inventory, algorithm selection rationale, prohibited uses, protected characteristics identification, proxy variable analysis

---

## What This Pillar Contains

### Checklists

| File | Description | When to Use |
|------|-------------|-------------|
| [checklists/eu-ai-act-risk-classification.yaml](checklists/eu-ai-act-risk-classification.yaml) | Structured checklist for determining the EU AI Act risk tier of an AI system | First step for every new AI initiative; determines governance intensity for all subsequent activities |

### Evaluations

| File | Description | When to Use |
|------|-------------|-------------|
| [evaluations/defining-acceptance-criteria.md](evaluations/defining-acceptance-criteria.md) | Guide for defining measurable acceptance criteria before development begins | After risk classification; before any development sprint |
| [evaluations/evaluation-strategy-template.yaml](evaluations/evaluation-strategy-template.yaml) | YAML template for documenting the complete evaluation strategy for an AI system | After acceptance criteria are defined; becomes the evaluation contract for Development Governance |
| [evaluations/ai-quality-metrics-catalog.md](evaluations/ai-quality-metrics-catalog.md) | Comprehensive catalog of metrics for AI quality, fairness, LLM behavior, product outcomes, and business impact | Reference when selecting metrics for acceptance criteria and evaluation strategy |

---

## The Discovery Gate

The Discovery Gate is the governance checkpoint at the end of the Discovery phase. An AI initiative may not proceed to development until it passes the Discovery Gate.

### Discovery Gate Criteria

| # | Criterion | Evidence Required | Risk Tier Applicability |
|---|-----------|-------------------|------------------------|
| 1 | EU AI Act risk classification completed | Completed [risk classification checklist](checklists/eu-ai-act-risk-classification.yaml) | All tiers |
| 2 | System is not in a prohibited category | Risk classification confirms no Article 5 violations | All tiers |
| 3 | Acceptance criteria defined with measurable thresholds | Completed [acceptance criteria](evaluations/defining-acceptance-criteria.md) document | All tiers |
| 4 | Evaluation strategy documented | Completed [evaluation strategy template](evaluations/evaluation-strategy-template.yaml) | All tiers |
| 5 | Protected characteristics identified | List of protected attributes relevant to the use case | Limited, High |
| 6 | Proxy variable risks documented | Analysis of features that may serve as proxies for protected characteristics | High |
| 7 | Ethical risk assessment completed | Documented assessment of potential harms, affected populations, and mitigations | Limited, High |
| 8 | Data Protection Impact Assessment initiated | DPIA started for systems processing personal data | High (if personal data) |
| 9 | AI Governance Committee approval obtained | Committee meeting minutes with approval decision | Limited, High |
| 10 | Business case validated against governance costs | Business case accounts for governance overhead at the appropriate risk tier | All tiers |

### Discovery Gate Approval Authority

| Risk Tier | Approval Authority |
|-----------|--------------------|
| Minimal | Product Manager + Team Lead |
| Limited | AI Governance Committee |
| High | AI Governance Committee + Board-level sponsor |

---

## Key Questions Discovery Governance Answers

1. **Is this AI application permitted?** Does it fall into a prohibited category under the EU AI Act Article 5?
2. **What is the risk tier?** How much governance will this system require throughout its lifecycle?
3. **What does "good" look like?** What are the measurable acceptance criteria that define success?
4. **How will we know if it is working?** What is the evaluation strategy -- which metrics, what thresholds, how often?
5. **Who could be harmed?** What populations are affected, what protected characteristics are at play, and what fairness standards apply?
6. **What happens if it fails?** What is the fallback, and what is the blast radius of a failure?
7. **Is the business case sound given governance requirements?** Does the ROI hold when you account for the governance overhead required by the risk tier?

---

## How This Pillar Connects to Others

Discovery Governance produces artifacts that flow directly into subsequent pillars:

| Discovery Output | Consumed By | Purpose |
|-----------------|-------------|---------|
| Risk classification | All pillars | Determines governance intensity everywhere |
| Acceptance criteria | [Development Governance](../02-development-governance/) | Become the pass/fail bar for [eval-driven development](../02-development-governance/evaluations/eval-driven-development.md) |
| Evaluation strategy | [Development Governance](../02-development-governance/) | Drives the [eval gate integration](../02-development-governance/evaluations/eval-gate-integration.md) in CI/CD |
| Fairness requirements | [Development Governance](../02-development-governance/) | Define bias testing requirements in the [pre-deployment gate](../02-development-governance/checklists/pre-deployment-gate.yaml) |
| Risk classification | [Runtime Governance](../03-runtime-governance/) | Determines guardrail stringency and monitoring intensity for [continuous evaluation](../03-runtime-governance/evaluations/continuous-online-evaluation.md) |
| Risk classification | [Operational Governance](../04-operational-governance/) | Determines audit frequency, incident response severity, and revalidation cadence |
| Business case + risk tier | [Enterprise Implementation](../07-enterprise-implementation/) | Feeds into [governance in agile sprints](../07-enterprise-implementation/process-integration/governance-in-agile-sprints.md) capacity planning |

---

## Getting Started

1. **New to AI governance?** Start with the [EU AI Act risk classification checklist](checklists/eu-ai-act-risk-classification.yaml). Classify your system first -- everything else follows from the risk tier.

2. **Know your risk tier, need to define success?** Go to [Defining Acceptance Criteria](evaluations/defining-acceptance-criteria.md) and work through the criteria framework.

3. **Need to pick metrics?** Browse the [AI Quality Metrics Catalog](evaluations/ai-quality-metrics-catalog.md) to find the right metrics for your system type and use case.

4. **Ready to document your evaluation plan?** Fill out the [Evaluation Strategy Template](evaluations/evaluation-strategy-template.yaml) -- this becomes the contract between Discovery and Development.

---

*Last updated: 2026-02-28*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
