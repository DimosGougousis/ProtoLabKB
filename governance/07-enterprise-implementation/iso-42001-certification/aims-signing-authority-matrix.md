# AIMS Signing Authority Matrix — ISO/IEC 42001 Accountability

> **Purpose:** Defines explicit signing authority for all AIMS decisions, ensuring clear accountability per ISO/IEC 42001 Clause 5.2 (Leadership) and Clause 5.3 (Organizational Roles).

**Version:** 1.0  
**Last Updated:** 2026-04-24  
**Owner:** Chief AI Officer (AIMS Owner)  
**Review Cycle:** Quarterly  

---

## Authority Levels

| Level | Title | Authority Scope | Delegation Allowed? |
|-------|-------|-----------------|---------------------|
| **L1 — Board** | Board of Directors | AI policy adoption, AIMS scope changes, major budget approvals | No |
| **L2 — Executive** | CAIO, VPs | AIMS objectives, risk appetite, certification decisions | No |
| **L3 — Director** | Directors, Safety Officer | Agent tier classification, safety validation, audit findings | Limited (to L4 with written authorization) |
| **L4 — Manager** | Engineering Managers, Product Managers | Deployment approvals, eval results acceptance, routine changes | Yes (to senior individual contributors) |
| **L5 — Individual** | Senior Engineers, Leads | Code reviews, test approvals, documentation sign-off | No |

---

## Signing Authority by Decision Type

### Agent Lifecycle Decisions

| Decision | Description | Authority Level | Signatory | Evidence Required |
|----------|-------------|-----------------|-----------|-------------------|
| **New agent proposal** | Propose development of new AI agent | L4 | Product Manager | `responsible-product-brief.md` |
| **Agent tier classification** | Classify agent as Tier 1/2/3 | L3 | Safety Officer + Technical Owner | `agent-tier-classification.yaml` |
| **Discovery Gate approval** | Approve agent for development | L3 | Policy Owner | Gate checklist complete |
| **Development Gate approval** | Approve agent for deployment | L3 | Policy Owner | Eval results, model card |
| **Deployment Gate approval** | Approve agent for production | L3 | Policy Owner + Safety Officer (if Tier 2/3) | Safety validation, kill switch test |
| **Agent retirement** | Decommission agent | L3 | Technical Owner + Policy Owner | `model-retirement-procedure.md` |
| **Agent reclassification** | Change agent tier | L3 | Safety Officer | Risk re-assessment |

### Safety-Critical Decisions

| Decision | Description | Authority Level | Signatory | Evidence Required |
|----------|-------------|-----------------|-----------|-------------------|
| **Tier 3 agent deployment** | Deploy high-autonomy agent | L2 | CAIO + Safety Officer | Full safety validation, board notification |
| **Kill switch bypass** | Temporarily disable kill switch | L2 | CAIO + Safety Officer | Emergency only, 24-hour max, logged |
| **Safety PLC access** | Any access to safety PLC | L1 | Board resolution required | Never delegated |
| **Safety Agent configuration change** | Modify Safety Agent rules | L3 | Safety Officer | Change impact assessment |
| **Emergency stop protocol change** | Modify E-stop procedures | L2 | VP Manufacturing + Safety Officer | Risk assessment, operator training |
| **Hard guardrail relaxation** | Weaken any hard guardrail | L2 | CAIO + Safety Officer | Never allowed for safety-critical guardrails |

### Financial Decisions

| Decision | Description | Authority Level | Signatory | Evidence Required |
|----------|-------------|-----------------|-----------|-------------------|
| **AIMS budget approval** | Approve annual AIMS budget | L1 | Board | `board-resolution-aims.md` |
| **Certification body contract** | Engage TÜV SÜD / BSI | L2 | CAIO | Procurement process |
| **Consultant engagement** | Hire ISO 42001 consultant | L3 | CAIO | SOW, budget availability |
| **Tool/platform purchase** | Buy AIMS infrastructure | L4 | VP Engineering | Business case, security review |
| **Training budget** | Approve training spend | L4 | HR + CAIO | Training plan |

### Risk and Compliance Decisions

| Decision | Description | Authority Level | Signatory | Evidence Required |
|----------|-------------|-----------------|-----------|-------------------|
| **Risk acceptance** | Accept residual risk | L3 | Policy Owner | Risk register, mitigation evidence |
| **High-risk acceptance** | Accept risk with impact >$X | L2 | CAIO | Board notification |
| **Incident classification** | Classify AI incident severity | L3 | Safety Officer / Compliance Officer | Incident report |
| **Regulatory disclosure** | Notify regulator of incident | L2 | CAIO + General Counsel | Legal review |
| **Client notification** | Notify client of AI incident | L3 | Policy Owner + Compliance Officer | Impact assessment |
| **Audit finding closure** | Close internal audit finding | L3 | Process Owner + Internal Audit | Corrective action evidence |
| **Management review minutes** | Approve quarterly review | L2 | CAIO | `aims-management-review-minutes-template.md` |

