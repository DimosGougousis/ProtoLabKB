# Prompt Registry

> **Document Type:** Development Governance — Prompt Management
> **Version:** 1.0
> **Effective Date:** 2026-04-28
> **Owner:** Technical Owner (per agent)
> **Approved By:** AI Governance Council
> **Review Cycle:** Quarterly, or upon any prompt change
> **Next Review:** 2026-07-28

---

## Purpose

This document serves as the centralized registry of all prompt templates used by ProtoLabs AI agents. Prompts are a first-class governance artifact — they shape agent behavior, carry implicit assumptions, and can introduce risks if changed without oversight. This registry ensures every prompt is versioned, owned, and auditable.

## When to Use

- When creating a new agent or adding a new prompt template
- When modifying an existing prompt (system prompt, user prompt template, few-shot examples)
- During model card review to verify prompt documentation
- During incident investigation to trace prompt changes
- During internal audit of agent behavior

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **Technical Owner** | **Accountable** — maintains prompt registry entries for their agents |
| **AI/ML Engineer** | **Responsible** — implements and tests prompt changes |
| **Policy Owner** | **Consulted** — validates prompt alignment with intended use |
| **Safety Officer** | **Reviewer** — reviews prompts for safety implications (Tier 2+) |

## Regulatory Basis

- **EU AI Act Article 11(2)(b)** — Description of system design including programming and training methodologies
- **EU AI Act Article 13(3)(b)** — Information on capabilities and limitations
- **ISO/IEC 42001 Clause 7.5** — Documented information
- **NIST AI RMF GV-7.1** — Model documentation complete

---

## Registry Format

Each prompt template is registered with the following fields:

| Field | Description |
|-------|-------------|
| `prompt_id` | Unique identifier (e.g., `PROMPT-CNC-001`) |
| `agent_id` | Which agent uses this prompt |
| `prompt_type` | `system` / `user_template` / `few_shot` / `guardrail` / `output_format` |
| `version` | Semantic version (e.g., `1.2.0`) |
| `status` | `active` / `deprecated` / `testing` |
| `owner` | Technical Owner name |
| `created_date` | ISO 8601 date |
| `last_modified` | ISO 8601 date |
| `change_summary` | Brief description of what changed in this version |
| `eval_required` | Whether prompt change requires eval suite re-run |
| `approval_required` | Whether prompt change requires governance approval |

---

## Active Prompt Registry

### DFM Router Agent (`dfm-router`)

| prompt_id | type | version | status | last_modified | change_summary |
|-----------|------|---------|--------|---------------|----------------|
| PROMPT-ROUTER-001 | system | 1.0.0 | active | 2026-04-28 | Initial system prompt for process classification |
| PROMPT-ROUTER-002 | user_template | 1.0.0 | active | 2026-04-28 | User input template with CAD description fields |
| PROMPT-ROUTER-003 | output_format | 1.0.0 | active | 2026-04-28 | JSON output schema for classification result |

### CNC Machining Agent (`cnc-machining`)

| prompt_id | type | version | status | last_modified | change_summary |
|-----------|------|---------|--------|---------------|----------------|
| PROMPT-CNC-001 | system | 1.0.0 | active | 2026-04-28 | System prompt for CNC DFM analysis |
| PROMPT-CNC-002 | user_template | 1.0.0 | active | 2026-04-28 | Part description + geometry input template |
| PROMPT-CNC-003 | few_shot | 1.0.0 | active | 2026-04-28 | Example DFM evaluations for complex features |
| PROMPT-CNC-004 | guardrail | 1.0.0 | active | 2026-04-28 | Citation enforcement and capability boundary guardrail |

### Injection Molding Agent (`injection-molding`)

| prompt_id | type | version | status | last_modified | change_summary |
|-----------|------|---------|--------|---------------|----------------|
| PROMPT-IM-001 | system | 1.0.0 | active | 2026-04-28 | System prompt for injection molding DFM analysis |
| PROMPT-IM-002 | user_template | 1.0.0 | active | 2026-04-28 | Part description + material + volume input template |
| PROMPT-IM-003 | few_shot | 1.0.0 | active | 2026-04-28 | Example evaluations for wall thickness, draft, gates |
| PROMPT-IM-004 | guardrail | 1.0.0 | active | 2026-04-28 | Citation enforcement and capability boundary guardrail |

### Sheet Metal Agent (`sheet-metal`)

| prompt_id | type | version | status | last_modified | change_summary |
|-----------|------|---------|--------|---------------|----------------|
| PROMPT-SM-001 | system | 1.0.0 | active | 2026-04-28 | System prompt for sheet metal DFM analysis |
| PROMPT-SM-002 | user_template | 1.0.0 | active | 2026-04-28 | Part description + gauge + bend input template |
| PROMPT-SM-003 | guardrail | 1.0.0 | active | 2026-04-28 | Citation enforcement and capability boundary guardrail |

