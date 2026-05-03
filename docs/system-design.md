# ProtoLab — System Design

> A comprehensive architectural overview of the ProtoLabs Product Office AI system for manufacturing design-for-manufacturability (DFM) guidance, AI governance, and strategic implementation.

---

## 1. System Overview

**ProtoLab** is an AI-powered knowledge-base and agent system that mirrors ProtoLabs' manufacturing resources library. It routes user prompts about parts, designs, materials, processes, and verticals to specialist agents that load cached ProtoLabs guidance and either:

1. **Evaluate a design** against ProtoLabs DFM rules, or
2. **Answer Q&A** grounded in cached ProtoLabs articles with source citations.

The system sits at the intersection of **manufacturing expertise**, **AI governance**, and **strategic product management** — providing DFM evaluation, compliance assessment, use-case discovery, and workshop facilitation.

---

## 2. Architectural Principles

| Principle | Rationale |
|-----------|-----------|
| **Domain-first routing** | Parse user intent for process, mode, and vertical before selecting an agent |
| **Progressive loading** | Load only the KB files and agent definitions required for the current request |
| **Source-grounded output** | Every claim cites a cached KB file + original ProtoLabs URL |
| **Governance by design** | Every agent has a risk registry, KILLSWITCH, and SAFEST coverage assessment |
| **Compliance-aware** | Regulated contexts (ITAR, EAR, FDA, EU AI Act) trigger conditional output templates |
| **Extensibility** | New agents, KB articles, and commands are added via convention-driven file placement |

---

## 3. System Architecture (C4 — Container Level)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              USER INTERFACE LAYER                            │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐ │
│  │ /pl-dfm-    │  │ /pl-ask     │  │ /pl-govern- │  │ /pl-funnel-intake   │ │
│  │   review    │  │             │  │   ance      │  │ /pl-agentic-tpm     │ │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘  │ /pl-use-case-explorer│ │
│         │                │                │         │ /pl-feasibility-probe │ │
│         │                │                │         │ /pl-rehearse          │ │
│         └────────────────┴────────────────┘         └─────────────────────┘ │
│                              │                                               │
└──────────────────────────────┼───────────────────────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                              ROUTING LAYER                                   │
│  ┌─────────────────────────────────────────────────────────────────────────┐ │
│  │                    protolabs-router (Skill)                              │ │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────────┐ │
│  │  │ Keyword     │  │ Intent      │  │ Agent       │  │ KB Slice        │ │
│  │  │ Parser      │→ │ Classifier  │→ │ Resolver    │→ │ Loader          │ │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────────┘ │
│  └─────────────────────────────────────────────────────────────────────────┘ │
└──────────────────────────────┬───────────────────────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                              AGENT LAYER                                     │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────────┐   │
│  │ dfm-     │ │ cnc-     │ │ injection│ │ sheet-   │ │ 3d-printing      │   │
│  │ router   │ │ machining│ │ molding  │ │ metal    │ │                  │   │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘ └──────────────────┘   │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────────┐   │
│  │ materials│ │ vertical │ │ vertical │ │ vertical │ │ trends-strategy  │   │
│  │ selection│ │ aerospace│ │ medical  │ │ auto/ev  │ │                  │   │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘ └──────────────────┘   │
│  ┌────────────────────────────────────────────────────────────────────────┐  │
│  │ change-management-orchestrator (bypasses router for cobot keywords)    │  │
│  └────────────────────────────────────────────────────────────────────────┘  │
└──────────────────────────────┬───────────────────────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           KNOWLEDGE BASE LAYER                               │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐            │
│  │ cnc-        │ │ injection-  │ │ sheet-      │ │ 3d-         │            │
│  │ machining   │ │ molding     │ │ metal       │ │ printing    │            │
│  │ (4 articles)│ │ (8 articles)│ │ (1 article) │ │ (8 articles)│            │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘            │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐            │
│  │ materials   │ │ verticals   │ │ trends      │ │ compliance  │            │
│  │ (5 articles)│ │ (4 articles)│ │ (4 articles)│ │ (14+ files) │            │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘            │
│  ┌─────────────┐ ┌─────────────┐                                            │
│  │ cad         │ │ ai          │                                            │
│  │ (CAD KB)    │ │ (AI KB)     │                                            │
│  └─────────────┘ └─────────────┘                                            │
└──────────────────────────────┬───────────────────────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           GOVERNANCE LAYER                                   │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐            │
│  │ 00-Getting  │ │ 01-Discovery│ │ 02-Develop- │ │ 03-Runtime  │            │
│  │   Started   │ │  Governance │ │   ment Gov  │ │  Governance │            │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘            │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐            │
│  │ 04-Opera-   │ │ 05-Cross-   │ │ 06-Executive│ │ 07-Enter-   │            │
│  │   tional    │ │   Cutting   │ │             │ │   prise     │            │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘            │
│  ┌────────────────────────────────────────────────────────────────────────┐  │
│  │ protolabs/ — Agent risk registry, SAFEST matrix, KILLSWITCH files,    │  │
│  │              source-grounding contracts, KB freshness SLAs,           │  │
│  │              red-team playbook, DFM accuracy eval suite               │  │
│  └────────────────────────────────────────────────────────────────────────┘  │
└──────────────────────────────┬───────────────────────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           OUTPUT LAYER                                       │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐            │
│  │ dfm-eval-   │ │ qa-response │ │ compliance- │ │ funnel-     │            │
│  │   report    │ │             │ │ assessment  │ │   canvas    │            │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘            │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Component Breakdown

