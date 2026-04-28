# AIMS Signing Authority Matrix

> **Document Type:** Cross-Cutting — Authority and Accountability
> **Version:** 1.0
> **Effective Date:** 2026-04-28
> **Owner:** Chief AI Officer (CAIO)
> **Approved By:** Board of Directors
> **Review Cycle:** Annual

---

## Purpose

This matrix defines who has authority to sign off on AIMS decisions. ISO 42001 Clause 5.3 requires defined authorities, and the ISO 42001 gap analysis identified the absence of an explicit signing authority matrix as a gap.

## Regulatory Basis

- **ISO/IEC 42001 Clause 5.3** — Organizational roles, responsibilities, and authorities
- **EU AI Act Article 26(2)** — Human oversight by persons with appropriate competence

---

## Signing Authority Matrix

| Decision | Primary Authority | Secondary Authority | Escalation |
|----------|------------------|-------------------|------------|
| **Tier 1 deployment approval** | Technical Owner | Security Lead | Governance Council |
| **Tier 2 deployment approval** | Governance Council (majority vote) | N/A | Board |
| **Tier 3 deployment approval** | Board of Directors | N/A | N/A |
| **Risk tier classification** | Technical Owner + Safety Officer | Governance Council (if disputed) | Board |
| **Model card approval** | Technical Owner | Policy Owner | Governance Council |
| **Vendor AI integration (non-customer)** | Security Lead | CAIO | Governance Council |
| **Vendor AI integration (customer data)** | Governance Council | N/A | Board |
| **Incident severity classification** | First Responder (initial) | CAIO (reclassification) | Board |
| **Agent retirement** | Technical Owner (Tier 1) | Governance Council (Tier 2+) | Board (Tier 3) |
| **Policy amendment (minor)** | CAIO | N/A | Governance Council |
| **Policy amendment (major)** | Governance Council | N/A | Board |
| **Risk appetite change** | Board of Directors | N/A | N/A |
| **Budget approval (AIMS operations)** | CAIO (within authority) | Board (exceeds authority) | N/A |
| **Regulatory response** | CAIO + Legal Counsel | Board (if enforcement action) | N/A |
| **Corrective action closure** | Head of Internal Audit | CAIO | Governance Council |

---

## Delegation Rules

1. Each authority holder must designate a **named delegate** in writing to the CAIO.
2. Delegates have the same signing authority when acting in the primary's absence.
3. Delegation does not transfer accountability — the primary authority holder remains accountable.
4. Delegation must be documented in the Council meeting minutes.

---

## Cross-References

| Document | Relationship |
|----------|-------------|
| [AI Governance Policy](ai-governance-policy.md) | Parent policy |
| [AI Governance Council Charter](ai-governance-council-charter.md) | Council authority defined here |
| [Approval Thresholds by Tier](approval-thresholds-by-tier.md) | Per-tier approval rules |
| [Governance Roles & RACI](governance-roles-raci.md) | Detailed role definitions |

---

*This document is version-controlled and auditable.*
