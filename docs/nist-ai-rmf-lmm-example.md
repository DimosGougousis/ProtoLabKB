# NIST AI RMF Assessment: Large Manufacturing Model (LMM)

> **Purpose:** Complete NIST AI Risk Management Framework 1.0 assessment for a Large Manufacturing Model (LMM) that generates CAD designs and manufacturing instructions. This document serves as the reference implementation for manufacturing-focused AI governance at ProtoLabs.

**Project:** Large Manufacturing Model (LMM) for Automated CAD Design Generation  
**Agent ID:** `lmm-cad-generator-v1`  
**Assessment Date:** 2026-04-23  
**Risk Tier:** High-Risk (EU AI Act Annex III - would apply if autonomous)  
**Current Status:** Limited-Risk (Human-in-the-Loop Required)  
**Next Review:** 2026-07-23 (Quarterly)

---

## Executive Summary

This assessment evaluates a Large Manufacturing Model (LMM) designed to generate CAD designs, structural analyses, and manufacturing toolpaths from natural language prompts and reference geometries. The system integrates with ProtoLabs' CNC machining, injection molding, and 3D printing workflows.

**Overall NIST AI RMF Score:** `MEETS` (with conditions)  
**Critical Blockers:** None  
**Conditions:** FEA validation workflow must be operational before production deployment

---

## 1. PROJECT IDENTIFICATION

| Field | Value |
|-------|-------|
| **Project Name** | Large Manufacturing Model (LMM) for CAD Design Generation |
| **Agent ID** | `lmm-cad-generator-v1` |
| **Assessment Date** | 2026-04-23 |
| **Assessment Team** | |
| &nbsp;&nbsp;&nbsp;&nbsp;Product Owner | [Name], Senior Product Manager - AI Systems |
| &nbsp;&nbsp;&nbsp;&nbsp;ML/AI Engineer | [Name], Principal AI Engineer |
| &nbsp;&nbsp;&nbsp;&nbsp;Ethics/Risk Lead | [Name], AI Risk & Compliance Lead |
| &nbsp;&nbsp;&nbsp;&nbsp;Governance Lead | [Name], AI Governance Manager |
| &nbsp;&nbsp;&nbsp;&nbsp;Security Engineer | [Name], Principal Security Engineer |
| &nbsp;&nbsp;&nbsp;&nbsp;Licensed PE (Advisor) | [Name], Professional Engineer - Mechanical |

### Assessment Status

| Checklist ID | Requirement | Status | Evidence |
|--------------|-------------|--------|----------|
| PROJ-ID-001 | Project name documented | ✅ Complete | This document |
| PROJ-ID-002 | Agent ID from registry assigned | ✅ Complete | `lmm-cad-generator-v1` registered in agent-risk-registry.yaml |
| PROJ-ID-003 | Assessment date recorded | ✅ Complete | 2026-04-23 |
| PROJ-ID-004 | Assessment team identified with roles | ✅ Complete | See table above |

---

## 2. GOVERN FUNCTION (GV) ASSESSMENT

> **Objective:** Cultivate a culture of risk management where AI safety is integrated into the engineering lifecycle.

### 2.1 Policies, Processes, Procedures, & Practices (GV-1)

| Checklist ID | Requirement | Status | Evidence | Notes |
|--------------|-------------|--------|----------|-------|
| GV-1.1 | Legal and regulatory requirements applicable to AI system identified and documented | ✅ Complete | `lmm-legal-requirements-matrix.xlsx` | Covers EU AI Act, ITAR/EAR for defense contracts, ISO 9001 for manufacturing |
| GV-1.2 | Accountability structures defined, with roles and responsibilities documented | ✅ Complete | `governance-roles-raci.md` | PE sign-off required for all structural designs |
| GV-1.3 | AI risk management policies approved by appropriate authority | ✅ Complete | Board resolution #2026-04-15 | CAIO authorized to enforce HITL mandate |

**LMM-Specific Implementation:**

| Sub-Category | Action Item | Implementation |
|--------------|-------------|----------------|
| **GV-1.1: Legal & IP** | Establish protocols for **Proprietary CAD Data** | Training data scrubbed of sensitive IP; LMM operates in private cloud instance with no external API calls. Microsoft Purview sensitivity labels applied: "Highly Confidential - Engineering" |
| **GV-1.2: Human Agency** | Define **"Human-in-the-loop" (HITL)** mandate | No AI-generated structural design sent to shop floor without sign-off from licensed Professional Engineer (PE). Workflow enforced in PLM system. |
| **GV-1.3: Tooling** | Map compliance controls to **Microsoft Purview** | Sensitivity labels prevent LMM from exfiltrating blueprints. DLP policies block downloads of generated CAD files pending PE approval. |

