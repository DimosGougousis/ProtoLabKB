# DNB SAFEST Principles — Pre-Application Meeting Checklist

> **Purpose:** Structured preparation checklist for a pre-application meeting (vooroverleg) with De Nederlandsche Bank, addressing all six SAFEST pillars for FinTech companies deploying AI in regulated financial services (PSP, EMI, CASP).
>
> **Regulatory Basis:** DNB Good Practice for AI in the Financial Sector; Wft Section 3:17 (sound business operations); EU AI Act (Regulation (EU) 2024/1689); DORA (Regulation (EU) 2022/2554); GDPR; PSD2/MiCAR as applicable.
>
> **How to use:** For each item, prepare evidence or a clear explanation. Items marked 🔴 are critical — DNB will expect substantive answers. Items marked 🟡 are important — demonstrates maturity. Items marked 🟢 are recommended — differentiates your application.

---

## Pillar 1: SOUNDNESS (Deugdelijkheid)

*"The AI must be technically robust and accurate. It shouldn't break the payment chain if it encounters an edge case."*

DNB expects you to demonstrate that every AI system is fit for purpose, validated, and will not introduce systemic risk into the financial infrastructure.

### 1.1 Model Technical Robustness

| # | Item | Priority | Status | Evidence / Notes |
|---|------|----------|--------|-----------------|
| S-01 | **AI system inventory**: Complete register of all AI/ML models in scope, including purpose, risk classification, data inputs, outputs, and lifecycle stage | 🔴 | ☐ | |
| S-02 | **Algorithm selection rationale**: Document why each AI/ML approach was chosen over simpler alternatives (proportionality principle). Include complexity-vs-interpretability trade-off analysis | 🔴 | ☐ | |
| S-03 | **Model performance metrics**: Define and document acceptance criteria per model (accuracy, precision, recall, F1, AUC-ROC, calibration) with thresholds that trigger remediation | 🔴 | ☐ | |
| S-04 | **Edge case analysis**: Document known edge cases, how each model behaves under boundary conditions, and what happens when the model encounters data outside its training distribution | 🔴 | ☐ | |
| S-05 | **Stress testing results**: Model performance under adverse scenarios — economic stress, data quality degradation, extreme transaction volumes, out-of-distribution inputs | 🔴 | ☐ | |
| S-06 | **Adversarial robustness testing**: Results of testing against adversarial inputs, data poisoning scenarios, and model evasion attempts | 🟡 | ☐ | |
| S-07 | **Model confidence and uncertainty quantification**: How the system communicates prediction confidence and handles low-confidence outputs (fallback logic) | 🟡 | ☐ | |

### 1.2 Data Quality and Integrity

| # | Item | Priority | Status | Evidence / Notes |
|---|------|----------|--------|-----------------|
| S-08 | **Training data documentation**: Datasheets for each dataset — source, collection method, size, date range, representativeness, known limitations, and licensing/IP status | 🔴 | ☐ | |
| S-09 | **Data quality framework**: Defined quality dimensions (accuracy, completeness, timeliness, consistency) with measurement methodology and acceptance thresholds | 🔴 | ☐ | |
| S-10 | **Data lineage and provenance**: Full traceability from raw source through all transformations to model input features. Versioning of datasets | 🔴 | ☐ | |
| S-11 | **Feature engineering documentation**: All features documented with business justification, statistical properties, and sensitivity analysis | 🟡 | ☐ | |
| S-12 | **Data drift detection**: Mechanisms to detect when production data distributions deviate from training data. Defined thresholds and response procedures | 🟡 | ☐ | |

### 1.3 Operational Resilience

