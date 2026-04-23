# ML / AI Product Lifecycle Canvas

## Purpose

The Lifecycle Canvas is a one-page snapshot of your AI product's key dimensions -- from business value to governance profile. It forces you to think through the full lifecycle before committing resources, and it serves as the foundational reference document for all governance activities that follow.

## When to Use

- At the start of any new AI product initiative, before development begins
- When an existing AI product is being significantly redesigned or its scope is expanding
- During annual governance reviews to verify that the canvas still reflects reality
- When onboarding new team members who need to understand the product's governance context

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| Product Owner | Fills out Product Vision and Evaluation Strategy sections |
| ML/AI Engineer | Fills out AI/ML Approach and Deployment & Operations sections |
| Ethics/Risk Lead | Fills out Risk & Ethics section |
| Governance Lead | Fills out Governance Profile section and reviews the complete canvas |

## Regulatory Basis

EU AI Act Article 9 (Risk Management System) requires a systematic process to identify, analyze, and mitigate risks. This canvas serves as the initial risk identification and product scoping artifact. DNB guidance on AI governance expects a documented understanding of AI system scope, purpose, and risk profile.

---

## Instructions

1. **Gather the right people.** This canvas works best as a collaborative exercise with the Product Owner, lead engineer, and risk/compliance representative.
2. **Fill out each section honestly.** Mark unknowns as "TBD -- to be determined by [date]" rather than guessing. Unknown risks are more dangerous than known ones.
3. **Keep it to one page.** The canvas is a summary, not a specification. Link to detailed documents where depth is needed.
4. **Review and update quarterly** or whenever the product scope changes significantly.
5. **Store the completed canvas** in the product's governance folder and reference it from all pillar-specific artifacts.

---

## Canvas Template

### Section 1: Product Vision

| Dimension | Your Product |
|-----------|-------------|
| **Problem Statement** | What specific problem does this AI product solve? For whom? |
| **Target Users** | Who interacts with or is affected by this AI system? (Direct users, indirect stakeholders, impacted populations) |
| **Value Proposition** | Why is AI the right approach? What does AI enable that was not possible or practical before? |
| **Success Criteria** | How will you know this product is successful? (Business metrics, user outcomes) |
| **Scope Boundaries** | What does this AI product explicitly NOT do? Where are the boundaries of its authority? |

### Section 2: AI/ML Approach

| Dimension | Your Product |
|-----------|-------------|
| **Model Type** | Foundation model (which?), fine-tuned model, custom-trained, hybrid, multi-agent system? |
| **Data Sources** | What training/grounding data is used? Where does it come from? How is it refreshed? |
| **Training Strategy** | Pre-trained + fine-tuned, RAG, prompt engineering, RLHF, or combination? |
| **Agent Architecture** | Single agent, multi-agent orchestration, tool-using agent? Describe the delegation chain. |
| **Key Technical Decisions** | What are the most impactful technical choices (model selection, context window, temperature, etc.)? |
| **Known Limitations** | What does the model/system do poorly? Where are the known failure modes? |

### Section 3: Risk & Ethics

| Dimension | Your Product |
|-----------|-------------|
| **EU AI Act Risk Tier** | Unacceptable / High / Limited / Minimal -- with justification. See `01-discovery-governance/eu-ai-act-risk-classification.yaml` |
| **Fairness Considerations** | Which populations could be disproportionately affected? What protected attributes are relevant? |
| **Transparency Requirements** | Must users know they are interacting with AI? What disclosure obligations apply? |
| **Autonomy Level** | Fully autonomous / Human-in-the-loop / Human-on-the-loop / Human-in-command? |
| **Harm Scenarios** | What is the worst thing this system could do? List the top 3 harm scenarios with severity and likelihood. |
| **Data Privacy** | What personal data is processed? GDPR basis? Data retention policy? |

### Section 4: Evaluation Strategy

