# GRC Platform Integration for AI Governance

## Purpose

This document defines the strategy for mapping the YAML governance checklists and governance artifacts in this framework to enterprise Governance, Risk, and Compliance (GRC) platforms -- specifically ServiceNow GRC, RSA Archer, and OneTrust. GRC platforms are the enterprise system of record for regulatory compliance, risk management, and audit. Without integration, AI governance exists in parallel to the enterprise compliance program, creating duplicate work, inconsistent reporting, and blind spots during regulatory examinations. This integration makes AI governance a first-class participant in the enterprise GRC ecosystem.

## When to Use

- When implementing the GRC integration phase of the [Adoption Playbook](../../07-enterprise-implementation/risk-based-adoption/adoption-playbook.md) (Months 10-12)
- When the organization already uses a GRC platform and wants to incorporate AI governance controls
- When preparing for regulatory examinations where AI governance evidence must be presented alongside enterprise risk and compliance evidence
- When designing automated evidence collection pipelines from AI monitoring to GRC attestation
- When mapping SAFEST items to enterprise control frameworks (COBIT, ISO 27001)

## Who Is Responsible

| Role | R | A | C | I |
|------|---|---|---|---|
| **GRC Platform Administrator** | X | | | | Configures GRC platform objects, mappings, and workflows |
| **Compliance Officer (2nd Line)** | | X | | | Owns the control mapping; validates completeness and accuracy |
| **AI Governance PM** | X | | | | Defines AI-specific mapping requirements; validates integration |
| **CAIO** | | | X | | Consulted on AI governance scope within enterprise GRC |
| **Internal Audit (3rd Line)** | | | X | | Consulted on audit trail requirements and evidence standards |
| **IT Operations** | | | X | | Consulted on integration architecture (APIs, data flows) |
| **Model Owner** | | | | X | Informed of evidence collection requirements from their systems |

## Regulatory Basis

- **SAFEST items A-01 through A-18** -- All Accountability pillar items require documented controls and evidence
- **EU AI Act Article 17** -- Quality management system; GRC integration demonstrates systematic QMS
- **EU AI Act Article 12** -- Record-keeping; GRC platform provides centralized audit trail
- **DORA Article 5** -- ICT governance framework; GRC platform is the enterprise governance system
- **DORA Article 13** -- ICT logging and audit trail requirements
- **DORA Article 28(3)** -- Register of Information; GRC can host or integrate with the Register
- **ISO/IEC 42001 Clause 7.5** -- Documented information management
- **Best practice** -- Enterprise GRC integration prevents AI governance from becoming a siloed, shadow compliance program

---

## 1. Mapping Strategy

### 1.1 Architecture Overview

```
+---------------------------+         +---------------------------+
| AI Governance Framework   |         | Enterprise GRC Platform   |
| (This Repository)         |         | (ServiceNow / Archer /    |
|                           |         |  OneTrust)                |
| +---------------------+  |  API /  | +---------------------+  |
| | YAML Checklists     |--+--ETL--->| | Control Catalog      |  |
| | (.yaml files)       |  |         | | (AI-specific controls)|  |
| +---------------------+  |         | +---------------------+  |
|                           |         |                           |
| +---------------------+  |  API /  | +---------------------+  |
| | Jira Governance     |--+--Sync-->| | Issues & Findings    |  |
| | Tickets             |  |         | | (AI governance items) |  |
| +---------------------+  |         | +---------------------+  |
|                           |         |                           |
| +---------------------+  |  API /  | +---------------------+  |
| | Monitoring Dashboard|--+--Feed-->| | Risk Indicators      |  |
| | (metrics & alerts)  |  |         | | (KRIs for AI)        |  |
| +---------------------+  |         | +---------------------+  |
|                           |         |                           |
| +---------------------+  |  Link / | +---------------------+  |
| | Evidence Artifacts  |--+--Ref--->| | Evidence Library     |  |
| | (docs, reports)     |  |         | | (attestation docs)   |  |
| +---------------------+  |         | +---------------------+  |
+---------------------------+         +---------------------------+
```

### 1.2 Mapping Principles

