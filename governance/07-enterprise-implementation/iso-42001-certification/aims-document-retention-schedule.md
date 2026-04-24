# AIMS Document Retention Schedule — ISO/IEC 42001 Clause 7.5

> **Purpose:** Defines retention periods for all AIMS documented information, ensuring ISO/IEC 42001 Clause 7.5 compliance and audit readiness.

**Version:** 1.0  
**Last Updated:** 2026-04-24  
**Owner:** Compliance Officer  
**Review Cycle:** Annual  

---

## Retention Principles

1. **Regulatory Minimum** — Retention meets or exceeds all applicable regulatory requirements (EU AI Act, GDPR, ITAR, FDA)
2. **Audit Evidence** — All certification audit evidence retained for the certification cycle plus one surveillance period
3. **Legal Hold** — Litigation or investigation may override standard retention; legal hold procedures apply
4. **Secure Disposal** — Documents past retention are securely deleted with evidence of destruction

---

## Retention Schedule by Document Category

### Governance and Policy Documents

| Document Type | Retention Period | Legal Basis | Storage | Disposal Method |
|--------------|------------------|-------------|---------|-----------------|
| AI governance charter | 7 years | ISO 42001, corporate governance | Document control system | Secure deletion |
| Board resolutions | Permanent | Corporate law | Board portal | Archive only |
| AI policy and procedures | 7 years + 1 certification cycle | ISO 42001 Clause 7.5 | Document control system | Secure deletion |
| Policy ownership registry | 7 years | ISO 42001 Clause 5.2 | Governance portal | Secure deletion |
| Risk appetite framework | 7 years | ISO 42001 Clause 6.1 | Governance portal | Secure deletion |

### Risk Management Documents

| Document Type | Retention Period | Legal Basis | Storage | Disposal Method |
|--------------|------------------|-------------|---------|-----------------|
| Risk management plan | 7 years | ISO 42001 Clause 6.1, EU AI Act Art 9 | Governance portal | Secure deletion |
| Risk registers | 7 years | ISO 42001 Clause 6.1 | Governance portal | Secure deletion |
| Risk assessments (per agent) | Life of agent + 7 years | ISO 42001 Clause 8.2 | Agent registry | Secure deletion |
| Risk treatment plans | 7 years | ISO 42001 Clause 8.3 | Governance portal | Secure deletion |
| Impact assessments (DPIA) | Life of system + 7 years | GDPR | Secure archive | Secure deletion |

### AI System Lifecycle Documents

| Document Type | Retention Period | Legal Basis | Storage | Disposal Method |
|--------------|------------------|-------------|---------|-----------------|
| Model cards | Life of model + 7 years | ISO 42001 Clause 7.5, EU AI Act Art 11 | Model registry | Secure deletion |
| Data sheets | Life of model + 7 years | ISO 42001 Clause 7.5 | Model registry | Secure deletion |
| Test plans and results | Life of model + 7 years | ISO 42001 Clause 8.4, EU AI Act Art 15 | Eval repository | Secure deletion |
| Evaluation reports | Life of model + 7 years | ISO 42001 Clause 9.1 | Eval repository | Secure deletion |
| Pre-deployment gate records | Life of model + 7 years | ISO 42001 Clause 8.4 | Governance portal | Secure deletion |
| Deployment logs | Life of model + 7 years | ISO 42001 Clause 8.1 | MLOps system | Secure deletion |
| Change management records | 7 years | ISO 42001 Clause 8.1 | Change management system | Secure deletion |
| Model retirement records | 10 years | ISO 42001 Clause 8.4 | Archive | Secure deletion |

### Safety and Security Documents

| Document Type | Retention Period | Legal Basis | Storage | Disposal Method |
|--------------|------------------|-------------|---------|-----------------|
| Safety validation reports | 10 years | ISO 10218, ISO 42001 Clause 8.3 | Safety management system | Secure deletion |
| Kill switch test records | 10 years | ISO 42001 Clause 8.3 | Safety management system | Secure deletion |
| Safety Agent audit logs | 7 years | ISO 42001 Clause 9.1 | SIEM | Secure deletion |
| Hard guardrail configuration | Life of guardrail + 7 years | ISO 42001 Clause 8.2 | Governance portal | Secure deletion |
| Security incident reports | 7 years | NIST CSF, GDPR | Incident management system | Secure deletion |
| Red team reports | 7 years | ISO 42001 Clause 9.2 | Security archive | Secure deletion |
| Vulnerability assessments | 7 years | ISO 42001 Clause 6.1 | Security archive | Secure deletion |
| Penetration test reports | 7 years | ISO 42001 Clause 9.2 | Security archive | Secure deletion |

### Audit and Compliance Documents

