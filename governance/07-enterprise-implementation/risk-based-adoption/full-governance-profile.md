# Full Governance Profile (High-Risk AI Systems)

## Purpose

Define the complete governance profile for high-risk AI systems in regulated FinTech: credit scoring models, AML transaction monitoring, fraud detection engines, and any AI system that directly makes or materially influences decisions about customers' access to financial services. This document specifies every mandatory artifact, review, approval, and reporting obligation across the full AI lifecycle. Where [Minimum Viable Governance](minimum-viable-governance.md) defines the floor, this document defines the ceiling.

## When to Use

- When deploying any AI system classified as high-risk under the [Risk Tiering Model](risk-tiering-model.md)
- When an existing AI system is reclassified from limited to high-risk due to scope expansion
- When preparing for DNB on-site examinations of high-risk AI systems
- When setting up governance for credit scoring, AML screening, fraud detection, or automated lending decisions
- As the benchmark against which minimum-viable-governance.md and standard governance profiles are compared

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **CAIO** | **Accountable** -- ensures full governance profile is implemented for every high-risk system |
| **Model Owner** | **Responsible** -- executes governance requirements, maintains artifacts |
| **AI Risk Analyst** | **Responsible** -- performs independent validation (2nd line) |
| **Compliance Officer** | **Consulted** -- validates regulatory compliance of governance artifacts |
| **AI Governance Committee** | **Approves** -- deployment decisions for high-risk systems |
| **Board** | **Approves** -- go/no-go for high-risk AI systems with strategic implications |
| **Internal Audit** | **Assures** -- annual independent assurance of governance effectiveness |

## Regulatory Basis

- **EU AI Act Articles 6, 9-15, 17, 26, 72** -- full lifecycle obligations for high-risk AI systems
- **SAFEST items S-01 through S-22, A-01 through A-15, F-01 through F-11, E-01 through E-12, K-01 through K-11, T-01 through T-17** -- comprehensive coverage of all six pillars
- **DORA Articles 5-16** -- ICT risk management for critical systems
- **GDPR Articles 22, 35** -- automated decision-making, data protection impact assessment
- **DNB Good Practice for AI** -- full supervisory expectations for AI in critical financial processes
- **ISO/IEC 42001** -- AI management system requirements

---

## 1. Mandatory Artifacts by Lifecycle Stage

### 1.1 Discovery Phase

| # | Artifact | Description | SAFEST Ref | Owner | Reviewer |
|---|----------|------------|-----------|-------|----------|
| 1 | AI system inventory entry | Complete registry entry with risk classification, purpose, data inputs, outputs | S-01 | Model Owner | CAIO |
| 2 | Risk classification rationale | Documented assessment against EU AI Act Article 6 and Annex III | S-01 | Model Owner | Compliance Officer |
| 3 | AI Ethics Impact Assessment | Full FRIA (Fundamental Rights Impact Assessment) | E-12 | AI Ethics Lead | AI Ethics Board |
| 4 | Responsible Product Brief | Business case with ethical dimensions and stakeholder impact | E-01 | Product Manager | CAIO |
| 5 | Data Protection Impact Assessment (DPIA) | Required under GDPR Article 35 for automated decision-making | E-08 | DPO / Compliance | Autoriteit Persoonsgegevens (if required) |
| 6 | Prohibited uses screening | Verification that use case is not prohibited under EU AI Act Article 5 | E-03 | Compliance Officer | AI Ethics Board |
| 7 | Stakeholder value map | Identification of all affected stakeholders and impact assessment | E-02 | Product Manager | CAIO |
| 8 | Go/no-go decision record | Board-level approval for high-risk AI development | A-01 | CAIO | Board |

### 1.2 Design Phase

| # | Artifact | Description | SAFEST Ref | Owner | Reviewer |
|---|----------|------------|-----------|-------|----------|
| 9 | Acceptance criteria specification | Minimum 5 metrics with thresholds covering accuracy, fairness, reliability, safety, explainability | S-03 | Product Manager + Data Scientist | CAIO |
| 10 | Human-in-the-loop design | Architecture for human oversight, intervention, and override capability | A-06 | Engineering Lead | CAIO + Compliance |
| 11 | Fallback and kill switch design | Automated and manual fallback procedures, rollback capability | S-13 | Engineering Lead | CAIO |
| 12 | Explainability approach | How decisions will be explained to customers and internal reviewers | T-06 | Data Scientist | Product Manager + Compliance |
| 13 | Audit trail architecture | Immutable logging of inputs, outputs, decisions, model versions, timestamps | A-11 | Engineering Lead | Internal Audit |
| 14 | Customer transparency plan | How customers will be informed of AI involvement (EU AI Act Art. 13) | T-06 | Product Manager | Compliance Officer |
| 15 | Data governance plan | Data quality, lineage, bias assessment for training data | S-10 | Data Scientist | AI Risk Analyst |

