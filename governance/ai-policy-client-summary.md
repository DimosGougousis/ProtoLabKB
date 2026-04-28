# ProtoLabs AI Governance — Client Summary

> **Document Type:** Client-Facing AI Policy Summary
> **Version:** 1.0
> **Last Updated:** 2026-04-28
> **Classification:** External — For Client Distribution

---

## Our Commitment to Responsible AI

ProtoLabs uses AI systems to accelerate manufacturing intelligence — from design-for-manufacturing analysis to material selection and process optimization. We are committed to deploying AI that is accurate, transparent, safe, and compliant with the highest industry standards.

---

## How We Govern AI

ProtoLabs maintains a comprehensive AI governance framework aligned with:

| Framework | Relevance |
|-----------|-----------|
| **EU AI Act** | Risk-based classification and proportional controls for all AI systems |
| **NIST AI RMF 1.0** | Systematic risk management across the AI lifecycle |
| **ISO/IEC 42001** | Certifiable AI management system (certification target: Q1 2027) |
| **GDPR** | Data protection for all customer data processed by AI systems |
| **ITAR/EAR** | Export control compliance for defense and dual-use manufacturing |

---

## Key Principles

1. **Human Oversight** — AI recommendations are advisory. All structural designs require validation by a licensed Professional Engineer (PE) before production.

2. **Transparency** — Every AI-generated output includes source citations back to ProtoLabs' manufacturing knowledge base. You can see where each recommendation comes from.

3. **Data Protection** — Your CAD files and design data are encrypted at rest and in transit. We do not use your data to train AI models. Access is logged and auditable.

4. **Accuracy** — Our AI systems are continuously evaluated against golden datasets. We maintain >90% accuracy targets for all DFM analysis agents.

5. **Safety** — Kill switch mechanisms allow immediate shutdown of any AI system. Safety agents monitor outputs in real-time for quality, drift, and boundary violations.

6. **Accountability** — Every AI system has a named business owner and technical owner responsible for its outcomes and compliance.

---

## Risk Classification

ProtoLabs classifies all AI systems into three tiers:

| Tier | Description | Example | Human Involvement |
|------|------------|---------|-------------------|
| **Tier 1** | Advisory — provides recommendations | DFM analysis, material selection | Human decides; AI suggests |
| **Tier 2** | Semi-autonomous — can take actions with human approval | Quote generation, scheduling | Human approves exceptions |
| **Tier 3** | Highly autonomous — acts within defined boundaries | Parameter optimization | Human monitors by exception |

Currently, all customer-facing ProtoLabs AI systems operate at **Tier 1 (Advisory)** — they provide recommendations that human engineers review and act upon.

---

## Your Data

| Concern | Our Practice |
|---------|-------------|
| **CAD file handling** | Encrypted at rest (AES-256) and in transit (TLS 1.2+); access logged |
| **Model training** | Your data is NOT used to train AI models |
| **Data retention** | Per our data processing agreement; deletion available on request |
| **Data residency** | Processing in EU/US data centers per your contract |
| **IP protection** | Design data is isolated per customer; no cross-customer data sharing |

---

## Incident Response

If an AI system produces incorrect or unexpected output:

1. **Detection** — Automated monitoring detects anomalies in real-time
2. **Containment** — Safety mechanisms activate within 30 seconds
3. **Notification** — Affected clients are notified per our incident severity framework
4. **Resolution** — Root cause analysis and corrective action within defined SLAs
5. **Prevention** — Systemic improvements implemented to prevent recurrence

---

## Compliance Certifications

| Certification | Status | Target |
|--------------|--------|--------|
| **ISO/IEC 42001** (AI Management System) | In progress (65% readiness) | Q1 2027 |
| **SOC 2 Type II** | Active | Annual renewal |
| **ISO 9001** (Quality Management) | Active | Annual renewal |

---

## Questions?

Contact your ProtoLabs account representative or email **ai-governance@protolabs.com** for questions about our AI governance practices.

---

*This summary is derived from the ProtoLabs AI Governance Policy. The full policy is available under NDA for enterprise clients.*
