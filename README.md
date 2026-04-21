# ProtoLabs Product Office

A specialized knowledge-base and agent system for ProtoLabs manufacturing design-for-manufacturability (DFM) guidance.

## Overview

This repository contains:
- **10 Specialist Agents** for CNC machining, injection molding, sheet metal, 3D printing, materials selection, and vertical-specific guidance (aerospace, medical, automotive/EV)
- **Cached Knowledge Base** of 28 ProtoLabs articles with source citations
- **Router + Commands** for design evaluation and Q&A workflows

## Quick Start

1. **Design Review**: Use `/pl-dfm-review <part-description>` to evaluate a part against ProtoLabs DFM rules
2. **Ask a Question**: Use `/pl-ask <question>` to get answers grounded in ProtoLabs guidance
3. **Refresh Knowledge**: Use `/pl-refresh-kb [folder]` to update cached articles

## Agent Inventory

| Agent | Purpose | Loads |
|-------|---------|-------|
| `dfm-router` | Intent classification & routing | - |
| `cnc-machining` | CNC DFM evaluation | CNC KB + metals |
| `injection-molding` | Injection molding DFM | IM KB + thermoplastics |
| `sheet-metal` | Sheet metal DFM | Sheet metal KB |
| `3d-printing` | 3D printing DFM | 3DP KB |
| `materials-selection` | Material recommendations | Materials KB |
| `vertical-aerospace` | Aerospace-specific guidance | Aerospace vertical |
| `vertical-medical` | Medical device guidance | Medical vertical |
| `vertical-automotive-ev` | Automotive/EV guidance | Automotive + EV |
| `trends-strategy` | Strategic trend analysis | Trends KB |

## Knowledge Base Coverage

- **CNC Machining**: 4 articles
- **Injection Molding**: 8 articles (including LSR, overmolding)
- **Sheet Metal**: 1 article
- **3D Printing**: 8 articles (including metal 3DP, MJF vs SLS)
- **Materials**: 5 articles (metals, plastics selection)
- **Verticals**: 4 articles (aerospace, medical, automotive, EV)
- **Trends**: 4 articles (2026 innovation, Industry 4.0)

## Repository Structure

```
ProtoLab/
├── agents/              # Specialist agent definitions
├── knowledge/           # Cached ProtoLabs articles
│   ├── cnc-machining/
│   ├── injection-molding/
│   ├── sheet-metal/
│   ├── 3d-printing/
│   ├── materials/
│   ├── verticals/
│   └── trends/
├── templates/           # Output templates (DFM report, Q&A)
├── intake/              # Example part descriptions
├── reference/           # Interview prep materials
│   └── interview-prep/
├── .claude/
│   ├── commands/        # Slash commands
│   └── skills/          # Router skill
├── CLAUDE.md            # Entry point (router + registry)
├── README.md            # This file
├── PLAN.md              # Full architecture
└── TODO.md              # Delivery checklist
```

## Verification

Run the verification suite to confirm everything works:

```bash
# Check knowledge base inventory
ls knowledge/*/*.md | wc -l  # Should be 28

# Test DFM review
/pl-dfm-review intake/_example-complex-machined.md

# Test Q&A
/pl-ask "Minimum wall thickness for a PP injection-molded enclosure?"
```

## License

Internal use only — ProtoLabs knowledge base content © ProtoLabs, Inc.
Cached for educational and reference purposes.

---

Built with the VS Code Agent extension system.
