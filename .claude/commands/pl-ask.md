---
type: command
name: pl-ask
description: Ask a manufacturing question grounded in ProtoLabs guidance
usage: /pl-ask <question>
---

# /pl-ask

Ask a manufacturing question and receive an answer grounded in ProtoLabs knowledge base articles with source citations.

## Usage

```
/pl-ask <question>
```

## Examples

```
/pl-ask "What is the minimum wall thickness for a PP injection-molded enclosure?"
/pl-ask "Can I machine a 0.5mm hole in aluminum?"
/pl-ask "What's the difference between MJF and SLS 3D printing?"
/pl-ask "Which material should I use for a corrosion-resistant marine component?"
```

## Procedure

1. **Parse Question**
   - Extract the user's question
   - Identify key entities (process, material, feature, vertical)

2. **Classify Intent** (using protolabs-router skill)
   - Extract process keywords (CNC, injection, sheet metal, 3D printing, materials)
   - Extract vertical keywords (aerospace, medical, automotive)
   - Determine mode: Q&A

3. **Route to Specialist Agent**
   - Load the appropriate process agent
   - If vertical specified, also load vertical agent
   - If materials question, load materials-selection agent

4. **Execute Q&A**
   - Agent loads its KB files
   - Searches KB for relevant information
   - Synthesizes answer from multiple sources if needed
   - Identifies key rules and caveats

5. **Generate Response**
   - Use `templates/qa-response.md` format
   - Include direct answer
   - List key rules with values and sources
   - Include important caveats
   - Add related considerations
   - Cite all sources

## Output Format

Output follows `templates/qa-response.md`:

- Question (restated)
- Answer (direct, comprehensive)
- Key Rules & Guidelines table (rule, value, source)
- Important Caveats (bullet list)
- Related Considerations
- Sources (with KB file paths and ProtoLabs URLs)

## Source Citation

Every claim must cite:
- Cached KB file: `knowledge/<folder>/<file>.md`
- Original URL from file's `source_url` frontmatter

Format: `[knowledge/<folder>/<file>.md → <source_url>]`

## Multi-Process Questions

If a question spans multiple processes (e.g., "Should I machine or 3D print this part?"):

1. Load agents for all relevant processes
2. Consult each KB for applicable information
3. Provide comparative analysis
4. Include pros/cons for each process
5. Make recommendation based on part requirements

## Error Handling

- If process cannot be determined: Ask clarifying question
- If question is outside KB scope: State limitations and suggest alternatives
- If conflicting information found: Present both perspectives with sources
