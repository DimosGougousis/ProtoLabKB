# Expanded Regulatory Mapping

## Purpose

This document extends the framework's regulatory coverage beyond the EU AI Act, GDPR, and DORA to include SOC 2, HIPAA, Colorado AI Act, and PCI DSS. It maps each regulation's requirements to specific framework artifacts, enabling organizations to demonstrate compliance across multiple regulatory regimes.

Multi-regulatory compliance is essential for organizations operating across jurisdictions and industries. This mapping ensures that implementing the framework addresses requirements from all applicable regulations.

## When to Use

- When determining which regulations apply to your AI deployment
- When preparing for multi-framework compliance audits
- When expanding operations to new jurisdictions
- When handling data subject to multiple regulatory regimes (e.g., healthcare + financial)
- When mapping framework controls to auditor expectations
- When identifying gaps in regulatory coverage

## Who Is Responsible

| Role | R/A/C/I | Responsibility |
|------|---------|---------------|
| **Compliance Officer** | Accountable | Maintains regulatory mapping and ensures completeness |
| **Legal Counsel** | Responsible | Interprets regulatory requirements and updates |
| **Risk Manager** | Responsible | Assesses regulatory risk and prioritization |
| **AI Governance Committee** | Approver | Reviews and approves compliance strategy |
| **Internal Audit** | Reviewer | Validates mapping accuracy and control effectiveness |

---

## 1. Regulatory Coverage Matrix

| Regulation | Domain | Geographic Scope | Framework Artifacts |
|------------|--------|------------------|---------------------|
| **EU AI Act** | AI Systems | EU/EEA | Comprehensive coverage across all pillars |
| **GDPR** | Data Protection | EU/EEA + global reach | Data contracts, audit records, consent |
| **DORA** | ICT Risk | EU Financial Sector | Operational resilience, incident management |
| **SOC 2** | Security & Availability | Global (US-focused) | Security controls, monitoring, audit |
| **HIPAA** | Health Information | US Healthcare | PHI protection, access controls, audit |
| **Colorado AI Act** | AI Systems | Colorado, USA | High-risk AI, algorithmic discrimination |
| **PCI DSS** | Payment Security | Global | Cardholder data protection, access controls |

---

## 2. SOC 2 Mapping

### 2.1 SOC 2 Trust Services Criteria

| TSC Category | SOC 2 Requirement | Framework Artifact | Implementation |
|--------------|-------------------|-------------------|----------------|
| **Security (CC6)** | Logical access controls | Agent Permission Boundaries | NHI, RBAC, SPIFFE identities |
| **Security (CC6)** | Access removal | Agent Registry | Decommissioning procedures |
| **Security (CC7)** | System monitoring | Model Monitoring Dashboard | Real-time monitoring, alerting |
| **Availability (A1)** | System availability | Fallback Procedure | Degradation levels, recovery |
| **Availability (A1)** | Incident response | Kill Switch Specification | Emergency procedures |
| **Processing Integrity (PI1)** | Complete processing | Delegation Chain Audit | Full transaction tracing |
| **Processing Integrity (PI1)** | Valid processing | Governance Enforcement Pipeline | Validation at each layer |
| **Confidentiality (C1)** | Confidential information protection | Multi-Tenant Isolation | 6-layer isolation model |
| **Confidentiality (C1)** | Encryption | Audit Record Schema | Encryption at rest/transit |

### 2.2 SOC 2 Type II Evidence

| SOC 2 Control | Evidence Location | Retention |
|---------------|-------------------|-----------|
| Access reviews | Agent Registry quarterly reviews | 7 years |
| Change management | CI/CD governance gates | 7 years |
| Incident response | Kill switch test records | 7 years |
| System monitoring | Model monitoring dashboards | 1 year |
| Audit trails | Audit Record Schema logs | 7 years |

---

## 3. HIPAA Mapping

### 3.1 HIPAA Security Rule

| HIPAA Requirement | Framework Artifact | Implementation |
|-------------------|-------------------|----------------|
| **§164.312(a)(1)** - Access Control | Agent Permission Boundaries | Unique user identification, emergency access |
| **§164.312(a)(2)(i)** - Audit Controls | Audit Record Schema | Record all PHI access with integrity chain |
| **§164.312(a)(2)(ii)** - Integrity | Multi-Tenant Isolation | Data integrity controls, no unauthorized modification |
| **§164.312(a)(2)(iv)** - Encryption | Audit Record Schema | Encryption of PHI at rest and in transit |
| **§164.312(b)** - Audit Controls | Delegation Chain Audit | Full audit trail of PHI access |
| **§164.312(c)(1)** - Integrity Controls | Governance Enforcement Pipeline | Layer 1 compliance checks |
| **§164.312(c)(2)** - Mechanism to Authenticate | SPIFFE Agent Identity | Cryptographic authentication |
| **§164.312(d)** - Person/Entity Authentication | Per-Skill RBAC | Verify identity before PHI access |
| **§164.312(e)(1)** - Transmission Security | Multi-Tenant Isolation | Network isolation, TLS 1.3 |