| Dimension | Your Product |
|-----------|-------------|
| **Product Metrics** | Business KPIs (conversion, satisfaction, resolution rate, etc.) |
| **AI Quality Metrics** | Accuracy, precision/recall, hallucination rate, latency, consistency, etc. |
| **Safety Metrics** | Harmful output rate, guardrail trigger rate, escalation rate, jailbreak resistance |
| **Fairness Metrics** | Demographic parity, equalized odds, or other fairness criteria across protected groups |
| **Acceptance Criteria** | What must be true before this product can go to production? Quantify the bar. |
| **Eval Cadence** | How often are evals run? (Every commit, daily, weekly, on-demand?) |

### Section 5: Governance Profile

| Dimension | Your Product |
|-----------|-------------|
| **Governance Intensity** | Light / Standard / Intensive -- based on risk tier (see table below) |
| **Key Checkpoints** | Which governance gates apply? (Discovery Gate, Development Gate, Deployment Gate, Periodic Review) |
| **Accountable Roles** | Who has final accountability for governance compliance? (Name + role) |
| **Regulatory Requirements** | Specific regulatory articles and obligations that apply |
| **Audit Frequency** | How often is a formal governance audit conducted? |

**Governance Intensity Guide:**

| Risk Tier | Governance Intensity | Required Gates | Audit Frequency |
|-----------|---------------------|----------------|-----------------|
| Minimal | Light | Discovery Gate, Deployment Gate | Annual |
| Limited | Standard | All four gates | Semi-annual |
| High | Intensive | All four gates + continuous monitoring + external audit | Quarterly |
| Unacceptable | Do not proceed | N/A -- system must be redesigned or abandoned | N/A |

### Section 6: Deployment & Operations

| Dimension | Your Product |
|-----------|-------------|
| **Deployment Strategy** | Canary, blue-green, shadow mode, gradual rollout? |
| **Monitoring Plan** | What is monitored in production? (Latency, error rate, guardrail triggers, drift indicators) |
| **Rollback Procedure** | How do you revert to the previous version? What triggers a rollback? |
| **Escalation Path** | When the agent cannot handle a situation, what happens? (Human handoff, fallback system, graceful degradation) |
| **Decommissioning Plan** | When and how would this system be shut down? What happens to users? What happens to data? |

---

## Example: Fraud Detection Agent

Below is a completed canvas for a hypothetical fraud detection agent used by a FinTech company.

### Section 1: Product Vision

| Dimension | Fraud Detection Agent |
|-----------|----------------------|
| **Problem Statement** | Real-time transaction fraud detection for retail banking customers. Current rule-based system has a 12% false positive rate, causing customer friction and operational cost. |
| **Target Users** | Direct: Fraud operations team. Indirect: Banking customers whose transactions are flagged or blocked. |
| **Value Proposition** | AI-driven fraud scoring reduces false positives by 60% while maintaining or improving fraud catch rate. Faster detection (sub-second) enables real-time blocking. |
| **Success Criteria** | False positive rate below 5%, fraud catch rate above 95%, customer complaint rate regarding false blocks decreases by 50%. |
| **Scope Boundaries** | The agent scores transactions and recommends actions. It does NOT autonomously block transactions above a configurable threshold (human review required for high-value blocks). |

### Section 2: AI/ML Approach

| Dimension | Fraud Detection Agent |
|-----------|----------------------|
| **Model Type** | Ensemble: gradient-boosted decision tree for scoring + LLM for transaction narrative analysis |
| **Data Sources** | Historical transaction data (3 years), known fraud cases, customer behavioral profiles, merchant risk scores |
| **Training Strategy** | Supervised learning on labeled fraud/non-fraud transactions, retrained monthly with new labeled data |
| **Agent Architecture** | Single agent with tool access (customer profile lookup, merchant database, transaction history) |
| **Key Technical Decisions** | Score threshold at 0.7 for auto-flag, 0.9 for human-review-required block. LLM used only for narrative explanation, not for scoring. |
| **Known Limitations** | New fraud patterns not in training data take up to 30 days to detect. International transactions have higher false positive rates due to sparser behavioral data. |

### Section 3: Risk & Ethics

