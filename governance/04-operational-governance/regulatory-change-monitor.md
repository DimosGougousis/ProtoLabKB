# Regulatory Change Monitor

> **Document Type:** Operational Governance — Regulatory Compliance
> **Version:** 1.0
> **Effective Date:** 2026-04-28
> **Owner:** Legal Counsel
> **Approved By:** AI Governance Council
> **Review Cycle:** Quarterly
> **Next Review:** 2026-07-28

---

## Purpose

This document defines who monitors regulatory changes affecting ProtoLabs' AI governance framework, how changes are assessed, and how the framework is updated. Regulations evolve — the EU AI Act implementing measures, NIST AI RMF updates, ISO 42001 amendments, and sector-specific requirements (ITAR, EAR, FDA, AS9100D) all change over time. Without a systematic monitoring process, ProtoLabs risks compliance drift.

## Regulatory Basis

- **ISO/IEC 42001 Clause 4.1** — Understanding external issues (including regulatory)
- **ISO/IEC 42001 Clause 6.1** — Actions to address risks and opportunities
- **NIST AI RMF GV-1.1** — Legal and regulatory requirements identified and documented
- **EU AI Act Article 72** — Post-market monitoring obligations

---

## 1. Regulatory Sources Monitored

| Source | Monitored By | Frequency | Method |
|--------|-------------|-----------|--------|
| **EU AI Act** (Official Journal, implementing acts) | Legal Counsel | Weekly | EUR-Lex alerts, AI Act newsletter |
| **NIST AI RMF** (updates, companion documents) | CAIO | Monthly | NIST website, AI RMF community |
| **ISO/IEC 42001** (amendments, guidance) | Head of Internal Audit | Quarterly | ISO website, certification body updates |
| **GDPR** (EDPB guidelines, national DPA guidance) | DPO | Monthly | EDPB website, IAPP alerts |
| **ITAR/EAR** (DDTC, BIS updates) | Security Lead | Monthly | Federal Register, DDTC/BIS websites |
| **FDA 21 CFR 820** (medical device AI guidance) | Legal Counsel | Monthly | FDA website, industry associations |
| **AS9100D / IATF 16949** (aerospace/automotive) | Legal Counsel | Quarterly | Industry association updates |
| **Singapore MGF** (updates) | CAIO | Quarterly | IMDA website |
| **US state AI laws** (Colorado, others) | Legal Counsel | Monthly | State legislature tracking services |

---

## 2. Change Assessment Process

```
Regulatory change detected
        |
        v
  +---------------------------+
  | STEP 1: LOG               |
  |                           |
  | Record: source, date,     |
  | summary, URL              |
  +---------------------------+
        |
        v
  +---------------------------+
  | STEP 2: IMPACT ASSESS     |
  |                           |
  | Does this affect:         |
  | - AI Governance Policy?   |
  | - Risk classification?    |
  | - Control requirements?   |
  | - Documentation?          |
  | - Reporting obligations?  |
  +---------------------------+
        |
        v
  +---------------------------+
  | STEP 3: CLASSIFY IMPACT   |
  |                           |
  | Minor: No framework change|
  | Moderate: Targeted update |
  | Major: Policy revision    |
  | Critical: Board escalation|
  +---------------------------+
        |
        v
  +---------------------------+
  | STEP 4: PLAN RESPONSE     |
  |                           |
  | Assign owner, set         |
  | deadline, identify        |
  | affected artifacts        |
  +---------------------------+
        |
        v
  +---------------------------+
  | STEP 5: IMPLEMENT         |
  |                           |
  | Update framework,         |
  | communicate changes,      |
  | log in changelog          |
  +---------------------------+
```

---

## 3. Response SLAs

| Impact Level | Assessment SLA | Implementation SLA | Approval |
|-------------|---------------|-------------------|----------|
| **Minor** | 15 business days | 30 business days | CAIO |
| **Moderate** | 10 business days | 20 business days | CAIO + Council notification |
| **Major** | 5 business days | 15 business days | Council |
| **Critical** | 48 hours | 10 business days | Board |

---

## 4. Regulatory Change Log

| ID | Date | Source | Summary | Impact | Owner | Status |
|----|------|--------|---------|--------|-------|--------|
| REG-001 | 2026-04-28 | EU AI Act | Framework created with current EU AI Act requirements as baseline | Baseline | CAIO | Closed |

---

## Cross-References

| Document | Relationship |
|----------|-------------|
| [AI Governance Policy](../ai-governance-policy.md) | Policy review triggered by regulatory changes |
| [Governance Framework Changelog](../05-cross-cutting/governance-framework-changelog.md) | Regulatory changes logged here |
| [Regulatory Reference Index](../05-cross-cutting/regulatory-reference-index.md) | Master index of all regulations |
| [ISO 42001 Gap Analysis](../../docs/iso-42001-gap-analysis.md) | Gap analysis updated when regulations change |

---

*This document is version-controlled and auditable.*
