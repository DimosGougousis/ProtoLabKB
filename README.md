# ProtoLabs Product Office

A comprehensive AI-powered knowledge-base, governance framework, and agent system for ProtoLabs manufacturing design-for-manufacturability (DFM) guidance, AI governance, and strategic implementation.

## Overview

This repository contains:
- **11 Specialist Agents** for CNC machining, injection molding, sheet metal, 3D printing, materials selection, vertical-specific guidance (aerospace, medical, automotive/EV), and strategic trend analysis
- **68 Knowledge Base Articles** cached from ProtoLabs resources with source citations and compliance coverage
- **AI Governance Framework** — 140+ governance artifacts adapted from upstream ProductGovernance4AgenticWorkflows, tailored for digital manufacturing
- **AI Implementation Workstreams** — Jobs-to-be-Done framework, P0/P1 problem statements, 4 agentic-ready work packages, and decision frameworks
- **CAD AI Design Features Catalogue** — Multi-format CAD parsing, feature recognition, VLM integration, and DFM rule engine specifications
- **Executive Presentations & Strategic Docs** — C-Board presentations, TPM strategy guides, ISO 42001 gap analysis, governance-by-stage framework
- **Router + Commands** for design evaluation, Q&A, knowledge refresh, and governance assessment
- **Templates** for DFM evaluation reports, Q&A responses, and compliance assessments

## Quick Start

1. **Design Review**: Use `/pl-dfm-review <part-description>` to evaluate a part against ProtoLabs DFM rules
2. **Ask a Question**: Use `/pl-ask <question>` to get answers grounded in ProtoLabs guidance
3. **Refresh Knowledge**: Use `/pl-refresh-kb [folder]` to update cached articles
4. **Governance Assessment**: Use `/pl-governance <assessment-type> [scope]` to assess AI governance compliance

## Agent Inventory

| Agent | Purpose | Loads | Compliance Coverage |
|-------|---------|-------|---------------------|
| `dfm-router` | Intent classification & routing | — | Sets `regulated` flag from keywords |
| `cnc-machining` | CNC DFM evaluation | CNC KB + compliance | ITAR, EAR, ISO 9001/13485/AS9100, NIST, GDPR |
| `injection-molding` | Injection molding DFM | IM KB + compliance | ITAR, EAR, ISO 9001/13485/AS9100/IATF 16949, NIST, GDPR |
| `sheet-metal` | Sheet metal DFM | Sheet metal KB + compliance | ITAR, EAR, ISO 9001/AS9100, NIST, GDPR, RoHS, REACH |
| `3d-printing` | 3D printing DFM | 3DP KB + compliance | ITAR, EAR, ISO 9001/13485/AS9100, NIST, GDPR, EU AI Act |
| `materials-selection` | Material recommendations | Materials KB + compliance | Export controls, biocompatibility, aerospace/medical/automotive certs |
| `vertical-aerospace` | Aerospace-specific guidance | Aerospace vertical + compliance | AS9100D, FAR 25, NADCAP, ITAR/EAR for defense |
| `vertical-medical` | Medical device guidance | Medical vertical + compliance | FDA 21 CFR 820, ISO 13485, EU MDR, biocompatibility |
| `vertical-automotive-ev` | Automotive/EV guidance | Automotive + EV + compliance | IATF 16949, UNECE R100, PPAP, APQP, RoHS/REACH |
| `trends-strategy` | Strategic trend analysis | Trends KB + compliance | Regulatory trend monitoring, AI governance, cybersecurity |
| `cad-parser` | CAD file parsing & feature extraction | CAD KB + DFM rules | STEP, STL, OBJ, 3MF, IGES parsing |

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

### Compliance Knowledge Base (14+ files)
| Category | Files | Coverage |
|----------|-------|----------|
| Export Controls | ITAR/EAR (CNC, 3DP), additive export controls | Defense, dual-use |
| Quality Standards | ISO 9001/13485/AS9100 (CNC), additive quality | Medical, aerospace |
| Cybersecurity | NIST 800-171, CMMC, AI RMF | DoD, CUI protection |
| AI Governance | EU AI Act (CNC, 3DP) | EU market, high-risk AI |
| Vertical | Aerospace, Medical, Automotive compliance | Industry-specific |
| Biocompatibility | FDA biocompatibility (3DP) | Medical devices |

**Total: 68+ knowledge articles with full compliance coverage**

## AI Governance Framework

A Protolabs-specific adaptation of the ProductGovernance4AgenticWorkflows framework, governing the 10 DFM agents with:

- **7 Governance Stages**: Getting Started → Discovery → Development → Runtime → Operational → Cross-Cutting → Executive → Enterprise Implementation
- **Per-Agent Guardrails**: Agent risk registry, SAFEST coverage matrix, KILLSWITCH files, skill manifests, source-grounding data contracts
- **Compliance Routing**: `{{#regulated}}` template conditionals for ITAR/EAR, ISO, FDA, EU AI Act, NIST, GDPR
- **Executive Dashboards**: T1–T4 board views, quarterly reports, ML lifecycle canvas
- **Protolabs-Specific Artifacts**: Customer CAD/IP protection, DFM accuracy eval suite, KB-freshness SLAs, red-team playbook

See `governance/README.md` for the full framework structure and reading order.

## AI Implementation Workstreams

Structured implementation planning using the Jobs-to-be-Done (JTBD) framework:

