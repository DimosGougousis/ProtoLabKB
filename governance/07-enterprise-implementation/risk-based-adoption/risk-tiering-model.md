# Risk Tiering Model: Mapping EU AI Act Risk Levels to Governance Intensity

> **Purpose:** Define a practical risk tiering model that maps EU AI Act risk classifications to specific governance requirements, enabling FinTechs to apply proportional governance to each AI system.
>
> **Regulatory Basis:** EU AI Act (Regulation (EU) 2024/1689) Articles 5, 6, 50, 52, and Annexes I-III; DNB Good Practice for AI; SAFEST item S-01 (AI system inventory with risk classifications).
>
> **Key Principle:** Governance intensity must be proportional to risk. Over-governing low-risk AI wastes resources and creates governance fatigue. Under-governing high-risk AI creates regulatory exposure and customer harm. The risk tiering model solves both problems.

---

## 1. Risk Classification Framework

### 1.1 Four Risk Tiers

| Risk Tier | EU AI Act Basis | Governance Profile | Governance Intensity |
|-----------|----------------|-------------------|---------------------|
| **Unacceptable** | Article 5 | **Prohibited** -- do not deploy | N/A (no deployment) |
| **High** | Article 6, Annex III | **Full Governance** -- all pillars, all checklists, external validation, board approval | Maximum |
| **Limited** | Article 50 | **Standard Governance** -- core checklists, transparency obligations, Committee approval | Moderate |
| **Minimal** | Residual category | **Lightweight Governance** -- minimum viable governance, annual review | Minimum |

### 1.2 Unacceptable Risk -- Prohibited (EU AI Act Article 5)

The following AI practices are prohibited. If your AI system falls into this category, **do not deploy it**.

| Prohibited Practice | Financial Services Example | Why Prohibited |
|--------------------|--------------------------|----------------|
| Social scoring by public authorities (or equivalent private use) | AI scoring customers based on social behavior to determine financial service access | Violates fundamental rights |
| Subliminal manipulation causing harm | AI-driven UX designed to manipulate customers into unsuitable financial products | Exploits vulnerabilities |
| Exploitation of vulnerabilities (age, disability, social situation) | AI targeting financially vulnerable customers with high-risk products | Predatory practice |
| Real-time remote biometric identification in public spaces (law enforcement) | Not typically applicable to FinTech | Civil liberties |
| Emotion recognition in workplace or education | AI monitoring employee emotions to influence employment decisions | Privacy violation |
| Untargeted facial image scraping | Building facial recognition databases from internet images for KYC | Data protection violation |

**Action:** Review SAFEST item E-03 (Prohibited AI uses). Maintain an explicit list of AI applications your organization will NOT pursue.

### 1.3 High Risk (EU AI Act Article 6, Annex III)

An AI system is high-risk if it falls under one of the use cases listed in Annex III. For FinTechs, the most relevant are:

| Annex III Category | FinTech Use Case | Why High-Risk |
|-------------------|-----------------|---------------|
| **5(a):** AI for evaluating creditworthiness | AI credit scoring for lending decisions | Directly affects access to financial services |
| **5(b):** AI for credit scoring | ML-based credit risk models | Determines financial access and cost |
| **3(a):** AI for critical infrastructure management | AI managing core payment processing infrastructure | Systemic risk to financial infrastructure |
| **1(a):** AI biometric identification (where permitted) | AI-powered identity verification for KYC/AML | Privacy and access implications |
| **4(a):** AI in employment decisions | AI screening job applicants for FinTech roles | Employment discrimination risk |

Additionally, an AI system is high-risk if it is a safety component of a product covered by EU harmonization legislation (Article 6(1)), or if it performs profiling of natural persons (Recital 47).

**FinTech-specific high-risk systems:**

