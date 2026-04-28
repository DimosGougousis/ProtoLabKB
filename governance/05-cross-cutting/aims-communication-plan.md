# AIMS Communication Plan

> **Document Type:** Cross-Cutting — Communication
> **Version:** 1.0
> **Effective Date:** 2026-04-28
> **Owner:** Chief AI Officer (CAIO)
> **Approved By:** AI Governance Council
> **Review Cycle:** Annual

---

## Purpose

This plan defines what AI governance information is communicated, to whom, when, and through which channels. ISO 42001 Clause 7.4 requires the organization to determine the internal and external communications relevant to the AIMS.

## Regulatory Basis

- **ISO/IEC 42001 Clause 7.4** — Communication
- **EU AI Act Article 13** — Transparency obligations
- **NIST AI RMF GV-1.1** — Policies communicated

---

## Internal Communication

| Communication | Audience | Frequency | Channel | Owner |
|--------------|----------|-----------|---------|-------|
| AI Governance Policy updates | All staff | As needed | Email + intranet | CAIO |
| Quarterly governance report | Board, Council, senior leadership | Quarterly | Board meeting + written report | CAIO |
| Council meeting minutes | Council members + delegates | Monthly | Secure document repository | CAIO |
| Incident notifications (Sev1) | CAIO, Board, affected teams | As needed | PagerDuty + email | Safety Officer |
| Incident notifications (Sev2) | Council, affected teams | As needed | Slack + email | Technical Owner |
| AI literacy training | All relevant staff | Annual | LMS | CAIO |
| Governance onboarding | New governance role holders | Onboarding | Live session + documentation | CAIO |
| Eval results summary | Engineering teams | Per deployment | CI/CD dashboard | Technical Owner |
| Regulatory change alerts | Council, Legal, Compliance | As needed | Email | Legal Counsel |

---

## External Communication

| Communication | Audience | Frequency | Channel | Owner |
|--------------|----------|-----------|---------|-------|
| Client-facing AI policy summary | Clients, prospects | On request + during procurement | Document (PDF) | VP Product |
| Procurement questionnaire responses | Client procurement teams | As needed | RFP response | VP Product + Legal |
| Data breach notification | Affected clients, supervisory authority | As needed (within SLA) | Email + formal letter | DPO + Legal |
| AI incident notification (customer-facing) | Affected clients | As needed | Email + account manager | Policy Owner |
| ISO 42001 certification status | Clients, prospects, partners | Upon achievement + annual | Website + marketing | CAIO |
| Regulatory reporting | Supervisory authorities | As required | Formal submission | Legal Counsel |

---

## Communication SLAs

| Communication Type | SLA |
|-------------------|-----|
| Sev1 incident → Board notification | ≤2 hours |
| Sev1 incident → Client notification | ≤24 hours (if client affected) |
| Data breach → Supervisory authority | ≤72 hours (GDPR Art. 33) |
| Regulatory change → Council notification | ≤10 business days |
| Policy update → All staff | ≤5 business days |

---

## Cross-References

| Document | Relationship |
|----------|-------------|
| [AI Governance Policy](ai-governance-policy.md) | Parent policy |
| [Incident Severity Classification](../04-operational-governance/incident-severity-classification.md) | Incident communication SLAs |
| [Client-Facing AI Policy Summary](../ai-policy-client-summary.md) | External communication artifact |
| [Regulatory Change Monitor](../04-operational-governance/regulatory-change-monitor.md) | Regulatory change communication |

---

*This document is version-controlled and auditable.*
