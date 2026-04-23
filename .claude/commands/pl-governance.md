---
type: command
name: pl-governance
description: Assess compliance with AI governance framework and regulatory requirements
usage: /pl-governance <assessment-type> [scope]
---

# /pl-governance

Assess compliance with the ProtoLabs AI Governance Framework, evaluate against regulatory requirements (EU AI Act, GDPR, NIST CSF, ISO 42001), and generate governance reports.

## Usage

```
/pl-governance <assessment-type> [scope]
/pl-governance checklist <pillar>
/pl-governance assess <agent-name>
/pl-governance report [quarterly|incident|audit]
```

## Examples

```
/pl-governance checklist discovery
/pl-governance assess cnc-machining
/pl-governance assess all
/pl-governance report quarterly
/pl-governance gap-analysis
/pl-governance "Evaluate our compliance with EU AI Act Article 9"
/pl-governance "What checks are required before deploying a new agent?"
```

## Assessment Types

| Type | Description | Output |
|------|-------------|--------|
| `checklist` | Run a pillar-specific governance checklist | Completed checklist with status |
| `assess` | Assess a specific agent or all agents against governance requirements | Compliance assessment report |
| `report` | Generate governance reports | Formatted governance report |
| `gap-analysis` | Identify gaps in current governance coverage | Gap analysis with priorities |
| `question` | Answer governance/compliance questions | Cited answer with references |

## Procedure

1. **Parse Input**
   - Identify assessment type (checklist, assess, report, gap-analysis, question)
   - Extract scope (pillar name, agent name, report type, or question)

2. **Load Governance Framework**
   - Load relevant governance documents from `governance/` folder
   - Load regulatory reference index
   - Load applicable checklists and templates

3. **Execute Assessment**

   **For Checklist:**
   - Load the specified pillar's checklists from `governance/0X-<pillar>-governance/checklists/`
   - Present checklist items with current status
   - Allow interactive completion
   - Generate completion report

   **For Agent Assessment:**
   - Load agent definition from `agents/<agent>.agent.md`
   - Check against governance requirements:
     - Discovery: Risk classification, data governance, acceptance criteria
     - Development: Evaluations, quality gates, model cards
     - Runtime: Guardrails, human oversight, transparency controls
     - Operational: Incident response, drift detection, re-certification
   - Generate compliance score and findings

   **For Report:**
   - Aggregate governance metrics across all pillars
   - Generate executive summary
   - Include risk heat map
   - Provide recommendations

   **For Gap Analysis:**
   - Compare current state against framework requirements
   - Identify missing checklists, undocumented processes, incomplete evaluations
   - Prioritize gaps by risk level

4. **Generate Output**
   - Use `templates/compliance-assessment.md` format
   - Include regulatory citations
   - Provide actionable remediation steps
   - Reference specific governance files

## Governance Pillars

| Pillar | Folder | Checklist Prefix | Focus |
|--------|--------|------------------|-------|
| Discovery | `01-discovery-governance/` | `DISC-` | Risk classification, requirements, data governance |
| Development | `02-development-governance/` | `DEV-` | Evaluations, quality gates, model cards |
| Runtime | `03-runtime-governance/` | `RUN-` | Guardrails, monitoring, human oversight |
| Operational | `04-operational-governance/` | `OPS-` | Incident response, drift detection, re-certification |
| Cross-Cutting | `05-cross-cutting/` | `CROSS-` | Roles, glossary, regulatory mapping |
| Executive | `06-executive/` | — | Dashboards, reporting, financial governance |

## Regulatory Frameworks Covered

- **EU AI Act** — Risk classification, risk management, transparency, human oversight
- **GDPR** — Data protection, automated decision-making, DPIA
- **NIST CSF 2.0** — Cybersecurity governance, identify, protect, detect, respond, recover
- **ISO/IEC 42001** — AI Management System requirements
- **Manufacturing-Specific:** ITAR, EAR, AS9100D, ISO 13485, IATF 16949, FDA 21 CFR 820

## Output Format

Output follows `templates/compliance-assessment.md`:

- **Assessment Scope** — What was evaluated
- **Regulatory Basis** — Applicable regulations and articles
- **Compliance Score** — Pass/fail or percentage by pillar
- **Findings** — Detailed findings with severity (critical/high/medium/low)
- **Evidence References** — Links to completed checklists, evaluations, or artifacts
- **Remediation Plan** — Prioritized actions to address gaps
- **Next Review Date** — When reassessment is required

## Source Citation

Every claim must cite:
- The governance file: `governance/0X-<pillar>-governance/<file>.md`
- The regulatory reference: `governance/05-cross-cutting/regulatory-reference-index.md`
- The compliance KB file when applicable: `knowledge/compliance/<file>.md`