### 1.3 Development Phase

| # | Artifact | Description | SAFEST Ref | Owner | Reviewer |
|---|----------|------------|-----------|-------|----------|
| 16 | Model card (complete) | Full technical documentation per template | T-12 | Data Scientist | AI Risk Analyst |
| 17 | Data sheet | Training data documentation, sources, lineage, preprocessing | S-10 | Data Scientist | AI Risk Analyst |
| 18 | Evaluation pipeline | Automated eval suite covering all acceptance criteria | S-03 | ML Engineer | CAIO |
| 19 | Bias and fairness evaluation | Testing across all relevant protected characteristics | F-03 | Data Scientist | AI Risk Analyst |
| 20 | Stress test results | Performance under adverse conditions, edge cases, extreme inputs | S-05 | ML Engineer | AI Risk Analyst |
| 21 | Adversarial test results | Robustness against adversarial inputs, prompt injection (if LLM-based) | S-06 | Security Engineer | CISO |
| 22 | Guardrail configuration | Input/output filtering rules, safety boundaries, content policies | S-07 | ML Engineer | Security Engineer |
| 23 | Independent model validation | 2nd line validation of model methodology, data, and performance | S-19 | AI Risk Analyst | CAIO |

### 1.4 Testing Phase

| # | Artifact | Description | SAFEST Ref | Owner | Reviewer |
|---|----------|------------|-----------|-------|----------|
| 24 | Full eval suite execution report | All acceptance criteria evaluated with pass/fail results | S-03 | ML Engineer | AI Risk Analyst |
| 25 | Integration test results | End-to-end testing in staging environment | S-04 | ML Engineer | Engineering Lead |
| 26 | UAT with governance criteria | User acceptance testing that includes governance requirements | A-04 | Product Manager | CAIO |
| 27 | Fallback / kill switch test results | Verified rollback and emergency shutdown procedures | S-13 | ML Engineer | CAIO |
| 28 | Deployment readiness package | Consolidated evidence package for CAB and Committee review | A-04 | Model Owner | CAIO |

### 1.5 Deployment Phase

| # | Artifact | Description | SAFEST Ref | Owner | Reviewer |
|---|----------|------------|-----------|-------|----------|
| 29 | CAB change request (approved) | Formal change request with impact assessment and approvals | A-12 | Model Owner | CAB |
| 30 | AI Governance Committee deployment approval | Committee approval with documented rationale | A-01 | CAIO | Committee |
| 31 | Board notification | Board informed of high-risk AI deployment | K-02 | CAIO | Board |
| 32 | Monitoring configuration | Production monitoring for all acceptance criteria, drift detection, alerting | S-12 | ML Engineer | CAIO |
| 33 | Customer notification (if required) | Transparency notice to affected customers | T-06 | Product Manager | Compliance |

### 1.6 Monitoring Phase (Ongoing)

| # | Artifact | Description | SAFEST Ref | Owner | Frequency |
|---|----------|------------|-----------|-------|-----------|
| 34 | Performance monitoring report | Automated tracking of all acceptance criteria in production | S-12 | ML Engineer | Continuous + monthly summary |
| 35 | Data drift detection report | Statistical monitoring for input data distribution changes | S-12 | ML Engineer | Weekly |
| 36 | Fairness monitoring report | Ongoing fairness metrics across protected groups | F-11 | Data Scientist | Monthly |
| 37 | Incident log | All AI-related incidents, near-misses, and complaints | A-15 | Model Owner | Continuous |
| 38 | Customer feedback analysis | Analysis of AI-related customer complaints and feedback | T-08 | Product Manager | Monthly |
| 39 | Audit trail integrity check | Verification that logging is complete and unaltered | A-11 | ML Engineer | Quarterly |

### 1.7 Revalidation Phase

| # | Artifact | Description | SAFEST Ref | Owner | Frequency |
|---|----------|------------|-----------|-------|-----------|
| 40 | Revalidation eval results | Full re-execution of all acceptance criteria evaluations | S-19 | ML Engineer | Quarterly (high-risk) |
| 41 | Independent re-validation | 2nd line independent assessment of continued model fitness | S-19 | AI Risk Analyst | Annually |
| 42 | Champion-challenger comparison | Comparison of current model performance against alternatives | S-20 | Data Scientist | Annually |
| 43 | Updated model card | Model card refreshed with current performance data | T-12 | Data Scientist | After each revalidation |
| 44 | Redeployment approval (if changes) | Committee approval for material changes from revalidation | A-01 | CAIO | Per change |

