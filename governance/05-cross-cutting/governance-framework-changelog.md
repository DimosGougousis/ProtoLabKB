# Governance Framework Changelog

> **Document Type:** Cross-Cutting — Version Control
> **Version:** 1.0
> **Effective Date:** 2026-04-28
> **Owner:** Chief AI Officer (CAIO)
> **Review Cycle:** Continuous (updated with every material change)

---

## Purpose

This changelog tracks every material change to the ProtoLabs AI governance framework. It answers: what changed, when, why, who approved it, and what triggered the change. Without this record, governance drift is invisible and audit trails are incomplete.

## Scope

This changelog covers changes to:
- AI Governance Policy and all documents it references
- Governance Council Charter and operating procedures
- Approval thresholds and decision rules
- Incident severity classification and response procedures
- Risk classification methodology
- Any governance artifact in `governance/` directory

---

## Changelog

### 2026-04-28 — Framework v1.0 (Initial Release)

**Trigger:** Initial governance framework creation based on industry best-practice evaluation.

| Change ID | Document | Change Type | Description | Approved By |
|-----------|----------|-------------|-------------|-------------|
| CHG-001 | `ai-governance-policy.md` | Created | One-page AI governance policy (8 sections) | CAIO |
| CHG-002 | `05-cross-cutting/ai-governance-council-charter.md` | Created | Council composition, authority, meeting cadence, decision process | CAIO |
| CHG-003 | `05-cross-cutting/approval-thresholds-by-tier.md` | Created | Decision rules: who approves what by risk tier | CAIO |
| CHG-004 | `04-operational-governance/incident-severity-classification.md` | Created | Sev1-Sev4 definitions, response SLAs, escalation paths | CAIO |
| CHG-005 | `02-development-governance/checklists/model-card-completeness-checklist.yaml` | Created | 32-item checklist validating model card completeness | CAIO |
| CHG-006 | `02-development-governance/prompt-registry.md` | Created | Centralized prompt template registry with version tracking | CAIO |
| CHG-007 | `05-cross-cutting/third-party-ai-vendor-controls.md` | Created | Vendor assessment, DPA requirements, exit strategies | CAIO |
| CHG-008 | `04-operational-governance/aims-internal-audit-plan.md` | Created | ISO 42001 internal audit program and annual calendar | CAIO |
| CHG-009 | `03-runtime-governance/agentic-workflows/safety-agent-architecture.md` | Created | Safety Agent (Governor) architecture specification | CAIO |
| CHG-010 | `04-operational-governance/model-retirement-procedure.md` | Created | Agent/model retirement procedure with dependency assessment | CAIO |
| CHG-011 | `05-cross-cutting/governance-framework-changelog.md` | Created | This document | CAIO |
| CHG-012 | `04-operational-governance/regulatory-change-monitor.md` | Created | Regulatory change monitoring and update process | CAIO |
| CHG-013 | `05-cross-cutting/aims-document-retention-schedule.md` | Created | Retention periods for all AIMS document types | CAIO |
| CHG-014 | `06-executive/aims-objectives-and-kpis.md` | Created | AIMS SMART objectives and KPI targets | CAIO |
| CHG-015 | `04-operational-governance/aims-corrective-action-template.md` | Created | 8D-style corrective action template for nonconformities | CAIO |
| CHG-016 | `04-operational-governance/aims-management-review-agenda.md` | Created | ISO 42001 management review agenda template | CAIO |
| CHG-017 | `01-discovery-governance/ai-opportunity-register.md` | Created | AI opportunity register (ISO 42001 Cl. 6.1) | CAIO |
| CHG-018 | `05-cross-cutting/aims-signing-authority-matrix.md` | Created | Signing authority for AIMS decisions | CAIO |
| CHG-019 | `ai-policy-client-summary.md` | Created | Client-facing one-page AI policy summary | CAIO |
| CHG-020 | `05-cross-cutting/aims-competence-matrix.md` | Created | Role-to-competence mapping for AIMS | CAIO |
| CHG-021 | `05-cross-cutting/aims-communication-plan.md` | Created | Internal/external communication protocols | CAIO |
| CHG-022 | `04-operational-governance/aims-improvement-register.md` | Created | Continual improvement tracking | CAIO |
| CHG-023 | `04-operational-governance/aims-evaluation-repository-index.md` | Created | Centralized index of all eval results | CAIO |

---

## Change Categories

| Category | Description | Approval Required |
|----------|-------------|-------------------|
| **Created** | New governance artifact added to framework | CAIO |
| **Updated** | Existing artifact modified | Per change impact (minor: CAIO; major: Council) |
| **Deprecated** | Artifact marked for removal | Council |
| **Removed** | Artifact deleted from framework | Council + Board notification |
| **Reclassified** | Risk tier or control classification changed | Council |

---

## Change Impact Assessment

Every change must be assessed for impact:

| Impact Level | Definition | Approval | Communication |
|-------------|-----------|----------|---------------|
| **Minor** | Typo fix, formatting, clarifying language | CAIO | Changelog only |
| **Moderate** | New control, updated threshold, added requirement | CAIO | Changelog + Council notification |
| **Major** | New policy section, changed approval authority, new risk tier | Council | Changelog + Council approval + Board notification |
| **Critical** | Policy scope change, regulatory response, risk appetite change | Board | Changelog + Board approval |

---

## How to Use This Changelog

1. **Before making a change:** Check recent entries for related changes.
2. **When making a change:** Add an entry with change ID, document, type, description, and approver.
3. **When reviewing governance:** Use this changelog to understand what changed since last review.
4. **During audit:** This changelog demonstrates change management discipline.

---

*This document is version-controlled and auditable. Unauthorized modifications void governance compliance claims.*
