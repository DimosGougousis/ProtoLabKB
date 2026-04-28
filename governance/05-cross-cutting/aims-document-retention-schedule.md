# AIMS Document Retention Schedule

> **Document Type:** Cross-Cutting — Document Control
> **Version:** 1.0
> **Effective Date:** 2026-04-28
> **Owner:** Head of Internal Audit
> **Approved By:** AI Governance Council
> **Review Cycle:** Annual
> **Next Review:** 2027-04-28

---

## Purpose

This schedule defines how long each type of AIMS document and record must be retained, where it is stored, and how it is disposed of. ISO 42001 Clause 7.5 requires documented information to be controlled, and retention periods must be explicit.

## Regulatory Basis

- **ISO/IEC 42001 Clause 7.5** — Documented information (control, storage, retention)
- **EU AI Act Article 18** — Record-keeping obligations for high-risk AI
- **GDPR Article 5(1)(e)** — Storage limitation principle
- **ITAR §122.5** — Technical data retention (5 years minimum)

---

## Retention Schedule

| Document Type | Retention Period | Storage Location | Disposal Method |
|--------------|-----------------|-----------------|-----------------|
| **AI Governance Policy** | Permanent (superseded versions: 7 years) | Version control (Git) | Archive superseded versions |
| **Council Charter** | Permanent (superseded versions: 7 years) | Version control (Git) | Archive superseded versions |
| **Council Meeting Minutes** | 7 years | `governance/05-cross-cutting/council-minutes/` | Secure deletion |
| **Council Decision Log** | 7 years | `governance/05-cross-cutting/council-decision-log.yaml` | Secure deletion |
| **Model Cards** | Life of model + 7 years | Agent registry | Archive to cold storage |
| **Eval Results** | Life of model + 7 years | Eval repository | Archive to cold storage |
| **Prompt Templates** | Life of agent + 7 years | `agents/` directory | Archive to cold storage |
| **Incident Records** | 7 years | `governance/04-operational-governance/incident-records/` | Secure deletion |
| **Approval Records** | 7 years | `governance/05-cross-cutting/approval-records/` | Secure deletion |
| **Audit Reports** | 7 years | Internal audit repository | Archive to cold storage |
| **Risk Assessments** | Life of system + 7 years | `governance/01-discovery-governance/` | Archive to cold storage |
| **Vendor Assessments** | Life of contract + 7 years | `governance/05-cross-cutting/` | Secure deletion |
| **DPAs** | Life of contract + 7 years | Legal repository | Secure deletion |
| **Training Records** | Duration of employment + 3 years | HR/LMS | Secure deletion |
| **Customer Data** (processed by agents) | Per DPA / GDPR | Per agent data store | Secure deletion with certificate |
| **Audit Logs** | 7 years | Logging infrastructure | Automated purge |
| **Kill Switch Test Logs** | 7 years | Safety agent logs | Archive to cold storage |
| **Regulatory Change Log** | 7 years | `governance/04-operational-governance/` | Archive to cold storage |

---

## Storage Requirements

| Requirement | Implementation |
|-------------|---------------|
| **Integrity** | Version control (Git) for documents; checksums for archived records |
| **Availability** | Active documents accessible to authorized roles; archived records retrievable within 5 business days |
| **Confidentiality** | Access control per role-based permissions; encrypted at rest |
| **Auditability** | All access logged; retention status trackable |

---

## Cross-References

| Document | Relationship |
|----------|-------------|
| [AI Governance Policy](ai-governance-policy.md) | Parent policy |
| [ISO 42001 Gap Analysis](../../docs/iso-42001-gap-analysis.md) | Gap flagged this as missing |
| [Third-Party Vendor Controls](third-party-ai-vendor-controls.md) | Vendor DPA retention requirements |

---

*This document is version-controlled and auditable.*