### Technical Decisions

| Decision | Description | Authority Level | Signatory | Evidence Required |
|----------|-------------|-----------------|-----------|-------------------|
| **Model update deployment** | Deploy new model version | L4 | MLOps Lead | Eval results, rollback plan |
| **Architecture change** | Modify agent architecture | L4 | Technical Owner | Architecture review, impact assessment |
| **Tool addition** | Add new tool to agent registry | L4 | Technical Owner | `tool-use-risk-model.yaml` update |
| **API integration** | Integrate with new external API | L4 | Technical Owner + Security Engineer | Security review |
| **Data schema change** | Modify data handling | L4 | Technical Owner + DPO | DPIA review |
| **Eval suite change** | Modify evaluation criteria | L4 | ML Lead | Peer review |

---

## Emergency Authority

### Emergency Override Protocol

In emergency situations (safety incident, active breach, system failure), the following override authority applies:

| Emergency Type | Immediate Authority | Notification Required | Duration |
|----------------|---------------------|----------------------|----------|
| Safety emergency | Safety Officer (any action to protect life) | CAIO within 1 hour | Until safe state restored |
| Security breach | Security Engineer (isolate systems) | CAIO + Compliance within 1 hour | Until containment verified |
| System failure | On-call MLOps Engineer (rollback) | Technical Owner within 30 min | Until service restored |
| Kill switch activation | Any operator (immediate) | Safety Officer within 15 min | Until investigation complete |

**Post-Emergency:** All emergency actions must be documented in `ai-incident-report.md` and reviewed at next management review.

---

## Delegation Rules

### Permitted Delegations

| From | To | Scope | Conditions |
|------|-----|-------|------------|
| CAIO (L2) | VP Engineering (L3) | Technical decisions | Written authorization, 30-day limit |
| Safety Officer (L3) | Senior Safety Engineer (L4) | Routine safety checks | Training complete, quarterly review |
| Policy Owner (L3) | Product Manager (L4) | Gate checklist review | Training complete, monthly check-in |
| Technical Owner (L3) | Engineering Manager (L4) | Deployment approvals | Eval results pass, no safety impact |

### Prohibited Delegations

| Decision | Cannot Be Delegated To | Reason |
|----------|------------------------|--------|
| Tier 3 agent deployment | Below L2 | Safety-critical, board notification required |
| Kill switch bypass | Below L2 | Life safety impact |
| Safety PLC access | Anyone | Never allowed per `safety-plc-readonly-policy.yaml` |
| Hard guardrail relaxation | Below L2 | Could enable unsafe actions |
| AIMS budget approval | Below L1 | Board authority per resolution |
| Regulatory disclosure | Below L2 | Legal exposure |

---

## Signature Registry

### Current Authorized Signatories

| Name | Role | Authority Level | Signature Date | Valid Until |
|------|------|-----------------|----------------|-------------|
| [CAIO Name] | Chief AI Officer | L2 | 2026-04-24 | 2027-04-24 |
| [VP Product Name] | VP of Product | L3 (Policy) | 2026-04-24 | 2027-04-24 |
| [VP Engineering Name] | VP of Engineering | L3 (Technical) | 2026-04-24 | 2027-04-24 |
| [Safety Officer Name] | Director of Manufacturing Safety | L3 (Safety) | 2026-04-24 | 2027-04-24 |
| [Compliance Officer Name] | General Counsel / DPO | L3 (Compliance) | 2026-04-24 | 2027-04-24 |
| [ML Lead Name] | ML Engineering Lead | L4 | 2026-04-24 | 2027-04-24 |
| [MLOps Lead Name] | MLOps Lead | L4 | 2026-04-24 | 2027-04-24 |

### Signature Update Procedure

1. Role change triggers update requirement
2. New signatory completes competence verification (`aims-competence-matrix.md`)
3. AIMS Owner approves new signatory
4. Signature registry updated with date and validity period
5. Previous signatory access revoked within 24 hours

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-24 | ProtoLabs AI Governance Office | Initial signing authority matrix |

---

## See Also

- `governance/05-cross-cutting/governance-roles-raci.md` — RACI matrix
- `governance/07-enterprise-implementation/iso-42001-certification/aims-competence-matrix.md` — Competence requirements
- `governance/07-enterprise-implementation/iso-42001-certification/board-resolution-aims.md` — Board resolution