| # | Item | Priority | Status | Evidence / Notes |
|---|------|----------|--------|-----------------|
| S-13 | **Fallback procedures**: For every AI system, document what happens when the AI fails or is unavailable. Manual/rule-based backup processes that maintain service continuity | 🔴 | ☐ | |
| S-14 | **Recovery Time Objective (RTO)**: Defined RTO for each AI system with tested recovery procedures. How quickly can you revert to the last known-good model version? | 🔴 | ☐ | |
| S-15 | **Payment chain impact analysis**: Specific analysis of how AI failure scenarios affect end-to-end payment processing (for PSP/EMI) or transaction execution (for CASP) | 🔴 | ☐ | |
| S-16 | **Model rollback capability**: Demonstrated ability to roll back to a previous model version within a defined timeframe without service interruption | 🟡 | ☐ | |
| S-17 | **Graceful degradation**: System continues to function (potentially with reduced capability) rather than failing completely when AI components encounter errors | 🟡 | ☐ | |
| S-18 | **DORA ICT risk management alignment**: AI systems covered within ICT risk management framework per DORA Articles 5-16, including identification, protection, detection, response, and recovery | 🔴 | ☐ | |
| S-19a | **DORA Register of Information (Art. 28(3))**: Complete Register of Information maintained for ALL contractual arrangements on the use of ICT services provided by third-party ICT service providers — including AI/ML cloud services, model APIs, data providers, and MLOps platforms. Register follows the ESA/EBA ITS template format (Commission Implementing Regulation (EU) 2025/302) | 🔴 | ☐ | |
| S-19b | **Register of Information — 116 DNB validation rules**: Register passes all 116 validation rules DNB applies during submission review. These cover: (i) completeness checks — all mandatory fields populated per entity type; (ii) consistency checks — cross-references between tables (provider ↔ contract ↔ function mapping) are internally consistent; (iii) format checks — LEI codes valid, dates in correct format, NUTS codes for EU locations; (iv) business logic checks — risk assessments align with criticality classifications, subcontracting chains are fully mapped, exit strategy documentation referenced for critical/important functions | 🔴 | ☐ | |
| S-19c | **AI-specific entries in Register**: Each AI/ML third-party service separately identified — cloud AI inference (e.g., Azure OpenAI, AWS SageMaker), pre-trained model providers, training data providers, MLOps platforms. Criticality assessment per arrangement, with critical/important function flag where AI supports core financial processes (fraud detection, AML, credit scoring, payment processing) | 🔴 | ☐ | |
| S-19d | **Register submission readiness**: Register in machine-readable format (XBRL/XML per EBA ITS) ready for DNB submission. Dry-run validation completed internally before filing. DNB expects initial submission and ongoing maintenance | 🟡 | ☐ | |

### 1.4 Validation and Testing

| # | Item | Priority | Status | Evidence / Notes |
|---|------|----------|--------|-----------------|
| S-19 | **Independent model validation**: Validation performed by a team/individual independent from model development (second line of defense). Covers conceptual soundness, data integrity, discriminatory power, calibration, and stability | 🔴 | ☐ | |
| S-20 | **Validation frequency**: Schedule for periodic revalidation (minimum annually for high-risk models; triggered by material changes) | 🔴 | ☐ | |
| S-21 | **Backtesting results**: Model predictions compared against actual outcomes over a meaningful time period | 🟡 | ☐ | |
| S-22 | **Champion-challenger framework**: Process for comparing new model versions against incumbent before production promotion | 🟢 | ☐ | |

> **Important — EBA Guidelines status note (post-DORA):** Since DORA became applicable on January 17, 2025, the EBA's ICT and security risk management guidelines have been restructured. **EBA/GL/2019/04** (ICT and security risk management) has been largely superseded by DORA's own provisions (Chapter II) for DORA-covered entities including payment institutions and e-money institutions. The EBA has issued revised **Guidelines on ICT and security risk management under PSD2** (EBA/GL/2017/17, as revised) that now focus narrowly on **payment service user relationship management** — covering how PSPs manage ICT risks that directly affect the payment service user relationship, rather than the full ICT risk management landscape which DORA now governs directly. Similarly, **EBA/GL/2019/02** (outsourcing) continues to apply but must be read alongside DORA Chapter V (third-party ICT risk). When preparing testing and validation evidence, cite **DORA Art. 25-27** as the primary statutory basis for ICT testing, not the superseded EBA guidelines.

---

## Pillar 2: ACCOUNTABILITY (Verantwoordelijkheid)

*"A human must still be in the loop. You cannot blame the algorithm for a regulatory breach."*

DNB expects clear lines of responsibility, meaningful human oversight, and a governance structure where individuals — not algorithms — are accountable for outcomes.

### 2.1 Governance Structure

| # | Item | Priority | Status | Evidence / Notes |
|---|------|----------|--------|-----------------|
| A-01 | **Board-level AI accountability**: Named board member(s) with explicit accountability for AI governance and AI risk. Documented in board mandate/charter | 🔴 | ☐ | |
| A-02 | **Three-lines-of-defense model for AI**: Clear mapping — 1st line (AI development/operations teams), 2nd line (AI risk/compliance), 3rd line (internal audit). Documented with reporting lines | 🔴 | ☐ | |
| A-03 | **AI Governance Committee/Board**: Established body with terms of reference, membership, meeting cadence, decision authority, and escalation paths | 🔴 | ☐ | |
| A-04 | **RACI matrix for AI lifecycle**: Responsibility assignment for every lifecycle stage (design, build, validate, deploy, monitor, retire) across all organizational roles | 🟡 | ☐ | |
| A-05 | **Model ownership**: Named model owner for each AI system, with documented accountability for model performance, compliance, and risk management | 🔴 | ☐ | |

### 2.2 Human Oversight

