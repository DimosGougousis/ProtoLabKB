# Agent Instructions for ProductGovernance4AgenticWorkflows

These instructions apply to any AI coding agent (Claude, Copilot, Cursor, etc.) working in this repository.

## Repository Nature

This is a **documentation-first governance framework**. There is no application code. The deliverables are:

- Markdown documents (`.md`) -- governance guides, process descriptions, decision frameworks
- YAML checklists (`.yaml`) -- structured checklists for audits, reviews, and assessments
- Templates -- reusable governance artifacts for teams to fill out

Do not create application code, scripts, or tooling unless explicitly requested. The value of this repository is in the clarity and actionability of its written governance artifacts.

## Content Standards

### Actionable, Not Theoretical

Every document must answer "what do I do with this?" If a governance artifact cannot be directly used by a team member in their daily work, it is not ready.

Bad: "Organizations should consider the ethical implications of their AI systems."
Good: "Before proceeding past the Discovery Gate, complete the ethical risk assessment checklist (01-discovery-governance/ethical-risk-assessment.yaml). The checklist requires sign-off from the Product Owner, Ethics Lead, and a member of the Risk team."

### Required Sections for Governance Artifacts

When creating a new governance artifact (checklist, guide, template, or process), always include these metadata sections at the top:

```markdown
## Purpose
What this artifact is for and what problem it solves.

## When to Use
The specific trigger or lifecycle phase when this artifact is relevant.

## Who Is Responsible
The roles accountable for completing, reviewing, and approving this artifact (use RACI where appropriate).

## Regulatory Basis
Which regulations, standards, or frameworks require or motivate this artifact (EU AI Act articles, DNB guidelines, DORA requirements, SAFEST pillars, etc.). If there is no direct regulatory basis, state "Best practice" with a brief rationale.
```

### YAML Checklist Format

All YAML checklists follow the SAFEST template pattern. Each checklist item must include:

```yaml
- id: PILLAR-AREA-NNN        # Unique identifier (e.g., DISC-RISK-001)
  item: "Description"         # What must be done or verified
  priority: critical|high|medium|low
  status: not_started|in_progress|completed|not_applicable
  evidence_ref: ""            # Link to evidence document, artifact, or tool output
  notes: ""                   # Additional context, findings, or exceptions
  regulatory_ref: ""          # Specific regulation article (e.g., "EU AI Act Art. 9(2)")
```

The `id` prefix scheme:
- `DISC-` -- Discovery Governance (Pillar 1)
- `DEV-` -- Development Governance (Pillar 2)
- `RUN-` -- Runtime Governance (Pillar 3)
- `OPS-` -- Operational Governance (Pillar 4)
- `CROSS-` -- Cross-cutting concerns (Pillar 5)

### Cross-Referencing

Markdown documents must include cross-references to related files in other pillars. Governance does not live in silos. Examples:

- A risk assessment in Discovery Governance should reference the corresponding eval strategy in Development Governance
- A guardrail configuration in Runtime Governance should reference the acceptance criteria that motivated it in Development Governance
- An incident response playbook in Operational Governance should reference the escalation policies in Runtime Governance

Use relative links: `[eval strategy](../02-development-governance/eval-driven-development.md)`

### Evaluations as First-Class Concern

Evaluations (evals) are central to this framework. Every pillar has an evaluation dimension:

- **Discovery**: What acceptance criteria define success? What metrics will we track?
- **Development**: What eval suites validate quality, safety, and fairness? What is the pass/fail bar?
- **Runtime**: What continuous evaluations monitor live behavior? What thresholds trigger alerts?
- **Operational**: What periodic re-evaluations detect drift? When do we re-certify?

When writing content for any pillar, always ask: "Where is the evaluation aspect?" If it is missing, add it.

## File Naming and Organization

- **File names**: lowercase-with-hyphens (e.g., `ethical-risk-assessment.yaml`, `eval-driven-development.md`)
- **File types**: `.md` for documents, `.yaml` for checklists and structured data
- **No nested subdirectories** within pillars unless the pillar README explicitly defines them
- **Each pillar directory** must have a `README.md` that serves as the table of contents for that pillar