### 2.2 Risk Management Culture (GV-2)

| Checklist ID | Requirement | Status | Evidence | Notes |
|--------------|-------------|--------|----------|-------|
| GV-2.1 | Risk-aware culture established within the AI development team | ✅ Complete | Team charter signed 2026-03-01 | Weekly "safety standups" review harm scenarios |
| GV-2.2 | AI risk management training completed by relevant personnel | ✅ Complete | Training records in LMS | 100% completion for 12 team members |

### 2.3 Workforce Diversity & Inclusion (GV-3)

| Checklist ID | Requirement | Status | Evidence | Notes |
|--------------|-------------|--------|----------|-------|
| GV-3.1 | Diverse perspectives included in AI development and risk assessment | ✅ Complete | Team composition: 40% female, 25% underrepresented minorities | Includes mechanical engineer with 15 years shop floor experience |
| GV-3.2 | Bias awareness training completed by team members | ✅ Complete | Certificates on file | Completed 2026-02-15 |

### 2.4 Risk Tolerance & Appetite (GV-4)

| Checklist ID | Requirement | Status | Evidence | Notes |
|--------------|-------------|--------|----------|-------|
| GV-4.1 | Risk tolerance statements defined for this AI system | ✅ Complete | `ai-risk-appetite-framework.md` | See Section 8 below |
| GV-4.2 | Risk appetite approved by board or appropriate authority | ✅ Complete | Board minutes 2026-04-15 | Zero tolerance for autonomous structural design deployment |

**LMM Risk Appetite Statement:**
> "The LMM may generate design suggestions, but zero tolerance exists for autonomous deployment to production. All structural designs require PE validation. Material usage variance >15% triggers automatic hold."

### 2.5 Ongoing Monitoring & Review (GV-5)

| Checklist ID | Requirement | Status | Evidence | Notes |
|--------------|-------------|--------|----------|-------|
| GV-5.1 | AI policies and procedures reviewed at defined cadence | ✅ Complete | Review schedule: Quarterly | Next review: 2026-07-23 |
| GV-5.2 | Governance effectiveness evaluated periodically | 🔄 In Progress | Quarterly governance report template | First report due 2026-06-30 |

### 2.6 Third-Party Risk Management (GV-6)

| Checklist ID | Requirement | Status | Evidence | Notes |
|--------------|-------------|--------|----------|-------|
| GV-6.1 | Third-party AI components (models, APIs, data) identified | ✅ Complete | `third-party-components-inventory.yaml` | Base model: GPT-4; Fine-tuning data: proprietary CAD dataset |
| GV-6.2 | Third-party risk assessment completed | ✅ Complete | `third-party-model-assessment.md` | OpenAI API contract includes data retention guarantees |

### 2.7 Documentation & Reporting (GV-7)

| Checklist ID | Requirement | Status | Evidence | Notes |
|--------------|-------------|--------|----------|-------|
| GV-7.1 | Model cards required and template provided | ✅ Complete | `model-card-lmm-cad-generator.md` | Includes training data provenance, known limitations |
| GV-7.2 | Audit trails configured for AI system decisions | ✅ Complete | `audit-record-schema.yaml` | Every design generation logged with prompt, output, PE approval status |

### GOVERN Function Score: ✅ MEETS

---

## 3. MAP FUNCTION (MP) ASSESSMENT

> **Objective:** Identify context-specific risks where AI outputs meet physical production.

### 3.1 Context of Use (MP-1)

| Checklist ID | Requirement | Status | Evidence | Notes |
|--------------|-------------|--------|----------|-------|
| MP-1.1 | Use cases documented with expected benefits and limitations | ✅ Complete | `lmm-use-cases.md` | Primary: Generate initial CAD concepts from text prompts. Limitation: Not for final production designs without PE review |
| MP-1.2 | User needs and expectations identified | ✅ Complete | User research report #UR-2026-03 | Engineers want 50% faster concept iteration |
| MP-1.3 | Deployment context (environment, scale, criticality) documented | ✅ Complete | `lmm-deployment-context.md` | Staging: 10 users. Production: 50 engineers. Criticality: High (affects physical products) |

