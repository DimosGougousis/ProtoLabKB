# ProtoLabs Product Office — Execution Checklist

> Atomic, phase-ordered tasks. Check off with `- [x]` as completed.
> Design rationale and authoritative references: [`PLAN.md`](./PLAN.md).
> Status cheat: **◯ not started** · **◐ in progress** · **● done** · **✕ blocked**

Status: **◯ not started** (team review in progress, 2026-04-21).

---

## Phase 0 — Repo init & housekeeping

- [ ] 0.1 Confirm workspace root is `C:\Users\dimos\ProtoLab\` (PLAN §2.1)
- [ ] 0.2 Write `.gitignore` (node_modules, .DS_Store, slides_out/, *.tmp, .env)
- [ ] 0.3 Write `README.md` entry point (already drafted in review)
- [ ] 0.4 Relocate existing interview-prep files into `reference/interview-prep/` (pptx, pdf, html, build_deck.js, export_slides.ps1, slides_out/, _prep_readonly.md)
- [ ] 0.5 `git init` → set default branch `main`
- [ ] 0.6 `git remote add origin https://github.com/DimosGougousis/ProtoLabKB.git`
- [ ] 0.7 Commit: `chore: scaffold ProtoLabs Product Office (plan + readme)`
- [ ] 0.8 `git push -u origin main`
- [ ] 0.9 Verify: `gh repo view DimosGougousis/ProtoLabKB` shows populated default branch

## Phase 1 — Scaffold tree, CLAUDE.md, templates

- [ ] 1.1 Create folders: `agents/`, `knowledge/{cnc-machining,injection-molding,sheet-metal,3d-printing,materials,verticals,trends}/`, `templates/`, `intake/`, `.claude/commands/`, `.claude/skills/`
- [ ] 1.2 Write root `CLAUDE.md` (registry, keyword map, progressive-loading rule) — follows PLAN §6
- [ ] 1.3 Write `.claude/CLAUDE.md` (lists local commands + skills)
- [ ] 1.4 Write `templates/dfm-eval-report.md` per PLAN §7.3
- [ ] 1.5 Write `templates/qa-response.md` per PLAN §7.3
- [ ] 1.6 Write `intake/_example-complex-machined.md` fixture (spec in PLAN §9.2)
- [ ] 1.7 Seed each `knowledge/<folder>/_index.md` with the URLs from PLAN §4.1–§4.7
- [ ] 1.8 Commit: `feat: scaffold folder tree + CLAUDE.md + templates`

## Phase 2 — Cache the 28 KB articles (PLAN §4)

Contract: each file follows PLAN §7.2 frontmatter. Batch 4 parallel `WebFetch` calls per sub-phase.

- [ ] 2.1 CNC Machining — 4 files per PLAN §4.1
- [ ] 2.2 Injection Molding — 8 files per PLAN §4.2
- [ ] 2.3 Sheet Metal — 1 file per PLAN §4.3
- [ ] 2.4 3D Printing — 8 files per PLAN §4.4
- [ ] 2.5 Materials — 5 files per PLAN §4.5
- [ ] 2.6 Verticals — 4 files per PLAN §4.6
- [ ] 2.7 Trends — 4 files per PLAN §4.7
- [ ] 2.8 Inventory check: 28 articles exist, each `source_url` non-empty, body ≥ 500 chars
- [ ] 2.9 Commit: `feat: cache 28 ProtoLabs articles as local knowledge base`

## Phase 3 — Specialist agents (PLAN §5)

- [ ] 3.1 `agents/dfm-router.agent.md` — intent classifier per PLAN §6
- [ ] 3.2–3.10 Write the 9 specialist agents per PLAN §5.2–§5.10 (one commit per agent is fine)
- [ ] 3.11 Commit batch: `feat: add 10 ProtoLabs specialist agents`

## Phase 4 — Router skill + slash commands

- [ ] 4.1 `.claude/skills/protolabs-router.md` — keyword → agent resolution procedure
- [ ] 4.2 `.claude/commands/pl-dfm-review.md` — M1 entry point
- [ ] 4.3 `.claude/commands/pl-ask.md` — M2 entry point
- [ ] 4.4 `.claude/commands/pl-refresh-kb.md` — re-fetch URLs from `_index.md`
- [ ] 4.5 Commit: `feat: add router skill + 3 slash commands`

## Phase 5 — Verification (run tests from PLAN §9)

- [ ] 5.1 PLAN §9.1 — inventory check passes
- [ ] 5.2 PLAN §9.2 — M1 golden test passes
- [ ] 5.3 PLAN §9.3 — M2 golden test passes
- [ ] 5.4 PLAN §9.4 — ambiguity test passes
- [ ] 5.5 PLAN §9.5 — refresh test passes
- [ ] 5.6 Save run logs to `reference/verification-runs/2026-04-XX.md`

## Phase 6 — Publish

- [ ] 6.1 `git status` clean; all phase commits present
- [ ] 6.2 Tag: `v0.1.0-kb-scaffold`
- [ ] 6.3 `git push origin main --tags`
- [ ] 6.4 PLAN §9.6 — publish verification passes
- [ ] 6.5 `gh repo edit DimosGougousis/ProtoLabKB --description "ProtoLabs Product Office — routing agents + cached DFM knowledge base"`
- [ ] 6.6 Open summary issue on ProtoLabKB listing agent inventory + KB coverage

## Post-v1 backlog (PLAN §11)

- [ ] CI: link checker on `_index.md` URLs + frontmatter validator
- [ ] STEP/STL geometry parsing for true CAD-driven DFM
- [ ] Scheduled KB refresh via `scheduled-tasks` MCP
- [ ] ProtoLabs live quoting integration (if API access granted)
- [ ] Additional verticals (defense, consumer electronics)
