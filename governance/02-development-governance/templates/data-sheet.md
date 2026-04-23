# Datasheet for Dataset: [FILL IN: Dataset Name]

> **Template version:** 1.0.0
> **Aligned to:** SAFEST S-08, EU AI Act Art 10, Gebru et al. "Datasheets for Datasets"
> **Cross-references:** `../checklists/data-quality-checklist.yaml`, `../checklists/bias-testing-checklist.yaml`

---

| Field                 | Value                                           |
|-----------------------|-------------------------------------------------|
| **Dataset name**      | [FILL IN]                                       |
| **Dataset ID**        | [FILL IN: unique identifier, e.g., DS-2026-001] |
| **Version**           | [FILL IN: e.g., 1.0.0]                          |
| **Date created**      | [FILL IN: YYYY-MM-DD]                           |
| **Last updated**      | [FILL IN: YYYY-MM-DD]                           |
| **Owner**             | [FILL IN: team or individual]                   |
| **Risk tier**         | [FILL IN: high / medium / low]                  |
| **Classification**    | [FILL IN: public / internal / confidential / restricted] |
| **Regulatory scope**  | [FILL IN: e.g., EU AI Act high-risk, GDPR Art 9 applicable] |
| **Related model(s)**  | [FILL IN: model IDs that use this dataset]      |

---

## 1. Motivation

### 1.1 Purpose

**Why was the dataset created?**

[FILL IN: Describe the specific business need or research question that motivated the creation of this dataset. Include the intended AI/ML use case (e.g., credit scoring, fraud detection, customer service automation).]

**Was there a specific task in mind?**

[FILL IN: Describe the machine learning task (classification, regression, ranking, generation, retrieval) and the target variable or output.]

**Who created the dataset and on behalf of which organization?**

[FILL IN: Name the team, department, and legal entity. If external vendors were involved, identify them.]

### 1.2 Funding & Sponsorship

**Who funded the creation of the dataset?**

[FILL IN: Internal budget, external grant, vendor contract, or open-source contribution.]

**Are there any conflicts of interest?**

[FILL IN: Document any relationships that could bias dataset construction (e.g., vendor has financial interest in a particular outcome).]

---

## 2. Composition

### 2.1 Overview

**What do the instances represent?**

[FILL IN: Describe what each row/record/document represents (e.g., a loan application, a customer interaction, a financial transaction).]

| Property                    | Value                                |
|-----------------------------|--------------------------------------|
| **Total instances**         | [FILL IN]                            |
| **Number of features**      | [FILL IN]                            |
| **Number of label columns** | [FILL IN]                            |
| **Feature types**           | [FILL IN: numeric, categorical, text, image, time-series, mixed] |
| **Time span covered**       | [FILL IN: start date to end date]    |
| **Geographic scope**        | [FILL IN: countries, regions]        |

### 2.2 Data Splits

| Split        | Size       | Percentage | Selection method               |
|--------------|------------|------------|---------------------------------|
| Training     | [FILL IN]  | [FILL IN]  | [FILL IN: random / temporal / stratified] |
| Validation   | [FILL IN]  | [FILL IN]  | [FILL IN]                       |
| Test         | [FILL IN]  | [FILL IN]  | [FILL IN]                       |
| Out-of-time  | [FILL IN]  | [FILL IN]  | [FILL IN: temporal holdout]     |

### 2.3 Feature Inventory

| Feature name   | Type        | Description           | Source system   | Contains PII | Protected attribute proxy risk |
|----------------|-------------|-----------------------|-----------------|--------------|-------------------------------|
| [FILL IN]      | [FILL IN]   | [FILL IN]             | [FILL IN]       | [Yes/No]     | [None / Low / Medium / High]  |
| [FILL IN]      | [FILL IN]   | [FILL IN]             | [FILL IN]       | [Yes/No]     | [None / Low / Medium / High]  |

> Add rows as needed. For datasets with many features, attach a complete feature inventory as a supplementary CSV and reference it here.

### 2.4 Label Description

**What is the target variable?**

[FILL IN: Name, type, and definition of the label. For classification, list all classes and their definitions.]

**How were labels assigned?**

[FILL IN: Human annotation, automated rule-based, derived from outcome data, self-reported, etc.]

**Label distribution:**