| System | Risk Tier | Rationale |
|--------|-----------|-----------|
| AI fraud detection (blocking customer transactions) | **High** | Directly blocks access to funds; false positives cause customer harm |
| AI AML transaction monitoring | **High** | False negatives create regulatory risk; false positives affect customer access |
| AI credit scoring / underwriting | **High** | Annex III category 5; directly determines financial access |
| AI customer onboarding / KYC identity verification | **High** | Annex III category 1(a); determines access to financial services |
| AI-driven debt collection prioritization | **High** | Affects vulnerable consumers; profiling of natural persons |

### 1.4 Limited Risk (EU AI Act Article 50)

AI systems that interact with natural persons or generate content, but do not fall under high-risk categories, carry transparency obligations.

| Transparency Obligation | FinTech Application |
|------------------------|---------------------|
| Disclose AI interaction (chatbot/voice) | Customer service chatbots must identify as AI |
| Label AI-generated content | AI-generated financial reports, summaries, or communications |
| Disclose deepfake-generated content | N/A for most FinTechs |
| Disclose emotion recognition/biometric categorization | If used in customer analytics |

**FinTech-specific limited-risk systems:**

| System | Risk Tier | Rationale |
|--------|-----------|-----------|
| AI product recommendation engine | **Limited** | Influences but does not determine financial decisions; transparency required |
| AI customer service chatbot | **Limited** | Must disclose AI nature; does not make consequential decisions |
| AI document summarization for compliance review | **Limited** | Assists human decision-makers; transparency to users required |
| AI-powered financial insights/dashboards for customers | **Limited** | Informational; customer should know AI-generated |
| AI email/communication drafting tools | **Limited** | Content generation; transparency about AI involvement |

### 1.5 Minimal Risk (Residual Category)

AI systems that do not fall into any of the above categories. These are the majority of AI systems in practice.

**FinTech-specific minimal-risk systems:**

| System | Risk Tier | Rationale |
|--------|-----------|-----------|
| AI-powered internal log analysis and alerting | **Minimal** | Internal tool; no direct customer impact |
| AI code review / development assistant tools | **Minimal** | Internal productivity; human reviews all output |
| AI-based internal analytics and forecasting | **Minimal** | Business intelligence; no individual impact |
| AI spam/phishing detection for internal email | **Minimal** | Internal security; no customer-facing decisions |
| AI-assisted internal knowledge management | **Minimal** | Search and summarization for employees |

---

## 2. Governance Requirements by Risk Tier

### 2.1 Full Comparison Matrix