| # | Item | Priority | Status | Evidence / Notes |
|---|------|----------|--------|-----------------|
| A-06 | **Human-in-the-loop design**: For high-risk decisions (credit, AML, fraud blocking), document exactly how and when a human reviews, overrides, or approves AI outputs | 🔴 | ☐ | |
| A-07 | **Override capability**: Demonstrate that authorized humans can override any AI decision in real-time, with the override logged and tracked | 🔴 | ☐ | |
| A-08 | **Automation bias mitigation**: Measures to prevent staff from rubber-stamping AI recommendations. Training, calibration exercises, periodic quality reviews of human override decisions | 🟡 | ☐ | |
| A-09 | **Kill switch / circuit breaker**: Ability to immediately disable any AI system and revert to manual/rule-based processing. Tested and documented | 🔴 | ☐ | |
| A-10 | **Escalation procedures**: Defined triggers and paths for escalating AI-related concerns (bias detected, unexpected behavior, regulatory issues) to management and board | 🔴 | ☐ | |

### 2.3 Audit Trail and Record-Keeping

| # | Item | Priority | Status | Evidence / Notes |
|---|------|----------|--------|-----------------|
| A-11 | **Decision audit trail**: Every AI-assisted decision logged with: input data, model version, output/score, confidence level, human reviewer (if applicable), final action taken | 🔴 | ☐ | |
| A-12 | **Model change log**: Complete record of all model changes — retraining, parameter updates, feature changes, data pipeline modifications — with approval records | 🔴 | ☐ | |
| A-13 | **Retention policy**: Audit logs retained for minimum 5 years (Wwft) or 10 years (EU AI Act technical documentation). Policy documented and implemented | 🔴 | ☐ | |
| A-14 | **Regulatory access**: DNB can access all AI-related documentation, logs, and source code upon request. Technical capability and process documented | 🟡 | ☐ | |

### 2.4 Incident Management

| # | Item | Priority | Status | Evidence / Notes |
|---|------|----------|--------|-----------------|
| A-15 | **AI incident response plan**: Defined incident categories, severity levels, response procedures, communication plan, and post-incident review process specific to AI failures | 🔴 | ☐ | |
| A-16 | **DORA incident reporting readiness**: Process to classify and report AI-related ICT incidents within DORA timeframes (initial: 4 hours; intermediate: 72 hours; final: 1 month) | 🔴 | ☐ | |
| A-17 | **Serious incident reporting (EU AI Act)**: Process to report serious AI incidents to market surveillance authority within 15 days (applicable from Aug 2026 for high-risk) | 🟡 | ☐ | |
| A-18 | **Root cause analysis**: Methodology for post-incident analysis of AI failures, with documented learnings fed back into model development and risk management | 🟡 | ☐ | |

---

## Pillar 3: FAIRNESS (Eerlijkheid)

*"You must prove the AI doesn't discriminate — e.g., rejecting payments or credit based on biased data."*

DNB expects proactive testing and monitoring for discriminatory outcomes across all protected characteristics, with documented remediation when bias is found.

### 3.1 Bias Assessment

| # | Item | Priority | Status | Evidence / Notes |
|---|------|----------|--------|-----------------|
| F-01 | **Protected characteristics mapping**: Identify all legally protected characteristics relevant to your services (race, ethnicity, gender, age, disability, religion, sexual orientation, nationality) and how they could be affected by AI decisions | 🔴 | ☐ | |
| F-02 | **Proxy variable analysis**: Document analysis of whether any model features serve as proxies for protected characteristics (e.g., postal code as proxy for ethnicity). Mitigation approach if proxies identified | 🔴 | ☐ | |
| F-03 | **Pre-deployment bias testing**: Results of bias/fairness testing performed before each model goes into production. Include methodology, metrics used, results by subgroup, and acceptance thresholds | 🔴 | ☐ | |
| F-04 | **Fairness metrics selection and justification**: Document which fairness metrics are used (demographic parity, equalized odds, predictive parity, disparate impact ratio) and why — acknowledging inherent trade-offs between metrics | 🔴 | ☐ | |
| F-05 | **Disparate impact analysis**: Quantified analysis showing outcome rates across protected groups. Four-fifths (80%) rule assessment where applicable | 🟡 | ☐ | |
| F-06 | **Intersectional analysis**: Bias testing across combinations of protected characteristics (e.g., gender × ethnicity), not just individual dimensions | 🟡 | ☐ | |

### 3.2 Training Data Fairness

| # | Item | Priority | Status | Evidence / Notes |
|---|------|----------|--------|-----------------|
| F-07 | **Historical bias assessment**: Analysis of whether training data encodes historical discrimination (e.g., past lending patterns reflecting redlining, historical fraud flagging patterns reflecting racial bias) | 🔴 | ☐ | |
| F-08 | **Representativeness analysis**: Document whether training data is representative of the target population. Identify and document any under- or over-represented groups | 🔴 | ☐ | |
| F-09 | **Label bias review**: Assessment of whether ground-truth labels in training data contain human bias (e.g., biased fraud investigation outcomes used as training labels) | 🟡 | ☐ | |
| F-10 | **Bias mitigation techniques**: Document techniques applied — pre-processing (reweighing, resampling), in-processing (fairness constraints), post-processing (threshold adjustment) — with justification | 🟡 | ☐ | |