| Label value  | Count      | Percentage |
|--------------|------------|------------|
| [FILL IN]    | [FILL IN]  | [FILL IN]  |
| [FILL IN]    | [FILL IN]  | [FILL IN]  |

### 2.5 Sensitive & Protected Data

**Does the dataset contain personal data (GDPR)?**

[FILL IN: Yes / No. If yes, list categories of personal data.]

**Does the dataset contain special category data (GDPR Art 9)?**

[FILL IN: Yes / No. If yes, specify: racial/ethnic origin, political opinions, religious beliefs, trade union membership, genetic data, biometric data, health data, sex life/orientation.]

**Does the dataset include any of the following protected attributes (directly or via proxy)?**

- [ ] Age
- [ ] Gender
- [ ] Ethnicity / race
- [ ] Disability status
- [ ] Geographic location (as proxy for ethnicity or income)
- [ ] Income level
- [ ] Other: [FILL IN]

---

## 3. Collection Process

### 3.1 Data Sources

**How was the data collected?**

[FILL IN: Direct observation, surveys, web scraping, API extraction, manual entry, sensor data, third-party purchase, public records, core banking system exports, etc.]

**Source systems and their descriptions:**

| Source system      | Description                | Data type       | Extraction method |
|--------------------|----------------------------|-----------------|-------------------|
| [FILL IN]          | [FILL IN]                  | [FILL IN]       | [FILL IN]         |
| [FILL IN]          | [FILL IN]                  | [FILL IN]       | [FILL IN]         |

### 3.2 Consent & Legal Basis

**What is the legal basis for data processing (GDPR Art 6)?**

[FILL IN: Consent (Art 6(1)(a)), contract (Art 6(1)(b)), legal obligation (Art 6(1)(c)), vital interests (Art 6(1)(d)), public interest (Art 6(1)(e)), legitimate interest (Art 6(1)(f)).]

**Was informed consent obtained from data subjects?**

[FILL IN: Yes / No / Not applicable. If yes, describe the consent mechanism and what subjects were told about AI usage.]

**Has a Data Protection Impact Assessment (DPIA) been completed?**

[FILL IN: Yes / No / In progress. Reference: [Link to DPIA document]]

### 3.3 Collection Timeframe

**Over what timeframe was the data collected?**

[FILL IN: Exact date range. Note any gaps, outages, or known periods of incomplete data.]

### 3.4 Known Collection Biases

**Are there known biases in the collection process?**

[FILL IN: Survivorship bias, selection bias, reporting bias, measurement bias, etc. Describe each and its potential impact on model fairness.]

---

## 4. Preprocessing & Transformation

### 4.1 Cleaning Steps

**What preprocessing was applied?**

| Step                  | Description                                     | Rationale                | Records affected |
|-----------------------|-------------------------------------------------|--------------------------|------------------|
| [FILL IN]             | [FILL IN]                                       | [FILL IN]                | [FILL IN]        |
| [FILL IN]             | [FILL IN]                                       | [FILL IN]                | [FILL IN]        |

### 4.2 Feature Engineering

**Were new features derived?**

[FILL IN: List derived features, their computation logic, and business rationale.]

### 4.3 Missing Value Treatment

| Feature       | Missing rate | Mechanism (MCAR/MAR/MNAR) | Imputation method | Bias impact assessed |
|---------------|-------------|---------------------------|-------------------|----------------------|
| [FILL IN]     | [FILL IN]   | [FILL IN]                 | [FILL IN]         | [Yes/No]             |

### 4.4 Outlier Treatment

[FILL IN: Describe outlier detection method, thresholds, and handling decisions (cap, remove, keep).]

### 4.5 Transformation Pipeline

**Is the preprocessing pipeline versioned and reproducible?**

[FILL IN: Yes / No. Reference: [Link to pipeline code repository and version tag]]

---

## 5. Uses

### 5.1 Intended Uses

**What are the intended use cases for this dataset?**

[FILL IN: List specific AI/ML models, experiments, or analyses this dataset is designed to support.]

### 5.2 Not Recommended Uses

**Are there use cases for which this dataset should NOT be used?**

[FILL IN: Document known limitations that make the dataset unsuitable for certain applications. For example: "This dataset should not be used for real-time decision-making without additional recency checks because the data is updated monthly."]

