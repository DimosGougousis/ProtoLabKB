# ML / AI Product Lifecycle Canvas — NIST AI RMF Edition

> **Purpose:** One-page snapshot of your AI product's key dimensions, incorporating the **NIST AI RMF Four Functions** and **Seven Characteristics of Trustworthy AI** as mandatory assessment dimensions. This edition ensures every AI project is evaluated against internationally recognized risk management standards.

**When to Use:**
- At the start of any new AI product initiative, before development begins
- When an existing AI product is being significantly redesigned or scope is expanding
- During annual governance reviews to verify NIST AI RMF compliance
- When onboarding new team members who need to understand the product's governance context

**Who Is Responsible:**

| Role | Responsibility |
|------|---------------|
| Product Owner | Completes Product Vision and NIST AI RMF Governance sections |
| ML/AI Engineer | Completes AI/ML Approach and NIST AI RMF Measure sections |
| Ethics/Risk Lead | Completes Risk & Ethics and NIST AI RMF Map sections |
| Governance Lead | Completes NIST AI RMF Govern section and reviews the complete canvas |
| Security Engineer | Completes NIST AI RMF Secure & Resilient assessment |

**Regulatory Basis:**
- **NIST AI RMF 1.0** — Four Functions (Govern, Map, Measure, Manage) and Seven Characteristics of Trustworthy AI
- **EU AI Act Article 9** — Risk Management System requires systematic risk identification, analysis, and mitigation
- **ISO/IEC 42001** — Expects documented understanding of AI system scope, purpose, and risk profile
- **EO 14110** — Executive Order on Safe, Secure, and Trustworthy AI

---

## Instructions

1. **Gather the right people.** This canvas requires collaborative input from Product, Engineering, Risk, and Governance.
2. **Complete all NIST AI RMF sections.** The seven characteristics are mandatory, not optional.
3. **Mark unknowns as "TBD"** with a target resolution date rather than guessing.
4. **Keep it to one page** — link to detailed documents where depth is needed.
5. **Review and update quarterly** or whenever the product scope changes significantly.
6. **Store the completed canvas** in the product's governance folder and reference it from all pillar-specific artifacts.

---

## Canvas Template

### Section 1: Product Vision

| Dimension | Your Product |
|-----------|-------------|
| **Problem Statement** | What specific problem does this AI product solve? For whom? |
| **Target Users** | Who interacts with or is affected by this AI system? |
| **Value Proposition** | Why is AI the right approach? What does AI enable? |
| **Success Criteria** | How will you know this product is successful? |
| **Scope Boundaries** | What does this AI product explicitly NOT do? |

---

### Section 2: AI/ML Approach

| Dimension | Your Product |
|-----------|-------------|
| **Model Type** | Foundation model, fine-tuned, custom-trained, hybrid, multi-agent? |
| **Data Sources** | What training/grounding data is used? How is it refreshed? |
| **Training Strategy** | Pre-trained + fine-tuned, RAG, prompt engineering, RLHF? |
| **Agent Architecture** | Single agent, multi-agent orchestration, tool-using agent? |
| **Skill Manifest** | Which skills does this agent load? Link to skill-manifest.yaml |
| **Tool-Use Registry** | What tools can the agent invoke? |
| **KB Grounding Contract** | Which knowledge-base articles are loaded? |
| **Capability Boundaries** | What can this agent NOT do? What actions are forbidden? |
| **Known Limitations** | What does the model/system do poorly? Known failure modes? |

---

### Section 3: NIST AI RMF — GOVERN Function

> **Purpose:** Establish organizational culture, structures, processes, and workforce competencies for AI risk management.