### 3.3 Ongoing Fairness Monitoring

| # | Item | Priority | Status | Evidence / Notes |
|---|------|----------|--------|-----------------|
| F-11 | **Production fairness monitoring**: Continuous monitoring of model outcomes across protected groups in production. Dashboards, alert thresholds, and response procedures | 🔴 | ☐ | |
| F-12 | **Outcome tracking**: Track actual outcomes (not just predictions) by demographic group over time to detect emergent bias | 🟡 | ☐ | |
| F-13 | **Consumer complaints analysis**: Process to identify bias-related patterns in customer complaints, chargebacks, or service denials | 🟡 | ☐ | |
| F-14 | **Remediation procedures**: Documented process for what happens when bias is detected — investigation, root cause, model adjustment, affected customer notification, regulatory notification if warranted | 🔴 | ☐ | |

### 3.4 Specific Use Case Fairness

| # | Item | Priority | Status | Evidence / Notes |
|---|------|----------|--------|-----------------|
| F-15 | **Payment processing fairness** (PSP): AI does not selectively block/delay payments based on sender/receiver demographics. False positive rates in fraud detection are equitable across groups | 🔴 | ☐ | |
| F-16 | **Credit/lending fairness** (if applicable): AI credit scoring complies with EBA GL/2020/06 non-discrimination requirements. Adverse action explanations provided | 🔴 | ☐ | |
| F-17 | **Onboarding/KYC fairness**: AI-assisted customer onboarding and identity verification do not disproportionately reject individuals from specific demographic groups | 🔴 | ☐ | |
| F-18 | **Transaction monitoring fairness** (AML): AI-based AML monitoring does not disproportionately flag transactions from specific nationalities, ethnicities, or religions | 🟡 | ☐ | |

---

## Pillar 4: ETHICS (Ethiek)

*"The use of AI should align with societal values and not exploit vulnerable consumers."*

DNB expects your AI applications to serve customers' interests, protect vulnerable populations, and contribute positively to the financial system.

### 4.1 Ethical Framework

| # | Item | Priority | Status | Evidence / Notes |
|---|------|----------|--------|-----------------|
| E-01 | **AI ethics principles statement**: Board-approved document defining ethical principles governing AI use — aligned with OECD AI Principles, EU AI Act values, and DNB SAFEST | 🔴 | ☐ | |
| E-02 | **Ethical use case review process**: Formal process for evaluating proposed AI use cases against ethical principles before development begins. Include review criteria and decision authority | 🔴 | ☐ | |
| E-03 | **Prohibited AI uses**: Explicit list of AI applications the organization will NOT pursue (e.g., social scoring, subliminal manipulation, exploitation of vulnerabilities) — aligned with EU AI Act Article 5 | 🔴 | ☐ | |
| E-04 | **Ethical dilemma escalation**: Process for escalating ethical concerns about AI applications, with whistleblower protections | 🟡 | ☐ | |

### 4.2 Vulnerable Consumer Protection

| # | Item | Priority | Status | Evidence / Notes |
|---|------|----------|--------|-----------------|
| E-05 | **Vulnerable customer identification**: How AI systems identify and protect vulnerable consumers (elderly, financially illiterate, persons with disabilities, minors) | 🔴 | ☐ | |
| E-06 | **No exploitation safeguards**: Demonstrate that AI-driven pricing, product recommendations, or service decisions do not exploit vulnerable consumers' behavioral patterns or limited understanding | 🔴 | ☐ | |
| E-07 | **Accessibility**: AI-powered interfaces and services are accessible to persons with disabilities (WCAG compliance, alternative channels) | 🟡 | ☐ | |
| E-08 | **Dark pattern prohibition**: AI-driven UX does not employ dark patterns, manipulative nudges, or deceptive design to influence financial decisions | 🔴 | ☐ | |

### 4.3 Societal Impact

| # | Item | Priority | Status | Evidence / Notes |
|---|------|----------|--------|-----------------|
| E-09 | **Broader impact assessment**: Assessment of AI system impacts beyond direct users — effects on financial inclusion, market integrity, and systemic risk | 🟡 | ☐ | |
| E-10 | **Financial inclusion**: AI does not create or reinforce financial exclusion. Consider impact on underbanked/unbanked populations | 🟡 | ☐ | |
| E-11 | **Environmental sustainability**: Awareness of and measures to manage computational resource consumption and environmental impact of AI training and inference | 🟢 | ☐ | |
| E-12 | **Fundamental Rights Impact Assessment (FRIA)**: For high-risk AI systems, formal assessment of impacts on fundamental rights per EU AI Act Article 27 (required from Aug 2026) | 🟡 | ☐ | |

