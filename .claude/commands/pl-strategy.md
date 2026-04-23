---
type: command
name: pl-strategy
description: Discuss manufacturing strategy, trends, innovation, and Industry 4.0 insights
usage: /pl-strategy <topic|question>
---

# /pl-strategy

Discuss manufacturing strategy, trends, innovation patterns, and Industry 4.0 insights to guide product strategy and technology adoption decisions.

## Usage

```
/pl-strategy <topic>
/pl-strategy <question>
```

## Examples

```
/pl-strategy "What are the key trends in additive manufacturing for 2026?"
/pl-strategy "How should we approach supply chain resilience in our product roadmap?"
/pl-strategy "Compare nearshoring vs offshoring strategies for CNC machining"
/pl-strategy "What Industry 4.0 technologies should we prioritize?"
/pl-strategy "Analyze the sustainability trends affecting injection molding"
```

## Procedure

1. **Parse Input**
   - Extract the user's topic or question
   - Identify key themes (trends, innovation, strategy, compliance, vertical)

2. **Classify Intent** (using protolabs-router skill)
   - Extract trend keywords (innovation, industry 4.0, digital thread, digital twin, smart manufacturing)
   - Extract strategy keywords (supply chain, sustainability, reshoring, nearshoring, agile)
   - Extract compliance keywords (regulatory trends, cybersecurity, data protection, ITAR, EAR, AS9100, ISO 13485)
   - Extract vertical keywords (aerospace, medical, automotive)
   - Determine mode: Strategic Analysis

3. **Route to Trends-Strategy Agent**
   - Load `agents/trends-strategy.agent.md`
   - If vertical specified, also load vertical agent
   - If compliance/regulatory focus, include compliance knowledge files

4. **Execute Strategic Analysis**
   - Agent loads its KB files (trends, innovation, compliance)
   - Synthesizes insights from multiple sources
   - Provides actionable recommendations
   - Identifies risks and opportunities

5. **Generate Response**
   - Use `templates/qa-response.md` format
   - Include trend analysis with data points
   - Provide strategic recommendations
   - Cite all sources

## Output Format

Output follows `templates/qa-response.md`:

- **Topic Summary** — Brief overview of the strategic question
- **Key Trends** — Relevant manufacturing trends and data points
- **Strategic Implications** — What this means for product strategy
- **Recommendations** — Actionable next steps
- **Risk Considerations** — Compliance, supply chain, or technical risks
- **Sources** — Citations from knowledge base

## Source Citation

Every claim must cite:
- The cached KB file: `knowledge/trends/<article>.md`
- The original ProtoLabs URL from the file's `source_url` frontmatter

Example: "Additive manufacturing adoption increased 40% in aerospace [knowledge/trends/3d-printing-trend-report.md → https://www.protolabs.com/resources/guides-and-trend-reports/3d-printing-trend-report/]"