| Sub-Category | Assessment | Evidence |
|--------------|------------|----------|
| **GV-1.1** — Legal & Regulatory Requirements | [ ] Identified [ ] Documented | Link: |
| **GV-1.2** — Accountability Structures | [ ] RACI defined [ ] Approved | Link: |
| **GV-2.1** — Risk Management Culture | [ ] Risk-aware culture [ ] Training complete | Link: |
| **GV-3.1** — Workforce Diversity & Inclusion | [ ] Diverse team [ ] Bias awareness training | Link: |
| **GV-4.1** — Risk Tolerance Statements | [ ] Defined [ ] Approved by board | Link: |
| **GV-5.1** — Policies & Procedures | [ ] AI policies documented [ ] Reviewed quarterly | Link: |
| **GV-6.1** — Third-Party Risk Management | [ ] Vendor assessment complete | Link: |
| **GV-7.1** — Documentation Practices | [ ] Model cards required [ ] Audit trails configured | Link: |

**Govern Function Score:** [ ] Meets/Exceeds [ ] Meets [ ] Partially Meets [ ] Does Not Meet

---

### Section 4: NIST AI RMF — MAP Function

> **Purpose:** Establish context to frame risks related to an AI system.

| Sub-Category | Assessment | Evidence |
|--------------|------------|----------|
| **MP-1.1** — Context of Use Defined | [ ] Use cases documented [ ] User needs identified | Link: |
| **MP-1.2** — Categorization of AI System | [ ] Risk tier assigned [ ] EU AI Act classification | Link: |
| **MP-2.1** — AI System Categorization | [ ] System type defined [ ] Capabilities documented | Link: |
| **MP-3.1** — Impacts Identified | [ ] Stakeholder impacts [ ] Societal impacts | Link: |
| **MP-3.2** — Impact Categories | [ ] Individual [ ] Group [ ] Organizational [ ] Societal | Link: |
| **MP-4.1** — Likelihood & Severity | [ ] Risk likelihood rated [ ] Severity rated | Link: |
| **MP-5.1** — Risk Tracking | [ ] Risk register updated [ ] Tracking mechanism defined | Link: |

**Map Function Score:** [ ] Meets/Exceeds [ ] Meets [ ] Partially Meets [ ] Does Not Meet

---

### Section 5: NIST AI RMF — MEASURE Function

> **Purpose:** Identify appropriate metrics and methods to assess, analyze, and track AI risk and related impacts.

| Sub-Category | Assessment | Evidence |
|--------------|------------|----------|
| **MS-1.1** — Appropriate Methods Selected | [ ] Evaluation methods defined [ ] Metrics identified | Link: |
| **MS-1.2** — Effectiveness of Metrics | [ ] Metrics validated [ ] Baseline established | Link: |
| **MS-2.1** — Evaluation of AI System | [ ] Pre-deployment evals [ ] Ongoing monitoring | Link: |
| **MS-2.2** — Uncertainty & Confidence | [ ] Uncertainty quantified [ ] Confidence intervals | Link: |
| **MS-3.1** — Tracking Over Time | [ ] Performance tracked [ ] Drift detection active | Link: |
| **MS-4.1** — Feedback Mechanisms | [ ] User feedback collected [ ] Incident reporting | Link: |
| **MS-5.1** — Assurance of Processes | [ ] Internal audits [ ] External validation | Link: |

**Measure Function Score:** [ ] Meets/Exceeds [ ] Meets [ ] Partially Meets [ ] Does Not Meet

---

### Section 6: NIST AI RMF — MANAGE Function

> **Purpose:** Respond to identified risks once evaluated.

| Sub-Category | Assessment | Evidence |
|--------------|------------|----------|
| **MG-1.1** — Risk Response Planning | [ ] Response strategies defined [ ] Resources allocated | Link: |
| **MG-1.2** — Risk Treatment | [ ] Mitigation measures [ ] Risk acceptance documented | Link: |
| **MG-2.1** — Incident Response | [ ] Playbook defined [ ] Team trained | Link: |
| **MG-2.2** — Incident Recovery | [ ] Recovery procedures [ ] Business continuity | Link: |
| **MG-3.1** — Regular Review & Update | [ ] Review cadence defined [ ] Last review date | Link: |
| **MG-4.1** — Risk Communication | [ ] Stakeholder communication plan [ ] Reporting cadence | Link: |

