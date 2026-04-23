# Cross-Cutting Concerns

## Purpose

Cross-cutting concerns are governance artifacts that span all four governance pillars (Discovery, Development, Runtime, Operational) and cannot be assigned to a single lifecycle phase. They provide the shared vocabulary, role definitions, regulatory mappings, and tooling context that every other governance document depends on. Without these foundations, pillar-specific governance artifacts lack consistency and traceability.

## When to Use

- During initial framework adoption to establish shared definitions and role clarity before pillar-specific work begins
- When onboarding new team members who need to understand governance terminology and responsibilities
- When preparing for regulatory inspections that require traceability from governance activities to specific regulatory requirements
- When resolving disputes about role boundaries, term definitions, or tool selection
- When auditors request a cross-pillar view of governance coverage

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **CAIO** | **Accountable** -- ensures cross-cutting artifacts are complete, consistent, and reviewed annually |
| **AI Governance Committee** | **Consulted** -- reviews and approves changes to roles, RACI, and regulatory mappings |
| **Governance Lead** | **Responsible** -- maintains glossary, regulatory index, and tool landscape |
| **All Model Owners** | **Informed** -- consume cross-cutting artifacts to ensure consistent governance execution |
| **Internal Audit** | **Consulted** -- validates that cross-cutting mappings support audit evidence collection |

## Regulatory Basis

- **EU AI Act Article 3** -- definitions of key terms used throughout the regulation
- **SAFEST item A-04** -- RACI matrix for AI lifecycle activities
- **ISO/IEC 42001 Section 3** -- terms and definitions for AI management systems
- **DNB Good Practice for AI** -- expectation of clear accountability structures and consistent terminology

---

## Contents

This section contains the following cross-cutting governance artifacts:

### Roles and Accountability

| File | Purpose |
|------|---------|
| [Governance Roles and RACI Matrix](governance-roles-raci.md) | Comprehensive RACI matrix for AI governance across the entire lifecycle, defining the CAIO role, federated governance model (~75% central / ~25% local), and tiered governance mapping (Tier 1 Strategic through Tier 4 Runtime) |

### Terminology

| File | Purpose |
|------|---------|
| [Unified Glossary](glossary.md) | Consistent definitions for governance, AI/ML, regulatory, and agentic workflow terminology used across all pillars |

### Regulatory Mapping

| File | Purpose |
|------|---------|
| [Regulatory Reference Index](regulatory-reference-index.md) | Master index mapping EU AI Act articles, DORA requirements, GDPR provisions, PSD2 obligations, and DNB guidelines to specific framework sections |
| [SAFEST to Four Pillars Mapping](safest-to-four-pillars-mapping.yaml) | Structured YAML mapping of every SAFEST checklist item (Soundness, Accountability, Fairness, Ethics, Skills, Transparency) to the governance pillar and artifact that addresses it |

### Tooling

| File | Purpose |
|------|---------|
| [AI Governance Tool Landscape](tool-landscape.md) | Governance-oriented evaluation of evaluation tools, monitoring platforms, guardrail frameworks, and GRC systems |

---

## How Cross-Cutting Artifacts Connect to the Four Pillars

```
+---------------------+     +---------------------+
| 01 Discovery        |     | 02 Development      |
| Governance          |     | Governance           |
|                     |     |                      |
| Uses: Glossary,     |     | Uses: RACI, Tool     |
| RACI, Regulatory    |     | Landscape, SAFEST    |
| Index               |     | Mapping              |
+---------------------+     +---------------------+
         |                            |
         +------- CROSS-CUTTING ------+
         |        05-cross-cutting    |
         |                            |
         |  - governance-roles-raci   |
         |  - glossary                |
         |  - regulatory-ref-index    |
         |  - safest-mapping          |
         |  - tool-landscape          |
         |                            |
         +------- CROSS-CUTTING ------+
         |                            |
+---------------------+     +---------------------+
| 03 Runtime          |     | 04 Operational       |
| Governance          |     | Governance           |
|                     |     |                      |
| Uses: RACI, Tool    |     | Uses: Regulatory     |
| Landscape, SAFEST   |     | Index, RACI, SAFEST  |
| Mapping             |     | Mapping              |
+---------------------+     +---------------------+
```

Every pillar-specific artifact cross-references at least one cross-cutting document. When writing new governance artifacts, always:

1. **Check the glossary** -- use terms as defined, or propose additions for new terms.
2. **Cite the regulatory basis** -- use the regulatory reference index to find the correct article or item number.
3. **Assign RACI roles** -- use role abbreviations from the governance roles document.
4. **Reference SAFEST items** -- use the SAFEST mapping to confirm which checklist items your artifact addresses.

---

## Relationship to Enterprise Implementation

Cross-cutting concerns inform but are distinct from the enterprise implementation artifacts in `07-enterprise-implementation/`. The distinction:

| Concern | Cross-Cutting (05) | Enterprise Implementation (07) |
|---------|--------------------|---------------------------------|
| **Roles** | Defines what each role does | Defines how to staff and organize those roles (CoE, 3LoD, Committee) |
| **Regulatory** | Maps regulations to framework sections | Defines how to operationalize regulatory compliance (reporting calendars, GRC integration) |
| **Tooling** | Evaluates tool capabilities | Defines how to integrate tools into workflows (Jira workflows, CI/CD gates) |
| **SAFEST** | Maps items to pillars | Defines how to evidence items at each governance maturity level |

---

## Maintenance Schedule

| Artifact | Review Frequency | Trigger for Unscheduled Review |
|----------|-----------------|-------------------------------|
| Governance Roles and RACI | Annually + at org restructure | Role change, new AI system category |
| Glossary | Quarterly | New regulation or technology adoption |
| Regulatory Reference Index | Quarterly + at regulatory change | New regulation published, regulatory guidance updated |
| SAFEST Mapping | Annually | DNB updates Good Practice guidance |
| Tool Landscape | Semi-annually | Major tool release, vendor acquisition, new governance requirement |

---

## Cross-References

- **Getting Started:** [Framework Navigation Guide](../00-getting-started/framework-navigation-guide.md) -- where to start based on your role
- **Discovery Governance:** [README](../01-discovery-governance/README.md) -- risk assessment and ethical review
- **Development Governance:** [README](../02-development-governance/README.md) -- eval-driven development and quality gates
- **Runtime Governance:** [README](../03-runtime-governance/README.md) -- guardrails, monitoring, and escalation
- **Operational Governance:** [README](../04-operational-governance/README.md) -- incident response, audit, and decommissioning
- **Enterprise Implementation:** [README](../07-enterprise-implementation/README.md) -- organizational adoption and rollout

---

*Last updated: 2026-03-01*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
