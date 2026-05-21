# AIGP Plan 1: Foundation & Repo Hygiene

> **Status:** ready · **Duration:** ~2 weeks · **Depends on:** — · **Master plan:** [critically-review-and-recommend-starry-creek.md](./critically-review-and-recommend-starry-creek.md)

## Context

The AI Governance Platform repo at [github.com/DimosGougousis/ai-governance-platform](https://github.com/DimosGougousis/ai-governance-platform) is a solo-author prototype with **no license, no CI, no tests, schema-only audit, hardcoded policy logic in TS** (`packages/api/src/routes/governance.ts`). Before any real engineering can happen, the repo needs basic hygiene so contributors and CI can do credible work.

This plan is the **foundation phase** of a 6-plan, ~25-week implementation roadmap to transform the repo into a credible governance harness for 30 multi-agent execution patterns. See master plan for architectural context (5-plane harness, 8 governance archetype clusters, 5-tier risk model, 5-level trust verification).

## Goal

Bring the repo to a state where:
- A new engineer can clone it and have a working dev environment in <10 minutes
- CI green is a precondition for merge
- The README accurately describes what v3 architecture is and isn't
- Test infrastructure is in place (even if test coverage is initially low)

## Dependencies

None. This plan is the foundation; everything else depends on it.

## Deliverables

### 1. License (decide first)

Pick one before any other work starts:
- **Apache-2.0** — permissive, business-friendly, allows proprietary derivatives. Recommended default for max adoption.
- **AGPL-3.0** — copyleft, ensures derivative SaaS products stay open. Pick if open-source health matters more than corporate adoption.

Add `LICENSE` file at repo root; update `package.json` `license` field across all workspace packages; add SPDX license headers to source files via automation script.

### 2. CI pipeline (GitHub Actions)

Create `.github/workflows/ci.yml` with parallel jobs:
- `typecheck` — `pnpm typecheck` across all packages
- `lint` — `pnpm lint`
- `test` — `pnpm test --coverage`, upload to Codecov
- `build` — `pnpm build`, verify dist artifacts produced
- `docker-build` — build prod images, run smoke healthcheck

Coverage gate: changed-file coverage must be >70% for PR approval. Required status checks configured in branch protection.

### 3. Test framework

- Vitest configured per package with coverage via `@vitest/coverage-v8`
- `packages/test-utils/` shared utilities (DB fixtures, NATS mocks, agent mocks)
- Smoke tests for every existing route in `packages/api/src/routes/{agents,dashboard,governance}.ts`
- Smoke tests for one Next.js page

### 4. Linting + formatting

- ESLint config locked at repo root, extended per package
- Prettier config locked at repo root
- Husky + lint-staged pre-commit hook
- CI enforces both

### 5. ADR directory

Create `docs/adr/` with `template.md` plus first 5 ADRs:
- ADR-001: Five-plane harness architecture
- ADR-002: Apache AGE for lineage (vs Neo4j)
- ADR-003: OPA + YAML→Rego for policy DSL
- ADR-004: Risk-tier model (R0–R4) with 6 dimensions
- ADR-005: Trust verification levels (L0–L4)

Each ADR ≤2 pages. Reference the master plan for source decisions.

### 6. README rewrite

Honest current-state README:
- What the platform is (governance plane for external agents) and isn't (no agent runtime)
- Architecture diagram (Mermaid)
- Quick start: `pnpm i && pnpm dev` produces working stack
- Link to ADRs and master plan
- Roadmap section pointing to plans 2–6
- Contribution guide pointer

### 7. Governance documents

- `CONTRIBUTING.md` — dev workflow, PR template, conventional commits
- `CODE_OF_CONDUCT.md` — Contributor Covenant 2.1
- `SECURITY.md` — vulnerability reporting + security@ email
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/{bug.yml,feature.yml,question.yml}`

### 8. Docker Compose dev environment validation

- `docker-compose.dev.yml` brings up: Postgres+TimescaleDB 16, Redis 7, NATS JetStream, MinIO
- `docker-compose.prod.yml` validated for production deploy
- Healthchecks on all services
- Scripts: `pnpm dev:up`, `pnpm dev:down`, `pnpm dev:reset`, `pnpm dev:logs`

### 9. Existing schema audit

- Read all migrations in `packages/api/migrations/` and `packages/api/src/db/schema.ts`
- Identify dead tables, unused columns, naming inconsistencies
- Open GitHub issues per finding, tagged `tech-debt`
- Decisions deferred to plan 2 schema migration; document here

### 10. Repo workspace divergence resolution

There's a divergent local workspace at `C:\Users\dimos\AIGovernance` with auth/RBAC focus, not a clone of the GitHub repo. Decide:
- Merge useful elements (PM docs, executive presentation) into the GitHub repo
- Or formally archive the divergent workspace and document why
- Either way, eliminate the divergence so there's one source of truth

## Implementation tasks

Each task: write the change, verify locally, commit. No backlog.

1. Choose license → add `LICENSE` + update `package.json`
2. Add SPDX headers script + run it across packages
3. Create `.github/workflows/ci.yml` with `typecheck` job; verify on draft PR
4. Add `lint` job to CI
5. Add `test` job with coverage upload
6. Add `build` job
7. Add `docker-build` job
8. Configure required status checks in branch protection
9. Set up Vitest in `packages/api` with coverage; write 1 trivial test
10. Set up Vitest in `packages/web` with coverage; write 1 trivial test
11. Set up Vitest in `packages/shared`
12. Create `packages/test-utils/`
13. Write smoke tests for existing API routes
14. Lock ESLint at repo root, extend per package
15. Lock Prettier at repo root
16. Add Husky + lint-staged
17. Verify pre-commit hook fires on a known-bad commit
18. Create `docs/adr/template.md`
19. Write ADR-001 through ADR-005
20. Rewrite README with new architecture diagram
21. Create CONTRIBUTING / CODE_OF_CONDUCT / SECURITY
22. Create issue + PR templates
23. Validate `docker-compose.dev.yml` end-to-end
24. Validate `docker-compose.prod.yml` end-to-end
25. Add `pnpm dev:up/down/reset/logs` scripts
26. Schema audit walkthrough; open issues
27. Decide divergence resolution; execute decision

## Risk

**Low.** Repo hygiene is well-understood territory. Main risks:
- Bikeshedding on license choice — mitigated by deciding upfront
- Coverage gate set too strict, blocking velocity — start at 70%, raise later
- Husky pre-commit slow on large changes — add fast-path bypass for emergencies (`--no-verify` documented but discouraged)

## Acceptance criteria

- [ ] CI green on a trivial PR (e.g., dot in README)
- [ ] New contributor can `git clone && pnpm i && pnpm dev` and have working stack with all services healthy in <10 min
- [ ] Coverage gate enforced (>70% on changed files)
- [ ] All 5 initial ADRs written
- [ ] README accurately describes v3 architecture and current gaps
- [ ] License consistent across packages
- [ ] Pre-commit hook prevents non-formatted commits
- [ ] Schema audit issues opened
- [ ] Divergent workspace decision executed and documented

## Verification commands

```bash
# Clone-to-dev test (fresh directory)
git clone https://github.com/DimosGougousis/ai-governance-platform.git
cd ai-governance-platform
pnpm i
pnpm dev:up
sleep 30
curl http://localhost:4000/health
curl http://localhost:3000

# CI dry run
pnpm typecheck && pnpm lint && pnpm test && pnpm build

# Coverage
pnpm test --coverage
```

## Notes

- License decision must precede any other work in this plan.
- This plan does NOT include feature work; it only puts the repo in a state where feature work can be done credibly.
- The schema audit may surface follow-ups for plan 2's TimescaleDB migration.
- **Divergent workspace at `C:\Users\dimos\AIGovernance`** is not a clone of the GitHub repo. Resolution decision is part of this plan.
