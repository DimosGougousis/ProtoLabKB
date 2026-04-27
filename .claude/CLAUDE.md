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
| `/pl-funnel-intake` | `.claude/commands/pl-funnel-intake.md` | Use-case funnel intake: 6-box canvas + 4 appendices (A/B/C/D) |
| `/pl-use-case-explorer` | `.claude/commands/pl-use-case-explorer.md` | Generate and rank candidate AI use cases for a Protolabs domain |
| `/pl-feasibility-probe` | `.claude/commands/pl-feasibility-probe.md` | Sharpen Solution Architecture for engineering-facing conversation |
| `/pl-rehearse` | `.claude/commands/pl-rehearse.md` | Workshop rehearsal: skeptical engineer pushback simulation |

## Skills

| Skill | File | Description |
|-------|------|-------------|
| `protolabs-router` | `.claude/skills/protolabs-router.md` | Route user prompts to appropriate specialist agents |
| `pl-funnel-intake` | `.claude/skills/pl-funnel-intake/SKILL.md` | Use-case funnel intake skill (canvas + appendices) |
| `pl-use-case-explorer` | `.claude/skills/pl-use-case-explorer/SKILL.md` | Use case discovery and ranking skill |
| `pl-feasibility-probe` | `.claude/skills/pl-feasibility-probe/SKILL.md` | Solution architecture and feasibility skill |
| `pl-rehearse` | `.claude/skills/pl-rehearse/SKILL.md` | Workshop rehearsal and pushback simulation skill |

## Usage

1. **Design Review**: `/pl-dfm-review <path|description>` — Routes to appropriate process agent for DFM evaluation
2. **Q&A**: `/pl-ask <question>` — Routes to appropriate agent for knowledge-based answer
3. **Strategy Discussion**: `/pl-strategy <topic|question>` — Discuss trends, innovation, and strategic insights
4. **Governance Assessment**: `/pl-governance <assessment-type> [scope]` — Assess AI governance compliance
5. **Comprehensive Assessment**: `/pl-assess <target> [criteria]` — Combined DFM + governance evaluation
6. **Refresh KB**: `/pl-refresh-kb [folder]` — Updates cached articles from ProtoLabs website
7. **Funnel Intake**: `/pl-funnel-intake <use-case>` — Generate 6-box canvas + 4 appendices for workshop prep
8. **Use Case Explorer**: `/pl-use-case-explorer <domain>` — Rank candidate AI use cases for a domain
9. **Feasibility Probe**: `/pl-feasibility-probe <use-case>` — Deep-dive architecture for engineering review
10. **Workshop Rehearsal**: `/pl-rehearse <use-case>` — Simulate skeptical engineer pushback

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
