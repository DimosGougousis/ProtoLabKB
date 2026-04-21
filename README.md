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

| Agent | Purpose | Loads | Compliance Coverage |
|-------|---------|-------|---------------------|
| `dfm-router` | Intent classification & routing | - | Sets `regulated` flag from keywords |
| `cnc-machining` | CNC DFM evaluation | CNC KB + compliance | ITAR, EAR, ISO 9001/13485/AS9100, NIST, GDPR |
| `injection-molding` | Injection molding DFM | IM KB + compliance | ITAR, EAR, ISO 9001/13485/AS9100/IATF 16949, NIST, GDPR |
| `sheet-metal` | Sheet metal DFM | Sheet metal KB + compliance | ITAR, EAR, ISO 9001/AS9100, NIST, GDPR, RoHS, REACH |
| `3d-printing` | 3D printing DFM | 3DP KB + compliance | ITAR, EAR, ISO 9001/13485/AS9100, NIST, GDPR, EU AI Act |
| `materials-selection` | Material recommendations | Materials KB + compliance | Export controls, biocompatibility, aerospace/medical/automotive certs |
| `vertical-aerospace` | Aerospace-specific guidance | Aerospace vertical + compliance | AS9100D, FAR 25, NADCAP, ITAR/EAR for defense |
| `vertical-medical` | Medical device guidance | Medical vertical + compliance | FDA 21 CFR 820, ISO 13485, EU MDR, biocompatibility |
| `vertical-automotive-ev` | Automotive/EV guidance | Automotive + EV + compliance | IATF 16949, UNECE R100, PPAP, APQP, RoHS/REACH |
| `trends-strategy` | Strategic trend analysis | Trends KB + compliance | Regulatory trend monitoring, AI governance, cybersecurity |

## Knowledge Base Coverage

### Process Knowledge (34 articles)
- **CNC Machining**: 4 articles + 4 compliance files (ITAR, ISO, NIST, EU AI Act)
- **Injection Molding**: 8 articles + comprehensive compliance integration
- **Sheet Metal**: 1 article + comprehensive compliance integration
- **3D Printing**: 8 articles + 3 compliance files (FDA biocompatibility, export controls, quality standards)

### Cross-Cutting Knowledge (12 articles)
- **Materials**: 5 articles (metals, plastics selection) + compliance integration
- **Verticals**: 4 articles (aerospace, medical, automotive, EV) + 3 compliance files
- **Trends**: 4 articles (2026 innovation, Industry 4.0) + compliance awareness

### Compliance Knowledge Base (14 files)
| Category | Files | Coverage |
|----------|-------|----------|
| Export Controls | ITAR/EAR (CNC, 3DP), additive export controls | Defense, dual-use |
| Quality Standards | ISO 9001/13485/AS9100 (CNC), additive quality | Medical, aerospace |
| Cybersecurity | NIST 800-171, CMMC, AI RMF | DoD, CUI protection |
| AI Governance | EU AI Act (CNC, 3DP) | EU market, high-risk AI |
| Vertical | Aerospace, Medical, Automotive compliance | Industry-specific |
| Biocompatibility | FDA biocompatibility (3DP) | Medical devices |

**Total: 60+ knowledge articles with full compliance coverage**

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