---

## 2. Review Frequency

| Review Type | Frequency | Reviewer | Scope |
|------------|-----------|----------|-------|
| Performance monitoring | Continuous (automated) + monthly human review | ML Engineer + Model Owner | All acceptance criteria |
| Fairness monitoring | Monthly | Data Scientist + AI Risk Analyst | All protected group metrics |
| Model revalidation | Quarterly | AI Risk Analyst | Full eval suite re-execution |
| Independent validation | Annually | AI Risk Analyst (2nd line) or external validator | Complete model methodology review |
| Board reporting on this system | Quarterly | CAIO | Performance, risk, incidents, compliance |
| Internal audit | Annually | Internal Audit (3rd line) | Governance process effectiveness |
| DPIA refresh | Annually or at material change | DPO | Data protection impact re-assessment |
| Ethics review | Annually | AI Ethics Board | Ethical risk re-assessment |

---

## 3. Approval Workflows

### 3.1 Initial Deployment Approval

```
Model Owner prepares deployment readiness package (artifact #28)
        |
        v
AI Risk Analyst completes independent validation (artifact #23)
        |
        v
AI Steward verifies all 33 pre-deployment artifacts complete
        |
        v
CAIO reviews and recommends to AI Governance Committee
        |
        v
AI Governance Committee approves deployment
        |
        v
Board notified (artifact #31)
        |
        v
CAB change request approved (artifact #29)
        |
        v
ML Engineer executes deployment with post-deployment verification
```

### 3.2 Model Change Approval

See [Change Management for AI](../process-integration/change-management-for-ai.md) for the complete change approval workflow. For high-risk systems, all Normal and Emergency changes require CAB + CAIO approval.

---

## 4. Mandatory Evaluation Suites

For high-risk AI systems, the following evaluation categories are mandatory. The specific metrics within each category are defined by the CoE based on the system's domain.

| # | Eval Category | Minimum Metrics | Pass Criteria | Frequency |
|---|--------------|----------------|---------------|-----------|
| 1 | **Accuracy / Performance** | 3+ metrics (e.g., precision, recall, F1, AUROC) | All above CAIO-approved thresholds | Every deployment + quarterly |
| 2 | **Fairness / Bias** | Demographic parity, equalized odds, calibration across protected groups | No statistically significant disparity above threshold | Every deployment + monthly monitoring |
| 3 | **Robustness / Stress** | Performance under data shift, missing features, edge cases | Graceful degradation; no catastrophic failure | Every deployment + quarterly |
| 4 | **Security / Adversarial** | Adversarial input resistance, prompt injection defense (if LLM-based) | No harmful outputs under adversarial conditions | Every deployment + semi-annually |
| 5 | **Explainability** | Feature importance, decision rationale generation, SHAP/LIME | Explanations are accurate and human-interpretable | Every deployment + annually |
| 6 | **Reliability / Operational** | Latency, error rate, uptime, throughput | Within SLA thresholds | Continuous monitoring |
| 7 | **Data Quality** | Input data completeness, freshness, consistency | All within defined quality thresholds | Continuous monitoring |

---

## 5. Second and Third Line Review Requirements

### 5.1 Second Line (AI Risk Analyst / Compliance)

| Activity | Frequency | Scope | Output |
|----------|-----------|-------|--------|
| Independent model validation | Pre-deployment + annually | Methodology, data, performance, fairness | Validation report with findings and recommendations |
| Ongoing monitoring review | Monthly | Review monitoring dashboards and alert history | Monthly monitoring review memo |
| Governance artifact completeness check | Pre-deployment | Verify all mandatory artifacts are present and current | Completeness attestation |
| Regulatory compliance assessment | Semi-annually | Verify compliance with EU AI Act, DORA, GDPR obligations | Compliance assessment report |

### 5.2 Third Line (Internal Audit)

| Activity | Frequency | Scope | Output |
|----------|-----------|-------|--------|
| Governance process audit | Annually | End-to-end governance process for high-risk AI | Audit report with findings |
| Evidence quality audit | Annually | Sample-based review of governance artifact quality | Quality assessment |
| Three Lines of Defense effectiveness | Annually | Verify 1st and 2nd line operating effectively | 3LoD effectiveness report |
| Board reporting accuracy | Annually | Verify CAIO quarterly reports are accurate and complete | Accuracy verification |