1. **YAML checklist items map to GRC controls.** Each YAML item with an `id` field (e.g., `OPS-MON-01`) becomes a control in the GRC platform's control catalog
2. **SAFEST items are the primary control framework.** The SAFEST taxonomy (S-01 through T-20) provides the control numbering that maps to GRC
3. **Evidence flows from source systems to GRC.** Evidence is generated in CI/CD pipelines, monitoring dashboards, and Jira tickets, then referenced or ingested by the GRC platform
4. **GRC is the reporting layer, not the execution layer.** Teams work in their native tools (Jira, Git, dashboards); GRC aggregates for compliance reporting
5. **Bidirectional status sync.** Control status updates in GRC should reflect the latest state in source systems, and vice versa

---

## 2. YAML Fields to GRC Controls Mapping

### 2.1 Field Mapping Table

| YAML Checklist Field | ServiceNow GRC Field | RSA Archer Field | OneTrust Field | Notes |
|---------------------|---------------------|-----------------|---------------|-------|
| `id` | Control ID | Control ID | Control Identifier | Primary key for mapping |
| `item` | Control Description | Control Statement | Control Description | Human-readable requirement |
| `priority` | Control Criticality | Risk Rating | Priority | Maps: critical=Critical, high=High, medium=Medium, low=Low |
| `status` | Assessment Status | Compliance Status | Control Status | Maps: not_started=Not Assessed, in_progress=In Progress, completed=Effective, not_applicable=N/A |
| `evidence_ref` | Evidence Attachment / URL | Supporting Documentation | Evidence Record | Link to evidence artifact |
| `notes` | Assessment Notes | Findings / Observations | Assessment Notes | Free-text findings |
| `regulatory_ref` | Authority Document Reference | Regulatory Mapping | Regulation Reference | Links to specific regulation article |

### 2.2 YAML Checklist to GRC Control Set Mapping

| YAML Checklist File | GRC Control Set Name | Number of Controls | Regulatory Mapping |
|--------------------|---------------------|-------------------|-------------------|
| `eu-ai-act-risk-classification.yaml` | AI-DISC-RISK | 12 | EU AI Act Art. 6, Annex III |
| `ethical-product-discovery.yaml` | AI-DISC-ETHICS | 18 | EU AI Act Art. 5, 9; SAFEST E-01 to E-06 |
| `user-agency-assessment.yaml` | AI-DISC-AGENCY | 10 | EU AI Act Art. 14; SAFEST F-01 to F-04 |
| `data-quality-checklist.yaml` | AI-DEV-DATA | 15 | EU AI Act Art. 10; SAFEST S-08 to S-12 |
| `bias-testing-checklist.yaml` | AI-DEV-BIAS | 14 | EU AI Act Art. 10(2)(f); SAFEST E-01 to E-03 |
| `model-validation-checklist.yaml` | AI-DEV-VALID | 16 | EU AI Act Art. 9, 15; SAFEST S-19 to S-21 |
| `pre-deployment-gate.yaml` | AI-DEV-GATE | 22 | EU AI Act Art. 17; SAFEST comprehensive |
| `guardrail-deployment-checklist.yaml` | AI-RUN-GUARD | 12 | EU AI Act Art. 14; SAFEST S-13, S-17 |
| `safety-policy-checklist.yaml` | AI-RUN-SAFETY | 15 | EU AI Act Art. 15; SAFEST S-06 |
| `monitoring-setup-checklist.yaml` | AI-OPS-MON | 20 | EU AI Act Art. 72; DORA Art. 10; SAFEST T-15, T-17 |
| `incident-response-checklist.yaml` | AI-OPS-INC | 14 | DORA Art. 17-19; SAFEST A-15 to A-18 |
| `security-threat-model.yaml` | AI-OPS-SEC | 18 | EU AI Act Art. 15; DORA Art. 8-9; SAFEST S-06 |
| `model-retirement-checklist.yaml` | AI-OPS-RET | 10 | Best practice; SAFEST S-01 inventory management |

---

## 3. SAFEST Items Mapping Table

This table maps every SAFEST item to the GRC control structure, enabling direct traceability from DNB supervisory expectations to enterprise compliance tracking.

### 3.1 SOUNDNESS (S) Items