### P0 Critical — Agentic-Ready (4 work packages)
| WP | Name | Problem Solved | Status |
|----|------|----------------|--------|
| WP01 | Input Sanitization | Unprotected AI inputs (prompt injection) | 🔴 Blocked — code incomplete |
| WP02 | Adversarial Defense | No multi-layer defense against attacks | 🔴 Blocked — code incomplete |
| WP03 | Runtime Monitoring | Blind spot in AI system behavior | 🔴 Blocked — code incomplete |
| WP04 | Audit & Compliance | Missing tamper-evident audit trails | 🔴 Blocked — code incomplete |
| WP-CAD | CAD AI Evaluation | Manual DFM analysis bottleneck | 🟡 Planning — $600K strategic initiative |

### P1 High Priority — Human Discussion Required (4 agendas)
- Zero-Trust Architecture
- Adversarial Defense System
- Insider Threat Program
- Nation-State Countermeasures

### Decision Frameworks
- Risk-based decision matrix for prioritization
- Governance framework mapping (NIST AI RMF ↔ Agentic Governance ↔ Singapore MGF)

See `ai-implementation-workstreams/README.md` for the master index and status dashboard.

## CAD AI Design Features Catalogue

Comprehensive feature specification for AI-powered CAD evaluation:

| Category | Features |
|----------|----------|
| **CAD Ingestion** | Multi-format parser (STEP/STL/OBJ/3MF/IGES), geometry extraction, PMI harvesting, assembly parsing |
| **Feature Recognition** | Hole detection, pocket recognition, boss ID, fillet/chamfer, threads, thin walls, undercuts, draft angles |
| **VLM Integration** | 2D view generation, section views, detail extraction, visual DFM assessment, design comparison, anomaly detection |
| **DFM Rule Engine** | Rulebook codification, geometric constraint checking, tolerance stack-up, material-process compatibility, cost estimation, manufacturability scoring |
| **Historical Learning** | Past project comparison, similarity search, pattern recognition |

See `ai-implementation-workstreams/AI-CAD-DESIGN-FEATURES-CATALOGUE.md` for full specifications.

## Strategic Documents

| Document | Purpose |
|----------|---------|
| `docs/executive-presentation-c-board.md` | C-Board presentation: AI transformation readiness, agentic landscape, governance model |
| `docs/TPM-Strategy-Agent-Guide.md` | Technical Product Manager's guide to using the Strategy Agent |
| `docs/governance-by-stage-framework.md` | Stage-gate governance framework for AI lifecycle management |
| `docs/iso-42001-gap-analysis.md` | ISO 42001 readiness assessment and certification roadmap |
| `docs/nist-ai-rmf-lmm-example.md` | NIST AI RMF worked example for large manufacturing models |
| `docs/client-journey-agentic-workflow.mmd` | Mermaid diagram of the client journey through agentic workflows |

## Reference Materials

| Document | Purpose |
|----------|---------|
| `reference/agent-evaluation-framework.md` | Systematic evaluation of 3D Printing agent with guardrail analysis |
| `reference/agent-skills-gap-analysis.md` | Cross-agent compliance maturity assessment (10 agents × 7 standard categories) |
| `reference/verification-runs/` | Golden test logs for DFM review, Q&A, ambiguity, and refresh verification |

## Templates

| Template | Use Case |
|----------|----------|
| `templates/dfm-eval-report.md` | Structured DFM evaluation output with severity ratings |
| `templates/qa-response.md` | Q&A response format with source citations |
| `templates/compliance-assessment.md` | Regulated-industry compliance check with `{{#regulated}}` conditionals |

## Repository Structure

```
ProtoLab/
├── agents/                    # 11 specialist agent definitions
├── knowledge/                 # 68+ cached ProtoLabs articles
│   ├── cnc-machining/
│   ├── injection-molding/
│   ├── sheet-metal/
│   ├── 3d-printing/
│   ├── materials/
│   ├── verticals/
│   ├── trends/
│   ├── compliance/
│   └── ai/
├── templates/                 # DFM report, Q&A, compliance assessment
├── intake/                    # Example part descriptions
├── reference/                 # Agent evaluation, skills gap analysis, verification runs
├── governance/                # 140+ AI governance framework files
│   ├── 00-getting-started/
│   ├── 01-discovery-governance/
│   ├── 02-development-governance/
│   ├── 03-runtime-governance/
│   ├── 04-operational-governance/
│   ├── 05-cross-cutting/
│   ├── 06-executive/
│   ├── 07-enterprise-implementation/
│   ├── protolabs/            # Protolabs-specific governance layer
│   └── dashboards/
├── ai-implementation-workstreams/  # JTBD framework, work packages, decision tools
│   ├── 00-JTBD-and-problem-statements/
│   ├── 01-agentic-ready-implementations/
│   ├── 02-human-discussion-required/
│   ├── 03-decision-frameworks/
│   └── 04-strategic-analysis/
├── docs/                      # Executive presentations, strategy guides, gap analyses
├── tools/
│   └── cad-parser/           # CAD parsing utilities
├── .claude/
│   ├── commands/             # Slash commands (/pl-dfm-review, /pl-ask, etc.)
│   └── skills/               # Router skill
├── CLAUDE.md                 # Entry point (router + registry)
├── README.md                 # This file
├── PLAN.md                   # Full architecture
└── TODO.md                   # Delivery checklist
```

## Verification

Run the verification suite to confirm everything works:

```bash
# Check knowledge base inventory
ls knowledge/*/*.md | wc -l  # Should be 68+

# Test DFM review
/pl-dfm-review intake/_example-complex-machined.md

# Test Q&A
/pl-ask "Minimum wall thickness for a PP injection-molded enclosure?"

# Test governance assessment
/pl-governance ai-act scope=3d-printing
```

## License

Internal use only — ProtoLabs knowledge base content © ProtoLabs, Inc.
Cached for educational and reference purposes.

---

Built with the VS Code Agent extension system.