### 3.2 HIPAA Privacy Rule

| HIPAA Requirement | Framework Artifact | Implementation |
|-------------------|-------------------|----------------|
| **Minimum Necessary** | Agent Permission Boundaries | Least privilege access to PHI |
| **Accounting of Disclosures** | Audit Record Schema | 20+ field audit records |
| **Business Associate Agreements** | Compliance-as-Configuration | Contractual compliance rules |

### 3.3 HIPAA-Specific Controls

```yaml
# HIPAA-specific compliance configuration
hipaa_controls:
  phi_access:
    requires_authorization: true
    minimum_necessary: true
    audit_all_access: true
    
  encryption:
    at_rest: "AES-256-GCM"
    in_transit: "TLS-1.3"
    key_management: "HSM-backed"
    
  access_control:
    unique_user_id: true
    emergency_access_procedure: documented
    automatic_logoff: 15_minutes
    
  audit:
    record_all_phi_access: true
    integrity_protection: hash_chain
    retention: 6_years
```

---

## 4. Colorado AI Act Mapping

### 4.1 Colorado AI Act Requirements

The Colorado AI Act (SB 24-205), effective February 1, 2026, regulates high-risk AI systems to prevent algorithmic discrimination.

| CO AI Act Requirement | Framework Artifact | Implementation |
|-----------------------|-------------------|----------------|
| **Risk Assessment** | EU AI Act Risk Classification | 5-dimension risk assessment |
| **Algorithmic Discrimination** | Bias Testing in Evaluations | Fairness metrics, disparate impact |
| **Notice to Consumers** | Customer-Facing Agent Safety | Disclosure requirements |
| **Human Oversight** | Human-in-the-Loop Patterns | HITL/HOTL/HOTA models |
| **Documentation** | Model Cards | High-risk system documentation |
| **Annual Review** | Governance Maturity Roadmap | Continuous review process |

### 4.2 High-Risk System Definition (Colorado)

| Category | Colorado Definition | Framework Mapping |
|----------|---------------------|-------------------|
| **Employment** | Screening, hiring, promotion | Agent risk tier: High |
| **Housing** | Rental, sale, financing | Agent risk tier: High |
| **Education** | Admissions, discipline | Agent risk tier: High |
| **Financial Services** | Credit, lending, insurance | Agent risk tier: High |
| **Healthcare** | Care decisions, prior auth | Agent risk tier: High |
| **Legal** | Legal representation | Agent risk tier: High |

### 4.3 Colorado-Specific Configuration

```yaml
# Colorado AI Act compliance configuration
colorado_ai_act:
  applicable: true
  effective_date: "2026-02-01"
  
  high_risk_systems:
    - system_type: "employment_screening"
      risk_tier: "high"
      bias_testing_required: true
      notice_to_applicants: true
      human_review_required: true
      
    - system_type: "credit_decision"
      risk_tier: "high"
      disparate_impact_threshold: 0.80  # Four-fifths rule
      annual_audit_required: true
  
  documentation_required:
    - risk_assessment
    - bias_audit_results
    - oversight_measures
    - consumer_notice
```

---

## 5. PCI DSS Mapping

### 5.1 PCI DSS Requirements

| PCI DSS Requirement | Framework Artifact | Implementation |
|---------------------|-------------------|----------------|
| **Req 1** - Firewall | Multi-Tenant Isolation | Network segmentation |
| **Req 2** - Default Security | Agent Permission Boundaries | Default deny, least privilege |
| **Req 3** - Stored CHD Protection | Audit Record Schema | Encryption, tokenization |
| **Req 4** - Transmission Encryption | Multi-Tenant Isolation | TLS 1.3, strong cryptography |
| **Req 7** - Access Control | Per-Skill RBAC | Need-to-know access |
| **Req 8** - Identity Management | SPIFFE Agent Identity | Strong authentication |
| **Req 10** - Logging | Audit Record Schema | Comprehensive audit trail |
| **Req 11** - Security Testing | Evaluations | Regular security testing |

