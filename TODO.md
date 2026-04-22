# ProtoLabs Product Office — Execution Checklist

> Atomic, phase-ordered tasks. Check off with `- [x]` as completed.
> Design rationale and authoritative references: [`PLAN.md`](./PLAN.md).
> Status cheat: **◯ not started** · **◐ in progress** · **● done** · **✕ blocked**

Status: **● done** Phases 0-6 completed. Phase 7 (compliance guardrails refactor) in progress.

---

## Phase 0 — Repo init & housekeeping ✅

- [x] 0.1 Confirm workspace root is `C:\Users\dimos\ProtoLab\` (PLAN §2.1)
- [x] 0.2 Write `.gitignore` (node_modules, .DS_Store, slides_out/, *.tmp, .env)
- [x] 0.3 Write `README.md` entry point (already drafted in review)
- [x] 0.4 Relocate existing interview-prep files into `reference/interview-prep/` (pptx, pdf, html, build_deck.js, export_slides.ps1, slides_out/, _prep_readonly.md)
- [x] 0.5 `git init` → set default branch `main`
- [x] 0.6 `git remote add origin https://github.com/DimosGougousis/ProtoLabKB.git`
- [x] 0.7 Commit: `chore: scaffold ProtoLabs Product Office (plan + readme)`
- [x] 0.8 `git push -u origin main`
- [x] 0.9 Verify: `gh repo view DimosGougousis/ProtoLabKB` shows populated default branch

## Phase 1 — Scaffold tree, CLAUDE.md, templates ✅

- [x] 1.1 Create folders: `agents/`, `knowledge/{cnc-machining,injection-molding,sheet-metal,3d-printing,materials,verticals,trends}/`, `templates/`, `intake/`, `.claude/commands/`, `.claude/skills/`
- [x] 1.2 Write root `CLAUDE.md` (registry, keyword map, progressive-loading rule) — follows PLAN §6
- [x] 1.3 Write `.claude/CLAUDE.md` (lists local commands + skills)
- [x] 1.4 Write `templates/dfm-eval-report.md` per PLAN §7.3
- [x] 1.5 Write `templates/qa-response.md` per PLAN §7.3
- [x] 1.6 Write `intake/_example-complex-machined.md` fixture (spec in PLAN §9.2)
- [x] 1.7 Seed each `knowledge/<folder>/_index.md` with the URLs from PLAN §4.1–§4.7
- [x] 1.8 Commit: `feat: scaffold folder tree + CLAUDE.md + templates`

## Phase 2 — Cache the 28 KB articles (PLAN §4) ✅

Contract: each file follows PLAN §7.2 frontmatter. Batch 4 parallel `WebFetch` calls per sub-phase.

- [x] 2.1 CNC Machining — 4 files per PLAN §4.1
- [x] 2.2 Injection Molding — 8 files per PLAN §4.2
- [x] 2.3 Sheet Metal — 1 file per PLAN §4.3
- [x] 2.4 3D Printing — 8 files per PLAN §4.4
- [x] 2.5 Materials — 5 files per PLAN §4.5
- [x] 2.6 Verticals — 4 files per PLAN §4.6
- [x] 2.7 Trends — 4 files per PLAN §4.7
- [x] 2.8 Inventory check: 28 articles exist, each `source_url` non-empty, body ≥ 500 chars
- [x] 2.9 Commit: `feat: cache 28 ProtoLabs articles as local knowledge base`

## Phase 3 — Specialist agents (PLAN §5) ✅

- [x] 3.1 `agents/dfm-router.agent.md` — intent classifier per PLAN §6
- [x] 3.2–3.10 Write the 9 specialist agents per PLAN §5.2–§5.10 (one commit per agent is fine)
- [x] 3.11 Commit batch: `feat: add 10 ProtoLabs specialist agents`

## Phase 4 — Router skill + slash commands ✅

- [x] 4.1 `.claude/skills/protolabs-router.md` — keyword → agent resolution procedure
- [x] 4.2 `.claude/commands/pl-dfm-review.md` — M1 entry point
- [x] 4.3 `.claude/commands/pl-ask.md` — M2 entry point
- [x] 4.4 `.claude/commands/pl-refresh-kb.md` — re-fetch URLs from `_index.md`
- [x] 4.5 Commit: `feat: add router skill + 3 slash commands`

## Phase 5 — Verification (run tests from PLAN §9) ✅

- [x] 5.1 PLAN §9.1 — inventory check passes
- [x] 5.2 PLAN §9.2 — M1 golden test passes
- [x] 5.3 PLAN §9.3 — M2 golden test passes
- [x] 5.4 PLAN §9.4 — ambiguity test passes
- [x] 5.5 PLAN §9.5 — refresh test passes
- [x] 5.6 Save run logs to `reference/verification-runs/2026-04-XX.md`

## Phase 6 — Publish ✅

- [x] 6.1 `git status` clean; all phase commits present
- [x] 6.2 Tag: `v0.1.0-kb-scaffold`
- [x] 6.3 `git push origin main --tags`
- [x] 6.4 PLAN §9.6 — publish verification passes
- [x] 6.5 `gh repo edit DimosGougousis/ProtoLabKB --description "ProtoLabs Product Office — routing agents + cached DFM knowledge base"`
- [x] 6.6 Open summary issue on ProtoLabKB listing agent inventory + KB coverage

## Phase 7 — Per-Agent Compliance Guardrails (Post-v1 Refactor) ✅

- [x] 7.1 Add frontmatter to 4 CNC compliance files (source_url, fetched_at, type)
- [x] 7.2 Retire orphan: knowledge/compliance/regulatory-framework.md (content moved to per-process files)
- [x] 7.3 Extract 3DP inline compliance to 3 new KB files (fda-biocompatibility, additive-export-controls, additive-quality-standards)
- [x] 7.4 Slim 3D Printing agent - replace inline with loads: references
- [x] 7.5 Create 3 vertical compliance KB files (aerospace-compliance, medical-compliance, automotive-ev-compliance)
- [x] 7.6 Update vertical agents with compliance loads: (wire up the new KB files)
- [x] 7.7 Wrap template compliance sections in {{#regulated}} conditionals
- [x] 7.8 Update CLAUDE.md with compliance routing keywords (sets regulated=true)
- [x] 7.9 Update PLAN.md §5 to reflect per-agent guardrails decision
- [x] 7.10 Update README.md status and add compliance coverage rows
- [x] 7.11 Update TODO.md mark Phases 0-6 ☑ and add Phase 7
- [x] 7.12 Commit and push all changes

## Post-v1 backlog (PLAN §11)

- [ ] CI: link checker on `_index.md` URLs + frontmatter validator
- [ ] STEP/STL geometry parsing for true CAD-driven DFM
- [ ] Scheduled KB refresh via `scheduled-tasks` MCP
- [ ] ProtoLabs live quoting integration (if API access granted)
- [ ] Additional verticals (defense, consumer electronics)