| Governance Requirement | Minimal | Limited | High |
|-----------------------|---------|---------|------|
| **DOCUMENTATION** | | | |
| AI system inventory entry (S-01) | Required | Required | Required |
| Model Card (T-12) | Basic (1 page) | Standard (2-3 pages) | Comprehensive (full template) |
| Algorithm selection rationale (S-02) | Brief note | Documented | Detailed with alternatives analysis |
| EU AI Act Annex IV technical documentation | Not required | Not required | Required (from Aug 2026) |
| FRIA - Fundamental Rights Impact Assessment (E-12) | Not required | Not required | Required (from Aug 2026) |
| DPIA (GDPR) | If personal data | If personal data | Required |
| Fallback procedure documentation (S-13) | Brief description | Documented | Detailed with tested runbooks |
| | | | |
| **EVALUATIONS** | | | |
| Pre-deployment acceptance criteria (S-03) | 3 minimum metrics | 5+ metrics with thresholds | Full evaluation suite |
| Pre-deployment bias testing (F-03) | Not required | Basic fairness check | Full bias testing across all protected groups |
| Stress testing (S-05) | Not required | Basic stress scenarios | Comprehensive adverse scenario testing |
| Adversarial robustness testing (S-06) | Not required | Not required | Required |
| Edge case analysis (S-04) | Brief notes | Documented | Comprehensive with boundary conditions |
| Independent model validation (S-19) | Not required | Not required | Required (2nd line) |
| Backtesting (S-21) | Not required | Recommended | Required |
| | | | |
| **RUNTIME MONITORING** | | | |
| Performance monitoring | Basic health checks | Defined metrics with alerts | Real-time dashboards with automated alerts |
| Data drift detection (S-12) | Not required | Recommended | Required with automated response |
| Fairness monitoring (F-11) | Not required | Annual review | Continuous monitoring with alerts |
| Audit trail (A-11) | Basic logging | Decision logging | Full decision audit trail with reconstruction capability |
| | | | |
| **REVIEW AND APPROVAL** | | | |
| Deployment approval authority | Team lead sign-off | AI Governance Committee | AI Governance Committee + Board approval |
| Review cadence | Annual | Semi-annual | Quarterly + triggered reviews |
| Revalidation frequency (S-20) | Biennial | Annual | Annual + triggered by material changes |
| Kill switch / circuit breaker (A-09) | Good practice | Required | Required and tested quarterly |
| | | | |
| **HUMAN OVERSIGHT** | | | |
| Human-in-the-loop (A-06) | Not required | Recommended for consequential outputs | Required for all decisions |
| Override capability (A-07) | Good practice | Required | Required and tested |
| Automation bias mitigation (A-08) | Not required | Awareness training | Active mitigation program |
| | | | |
| **TRANSPARENCY** | | | |
| Customer AI disclosure (T-06) | Not required | Required | Required |
| Customer decision explanation (T-07) | Not required | On request | Proactive for adverse decisions |
| Right to human review (T-08) | Not required | On request | Proactive offer |
| Explainability method documented (T-01) | Not required | Basic approach | Full xAI methodology per model |
| | | | |
| **SKILLS** | | | |
| AI literacy training for users (K-09) | General awareness | Role-specific | Role-specific + model-specific |
| Model owner competency (K-05) | Basic ML knowledge | Demonstrated expertise | Senior expertise + domain knowledge |
| Third-party AI understanding (K-13) | Awareness | Documented understanding | Demonstrated challenge capability |

### 2.2 Checklist Summary by Tier

**Minimal Risk -- 10 Required Items:**
1. AI system inventory entry (S-01)
2. Basic model card (T-12)
3. Brief algorithm selection rationale (S-02)
4. 3 acceptance criteria defined and measured (S-03)
5. Basic fallback description (S-13)
6. Basic logging (A-11)
7. Named model owner (A-05)
8. Annual review scheduled (S-20)
9. Team lead sign-off on deployment
10. General AI literacy training completed (K-09)

**Limited Risk -- 22 Required Items (includes all minimal + 12 additional):**
All 10 minimal items, plus:
11. Standard model card (T-12)
12. 5+ evaluation metrics with thresholds (S-03)
13. Basic fairness check (F-03)
14. Basic stress testing (S-05)
15. Edge case documentation (S-04)
16. AI disclosure to customers (T-06)
17. Override capability implemented (A-07)
18. Decision logging (A-11)
19. Kill switch implemented (A-09)
20. Semi-annual review cadence
21. AI Governance Committee approval
22. Role-specific training for model operators (K-10)

**High Risk -- 40+ Required Items (includes all limited + 18+ additional):**
All 22 limited items, plus:
23. Comprehensive model card with full template (T-12)
24. EU AI Act Annex IV technical documentation (T-11)
25. FRIA (E-12)
26. Full bias testing across all protected groups (F-03)
27. Comprehensive stress testing with adverse scenarios (S-05)
28. Adversarial robustness testing (S-06)
29. Independent model validation by 2nd line (S-19)
30. Backtesting results (S-21)
31. Real-time performance dashboards (T-17)
32. Automated data drift detection (S-12)
33. Continuous fairness monitoring with alerts (F-11)
34. Full decision audit trail with reconstruction (A-11, T-16)
35. Board approval for deployment
36. Quarterly review cadence + triggered reviews
37. Human-in-the-loop for all decisions (A-06)
38. Automation bias mitigation program (A-08)
39. Proactive customer decision explanations (T-07)
40. Full xAI methodology documented (T-01)
41. Champion-challenger framework (S-22)
42. Quarterly kill switch testing (A-09)