### 5.2 Cardholder Data Environment (CDE) Isolation

For agents processing payment data:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    PCI DSS COMPLIANT AGENT ARCHITECTURE                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    CARDHOLDER DATA ENVIRONMENT                       │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────────┐  │   │
│  │  │   Payment   │  │   Token     │  │   Audit Log (No CHD)        │  │   │
│  │  │   Agent     │  │   Service   │  │   • Access attempts         │  │   │
│  │  │             │  │             │  │   • Tool invocations        │  │   │
│  │  │ • CHD only  │  │ • PAN →     │  │   • Decisions               │  │   │
│  │  │   in memory │  │   Token     │  │   • No sensitive data       │  │   │
│  │  │ • No logs   │  │             │  │                             │  │   │
│  │  └─────────────┘  └─────────────┘  └─────────────────────────────┘  │   │
│  │                                                                     │   │
│  │  Network: Isolated VLAN, no direct internet access                  │   │
│  │  Access: SPIFFE identity + MFA + JIT access                         │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                              │                                              │
│                              │ API Gateway (Tokenized)                      │
│                              ▼                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    CORPORATE NETWORK                                 │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────────┐  │   │
│  │  │   Other     │  │   Audit     │  │   Monitoring                │  │   │
│  │  │   Agents    │  │   System    │  │   Dashboard                 │  │   │
│  │  │             │  │             │  │                             │  │   │
│  │  │ • No CHD    │  │ • Complete  │  │ • No CHD in logs            │  │   │
│  │  │   access    │  │   audit     │  │ • Token references only     │  │   │
│  │  └─────────────┘  └─────────────┘  └─────────────────────────────┘  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 5.3 PCI DSS-Specific Controls

```yaml
# PCI DSS compliance configuration
pci_dss:
  applicable: true
  saq_type: "D"  # Service Provider
  
  chd_handling:
    storage: "prohibited"  # Agents never store CHD
    processing: "tokenized"
    transmission: "encrypted_tls_1_3"
    
  network_segmentation:
    cde_isolated: true
    firewall_rules: "default_deny"
    access_logging: true
    
  access_control:
    unique_ids: true
    role_based: true
    least_privilege: true
    quarterly_review: true
    
  monitoring:
    audit_all_cde_access: true
    integrity_monitoring: true
    daily_log_review: true
```

---

## 6. Cross-Regulatory Compliance Strategy

### 6.1 Common Controls

Controls that satisfy multiple regulations:

| Control | EU AI Act | GDPR | DORA | SOC 2 | HIPAA | CO AI | PCI DSS |
|---------|-----------|------|------|-------|-------|-------|---------|
| Audit Logging | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Access Control | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Encryption | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Risk Assessment | ✓ | ✓ | ✓ | | | ✓ | |
| Human Oversight | ✓ | | | | | ✓ | |
| Bias Testing | ✓ | | | | | ✓ | |
| Incident Response | ✓ | ✓ | ✓ | ✓ | ✓ | | ✓ |
| Data Minimization | | ✓ | | | ✓ | | ✓ |

### 6.2 Compliance Automation

```yaml
# Multi-regulatory compliance rule
multi_regulatory_rule:
  rule_id: "COMMON-AUDIT-001"
  name: "Comprehensive Audit Logging"
  
  satisfies:
    - regulation: "EU_AI_ACT"
      article: "12"
      
    - regulation: "GDPR"
      article: "30"
      
    - regulation: "DORA"
      article: "9"
      
    - regulation: "SOC2"
      criterion: "CC7.2"
      
    - regulation: "HIPAA"
      section: "164.312(b)"
      
    - regulation: "COLORADO_AI_ACT"
      requirement: "documentation"
      
    - regulation: "PCI_DSS"
      requirement: "10.1"
  
  implementation:
    artifact: "audit-record-schema.yaml"
    fields: 20
    integrity: "hash_chain"
    retention: "7_years"
    encryption: "AES-256-GCM"
```

---

## 7. Related Artifacts

- [Compliance-as-Configuration](../templates/compliance-as-configuration.md) -- Policy engine integration
- [Compliance Rule Config](../templates/compliance-rule-config.yaml) -- Individual rule template
- [Audit Record Schema](../templates/audit-record-schema.yaml) -- Multi-regulatory audit logging
- [Regulatory Reference Index](../../05-cross-cutting/regulatory-reference-index.md) -- Quick reference

---

*Last updated: 2026-03-26 / Version: 1.0 / Classification: Internal*
