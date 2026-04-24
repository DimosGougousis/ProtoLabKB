# AI & Agentic Learning Roadmap — ProtoLabs Human-Augmented Manufacturing Ambition

> **Purpose:** Defines the comprehensive learning and upskilling program to transition ProtoLabs teams from traditional manufacturing expertise to AI-augmented, agentic-enabled, human-in-the-loop operations. Supports ISO/IEC 42001 Clause 7.2 (Competence) and the broader AI governance framework.

**Version:** 1.0  
**Date:** 2026-04-24  
**Owner:** Chief AI Officer / Chief People Officer  
**Review Cycle:** Quarterly  
**Classification:** Internal Use  

---

## Executive Summary

ProtoLabs' ambition to become a **human-augmented, AI-powered manufacturing leader** requires more than technology deployment — it requires a **fundamental transformation of workforce capabilities**. This roadmap ensures every team member has the skills to work alongside AI agents, interpret AI recommendations, override unsafe outputs, and continuously improve AI systems through human feedback.

**The Human-Augmented Vision:**
> *"AI agents handle routine analysis, pattern recognition, and initial recommendations. Human experts apply judgment, creativity, and domain expertise to validate, refine, and decide. The result: faster quotes, better designs, fewer iterations, and uncompromising safety."*

---

## 1. Current State Assessment

### 1.1 Skills Landscape (April 2026)

| Role Category | Current AI Literacy | Gap | Priority |
|--------------|---------------------|-----|----------|
| **Manufacturing Engineers** | Low — familiar with CAD/CAM, limited AI exposure | High | Critical |
| **Process Engineers (PE)** | Low-Medium — process experts, limited ML understanding | High | Critical |
| **Quality Engineers** | Low — traditional SPC/MSA, no AI validation experience | High | Critical |
| **Account Managers** | Low — client-facing, no AI explanation training | Medium | High |
| **Software Engineers** | Medium — development skills, limited manufacturing domain | Medium | High |
| **ML Engineers** | Medium-High — technical ML, limited manufacturing context | Medium | Medium |
| **MLOps Engineers** | Medium — infrastructure, limited AI governance | Medium | Medium |
| **Compliance/Legal** | Low-Medium — regulatory knowledge, limited AI-specific | High | Critical |
| **Executives / Board** | Low — strategic vision, limited AI operational understanding | High | Critical |
| **Shop Floor Operators** | Very Low — hands-on manufacturing, no AI interaction | Very High | Critical |

### 1.2 Competence Gaps by Domain

| Domain | Gap Description | Impact if Unaddressed |
|--------|----------------|----------------------|
| **AI Fundamentals** | Most staff cannot explain how AI makes recommendations | Distrust of AI, poor adoption, incorrect overrides |
| **Agentic AI** | No understanding of multi-agent orchestration, tool-use risks | Safety incidents, incorrect agent coordination |
| **Human-in-the-Loop** | Unclear when to trust AI vs. when to override | Safety incidents, quality escapes, liability |
| **AI Governance** | Limited understanding of EU AI Act, ISO 42001, NIST RMF | Compliance failures, certification delays |
| **Data Literacy** | Cannot assess data quality, provenance, or bias | Poor AI outputs, undetected data issues |
| **Prompt Engineering** | Cannot effectively interact with AI systems | Suboptimal AI outputs, wasted time |
| **AI Safety** | Unaware of kill switches, guardrails, adversarial risks | Safety incidents, security breaches |
| **Explainability** | Cannot interpret AI confidence scores, citations | Poor decision-making, client distrust |

---

## 2. Target State: Human-Augmented Competence Model

### 2.1 The Three-Pillar Competence Framework