---

## Pillar 5: SKILLS (Vaardigheden)

*"Your board and staff must actually understand how the AI works. You can't outsource the understanding."*

DNB will test whether your organization genuinely understands its AI. This is one of the most common areas where FinTech applicants fall short.

### 5.1 Statutory Board Requirements

> **Wft §3:15 — Four-Eyes Principle (Vierogenbeginsel):** DNB requires that the day-to-day policy of every licensed financial institution is determined by at least **two natural persons**. This is a hard licensing prerequisite — your application will be rejected without it. DNB assesses each policymaker individually for fitness (geschiktheid, §3:8) and propriety (betrouwbaarheid, §3:9). For AI-intensive FinTechs, DNB expects **at least one policymaker** to have sufficient understanding of the AI systems to exercise meaningful oversight.

| # | Item | Priority | Status | Evidence / Notes |
|---|------|----------|--------|-----------------|
| K-00a | **Two-person rule (Wft §3:15)**: At least two natural persons are designated as day-to-day policymakers (dagelijks beleidsbepalers). Both identified by name with CVs prepared for DNB assessment | 🔴 | ☐ | |
| K-00b | **Fitness assessment readiness (Wft §3:8, geschiktheid)**: Each policymaker prepared for DNB fitness interview — education, experience, competency in financial services, AND demonstrable understanding of the organization's AI systems and associated risks | 🔴 | ☐ | |
| K-00c | **Propriety assessment readiness (Wft §3:9, betrouwbaarheid)**: Each policymaker prepared for DNB propriety screening — criminal record checks (VOG), financial history, regulatory history, integrity declarations | 🔴 | ☐ | |
| K-00d | **AI competency distribution across policymakers**: At least one policymaker can explain the AI systems at a technical-strategic level (architecture, risks, limitations). The other can explain the business and compliance implications. DNB may test this separately in individual interviews | 🔴 | ☐ | |
| K-00e | **Supervisory board / co-policymaker AI awareness (Wft §3:8)**: If a supervisory board or co-policymakers exist, their collective AI knowledge is documented. DNB may assess their ability to exercise effective oversight of AI-related decisions | 🟡 | ☐ | |

### 5.2 Board AI Competency and Reporting

| # | Item | Priority | Status | Evidence / Notes |
|---|------|----------|--------|-----------------|
| K-01 | **Board AI competency**: Evidence that policymakers understand how the AI systems work at a strategic level — risks, limitations, failure modes, and business implications. Training records, board papers, Q&A logs | 🔴 | ☐ | |
| K-02 | **Board AI risk reporting**: Regular board reporting on AI performance, risk metrics, incidents, and compliance status. Sample board reports prepared | 🔴 | ☐ | |
| K-03 | **Suitability preparation (geschiktheidstoets)**: Policymakers have rehearsed for DNB suitability interviews with specific attention to AI-related questions. Evidence includes: board education sessions on AI, documented challenge of AI decisions, questions raised in board minutes | 🔴 | ☐ | |
| K-04 | **Senior management AI understanding**: Key managers (CTO, CRO, CCO, MLRO) can articulate how each AI system works, its limitations, and when it should be overridden | 🔴 | ☐ | |

### 5.2 Technical Team Competency

| # | Item | Priority | Status | Evidence / Notes |
|---|------|----------|--------|-----------------|
| K-05 | **AI/ML team qualifications**: CVs, certifications, and relevant experience of data science and ML engineering team members. Demonstrate capability to develop, validate, and maintain AI systems | 🔴 | ☐ | |
| K-06 | **Model risk team qualifications**: Independent model validation team/resources with demonstrable expertise. Qualifications distinct from the development team | 🔴 | ☐ | |
| K-07 | **Compliance team AI knowledge**: Compliance officers understand AI-specific regulatory requirements (EU AI Act, GDPR Article 22, Wwft implications) and can effectively oversee AI systems | 🟡 | ☐ | |
| K-08 | **Succession planning**: Plan for key-person risk in AI teams. What happens if the lead data scientist leaves? | 🟡 | ☐ | |

### 5.3 AI Literacy Program

| # | Item | Priority | Status | Evidence / Notes |
|---|------|----------|--------|-----------------|
| K-09 | **Organization-wide AI literacy program**: Training program covering AI basics, risks, and responsible use for ALL employees who interact with AI systems — per EU AI Act Article 4 (applicable since Feb 2025) | 🔴 | ☐ | |
| K-10 | **Role-specific training**: Tailored training programs — board (strategic risks), compliance (regulatory), operations (usage), developers (responsible AI practices) | 🟡 | ☐ | |
| K-11 | **Training records**: Documented evidence of training completion, including dates, content, assessments, and pass rates | 🔴 | ☐ | |
| K-12 | **Continuous learning**: Ongoing professional development program to keep pace with evolving AI technology and regulation. Budget allocated | 🟢 | ☐ | |