| SAFEST ID | SAFEST Item | GRC Control Set | GRC Control ID | Evidence Source |
|-----------|------------|----------------|---------------|----------------|
| S-01 | AI system inventory | AI-OPS-REG | SAFEST-S-01 | AI system registry (manual or automated) |
| S-02 | Algorithm selection rationale | AI-DEV-VALID | SAFEST-S-02 | Model card -- algorithm selection section |
| S-03 | Model performance metrics | AI-DEV-VALID | SAFEST-S-03 | Eval suite results; monitoring dashboard |
| S-04 | Edge case analysis | AI-DEV-VALID | SAFEST-S-04 | Test plan -- edge case section |
| S-05 | Stress testing results | AI-DEV-VALID | SAFEST-S-05 | Stress test report |
| S-06 | Adversarial robustness testing | AI-OPS-SEC | SAFEST-S-06 | Red-teaming report; vulnerability register |
| S-07 | Confidence and uncertainty quantification | AI-DEV-VALID | SAFEST-S-07 | Model card -- uncertainty section |
| S-08 | Training data documentation | AI-DEV-DATA | SAFEST-S-08 | Data sheet |
| S-09 | Data quality framework | AI-DEV-DATA | SAFEST-S-09 | Data quality assessment report |
| S-10 | Data lineage and provenance | AI-DEV-DATA | SAFEST-S-10 | Data lineage tool output |
| S-11 | Feature engineering documentation | AI-DEV-DATA | SAFEST-S-11 | Model card -- features section |
| S-12 | Data drift detection | AI-OPS-MON | SAFEST-S-12 | Monitoring dashboard -- drift metrics |
| S-13 | Fallback procedures | AI-RUN-GUARD | SAFEST-S-13 | Fallback procedure documentation |
| S-14 | Recovery Time Objective | AI-OPS-MON | SAFEST-S-14 | DR test results |
| S-15 | Payment chain impact analysis | AI-OPS-INC | SAFEST-S-15 | Impact analysis document |
| S-16 | Model rollback capability | AI-RUN-GUARD | SAFEST-S-16 | Rollback test results |
| S-17 | Graceful degradation | AI-RUN-GUARD | SAFEST-S-17 | Degradation test results |
| S-18 | DORA ICT risk management alignment | AI-OPS-REG | SAFEST-S-18 | DORA compliance mapping |
| S-19a | Register of Information | AI-OPS-REG | SAFEST-S-19a | Register of Information (XBRL/XML) |
| S-19b | 116 DNB validation rules | AI-OPS-REG | SAFEST-S-19b | Validation rule test results |
| S-19c | AI-specific entries in Register | AI-OPS-REG | SAFEST-S-19c | Register extract for AI providers |
| S-19d | Register submission readiness | AI-OPS-REG | SAFEST-S-19d | Dry-run submission confirmation |
| S-19 | Independent model validation | AI-DEV-VALID | SAFEST-S-19 | Independent validation report |
| S-20 | Validation frequency | AI-OPS-MON | SAFEST-S-20 | Revalidation schedule + completion records |
| S-21 | Backtesting results | AI-DEV-VALID | SAFEST-S-21 | Backtesting report |

### 3.2 Remaining Pillars (Summary)

| SAFEST Pillar | Item Range | GRC Control Set Prefix | Total Controls |
|--------------|-----------|----------------------|---------------|
| **A -- Accountability** | A-01 to A-18 | AI-GOV-ACC | 18 |
| **F -- Fairness** | F-01 to F-08 | AI-DEV-BIAS / AI-DISC-ETHICS | 8 |
| **E -- Ethics** | E-01 to E-08 | AI-DISC-ETHICS | 8 |
| **S -- Soundness** | S-01 to S-21 | Various (see 3.1) | 25 |
| **T -- Transparency** | T-01 to T-20 | AI-GOV-TRANS | 20 |
| **K -- Knowledge** | K-01 to K-15 | AI-GOV-KNOW | 15 |

---

## 4. Platform-Specific Integration

### 4.1 ServiceNow GRC

**Module:** ServiceNow Integrated Risk Management (IRM) / Policy and Compliance Management