### 3.2 Categorization of AI System (MP-2)

| Checklist ID | Requirement | Status | Evidence | Notes |
|--------------|-------------|--------|----------|-------|
| MP-2.1 | AI system type classified | ✅ Complete | Architecture doc | Fine-tuned LLM with RAG over ProtoLabs KB |
| MP-2.2 | EU AI Act risk tier assigned | ✅ Complete | Risk classification: **Limited-Risk** (with HITL) | Would be High-Risk if autonomous (Annex III, critical infrastructure) |
| MP-2.3 | System capabilities and limitations documented | ✅ Complete | `lmm-capabilities-limitations.md` | Can generate: Concepts, stress analysis suggestions. Cannot: Replace PE judgment, guarantee manufacturability |

### 3.3 Impacts Analysis (MP-3)

| Checklist ID | Requirement | Status | Evidence | Notes |
|--------------|-------------|--------|----------|-------|
| MP-3.1 | Individual-level impacts identified and assessed | ✅ Complete | Impact assessment | Engineers may over-rely on AI suggestions; training addresses this |
| MP-3.2 | Group-level impacts identified and assessed | ✅ Complete | Impact assessment | Design team workflows change; change management plan in place |
| MP-3.3 | Organizational impacts identified and assessed | ✅ Complete | Business impact analysis | Potential 30% faster time-to-quote; liability exposure if designs fail |
| MP-3.4 | Societal impacts identified and assessed | ✅ Complete | Societal impact review | Products used in medical/aerospace; failure could harm end-users |

### 3.4 Likelihood & Severity Assessment (MP-4)

| Checklist ID | Requirement | Status | Evidence | Notes |
|--------------|-------------|--------|----------|-------|
| MP-4.1 | Risk likelihood rated for each identified risk | ✅ Complete | `lmm-risk-register.xlsx` | See Critical Risk Vectors below |
| MP-4.2 | Risk severity rated for each identified risk | ✅ Complete | `lmm-risk-register.xlsx` | Structural failure: Critical severity |
| MP-4.3 | Overall risk rating determined | ✅ Complete | Risk matrix | **HIGH** without HITL; **MEDIUM** with HITL |

**Critical Risk Vectors (LMM-Specific):**

| Risk ID | Risk Description | Likelihood | Severity | Overall |
|---------|------------------|------------|----------|---------|
| R-001 | **Design Integrity:** "Hallucinated" geometry with insufficient wall thickness for stress load | Medium | Critical | High |
| R-002 | **Physical Safety:** Flawed machine tool path causes 5-axis CNC crash | Low | Critical | Medium |
| R-003 | **Supply Chain:** Third-party CAD plugin introduces non-standard materials | Low | High | Medium |
| R-004 | **IP Exposure:** Proprietary design features leaked in training data | Low | Critical | Medium |
| R-005 | **Over-reliance:** Engineers accept AI suggestions without adequate review | Medium | High | Medium |

### 3.5 Risk Tracking (MP-5)

| Checklist ID | Requirement | Status | Evidence | Notes |
|--------------|-------------|--------|----------|-------|
| MP-5.1 | Risk register updated with AI-specific risks | ✅ Complete | `lmm-risk-register.xlsx` | 12 risks identified, 8 mitigated, 4 monitored |
| MP-5.2 | Risk tracking mechanism defined and operational | ✅ Complete | Jira risk dashboard | Weekly risk review in standup |

### MAP Function Score: ✅ MEETS

---

## 4. MEASURE FUNCTION (MS) ASSESSMENT

> **Objective:** Quantify the "trustworthiness" of the LMM using engineering benchmarks.

### 4.1 Appropriate Methods & Metrics (MS-1)

| Checklist ID | Requirement | Status | Evidence | Notes |
|--------------|-------------|--------|----------|-------|
| MS-1.1 | Evaluation methods selected for each risk category | ✅ Complete | `lmm-eval-plan.md` | FEA validation, red teaming, bias testing |
| MS-1.2 | Key metrics identified and defined | ✅ Complete | Metrics dashboard | Accuracy, safety, fairness metrics defined |
| MS-1.3 | Metrics validated for appropriateness | 🔄 In Progress | Metric validation report | FEA correlation study ongoing |

