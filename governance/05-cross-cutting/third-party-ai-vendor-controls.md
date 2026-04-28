# Third-Party AI Vendor Controls

> **Document Type:** Cross-Cutting Governance — Vendor Management
> **Version:** 1.0
> **Effective Date:** 2026-04-28
> **Owner:** Chief AI Officer (CAIO)
> **Approved By:** AI Governance Council
> **Review Cycle:** Semi-annual, or upon vendor change
> **Next Review:** 2026-10-28

---

## Purpose

This document defines the controls ProtoLabs applies when integrating third-party AI models, APIs, or services into its workflows. Third-party AI introduces risks that internal development does not: vendor lock-in, opaque model changes, data sovereignty concerns, and supply chain dependencies. These controls ensure that external AI is governed with the same rigor as internal systems.

## When to Use

- When evaluating a new third-party AI model, API, or SaaS tool for integration
- When an existing vendor changes their model, pricing, terms of service, or data handling practices
- When a vendor experiences a security incident or service disruption
- During quarterly vendor review cycle
- During internal audit of third-party AI dependencies

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **CAIO** | **Accountable** — approves all third-party AI integrations |
| **Security Lead** | **Responsible** — conducts vendor security assessment |
| **Legal Counsel** | **Responsible** — reviews contracts and data processing agreements |
| **Technical Owner** | **Responsible** — evaluates technical fit and integration architecture |
| **DPO** | **Reviewer** — validates data protection compliance |
| **Governance Council** | **Approver** — approves integrations touching customer data or production decisions |

## Regulatory Basis

- **EU AI Act Article 25** — Obligations of providers of general-purpose AI models
- **EU AI Act Article 28** — Obligations of importers, distributors, and deployers
- **GDPR Article 28** — Processor agreements
- **ISO/IEC 42001 Clause 8.1** — Operational planning and control (supply chain)
- **NIST AI RMF GV-6.1** — Third-party resources identified and documented
- **NIST AI RMF GV-6.2** — Third-party risk management practices established

---

## 1. Vendor Assessment Checklist

Before any third-party AI is integrated, the following assessment must be completed:

### 1.1 Security Assessment

| ID | Requirement | Priority | Status | Evidence |
|----|-------------|----------|--------|----------|
| VENDOR-SEC-001 | Vendor provides SOC 2 Type II report or equivalent | Critical | | |
| VENDOR-SEC-002 | Vendor encrypts data in transit (TLS 1.2+) and at rest (AES-256+) | Critical | | |
| VENDOR-SEC-003 | Vendor provides incident notification SLA (≤72 hours) | Critical | | |
| VENDOR-SEC-004 | Vendor has vulnerability management program | High | | |
| VENDOR-SEC-005 | Vendor provides penetration test results (annual) | High | | |
| VENDOR-SEC-006 | Vendor supports API key rotation and access revocation | High | | |
| VENDOR-SEC-007 | Vendor provides data residency options (EU/US) | Medium | | |

### 1.2 Privacy and Data Protection Assessment

| ID | Requirement | Priority | Status | Evidence |
|----|-------------|----------|--------|----------|
| VENDOR-DP-001 | Vendor provides Data Processing Agreement (DPA) | Critical | | |
| VENDOR-DP-002 | DPA specifies data retention and deletion obligations | Critical | | |
| VENDOR-DP-003 | Vendor confirms customer data is NOT used for model training | Critical | | |
| VENDOR-DP-004 | Vendor provides GDPR Article 28-compliant processor terms | Critical | | |
| VENDOR-DP-005 | Vendor supports data subject access requests (DSAR) | High | | |
| VENDOR-DP-006 | Vendor provides data breach notification within 48 hours | High | | |

### 1.3 Model Governance Assessment

| ID | Requirement | Priority | Status | Evidence |
|----|-------------|----------|--------|----------|
| VENDOR-MG-001 | Vendor provides advance notice of model changes (≥30 days) | Critical | | |
| VENDOR-MG-002 | Vendor provides model version pinning (ability to stay on specific version) | Critical | | |
| VENDOR-MG-003 | Vendor provides model performance SLA (uptime, latency) | High | | |
| VENDOR-MG-004 | Vendor provides content safety and filtering capabilities | High | | |
| VENDOR-MG-005 | Vendor provides usage analytics and audit logs | Medium | | |
| VENDOR-MG-006 | Vendor provides model evaluation methodology or benchmarks | Medium | | |

### 1.4 Commercial Assessment

| ID | Requirement | Priority | Status | Evidence |
|----|-------------|----------|--------|----------|
| VENDOR-COM-001 | Pricing model documented with cost projections at expected volume | Critical | | |
| VENDOR-COM-002 | Contract includes termination clause with data return/deletion | Critical | | |
| VENDOR-COM-003 | Contract includes liability and indemnification terms | High | | |
| VENDOR-COM-004 | Vendor provides business continuity plan | High | | |
| VENDOR-COM-005 | Vendor provides SLA with financial penalties for breach | Medium | | |