---

## 6. Regulatory Reporting Obligations

| Obligation | Regulation | Content | Frequency |
|-----------|-----------|---------|-----------|
| High-risk AI system registration | EU AI Act Art. 49 | Register system in EU database before market placement | Pre-deployment + material changes |
| Post-market monitoring | EU AI Act Art. 72 | Continuous monitoring plan and results | Continuous + annual report |
| Serious incident reporting | EU AI Act Art. 62 | Report serious incidents to market surveillance authority | Within 15 days of awareness |
| DORA incident reporting | DORA Art. 19 | Major ICT incidents involving this system | 4h initial / 72h intermediate / 1 month final |
| GDPR compliance | GDPR Art. 22, 35 | DPIA, automated decision-making safeguards | Pre-deployment + annual DPIA refresh |
| Board governance report | SAFEST K-02 | High-risk system status in quarterly governance report | Quarterly |

---

## 7. Documentation Retention

| Document Category | Minimum Retention Period | Basis | Storage |
|------------------|------------------------|-------|---------|
| Model card and technical documentation | 10 years after retirement | EU AI Act Art. 18 | Document management system |
| Training data documentation | 10 years after retirement | EU AI Act Art. 18 | Data catalog |
| Evaluation results | 10 years after retirement | EU AI Act Art. 18 | Evaluation pipeline output repository |
| Change requests and approvals | 5 years minimum | DORA Art. 8 | GRC platform |
| Incident reports | 5 years minimum | DORA Art. 19 | Incident management system |
| Monitoring data and alerts | 3 years minimum | Internal policy (or as required by supervisor) | Monitoring platform |
| Board and Committee minutes (AI-related) | 10 years | Wft / Corporate governance | Board portal |
| Customer communications (AI transparency) | 5 years | GDPR + consumer protection | CRM / communications archive |

---

## 8. Full vs. Minimum Viable Governance Comparison

| Dimension | MVG (Minimal Risk) | Full Governance (High Risk) |
|-----------|-------------------|---------------------------|
| **Mandatory artifacts** | 10 | 44 |
| **Initial setup effort** | 1-2 days | 4-8 weeks |
| **Acceptance criteria** | 3 metrics | 5+ metrics across 7 categories |
| **Independent validation** | Not required | Pre-deployment + annually |
| **Bias testing** | Not required | Pre-deployment + monthly monitoring |
| **Deployment approval** | Model Owner | CAB + Committee + Board notification |
| **Review frequency** | Annual | Quarterly revalidation + continuous monitoring |
| **Board reporting** | Not required | Quarterly as part of governance report |
| **Incident reporting** | Internal only | Internal + potentially external (DORA, EU AI Act) |
| **Document retention** | 5 years | 10 years |
| **Audit** | None required | Annual 3rd line audit |

---

## Cross-References

- **Minimum Viable Governance:** [minimum-viable-governance.md](minimum-viable-governance.md) -- the lightest governance profile, for contrast
- **Risk Tiering Model:** [risk-tiering-model.md](risk-tiering-model.md) -- classification that determines whether full governance applies
- **Governance Roles and RACI:** [../../05-cross-cutting/governance-roles-raci.md](../../05-cross-cutting/governance-roles-raci.md) -- who is responsible at each stage
- **Bias and Fairness Evals:** [../../02-development-governance/evaluations/bias-and-fairness-evals.md](../../02-development-governance/evaluations/bias-and-fairness-evals.md) -- detailed bias evaluation methodology
- **Change Management for AI:** [../process-integration/change-management-for-ai.md](../process-integration/change-management-for-ai.md) -- CAB process for model changes
- **Supervisory Reporting Calendar:** [../process-integration/supervisory-reporting-calendar.md](../process-integration/supervisory-reporting-calendar.md) -- external reporting deadlines
- **Governance in CI/CD:** [../process-integration/governance-in-cicd.md](../process-integration/governance-in-cicd.md) -- automated enforcement of governance gates
- **Model Card Template:** [../../02-development-governance/templates/model-card.md](../../02-development-governance/templates/model-card.md) -- model card template
- **AI Ethics Impact Assessment:** [../../01-discovery-governance/templates/ai-ethics-impact-assessment.md](../../01-discovery-governance/templates/ai-ethics-impact-assessment.md) -- FRIA template

---

*Last updated: 2026-03-01*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