### 4.2 Evaluation of AI System (MS-2)

| Checklist ID | Requirement | Status | Evidence | Notes |
|--------------|-------------|--------|----------|-------|
| MS-2.1 | Pre-deployment evaluation suite defined and executed | 🔄 In Progress | `lmm-eval-results/` | 80% complete; FEA validation pending |
| MS-2.2 | Evaluation covers validity, reliability, safety, and fairness | 🔄 In Progress | Eval plan | All dimensions covered |
| MS-2.3 | Uncertainty and confidence levels quantified where possible | 🔄 In Progress | Uncertainty quantification study | Confidence intervals for stress predictions |

**Technical Assessment Results:**

| Assessment | Method | Result | Threshold | Status |
|------------|--------|--------|-----------|--------|
| **Validation via Simulation** | FEA correlation study | 94% accuracy vs. traditional simulation | >90% | ✅ Pass |
| **Reliability Testing** | Red team: Impossible constraints | Model correctly flagged 18/20 impossible requests | >80% | ✅ Pass |
| **Bias in Design** | Method preference analysis | 60% preference for 3D printing vs. 40% casting | 50/50 ±10% | ⚠️ Review |

### 4.3 Tracking Over Time (MS-3)

| Checklist ID | Requirement | Status | Evidence | Notes |
|--------------|-------------|--------|----------|-------|
| MS-3.1 | Performance tracking mechanisms configured | ✅ Complete | MLflow + custom dashboard | Real-time monitoring of design generation metrics |
| MS-3.2 | Drift detection configured for model and data | ✅ Complete | Evidently AI integration | Alerts for input/output distribution drift |
| MS-3.3 | Performance baselines established | ✅ Complete | Baseline report | Baseline: 85% user satisfaction, 92% PE approval rate |

### 4.4 Feedback Mechanisms (MS-4)

| Checklist ID | Requirement | Status | Evidence | Notes |
|--------------|-------------|--------|----------|-------|
| MS-4.1 | User feedback collection mechanism implemented | ✅ Complete | In-app feedback widget | 4.2/5 average rating from 45 engineers |
| MS-4.2 | Incident reporting process defined and communicated | ✅ Complete | `ai-incident-report.md` | 24-hour reporting window; 0 incidents to date |

### 4.5 Assurance of Processes (MS-5)

| Checklist ID | Requirement | Status | Evidence | Notes |
|--------------|-------------|--------|----------|-------|
| MS-5.1 | Internal audit of AI processes completed | 🔄 In Progress | Audit scheduled 2026-05-15 | Pre-deployment audit |
| MS-5.2 | External validation conducted | ⏳ Not Started | N/A | Not required for Limited-Risk; considered for High-Risk upgrade |

### MEASURE Function Score: ⚠️ PARTIALLY MEETS

**Condition:** FEA validation workflow must demonstrate >90% correlation before production deployment.

---

## 5. MANAGE FUNCTION (MG) ASSESSMENT

> **Objective:** Deploy controls to mitigate risks and maintain operational continuity.

### 5.1 Risk Response Planning & Treatment (MG-1)

| Checklist ID | Requirement | Status | Evidence | Notes |
|--------------|-------------|--------|----------|-------|
| MG-1.1 | Risk response strategies defined | ✅ Complete | `lmm-risk-response-plan.md` | Mitigate: HITL, FEA validation. Avoid: No autonomous deployment |
| MG-1.2 | Resources allocated for risk mitigation | ✅ Complete | Budget approved | $50K allocated for PE review workflow integration |
| MG-1.3 | Risk acceptance documented for residual risks | ✅ Complete | Risk acceptance memo | Residual risk: Medium; accepted by CAIO |

### 5.2 Incident Response & Recovery (MG-2)

| Checklist ID | Requirement | Status | Evidence | Notes |
|--------------|-------------|--------|----------|-------|
| MG-2.1 | Incident response playbook defined | ✅ Complete | `lmm-incident-response-playbook.md` | Includes "Return to Known Good" procedure |
| MG-2.2 | Incident response team trained | ✅ Complete | Training certificates | 5 team members trained |
| MG-2.3 | Recovery procedures documented and tested | ✅ Complete | DR drill report 2026-03-20 | RTO: 4 hours for LMM service |
| MG-2.4 | Kill switch configured and tested | ✅ Complete | Kill switch test log | Tested monthly; last test: 2026-04-10 |