## Directory Structure Reference

```
00-getting-started/          # Onboarding, adoption paths, lifecycle canvas
01-discovery-governance/     # Risk assessment, ethical review, opportunity validation
02-development-governance/   # Eval-driven development, bias testing, quality gates
03-runtime-governance/       # Guardrails, prompt security, escalation, safety rails
04-operational-governance/   # Monitoring, incident response, audit, decommissioning
05-cross-cutting/            # Glossary, RACI, shared templates
06-executive/                # Board-level summaries, investment frameworks
07-enterprise-implementation/# Rollout playbooks, org change, tooling
docs/plans/                  # Implementation plans and design decisions
```

## Agentic AI Governance Concepts

This framework has a special focus on **business AI agents** (customer-facing chatbots, autonomous decision-makers, multi-agent orchestration systems). Key concepts that must be reflected in relevant artifacts:

### Machine Identity / Non-Human Identity (NHI)
Agents are first-class IAM citizens with least-privilege scopes, credential rotation, and audit trails. See `agent-permission-boundaries.md` for the NHI lifecycle model.

### Agentic Tool Sovereignty
Three governance layers for agent tool use: Configuration (tool discovery), Policy (tool selection), Network (execution/sandboxing). See `agent-permission-boundaries.md`.

### HITL / HOTL / HOTA
Three human oversight models scaled by risk:
- **HITL** (Human-in-the-Loop): Human approves every consequential action (high-risk)
- **HOTL** (Human-on-the-Loop): Human monitors and can intervene (medium-risk)
- **HOTA** (Human-out-of-the-Loop Autonomy): Human audits retrospectively (low-risk)
See `human-in-the-loop-patterns.md`.

### Two-System Architecture
The framework distinguishes between:
1. **Agent Fleet Command Dashboard** -- Operational visibility (fleet health, per-agent KPIs, cost, MLOps)
2. **Agentic Governance Framework** -- Policy + process backbone (permissions, safety, evals, drift detection)
See `agent-fleet-operations.md` for the bridge between them, and `governance-dashboard-spec.md` for executive views.

### Tiered Governance
Four tiers: Strategic (Board/CAIO), Policy (Ethics Board/Compliance), Lifecycle (Product Teams), Runtime (Automated). Governance intensity scales with EU AI Act risk tier.

### Enterprise Standards
- **ISO/IEC 42001**: AI Management System (AIMS) with PDCA model
- **CAIO Role**: Chief AI Officer owning enterprise AI risk
- **Federated Governance**: Central body sets ~75% of rules; local teams execute with ~25% autonomy

### Observability Platforms
Tracing agent reasoning via "Spans": LangSmith, Arize Phoenix, Opik, Langfuse. See `traceability-with-langchain.md`.

### Automated Red-Teaming
Continuous adversarial testing via Noma AI, Straiker, Giskard LLM Scan. See `red-teaming-ai-systems.md`.

## Implementation Context

For the implementation plan and phased rollout of this framework, see `docs/plans/`. Design decisions and rationale for the framework structure are documented there.

## Quality Checklist for New Content

Before considering a new document or checklist complete, verify:

- [ ] Purpose section is present and clear
- [ ] When to Use section identifies the specific trigger or lifecycle phase
- [ ] Who Is Responsible section names concrete roles (not vague "stakeholders")
- [ ] Regulatory Basis section cites specific articles or states "Best practice"
- [ ] Cross-references link to at least one related artifact in another pillar
- [ ] Evaluation dimension is addressed (what gets measured, what is the bar)
- [ ] Language is actionable (verbs, not adjectives; "do X" not "consider X")
- [ ] YAML checklists use the SAFEST template pattern with all required fields
- [ ] File name follows lowercase-with-hyphens convention
- [ ] Content is substantive (no stubs, no placeholder text, no "TBD" sections)