### 4.1 User Interface Layer — Commands

| Command | Trigger | Output Template | Primary Agent |
|---------|---------|-----------------|---------------|
| `/pl-dfm-review` | Part description or file path | `dfm-eval-report.md` | Process-specific DFM agent |
| `/pl-ask` | Manufacturing question | `qa-response.md` | Process-specific Q&A agent |
| `/pl-strategy` | Trend or strategy topic | `qa-response.md` | `trends-strategy` |
| `/pl-governance` | Assessment type + scope | `compliance-assessment.md` | Governance framework |
| `/pl-assess` | Target + criteria | Combined DFM + governance | Multi-agent orchestration |
| `/pl-refresh-kb` | Folder (optional) | Refresh confirmation | N/A — file operation |
| `/pl-funnel-intake` | Use-case description | 6-box canvas + 4 appendices | `pl-funnel-intake` skill |
| `/pl-agentic-tpm` | Use-case description | 12-section canvas + YAML | `agentic-tpm` skill |
| `/pl-use-case-explorer` | Domain | Scored candidate table | `pl-use-case-explorer` skill |
| `/pl-feasibility-probe` | Use-case | Architecture sketch | `pl-feasibility-probe` skill |
| `/pl-rehearse` | Use-case | Pushback simulation | `pl-rehearse` skill |

### 4.2 Routing Layer — `protolabs-router` Skill

The router is the central nervous system. It performs four operations in sequence:

1. **Keyword Parser** — Scans input for process, mode, vertical, and compliance keywords
2. **Intent Classifier** — Determines if the request is a design evaluation, Q&A, strategy discussion, or governance assessment
3. **Agent Resolver** — Maps the classified intent to a specialist agent ID
4. **KB Slice Loader** — Loads only the KB files specified in the agent's `loads:` frontmatter

**Special routing rule**: If change management keywords (cobot, workforce transformation, resistant engineers) are detected, the router bypasses normal classification and loads `change-management-orchestrator.agent.md` directly.

### 4.3 Agent Layer — 11 Specialist Agents

| Agent ID | Domain | KB Articles Loaded | Compliance Coverage |
|----------|--------|-------------------|---------------------|
| `dfm-router` | Intent classification | — | Sets `regulated` flag |
| `cnc-machining` | CNC DFM evaluation | 4 CNC + compliance | ITAR, EAR, ISO 9001/13485/AS9100, NIST, GDPR |
| `injection-molding` | Injection molding DFM | 8 IM + compliance | ITAR, EAR, ISO 9001/13485/AS9100/IATF 16949, NIST, GDPR |
| `sheet-metal` | Sheet metal DFM | 1 sheet metal + compliance | ITAR, EAR, ISO 9001/AS9100, NIST, GDPR, RoHS, REACH |
| `3d-printing` | 3D printing DFM | 8 3DP + compliance | ITAR, EAR, ISO 9001/13485/AS9100, NIST, GDPR, EU AI Act |
| `materials-selection` | Material recommendations | 5 materials + compliance | Export controls, biocompatibility, aerospace/medical/automotive certs |
| `vertical-aerospace` | Aerospace guidance | Aerospace vertical + compliance | AS9100D, FAR 25, NADCAP, ITAR/EAR |
| `vertical-medical` | Medical device guidance | Medical vertical + compliance | FDA 21 CFR 820, ISO 13485, EU MDR, biocompatibility |
| `vertical-automotive-ev` | Automotive/EV guidance | Automotive + EV + compliance | IATF 16949, UNECE R100, PPAP, APQP, RoHS/REACH |
| `trends-strategy` | Strategic trend analysis | Trends KB + compliance | Regulatory trend monitoring, AI governance, cybersecurity |
| `change-management-orchestrator` | Cobot adoption | Change management KB | Workforce transformation, behavioral change |