**The "Kill Switch" Protocol:**

```yaml
kill_switch_configuration:
  trigger_conditions:
    - metric: "material_usage_variance"
      threshold: "> 15%"
      action: "automatic_hold_for_review"
      system: "PLM"
    - metric: "fea_validation_failure_rate"
      threshold: "> 10%"
      action: "pause_design_generation"
      system: "LMM API"
    - metric: "user_reported_safety_concern"
      threshold: ">= 1"
      action: "immediate_shutdown_pending_investigation"
      system: "LMM API"
  
  activation_time_sla: "30 seconds"
  last_test_date: "2026-04-10"
  next_test_date: "2026-05-10"
  
  escalation_chain:
    - level_1: "On-call AI Engineer"
    - level_2: "AI Risk & Compliance Lead"
    - level_3: "CAIO"
    - level_4: "Board Technology Committee"
```

### 5.3 Regular Review & Update (MG-3)

| Checklist ID | Requirement | Status | Evidence | Notes |
|--------------|-------------|--------|----------|-------|
| MG-3.1 | Review cadence defined | ✅ Complete | Review schedule | Quarterly re-training; monthly performance review |
| MG-3.2 | Last/next review dates recorded | ✅ Complete | Calendar | Last: 2026-04-23; Next: 2026-07-23 |
| MG-3.3 | Risk management approach updated | 🔄 In Progress | Lessons learned log | Continuous improvement process active |

**Continuous Monitoring & Model Maintenance:**

| Activity | Cadence | Status |
|----------|---------|--------|
| Model drift detection | Continuous | ✅ Active |
| Performance dashboard review | Weekly | ✅ Active |
| Re-training with new shop floor data | Quarterly | Next: 2026-07-01 |
| PE approval rate analysis | Monthly | ✅ Active |
| Red team exercise | Semi-annual | Next: 2026-09-01 |

### 5.4 Risk Communication (MG-4)

| Checklist ID | Requirement | Status | Evidence | Notes |
|--------------|-------------|--------|----------|-------|
| MG-4.1 | Stakeholder communication plan defined | ✅ Complete | `lmm-communication-plan.md` | Monthly updates to engineering leadership |
| MG-4.2 | Risk reporting cadence established | ✅ Complete | Report schedule | Weekly operational; Monthly executive |
| MG-4.3 | Board/executive reporting configured | ✅ Complete | Dashboard | Integrated into quarterly governance report |

### MANAGE Function Score: ✅ MEETS

---

## 6. SEVEN CHARACTERISTICS OF TRUSTWORTHY AI

### 6.1 Valid and Reliable (CHAR-1)

| Checklist ID | Requirement | Status | Evidence | Score |
|--------------|-------------|--------|----------|-------|
| CHAR-1.1 | Intended purpose defined | ✅ Complete | Use case doc | Meets |
| CHAR-1.2 | Real-world validation | 🔄 In Progress | Pilot with 5 engineers | Partially Meets |
| CHAR-1.3 | Performance consistency | ✅ Complete | Consistency testing | Meets |
| CHAR-1.4 | Failure modes documented | ✅ Complete | Failure mode analysis | Meets |
| CHAR-1.5 | Accuracy metrics met | 🔄 In Progress | 94% FEA correlation | Meets |

**Characteristic Score:** ⚠️ **PARTIALLY MEETS**  
**Evidence:** FEA validation shows 94% accuracy vs. traditional simulation (exceeds 90% threshold). Real-world pilot ongoing with 5 engineers; preliminary results positive.

### 6.2 Safe (CHAR-2)

| Checklist ID | Requirement | Status | Evidence | Score |
|--------------|-------------|--------|----------|-------|
| CHAR-2.1 | Top 3 harm scenarios | ✅ Complete | Risk register | Meets |
| CHAR-2.2 | Safety testing | ✅ Complete | Red team results | Meets |
| CHAR-2.3 | Pre-deployment safety | 🔄 In Progress | Safety validation ongoing | Partially Meets |
| CHAR-2.4 | Safety guidance | ✅ Complete | User documentation | Meets |
| CHAR-2.5 | Risks documented | ✅ Complete | Risk register | Meets |
| CHAR-2.6 | Kill switch configured | ✅ Complete | Test log | Meets |

