# Compliance-as-Configuration

## Purpose

This document defines the architecture for implementing compliance-as-configuration using policy-as-code engines (OPA, Cedar). It enables organizations to define compliance rules in YAML format, evaluate them at runtime, and maintain jurisdictional mappings for multi-region deployments. This approach transforms compliance from documentation into executable, testable, version-controlled configuration.

Compliance-as-Configuration ensures that regulatory requirements are enforced automatically at the governance enforcement pipeline layer, with clear audit trails and the ability to prove compliance through configuration artifacts rather than manual attestations.

## When to Use

- When implementing policy-as-code for AI governance
- When deploying agents across multiple jurisdictions with different regulations
- When automating compliance checks in the governance pipeline
- When preparing for regulatory audits with evidence-based compliance
- When updating compliance rules to match regulatory changes
- When integrating compliance into CI/CD pipelines

## Who Is Responsible

| Role | R/A/C/I | Responsibility |
|------|---------|---------------|
| **Compliance Engineer** | Accountable | Defines compliance rules and jurisdictional mappings |
| **Policy Engine Administrator** | Responsible | Manages OPA/Cedar deployment and rule distribution |
| **Security Engineer** | Responsible | Ensures policy engine integrity and access controls |
| **AI/ML Engineer** | Consulted | Integrates compliance checks into agent runtime |
| **Legal Counsel** | Consulted | Validates regulatory interpretation |
| **Internal Audit (3rd Line)** | Reviewer | Independently verifies compliance rule effectiveness |

## Regulatory Basis

- **EU AI Act Article 9** -- Risk management system including automated controls
- **EU AI Act Article 12** -- Record-keeping with automated logging
- **GDPR Article 25** -- Data protection by design and by default
- **DORA Article 9** -- ICT risk management framework
- **SOC 2 CC6.1** -- Logical access security with automated enforcement
- **ISO 27001 A.12.1** -- Operational procedures with automated controls

---

## 1. Policy Engine Architecture

### 1.1 OPA (Open Policy Agent) Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         OPA POLICY ENGINE ARCHITECTURE                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐       │
│  │   Policy Bundle │────>│   OPA Server    │<────│   Agent Runtime │       │
│  │   (Rego + YAML) │     │                 │     │   (Query/Update)│       │
│  └─────────────────┘     │  ┌───────────┐  │     └─────────────────┘       │
│          ▲               │  │  Policy   │  │              ▲                │
│          │               │  │  Cache    │  │              │                │
│  ┌───────┴───────┐       │  └───────────┘  │     ┌────────┴────────┐       │
│  │  Policy Repo  │       │  ┌───────────┐  │     │  Decision Logs  │       │
│  │  (Git)        │       │  │  Data     │  │     │  (Audit Trail)  │       │
│  └───────────────┘       │  │  Cache    │  │     └─────────────────┘       │
│                          │  └───────────┘  │                               │
│                          └─────────────────┘                               │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Key Components:**

| Component | Purpose | Implementation |
|-----------|---------|----------------|
| **Policy Bundle** | Versioned Rego policies and YAML data | Git repository with CI/CD |
| **OPA Server** | Policy evaluation engine | Kubernetes deployment or sidecar |
| **Data Cache** | Contextual data for policy decisions | In-memory with refresh |
| **Decision Logs** | Every policy decision logged | Append-only audit stream |

### 1.2 Cedar Architecture

Cedar is AWS's policy language designed specifically for authorization:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         CEDAR POLICY ARCHITECTURE                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐       │
│  │   Cedar Schema  │────>│   Cedar Engine  │<────│   Agent Runtime │       │
│  │   (Entities)    │     │                 │     │   (AuthZ Query) │       │
│  └─────────────────┘     │  ┌───────────┐  │     └─────────────────┘       │
│          ▲               │  │  Policy   │  │              ▲                │
│          │               │  │  Store    │  │              │                │
│  ┌───────┴───────┐       │  └───────────┘  │     ┌────────┴────────┐       │
│  │  Policy Repo  │       │  ┌───────────┐  │     │  Audit Events   │       │
│  │  (Cedar)      │       │  │  Entity   │  │     │  (CloudTrail)   │       │
│  └───────────────┘       │  │  Store    │  │     └─────────────────┘       │
│                          │  └───────────┘  │                               │
│                          └─────────────────┘                               │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. YAML Compliance Rule Format

### 2.1 Rule Structure