### 5.4 Third-Party AI Understanding

| # | Item | Priority | Status | Evidence / Notes |
|---|------|----------|--------|-----------------|
| K-13 | **No "black box" outsourcing**: If using third-party AI (cloud APIs, vendor models), demonstrate that the organization understands how the AI works, not just what it outputs | 🔴 | ☐ | |
| K-14 | **Vendor AI documentation**: Complete technical documentation obtained from AI vendors — model methodology, training data description, performance characteristics, limitations | 🔴 | ☐ | |
| K-15 | **Internal challenge capability**: Demonstrate ability to independently validate, question, and challenge third-party AI outputs. Not just relying on vendor assurances | 🔴 | ☐ | |

---

## Pillar 6: TRANSPARENCY (Transparantie)

*"You must be able to explain how the AI reached a decision (Explainable AI or xAI)."*

DNB expects transparency at multiple levels: to the regulator, to the customer, and internally within the organization.

### 6.1 Explainability (xAI)

| # | Item | Priority | Status | Evidence / Notes |
|---|------|----------|--------|-----------------|
| T-01 | **Explainability approach per model**: Document the explainability method used for each AI system — SHAP, LIME, feature importance, counterfactual explanations, inherently interpretable models — with justification for the choice | 🔴 | ☐ | |
| T-02 | **Global model explanations**: Ability to explain overall model behavior — which features drive decisions, how features interact, what the model has "learned" | 🔴 | ☐ | |
| T-03 | **Local/individual explanations**: Ability to explain individual decisions — why this specific transaction was blocked, why this customer was flagged, why this credit score was assigned | 🔴 | ☐ | |
| T-04 | **Explanation fidelity**: Evidence that explanations accurately represent the model's actual decision process (not simplified to the point of being misleading) | 🟡 | ☐ | |
| T-05 | **Audience-appropriate explanations**: Different explanation formats for different audiences — technical (regulators/auditors), operational (compliance officers), accessible (customers) | 🟡 | ☐ | |

### 6.2 Customer Transparency

| # | Item | Priority | Status | Evidence / Notes |
|---|------|----------|--------|-----------------|
| T-06 | **AI disclosure**: Customers informed when AI is used in decisions that affect them (required by EU AI Act Article 50 and GDPR Articles 13-14) | 🔴 | ☐ | |
| T-07 | **Decision explanations to customers**: When AI-driven decisions adversely affect customers (payment blocked, application declined, account flagged), the customer receives a meaningful explanation | 🔴 | ☐ | |
| T-08 | **Right to human review**: Customers can request human review of AI-driven decisions per GDPR Article 22. Process documented, staffed, and accessible | 🔴 | ☐ | |
| T-09 | **Appeal/redress mechanism**: Clear process for customers to challenge AI decisions, with defined timeframes and escalation paths | 🔴 | ☐ | |
| T-10 | **Privacy transparency**: Clear communication about what personal data is processed by AI, for what purpose, and under what legal basis (GDPR Articles 13-14 + UAVG) | 🔴 | ☐ | |

### 6.3 Regulatory Transparency

| # | Item | Priority | Status | Evidence / Notes |
|---|------|----------|--------|-----------------|
| T-11 | **Technical documentation (EU AI Act)**: For high-risk AI systems, Annex IV-compliant technical documentation prepared or in progress (required from Aug 2026) | 🟡 | ☐ | |
| T-12 | **Model Cards**: Standardized model documentation for each AI system — purpose, training data, performance metrics, limitations, fairness assessment, ethical considerations | 🔴 | ☐ | |
| T-13 | **Source code accessibility**: DNB has the right to inspect source code under DORA. Demonstrate technical and process readiness to provide access | 🟡 | ☐ | |
| T-14 | **Regular regulatory reporting**: Process for providing AI performance, risk, and incident data to DNB as part of ongoing supervisory relationship | 🟡 | ☐ | |

### 6.4 Internal Transparency

| # | Item | Priority | Status | Evidence / Notes |
|---|------|----------|--------|-----------------|
| T-15 | **Internal model documentation**: Comprehensive documentation maintained for each AI system — development rationale, methodology, data, performance, limitations, change history | 🔴 | ☐ | |
| T-16 | **Decision traceability**: Any AI-influenced decision can be reconstructed after the fact — which model version, which input data, which features, which output, which human action | 🔴 | ☐ | |
| T-17 | **Monitoring dashboards**: Real-time visibility into AI system performance, fairness metrics, drift indicators, and operational health accessible to relevant stakeholders | 🟡 | ☐ | |
| T-18 | **Change communication**: Internal stakeholders informed of material changes to AI systems — new models, retraining, feature changes, performance shifts | 🟡 | ☐ | |