| Dimension | Fraud Detection Agent |
|-----------|----------------------|
| **EU AI Act Risk Tier** | **High** -- AI system used in credit/financial decisions affecting individuals. Falls under Annex III, Section 5(b). |
| **Fairness Considerations** | Transaction patterns differ across demographic groups. International customers and customers with irregular income patterns may face higher false positive rates. Fairness testing required across nationality, income level, and transaction geography. |
| **Transparency Requirements** | Customers must be informed that AI is used in fraud detection. When a transaction is blocked, the customer must receive a human-understandable explanation. |
| **Autonomy Level** | Human-in-the-loop for blocks above the configured threshold. Fully autonomous for low-score approvals. |
| **Harm Scenarios** | (1) Legitimate high-value transaction blocked, causing financial harm to customer. (2) Systematic bias against a demographic group leading to discriminatory blocking. (3) Fraud pattern missed due to model drift, causing financial losses. |
| **Data Privacy** | Processes transaction data (GDPR Art. 6(1)(b) -- contractual necessity). Customer behavioral profiles retained for 3 years. Right to explanation under Art. 22. |

### Section 4: Evaluation Strategy

| Dimension | Fraud Detection Agent |
|-----------|----------------------|
| **Product Metrics** | False positive rate, fraud catch rate, customer complaint rate, time-to-resolution |
| **AI Quality Metrics** | AUC-ROC > 0.98, precision > 0.95 at recall > 0.95, latency P99 < 200ms |
| **Safety Metrics** | Explanation quality score > 4.0/5.0, guardrail bypass rate < 0.1%, human escalation response time < 5 min |
| **Fairness Metrics** | False positive rate disparity across demographic groups < 2x, equalized odds within 5% |
| **Acceptance Criteria** | All quality and fairness metrics met on holdout test set AND 2-week shadow mode with zero critical fairness violations |
| **Eval Cadence** | Full eval suite on every model retrain (monthly). Continuous monitoring of production metrics (real-time). Quarterly fairness audit. |

### Section 5: Governance Profile

| Dimension | Fraud Detection Agent |
|-----------|----------------------|
| **Governance Intensity** | **Intensive** -- High-risk AI system under EU AI Act |
| **Key Checkpoints** | Discovery Gate (completed), Development Gate (per retrain), Deployment Gate (per release), Monthly Periodic Review |
| **Accountable Roles** | Chief Risk Officer (ultimate accountability), Head of Fraud Operations (operational), ML Team Lead (technical) |
| **Regulatory Requirements** | EU AI Act Art. 9 (risk management), Art. 10 (data governance), Art. 13 (transparency), Art. 14 (human oversight), Art. 15 (accuracy). DNB Guidance on AI in financial services. |
| **Audit Frequency** | Internal: Quarterly. External: Annual (by independent auditor). |

### Section 6: Deployment & Operations

| Dimension | Fraud Detection Agent |
|-----------|----------------------|
| **Deployment Strategy** | Shadow mode (2 weeks) then canary (5% traffic for 1 week) then full rollout |
| **Monitoring Plan** | Real-time: latency, error rate, score distribution, guardrail triggers. Daily: false positive rate, fraud catch rate. Weekly: fairness metrics by demographic group. |
| **Rollback Procedure** | Automated rollback if false positive rate exceeds 8% or fraud catch rate drops below 90% for 1 hour. Manual rollback available via deployment pipeline. Rollback target: previous model version (always retained). |
| **Escalation Path** | High-confidence fraud (score > 0.9): block + immediate human review. Medium confidence (0.7-0.9): flag for human review within 5 minutes. Low confidence (< 0.7): approve, log for batch review. |
| **Decommissioning Plan** | If decommissioned, revert to rule-based system (maintained in parallel). Customer data retained per GDPR retention policy. Model artifacts archived for audit purposes (7 years). |

---

*After completing this canvas, proceed to the relevant governance pillar based on your product's lifecycle phase. For new products, start with [Discovery Governance](../01-discovery-governance/). For products already in development, jump to [Development Governance](../02-development-governance/).*
