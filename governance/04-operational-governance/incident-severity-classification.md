# AI Incident Severity Classification

> **Document Type:** Operational Governance — Incident Management
> **Version:** 1.0
> **Effective Date:** 2026-04-28
> **Owner:** Chief AI Officer (CAIO)
> **Approved By:** AI Governance Council
> **Review Cycle:** Semi-annual, or after any Sev1 incident
> **Next Review:** 2026-10-28

---

## Purpose

This document defines how ProtoLabs classifies AI incidents by severity, what response each severity demands, and who must be involved. It replaces ad-hoc escalation with a deterministic classification system so that every incident is handled with proportionate urgency.

## When to Use

- When an AI system produces unexpected, incorrect, or harmful output
- When an AI system experiences performance degradation, drift, or availability issues
- When a security breach, data leak, or adversarial attack targets an AI system
- When a customer reports a problem with AI-generated output
- When a regulatory body inquires about an AI system's behavior

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **First Responder** (Technical Owner / On-Call Engineer) | Classifies initial severity; executes immediate containment |
| **Safety Officer** | Validates safety-related severity classifications; leads Sev1 response |
| **CAIO** | Owns Sev1 escalation to Board; approves severity reclassifications |
| **Governance Council** | Reviews Sev2 incidents; approves post-incident corrective actions |
| **Head of Internal Audit** | Ensures post-incident evidence quality; validates root cause analysis |

## Regulatory Basis

- **EU AI Act Article 72** — Post-market monitoring and serious incident reporting
- **EU AI Act Article 26(5)** — Obligation to report serious incidents to market surveillance authorities
- **ISO/IEC 42001 Clause 10.1** — Nonconformity and corrective action
- **NIST AI RMF MG-2.1** — Incident response playbook defined
- **NIST AI RMF MG-3.1** — Regular review and update of risk management approach

---

## 1. Severity Definitions

### Severity Matrix

| Severity | Name | Definition | Examples |
|----------|------|-----------|----------|
| **Sev1** | Critical | Actual harm to persons, data breach, regulatory violation, or safety-critical failure | Incorrect structural DFM that reaches shop floor without PE review; customer CAD data exfiltration; ITAR-controlled data exposed; AI system used in EU AI Act prohibited manner |
| **Sev2** | High | Significant accuracy degradation, customer-facing incorrect output, or control failure without realized harm | DFM accuracy drops >10% from baseline; quote agent generates materially incorrect pricing; kill switch fails to activate when triggered; citation hallucination rate exceeds 5% |
| **Sev3** | Medium | Non-critical accuracy drift, minor control gaps, or operational issues | Model drift detected but within tolerance; logging gaps in audit trail; non-critical eval suite failures; KB article staleness beyond SLA |
| **Sev4** | Low | Cosmetic issues, minor logging gaps, or non-impactful anomalies | UI display errors in agent output formatting; non-critical monitoring alert noise; documentation gaps |

### Classification Decision Tree

```
Was there actual harm to a person?
  YES → Sev1
  NO  ↓

Was customer data (CAD, PII, IP) exposed or exfiltrated?
  YES → Sev1
  NO  ↓

Did the incident involve ITAR/EAR-controlled data?
  YES → Sev1
  NO  ↓

Did the incident constitute a regulatory violation (EU AI Act, GDPR)?
  YES → Sev1
  NO  ↓

Did the AI system produce output that affected a binding business commitment
(price, lead time, quality guarantee) without required human approval?
  YES → Sev1 (if commitment was delivered) / Sev2 (if caught before delivery)
  NO  ↓

Is accuracy degradation >10% from baseline?
  YES → Sev2
  NO  ↓

Did a kill switch or safety control fail to activate when triggered?
  YES → Sev2
  NO  ↓

Is citation hallucination rate >5%?
  YES → Sev2
  NO  ↓

Is there measurable model drift beyond tolerance thresholds?
  YES → Sev3
  NO  ↓

Are there audit trail gaps or logging failures?
  YES → Sev3
  NO  ↓

Is the issue cosmetic or non-impactful?
  YES → Sev4
```

---

## 2. Response Requirements by Severity

### 2.1 Response SLAs

| Severity | Initial Response | Containment | Root Cause Analysis | Corrective Action | Post-Incident Review |
|----------|-----------------|-------------|--------------------|--------------------|---------------------|
| **Sev1** | 15 minutes | 1 hour | 48 hours | 5 business days | Mandatory (within 10 business days) |
| **Sev2** | 2 hours | 4 hours | 5 business days | 10 business days | Mandatory (within 15 business days) |
| **Sev3** | 24 hours | 48 hours | 10 business days | 30 business days | Optional (at CAIO discretion) |
| **Sev4** | 1 week | N/A | N/A | Next sprint | Not required |

### 2.2 Escalation Path