| Integration Component | ServiceNow Object | Configuration |
|----------------------|-------------------|---------------|
| Control catalog | `sn_compliance_control` | Import YAML items as controls with regulatory mappings |
| Control assessments | `sn_compliance_assessment` | Scheduled assessments per revalidation calendar |
| Evidence collection | `sn_compliance_evidence` | Automated evidence attachment from CI/CD and monitoring |
| Risk indicators (KRIs) | `sn_risk_indicator` | Feed AI metrics (drift scores, error rates, SLA breaches) as risk indicators |
| Issues and findings | `sn_compliance_issue` | Sync from Jira governance tickets |
| Audit trail | `sn_audit` | Immutable record of all control status changes |

**Integration Method:**
- **ServiceNow IntegrationHub** for Jira bidirectional sync
- **REST API** for pushing monitoring metrics as risk indicators
- **Import Sets** for bulk YAML-to-control ingestion
- **MID Server** for on-premise data source integration

**Automation Example -- Evidence Collection:**
```
Trigger: CI/CD pipeline completes bias evaluation
Action:
  1. Pipeline pushes evaluation result to ServiceNow REST API
  2. ServiceNow creates Evidence record linked to SAFEST-E-01 control
  3. Control assessment status updated to "Evidence Collected"
  4. If evaluation fails: create Issue record, notify Compliance Officer
```

### 4.2 RSA Archer

**Module:** Archer Policy Management / Regulatory Compliance Management

| Integration Component | Archer Object | Configuration |
|----------------------|--------------|---------------|
| Control catalog | Policy/Standard | Import YAML items as policy statements with control mappings |
| Control assessments | Control Assessment | Questionnaire-based assessment linked to controls |
| Evidence collection | Supporting Documentation | File attachments or URLs linked to control assessments |
| Risk indicators | Key Risk Indicator | AI metrics fed via data feed |
| Issues and findings | Exception / Finding | Synced from Jira governance tickets |
| Regulatory mapping | Authority Document | Map SAFEST items to regulation articles |

**Integration Method:**
- **Archer Data Feeds** for bulk ingestion of YAML controls and metrics
- **Archer REST API** for real-time evidence submission
- **Archer GRC Data Publication** for reporting to external systems

### 4.3 OneTrust

**Module:** OneTrust AI Governance / Ethics & Compliance

| Integration Component | OneTrust Object | Configuration |
|----------------------|----------------|---------------|
| AI system inventory | AI System Record | Sync from AI system registry |
| Risk assessments | AI Impact Assessment | Map to ethics impact assessment template |
| Control catalog | Compliance Control | Import YAML items as compliance controls |
| Evidence collection | Evidence Artifact | Automated upload from CI/CD |
| Regulatory mapping | Regulatory Framework | Map SAFEST and EU AI Act requirements |
| Vendor risk | Third-Party Risk Assessment | LLM provider assessments synced to vendor records |

**Integration Method:**
- **OneTrust REST API** for real-time data exchange
- **OneTrust integrations marketplace** for pre-built connectors
- **Webhook-based** triggers from monitoring and CI/CD systems

---

## 5. Automated Evidence Collection

### 5.1 Evidence Collection Pipeline

| Evidence Type | Source System | Collection Method | GRC Destination | Frequency |
|--------------|-------------|-------------------|----------------|-----------|
| Bias evaluation results | CI/CD pipeline (Giskard, Fairlearn) | API push on pipeline completion | Control SAFEST-E-01, SAFEST-F-01 | Per model deployment |
| Drift detection metrics | Monitoring dashboard (Prometheus/Grafana) | Scheduled API pull (daily) | KRI for SAFEST-S-12 | Daily |
| Model validation report | ML experiment tracker (MLflow, W&B) | API push on validation completion | Control SAFEST-S-19 | Per validation event |
| Penetration test results | Security testing tool (Garak, custom) | Manual upload or API push | Control SAFEST-S-06 | Quarterly or per test |
| Guardrail effectiveness metrics | Runtime monitoring (NeMo, custom) | Scheduled API pull (weekly) | KRI for SAFEST-S-13, S-17 | Weekly |
| Incident reports | Jira (AI Incident tickets) | Bidirectional sync | Issue/Finding records | Per incident |
| Training completion records | LMS / HR system | Scheduled API pull (monthly) | Control SAFEST-K-09, K-11 | Monthly |
| Data quality metrics | Data pipeline monitoring | Scheduled API pull (daily) | KRI for SAFEST-S-09 | Daily |

