# EU AI Act Incident Reporting Procedure — Article 73

> **Purpose:** Defines the mandatory incident reporting process for ProtoLabs high-risk AI systems under the EU AI Act, ensuring timely notification to national market surveillance authorities of serious incidents.

**Version:** 1.0  
**Date:** 2026-04-24  
**Owner:** Safety Officer  
**Classification:** Confidential — Internal Distribution  
**Regulatory Basis:** EU AI Act Articles 73, 74, 75  

---

## 1. Scope

This procedure applies to all ProtoLabs AI systems classified as **high-risk** under the EU AI Act. It mandates reporting of **serious incidents** to the national market surveillance authority of the EU member state where the incident occurred.

---

## 2. Definition of Serious Incident

### 2.1 EU AI Act Definition (Article 73)

A serious incident means any incident that directly or indirectly involves a high-risk AI system and:

| Category | Examples Relevant to ProtoLabs |
|----------|-------------------------------|
| **Death of a person** | Fatal accident linked to AI-recommended manufacturing process |
| **Serious damage to health** | Injury from AI-recommended tooling parameters |
| **Serious damage to property** | Equipment damage from AI-recommended maintenance schedule |
| **Breach of fundamental rights** | Discriminatory outcome from AI system |
| **Serious and irreversible disruption of critical infrastructure** | Manufacturing line shutdown from AI system failure |

### 2.2 Manufacturing-Specific Serious Incidents

| Incident Type | Example | Reporting Required? |
|--------------|---------|---------------------|
| AI-recommended CNC parameters cause tool breakage and injury | Spindle crash due to incorrect feed/speed recommendation | ✅ Yes |
| AI material substitution recommendation leads to part failure in safety-critical application | Medical implant fails due to wrong material | ✅ Yes |
| AI predictive maintenance misses critical failure | Equipment catastrophic failure causing injury | ✅ Yes |
| AI quality control system passes defective safety-critical part | Defective aerospace component shipped | ✅ Yes |
| AI system bias leads to discriminatory supplier selection | Systematic exclusion of certain suppliers | ✅ Yes |
| AI system vulnerability exploited by adversarial attack | Unauthorized modification of AI outputs | ✅ Yes |

---

## 3. Reporting Timeline

### 3.1 Mandatory Reporting Deadlines

| Incident Severity | Reporting Deadline | To Whom |
|-------------------|-------------------|---------|
| **Serious incident with ongoing risk** | **Immediately** (no later than 15 days after awareness) | National market surveillance authority |
| **Incident requiring field safety corrective action** | **Immediately** | National market surveillance authority + affected deployers |
| **Pattern of related incidents** | **Without delay** | National market surveillance authority |

### 3.2 ProtoLabs Internal Timeline

| Phase | Deadline | Action |
|-------|----------|--------|
| **Detection** | T+0 | Incident detected or reported |
| **Triage** | T+2 hours | Initial assessment: serious incident? |
| **Escalation** | T+4 hours | Escalate to Safety Officer and CAIO if serious |
| **Investigation** | T+24 hours | Preliminary investigation, evidence preservation |
| **Authority Notification** | T+72 hours | Submit initial report to national authority |
| **Follow-up Report** | T+15 days | Submit detailed report with root cause |
| **Corrective Action** | T+30 days | Implement corrective action, report to authority |

---

## 4. Reporting Process

### Step 1: Incident Detection and Triage

| Activity | Owner | Evidence |
|----------|-------|----------|
| 1.1 Detect incident via monitoring, client report, or internal observation | All staff | Incident report form |
| 1.2 Log incident in incident tracking system | First responder | Incident log |
| 1.3 Assess if incident meets "serious incident" criteria | Safety Officer | Triage checklist |
| 1.4 Classify severity: Critical / Major / Minor | Safety Officer | Severity classification |

### Step 2: Immediate Actions (for Serious Incidents)

| Action | Owner | Timing |
|--------|-------|--------|
| 2.1 Preserve all evidence (logs, model state, inputs/outputs) | MLOps Engineer | Immediate |
| 2.2 Isolate affected system if ongoing risk | MLOps Engineer | Immediate |
| 2.3 Notify Safety Officer and CAIO | First responder | Within 2 hours |
| 2.4 Notify Legal Counsel | CAIO | Within 4 hours |
| 2.5 Assess need for immediate authority notification | Safety Officer + Legal | Within 4 hours |
| 2.6 Notify affected clients/deployers | Policy Owner | Within 24 hours |

### Step 3: Authority Notification

| Field | Description | Source |
|-------|-------------|--------|
| Provider information | ProtoLabs name, address, contact | Company registry |
| AI system identification | Name, version, registration number | EU database registration |
| Incident description | What happened, when, where | Incident investigation |
| Seriousness justification | Why this meets serious incident criteria | Triage assessment |
| Immediate measures taken | Containment, isolation, client notification | Incident response log |
| Affected parties | Clients, deployers, individuals affected | Client records |

### Step 4: Detailed Investigation and Follow-up

