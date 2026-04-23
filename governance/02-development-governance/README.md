# Pillar 2: Development Governance

## Purpose

Development Governance ensures that AI systems are built responsibly, with systematic testing for quality, safety, and fairness **before** they reach production. This is where the acceptance criteria defined during Discovery become automated evaluation suites, where bias is detected and addressed, and where quality gates prevent unsafe or underperforming systems from being deployed.

The core methodology of this pillar is **eval-driven development** -- the AI equivalent of test-driven development. No AI feature ships without automated acceptance criteria that prove it works.

## When to Use

Apply Development Governance throughout the entire build phase of an AI system:

- When starting a development sprint that includes AI/ML/LLM work
- When building or modifying a model, prompt, agent, or AI-powered feature
- When retraining an existing model on new data
- When integrating a third-party AI component
- When preparing a deployment package for the AI Governance Committee

**Trigger:** Any code change that modifies AI system behavior (model weights, prompts, guardrails, data pipelines, feature engineering) must go through Development Governance.

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **AI/ML Engineer** | **Responsible** -- builds eval suites, runs bias tests, writes model documentation, implements quality gates |
| **Model Owner** | **Accountable** -- ensures all Development Governance artifacts are complete and accurate before requesting deployment approval |
| **Product Manager** | **Consulted** -- validates that product-level acceptance criteria are met; owns business metric verification |
| **Compliance Officer (2nd Line)** | **Reviewer** -- independently validates model performance for limited/high-risk systems; reviews fairness testing results |
| **AI Governance Committee** | **Approver** -- grants deployment approval for limited and high-risk systems based on the deployment package |

## Regulatory Basis

- **EU AI Act Article 9** -- Risk management system, including testing and validation
- **EU AI Act Article 10** -- Data governance requirements for training, validation, and testing datasets
- **EU AI Act Article 15** -- Accuracy, robustness, and cybersecurity requirements
- **SAFEST items S-03** (acceptance criteria), **S-04** (edge cases), **S-05** (stress testing), **S-06** (adversarial robustness), **S-19** (independent validation), **F-03** (bias testing), **T-12** (model card)
- **DNB Good Practice** -- Expectation of rigorous model validation, including independent challenge by 2nd line

---

## What This Pillar Contains

### Evaluations

| File | Description | When to Use |
|------|-------------|-------------|
| [evaluations/eval-driven-development.md](evaluations/eval-driven-development.md) | **Core methodology** -- the eval-first cycle for AI feature development | Read before starting any AI development work; defines the development workflow |
| [evaluations/acceptance-criteria-automation.yaml](evaluations/acceptance-criteria-automation.yaml) | YAML template for machine-executable acceptance criteria | Use to translate Discovery's acceptance criteria into automated evaluation definitions |
| [evaluations/eval-gate-integration.md](evaluations/eval-gate-integration.md) | Guide for wiring eval results into CI/CD as blocking quality gates | When setting up or modifying the CI/CD pipeline for an AI system |

### Checklists

| File | Description | When to Use |
|------|-------------|-------------|
| [checklists/pre-deployment-gate.yaml](checklists/pre-deployment-gate.yaml) | The must-pass checklist before any AI system goes to production | Before every deployment; serves as the deployment approval evidence package |

---

## The Development Governance Workflow

```
  Discovery Gate Output              Development Governance              Deployment Gate
  (acceptance criteria,     -->      (build, test, validate)     -->    (pre-deployment
   evaluation strategy,                                                  checklist)
   risk classification)

  1. Receive acceptance          2. Write eval suite              5. Complete pre-deployment
     criteria from Discovery        (should fail initially)          checklist

                                 3. Build AI feature              6. Submit deployment
                                    (eval should pass)               package to Committee
                                                                     (limited/high-risk)
                                 4. Run bias testing,
                                    stress testing,              7. Obtain approval
                                    adversarial testing
```

### Key Principle: Eval-First

The [eval-driven development](evaluations/eval-driven-development.md) methodology requires this sequence:

1. **Define criteria** (from Discovery)
2. **Write eval suite** (automated tests encoding the criteria)
3. **Run eval suite** (it should FAIL because the feature does not exist yet)
4. **Build the feature** (implement the AI capability)
5. **Run eval suite** (it should PASS)
6. **Deploy** (only after passing the pre-deployment gate)

Skipping step 2 or 3 means you are not doing eval-driven development -- you are building first and testing later. This is the most common anti-pattern in AI development, and it is the one this pillar exists to prevent.

---

## How This Pillar Connects to Others

### Inputs from Discovery Governance

| Input | Source | Used For |
|-------|--------|----------|
| Risk classification | [EU AI Act Risk Classification](../01-discovery-governance/checklists/eu-ai-act-risk-classification.yaml) | Determines testing depth, documentation requirements, approval authority |
| Acceptance criteria | [Defining Acceptance Criteria](../01-discovery-governance/evaluations/defining-acceptance-criteria.md) | Become the pass/fail bar for eval suites |
| Evaluation strategy | [Evaluation Strategy Template](../01-discovery-governance/evaluations/evaluation-strategy-template.yaml) | Defines metrics, thresholds, data sources, and frequency for evaluations |
| Fairness requirements | Discovery Gate output | Define which protected attributes to test and which fairness metrics to use |

### Outputs to Runtime Governance

| Output | Destination | Purpose |
|--------|-------------|---------|
| Trained/configured model | Runtime environment | The AI system that will serve production traffic |
| Eval suite | [Continuous Online Evaluation](../03-runtime-governance/evaluations/continuous-online-evaluation.md) | Adapted for production monitoring with the same acceptance criteria |
| Guardrail specifications | Runtime Governance | Safety boundaries derived from testing results |
| Pre-deployment gate evidence | Audit trail | Evidence package for regulatory compliance |

### Outputs to Operational Governance

| Output | Destination | Purpose |
|--------|-------------|---------|
| Model documentation (model card, data sheet) | Operational records | Baseline for drift detection and revalidation |
| Evaluation baselines | Operational monitoring | Reference point for detecting degradation |
| Fallback procedure documentation | [Operational Governance](../04-operational-governance/) | Tested procedure for when the system fails in production |

---

## Integration with Agile Sprints

Development Governance integrates directly into the sprint workflow. See [Governance in Agile Sprints](../07-enterprise-implementation/process-integration/governance-in-agile-sprints.md) for:

- How to size governance tasks alongside feature work
- Definition of Done extensions for AI features by risk tier
- Governance user story templates
- Sprint capacity planning with governance overhead

---

## Getting Started

1. **Understand the methodology:** Read [Eval-Driven Development](evaluations/eval-driven-development.md) -- this is the foundation of everything in this pillar.

2. **Automate your criteria:** Use the [Acceptance Criteria Automation Template](evaluations/acceptance-criteria-automation.yaml) to translate Discovery's criteria into machine-executable form.

3. **Set up your pipeline:** Follow [Eval Gate Integration](evaluations/eval-gate-integration.md) to wire evaluations into your CI/CD pipeline.

4. **Prepare for deployment:** Complete the [Pre-Deployment Gate Checklist](checklists/pre-deployment-gate.yaml) before requesting production access.

---

*Last updated: 2026-02-28*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