| Severity | Immediate Notification | Escalation (if not contained) | Board Notification |
|----------|----------------------|------------------------------|-------------------|
| **Sev1** | CAIO + Safety Officer + Security Lead | Board (within 1 hour) | Mandatory (within 2 hours) |
| **Sev2** | Technical Owner + Policy Owner + Safety Officer | Governance Council (within 4 hours) | Quarterly report |
| **Sev3** | Technical Owner | Policy Owner (within 48 hours) | Not required |
| **Sev4** | Technical Owner | N/A | Not required |

### 2.3 Containment Actions

| Severity | Containment Options |
|----------|-------------------|
| **Sev1** | Immediate kill switch activation; agent quarantine; customer notification; regulatory notification (if required by EU AI Act Article 26(5)) |
| **Sev2** | Agent degradation to safe mode (e.g., disable API calls, revert to advisory-only); affected customer notification; enhanced monitoring |
| **Sev3** | Monitoring alert escalation; affected component rollback; increased eval frequency |
| **Sev4** | Log and track; fix in next sprint |

---

## 3. Incident Lifecycle

```
  ┌─────────────────────────────────────────────────────────────────┐
  │                    AI INCIDENT LIFECYCLE                         │
  └─────────────────────────────────────────────────────────────────┘

  DETECT → CLASSIFY → CONTAIN → INVESTIGATE → REMEDIATE → REVIEW → CLOSE
    │          │          │           │             │          │        │
    │          │          │           │             │          │        │
    v          v          v           v             v          v        v
  Alert    Decision   Stop the    Root cause    Fix +      Post-    Archive
  fires    tree       bleeding    analysis      verify     mortem   evidence
           (Sec 1)    (Sec 2.3)   (Sec 4)       (Sec 5)    (Sec 6)
```

### 3.1 DETECT — How Incidents Are Found

| Detection Method | Description | Typical Severity |
|-----------------|-------------|-----------------|
| Automated monitoring alert | Drift detection, accuracy threshold, anomaly detection | Sev2-Sev3 |
| Customer report | Client contacts ProtoLabs about incorrect AI output | Sev1-Sev3 |
| Internal discovery | Engineer or QA identifies issue during review | Sev2-Sev4 |
| Security alert | Adversarial attack detection, data breach alert | Sev1 |
| Regulatory inquiry | Authority requests information about AI behavior | Sev1-Sev2 |
| Audit finding | Internal or external audit identifies control gap | Sev2-Sev3 |

### 3.2 CLASSIFY — Applying the Decision Tree

1. First responder applies the decision tree (Section 1).
2. If classification is ambiguous, **default to the higher severity**.
3. Severity may be **reclassified** as more information becomes available:
   - **Upgrade** (Sev3 → Sev2): Any Council member or the CAIO may upgrade.
   - **Downgrade** (Sev2 → Sev3): Requires CAIO approval and documented justification.

### 3.3 CONTAIN — Stopping the Bleeding

Containment is about **preventing further harm**, not fixing the root cause.

| Action | When to Use | Who Executes |
|--------|------------|-------------|
| **Kill switch activation** | Sev1: any safety or data breach scenario | Safety Officer or Technical Owner |
| **Agent quarantine** | Sev1-Sev2: isolate agent from all integrations | Technical Owner |
| **Safe mode degradation** | Sev2: disable autonomous actions, revert to advisory | Technical Owner |
| **Rollback to previous version** | Sev2-Sev3: revert model or prompt to last known good | Technical Owner |
| **Enhanced monitoring** | Sev3: increase eval frequency, add alert thresholds | Technical Owner |
| **Customer notification** | Sev1: mandatory; Sev2: if customer was affected | Policy Owner + Legal Counsel |

### 3.4 INVESTIGATE — Root Cause Analysis

| Severity | RCA Method | Required Artifacts |
|----------|-----------|-------------------|
| **Sev1** | 8D or equivalent structured RCA | 8D report; timeline; evidence chain; contributing factors |
| **Sev2** | 5-Why or fishbone diagram | RCA document; timeline; evidence |
| **Sev3** | Lightweight investigation | Investigation notes; root cause statement |
| **Sev4** | N/A | N/A |

RCA template: [AI Incident Report Template](templates/ai-incident-report.md)

### 3.5 REMEDIATE — Fix and Verify

1. Implement corrective action addressing root cause.
2. Verify fix through eval suite re-run (must pass).
3. Verify containment can be safely lifted.
4. Document corrective action in incident record.

### 3.6 REVIEW — Post-Incident Review

| Severity | Review Required? | Review Participants | Output |
|----------|-----------------|-------------------|--------|
| **Sev1** | Mandatory | CAIO, Safety Officer, Technical Owner, Policy Owner, Head of Internal Audit | Post-incident report with systemic improvements |
| **Sev2** | Mandatory | Governance Council | Post-incident report with corrective actions |
| **Sev3** | At CAIO discretion | Technical Owner + Policy Owner | Lessons learned (if review conducted) |
| **Sev4** | No | N/A | N/A |