### 5.2 Evidence Quality Requirements

| Requirement | Description | Enforcement |
|-------------|-------------|-------------|
| **Timestamped** | Every evidence artifact must have a creation timestamp | Automated by source system |
| **Immutable** | Evidence cannot be modified after submission; new versions create new records | GRC platform versioning |
| **Attributable** | Evidence must identify the responsible person or system that produced it | Source system authentication |
| **Linked** | Evidence must be linked to the specific control and AI system it attests to | Mapping table in this document |
| **Complete** | Evidence must fully address the control requirement, not partially | Compliance Officer review |

---

## 6. Regulatory Reporting Automation

### 6.1 Reports Generated from GRC

| Report | Regulatory Audience | Data Sources | Frequency |
|--------|-------------------|-------------|-----------|
| **SAFEST Compliance Report** | DNB (pre-application / ongoing supervision) | All SAFEST control assessments + evidence | Per DNB request / annually |
| **EU AI Act Compliance Status** | Market surveillance authority | EU AI Act control mappings + conformity evidence | Annually / on significant change |
| **DORA Operational Resilience** | DNB / ECB | DORA control assessments + incident history + Register of Information | Annually / per DORA reporting schedule |
| **AI Risk Register** | Board / AI Governance Committee | All AI risk indicators + control effectiveness | Quarterly |
| **Audit Findings Tracker** | Internal Audit / External Auditors | All open findings, remediation status, evidence | Per audit cycle |
| **Quarterly Governance Report** | Board / CAIO | Aggregated control status + incident metrics + drift trends | Quarterly (see [quarterly governance report](../../06-executive/quarterly-governance-report.md)) |

### 6.2 Automated Report Generation

Configure GRC platforms to auto-generate reports on schedule:

1. **Data aggregation:** GRC platform queries all AI-related controls, assessments, evidence, and risk indicators
2. **Status calculation:** Compliance percentage computed per regulation, per SAFEST pillar, per AI system
3. **Trend analysis:** Compare current assessment results with previous period
4. **Exception highlighting:** Flag controls that are Not Assessed, Failed, or have expired evidence
5. **Report generation:** Produce formatted report in PDF/HTML for distribution
6. **Distribution:** Email to designated recipients per reporting schedule

---

## Cross-References

- [Jira Governance Workflows](./jira-governance-workflows.md) -- Jira configuration that feeds governance data into GRC
- [Automated Compliance Checks](./automated-compliance-checks.md) -- CI/CD automation that generates evidence for GRC ingestion
- [SAFEST Checklist Detailed](../../04-operational-governance/regulatory/safest-checklist-detailed.md) -- authoritative SAFEST item definitions mapped to GRC controls
- [SAFEST Compliance Tracker](../../04-operational-governance/regulatory/safest-compliance-tracker.yaml) -- YAML tracker that is the source for GRC control ingestion
- [SAFEST to Four Pillars Mapping](../../05-cross-cutting/safest-to-four-pillars-mapping.yaml) -- maps SAFEST items to governance pillars (useful for GRC control categorization)
- [EU AI Act Compliance Mapping](../../04-operational-governance/regulatory/eu-ai-act-compliance-mapping.md) -- article-by-article mapping used for GRC regulatory framework configuration
- [DORA AI Requirements](../../04-operational-governance/regulatory/dora-ai-requirements.md) -- DORA mapping used for GRC control set configuration
- [Quarterly Governance Report](../../06-executive/quarterly-governance-report.md) -- report template that consumes GRC aggregated data
- [Supervisory Reporting Calendar](../../07-enterprise-implementation/process-integration/supervisory-reporting-calendar.md) -- schedule that drives GRC report generation triggers
- [Tool Landscape](../../05-cross-cutting/tool-landscape.md) -- overview of all tooling including GRC platforms in the governance ecosystem

---

*Last updated: 2026-03-01* / *Version: 1.0* / *Classification: Internal / Regulatory Preparation*
