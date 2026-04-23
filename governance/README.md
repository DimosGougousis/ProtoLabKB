# ProtoLabs AI Governance Framework

**Governance, risk, and compliance for the ProtoLabs Product Office AI agent system.**

This is a Protolabs-specific adaptation of the generic [Product Governance for Agentic AI Workflows](https://github.com/DimosGougousis/ProductGovernance4AgenticWorkflows) framework. It governs the 10 Design-for-Manufacturability (DFM) agents defined in `../agents/`, is grounded in the compliance knowledge base in `../knowledge/compliance/` and the per-process compliance files in `../knowledge/*/`, and is tuned for the digital-manufacturing business domain (CNC machining, injection molding, sheet metal, 3D printing, plus aerospace/medical/automotive verticals).

---

## What This Framework Is

A **governance layer** sitting alongside the agents it governs. Every artifact here either:

- Mirrors an upstream governance file (adapted with Protolabs examples in place of the generic banking/fraud ones), or
- Is a **new Protolabs-specific artifact** (see `protolabs/`) that closes a gap the upstream framework did not cover — customer CAD/IP protection, DFM accuracy eval suite, per-agent KILLSWITCH files, source-grounding data contracts, KB-freshness SLAs, and the executive dashboard tailored to this agent fleet.

## What This Framework Is Not

- **Not** a DORA/financial-services framework. Material irrelevant to a non-financial manufacturing services company has been moved to `_archive/` with stub redirects (not deleted, for traceability).
- **Not** a replacement for the compliance KBs in `../knowledge/`. Governance files **link** to the compliance KB content; they never duplicate it.
- **Not** legal advice. The regulatory mapping (EU AI Act, ITAR/EAR, FDA 21 CFR 820, AS9100D, ISO 9001/13485, IATF 16949, GDPR, NIST CSF, RoHS, REACH) is operational guidance — consult qualified counsel for live decisions.

---

## Structure

```
governance/
├── 00-getting-started/           Quickstart, lifecycle canvas, navigation
├── 01-discovery-governance/      "Should we build it?" gates
├── 02-development-governance/    "How do we build it safely?" gates
├── 03-runtime-governance/        Guardrails, kill switches, skill manifests
├── 04-operational-governance/    Incident response, audit, regulatory mapping
├── 05-cross-cutting/             Glossary, RACI, regulatory index, tool landscape
├── 06-executive/                 Board/CAIO dashboards, quarterly reports
├── 07-enterprise-implementation/ Org model, process integration, risk-based adoption
├── dashboards/                   Live HTML dashboards (T1-T4)
├── pillars/                      Pillar landing pages
├── _archive/                     Non-applicable upstream content (DORA, financial-governance)
├── styles/                       Shared CSS
└── protolabs/                    ← Protolabs-specific governance layer (12 core + per-agent)
    ├── agent-risk-registry.yaml              Canonical ARI-scored registry of the 10 DFM agents
    ├── safest-coverage-matrix.md             10 × 112 SAFEST coverage matrix
    ├── customer-cad-ip-protection-guardrail.md
    ├── dfm-accuracy-eval-suite.yaml          Golden-set eval anchored on the bracket fixture
    ├── quote-bot-financial-guardrails.md     Forward-looking control for the not-yet-built quote-bot
    ├── source-grounding-data-contract.yaml   Formalizes the "cite KB + source_url" rule
    ├── manufacturing-compliance-routing.md   Formalizes the {{#regulated}} template pattern
    ├── red-team-playbook-dfm-agents.md       20-30 adversarial cases
    ├── kb-freshness-provenance-contract.md   Staleness SLA for the 59 cached KB articles
    ├── protolabs-ml-lifecycle-canvas.md      DFM Analysis Agent worked example
    ├── executive-dashboard-protolabs-ai.md   T1 board view spec
    └── agents/<agent-id>/                    10 folders × {registry.yaml, skill-manifest.yaml, KILLSWITCH.md, safest-assessment.md}
```

---

## Provenance

- **Upstream repository:** `https://github.com/DimosGougousis/ProductGovernance4AgenticWorkflows`
- **Upstream commit this clone was derived from:** `f21423b7908d3de84a3d4051a964c324936fbfa5` (2026-03-26, "Remove all V1 Framework links from nav and footer across 11 pages")
- **Original upstream README preserved at:** `./README.upstream.md`
- **Files cloned:** 153 files (104 .md, 27 .yaml, 18 .html, 1 .css, 1 LICENSE, 1 launch.json, 1 .gitkeep).

---

## Reading Order

1. **New to this framework?** Start with `00-getting-started/README.md`, then `00-getting-started/ml-lifecycle-canvas.md` for the DFM Analysis Agent worked example.
2. **Executive/board audience?** Go straight to `06-executive/` and `dashboards/board.html`.
3. **Engineering/AI team?** Start with `protolabs/agent-risk-registry.yaml` (what we have, what risk tier) then `protolabs/safest-coverage-matrix.md` (what's covered, what's a gap).
4. **Compliance audience?** `05-cross-cutting/regulatory-reference-index.md` plus `04-operational-governance/regulatory/expanded-regulatory-mapping.md` plus the linked KBs in `../knowledge/compliance/`.
5. **Incident responder / on-call?** `protolabs/agents/<agent-id>/KILLSWITCH.md` for the agent in question.

---

## Relationship to the ProtoLab Agent System

The governance framework **references and does not duplicate** the following ProtoLab assets:

| ProtoLab asset | Used by governance for |
|----------------|------------------------|
| `../agents/*.agent.md` (10 files) | Source of truth for the `protolabs/agent-risk-registry.yaml` |
| `../knowledge/compliance/*` (legacy framework file) | Regulatory mapping pivot |
| `../knowledge/cnc-machining/itar-ear-compliance.md` + 13 other compliance KBs | Linked from regulatory index and CAD/IP guardrail |
| `../intake/_example-complex-machined.md` (4-defect bracket) | Golden fixture for DFM accuracy eval suite |
| `../templates/dfm-eval-report.md` and `qa-response.md` | Exemplify the `{{#regulated}}` pattern formalized by `protolabs/manufacturing-compliance-routing.md` |
| `../CLAUDE.md` routing keywords | Source for `protolabs/manufacturing-compliance-routing.md` mapping table |

This is an intentional separation: operational knowledge stays in `../knowledge/`; governance lives here.

---

## Status

**Phase 1 complete:** skeleton clone (153 files). Phases 2-6 in progress — see `C:\Users\dimos\.claude\plans\moonlit-tinkering-pancake.md` for the current adaptation plan.