**Manage Function Score:** [ ] Meets/Exceeds [ ] Meets [ ] Partially Meets [ ] Does Not Meet

---

### Section 7: The Seven Characteristics of Trustworthy AI

> **Purpose:** Comprehensive assessment of AI system trustworthiness across seven critical dimensions.

#### 7.1 Valid and Reliable (V&R)

| Criterion | Assessment | Evidence |
|-----------|------------|----------|
| Intended purpose achieved in real-world conditions | [ ] Yes [ ] Partially [ ] No | Link: |
| Performance consistency validated | [ ] Yes [ ] Partially [ ] No | Link: |
| Failure modes documented | [ ] Yes [ ] No | Link: |
| Accuracy metrics meet acceptance criteria | [ ] Yes [ ] No | Threshold: [ ]% |

**Score:** [ ] Meets/Exceeds [ ] Meets [ ] Partially Meets [ ] Does Not Meet

---

#### 7.2 Safe

| Criterion | Assessment | Evidence |
|-----------|------------|----------|
| Top 3 harm scenarios identified and documented | [ ] Yes [ ] No | Link: |
| Safety testing completed (red team, adversarial) | [ ] Yes [ ] Partially [ ] No | Link: |
| Kill switch configured and tested | [ ] Yes [ ] No | Link: |
| Safety documentation published | [ ] Yes [ ] No | Link: |

**Score:** [ ] Meets/Exceeds [ ] Meets [ ] Partially Meets [ ] Does Not Meet

---

#### 7.3 Secure and Resilient (S&R)

| Criterion | Assessment | Evidence |
|-----------|------------|----------|
| Adversarial attack testing completed | [ ] Yes [ ] Partially [ ] No | Link: |
| Jailbreak resistance validated | [ ] Pass [ ] Partial [ ] Fail | Link: |
| Prompt injection defenses tested | [ ] Pass [ ] Partial [ ] Fail | Link: |
| Graceful degradation configured | [ ] Yes [ ] No | Link: |
| Resilience testing completed | [ ] Yes [ ] No | Link: |

**Score:** [ ] Meets/Exceeds [ ] Meets [ ] Partially Meets [ ] Does Not Meet

---

#### 7.4 Accountable and Transparent (A&T)

| Criterion | Assessment | Evidence |
|-----------|------------|----------|
| Accountability chain defined (RACI) | [ ] Yes [ ] No | Link: |
| Named individuals for each accountability role | [ ] Yes [ ] No | Names: |
| AI disclosure to users implemented | [ ] Yes [ ] No | Link: |
| Complete audit trail configured | [ ] Yes [ ] No | Link: |
| Source citation enforced | [ ] Yes [ ] No | Link: |

**Score:** [ ] Meets/Exceeds [ ] Meets [ ] Partially Meets [ ] Does Not Meet

---

#### 7.5 Explainable and Interpretable (E&I)

| Criterion | Assessment | Evidence |
|-----------|------------|----------|
| Model documentation complete (model card) | [ ] Yes [ ] No | Link: |
| Explanation methods defined | [ ] Yes [ ] No | Methods: |
| Interpretability tools available | [ ] Yes [ ] No | Tools: |
| Explanation quality validated with users | [ ] Yes [ ] No | Link: |
| Decision tracing implemented | [ ] Yes [ ] No | Link: |

**Score:** [ ] Meets/Exceeds [ ] Meets [ ] Partially Meets [ ] Does Not Meet

---

#### 7.6 Privacy-Enhanced

| Criterion | Assessment | Evidence |
|-----------|------------|----------|
| Data Protection Impact Assessment (DPIA) completed | [ ] Yes [ ] No | Link: |
| Data minimization practiced | [ ] Yes [ ] No | Link: |
| Privacy-enhancing technologies (PETs) implemented | [ ] Yes [ ] No | PETs: |
| Customer CAD/IP protection configured | [ ] Yes [ ] No | Link: |
| Data retention policy defined and enforced | [ ] Yes [ ] No | Link: |