| Activity | Owner | Timing |
|----------|-------|--------|
| 4.1 Conduct root cause analysis | Safety Officer + Technical Owner | Within 15 days |
| 4.2 Assess scope of impact | Safety Officer | Within 15 days |
| 4.3 Determine corrective actions | Technical Owner | Within 15 days |
| 4.4 Submit detailed report to authority | Compliance Officer | Within 15 days |
| 4.5 Implement corrective actions | Technical Owner | Within 30 days |
| 4.6 Verify effectiveness of corrective actions | Internal Audit | Within 60 days |
| 4.7 Submit closure report to authority | Compliance Officer | Within 60 days |

---

## 5. Reporting Templates

### 5.1 Initial Notification Template (Within 72 hours)

```
EU AI ACT SERIOUS INCIDENT NOTIFICATION — INITIAL REPORT

Notification Date: [YYYY-MM-DD]
Reporting Entity: ProtoLabs [Entity Name]
Contact: [Name, Email, Phone]

1. AI System Information:
   - Name: [System name]
   - Version: [Version]
   - EU Database Registration: [Number]
   - Risk Classification: [Annex III / Annex I]

2. Incident Summary:
   - Date/Time of Incident: [YYYY-MM-DD HH:MM]
   - Location: [Facility / Client site / Cloud]
   - Description: [Brief description]

3. Seriousness Justification:
   [ ] Death of a person
   [ ] Serious damage to health
   [ ] Serious damage to property
   [ ] Breach of fundamental rights
   [ ] Serious disruption of critical infrastructure
   Details: [Explanation]

4. Immediate Measures Taken:
   [Description of containment actions]

5. Affected Parties:
   [List of affected clients, deployers, individuals]

6. Contact for Follow-up:
   [Name, Email, Phone]
```

### 5.2 Detailed Report Template (Within 15 days)

```
EU AI ACT SERIOUS INCIDENT NOTIFICATION — DETAILED REPORT

Reference: [Initial notification reference]
Submission Date: [YYYY-MM-DD]

1. Detailed Incident Description:
   [Full narrative of what occurred]

2. Technical Analysis:
   - System state at time of incident
   - Inputs received
   - Outputs generated
   - Anomalies detected
   [Attach technical logs]

3. Root Cause Analysis:
   - Primary cause: [Description]
   - Contributing factors: [Description]
   - Evidence: [References]

4. Impact Assessment:
   - Human impact: [Injuries, deaths, rights violations]
   - Property impact: [Damage assessment]
   - Business impact: [Client impact, service disruption]
   - Regulatory impact: [Other authorities notified]

5. Corrective Actions:
   - Immediate: [Actions already taken]
   - Short-term: [Actions planned within 30 days]
   - Long-term: [Actions planned within 90 days]

6. Preventive Measures:
   [Changes to prevent recurrence]

7. Supporting Evidence:
   [List of attached documents, logs, test results]
```

---

## 6. National Authority Contact Directory

| EU Member State | Authority | Contact | Notes |
|-----------------|-----------|---------|-------|
| Germany | BSI / BAuA | [To be updated] | Federal Office for Information Security / Federal Institute for Occupational Safety and Health |
| France | ANSSI | [To be updated] | National Cybersecurity Agency |
| Netherlands | RDI / ILT | [To be updated] | Enterprise Agency / Human Environment and Transport Inspectorate |
| Italy | ACN | [To be updated] | National Cybersecurity Agency |
| Spain | CCN-CERT | [To be updated] | National Cryptologic Center |
| [Other states] | [To be updated] | [To be updated] | |

**Note:** Specific authority designations under the EU AI Act will be confirmed by each member state. This directory will be updated as designations are published.

---

## 7. Roles and Responsibilities

| Role | Responsibility |
|------|---------------|
| **Safety Officer** | Incident triage, investigation coordination, authority liaison |
| **CAIO** | Escalation decisions, board notification, strategic response |
| **Compliance Officer** | Regulatory compliance, report submission, authority communication |
| **Legal Counsel** | Legal risk assessment, privilege protection, regulatory interpretation |
| **Technical Owner** | Technical investigation, corrective action implementation |
| **MLOps Engineer** | Evidence preservation, log extraction, system isolation |
| **Policy Owner** | Client communication, deployer notification |
| **Internal Audit** | Effectiveness verification, process improvement |

---

## 8. Relationship to Other Procedures

| Procedure | Relationship |
|-----------|-------------|
| `aims-corrective-action-template.md` | CAR process triggered by incident investigation |
| `aims-internal-audit-report-template.md` | Audit may review incident handling effectiveness |
| `eu-ai-act-conformity-assessment-procedure.md` | Incident may trigger re-assessment |
| `ce-marking-procedure.md` | Serious incident may require withdrawal of CE marking |
| `eu-database-registration-procedure.md` | Incident reported against registered system |

---

## 9. Training Requirements

| Role | Training Topic | Frequency |
|------|---------------|-----------|
| All staff | Incident recognition and initial reporting | Annual |
| Safety Officer | Serious incident assessment and investigation | Annual |
| Compliance Officer | Authority notification procedures | Annual |
| CAIO | Escalation and strategic response | Annual |
| MLOps Engineers | Evidence preservation and log extraction | Annual |

---

## 10. Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-24 | ProtoLabs AI Governance Office | Initial incident reporting procedure |

---

## See Also

- `eu-ai-act-conformity-assessment-procedure.md` — Conformity assessment
- `ce-marking-procedure.md` — CE marking
- `eu-database-registration-procedure.md` — EU database registration
- `aims-corrective-action-template.md` — Corrective action process
