# Model Retirement Procedure

> **Document Type:** Operational Governance — Lifecycle Management
> **Version:** 1.0
> **Effective Date:** 2026-04-28
> **Owner:** Technical Owner (per agent)
> **Approved By:** AI Governance Council
> **Review Cycle:** Annual
> **Next Review:** 2027-04-28

---

## Purpose

This document defines the procedure for safely decommissioning AI agents and models at ProtoLabs. Retirement is not simply "turning off" — it requires data archival, knowledge transfer, dependency assessment, customer notification, and evidence preservation. Without a formal retirement procedure, retired agents leave orphaned data, broken delegation chains, and audit gaps.

## When to Use

- When an agent is being replaced by a newer version
- When a vendor discontinues a model that ProtoLabs depends on
- When a business function is discontinued
- When an agent is reclassified to a higher risk tier and the current implementation is inadequate
- When a Sev1 incident reveals fundamental flaws requiring agent replacement

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **Technical Owner** | **Accountable** — executes retirement procedure |
| **Policy Owner** | **Responsible** — approves retirement decision; manages customer communication |
| **Safety Officer** | **Reviewer** — validates safety implications of retirement |
| **Governance Council** | **Approver** — approves retirement for Tier 2+ agents |
| **Head of Internal Audit** | **Reviewer** — validates evidence preservation |

## Regulatory Basis

- **ISO/IEC 42001 Clause 8.4** — AI system lifecycle processes (including end-of-life)
- **EU AI Act Article 72(2)** — Post-market monitoring obligations continue after decommissioning
- **GDPR Article 17** — Right to erasure (data deletion after retirement)
- **NIST AI RMF MG-3.1** — Regular review and update (including retirement decisions)

---

## 1. Retirement Triggers

| Trigger | Description | Approval Required |
|---------|-------------|-------------------|
| **Planned replacement** | New version ready; old version retired per schedule | Technical Owner (Tier 1) / Council (Tier 2+) |
| **Vendor sunset** | Third-party model discontinued or API deprecated | Council |
| **Business discontinuation** | Business function no longer needed | Policy Owner + Council |
| **Accuracy degradation** | Agent accuracy below threshold with no viable fix | Council |
| **Sev1 incident** | Fundamental flaw requires replacement | Council + Board (Tier 3) |
| **Risk reclassification** | Agent reclassified to higher tier; current implementation inadequate | Council |
| **Regulatory requirement** | Regulation requires decommissioning | CAIO + Legal Counsel |

---

## 2. Retirement Procedure

### 2.1 Pre-Retirement Phase (Weeks 1-2)

| Step | Activity | Owner | Output |
|------|----------|-------|--------|
| 1 | Confirm retirement trigger and rationale | Policy Owner | Retirement justification document |
| 2 | Identify replacement agent (if applicable) | Technical Owner | Replacement agent ID |
| 3 | Validate replacement agent readiness | Technical Owner | Replacement passes full eval suite |
| 4 | Identify all dependencies (which agents delegate to this agent?) | Technical Owner | Dependency map |
| 5 | Identify all integrations (which systems call this agent?) | Technical Owner | Integration map |
| 6 | Assess customer impact | Policy Owner | Customer impact assessment |
| 7 | Submit retirement request to Governance Council (Tier 2+) | Policy Owner | Retirement request |

### 2.2 Transition Phase (Weeks 3-6)

| Step | Activity | Owner | Output |
|------|----------|-------|--------|
| 8 | Redirect delegation chains to replacement agent | Technical Owner | Updated delegation configuration |
| 9 | Redirect integrations to replacement agent | Technical Owner | Updated integration configuration |
| 10 | Shadow deployment: replacement handles production traffic while retired agent runs in parallel | Technical Owner | Shadow deployment log (minimum 14 days) |
| 11 | Validate replacement agent performance in production | Technical Owner | Performance comparison report |
| 12 | Notify affected customers (if customer-facing) | Policy Owner | Customer notification sent |
| 13 | Update prompt registry (deprecate retired agent prompts) | Technical Owner | Updated `prompt-registry.md` |
| 14 | Update model provenance registry | Technical Owner | Updated `vendor-registry.yaml` |

### 2.3 Decommissioning Phase (Week 7)

