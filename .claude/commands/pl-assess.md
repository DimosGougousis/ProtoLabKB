---
type: command
name: pl-assess
description: Comprehensive assessment of parts, processes, or agents against DFM and governance criteria
usage: /pl-assess <target> [criteria]
---

# /pl-assess

Run a comprehensive assessment combining DFM evaluation with governance compliance checks. This command provides a unified view of manufacturability and regulatory readiness.

## Usage

```
/pl-assess <part-description|file-path>
/pl-assess <part-description> --vertical <aerospace|medical|automotive>
/pl-assess agent <agent-name>
/pl-assess intake <file-path>
```

## Examples

```
/pl-assess "Aluminum bracket with 0.5mm holes for aerospace application"
/pl-assess intake/cad-review-request.md --vertical medical
/pl-assess agent injection-molding
/pl-assess cnc-machining --compliance-only
```

## Assessment Modes

| Mode | Target | Description |
|------|--------|-------------|
| `part` (default) | Part description or file | Combined DFM + governance assessment |
| `agent` | Agent name | Full governance compliance assessment |
| `intake` | Intake file | End-to-end intake review |
| `process` | Process name | Process capability assessment |

## Procedure

1. **Parse Input**
   - Identify assessment mode (part, agent, intake, process)
   - Extract target (description, file path, or name)
   - Parse options (--vertical, --compliance-only, --dfm-only)

2. **Classify Intent** (using protolabs-router skill)
   - Extract process keywords (CNC, injection, sheet metal, 3D printing)
   - Extract vertical keywords (aerospace, medical, automotive)
   - Extract compliance keywords (ITAR, EAR, AS9100, ISO 13485, FDA)
   - Determine regulated context

3. **Execute Assessment**

   **For Part Assessment:**
   - Run DFM evaluation via appropriate process agent
   - If vertical specified, add vertical-specific requirements
   - If regulated keywords detected, run compliance pre-check
   - Combine findings into unified report

   **For Agent Assessment:**
   - Load agent definition
   - Check all governance pillars:
     - Discovery: Risk classification complete?
     - Development: Evaluations defined? Quality gates passed?
     - Runtime: Guardrails configured? Human oversight ready?
     - Operational: Incident response defined? Drift detection enabled?
   - Generate compliance scorecard

   **For Intake Assessment:**
   - Parse intake file
   - Validate completeness
   - Check for compliance triggers
   - Route to appropriate specialist agents
   - Generate intake summary

4. **Generate Report**
   - Use `templates/dfm-eval-report.md` for DFM findings
   - Use `templates/compliance-assessment.md` for governance findings
   - Provide unified recommendations

## Output Sections

### For Part Assessment

- **Part Summary** — Name, process, material, vertical
- **DFM Evaluation** — Critical issues, warnings, notes with DFM score
- **Compliance Pre-Check** — Regulatory considerations (if triggered)
- **Manufacturing Recommendations** — Process-specific guidance
- **Next Steps** — Actions required before production

### For Agent Assessment

- **Agent Overview** — Name, purpose, loaded knowledge
- **Governance Scorecard** — By pillar (Discovery/Development/Runtime/Operational)
- **Risk Classification** — EU AI Act tier and justification
- **Evaluation Status** — Required vs completed evaluations
- **Guardrail Status** — Configured protections
- **Remediation Items** — Required before deployment

### For Intake Assessment

- **Intake Summary** — Part description, process, requirements
- **Completeness Check** — Required fields present
- **DFM Pre-Assessment** — Initial manufacturability screening
- **Compliance Flags** — Regulatory considerations
- **Routing Decision** — Recommended specialist agents
- **Estimated Complexity** — Simple/medium/complex

## Options

| Option | Description |
|--------|-------------|
| `--vertical <name>` | Specify vertical (aerospace, medical, automotive) |
| `--compliance-only` | Skip DFM, assess governance only |
| `--dfm-only` | Skip governance, assess DFM only |
| `--strict` | Apply strictest interpretation of all rules |

## Source Citation

Every claim must cite:
- DFM sources: `knowledge/<process>/<article>.md`
- Governance sources: `governance/0X-<pillar>-governance/<file>.md`
- Regulatory sources: `governance/05-cross-cutting/regulatory-reference-index.md`
