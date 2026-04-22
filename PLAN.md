# ProtoLabs Product Office — Implementation Plan

## Context

Stand up a new **Product Office for ProtoLabs** in a dedicated workspace that mirrors ProtoLabs' [manufacturing resources library](https://www.protolabs.com/resources/). Any prompt about a part (design, material, process, vertical) routes to a specialist agent that loads cached ProtoLabs guidance and either:

1. **Evaluates a design** against ProtoLabs DFM rules (e.g., complex machined part → CNC agent checks rules from [mastering-complex-features-on-machined-parts](https://www.protolabs.com/resources/design-tips/mastering-complex-features-on-machined-parts/)), or
2. **Answers Q&A** grounded in cached ProtoLabs articles with source citations.

### Confirmed decisions
- **Workspace:** `C:\Users\dimos\ProtoLab\` (existing folder, already holds ProtoLabs interview prep artifacts — those stay in place under a `reference/interview-prep/` subfolder).
- **GitHub remote:** `https://github.com/DimosGougousis/ProtoLabKB` (currently empty — we initialize and push).
- **Knowledge base:** cache ~28 key articles as local markdown (with `source_url` + `fetched_at` frontmatter).
- **Scope:** 4 core processes + materials + 3 verticals + trend reports.
- **Interaction:** design eval + Q&A.
- **Delivery checklist:** saved to `C:\Users\dimos\ProtoLab\TODO.md`.

## Target workspace layout

```
C:\Users\dimos\ProtoLab\
├── .git/                             # new, pushes to ProtoLabKB
├── .gitignore
├── README.md                         # repo overview + how to use
├── CLAUDE.md                         # router + loading rules (entry point)
├── TODO.md                           # delivery checklist (this plan)
├── agents/
│   ├── dfm-router.agent.md
│   ├── cnc-machining.agent.md
│   ├── injection-molding.agent.md
│   ├── sheet-metal.agent.md
│   ├── 3d-printing.agent.md
│   ├── materials-selection.agent.md
│   ├── vertical-aerospace.agent.md
│   ├── vertical-medical.agent.md
│   ├── vertical-automotive-ev.agent.md
│   └── trends-strategy.agent.md
├── knowledge/
│   ├── cnc-machining/   (+ _index.md, 4 articles)
│   ├── injection-molding/   (+ _index.md, 8 articles)
│   ├── sheet-metal/   (+ _index.md, 1 article)
│   ├── 3d-printing/   (+ _index.md, 8 articles)
│   ├── materials/   (+ _index.md, 5 articles)
│   ├── verticals/   (+ _index.md, 4 articles)
│   └── trends/   (+ _index.md, 4 articles)
├── templates/
│   ├── dfm-eval-report.md
│   └── qa-response.md
├── intake/
│   └── _example-complex-machined.md
├── reference/
│   └── interview-prep/               # moved: existing .pptx/.pdf/.html files
└── .claude/
    ├── commands/
    │   ├── pl-dfm-review.md
    │   ├── pl-ask.md
    │   └── pl-refresh-kb.md
    └── skills/
        └── protolabs-router.md
```

## File formats (adopt the existing `Product Office` repo conventions)

Captured during Phase 1 exploration. Agents, skills, commands all use the same frontmatter + body structure defined in [CLAUDE.md](.claude/CLAUDE.md) of the current repo. Each agent frontmatter includes `loads:` (KB file paths) and `source_urls:` (ProtoLabs canonical URLs).

## Routing flow

```
user prompt ──► ProtoLab/CLAUDE.md (agent registry + keyword map)
         ──► dfm-router.agent.md classifies { process, mode, vertical? }
         ──► loads specialist agent + only its KB slice
         ──► emits templates/dfm-eval-report.md OR templates/qa-response.md
         ──► every claim cites a cached KB file + original ProtoLabs URL
```

## Articles to cache (v1 = 28)

| Folder | Articles |
|---|---|
| `cnc-machining/` | mastering-complex-features, cnc-tolerances, cnc-threading, cnc-for-prototypes |
| `injection-molding/` | moldability-fundamentals, moldability-complex-features, wall-thickness, overmolding-insert-molding, cosmetic-appearance, scientific-molding, liquid-silicone-rubber, thermoplastic-selection |
| `sheet-metal/` | designing-for-sheetmetal-fab-guide |
| `3d-printing/` | what-is-3d-printing, design-for-additive-manufacturing, 3dp-materials-selection, metal-3dp-materials, 3dp-end-use-production, vapor-smoothing, combining-part-assemblies, mjf-vs-sls |
| `materials/` | corrosion-resistant-metals, uv-resistant-plastics, glass-transition-temperature, im-material-alternatives, metal-fabrication-guide |
| `verticals/` | aerospace-manufacturing, medical-low-volume, reducing-automotive-weight, ev-future |
| `trends/` | innovation-in-manufacturing-2026, 3d-printing-trend-report, product-development-trends, industry-4-0 |

Each `_index.md` holds the canonical URL list so `/pl-refresh-kb [folder]` can re-scrape cleanly.

## Delivery phases

0. **Repo init + gitignore + README + relocate interview-prep files**
1. **Scaffold folders, root CLAUDE.md, two templates, example intake**
2. **Cache the 28 KB articles via WebFetch** (batched per folder, 3–4 parallel fetches at a time)
3. **Write the 10 agent files** with correct `loads:` wiring
4. **Write router skill + 3 slash commands**
5. **Run verification suite** (see below)
6. **Commit + push to `DimosGougousis/ProtoLabKB`**

Fully itemized in `C:\Users\dimos\ProtoLab\TODO.md` (60+ tasks, grouped by phase).

## Reuse (no reinvention)

- File-format conventions from the existing `C:\Users\dimos\Product Office\` repo (agent, skill, command templates).
- `WebFetch` for scraping; `trend-researcher` skill for ongoing trend updates.
- Progressive-loading rule pattern from the root `CLAUDE.md`.
- GitHub workflow: `gh repo` + `gh pr` patterns already documented in root `CLAUDE.md`.

## Verification (end-to-end, post-approval)

1. **Inventory check** — `ls knowledge/*/` confirms every expected article exists with non-empty `source_url` frontmatter. Count = 28.
2. **Design-eval golden test** — `intake/_example-complex-machined.md` defines a part with: 0.5mm on-axis hole, 0.9" deep × 0.05" wide groove, internal square corner, 8pt recessed text. Run `/pl-dfm-review intake/_example-complex-machined.md`. Expect: router → `cnc-machining`; report flags hole-depth ratio, corner radius, text size/depth; cites [mastering-complex-features-on-machined-parts](https://www.protolabs.com/resources/design-tips/mastering-complex-features-on-machined-parts/).
3. **Q&A golden test** — `/pl-ask "Minimum wall thickness for a PP injection-molded enclosure?"`. Expect: router → `injection-molding`; cites wall-thickness + moldability-fundamentals KB files.
4. **Ambiguity test** — `/pl-ask "Machine or 3D print this aerospace bracket?"`. Expect: comparative answer consulting CNC + 3DP + aerospace-vertical agents.
5. **KB refresh test** — `/pl-refresh-kb cnc-machining`. Expect: 4 URLs re-fetched, `fetched_at` bumped.
6. **Git push test** — `git status` clean after push; `gh repo view DimosGougousis/ProtoLabKB` shows committed files; default branch populated.

## Out of scope (v1)

- Direct STEP/STL geometry parsing (v1 = text descriptions only).
- Live ProtoLabs quoting / pricing integration.
- Scheduled KB refresh (manual `/pl-refresh-kb` only).
- CI workflow on the ProtoLabKB repo (add in v2).

## §5 — Per-Agent Compliance Guardrails (Phase 7)

### Design Rationale

Post-v1, we refactored compliance from a centralized `knowledge/compliance/regulatory-framework.md` into **per-process, per-vertical compliance files** loaded only when needed. This follows the progressive-loading principle and ensures agents only receive relevant regulatory context.

### Compliance Architecture

```
User prompt with compliance keywords
         │
         ▼
┌─────────────────────┐
│  CLAUDE.md router   │─── Sets regulated=true from keywords
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Specialist Agent   │─── Loads process KB + compliance files
│  (cnc/3dp/vertical) │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Template with       │─── {{#regulated}} conditionals
│ {{#regulated}}      │    render compliance sections
└─────────────────────┘
```

### Compliance File Organization

| Category | Files | Loaded By |
|----------|-------|-----------|
| **Export Controls** | `itar-ear-compliance.md` | CNC, 3DP, Materials, Verticals |
| **Quality Standards** | `iso-quality-standards.md` | CNC, 3DP, Verticals |
| **Cybersecurity** | `nist-cybersecurity-framework.md` | CNC, 3DP, Trends |
| **AI Governance** | `eu-ai-act-governance.md` | CNC, 3DP, Trends |
| **Biocompatibility** | `fda-biocompatibility.md` | 3DP, Medical |
| **Additive Export** | `additive-export-controls.md` | 3DP |
| **Additive Quality** | `additive-quality-standards.md` | 3DP |
| **Vertical** | `aerospace-compliance.md` | Aerospace |
| **Vertical** | `medical-compliance.md` | Medical |
| **Vertical** | `automotive-ev-compliance.md` | Automotive/EV |

### Template Conditionals

Both `dfm-eval-report.md` and `qa-response.md` wrap compliance sections in `{{#regulated}}` blocks:

```mustache
{{#regulated}}
## Regulatory Compliance Assessment
### Industry Context
- **Target Industry**: {{industry}}
- **Regulatory Frameworks**: {{regulatory_frameworks}}
...
{{/regulated}}
```

The router sets `regulated=true` when keywords like `ITAR`, `EAR`, `AS9100`, `FDA`, `ISO 13485`, `NIST`, `CMMC`, `GDPR`, or `EU AI Act` are detected in the user prompt.

### Keyword Detection (in CLAUDE.md)

```yaml
Compliance & Export Control Keywords (Sets regulated=true):
  ITAR: itar, defense, military, munitions, usml, export control...
  EAR: ear, export administration, eccn, dual-use...
  Aerospace: as9100, as9102, faa, far 25, nadcap...
  Medical: iso 13485, fda, 510k, pma, biocompatible...
  Automotive: iatf 16949, ppap, apqp, fmea...
  Cybersecurity: nist, cmmc, 800-171, cybersecurity...
  Environmental: rohs, reach, conflict minerals...
  AI Governance: eu ai act, ai act, ai governance...
  Data Protection: gdpr, data protection, privacy...
```
