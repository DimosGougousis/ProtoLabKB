# ProtoLabs Product Office — Project CLAUDE.md

> Project-local commands and skills for the ProtoLabs manufacturing knowledge-base system.

## Commands

| Command | File | Description |
|---------|------|-------------|
| `/pl-dfm-review` | `.claude/commands/pl-dfm-review.md` | Evaluate a part design against ProtoLabs DFM rules |
| `/pl-ask` | `.claude/commands/pl-ask.md` | Ask a manufacturing question grounded in ProtoLabs guidance |
| `/pl-strategy` | `.claude/commands/pl-strategy.md` | Discuss manufacturing strategy, trends, and Industry 4.0 insights |
| `/pl-governance` | `.claude/commands/pl-governance.md` | Assess compliance with AI governance framework and regulations |
| `/pl-assess` | `.claude/commands/pl-assess.md` | Comprehensive assessment (DFM + governance) of parts or agents |
| `/pl-refresh-kb` | `.claude/commands/pl-refresh-kb.md` | Refresh cached knowledge base articles |

## Skills

| Skill | File | Description |
|-------|------|-------------|
| `protolabs-router` | `.claude/skills/protolabs-router.md` | Route user prompts to appropriate specialist agents |

## Usage

1. **Design Review**: `/pl-dfm-review <path|description>` — Routes to appropriate process agent for DFM evaluation
2. **Q&A**: `/pl-ask <question>` — Routes to appropriate agent for knowledge-based answer
3. **Strategy Discussion**: `/pl-strategy <topic|question>` — Discuss trends, innovation, and strategic insights
4. **Governance Assessment**: `/pl-governance <assessment-type> [scope]` — Assess AI governance compliance
5. **Comprehensive Assessment**: `/pl-assess <target> [criteria]` — Combined DFM + governance evaluation
6. **Refresh KB**: `/pl-refresh-kb [folder]` — Updates cached articles from ProtoLabs website

## Agent Loading

Commands use the `protolabs-router` skill to:
1. Parse user input for keywords (process, mode, vertical)
2. Classify intent (design eval vs Q&A)
3. Load the appropriate specialist agent
4. Execute with only the required KB files

## See Also

- `../CLAUDE.md` — Root agent registry and routing keywords
- `../PLAN.md` — Full implementation architecture
- `../agents/` — Specialist agent definitions