```
┌─────────────────────────────────────────────────────────────────────────────┐
│              HUMAN-AUGMENTED COMPETENCE MODEL                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│                         ┌─────────────────┐                                  │
│                         │   PILLAR 1      │                                  │
│                         │  AI Fluency     │                                  │
│                         │  (Everyone)     │                                  │
│                         │                 │                                  │
│                         │ • What AI can   │                                  │
│                         │   and cannot do │                                  │
│                         │ • How to read   │                                  │
│                         │   AI outputs    │                                  │
│                         │ • When to trust │                                  │
│                         │   vs. override  │                                  │
│                         └────────┬────────┘                                  │
│                                  │                                           │
│              ┌───────────────────┼───────────────────┐                       │
│              │                   │                   │                       │
│              ▼                   ▼                   ▼                       │
│    ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐              │
│    │   PILLAR 2      │ │   PILLAR 3      │ │   PILLAR 4      │              │
│    │ Domain-Augmented│ │  AI Governance  │ │  Agentic        │              │
│    │   Expertise     │   & Compliance    │   Collaboration   │              │
│    │                 │ │                 │ │                 │              │
│    │ • Apply domain  │ │ • EU AI Act     │ │ • Multi-agent   │              │
│    │   knowledge to  │ │   obligations   │ │   orchestration │              │
│    │   validate AI   │ │ • ISO 42001     │ │ • Tool-use risk │              │
│    │ • Identify AI   │ │   compliance    │ │   management    │              │
│    │   blind spots   │ │ • NIST RMF      │ │ • Feedback loops│              │
│    │ • Provide       │ │   application   │ │ • Continuous    │              │
│    │   feedback for  │ │ • Incident      │ │   improvement   │              │
│    │   improvement   │ │   response      │ │                 │              │
│    └─────────────────┘ └─────────────────┘ └─────────────────┘              │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 Competence Levels

| Level | Name | Description | Target Population |
|-------|------|-------------|-------------------|
| **L1** | **AI Aware** | Understands AI basics, can interpret outputs, knows when to escalate | All staff |
| **L2** | **AI Proficient** | Can effectively interact with AI, provide feedback, validate recommendations | Engineers, Managers |
| **L3** | **AI Specialist** | Can configure AI systems, design prompts, assess AI risks, lead governance | AI Team, Compliance |
| **L4** | **AI Expert** | Can develop AI systems, architect agentic workflows, lead AI strategy | ML Engineers, CAIO |
| **L5** | **AI Master** | Sets AI strategy, defines governance frameworks, represents organization externally | CAIO, Board AI Committee |

---

## 3. Role-Based Learning Paths

### 3.1 Path A: Manufacturing Engineers & Process Engineers

**Current State:** Domain experts, limited AI exposure  
**Target State:** AI-augmented domain experts who validate AI DFM recommendations and provide structured feedback

| Module | Duration | Format | Assessment |
|--------|----------|--------|------------|
| **A1: AI Fundamentals for Manufacturing** | 4 hours | Self-paced e-learning | Quiz (80% pass) |
| **A2: How ProtoLabs AI Agents Work** | 2 hours | Live demo + hands-on | Practical exercise |
| **A3: Interpreting DFM Agent Outputs** | 4 hours | Workshop | Case study evaluation |
| **A4: When to Trust vs. Override AI** | 4 hours | Workshop + simulation | Decision-making simulation |
| **A5: Providing Structured Feedback to AI** | 2 hours | Hands-on lab | Feedback quality review |
| **A6: AI Safety for Manufacturing** | 2 hours | Self-paced + quiz | Quiz (85% pass) |
| **A7: Advanced: Agentic Workflow Participation** | 4 hours | Advanced workshop | Multi-agent scenario |

**Total:** ~22 hours | **Target Completion:** 90 days | **Certification:** "AI-Augmented Manufacturing Engineer"

### 3.2 Path B: Quality Engineers

**Current State:** Traditional SPC/MSA, no AI validation experience  
**Target State:** AI quality validators who assess AI output accuracy, bias, and reliability

| Module | Duration | Format | Assessment |
|--------|----------|--------|------------|
| **B1: AI Fundamentals for Quality** | 4 hours | Self-paced e-learning | Quiz (80% pass) |
| **B2: Evaluating AI Accuracy & Reliability** | 4 hours | Workshop | Accuracy evaluation exercise |
| **B3: Bias Detection in AI Recommendations** | 4 hours | Workshop | Bias audit exercise |
| **B4: AI Validation Protocols** | 4 hours | Hands-on lab | Validation protocol design |
| **B5: Golden Dataset Management** | 2 hours | Hands-on lab | Dataset curation exercise |
| **B6: AI Incident Investigation** | 4 hours | Workshop | Root cause analysis exercise |

**Total:** ~22 hours | **Target Completion:** 90 days | **Certification:** "AI Quality Validator"

### 3.3 Path C: Account Managers & Client-Facing Staff

**Current State:** Client relationships, no AI explanation training  
**Target State:** AI translators who explain AI recommendations to clients with confidence

| Module | Duration | Format | Assessment |
|--------|----------|--------|------------|
| **C1: AI Fundamentals for Client Service** | 2 hours | Self-paced e-learning | Quiz (75% pass) |
| **C2: Explaining AI Recommendations to Clients** | 4 hours | Role-play workshop | Client explanation simulation |
| **C3: Handling Client AI Concerns** | 2 hours | Role-play workshop | Objection handling assessment |
| **C4: AI Transparency & Source Citations** | 2 hours | Workshop | Citation explanation exercise |
| **C5: AI Governance for Client Trust** | 2 hours | Self-paced | Quiz (80% pass) |

**Total:** ~12 hours | **Target Completion:** 60 days | **Certification:** "AI Client Translator"

### 3.4 Path D: Software & MLOps Engineers

**Current State:** Technical skills, limited manufacturing domain or AI governance  
**Target State:** Manufacturing-aware AI engineers who build and operate governed AI systems

| Module | Duration | Format | Assessment |
|--------|----------|--------|------------|
| **D1: Manufacturing Domain Fundamentals** | 8 hours | Self-paced + site visits | Domain knowledge quiz |
| **D2: ProtoLabs AI Architecture** | 4 hours | Technical deep-dive | Architecture diagram exercise |
| **D3: Agentic AI & Multi-Agent Orchestration** | 8 hours | Technical workshop | Agent design exercise |
| **D4: AI Governance Implementation** | 8 hours | Technical workshop | Governance control implementation |
| **D5: AI Safety Engineering** | 8 hours | Technical workshop | Safety mechanism implementation |
| **D6: MLOps for Manufacturing AI** | 8 hours | Technical workshop | Pipeline design exercise |
| **D7: Adversarial Defense Implementation** | 8 hours | Technical workshop | Defense layer implementation |

**Total:** ~52 hours | **Target Completion:** 120 days | **Certification:** "Manufacturing AI Engineer"

### 3.5 Path E: Compliance, Legal & Governance

**Current State:** Regulatory knowledge, limited AI-specific understanding  
**Target State:** AI governance experts who ensure regulatory compliance across all frameworks

| Module | Duration | Format | Assessment |
|--------|----------|--------|------------|
| **E1: AI Technology Fundamentals** | 8 hours | Self-paced e-learning | Quiz (85% pass) |
| **E2: EU AI Act Deep Dive** | 8 hours | Workshop + case studies | Compliance assessment exercise |
| **E3: ISO/IEC 42001 Implementation** | 8 hours | Workshop | Clause mapping exercise |
| **E4: NIST AI RMF Application** | 8 hours | Workshop | Risk assessment exercise |
| **E5: AI Incident Response & Reporting** | 4 hours | Simulation | Incident response simulation |
| **E6: AI Ethics & Bias** | 4 hours | Workshop | Ethics case study |
| **E7: AI Auditing Techniques** | 8 hours | Technical workshop | Audit simulation |

**Total:** ~48 hours | **Target Completion:** 120 days | **Certification:** "AI Governance Professional"

### 3.6 Path F: Executives & Board Members

**Current State:** Strategic vision, limited AI operational understanding  
**Target State:** AI-savvy leaders who make informed strategic decisions about AI investment and risk

| Module | Duration | Format | Assessment |
|--------|----------|--------|------------|
| **F1: AI for Executives — Strategic Overview** | 4 hours | Executive briefing | Strategic discussion |
| **F2: AI Risk & Opportunity for Manufacturing** | 4 hours | Executive workshop | Risk/opportunity assessment |
| **F3: AI Governance & Board Accountability** | 4 hours | Executive workshop | Governance framework review |
| **F4: AI Investment Decision-Making** | 4 hours | Case study workshop | Investment decision simulation |
| **F5: Regulatory Landscape for AI** | 2 hours | Executive briefing | Regulatory Q&A |

**Total:** ~18 hours | **Target Completion:** 90 days | **Certification:** "AI-Savvy Executive"

### 3.7 Path G: Shop Floor Operators

**Current State:** Hands-on manufacturing, no AI interaction  
**Target State:** AI-aware operators who can interact with AI-assisted equipment and escalate anomalies

| Module | Duration | Format | Assessment |
|--------|----------|--------|------------|
| **G1: What is AI? (Manufacturing Context)** | 2 hours | Interactive session | Group discussion |
| **G2: Working with AI-Assisted Equipment** | 4 hours | Hands-on training | Equipment interaction demo |
| **G3: Recognizing AI Errors & Escalating** | 2 hours | Scenario-based training | Scenario response assessment |
| **G4: AI Safety on the Shop Floor** | 2 hours | Interactive session | Safety quiz (80% pass) |

**Total:** ~10 hours | **Target Completion:** 60 days | **Certification:** "AI-Aware Operator"

---

## 4. Learning Delivery Infrastructure

### 4.1 Learning Management System (LMS)

| Requirement | Specification |
|-------------|---------------|
| **Platform** | Enterprise LMS with AI-specific content support |
| **Content Formats** | Video, interactive modules, hands-on labs, simulations |
| **Tracking** | Completion, assessment scores, time-on-task |
| **Certification** | Digital badges, printable certificates |
| **Integration** | HR system, competence matrix, performance management |

### 4.2 Hands-On Labs & Simulations

| Lab Environment | Purpose | Access |
|----------------|---------|--------|
| **ProtoLabs AI Sandbox** | Safe environment to interact with AI agents | All staff |
| **DFM Evaluation Simulator** | Practice validating AI DFM recommendations | Engineers |
| **Incident Response Simulator** | Practice AI incident triage and response | Safety/Compliance |
| **Adversarial Attack Playground** | Understand AI vulnerabilities | Technical staff |
| **Governance Dashboard Sandbox** | Practice using governance tools | Compliance |

### 4.3 Mentorship & Coaching

| Program | Description | Participants |
|---------|-------------|--------------|
| **AI Buddy System** | Pair AI-fluent staff with learners | All staff |
| **Technical Mentorship** | Senior ML engineers mentor junior staff | Technical staff |
| **Executive Coaching** | External AI strategy coach for executives | C-suite |
| **Peer Learning Circles** | Cross-functional groups discuss AI applications | All staff |

---

## 5. Implementation Timeline

### Phase 1: Foundation (Months 1-3)

| Week | Activity | Deliverable |
|------|----------|-------------|
| 1-2 | Launch AI awareness campaign | All-staff AI awareness session |
| 2-4 | Deploy LMS with foundational content | L1 content live for all staff |
| 4-8 | Begin Executive Path (F) | Executive briefings complete |
| 6-10 | Begin Compliance Path (E) | Compliance team training underway |
| 8-12 | Begin Engineering Paths (A, B, D) | Engineer training programs launched |

### Phase 2: Scale (Months 4-6)

| Week | Activity | Deliverable |
|------|----------|-------------|
| 13-16 | Complete L1 certification for all staff | 100% L1 completion |
| 16-20 | Begin Client-Facing Path (C) | AM training launched |
| 18-22 | Begin Shop Floor Path (G) | Operator training launched |
| 20-24 | Launch advanced specializations | L3/L4 programs open |

### Phase 3: Optimize (Months 7-9)

| Week | Activity | Deliverable |
|------|----------|-------------|
| 25-28 | Assess competence gaps | Gap analysis report |
| 28-32 | Launch targeted remediation | Remediation programs |
| 30-36 | First cohort L2 certifications | Certified AI-Augmented Engineers |
| 32-36 | Integrate feedback into AI systems | Human feedback loop operational |

### Phase 4: Sustain (Months 10-12)

| Week | Activity | Deliverable |
|------|----------|-------------|
| 37-40 | Quarterly refresher training | Refresher modules deployed |
| 40-44 | Advanced certifications (L3/L4) | First L3/L4 certifications |
| 44-48 | Annual competence review | Updated competence matrix |
| 48-52 | Continuous improvement | Learning program enhancements |

---

## 6. Success Metrics

| Metric | Baseline | 6-Month Target | 12-Month Target |
|--------|----------|----------------|-----------------|
| **L1 Certification Rate** | 0% | 100% | 100% |
| **L2 Certification Rate** | 0% | 60% | 85% |
| **L3 Certification Rate** | 0% | 20% | 40% |
| **Training Completion Rate** | 0% | 90% | 95% |
| **Assessment Pass Rate** | N/A | 85% | 90% |
| **AI System Adoption** | Low | 70% | 90% |
| **Human Override Rate** | N/A | <10% | <5% |
| **AI Feedback Quality Score** | N/A | >3.5/5 | >4.0/5 |
| **Incident Rate Related to AI Misuse** | N/A | Zero | Zero |
| **Client Confidence in AI** | N/A | >4.0/5 | >4.5/5 |

---

## 7. Governance of the Learning Program

### 7.1 RACI

| Activity | CAIO | CPO | HR | Line Managers | Learners |
|----------|:----:|:---:|:--:|:-------------:|:--------:|
| Define learning strategy | **A** | R | C | C | I |
| Develop content | C | C | C | **A** | I |
| Deliver training | I | I | R | R | **A** |
| Assess competence | **A** | C | R | C | I |
| Track progress | C | C | **A** | R | I |
| Certify completion | **A** | C | R | C | I |
| Integrate feedback into AI | **A** | I | I | C | R |

### 7.2 Budget

| Category | Estimated Cost | Notes |
|----------|---------------|-------|
| **LMS Platform** | $50K/year | Enterprise license |
| **Content Development** | $200K | Internal + external |
| **External Trainers** | $100K | Specialist consultants |
| **Lab Infrastructure** | $75K | Sandbox environments |
| **Certification Program** | $25K | Digital badges, exams |
| **Staff Time (opportunity cost)** | $300K | ~20 hours avg per person |
| **Total Year 1** | **$750K** | |

### 7.3 Integration with Governance Framework

| Governance Artifact | Learning Integration |
|--------------------|---------------------|
| `aims-competence-matrix.md` | Learning paths map directly to competence requirements |
| `aims-objectives-and-kpis.md` | Training metrics feed into AI objectives |
| `aims-internal-audit-checklist.md` | Audit verifies training completion and effectiveness |
| `aims-management-review-agenda.md` | Quarterly review includes learning program status |
| `aims-improvement-register.md` | Learning gaps drive improvement opportunities |

---

## 8. Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-24 | ProtoLabs AI Governance Office | Initial AI learning roadmap |

---

## See Also

- `aims-competence-matrix.md` — Role-by-role competence requirements
- `aims-management-review-agenda.md` — Quarterly review includes learning status
- `ai-opportunity-register.md` — Learning enables AI opportunities
- `governance-by-stage-framework.md` — Governance gates require competent staff