**Top 3 Harm Scenarios:**

1. **H-001: Structural Failure** - AI-generated design with insufficient wall thickness fails under load, causing injury or property damage
   - Likelihood: Low (mitigated by FEA validation)
   - Severity: Critical
   - Mitigation: Mandatory FEA validation + PE sign-off

2. **H-002: CNC Crash** - Flawed toolpath causes machine collision
   - Likelihood: Low (toolpaths not AI-generated, only suggested)
   - Severity: Critical
   - Mitigation: Clear scope boundary: LMM does not generate final toolpaths

3. **H-003: Material Failure** - AI suggests inappropriate material for application
   - Likelihood: Medium
   - Severity: High
   - Mitigation: Material suggestions flagged as "advisory only"; PE validation required

**Characteristic Score:** ✅ **MEETS**

### 6.3 Secure and Resilient (CHAR-3)

| Checklist ID | Requirement | Status | Evidence | Score |
|--------------|-------------|--------|----------|-------|
| CHAR-3.1 | Adversarial testing | ✅ Complete | Red team report | Meets |
| CHAR-3.2 | Jailbreak resistance | ✅ Complete | Jailbreak test results | Meets |
| CHAR-3.3 | Prompt injection | ✅ Complete | Injection test results | Meets |
| CHAR-3.4 | Data poisoning | 🔄 In Progress | Data validation ongoing | Partially Meets |
| CHAR-3.5 | Graceful degradation | ✅ Complete | Degradation test | Meets |
| CHAR-3.6 | Resilience testing | ⏳ Not Started | Scheduled Q3 | Not Started |

**Characteristic Score:** ⚠️ **PARTIALLY MEETS**  
**Evidence:** Jailbreak resistance validated (0% success rate for 50 attempts). Prompt injection defenses tested and passed. Data poisoning validation ongoing for training dataset.

### 6.4 Accountable and Transparent (CHAR-4)

| Checklist ID | Requirement | Status | Evidence | Score |
|--------------|-------------|--------|----------|-------|
| CHAR-4.1 | Accountability chain | ✅ Complete | RACI matrix | Meets |
| CHAR-4.2 | RACI completed | ✅ Complete | Approved RACI | Meets |
| CHAR-4.3 | AI disclosure | ✅ Complete | UI implementation | Meets |
| CHAR-4.4 | Audit trail | ✅ Complete | Audit logs | Meets |
| CHAR-4.5 | Source citation | ✅ Complete | KB grounding | Meets |
| CHAR-4.6 | Challenge/appeal | ✅ Complete | Feedback mechanism | Meets |

**Accountability Chain:**

| Role | Name | Responsibility |
|------|------|----------------|
| Product Owner | [Name] | Overall accountability for LMM performance |
| ML/AI Engineer | [Name] | Technical accountability for model behavior |
| Licensed PE | [Name] | Professional accountability for structural designs |
| Governance Lead | [Name] | Compliance accountability |

**Characteristic Score:** ✅ **MEETS**

### 6.5 Explainable and Interpretable (CHAR-5)

| Checklist ID | Requirement | Status | Evidence | Score |
|--------------|-------------|--------|----------|-------|
| CHAR-5.1 | Model documentation | ✅ Complete | Model card | Meets |
| CHAR-5.2 | Explanation methods | ✅ Complete | Explanation framework | Meets |
| CHAR-5.3 | Interpretability tools | ✅ Complete | Tool documentation | Meets |
| CHAR-5.4 | Explanation quality | 🔄 In Progress | User study ongoing | Partially Meets |
| CHAR-5.5 | Decision tracing | ✅ Complete | Delegation chain audit | Meets |
| CHAR-5.6 | RAG context display | ✅ Complete | UI feature | Meets |

**Characteristic Score:** ⚠️ **PARTIALLY MEETS**  
**Evidence:** Model card complete with architecture, training data, and limitations. Explanation methods include: (1) Design rationale display, (2) Confidence scoring, (3) Alternative suggestions. User study for explanation quality in progress (n=20, preliminary satisfaction: 4.1/5).

### 6.6 Privacy-Enhanced (CHAR-6)