### 5.3 Use Restrictions

**Are there regulatory or ethical restrictions on use?**

[FILL IN: GDPR purpose limitation, contractual restrictions from data providers, ethical review board conditions, etc.]

---

## 6. Distribution & Access

### 6.1 Distribution

**How is the dataset distributed internally?**

[FILL IN: Data lake path, feature store reference, API endpoint, etc.]

**Is the dataset available externally?**

[FILL IN: Yes / No. If yes, under what license or agreement.]

### 6.2 Access Controls

| Access level     | Who has access                  | Justification              |
|------------------|---------------------------------|----------------------------|
| Read             | [FILL IN]                       | [FILL IN]                  |
| Write / modify   | [FILL IN]                       | [FILL IN]                  |
| Admin            | [FILL IN]                       | [FILL IN]                  |

### 6.3 Export Controls

**Are there restrictions on exporting the data outside the EU/EEA?**

[FILL IN: Document GDPR Chapter V compliance for international transfers.]

---

## 7. Maintenance

### 7.1 Ownership & Stewardship

| Role                     | Name / Team                   | Contact              |
|--------------------------|-------------------------------|----------------------|
| Dataset owner            | [FILL IN]                     | [FILL IN]            |
| Data steward             | [FILL IN]                     | [FILL IN]            |
| Technical maintainer     | [FILL IN]                     | [FILL IN]            |

### 7.2 Update Schedule

**How often is the dataset updated?**

[FILL IN: Real-time, daily, weekly, monthly, quarterly, ad-hoc, one-time.]

**What triggers an update?**

[FILL IN: Scheduled refresh, data drift detection, model retraining cycle, regulatory requirement.]

### 7.3 Versioning

**How are dataset versions managed?**

[FILL IN: DVC, Delta Lake versioning, S3 versioned buckets, manual snapshots, etc.]

### 7.4 Deprecation & Retention

**What is the data retention period?**

[FILL IN: Per GDPR storage limitation principle and business requirements.]

**What is the deprecation process?**

[FILL IN: How will downstream consumers be notified? What is the sunset timeline?]

---

## 8. Data Provenance & Lineage

### 8.1 Lineage Diagram

[FILL IN: Attach or link to a data lineage diagram showing the end-to-end flow from source systems through transformations to the final dataset. Tools: dbt lineage, Apache Atlas, DataHub, or manual diagram.]

### 8.2 Lineage Record

| Stage                | System / Tool    | Input                 | Output                | Owner        | Timestamp   |
|----------------------|------------------|-----------------------|-----------------------|--------------|-------------|
| Extraction           | [FILL IN]        | [FILL IN]             | [FILL IN]             | [FILL IN]    | [FILL IN]   |
| Cleaning             | [FILL IN]        | [FILL IN]             | [FILL IN]             | [FILL IN]    | [FILL IN]   |
| Feature engineering  | [FILL IN]        | [FILL IN]             | [FILL IN]             | [FILL IN]    | [FILL IN]   |
| Splitting            | [FILL IN]        | [FILL IN]             | [FILL IN]             | [FILL IN]    | [FILL IN]   |
| Storage              | [FILL IN]        | [FILL IN]             | [FILL IN]             | [FILL IN]    | [FILL IN]   |

---

## 9. Checklist Completion Tracker

Before this datasheet is considered complete, confirm:

- [ ] All sections above are filled in (no remaining `[FILL IN]` placeholders)
- [ ] Data quality checklist (`data-quality-checklist.yaml`) passed
- [ ] Bias testing checklist (`bias-testing-checklist.yaml`) initiated
- [ ] DPIA completed and approved
- [ ] Data lineage diagram attached
- [ ] Dataset registered in the data catalog
- [ ] Access controls configured and verified
- [ ] Version tag applied to the dataset

---

## 10. Approval

| Role                     | Name       | Date       | Signature / Approval ID |
|--------------------------|------------|------------|--------------------------|
| Dataset Owner            | [FILL IN]  | [FILL IN]  | [FILL IN]                |
| Data Protection Officer  | [FILL IN]  | [FILL IN]  | [FILL IN]                |
| AI Governance Lead       | [FILL IN]  | [FILL IN]  | [FILL IN]                |

---

*This template is part of the AI Governance Framework. For questions, contact the AI Governance Team.*