---

## Pre-Application Meeting Preparation Summary

### Documents to Bring to DNB

| # | Document | SAFEST Pillar(s) | Priority |
|---|----------|-----------------|----------|
| 1 | AI Governance Framework (board-approved) | A, E | 🔴 |
| 2 | AI System Inventory with risk classifications | S, T | 🔴 |
| 3 | Business Plan with AI strategy section | All | 🔴 |
| 4 | Model documentation / Model Cards (per AI system) | S, T | 🔴 |
| 5 | Validation reports (independent) | S, A | 🔴 |
| 6 | Bias/fairness testing results | F | 🔴 |
| 7 | Human oversight design documentation | A | 🔴 |
| 8 | AI incident response plan | A, S | 🔴 |
| 9 | Fallback procedures per AI system | S | 🔴 |
| 10 | AI ethics principles statement | E | 🔴 |
| 11 | AI literacy/training program and records | K | 🔴 |
| 12 | Board AI competency evidence | K | 🔴 |
| 13 | Explainability methodology documentation | T | 🔴 |
| 14 | GDPR compliance evidence (DPIAs, Art. 22 procedures) | T, E | 🔴 |
| 15 | Third-party AI risk assessment (if applicable) | K, S, A | 🔴 |
| 16 | DORA ICT risk management framework | S, A | 🔴 |
| 17 | Wwft/AML transaction monitoring documentation | S, F, T | 🔴 |
| 18 | Security certifications (ISO 27001 or roadmap) | S | 🟡 |
| 19 | Data governance framework | S, F | 🟡 |
| 20 | EU AI Act compliance roadmap | All | 🟡 |

### Readiness Scoring

Before scheduling the DNB pre-application meeting, assess your readiness:

| Level | Criteria | Recommendation |
|-------|----------|----------------|
| **Ready** (≥80% of 🔴 items complete) | All critical items addressed with substantive evidence | Schedule the meeting |
| **Nearly ready** (60-79% of 🔴 items complete) | Most critical items addressed; some gaps remain | Schedule in 4-8 weeks; close gaps |
| **Not yet ready** (<60% of 🔴 items complete) | Significant gaps in critical areas | Defer meeting; address gaps first |

### Common DNB Questions to Prepare For

1. *"Walk us through how your AI system makes a [payment/credit/AML] decision, step by step."*
2. *"What happens if your AI model fails at 2 AM on a Sunday?"*
3. *"How do you know your AI doesn't discriminate against [specific group]?"*
4. *"Who on your board understands how the AI works? Can they explain it?"*
5. *"If we asked to see your model's source code today, how quickly could you provide it?"*
6. *"How would a customer challenge a decision your AI made?"*
7. *"What would you do if you discovered your AML model was systematically missing a specific typology?"*
8. *"How do you ensure your third-party AI provider doesn't use your customer data to train models for others?"*
9. *"Show us the last time your model was independently validated. What were the findings?"*
10. *"How does your AI governance scale as you grow from 100 to 100,000 customers?"*
11. *"You offer crypto payment services — do you hold a PSD2 license, MiCAR authorization, or both? Explain the boundary."*

---

## MiCAR / PSD2 Overlap — Licensing Boundary for AI-Powered Crypto Payment Services

> **Critical for dual-license applicants:** If your FinTech offers crypto-asset services that include payment-like functionality (especially involving e-money tokens), you must address the MiCAR/PSD2 overlap directly with DNB. Getting this wrong means applying for the wrong license.

### The Overlap Problem

| Scenario | Primary License | Secondary License | Statutory Basis |
|----------|----------------|-------------------|-----------------|
| Crypto exchange / custody only (no payment initiation) | MiCAR CASP | None | MiCAR Art. 59 |
| Issuing e-money tokens (EMTs) | EMI (EMD2/Wft §2:10a) | MiCAR Art. 48 requires EMI/credit institution status | MiCAR Art. 48(1); EMD2 Art. 2 |
| Payment initiation using crypto-assets (not EMTs) | MiCAR CASP | Consider PSD2 PSP if fiat leg involved | MiCAR Art. 3(1)(16); PSD2 Art. 4(3) |
| Payment initiation using EMTs | PSD2 PSP / EMI | MiCAR CASP (if also providing other crypto services) | MiCAR Art. 48; PSD2 Annex I |
| Crypto-asset transfers (non-payment) | MiCAR CASP (service 10) | None | MiCAR Art. 3(1)(16)(10) |
| Fiat-to-crypto on-ramp with payment processing | PSD2 PSP (for fiat leg) | MiCAR CASP (for crypto leg) | PSD2 Art. 4(3); MiCAR Art. 59 |