| Checklist ID | Requirement | Status | Evidence | Score |
|--------------|-------------|--------|----------|-------|
| CHAR-6.1 | DPIA completed | ✅ Complete | DPIA document | Meets |
| CHAR-6.2 | Data minimization | ✅ Complete | Data inventory | Meets |
| CHAR-6.3 | PETs implemented | ✅ Complete | Encryption config | Meets |
| CHAR-6.4 | CAD/IP protection | ✅ Complete | IP guardrail config | Meets |
| CHAR-6.5 | Retention policy | ✅ Complete | Policy document | Meets |
| CHAR-6.6 | Anonymization | ✅ Complete | Data processing log | Meets |

**Characteristic Score:** ✅ **MEETS**  
**Evidence:** DPIA completed 2026-03-01. Training data scrubbed of customer IP; only public domain and synthetic CAD used. Microsoft Purview sensitivity labels prevent data exfiltration. Retention: 90 days for generated designs pending PE approval; indefinite after approval.

### 6.7 Fair with Harmful Bias Managed (CHAR-7)

| Checklist ID | Requirement | Status | Evidence | Score |
|--------------|-------------|--------|----------|-------|
| CHAR-7.1 | Fairness criteria | ✅ Complete | Fairness criteria doc | Meets |
| CHAR-7.2 | Protected groups | ✅ Complete | Group analysis | Meets |
| CHAR-7.3 | Bias testing | ✅ Complete | Bias test results | Meets |
| CHAR-7.4 | Demographic parity | ✅ Complete | Parity analysis | Meets |
| CHAR-7.5 | Fairness metrics | ✅ Complete | Metrics dashboard | Meets |
| CHAR-7.6 | Fairness monitoring | ✅ Complete | Monitoring active | Meets |
| CHAR-7.7 | Bias reporting | ✅ Complete | Reporting process | Meets |
| CHAR-7.8 | Training data audit | ✅ Complete | Data audit report | Meets |

**Fairness Assessment:**

| Metric | Result | Threshold | Status |
|--------|--------|-----------|--------|
| Design method preference (3D print vs. casting) | 60/40 split | 50/50 ±15% | ⚠️ Review |
| Material suggestion bias | No significant bias | p > 0.05 | ✅ Pass |
| Cost estimation bias | Within 10% across part types | ±15% | ✅ Pass |

**Note:** Slight preference for 3D printing detected. Investigating whether this reflects training data distribution or model bias. Mitigation: Explicitly include casting examples in prompt engineering.

**Characteristic Score:** ✅ **MEETS**

---

## 7. OVERALL ASSESSMENT SUMMARY

### 7.1 Function Scores

| Function | Score | Critical Items | Blockers |
|----------|-------|----------------|----------|
| **GOVERN** | ✅ MEETS | 6/6 Complete | None |
| **MAP** | ✅ MEETS | 9/9 Complete | None |
| **MEASURE** | ⚠️ PARTIALLY MEETS | 6/7 Complete | FEA validation completion |
| **MANAGE** | ✅ MEETS | 7/7 Complete | None |

### 7.2 Characteristic Scores

| Characteristic | Score | Notes |
|----------------|-------|-------|
| **Valid and Reliable** | ⚠️ Partially Meets | Real-world pilot ongoing |
| **Safe** | ✅ Meets | All safety controls operational |
| **Secure and Resilient** | ⚠️ Partially Meets | Data poisoning validation pending |
| **Accountable and Transparent** | ✅ Meets | Full accountability chain |
| **Explainable and Interpretable** | ⚠️ Partially Meets | User study in progress |
| **Privacy-Enhanced** | ✅ Meets | DPIA complete, PETs implemented |
| **Fair** | ✅ Meets | Minor method preference under review |

### 7.3 Overall NIST AI RMF Score

**MEETS** (with conditions)

### 7.4 Conditions for Production Deployment

1. **FEA validation workflow operational** - Must demonstrate >90% correlation with traditional simulation
2. **Real-world pilot completion** - 30-day pilot with 10 engineers, minimum 80% satisfaction
3. **Data poisoning validation complete** - Training data audit finalized
4. **Explanation quality user study complete** - Minimum 4.0/5 satisfaction rating

### 7.5 Approval Status

| Role | Name | Signature | Date | Status |
|------|------|-----------|------|--------|
| Product Owner | [Name] | ___________ | ________ | ⏳ Pending |
| ML/AI Engineer | [Name] | ___________ | ________ | ⏳ Pending |
| Ethics/Risk Lead | [Name] | ___________ | ________ | ⏳ Pending |
| Governance Lead | [Name] | ___________ | ________ | ⏳ Pending |
| Security Engineer | [Name] | ___________ | ________ | ⏳ Pending |
| Licensed PE | [Name] | ___________ | ________ | ⏳ Pending |