**Score:** [ ] Meets/Exceeds [ ] Meets [ ] Partially Meets [ ] Does Not Meet

---

#### 7.7 Fair with Harmful Bias Managed

| Criterion | Assessment | Evidence |
|-----------|------------|----------|
| Fairness criteria defined | [ ] Yes [ ] No | Criteria: |
| Bias testing completed | [ ] Yes [ ] Partially [ ] No | Link: |
| Protected groups analysis performed | [ ] Yes [ ] No | Link: |
| Fairness metrics meet thresholds | [ ] Yes [ ] No | Link: |
| Fairness monitoring active | [ ] Yes [ ] No | Link: |
| Bias reporting process defined | [ ] Yes [ ] No | Link: |

**Score:** [ ] Meets/Exceeds [ ] Meets [ ] Partially Meets [ ] Does Not Meet

---

### Section 8: Risk & Ethics Summary

| Dimension | Your Product |
|-----------|-------------|
| **EU AI Act Risk Tier** | Unacceptable / High / Limited / Minimal |
| **NIST AI RMF Overall Score** | Meets/Exceeds / Meets / Partially Meets / Does Not Meet |
| **Characteristics Requiring Attention** | List any scoring "Partially Meets" or below |
| **Mitigation Plan** | Required if any characteristic is "Partially Meets" or below |
| **Autonomy Level** | Fully autonomous / Human-in-the-loop / Human-on-the-loop / Human-in-command |
| **Harm Scenarios** | Top 3 harm scenarios with severity and likelihood |
| **Data Privacy** | What personal data is processed? GDPR basis? |

---

### Section 9: Evaluation Strategy

| Dimension | Your Product |
|-----------|-------------|
| **Product Metrics** | Business KPIs (conversion, satisfaction, resolution rate) |
| **AI Quality Metrics** | Accuracy, precision/recall, hallucination rate, latency |
| **Agentic Metrics** | Tool-use correctness, delegation accuracy, KB citation accuracy |
| **Safety Metrics** | Harmful output rate, guardrail trigger rate, escalation rate |
| **Fairness Metrics** | Demographic parity, equalized odds across protected groups |
| **NIST AI RMF Metrics** | Four function maturity scores, seven characteristics scores |
| **Acceptance Criteria** | What must be true before production? Quantify the bar. |
| **Eval Cadence** | How often are evals run? |

---

### Section 10: Governance Profile

| Dimension | Your Product |
|-----------|-------------|
| **Governance Intensity** | Light / Standard / Intensive |
| **Key Checkpoints** | Discovery Gate / Development Gate / Deployment Gate / Periodic Review |
| **Accountable Roles** | Who has final accountability for governance compliance? |
| **Regulatory Requirements** | EU AI Act, GDPR, NIST AI RMF, ISO/IEC 42001, etc. |
| **Audit Frequency** | How often is a formal governance audit conducted? |
| **Next Review Date** | When is this canvas due for review? |

---

## Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Product Owner | | | |
| ML/AI Engineer | | | |
| Ethics/Risk Lead | | | |
| Governance Lead | | | |
| Security Engineer | | | |

---

## Cross-References

- [NIST AI RMF Reference Guide](../05-cross-cutting/nist-ai-rmf-reference-guide.md) — Complete NIST AI RMF guidance
- [SAFEST to NIST AI RMF Mapping](../protolabs/nist-ai-rmf-safest-mapping.md) — Crosswalk between methodologies
- [Original ML Lifecycle Canvas](./ml-lifecycle-canvas.md) — Base template without NIST AI RMF
- [NIST AI RMF Assessment Checklist](../01-discovery-governance/checklists/nist-ai-rmf-assessment.yaml) — Machine-readable checklist

---

*Last updated: 2026-04-23 / Version: 1.0 / Classification: Internal*