```yaml
# compliance-rule-config.yaml
rule_id: "<unique_identifier>"
rule_version: "<semver>"
rule_name: "<human_readable_name>"
description: "<what this rule enforces>"

# Regulatory mapping
regulatory_basis:
  regulation: "<EU_AI_ACT | GDPR | DORA | SOC2 | HIPAA | etc>"
  article: "<specific_article>"
  section: "<specific_section>"
  jurisdiction: "<applicable_jurisdiction>"
  effective_date: "<YYYY-MM-DD>"

# Rule metadata
metadata:
  created_by: "<author>"
  created_at: "<YYYY-MM-DD>"
  last_modified: "<YYYY-MM-DD>"
  review_date: "<YYYY-MM-DD>"
  status: "<draft | active | deprecated>"
  priority: "<critical | high | medium | low>"

# Enforcement configuration
enforcement:
  level: "<block | warn | audit | log>"
  auto_remediation: <true | false>
  escalation_required: <true | false>
  
# Policy logic (OPA Rego)
rego_policy: |
  package agent.compliance
  
  import future.keywords.if
  import future.keywords.in
  
  default allow := false
  
  allow if {
      input.agent.risk_tier == "minimal"
  }
  
  allow if {
      input.agent.risk_tier == "limited"
      input.oversight_model in ["HITL", "HOTL"]
  }
  
  allow if {
      input.agent.risk_tier == "high"
      input.oversight_model == "HITL"
      input.human_approval.obtained == true
  }

# Cedar policy (alternative)
cedar_policy: |
  permit (
      principal == Agent::"<agent_id>",
      action == Action::"<action>",
      resource == Resource::"<resource>"
  )
  when {
      context.risk_tier == "minimal" ||
      (context.risk_tier == "high" && context.hitl_approved == true)
  };

# Conditions
conditions:
  - type: "<risk_tier>"
    operator: "<equals | in | greater_than>"
    value: "<value>"
  
  - type: "<jurisdiction>"
    operator: "<in>"
    value: ["<jurisdiction1>", "<jurisdiction2>"]

# Exceptions
exceptions:
  - exception_id: "<id>"
    description: "<reason_for_exception>"
    approved_by: "<approver>"
    expiry_date: "<YYYY-MM-DD>"
    conditions:
      - "<specific_condition>"

# Audit requirements
audit:
  log_decision: <true | false>
  log_context: <true | false>
  retention_days: <integer>
  evidence_required: ["<evidence_type1>", "<evidence_type2>"]
```

### 2.2 Example: EU AI Act High-Risk System Rule

```yaml
rule_id: "EU-AI-ACT-HIGH-RISK-001"
rule_version: "1.0.0"
rule_name: "EU AI Act High-Risk System Requirements"
description: "Ensures high-risk AI systems meet EU AI Act Article 14-16 requirements"

regulatory_basis:
  regulation: "EU_AI_ACT"
  article: "14, 15, 16"
  section: "High-risk AI system obligations"
  jurisdiction: ["EU", "EEA"]
  effective_date: "2026-08-02"

metadata:
  created_by: "Compliance Engineering"
  created_at: "2026-03-26"
  last_modified: "2026-03-26"
  review_date: "2026-06-26"
  status: "active"
  priority: "critical"

enforcement:
  level: "block"
  auto_remediation: false
  escalation_required: true

rego_policy: |
  package eu_ai_act.high_risk
  
  import future.keywords.if
  
  default compliant := false
  
  # High-risk systems must have HITL
  compliant if {
      input.agent.risk_classification == "high"
      input.oversight_model == "HITL"
      input.human_oversight.measures_implemented == true
  }
  
  # Must have logging capability
  compliant if {
      input.agent.risk_classification == "high"
      input.logging.enabled == true
      input.logging.retention_days >= 6 * 365  # 6 years
  }
  
  # Must have accuracy measures
  compliant if {
      input.agent.risk_classification == "high"
      input.accuracy.metrics_defined == true
      input.accuracy.validation_performed == true
  }

conditions:
  - type: "risk_classification"
    operator: "equals"
    value: "high"
  
  - type: "jurisdiction"
    operator: "in"
    value: ["EU", "EEA"]

audit:
  log_decision: true
  log_context: true
  retention_days: 2555  # 7 years
  evidence_required: ["risk_assessment", "oversight_documentation", "accuracy_report"]
```

---

## 3. Jurisdictional Mapping

### 3.1 Multi-Jurisdiction Configuration

```yaml
# jurisdictional-mapping.yaml
mapping_version: "1.0.0"
last_updated: "2026-03-26"

jurisdictions:
  - code: "EU"
    name: "European Union"
    regulations:
      - "EU_AI_ACT"
      - "GDPR"
      - "DORA"
    default_rules:
      - "EU-AI-ACT-HIGH-RISK-001"
      - "GDPR-DATA-MINIMIZATION-001"
      - "DORA-ICT-RISK-001"
    data_residency: "EU"
    
  - code: "UK"
    name: "United Kingdom"
    regulations:
      - "UK_AI_REGULATION"
      - "UK_GDPR"
    default_rules:
      - "UK-AI-HIGH-RISK-001"
      - "UK-GDPR-DATA-001"
    data_residency: "UK"
    
  - code: "US-CA"
    name: "California, USA"
    regulations:
      - "CCPA"
      - "COLORADO_AI_ACT"
    default_rules:
      - "CCPA-CONSUMER-RIGHTS-001"
      - "CO-AI-HIGH-RISK-001"
    data_residency: "US"
    
  - code: "SG"
    name: "Singapore"
    regulations:
      - "PDPA"
      - "MAS_AI_GUIDANCE"
    default_rules:
      - "PDPA-CONSENT-001"
      - "MAS-AI-GOVERNANCE-001"
    data_residency: "APAC"

# Rule applicability matrix
rule_applicability:
  - rule_id: "EU-AI-ACT-HIGH-RISK-001"
    applies_to: ["EU", "EEA"]
    overrides: []
    
  - rule_id: "GDPR-DATA-MINIMIZATION-001"
    applies_to: ["EU", "EEA", "UK"]
    overrides: []
    
  - rule_id: "DORA-ICT-RISK-001"
    applies_to: ["EU"]
    overrides: []
    
  - rule_id: "CO-AI-HIGH-RISK-001"
    applies_to: ["US-CO", "US-CA"]  # Colorado AI Act applies to Colorado residents
    overrides: []

# Conflict resolution
conflict_resolution:
  strategy: "most_restrictive"  # When rules conflict, apply most restrictive
  precedence:
    - "EU_AI_ACT"
    - "GDPR"
    - "DORA"
    - "UK_AI_REGULATION"
    - "COLORADO_AI_ACT"
    - "CCPA"
```