---

## 3. Decision Tree for Classifying AI Systems

Use this decision tree to classify each AI system in your inventory.

```
START: Does the AI system perform any practice
       listed in EU AI Act Article 5?
       |
       +-- YES --> UNACCEPTABLE RISK: Do not deploy (E-03)
       |
       +-- NO
            |
            Does the AI system fall under Annex III
            use cases? (credit scoring, biometric ID,
            critical infrastructure, employment, etc.)
            |
            +-- YES --> HIGH RISK: Full governance
            |
            +-- NO
                 |
                 Is the AI system a safety component of
                 a product covered by EU harmonization
                 legislation? (Article 6(1))
                 |
                 +-- YES --> HIGH RISK: Full governance
                 |
                 +-- NO
                      |
                      Does the AI system profile natural
                      persons to make or materially influence
                      decisions about them?
                      |
                      +-- YES --> Consider HIGH RISK
                      |           (case-by-case assessment)
                      |
                      +-- NO
                           |
                           Does the AI system interact directly
                           with customers (chatbot, voice) or
                           generate content shown to customers?
                           |
                           +-- YES --> LIMITED RISK:
                           |           Standard governance
                           |           + transparency obligations
                           |
                           +-- NO --> MINIMAL RISK:
                                      Lightweight governance
```

### 3.1 Escalation Criteria

Even if a system classifies as minimal or limited risk through the decision tree, escalate it to a higher tier if:

| Condition | Escalate To |
|-----------|------------|
| System processes special category personal data (GDPR Art. 9) | At least Limited, consider High |
| System affects vulnerable consumers (elderly, minors, financially distressed) | At least Limited, consider High |
| System failure would disrupt payment chain or critical financial infrastructure | High |
| System operates autonomously with no human review of individual decisions | At least Limited |
| Regulatory authority has indicated heightened scrutiny for this use case | High |
| System is novel with limited industry precedent | At least Limited |
| Combined impact of multiple minimal-risk systems creates systemic risk | Assess aggregate risk; may require higher governance for the ensemble |

### 3.2 Classification Review

Risk classifications must be reviewed:
- **At deployment** -- initial classification by 1st line, approved by 2nd line
- **At each material change** -- retraining, new features, new data sources, expanded scope
- **Annually** -- as part of AI system inventory review (S-01)
- **When regulations change** -- EU AI Act implementing acts, DNB guidance updates

---

## 4. FinTech Risk Tiering Examples

### 4.1 Payment Service Provider (PSP)

| AI System | Risk Tier | Rationale | Key Governance Items |
|-----------|-----------|-----------|---------------------|
| AI fraud detection on card transactions | High | Blocks customer payments; false positives deny service | Full governance; F-15 fairness; A-06 HITL; S-13 fallback |
| AI AML transaction monitoring | High | Regulatory obligation; false negatives = criminal liability | Full governance; F-18 monitoring fairness; A-11 audit trail |
| AI merchant risk scoring for onboarding | High | Determines merchant access to payment services | Full governance; F-17 onboarding fairness |
| AI customer service chatbot | Limited | Customer interaction; does not make financial decisions | Standard governance; T-06 disclosure; A-07 escalation to human |
| AI product recommendation (merchant analytics) | Limited | Influences but does not determine business outcomes | Standard governance; T-06 disclosure |
| AI infrastructure capacity forecasting | Minimal | Internal operations; no customer impact | Lightweight governance; annual review |
| AI log anomaly detection (internal) | Minimal | Internal security tool | Lightweight governance; annual review |

### 4.2 Electronic Money Institution (EMI)

