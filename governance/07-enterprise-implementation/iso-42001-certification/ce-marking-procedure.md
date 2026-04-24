# CE Marking Procedure for High-Risk AI Systems — EU AI Act Article 48

> **Purpose:** Defines the process for affixing CE marking to ProtoLabs high-risk AI systems under the EU AI Act, ensuring lawful placement on the EU market.

**Version:** 1.0  
**Date:** 2026-04-24  
**Owner:** Compliance Officer  
**Classification:** Confidential — Internal Distribution  
**Regulatory Basis:** EU AI Act Articles 48, 49, 50  

---

## 1. Scope

This procedure applies to all ProtoLabs AI systems that:
- Are classified as **high-risk** under EU AI Act Articles 6, Annex III, or Annex I
- Are placed on the EU market or put into service in the EU
- Require CE marking as evidence of conformity with the EU AI Act

---

## 2. CE Marking Requirements

### 2.1 When CE Marking is Required

| Scenario | CE Marking Required? | Route |
|----------|---------------------|-------|
| High-risk AI system (Annex III) placed on EU market | ✅ Yes | Internal Production Control (Art. 43.1) |
| High-risk AI system (Annex I) — safety component in machinery | ✅ Yes | EU-Type Examination (Art. 43.2) |
| High-risk AI system (Annex I) — safety component in medical device | ✅ Yes | EU-Type Examination (Art. 43.2) |
| High-risk AI system (Annex I) — safety component in vehicle | ✅ Yes | EU-Type Examination (Art. 43.2) |
| Limited-risk AI system (Art. 52) | ❌ No | Transparency obligations only |
| Minimal-risk AI system | ❌ No | Voluntary codes of conduct |

### 2.2 CE Marking Specifications

| Attribute | Requirement |
|-----------|-------------|
| **Form** | CE marking consists of the initials "CE" |
| **Proportions** | If reduced or enlarged, proportions must be respected |
| **Visibility** | Must be visible, legible, and indelible |
| **Location** | Affixed to AI system or its accompanying documentation |
| **Accompanying Information** | Must include identification number of Notified Body (if involved) |

---

## 3. CE Marking Process

### Step 1: Verify Conformity Assessment Complete

| Check | Verification | Evidence |
|-------|------------|----------|
| 1.1 | Conformity assessment conducted per `eu-ai-act-conformity-assessment-procedure.md` | Conformity assessment report |
| 1.2 | EU Declaration of Conformity signed | Signed DoC |
| 1.3 | All essential requirements (Annex IV) satisfied | Essential requirements checklist |
| 1.4 | Technical documentation complete | Technical documentation index |

### Step 2: Prepare CE Marking

| Activity | Description | Owner |
|----------|-------------|-------|
| 2.1 | Generate CE marking graphic | Compliance Officer |
| 2.2 | Include Notified Body identification number (if applicable) | Compliance Officer |
| 2.3 | Prepare accompanying EU Declaration of Conformity | Compliance Officer |

### Step 3: Affix CE Marking

| System Type | Affixing Method | Location |
|-------------|----------------|----------|
| Software-only AI system | Digital CE mark in software interface + documentation | About page, documentation header |
| AI system embedded in hardware | Physical CE mark on hardware + digital in software | Hardware label, software about page |
| Cloud-based AI service | CE mark on service documentation and terms of use | Documentation, ToU |
| API-accessible AI | CE mark in API documentation and developer portal | API docs, portal |

### Step 4: Maintain Records

| Record | Retention Period | Location |
|--------|-----------------|----------|
| CE marking application log | 10 years post-market | `aims-document-retention-schedule.md` |
| EU Declaration of Conformity | 10 years post-market | Document repository |
| Technical documentation | 10 years post-market | Document repository |
| Conformity assessment records | 10 years post-market | Document repository |

---

## 4. Post-Market CE Marking Obligations

### 4.1 Monitoring

| Activity | Frequency | Owner |
|----------|-----------|-------|
| Verify CE marking remains valid | Continuous | Compliance Officer |
| Monitor for changes affecting conformity | Continuous | Model Owner |
| Review post-market surveillance data | Quarterly | Safety Officer |

### 4.2 Modifications Requiring Re-assessment

| Change Type | Action Required |
|-------------|-----------------|
| Change to AI model architecture | New conformity assessment |
| Change to training data methodology | New conformity assessment |
| Change to intended use | Re-classification + new conformity assessment |
| Change to risk classification | New conformity assessment |
| Minor bug fix (no functional change) | Document in change log |
| Security patch | Document in change log, verify no impact on conformity |

### 4.3 Withdrawal or Recall

| Scenario | Action |
|----------|--------|
| System no longer compliant | Remove CE marking, withdraw from market |
| Serious incident | Initiate recall, notify authorities per `eu-ai-act-incident-reporting-procedure.md` |
| End of support | Document end-of-life, maintain records for 10 years |

---

## 5. Prohibited Use of CE Marking

CE marking must NOT be affixed when:
- Conformity assessment is incomplete
- Essential requirements are not fully satisfied
- EU Declaration of Conformity is not signed
- System is not classified as high-risk
- System is placed on market before conformity assessment completion

**Penalty for improper CE marking:** Up to €15 million or 3% of global annual turnover (Article 99).

---

## 6. Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-24 | ProtoLabs AI Governance Office | Initial CE marking procedure |

---

## See Also

- `eu-ai-act-conformity-assessment-procedure.md` — Conformity assessment
- `eu-database-registration-procedure.md` — EU database registration
- `eu-ai-act-incident-reporting-procedure.md` — Incident reporting