---

## 8. GOVERNANCE GATE STATUS

| Gate | Status | Date | Notes |
|------|--------|------|-------|
| **Discovery Gate** | ✅ PASSED | 2026-03-15 | Project approved, risk classification: Limited-Risk |
| **Development Gate** | ✅ PASSED | 2026-04-10 | Eval suite defined, safety controls implemented |
| **Deployment Gate** | ⏳ CONDITIONAL | — | Pending FEA validation completion |
| **Periodic Review** | ⏳ SCHEDULED | 2026-07-23 | Quarterly review |

---

## 9. RISK APPETITE (LMM-Specific)

### 9.1 Risk Tolerance Statements

| Risk Category | Tolerance | Threshold | Action |
|---------------|-----------|-----------|--------|
| **Design Accuracy** | Low | <90% FEA correlation | Block deployment |
| **Safety Incidents** | Zero | Any occurrence | Immediate shutdown |
| **IP Exposure** | Zero | Any occurrence | Immediate shutdown |
| **Material Usage Variance** | Low | >15% vs. baseline | Automatic hold |
| **User Satisfaction** | Medium | <70% satisfaction | Review required |
| **PE Approval Rate** | High | <50% approval | Workflow review |

### 9.2 Zero Tolerance Items

The following are **non-negotiable**:

1. ❌ No autonomous deployment of structural designs without PE sign-off
2. ❌ No use of customer proprietary CAD data in training
3. ❌ No generation of final manufacturing toolpaths (advisory only)
4. ❌ No deployment with <90% FEA validation accuracy
5. ❌ No operation without active kill switch

---

## 10. EVIDENCE REPOSITORY

All evidence referenced in this assessment is stored in:

```
/protolabs/lmm-cad-generator-v1/
├── governance/
│   ├── nist-ai-rmf-assessment.yaml (this file)
│   ├── risk-register.xlsx
│   ├── risk-appetite-statement.md
│   └── raci-matrix.md
├── evaluations/
│   ├── fea-validation-results/
│   ├── red-team-results/
│   ├── bias-testing-results/
│   └── user-study-results/
├── documentation/
│   ├── model-card.md
│   ├── use-cases.md
│   ├── capabilities-limitations.md
│   └── incident-response-playbook.md
├── technical/
│   ├── architecture-diagram.pdf
│   ├── third-party-components-inventory.yaml
│   └── kill-switch-configuration.yaml
└── evidence/
    ├── training-certificates/
    ├── audit-logs/
    ├── test-logs/
    └── legal/
        ├── dpia.pdf
        └── third-party-contracts/
```

---

## 11. CROSS-REFERENCES

- [NIST AI RMF Reference Guide](../governance/05-cross-cutting/nist-ai-rmf-reference-guide.md)
- [NIST AI RMF Assessment Checklist](../governance/01-discovery-governance/checklists/nist-ai-rmf-assessment.yaml)
- [ML Lifecycle Canvas (NIST Edition)](../governance/00-getting-started/ml-lifecycle-canvas-nist-edition.md)
- [SAFEST to NIST AI RMF Mapping](../governance/protolabs/nist-ai-rmf-safest-mapping.md)
- [AI Risk Appetite Framework](../governance/06-executive/ai-risk-appetite-framework.md)
- [Customer CAD/IP Protection Guardrail](../governance/protolabs/customer-cad-ip-protection-guardrail.md)
- [DFM Accuracy Eval Suite](../governance/protolabs/dfm-accuracy-eval-suite.yaml)

---

## 12. REVISION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 2026-03-01 | [Name] | Initial draft |
| 0.2 | 2026-03-15 | [Name] | Added Discovery Gate evidence |
| 0.3 | 2026-04-10 | [Name] | Added Development Gate evidence |
| 1.0 | 2026-04-23 | [Name] | Final assessment for Deployment Gate review |

---

*This document is classified as Internal and contains pre-deployment assessment information. Distribution is limited to the AI Governance Committee and authorized stakeholders.*

**Last Updated:** 2026-04-23  
**Next Review:** 2026-07-23  
**Document Owner:** AI Governance Office  
**Classification:** Internal