---

## 2. Data Processing Agreement Requirements

Every third-party AI integration must have a DPA that includes:

| Clause | Requirement |
|--------|-------------|
| **Data scope** | Exactly what data is shared (inputs, outputs, metadata) |
| **Processing purpose** | Limited to ProtoLabs' stated use case |
| **Data retention** | Maximum retention period; deletion upon contract termination |
| **Sub-processor controls** | Vendor must notify ProtoLabs before engaging sub-processors |
| **Data location** | Where data is stored and processed (geographic restrictions) |
| **Training prohibition** | Explicit clause: vendor shall NOT use ProtoLabs data for model training |
| **Audit rights** | ProtoLabs may audit vendor's data handling (or accept third-party audit) |
| **Breach notification** | Vendor must notify ProtoLabs within 48 hours of data breach |
| **Data return** | Upon termination, vendor returns all ProtoLabs data and certifies deletion |

---

## 3. Model Provenance Registry

Every integrated third-party model must be registered:

```yaml
vendor_registry:
  - vendor_id: "VENDOR-ANTHROPIC"
    vendor_name: "Anthropic"
    model_name: "Claude 3.5 Sonnet"
    model_version: "2024-10-22"
    api_version: "v1"
    agents_using:
      - "dfm-router"
      - "cnc-machining"
      - "injection-molding"
      - "sheet-metal"
      - "3d-printing"
      - "materials-selection"
    integration_type: "api"
    data_shared: "part_description_text, cad_metadata"
    customer_data_shared: false
    dpa_signed: true
    dpa_expiry: "2027-04-28"
    security_assessment_date: "2026-04-28"
    security_assessment_result: "pass"
    next_review_date: "2026-10-28"
    exit_strategy: "Migrate to self-hosted open-source model (Llama 3 or equivalent)"
    exit_timeline: "4-6 weeks"
    exit_cost_estimate: "Engineering effort: 2 FTE-months"
    status: "active"
```

Registry is maintained at `governance/05-cross-cutting/vendor-registry.yaml`.

---

## 4. Exit Strategy Requirements

Every vendor integration must have a documented exit strategy:

| Component | Requirement |
|-----------|-------------|
| **Alternative model** | Identify at least one alternative (open-source or competing vendor) |
| **Migration path** | Document how to switch from vendor to alternative (API differences, prompt changes, eval re-run) |
| **Timeline estimate** | Estimated time to complete migration |
| **Cost estimate** | Engineering effort and any licensing costs |
| **Data migration** | How to extract and transfer any vendor-held data |
| **Testing plan** | How to validate the alternative meets performance requirements |
| **Trigger criteria** | What events trigger exit (vendor price increase >50%, terms of service change, security breach, service discontinuation) |

---

## 5. Ongoing Vendor Monitoring

| Activity | Frequency | Owner |
|----------|-----------|-------|
| Vendor security posture review | Semi-annual | Security Lead |
| DPA compliance verification | Annual | DPO |
| Model performance monitoring | Continuous | Technical Owner |
| Cost monitoring vs. projections | Monthly | Technical Owner |
| Vendor change notification review | As received | Technical Owner |
| Exit strategy readiness check | Annual | Technical Owner |
| Full vendor re-assessment | Annual | Governance Council |

---

## 6. Vendor Incident Response

If a third-party AI vendor experiences a security incident:

| Step | Action | Owner | SLA |
|------|--------|-------|-----|
| 1 | Vendor notifies ProtoLabs per DPA | Vendor | ≤48 hours |
| 2 | Assess impact on ProtoLabs data and systems | Security Lead | ≤4 hours |
| 3 | Determine if customer data is affected | DPO | ≤8 hours |
| 4 | Activate containment (disable API key, pause integration) | Technical Owner | ≤1 hour (if data breach) |
| 5 | Notify Governance Council | CAIO | ≤24 hours |
| 6 | Notify affected customers (if applicable) | Policy Owner + Legal | Per GDPR Art. 34 |
| 7 | Assess exit strategy activation | CAIO + Governance Council | ≤5 business days |
| 8 | Post-incident review | Governance Council | ≤15 business days |

---

## Cross-References

| Document | Relationship |
|----------|-------------|
| [AI Governance Policy](ai-governance-policy.md) | Parent policy; this document implements Section 7 |
| [Approval Thresholds by Tier](approval-thresholds-by-tier.md) | Vendor integrations require tier-appropriate approval |
| [Regulatory Reference Index](regulatory-reference-index.md) | Regulatory basis for vendor controls |
| [Incident Severity Classification](../04-operational-governance/incident-severity-classification.md) | Vendor incidents classified per severity framework |
| [Model Card Template](../02-development-governance/templates/model-card.md) | Model card documents third-party dependencies |
| [Prompt Registry](../02-development-governance/prompt-registry.md) | Prompt registry tracks vendor model versions |

---

*This document is version-controlled and auditable. Unauthorized modifications void governance compliance claims.*