| AI System | Risk Tier | Rationale | Key Governance Items |
|-----------|-----------|-----------|---------------------|
| AI e-money issuance risk assessment | High | Determines e-money access; prudential risk | Full governance; F-16 fairness |
| AI customer identity verification (KYC) | High | Annex III biometric; determines service access | Full governance; F-17 onboarding fairness |
| AI currency conversion optimization | Limited | Affects pricing but customer retains choice | Standard governance; T-06 transparency |
| AI spend categorization for PFM features | Limited | Customer-facing analytics; informational | Standard governance; T-06 disclosure |
| AI internal compliance report generation | Minimal | Internal efficiency tool; human reviews all output | Lightweight governance |

### 4.3 Crypto-Asset Service Provider (CASP under MiCAR)

| AI System | Risk Tier | Rationale | Key Governance Items |
|-----------|-----------|-----------|---------------------|
| AI crypto AML transaction monitoring | High | MiCAR Art. 68(9); regulatory obligation | Full governance; F-18 fairness |
| AI market manipulation detection | High | MiCAR Art. 92; market integrity | Full governance; A-11 audit trail |
| AI crypto wallet risk scoring | High | Affects customer transaction capability | Full governance; F-15 fairness |
| AI price feed aggregation | Limited | Affects pricing; customer-facing | Standard governance; T-06 transparency |
| AI market insights dashboard | Limited | Customer-facing analytics | Standard governance; T-06 disclosure |
| AI internal trade reconciliation | Minimal | Back-office automation | Lightweight governance |

---

## 5. Maintaining the Risk Tiering Model

### 5.1 Governance of the Model Itself

| Activity | Frequency | Responsible | Approver |
|----------|-----------|-------------|----------|
| Review classification criteria against regulatory developments | Semi-annually | 2nd Line (Compliance) | AI Governance Committee |
| Reclassify AI systems based on new criteria | As triggered | 1st Line (model owner) | 2nd Line (approves) |
| Audit classification accuracy | Annually | 3rd Line (Internal Audit) | Board |
| Update decision tree for new EU AI Act implementing acts | As published | 2nd Line (Compliance) | AI Governance Committee |

### 5.2 Common Classification Mistakes

| Mistake | Consequence | How to Avoid |
|---------|-------------|-------------|
| Classifying fraud detection as "limited" because it "assists" humans | Undergovernance of a system that blocks transactions | If the system can deny service, it is high-risk regardless of human review frequency |
| Classifying all internal tools as "minimal" without analysis | Missing internal tools that process personal data or affect employees | Apply the decision tree to every system, including internal ones |
| Never reclassifying as the system's scope expands | Risk tier stale; governance insufficient for current use | Require reclassification at every material change |
| Classifying third-party AI as "not our risk" | DNB holds you responsible for all AI you use, not just what you build | Apply the same tiering to vendor AI (K-13) |

---

## Cross-References

- **Minimum Viable Governance:** [minimum-viable-governance.md](minimum-viable-governance.md) -- the lightest governance profile for minimal/limited-risk systems
- **Adoption Playbook:** [adoption-playbook.md](adoption-playbook.md) -- how to roll out risk tiering across the organization
- **Three Lines of Defense:** [../organizational-model/three-lines-of-defense-for-ai.md](../organizational-model/three-lines-of-defense-for-ai.md) -- who classifies, who approves, who audits
- **AI Governance Committee Charter:** [../organizational-model/ai-governance-committee-charter.md](../organizational-model/ai-governance-committee-charter.md) -- deployment approval authority by tier
- **Governance in Agile Sprints:** [../process-integration/governance-in-agile-sprints.md](../process-integration/governance-in-agile-sprints.md) -- how risk tier drives sprint governance tasks
- **SAFEST Checklist:** See the parent AIGovernance repository at `docs/06-licensing-preparation/safest-checklist-dnb-pre-application.md`

---

*Last updated: 2026-02-28*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