Each agent file contains:
- **YAML frontmatter** with `loads:` (KB paths) and `source_urls:` (canonical URLs)
- **Procedure section** defining design eval vs Q&A workflow
- **Output template reference** (`dfm-eval-report.md` or `qa-response.md`)

### 4.4 Knowledge Base Layer — 68+ Articles

| Folder | Count | Content |
|--------|-------|---------|
| `knowledge/cnc-machining/` | 4 | Complex features, tolerances, threading, prototypes |
| `knowledge/injection-molding/` | 8 | Moldability, wall thickness, overmolding, LSR, materials |
| `knowledge/sheet-metal/` | 1 | Sheet metal fabrication guide |
| `knowledge/3d-printing/` | 8 | Design for AM, materials, end-use production, MJF vs SLS |
| `knowledge/materials/` | 5 | Corrosion-resistant metals, UV plastics, glass transition |
| `knowledge/verticals/` | 4 | Aerospace, medical, automotive, EV |
| `knowledge/trends/` | 4 | 2026 innovation, Industry 4.0, product development |
| `knowledge/compliance/` | 14+ | ITAR, EAR, ISO, FDA, NIST, GDPR, EU AI Act, RoHS, REACH |
| `knowledge/cad/` | — | CAD parsing, feature recognition, VLM integration |
| `knowledge/ai/` | — | AI governance, prompt injection, adversarial defense |

Each article is a markdown file with:
- `source_url` frontmatter — canonical ProtoLabs URL
- `fetched_at` frontmatter — cache timestamp
- Body — extracted article content

### 4.5 Governance Layer — 7-Stage Framework

The governance framework is a Protolabs-specific adaptation of the ProductGovernance4AgenticWorkflows framework:

| Stage | Question | Key Artifacts |
|-------|----------|---------------|
| **00 — Getting Started** | How do we begin? | Lifecycle canvas, navigation guide |
| **01 — Discovery Governance** | Should we build it? | Risk registry, feasibility gates |
| **02 — Development Governance** | How do we build it safely? | Skill manifests, SAFEST assessments |
| **03 — Runtime Governance** | How do we protect it live? | KILLSWITCH files, guardrails, monitoring |
| **04 — Operational Governance** | How do we respond to incidents? | Incident response, audit trails, regulatory mapping |
| **05 — Cross-Cutting** | What applies everywhere? | Glossary, RACI, regulatory index |
| **06 — Executive** | What does the board see? | T1–T4 dashboards, quarterly reports |
| **07 — Enterprise Implementation** | How do we scale? | Org model, process integration, risk-based adoption |

**Protolabs-specific governance artifacts** (`governance/protolabs/`):
- `agent-risk-registry.yaml` — ARI-scored registry of all 10 DFM agents
- `safest-coverage-matrix.md` — 10 × 112 SAFEST coverage matrix
- `customer-cad-ip-protection-guardrail.md` — Customer IP protection rules
- `dfm-accuracy-eval-suite.yaml` — Golden-set evaluation anchored on bracket fixture
- `source-grounding-data-contract.yaml` — Formalizes "cite KB + source_url" rule
- `red-team-playbook-dfm-agents.md` — 20–30 adversarial test cases
- `kb-freshness-provenance-contract.md` — Staleness SLA for cached articles
- Per-agent folders with `registry.yaml`, `skill-manifest.yaml`, `KILLSWITCH.md`, `safest-assessment.md`

### 4.6 Output Layer — Templates

| Template | Used By | Structure |
|----------|---------|-----------|
| `dfm-eval-report.md` | `/pl-dfm-review` | Part summary → Process match → DFM checks → Issues → Recommendations → Compliance flags |
| `qa-response.md` | `/pl-ask`, `/pl-strategy` | Direct answer → Supporting detail → Source citations → Related articles |
| `compliance-assessment.md` | `/pl-governance`, `/pl-assess` | Scope → Regulatory mapping → Gap analysis → Remediation → Risk rating |

All templates support `{{#regulated}}` conditionals for compliance-aware output.

---

## 5. Data Flow — Request Lifecycle