| Document Type | Retention Period | Legal Basis | Storage | Disposal Method |
|--------------|------------------|-------------|---------|-----------------|
| Internal audit plans | 7 years | ISO 42001 Clause 9.2 | Audit management system | Secure deletion |
| Internal audit checklists | 7 years | ISO 42001 Clause 9.2 | Audit management system | Secure deletion |
| Internal audit reports | 7 years | ISO 42001 Clause 9.2 | Audit management system | Secure deletion |
| Certification audit records | 10 years | ISO 42001, certification body requirements | Certification archive | Secure deletion |
| Management review minutes | 7 years | ISO 42001 Clause 9.3 | Governance portal | Secure deletion |
| Corrective action records | 7 years | ISO 42001 Clause 10.1 | Quality management system | Secure deletion |
| Nonconformity records | 7 years | ISO 42001 Clause 10.1 | Quality management system | Secure deletion |
| Compliance reports (regulatory) | 10 years | Regulatory requirements | Regulatory archive | Secure deletion |

### Operational Documents

| Document Type | Retention Period | Legal Basis | Storage | Disposal Method |
|--------------|------------------|-------------|---------|-----------------|
| Agent audit logs | 7 years | ISO 42001 Clause 9.1, EU AI Act Art 12 | SIEM / log store | Secure deletion |
| Decision logs (all agents) | 7 years | ISO 42001 Clause 9.1 | Audit database | Secure deletion |
| Monitoring dashboards | 3 years (snapshots) | ISO 42001 Clause 9.1 | Monitoring system | Automatic purge |
| Drift detection records | 7 years | ISO 42001 Clause 9.1 | MLOps system | Secure deletion |
| Incident response records | 7 years | ISO 42001 Clause 10.1 | Incident management system | Secure deletion |
| Training records | Life of employment + 7 years | ISO 42001 Clause 7.2 | LMS / HR system | Secure deletion |
| Competence assessments | Life of employment + 7 years | ISO 42001 Clause 7.2 | HR system | Secure deletion |

### Client and Commercial Documents

| Document Type | Retention Period | Legal Basis | Storage | Disposal Method |
|--------------|------------------|-------------|---------|-----------------|
| Client contracts | Life of contract + 7 years | Contract law | Contract management system | Secure deletion |
| Client communications (AI disclosure) | 7 years | ISO 42001 Clause 7.4 | CRM | Secure deletion |
| Client incident notifications | 7 years | GDPR, contract | CRM | Secure deletion |
| Quote records | 7 years | Tax, contract | ERP | Secure deletion |
| Production records | 7 years | ISO 9001, AS9100D | MES | Secure deletion |
| Quality records | 7-10 years (industry dependent) | ISO 9001, AS9100D, ISO 13485 | QMS | Secure deletion |
| CAD files (client) | Per client contract (minimum 7 years) | Contract, IP protection | Secure storage | Secure deletion |

---

## Special Retention Requirements

### Regulated Industries

| Industry | Additional Requirements | Retention Extension |
|----------|------------------------|---------------------|
| **Aerospace (AS9100D)** | Configuration management, traceability | 10 years minimum |
| **Medical Device (ISO 13485)** | Design history file, risk management file | Life of device + 2 years |
| **Automotive (IATF 16949)** | PPAP records, control plans | 15 years minimum |
| **ITAR/EAR Controlled** | Export control records, deemed export logs | 5 years from last activity |
| **EU AI Act High-Risk** | Risk management system, post-market monitoring | 10 years |

### Litigation Hold

When litigation or regulatory investigation is anticipated or commenced:

1. **Legal Hold Notice** issued by General Counsel
2. **Suspension of Disposal** for all potentially relevant documents
3. **Identification** of custodians and relevant document categories
4. **Preservation** in place until legal hold released
5. **Documentation** of hold and release in legal hold log

---

## Disposal Procedures

### Secure Deletion Standards

| Data Classification | Disposal Method | Verification |
|--------------------|-----------------|--------------|
| Public | Standard deletion | None |
| Internal | Secure erase (DoD 5220.22-M) | Log entry |
| Confidential | Cryptographic erasure + physical destruction (if applicable) | Certificate of destruction |
| Restricted (ITAR, medical) | Physical destruction of media + chain of custody | Certificate of destruction, witness signature |

### Disposal Log

| Date | Document Type | Retention Period Met | Disposal Method | Performed By | Verified By |
|------|--------------|---------------------|-----------------|--------------|-------------|
| [Example] | Model card (retired agent) | Yes (7 years) | Cryptographic erasure | MLOps Lead | Compliance Officer |

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-24 | ProtoLabs AI Governance Office | Initial retention schedule |

---

## See Also

- `governance/07-enterprise-implementation/iso-42001-certification/aims-communication-plan.md` — Communication plan
- `governance/04-operational-governance/templates/ai-incident-report.md` — Incident reporting
- `docs/iso-42001-gap-analysis.md` — Gap analysis (Clause 7.5)
