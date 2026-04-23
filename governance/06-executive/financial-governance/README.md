---
status: archived
moved_to: ../../_archive/financial-governance/
reason: The financial-governance sub-pillar was designed for token-economics in LLM-heavy SaaS products with high per-call costs (e.g., customer-facing chatbots running at scale). The ProtoLab agent system is an internal reference/demo with no production LLM billing surface and no live quoting API. These artifacts are preserved in _archive/ for future reinstatement if the ProtoLabs AI program moves to production LLM workloads or adds the quote-bot described in `../../protolabs/quote-bot-financial-guardrails.md`.
---

# Financial Governance — Archived (Stub Redirect)

Both artifacts from the upstream `06-executive/financial-governance/` sub-pillar have been moved to `../../_archive/financial-governance/`:

- `cost-attribution-dashboard.md` → `../../_archive/financial-governance/cost-attribution-dashboard.md`
- `token-usage-forecast.md` → `../../_archive/financial-governance/token-usage-forecast.md`

## Why Archived

The ProtoLab agent system (v0.1.0) is a **reference/demo system** running declarative Markdown + YAML agents. It does not yet:

- Bill customers per token or per agent invocation
- Run at scale where per-call LLM costs are material
- Expose a live quoting API that would trigger cost attribution across cost centers

## Forward-Looking Replacement

When the ProtoLabs AI program moves to live production workloads — in particular the not-yet-built **quote-bot** — the authoritative control is:

- `../../protolabs/quote-bot-financial-guardrails.md` (cost ceilings, variance thresholds, autonomy locked at A4 "recommend only")

At that point these two archived files should be re-examined, adapted with Protolabs cost-center mappings, and returned to active status.