### Key Statutory Provisions

- **MiCAR Art. 48(1):** E-money tokens may only be issued by credit institutions or EMIs authorized under EMD2. This means EMT issuance requires an EMI license FIRST, then MiCAR obligations layer on top.
- **MiCAR Art. 48(2):** EMTs are deemed electronic money under EMD2. All EMD2 rights (including redemption at par, Wft safeguarding requirements) apply.
- **MiCAR Recital 40:** Holders of EMTs should be granted a claim on the issuer denominated in the official currency referenced — linking directly to PSD2/EMD2 payment frameworks.
- **PSD2 Art. 3(k) exclusion scope:** Payment transactions based on crypto-assets are generally outside PSD2 UNLESS the transaction involves fiat currency or e-money tokens, at which point PSD2 applies to the fiat/EMT leg.

### Transitional Arrangements (Netherlands)

- **Pre-existing Wwft-registered CASPs**: May continue operating under transitional provisions until **July 1, 2026** (MiCAR Art. 143, NL implementation: 18-month period).
- **New CASPs from December 30, 2024**: Must apply for MiCAR authorization directly from DNB.
- **EMT issuers**: Must hold EMI license from application date — no transitional exemption for EMT issuance.
- **DNB approach**: DNB evaluates each application holistically. If your business model spans MiCAR and PSD2/EMD2, expect DNB to require clarity on which activities fall under which license and how AI governance applies to each.

### AI Governance Implications Across Dual Licenses

| AI Use Case | Applies Under | Governance Considerations |
|-------------|---------------|--------------------------|
| AI fraud detection on fiat payments | PSD2 (PSP obligations) | PSD2 Art. 5(1)(e) security; DORA Art. 6 ICT risk |
| AI fraud detection on crypto transfers | MiCAR (CASP obligations) | MiCAR Art. 68(9); DORA Art. 6 ICT risk |
| AI transaction monitoring for AML | Both (Wwft applies regardless) | Wwft Art. 3; DNB SAFEST applies to both |
| AI credit scoring for EMT-backed lending | PSD2/EMD2 + EU AI Act (high-risk) | Annex III point 5(b); EBA GL/2020/06 |
| AI market surveillance on trading platform | MiCAR Art. 76 | MiCAR Art. 92 (market abuse detection) |
| AI customer onboarding / KYC | Both (Wwft applies regardless) | Wwft Art. 3-5; DORA Art. 9 |

### What to Prepare for DNB

| # | Item | Priority |
|---|------|----------|
| 1 | Clear licensing boundary analysis — which activities fall under PSD2, which under MiCAR, which under both | 🔴 |
| 2 | Single AI governance framework that covers both license scopes (avoid separate siloed frameworks) | 🔴 |
| 3 | Wwft compliance covering ALL activities regardless of license type | 🔴 |
| 4 | DORA compliance covering ALL ICT arrangements regardless of license type | 🔴 |
| 5 | Articulation of how SAFEST applies consistently across both license scopes | 🟡 |

---

## Regulatory Cross-References

| SAFEST Pillar | EU AI Act | GDPR | DORA | Wft | Wwft | PSD2 | MiCAR |
|---------------|-----------|------|------|-----|------|------|-------|
| **Soundness** | Art. 9, 10, 15 | — | Art. 5-16, **28(3) (Register)** | §3:17 | — | Art. 5(1)(e) | Art. 68 |
| **Accountability** | Art. 14, 17, 72-73 | Art. 5(2) | Art. 17-23 | §3:17 | Art. 2d | Art. 96 | Art. 68(4) |
| **Fairness** | Art. 10 (bias), Recitals 44-47 | Art. 22 | — | §4:24a | — | — | Art. 72 |
| **Ethics** | Art. 5 (prohibitions) | Art. 25 | — | §4:24a | — | — | Art. 72 |
| **Skills** | Art. 4 (AI literacy) | — | Art. 13(6) | **§3:15 (two-person), §3:8, §3:9** | — | — | Art. 68 |
| **Transparency** | Art. 13, 50, Annex IV | Art. 13-14, 22 | Art. 6(5) | — | Art. 16 | Art. 97 | Art. 68(9) |

> **Note on EBA Guidelines:** For DORA-covered entities, EBA/GL/2019/04 (ICT risk management) has been largely superseded by DORA Chapter II. The residual EBA ICT guidance for PSPs now focuses on payment service user relationship management. EBA/GL/2019/02 (outsourcing) continues alongside DORA Chapter V. Always cite DORA as the primary statutory basis, with EBA guidelines as supplementary where they add specificity.

---

*Last updated: {{date}}*
*Version: 1.1*
*Classification: Internal / Regulatory Preparation*