### 3.2 Data Residency Enforcement

```yaml
# data-residency-config.yaml
residency_rules:
  - jurisdiction: "EU"
    data_classes: ["PII", "FINANCIAL", "HEALTH"]
    storage_location: "EU_WEST"
    processing_location: "EU_WEST"
    cross_border_transfer: "prohibited"
    exceptions:
      - "adequacy_decision"
      - "standard_contractual_clauses"
  
  - jurisdiction: "CN"
    data_classes: ["PII", "NATIONAL_SECURITY"]
    storage_location: "CN_NORTH"
    processing_location: "CN_NORTH"
    cross_border_transfer: "security_assessment_required"
    exceptions: []

enforcement:
  method: "block"
  audit: true
  alert: true
```

---

## 4. Runtime Integration

### 4.1 Governance Pipeline Integration

The compliance-as-configuration system integrates with Layer 1 of the governance enforcement pipeline:

```
Agent Request
    │
    v
┌─────────────────────────────────────┐
│ LAYER 1: COMPLIANCE CHECK           │
│                                     │
│ 1. Determine jurisdiction from      │
│    tenant_id / user_location        │
│                                     │
│ 2. Query OPA/Cedar with:            │
│    - agent context                  │
│    - requested action               │
│    - jurisdiction rules             │
│                                     │
│ 3. Evaluate all applicable rules    │
│                                     │
│ 4. Return: ALLOW / DENY + reasons   │
└─────────────────────────────────────┘
    │
    v (if ALLOW)
Continue to Layer 2 (Budget Check)
```

### 4.2 OPA Query Example

```python
import requests
import json

def check_compliance(agent_context, action, jurisdiction):
    """Query OPA for compliance decision"""
    
    query = {
        "input": {
            "agent": {
                "id": agent_context["agent_id"],
                "risk_tier": agent_context["risk_tier"],
                "oversight_model": agent_context["oversight_model"]
            },
            "action": action,
            "jurisdiction": jurisdiction,
            "timestamp": datetime.utcnow().isoformat()
        }
    }
    
    response = requests.post(
        "http://opa:8181/v1/data/agent/compliance/allow",
        json=query
    )
    
    decision = response.json()
    
    # Log decision for audit
    log_compliance_decision(agent_context, action, jurisdiction, decision)
    
    return decision["result"]
```

---

## 5. Testing and Validation

### 5.1 Policy Testing Framework

```yaml
# test-suite.yaml
test_suite_id: "compliance-tests-001"
tests:
  - name: "EU High-Risk Without HITL Should Fail"
    input:
      agent:
        risk_tier: "high"
        oversight_model: "HOTA"
      jurisdiction: "EU"
    expected_result: false
    expected_violations: ["EU-AI-ACT-HIGH-RISK-001"]
  
  - name: "EU High-Risk With HITL Should Pass"
    input:
      agent:
        risk_tier: "high"
        oversight_model: "HITL"
        human_oversight:
          measures_implemented: true
      jurisdiction: "EU"
    expected_result: true
    expected_violations: []
  
  - name: "Minimal Risk Any Oversight Should Pass"
    input:
      agent:
        risk_tier: "minimal"
        oversight_model: "HOTA"
      jurisdiction: "EU"
    expected_result: true
```

### 5.2 Continuous Compliance Validation

| Check | Frequency | Owner |
|-------|-----------|-------|
| Policy syntax validation | Every commit | CI/CD |
| Unit tests for rules | Every commit | CI/CD |
| Integration tests | Daily | Compliance Engineering |
| Rule coverage analysis | Weekly | Compliance Engineering |
| Staleness check (expired rules) | Weekly | Compliance Engineering |

---

## 6. Related Artifacts

- [Compliance Rule Config](compliance-rule-config.yaml) -- Individual rule template
- [Governance Enforcement Pipeline](../../03-runtime-governance/agentic-workflows/governance-enforcement-pipeline.md) -- Layer 1 integration
- [Audit Record Schema](audit-record-schema.yaml) -- Compliance decision logging
- [Expanded Regulatory Mapping](../regulatory/expanded-regulatory-mapping.md) -- Regulatory coverage matrix

---

*Last updated: 2026-03-26 / Version: 1.0 / Classification: Internal*
