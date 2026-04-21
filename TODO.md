# ProtoLabs Product Office — Delivery Checklist

> Exhaustive, phase-ordered todo list for standing up the ProtoLabs knowledge-base + agents in this workspace (`C:\Users\dimos\ProtoLab\`) and publishing to [DimosGougousis/ProtoLabKB](https://github.com/DimosGougousis/ProtoLabKB).
>
> **Convention:** each task is atomic (~2–10 min). Check off with `- [x]` as completed. Reference full architecture in `PLAN.md`.

---

## Phase 0 — Repo init & housekeeping

- [ ] 0.1 Confirm `C:\Users\dimos\ProtoLab\` is the target workspace
- [ ] 0.2 Create `.gitignore` (node_modules, .DS_Store, slides_out/, *.tmp)
- [ ] 0.3 Create `README.md` (project purpose, how to load, agent list, verification quickstart)
- [ ] 0.4 Copy `PLAN.md` into the workspace (from `~/.claude/plans/i-want-to-set-tranquil-thunder.md`)
- [ ] 0.5 Create `reference/interview-prep/` and move existing `.pptx`, `.pdf`, `.html`, `build_deck.js`, `export_slides.ps1`, `slides_out/`, `_prep_readonly.md` into it
- [ ] 0.6 `git init` and set `main` as default branch
- [ ] 0.7 `git remote add origin https://github.com/DimosGougousis/ProtoLabKB.git`
- [ ] 0.8 Initial commit: "chore: scaffold ProtoLabs Product Office (plan + readme)"
- [ ] 0.9 `git push -u origin main`
- [ ] 0.10 Verify push via `gh repo view DimosGougousis/ProtoLabKB`

## Phase 1 — Scaffold directory tree, root CLAUDE.md, templates

- [ ] 1.1 Create folder tree: `agents/`, `knowledge/{cnc-machining,injection-molding,sheet-metal,3d-printing,materials,verticals,trends}/`, `templates/`, `intake/`, `.claude/commands/`, `.claude/skills/`
- [ ] 1.2 Write `CLAUDE.md` (entry point) — doc index, agent registry table, routing keywords, progressive-loading rule
- [ ] 1.3 Write `.claude/CLAUDE.md` — list commands + skills (project-local)
- [ ] 1.4 Write `templates/dfm-eval-report.md` (part summary, rule-check table, critical issues, recommendations, score, sources)
- [ ] 1.5 Write `templates/qa-response.md` (answer, key rules, caveats, sources)
- [ ] 1.6 Write `intake/_example-complex-machined.md` (test case: 0.5mm hole, 0.9"×0.05" groove, square corners, 8pt recessed text)
- [ ] 1.7 Seed each `knowledge/<folder>/_index.md` with the canonical URL registry for that folder
- [ ] 1.8 Commit: "feat: scaffold folder tree + CLAUDE.md + templates"

## Phase 2 — Cache the 28 ProtoLabs articles (WebFetch → markdown)

**Contract per file:** frontmatter `source_url`, `fetched_at`, `process`, `summary`; body = faithful markdown of the article.

### CNC Machining (4)
- [ ] 2.1 `knowledge/cnc-machining/mastering-complex-features.md` — <https://www.protolabs.com/resources/design-tips/mastering-complex-features-on-machined-parts/>
- [ ] 2.2 `knowledge/cnc-machining/cnc-tolerances.md`
- [ ] 2.3 `knowledge/cnc-machining/cnc-threading.md`
- [ ] 2.4 `knowledge/cnc-machining/cnc-for-prototypes.md` — <https://www.protolabs.com/resources/guides-and-trend-reports/cnc-machining-for-prototypes-and-low-volume-production-parts/>

### Injection Molding (8)
- [ ] 2.5 `knowledge/injection-molding/moldability-fundamentals.md` — <https://www.protolabs.com/resources/guides-and-trend-reports/designing-for-moldability-fundamental-elements/>
- [ ] 2.6 `knowledge/injection-molding/moldability-complex-features.md` — <https://www.protolabs.com/resources/guides-and-trend-reports/designing-for-moldability-complex-features/>
- [ ] 2.7 `knowledge/injection-molding/wall-thickness.md` — <https://www.protolabs.com/resources/design-tips/solving-wall-thickness-issues-in-molded-parts/>
- [ ] 2.8 `knowledge/injection-molding/overmolding-insert-molding.md` — <https://www.protolabs.com/resources/guides-and-trend-reports/overmolding-and-insert-molding/>
- [ ] 2.9 `knowledge/injection-molding/cosmetic-appearance.md` — <https://www.protolabs.com/resources/guides-and-trend-reports/enhancing-cosmetic-appearance-on-molded-parts/>
- [ ] 2.10 `knowledge/injection-molding/scientific-molding.md` — <https://www.protolabs.com/resources/guides-and-trend-reports/scientific-molding-helps-ensure-repeatable-part-function/>
- [ ] 2.11 `knowledge/injection-molding/liquid-silicone-rubber.md` — <https://www.protolabs.com/resources/guides-and-trend-reports/design-considerations-for-liquid-silicone-rubber/>
- [ ] 2.12 `knowledge/injection-molding/thermoplastic-selection.md` — <https://www.protolabs.com/resources/guides-and-trend-reports/thermoplastic-material-selection-for-injection-molding/>

### Sheet Metal (1)
- [ ] 2.13 `knowledge/sheet-metal/designing-for-sheetmetal-fab-guide.md` — <https://www.protolabs.com/media/k4upqp5j/designing-for-sheetmetal-fab-guide-2018.pdf>

### 3D Printing (8)
- [ ] 2.14 `knowledge/3d-printing/what-is-3d-printing.md` — <https://www.protolabs.com/resources/guides-and-trend-reports/what-is-3d-printing/>
- [ ] 2.15 `knowledge/3d-printing/design-for-additive-manufacturing.md` — <https://www.protolabs.com/resources/guides-and-trend-reports/what-is-design-for-additive-manufacturing/>
- [ ] 2.16 `knowledge/3d-printing/3dp-materials-selection.md` — <https://www.protolabs.com/resources/guides-and-trend-reports/selecting-the-right-material-for-3d-printing/>
- [ ] 2.17 `knowledge/3d-printing/metal-3dp-materials.md` — <https://www.protolabs.com/resources/guides-and-trend-reports/metal-3d-printing-materials-guide/>
- [ ] 2.18 `knowledge/3d-printing/3dp-end-use-production.md` — <https://www.protolabs.com/resources/guides-and-trend-reports/3d-printing-for-end-use-production/>
- [ ] 2.19 `knowledge/3d-printing/vapor-smoothing.md` — <https://www.protolabs.com/resources/design-tips/why-you-should-use-vapor-smoothing-on-3d-printed-parts/>
- [ ] 2.20 `knowledge/3d-printing/combining-part-assemblies.md` — <https://www.protolabs.com/resources/guides-and-trend-reports/combining-part-assemblies-with-additive-manufacturing/>
- [ ] 2.21 `knowledge/3d-printing/mjf-vs-sls.md`

### Materials (5)
- [ ] 2.22 `knowledge/materials/corrosion-resistant-metals.md` — <https://www.protolabs.com/resources/design-tips/finding-the-right-corrosion-resistant-metals/>
- [ ] 2.23 `knowledge/materials/uv-resistant-plastics.md` — <https://www.protolabs.com/resources/design-tips/uv-resistant-plastics/>
- [ ] 2.24 `knowledge/materials/glass-transition-temperature.md` — <https://www.protolabs.com/resources/design-tips/glass-transition-temperature-of-polymers/>
- [ ] 2.25 `knowledge/materials/im-material-alternatives.md` — <https://www.protolabs.com/resources/guides-and-trend-reports/material-alternatives-for-plastic-injection-molding/>
- [ ] 2.26 `knowledge/materials/metal-fabrication-guide.md` — <https://www.protolabs.com/resources/guides-and-trend-reports/metal-fabrication-a-guide-to-manufacturing-metal-parts/>

### Verticals (4)
- [ ] 2.27 `knowledge/verticals/aerospace-manufacturing.md` — <https://www.protolabs.com/resources/guides-and-trend-reports/aerospace-manufacturing-methods-for-prototyping-and-production/>
- [ ] 2.28 `knowledge/verticals/medical-low-volume.md` — <https://www.protolabs.com/resources/guides-and-trend-reports/prototyping-and-low-volume-production-for-medical-applications/>
- [ ] 2.29 `knowledge/verticals/reducing-automotive-weight.md` — <https://www.protolabs.com/resources/guides-and-trend-reports/reducing-component-weight-for-automotive-applications/>
- [ ] 2.30 `knowledge/verticals/ev-future.md` — <https://www.protolabs.com/resources/guides-and-trend-reports/charging-toward-an-electric-vehicle-future/>

### Trends (4)
- [ ] 2.31 `knowledge/trends/innovation-in-manufacturing-2026.md` — <https://www.protolabs.com/resources/guides-and-trend-reports/innovation-in-manufacturing-2026/>
- [ ] 2.32 `knowledge/trends/3d-printing-trend-report.md` — <https://www.protolabs.com/resources/guides-and-trend-reports/3d-printing-trend-report/>
- [ ] 2.33 `knowledge/trends/product-development-trends.md` — <https://www.protolabs.com/resources/guides-and-trend-reports/product-development-trends/>
- [ ] 2.34 `knowledge/trends/industry-4-0.md` — <https://www.protolabs.com/resources/guides-and-trend-reports/data-digital-threads-and-industry-4-0/>

- [ ] 2.35 Inventory check: 28 files, each with non-empty `source_url` + body > 500 chars
- [ ] 2.36 Commit: "feat: cache 28 ProtoLabs resource articles as local knowledge base"

## Phase 3 — Write specialist agents (10)

- [ ] 3.1 `agents/dfm-router.agent.md` — intent classifier (keywords → {process, mode, vertical})
- [ ] 3.2 `agents/cnc-machining.agent.md` — loads CNC KB + metals; DFM rule set with numeric thresholds
- [ ] 3.3 `agents/injection-molding.agent.md` — loads IM KB + thermoplastics + LSR
- [ ] 3.4 `agents/sheet-metal.agent.md` — loads sheet-metal KB + metals
- [ ] 3.5 `agents/3d-printing.agent.md` — loads 3DP KB + metal-3dp materials
- [ ] 3.6 `agents/materials-selection.agent.md` — loads materials KB; cross-process
- [ ] 3.7 `agents/vertical-aerospace.agent.md` — loads verticals/aerospace + CNC + 3DP slices
- [ ] 3.8 `agents/vertical-medical.agent.md` — loads verticals/medical + LSR + biocompatible materials
- [ ] 3.9 `agents/vertical-automotive-ev.agent.md` — loads verticals/automotive + EV
- [ ] 3.10 `agents/trends-strategy.agent.md` — loads trends KB; used for strategic context
- [ ] 3.11 Commit: "feat: add 10 ProtoLabs specialist agents"

## Phase 4 — Router skill + slash commands

- [ ] 4.1 `.claude/skills/protolabs-router.md` — procedure for keyword extraction → agent resolution
- [ ] 4.2 `.claude/commands/pl-dfm-review.md` — `/pl-dfm-review <path|description>` → router → agent → DFM eval report
- [ ] 4.3 `.claude/commands/pl-ask.md` — `/pl-ask <question>` → router → agent → Q&A response
- [ ] 4.4 `.claude/commands/pl-refresh-kb.md` — `/pl-refresh-kb [folder]` → re-WebFetch URLs in `_index.md`
- [ ] 4.5 Commit: "feat: add router skill + 3 slash commands"

## Phase 5 — Verification suite

- [ ] 5.1 Inventory: `ls knowledge/*/*.md | wc -l` == 28 (+ 7 indexes = 35 total)
- [ ] 5.2 Frontmatter audit: each KB file has `source_url` + `fetched_at`
- [ ] 5.3 Run `/pl-dfm-review intake/_example-complex-machined.md` → expect CNC routing + hole-depth / radius / text-size flags citing the mastering-complex-features article
- [ ] 5.4 Run `/pl-ask "Minimum wall thickness for a PP injection-molded enclosure?"` → expect IM routing + wall-thickness + moldability citations
- [ ] 5.5 Run `/pl-ask "Machine or 3D print this aerospace bracket?"` → expect comparative answer across CNC + 3DP + aerospace-vertical
- [ ] 5.6 Run `/pl-refresh-kb cnc-machining` → verify `fetched_at` bumped on all 4 CNC files
- [ ] 5.7 Document verification outputs in `reference/verification-runs/<date>.md`

## Phase 6 — Final commit & GitHub publish

- [ ] 6.1 `git status` clean; all phase commits present
- [ ] 6.2 Tag release: `v0.1.0-kb-scaffold`
- [ ] 6.3 `git push origin main --tags`
- [ ] 6.4 Open a summary issue on ProtoLabKB listing agent inventory + KB coverage
- [ ] 6.5 Update repo description via `gh repo edit DimosGougousis/ProtoLabKB --description "ProtoLabs Product Office — routing agents + cached DFM knowledge base"`
- [ ] 6.6 Verify on GitHub web UI: README renders, agent files visible, knowledge tree browsable

## Post-v1 (not blocking)

- [ ] Add CI (link checker on `_index.md` URLs, frontmatter validator)
- [ ] STEP/STL geometry parsing for true CAD-driven DFM
- [ ] Scheduled KB refresh via cron / scheduled-tasks MCP
- [ ] Integrate with ProtoLabs live quoting (if API access granted)
