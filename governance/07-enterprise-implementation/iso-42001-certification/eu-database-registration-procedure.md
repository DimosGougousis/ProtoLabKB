# EU Database Registration Procedure — EU AI Act Article 71

> **Purpose:** Defines the process for registering ProtoLabs high-risk AI systems in the EU database established under Article 71 of the EU AI Act.

**Version:** 1.0  
**Date:** 2026-04-24  
**Owner:** Compliance Officer  
**Classification:** Confidential — Internal Distribution  
**Regulatory Basis:** EU AI Act Articles 71, 72, 73  

---

## 1. Scope

This procedure applies to all ProtoLabs AI systems classified as **high-risk** under the EU AI Act that must be registered in the EU database before placement on the EU market or putting into service.

---

## 2. Registration Obligations

### 2.1 Who Must Register

| Entity Type | Registration Required? | Timing |
|-------------|----------------------|--------|
| Provider of high-risk AI system (Annex III) | ✅ Yes | Before placing on market |
| Provider of high-risk AI system (Annex I) | ✅ Yes | Before placing on market |
| Deployer of high-risk AI system (public sector) | ✅ Yes | Before putting into service |
| Deployer (private sector, non-critical) | ❌ No | — |

### 2.2 ProtoLabs Registration Scenarios

| Scenario | Registration Required? | Role |
|----------|----------------------|------|
| ProtoLabs provides DFM evaluation AI to EU clients | ✅ Yes | Provider |
| ProtoLabs deploys AI in own EU manufacturing facility | ✅ Yes | Provider + Deployer |
| ProtoLabs AI embedded in client machinery (Annex I) | ✅ Yes | Provider |

---

## 3. Registration Process

### Step 1: Prepare Registration Information

| Data Field | Description | Source |
|------------|-------------|--------|
| Provider name and contact details | ProtoLabs entity information | Company registry |
| AI system name and version | System identifier | `model-card.md` |
| Risk classification | Annex III or Annex I category | `eu-ai-act-risk-classification.yaml` |
| Intended purpose | Description of system use | `model-card.md` |
| Basic functionality | What the system does | Technical documentation |
| Geographical coverage | EU member states where deployed | Deployment records |
| CE marking information | CE mark details | `ce-marking-procedure.md` |
| Conformity assessment details | Route, Notified Body (if applicable) | Conformity assessment report |
| URL of EU Declaration of Conformity | Link to signed DoC | Document repository |

### Step 2: Access EU Database

| Activity | Details |
|----------|---------|
| **Portal** | EU AI Act database (operated by European Commission) |
| **Access** | Secure authentication (eIDAS-compliant) |
| **Language** | English (accepted for all member states) |
| **Cost** | No registration fee |

### Step 3: Submit Registration

| Step | Action | Owner |
|------|--------|-------|
| 3.1 | Log in to EU database portal | Compliance Officer |
| 3.2 | Select "Register new high-risk AI system" | Compliance Officer |
| 3.3 | Enter provider information | Compliance Officer |
| 3.4 | Enter AI system information | Compliance Officer |
| 3.5 | Upload supporting documents (DoC, technical summary) | Compliance Officer |
| 3.6 | Review and confirm accuracy | Compliance Officer |
| 3.7 | Submit registration | Compliance Officer |
| 3.8 | Record registration number | Compliance Officer |

### Step 4: Post-Registration

| Activity | Timing | Owner |
|----------|--------|-------|
| Record registration number in system inventory | Within 1 business day | Compliance Officer |
| Update `unified-cross-framework-register.md` | Within 1 business day | Compliance Officer |
| Notify relevant stakeholders | Within 1 business day | Compliance Officer |
| Monitor for database updates or queries | Ongoing | Compliance Officer |

---

## 4. Registration Update Requirements

### 4.1 When Updates Are Required

| Change Type | Update Required? | Timing |
|-------------|-----------------|--------|
| Change to provider information | ✅ Yes | Within 1 month |
| Change to AI system name or version | ✅ Yes | Before placing updated system on market |
| Change to intended purpose | ✅ Yes | Before deployment |
| Change to risk classification | ✅ Yes | Immediately |
| Change to conformity assessment | ✅ Yes | Within 1 month |
| Change to geographical coverage | ✅ Yes | Before deployment in new member state |
| System withdrawn from market | ✅ Yes | Immediately |

### 4.2 Update Process

| Step | Action | Owner |
|------|--------|-------|
| 1 | Identify change triggering update requirement | Model Owner |
| 2 | Assess impact on registration | Compliance Officer |
| 3 | Prepare updated information | Compliance Officer |
| 4 | Submit update via EU database portal | Compliance Officer |
| 5 | Record update confirmation | Compliance Officer |
| 6 | Update internal records | Compliance Officer |

---

## 5. Registration Record Keeping

| Record | Retention Period | Location |
|--------|-----------------|----------|
| Registration confirmation | 10 years post-market | Document repository |
| Registration number | 10 years post-market | System inventory |
| All submitted information | 10 years post-market | Document repository |
| Update history | 10 years post-market | Document repository |

---

## 6. Roles and Responsibilities

| Role | Responsibility |
|------|---------------|
| **Compliance Officer** | Coordinates registration, maintains records, ensures timely updates |
| **CAIO** | Accountable for registration compliance |
| **Model Owner** | Provides accurate system information, notifies of changes |
| **Legal Counsel** | Advises on regulatory interpretation |

---

## 7. Timeline

| Milestone | Target Date |
|-----------|-------------|
| EU database operational | Expected mid-2026 |
| First ProtoLabs registration | Within 2 weeks of database launch |
| All high-risk systems registered | Within 4 weeks of database launch |
| Registration updates | Within timelines specified in Section 4 |

---

## 8. Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-24 | ProtoLabs AI Governance Office | Initial registration procedure |

---

## See Also

- `eu-ai-act-conformity-assessment-procedure.md` — Conformity assessment
- `ce-marking-procedure.md` — CE marking
- `eu-ai-act-incident-reporting-procedure.md` — Incident reporting