Post-incident review must answer:
1. What happened? (Timeline)
2. Why did it happen? (Root cause)
3. How did we respond? (Containment effectiveness)
4. What do we change? (Corrective actions)
5. How do we prevent recurrence? (Systemic improvements)
6. Does this affect our risk tier classification? (Re-classification assessment)
7. Does this require policy or charter updates? (Governance feedback loop)

### 3.7 CLOSE — Archive and Track

- Incident record closed only after all corrective actions are verified effective.
- Records retained for **7 years** per document retention schedule.
- Sev1 incidents included in next Quarterly Governance Report.
- Incident trends analyzed quarterly for systemic patterns.

---

## 4. Regulatory Reporting Obligations

| Trigger | Regulation | Reporting Requirement | Deadline | Owner |
|---------|-----------|----------------------|----------|-------|
| Serious incident involving high-risk AI | EU AI Act Art. 26(5) | Report to national market surveillance authority | Without delay (and in any event within 15 days) | CAIO + Legal Counsel |
| Personal data breach | GDPR Art. 33 | Report to supervisory authority | Within 72 hours | DPO |
| Personal data breach (high risk) | GDPR Art. 34 | Notify affected data subjects | Without undue delay | DPO |
| ITAR/EAR violation | ITAR §127.12 / EAR §764.5 | Report to DDTC / BIS | Immediately | Legal Counsel + Security Lead |
| Safety-critical manufacturing failure | Product liability (national law) | Preserve evidence; notify insurer | Immediately | Legal Counsel |

---

## 5. Incident Record Template

Every incident must produce a record:

```yaml
incident_record:
  incident_id: "INC-2026-001"
  severity: "Sev2"
  agent_id: "quote-generator-v1"
  detected_at: "2026-05-06T14:30:00Z"
  detected_by: "automated-monitoring"
  classification_method: "decision-tree"
  description: "Quote agent generated pricing 25% below baseline for aluminum CNC part"
  containment_actions:
    - action: "safe-mode-degradation"
      executed_at: "2026-05-06T14:45:00Z"
      executed_by: "Technical Owner"
  root_cause: "Pricing model trained on outdated material cost data"
  corrective_actions:
    - action: "retrain-pricing-model"
      owner: "Technical Owner"
      deadline: "2026-05-16"
      status: "in-progress"
  systemic_improvements:
    - action: "add-material-cost-freshness-check-to-eval-suite"
      owner: "Technical Owner"
      deadline: "2026-05-20"
  re_approval_required: true
  re_approval_owner: "Governance Council"
  closed_at: null
```

Incident records are stored in `governance/04-operational-governance/incident-records/`.

---

## 6. Metrics and Reporting

### 6.1 Incident KPIs (reported in Quarterly Governance Report)

| KPI | Target | Measurement |
|-----|--------|-------------|
| Sev1 incidents per quarter | 0 | Count |
| Mean time to contain (Sev1) | <1 hour | Time from detection to containment |
| Mean time to contain (Sev2) | <4 hours | Time from detection to containment |
| Incidents without RCA within SLA | 0 | Count |
| Repeat incidents (same root cause) | 0 | Count |
| Regulatory reporting SLA compliance | 100% | Count of on-time reports / total reports |

### 6.2 Trend Analysis

The CAIO reviews incident trends quarterly to identify:
- **Systemic patterns** — Are incidents clustering around a specific agent, vendor, or failure mode?
- **Control effectiveness** — Are containment actions working? Are kill switches activating reliably?
- **Risk tier accuracy** — Do incidents suggest an agent should be reclassified to a higher tier?
- **Governance gaps** — Do incidents reveal missing controls or policy gaps?

---

## Cross-References

| Document | Relationship |
|----------|-------------|
| [AI Governance Policy](../ai-governance-policy.md) | Parent policy; this document implements Section 6 |
| [AI Governance Council Charter](../05-cross-cutting/ai-governance-council-charter.md) | Council reviews Sev1/Sev2 incidents |
| [Approval Thresholds by Tier](../05-cross-cutting/approval-thresholds-by-tier.md) | Incidents may trigger re-approval |
| [AI Incident Report Template](templates/ai-incident-report.md) | Template for incident documentation |
| [Incident Response Checklist](checklists/incident-response-checklist.yaml) | Step-by-step response checklist |
| [Drift Detection Runbook](guides/drift-detection-runbook.md) | Drift-related incident detection |
| [Customer-Facing Agent Safety](../03-runtime-governance/agentic-workflows/customer-facing-agent-safety.md) | Kill switch and safety architecture |
| [AI Risk Appetite Framework](../06-executive/ai-risk-appetite-framework.md) | Risk tolerance thresholds that trigger incidents |
| [Quarterly Governance Report](../06-executive/quarterly-governance-report.md) | Incident trends reported quarterly |

---

*This document is version-controlled and auditable. Unauthorized modifications void governance compliance claims.*