| Step | Activity | Owner | Output |
|------|----------|-------|--------|
| 15 | Disable retired agent (soft kill — no new requests) | Technical Owner | Agent disabled |
| 16 | Wait period: 7 days with monitoring (verify no unexpected traffic) | Technical Owner | Monitoring log |
| 17 | Hard kill: terminate agent process and infrastructure | Technical Owner | Infrastructure decommissioned |
| 18 | Revoke API keys and access credentials | Security Lead | Credentials revoked |
| 19 | Archive agent artifacts (model card, eval results, config, logs) | Technical Owner | Archived to cold storage |
| 20 | Update agent registry (status: retired) | Technical Owner | Updated agent registry |

### 2.4 Post-Retirement Phase (Week 8+)

| Step | Activity | Owner | Output |
|------|----------|-------|--------|
| 21 | Data retention: apply retention policy to agent data | DPO | Retention policy applied |
| 22 | Data deletion: delete data per GDPR Art. 17 (if requested) | DPO | Deletion certificate |
| 23 | Audit evidence preservation: ensure audit trail is preserved for 7 years | Head of Internal Audit | Evidence preserved |
| 24 | Post-retirement review: verify no broken dependencies or orphaned data | Technical Owner | Retirement closure report |
| 25 | Update governance framework changelog | CAIO | Changelog entry |

---

## 3. Dependency Impact Assessment

Before retiring an agent, the Technical Owner must assess:

| Dependency Type | Assessment Question | Action if Affected |
|----------------|---------------------|-------------------|
| **Delegation chains** | Do other agents delegate to this agent? | Update delegating agents to use replacement |
| **API integrations** | Do external systems call this agent? | Update integrations before decommissioning |
| **Knowledge base** | Does this agent have unique KB dependencies? | Ensure replacement has same or better KB access |
| **Eval suites** | Do eval suites reference this agent? | Update eval suites |
| **Monitoring dashboards** | Does this agent appear on monitoring dashboards? | Update dashboards |
| **Governance artifacts** | Do governance documents reference this agent? | Update references |

---

## 4. Customer Notification

If the retired agent is customer-facing:

| Notification Timing | Content | Channel |
|--------------------|---------|---------|
| **30 days before** | Announcement of replacement; what changes customers should expect | Email + in-app notification |
| **7 days before** | Reminder; any action required from customers | Email |
| **Day of retirement** | Confirmation; how to access support if issues arise | In-app notification |
| **7 days after** | Follow-up; satisfaction check | Email |

---

## 5. Data Retention and Deletion

| Data Type | Retention Period | Deletion Method |
|-----------|-----------------|-----------------|
| Agent configuration and model card | 7 years (audit requirement) | Archive to cold storage |
| Eval results and test evidence | 7 years | Archive to cold storage |
| Audit logs | 7 years | Archive to cold storage |
| Customer data processed by agent | Per DPA / GDPR | Secure deletion with certificate |
| Prompt templates | 7 years | Archive to cold storage |
| Training data (if any) | Per data governance plan | Secure deletion or archive |

---

## 6. Retirement Checklist

Use the existing checklist: [Model Retirement Checklist](checklists/model-retirement-checklist.yaml)

Additional ProtoLabs-specific items:

| ID | Item | Priority | Status |
|----|------|----------|--------|
| RET-PL-001 | Delegation chains redirected to replacement | Critical | |
| RET-PL-002 | Customer notification sent (if customer-facing) | Critical | |
| RET-PL-003 | Prompt registry updated (retired prompts deprecated) | High | |
| RET-PL-004 | Vendor registry updated (if third-party model) | High | |
| RET-PL-005 | Governance framework changelog updated | Medium | |
| RET-PL-006 | Retirement closure report completed | High | |

---

## Cross-References

| Document | Relationship |
|----------|-------------|
| [AI Governance Policy](../ai-governance-policy.md) | Parent policy; retirement is part of lifecycle |
| [Model Retirement Checklist](checklists/model-retirement-checklist.yaml) | Detailed checklist for retirement execution |
| [Approval Thresholds by Tier](../../05-cross-cutting/approval-thresholds-by-tier.md) | Retirement approval per tier |
| [Prompt Registry](../../02-development-governance/prompt-registry.md) | Prompt deprecation on retirement |
| [Third-Party Vendor Controls](../../05-cross-cutting/third-party-ai-vendor-controls.md) | Vendor model retirement considerations |
| [ISO 42001 Gap Analysis](../../../docs/iso-42001-gap-analysis.md) | Gap flagged this as missing |

---

*This document is version-controlled and auditable. Unauthorized modifications void governance compliance claims.*