### 3D Printing Agent (`3d-printing`)

| prompt_id | type | version | status | last_modified | change_summary |
|-----------|------|---------|--------|---------------|----------------|
| PROMPT-3DP-001 | system | 1.0.0 | active | 2026-04-28 | System prompt for 3D printing DFM analysis |
| PROMPT-3DP-002 | user_template | 1.0.0 | active | 2026-04-28 | Part description + process + material input template |
| PROMPT-3DP-003 | few_shot | 1.0.0 | active | 2026-04-28 | Example evaluations for support structures, orientation |
| PROMPT-3DP-004 | guardrail | 1.0.0 | active | 2026-04-28 | Citation enforcement and capability boundary guardrail |

### Materials Selection Agent (`materials-selection`)

| prompt_id | type | version | status | last_modified | change_summary |
|-----------|------|---------|--------|---------------|----------------|
| PROMPT-MAT-001 | system | 1.0.0 | active | 2026-04-28 | System prompt for material recommendation |
| PROMPT-MAT-002 | user_template | 1.0.0 | active | 2026-04-28 | Application + constraints + process input template |
| PROMPT-MAT-003 | guardrail | 1.0.0 | active | 2026-04-28 | Citation enforcement and capability boundary guardrail |

### Vertical Agents (Aerospace, Medical, Automotive/EV)

| prompt_id | agent_id | type | version | status | last_modified |
|-----------|----------|------|---------|--------|---------------|
| PROMPT-AERO-001 | vertical-aerospace | system | 1.0.0 | active | 2026-04-28 |
| PROMPT-MED-001 | vertical-medical | system | 1.0.0 | active | 2026-04-28 |
| PROMPT-AUTO-001 | vertical-automotive-ev | system | 1.0.0 | active | 2026-04-28 |

---

## Change Management Rules

| Change Type | Eval Re-Run Required | Approval Required | Who Approves |
|-------------|---------------------|-------------------|-------------|
| Typo/grammar fix in prompt | No | No | Technical Owner |
| Few-shot example addition | Yes | No | Technical Owner |
| System prompt wording change | Yes | No (logged) | Technical Owner |
| System prompt logic change (new capability) | Yes | Yes (Tier 1: Security Lead; Tier 2+: Council) | Per tier |
| Guardrail prompt change | Yes | Yes | Safety Officer + Technical Owner |
| Output format change | Yes | No (logged) | Technical Owner |
| New prompt template | Yes | Yes (Tier 1: Security Lead; Tier 2+: Council) | Per tier |

---

## Version History Format

Each prompt template should maintain its own version history:

```yaml
prompt_id: "PROMPT-CNC-001"
agent_id: "cnc-machining"
prompt_type: "system"
current_version: "1.2.0"
status: "active"
owner: "[Name], AI/ML Engineer"

version_history:
  - version: "1.0.0"
    date: "2026-04-28"
    author: "[Name]"
    change: "Initial system prompt for CNC DFM analysis"
    eval_run: true
    eval_result: "pass"
    approved_by: "Technical Owner"

  - version: "1.1.0"
    date: "2026-05-15"
    author: "[Name]"
    change: "Added threading analysis guidance based on KB article update"
    eval_run: true
    eval_result: "pass"
    approved_by: "Technical Owner"

  - version: "1.2.0"
    date: "2026-06-01"
    author: "[Name]"
    change: "Refined citation enforcement to require source_url for every claim"
    eval_run: true
    eval_result: "pass"
    approved_by: "Security Lead"
```

---

## Storage

- **This registry** (summary view): `governance/02-development-governance/prompt-registry.md`
- **Individual prompt templates**: Stored alongside agent definitions in `agents/` directory
- **Version history**: Maintained in agent-specific YAML files in `agents/` directory

---

## Cross-References

| Document | Relationship |
|----------|-------------|
| [Model Card Template](templates/model-card.md) | Model card references prompt registry entries |
| [Model Card Completeness Checklist](checklists/model-card-completeness-checklist.yaml) | DEV-MCC-011 validates prompt documentation |
| [Pre-Deployment Gate](checklists/pre-deployment-gate.yaml) | References prompt registry for deployment approval |
| [Approval Thresholds by Tier](../05-cross-cutting/approval-thresholds-by-tier.md) | Defines who approves prompt changes by tier |
| [Governance Framework Changelog](../05-cross-cutting/governance-framework-changelog.md) | Prompt changes logged in framework changelog |

---

*This registry is version-controlled and auditable. Unauthorized modifications void governance compliance claims.*
