---
type: command
name: pl-dfm-review
description: Evaluate a part design against ProtoLabs DFM rules
usage: /pl-dfm-review <path|description>
---

# /pl-dfm-review

Evaluate a part design against ProtoLabs Design for Manufacturing (DFM) rules.

## Usage

```
/pl-dfm-review <path-to-file.md>
/pl-dfm-review <part-description-text>
```

## Examples

```
/pl-dfm-review intake/_example-complex-machined.md
/pl-dfm-review "Aluminum bracket with 0.5mm holes and internal square corners"
```

## Procedure

1. **Parse Input**
   - If argument is a file path, read the file content
   - If argument is text, use it directly as the part description

2. **Classify Intent** (using protolabs-router skill)
   - Extract process keywords (CNC, injection, sheet metal, 3D printing)
   - Extract vertical keywords (aerospace, medical, automotive)
   - Determine mode: DFM Review

3. **Route to Specialist Agent**
   - Load the appropriate process agent (cnc-machining, injection-molding, etc.)
   - If vertical specified, also load vertical agent

4. **Execute DFM Evaluation**
   - Agent loads its KB files
   - Analyzes part description against DFM rules
   - Identifies critical issues, warnings, and notes
   - Calculates DFM score

5. **Generate Report**
   - Use `templates/dfm-eval-report.md` format
   - Include part summary
   - List critical issues, warnings, notes with source citations
   - Provide DFM score breakdown
   - Include manufacturing recommendations
   - Cite all sources

## Output Format

Output follows `templates/dfm-eval-report.md`:

- Part Summary (name, process, material, vertical)
- Critical Issues table (issue, location, rule, recommendation, source)
- Warnings table
- Notes table
- DFM Score (geometry, tolerances, material, process, cost)
- Manufacturing Recommendations
- Sources (with KB file paths and ProtoLabs URLs)

## Source Citation

Every claim must cite:
- Cached KB file: `knowledge/<folder>/<file>.md`
- Original URL from file's `source_url` frontmatter

Format: `[knowledge/<folder>/<file>.md → <source_url>]`

## Error Handling

- If process cannot be determined: Ask clarifying question
- If file path doesn't exist: Report error with suggestions
- If multiple processes detected: Provide comparative analysis or ask for clarification