```
User Input
    │
    ▼
┌─────────────────┐
│ Command Parser  │ ──► Identifies command (/pl-dfm-review, /pl-ask, etc.)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Keyword Parser  │ ──► Extracts process, mode, vertical, compliance keywords
└────────┬────────┘
         │
         ▼
┌─────────────────┐     ┌─────────────────────────────┐
│ Intent Classifier│────►│ Change Management Keywords? │──Yes──► Load Change-Mgmt Orchestrator
└────────┬────────┘     └─────────────────────────────┘          └─────────────────────────────┘
         │                                    No
         ▼
┌─────────────────┐
│ Agent Resolver  │ ──► Maps to specialist agent (cnc-machining, injection-molding, etc.)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ KB Slice Loader │ ──► Loads only required KB files per agent's `loads:` frontmatter
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Agent Execution │ ──► Runs design eval or Q&A procedure against loaded KB
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Compliance Check│ ──► If regulated keywords detected, inject compliance warnings
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Template Render │ ──► Formats output using dfm-eval-report.md, qa-response.md, or compliance-assessment.md
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Source Citation │ ──► Appends [knowledge/<file>.md → <source_url>] for every claim
└────────┬────────┘
         │
         ▼
    Output to User
```

---

## 6. Cross-Cutting Concerns

### 6.1 Compliance Routing

When regulated keywords are detected (ITAR, EAR, FDA, EU AI Act, etc.), the system:
1. Sets `regulated=true` in the request context
2. Loads compliance KB files in addition to process KB files
3. Renders `{{#regulated}}` blocks in output templates
4. Appends compliance warnings and regulatory disclaimers

### 6.2 Source Grounding

Every claim in agent output must cite:
- The cached KB file path: `knowledge/<folder>/<article>.md`
- The original ProtoLabs URL from the file's `source_url` frontmatter

Example: *"Minimum hole diameter for CNC drilling is 0.5mm [knowledge/cnc-machining/mastering-complex-features.md → https://www.protolabs.com/resources/design-tips/mastering-complex-features-on-machined-parts/]"*

### 6.3 KB Freshness

- Articles are cached locally with `fetched_at` timestamps
- `/pl-refresh-kb [folder]` re-scrapes articles from ProtoLabs website
- `kb-freshness-provenance-contract.md` defines staleness SLAs

### 6.4 Agent Risk Management

Each agent has:
- **Risk registry entry** in `agent-risk-registry.yaml` with ARI score
- **SAFEST assessment** covering 112 control points
- **KILLSWITCH file** for immediate deactivation if needed
- **Skill manifest** documenting capabilities and limitations

---

## 7. Implementation Workstreams

The `ai-implementation-workstreams/` folder captures parallel engineering tracks:

| Track | Status | Description |
|-------|--------|-------------|
| **WP-CAD** | 🟡 Planning | CAD AI Evaluation — $600K strategic initiative for automated DFM analysis |
| **WP01 — Input Sanitization** | 🔴 Blocked | Unprotected AI inputs (prompt injection) |
| **WP02 — Adversarial Defense** | 🔴 Blocked | No multi-layer defense against attacks |
| **WP03 — Runtime Monitoring** | 🔴 Blocked | Blind spot in AI system behavior |
| **WP04 — Audit & Compliance** | 🔴 Blocked | Missing tamper-evident audit trails |
| **P1 — Zero-Trust Architecture** | 👥 Discussion | Network segmentation for AI services |
| **P1 — Insider Threat Program** | 👥 Discussion | Behavioral analytics for manufacturing data |
| **P1 — Nation-State Countermeasures** | 👥 Discussion | APT protection for manufacturing IP |

---

## 8. File Organization

```
ProtoLab/
├── CLAUDE.md                          # Root entry point: agent registry + routing rules
├── PLAN.md                            # Full implementation architecture
├── README.md                          # Repo overview + quick start
├── TODO.md                            # Delivery checklist
│
├── agents/                            # 11 specialist agent definitions
│   ├── dfm-router.agent.md
│   ├── cnc-machining.agent.md
│   ├── injection-molding.agent.md
│   ├── sheet-metal.agent.md
│   ├── 3d-printing.agent.md
│   ├── materials-selection.agent.md
│   ├── vertical-aerospace.agent.md
│   ├── vertical-medical.agent.md
│   ├── vertical-automotive-ev.agent.md
│   ├── trends-strategy.agent.md
│   └── change-management-orchestrator.agent.md
│
├── knowledge/                         # 68+ cached KB articles
│   ├── cnc-machining/
│   ├── injection-molding/
│   ├── sheet-metal/
│   ├── 3d-printing/
│   ├── materials/
│   ├── verticals/
│   ├── trends/
│   ├── compliance/
│   ├── cad/
│   └── ai/
│
├── templates/                         # Output templates
│   ├── dfm-eval-report.md
│   ├── qa-response.md
│   └── compliance-assessment.md
│
├── governance/                        # 7-stage AI governance framework
│   ├── 00-getting-started/
│   ├── 01-discovery-governance/
│   ├── 02-development-governance/
│   ├── 03-runtime-governance/
│   ├── 04-operational-governance/
│   ├── 05-cross-cutting/
│   ├── 06-executive/
│   ├── 07-enterprise-implementation/
│   ├── protolabs/                     # Protolabs-specific artifacts
│   └── dashboards/                    # HTML executive dashboards
│
├── ai-implementation-workstreams/     # JTBD framework + work packages
│   ├── 00-JTBD-and-problem-statements/
│   ├── 01-agentic-ready-implementations/
│   ├── 02-human-discussion-required/
│   └── 03-decision-frameworks/
│
├── docs/                              # Strategic documentation
│   ├── executive-presentation-c-board.md
│   ├── governance-framework-architecture.md
│   ├── iso-42001-gap-analysis.md
│   ├── TPM-Strategy-Agent-Guide.md
│   ├── plans/
│   └── vision/
│
├── .claude/                           # VS Code Copilot commands + skills
│   ├── commands/                      # 11 slash commands
│   └── skills/                        # Router + funnel intake skills
│
├── tools/                             # Engineering tools
│   └── cad-parser/
│
├── web/                               # Web interface (future)
│   └── src/
│
├── reference/                         # Evaluation frameworks, worked examples
│   ├── agent-evaluation-framework.md
│   ├── agent-skills-gap-analysis.md
│   └── verification-runs/
│
└── solutions-discovery/               # Solution architecture documents
    └── cad-design-to-order-aws-appstream.md
```

---

## 9. Presentation Options

This system design can be presented in multiple formats depending on audience:

### 9.1 Executive Summary (C-Board)
- **Focus**: Business value, risk posture, investment priorities
- **Key slides**: Agent inventory, compliance coverage, WP-CAD strategic initiative, governance maturity
- **Artifact**: `docs/executive-presentation-c-board.md`

### 9.2 Engineering Deep-Dive
- **Focus**: Architecture, data flow, agent wiring, KB loading
- **Key diagrams**: C4 container diagram, request lifecycle, agent-KB mapping
- **Artifact**: This document (`docs/system-design.md`)

### 9.3 Compliance Audit
- **Focus**: Governance coverage, regulatory mapping, gap analysis
- **Key artifacts**: `governance/protolabs/safest-coverage-matrix.md`, per-agent KILLSWITCH files
- **Artifact**: `governance/README.md`

### 9.4 Workshop Facilitation
- **Focus**: Use-case discovery, feasibility assessment, skeptical engineer rehearsal
- **Key commands**: `/pl-funnel-intake`, `/pl-feasibility-probe`, `/pl-rehearse`
- **Artifact**: `docs/TPM-Strategy-Agent-Guide.md`

### 9.5 Interactive Dashboard
- **Focus**: Live system status, KB freshness, agent health
- **Key artifacts**: `governance/dashboards/board.html` (T1–T4 views)

---

## 10. Key Metrics

| Metric | Current | Target |
|--------|---------|--------|
| KB Articles Cached | 68+ | 100+ |
| Specialist Agents | 11 | 15+ |
| Compliance Frameworks Mapped | 12 | 15+ |
| Governance Stages | 7 | 7 (complete) |
| P0 Work Packages | 4 | 0 (all resolved) |
| Source Citation Coverage | 100% | 100% |
| KB Freshness SLA | Manual refresh | Automated weekly |

---

## 11. ADR-001: Modular Monolith over Microservices

**Status**: Accepted

**Context**: The ProtoLab system is maintained by a small team. Independent scaling of agents is not required. The primary concern is maintainability and ease of adding new agents/KB articles.

**Decision**: Use a modular monolith architecture where agents are self-contained files that share a common routing and KB loading infrastructure. No independent deployable services.

**Consequences**:
- ✅ Easier to add new agents (copy file, register in CLAUDE.md)
- ✅ Single codebase, single review process
- ✅ No distributed system complexity
- ❌ Cannot scale individual agents independently
- ❌ All agents share the same release cycle

---

*Document version: 1.0 | Last updated: 2026-05-03*
