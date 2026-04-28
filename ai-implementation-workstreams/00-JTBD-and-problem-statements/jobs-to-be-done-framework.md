# Jobs to be Done (JTBD) Framework for ProtoLabs AI Governance

## Executive Summary

This document defines the Jobs to be Done framework for ProtoLabs AI Governance implementation, providing clear problem statements, functional/emotional/social jobs, and desired outcomes for each workstream.

---

## Primary Job Statement

**When** ProtoLabs engineers and customers use AI-powered manufacturing tools to design, analyze, and produce parts,
**I want to** ensure these AI systems are secure, compliant, trustworthy, and resilient against threats throughout the entire manufacturing lifecycle,
**So I can** protect intellectual property, maintain customer trust, meet regulatory requirements, ensure manufacturing quality, and deliver competitive advantage without security incidents or compliance violations.

---

## Functional Jobs by Workstream

### CAD AI Design Evaluation Jobs

#### Job: CAD-CORE - Evaluate CAD Files for Manufacturability

**Job Statement:**
**When** engineers upload 3D CAD files (STEP, STL, OBJ, 3MF) to ProtoLabs for manufacturing quotes,
**I want to** automatically parse geometry, extract features, and evaluate manufacturability using AI-powered analysis,
**So I can** receive instant DFM feedback, catch issues early, reduce design iterations, and accelerate time-to-market.

**Functional Requirements:**
- Parse multi-format CAD files with high precision (CAD-001)
- Extract geometric features: holes, pockets, bosses, fillets, threads (FTR-001 to FTR-008)
- Generate 2D orthographic and isometric views for analysis (VLM-001)
- Apply process-specific DFM rules (CNC, molding, 3D printing, sheet metal)
- Generate manufacturability score with issue prioritization
- Provide actionable fix recommendations with visual guidance

**Desired Outcomes:**
- <60 seconds end-to-end analysis time for typical parts
- >95% precision in feature detection
- 100% coverage of ProtoLabs DFM guidelines
- 40% reduction in design iterations
- >4.0/5.0 user satisfaction with explanations

---

#### Job: CAD-VLM - Visual Understanding of Manufacturing Complexity

**Job Statement:**
**When** geometric rules alone cannot determine manufacturability,
**I want to** leverage Vision-Language Models to visually assess designs and provide intuitive explanations,
**So I can** catch edge cases, understand nuanced issues, and receive guidance in natural language.

**Functional Requirements:**
- Analyze 2D/3D views for manufacturability issues (VLM-004)
- Compare designs against historical projects visually (VLM-005)
- Detect anomalous features that may indicate errors (VLM-006)
- Generate natural language explanations with visual annotations (VLM-007)
- Suggest design modifications with visual previews (VLM-008)

**Desired Outcomes:**
- >90% accuracy in visual DFM assessment
- Explanations rated helpful by >80% of users
- 30% of issues caught by VLM that rules missed
- <5 second VLM inference time per view

---

#### Job: CAD-HIST - Learn from Previous Projects

**Job Statement:**
**When** evaluating a new design,
**I want to** automatically compare it against previous similar projects and their outcomes,
**So I can** leverage institutional knowledge, avoid repeating past mistakes, and benchmark against successful designs.

**Functional Requirements:**
- Store vector embeddings of all CAD designs (HST-001)
- Generate geometry fingerprints for efficient comparison (HST-002)
- Map historical DFM issues to design patterns (HST-003)
- Retrieve similar projects for benchmarking (HST-004)
- Learn success patterns from high-performing designs (HST-005)
- Catalog failure modes with root causes (HST-006)
- Aggregate cross-project analytics (HST-007)
- Implement continuous learning from outcomes (HST-008)

**Desired Outcomes:**
- <100ms similarity search time
- Top-5 similar project accuracy >90%
- 20% improvement in DFM prediction accuracy with historical data
- 100% of designs indexed for comparison

---

### Workstream 1: Input Sanitization (WP01)

**Job Statement:**
**When** users submit queries, CAD files, or design parameters to ProtoLabs AI systems,
**I want to** automatically validate, sanitize, and secure all inputs before processing,
**So I can** prevent prompt injection attacks, block malicious payloads, protect proprietary algorithms, and ensure only safe, legitimate manufacturing requests are processed.

**Functional Requirements:**
- Detect and block prompt injection attempts in real-time
- Sanitize CAD file metadata before AI processing
- Validate input schema and encoding
- Enforce size limits and rate limiting
- Log all sanitization decisions for audit

**Desired Outcomes:**
- 100% of AI inputs sanitized before processing
- <10ms processing latency (negligible user impact)
- Zero successful prompt injection attacks
- <1% false positive rate (minimal legitimate request blocking)
- Complete audit trail of all sanitization decisions

---

### Workstream 2: Adversarial Defense (WP02)

**Job Statement:**
**When** AI systems process manufacturing data and generate recommendations for DFM, material selection, or CNC optimization,
**I want to** implement multi-layer defense against adversarial attacks across all input vectors,
**So I can** prevent jailbreaks, block data exfiltration attempts, stop model manipulation, protect proprietary algorithms, and ensure safe, reliable manufacturing recommendations.

**Functional Requirements:**
- Implement 5-layer defense-in-depth architecture
- Detect adversarial inputs using pattern matching (Layer 1)
- Analyze semantic intent using ML models (Layer 2)
- Profile user behavior for anomaly detection (Layer 3)
- Validate AI outputs for safety (Layer 4)
- Provide explainable detection decisions

**Desired Outcomes:**
- >98% adversarial detection rate (comprehensive coverage)
- <1% false positive rate (minimal disruption)
- <15ms processing latency per layer (real-time performance)
- 100% explainability (transparent decisions)
- Zero successful adversarial attacks (security assurance)

---

### Workstream 3: Runtime Monitoring (WP03)

**Job Statement:**
**When** AI systems operate in production manufacturing environments processing customer designs and generating recommendations,
**I want to** continuously monitor system behavior, user activity, and data access patterns in real-time,
**So I can** detect anomalies, identify insider threats, catch external attacks early, ensure system reliability, and maintain manufacturing quality without security incidents.

**Functional Requirements:**
- Collect metrics from all AI services in real-time
- Detect anomalies using statistical and ML-based methods
- Profile user behavior for baseline establishment
- Track session activity and access patterns
- Generate alerts for suspicious activity
- Provide forensic investigation capabilities

**Desired Outcomes:**
- 100% of AI services monitored (complete coverage)
- <30 second alert latency (rapid response)
- >90% anomaly detection rate (effective detection)
- <5% false positive rate (operational efficiency)
- 99.9% monitoring uptime (reliability)

---

### Workstream 4: Audit & Compliance (WP04)

**Job Statement:**
**When** Regulators, auditors, or customers request compliance evidence, or when security incidents require investigation,
**I want to** provide complete, tamper-evident audit trails of all AI system activities, decisions, and data access,
**So I can** demonstrate regulatory compliance (GDPR, CCPA, SOX, ISO 27001), avoid fines, investigate incidents, respond to data subject requests, and maintain customer trust.

---

## Strategic Decision Jobs (Pending — Gate-Dependent)

These JTBD entries represent work that **cannot begin** until upstream strategic decisions are made and prerequisite validation spikes pass. They are tracked here to ensure governance readiness when the gates open.

---

### SD-1: LMM Buy/Build Strategy Decision

**Job Statement:**
**When** ProtoLabs decides how to power its multimodal RFQ extraction and manufacturing intelligence capabilities,
**I want to** make a clear, phased buy → fine-tune → build decision with defined gate criteria,
**So I can** avoid vendor lock-in during Phase 1, capture training data from day one, and transition to a proprietary model when the data flywheel justifies the investment.

**Current Status:** 🔴 Undecided — Strategy drafted in `docs/proprietary-manufacturing-model-strategy.md` (Draft, not approved)

**Phased Approach Under Consideration:**

| Phase | Months | Approach | Decision Required |
|---|---|---|---|
| Augment | 0–6 | Buy Claude/GPT-4V for extraction; build provenance logging | Which vendor? API terms acceptable? |
| Fine-tune | 6–18 | Adapt Llama-3/Mistral on labelled pairs | Which base model? EU residency requirements? |
| Foundation | 18–36 | Own PL-LMM-Core trained on full archive | Platform readiness? Budget approval? |

**Prerequisites (Phase 0 Validation Spikes):**

| # | Spike | Pass Criteria | Owner | Status |
|---|---|---|---|---|
| 1 | Historical quotes linkable to manufactured outcomes at scale | Join key exists and works on >80% of records | Data Engineering | 🔴 Not started |
| 2 | Legacy contracts permit training use of customer CAD | >60% of contracts allow training use after NDA review | Legal | 🔴 Not started |
| 3 | ML platform can train 1B+ param model today | Infrastructure exists or can be provisioned within budget | Infra/ML Platform | 🔴 Not started |

**Dependencies:**
- **Upstream:** None — this is a root decision
- **Downstream:** SD-2 (Historical Data Pipeline), SD-3 (Governance Gap Resolution), Phase 2 fine-tuning, all model card/data card templates

**Impact if Undecided:**
- Cannot define model card templates (bought API vs. fine-tuned model vs. foundation model have different documentation requirements)
- Cannot specify training run logging standards (no training runs in Phase 1)
- Cannot design data lineage architecture (don't know what data flows where)
- Cannot budget Phase 2/3 infrastructure
- Governance framework has 3 open gaps that resolve automatically once this decision is made

**Decision Gate:** All 3 spikes must pass before Phase 1 kickoff is approved.

---

### SD-2: Historical Data Loading & Curation Pipeline

**Job Statement:**
**When** ProtoLabs needs to train or fine-tune manufacturing models on proprietary data,
**I want to** load, clean, label, and certify 20 years of historical quotes, DFM outcomes, and manufacturing results into a structured training corpus,
**So I can** create the proprietary data flywheel that no competitor can replicate and enable Phase 2 fine-tuning.

**Current Status:** 🔴 Blocked — Data exists but is unstructured; pipeline not built

**Data Assets & Gaps:**

| Data Asset | Volume | Structure | Status |
|---|---|---|---|
| Historical RFQ corpus | 100K–1M+ quotes | Semi-structured (CRM + ERP) | ✅ Exists, unstructured |
| DFM issue → outcome mapping | 10K–50K issues | Unstructured (engineer notes) | ✅ Exists, unstructured |
| Process-specific pricing signals | Embedded in ProDesk | Structured | ✅ Exists |
| Customer conversion data | 50K–200K interactions | Semi-structured (CRM) | ✅ Exists, unstructured |
| Labeled input → Order Object pairs | 500–2,000 needed | N/A | 🔴 Needs curation — Phase 1 deliverable |
| Engineer override taxonomy | 1,000+ events needed | N/A | 🔴 Needs build — Phase 1 deliverable |
| Quote → firm-quote delta | 5,000+ needed | N/A | 🟡 CRM pipeline tracking needed |
| Manufacturing outcome (actual vs. predicted) | 200–500 needed | N/A | 🟡 ERP integration needed |

**Prerequisites:**

| # | Prerequisite | Why Needed | Owner | Status |
|---|---|---|---|---|
| 1 | SD-1 decision (buy/build) | Determines what data format the pipeline must produce | AI Product | 🔴 Blocked |
| 2 | Legal review: NDA/customer-IP scoping | Cannot use customer data for training without contract clearance | Legal | 🔴 Not started |
| 3 | ITAR/EAR export-control classification | Controlled CAD must be segregated or excluded from training corpus | Legal + CISO | 🔴 Not started |
| 4 | ERP integration scope definition | Need to define which manufacturing outcome fields to extract | Data Engineering | 🟡 Discussion needed |
| 5 | Engineer override UI instrumentation | Override logging requires UI changes in review workflow | Product + Eng | 🟡 Discussion needed |

**Dependencies:**
- **Upstream:** SD-1 (LMM Strategy) — must be decided first
- **Downstream:** SD-3 (Governance Gap Resolution), Phase 2 fine-tuning, drift detection baselines, evaluation golden sets

**Impact if Not Built:**
- Phase 2 fine-tuning cannot start (needs 500–2,000 labeled pairs minimum)
- No ground truth for drift detection (can't measure if model accuracy degrades)
- No golden eval set for pre-deployment gates
- Data flywheel never starts — every quote that passes through without logging is a lost training signal
- Governance gaps (data cards, lineage, training logging) remain permanently open

---

### SD-3: Governance Gap Resolution (Data Cards, Lineage, Training Logging)

**Job Statement:**
**When** the LMM strategy is decided and the historical data pipeline is operational,
**I want to** create the three missing governance artifacts — data card templates, automated lineage specifications, and training run logging standards,
**So I can** close the remaining ~20% governance gap and achieve full ISO 42001 / EU AI Act Article 10 compliance.

**Current Status:** 🔴 Blocked — Cannot create meaningful artifacts until SD-1 and SD-2 progress

**Missing Artifacts:**

| Artifact | What It Covers | Why It Can't Be Built Now |
|---|---|---|
| **Data Card Template** | Dataset provenance, quality metrics, bias characteristics, certification status, ITAR/EAR segregation | Don't know what data sources will be in the training corpus until SD-2 defines the pipeline |
| **Automated Lineage Specification** | Data flow from source → cleaning → labeling → training → inference; GDPR Art 17 erasure capability | Don't know the pipeline architecture until SD-1 decides buy vs. build |
| **Training Run Logging Standard** | Hyperparameters, data slices, eval metrics per run, approval records, reproducibility requirements | No training runs exist in Phase 1 (buy an API); only relevant for Phase 2 fine-tuning |

**Prerequisites:**

| # | Prerequisite | Why Needed | Owner | Status |
|---|---|---|---|---|
| 1 | SD-1 decided (buy/build phase confirmed) | Determines which artifacts are needed now vs. later | AI Product | 🔴 Blocked |
| 2 | SD-2 pipeline architecture defined | Data card must reflect actual data sources and transformations | Data Engineering | 🔴 Blocked |
| 3 | ISO 42001 gap assessment refreshed | Current assessment doesn't account for LMM-specific requirements | Governance | 🟡 Can start now |

**Dependencies:**
- **Upstream:** SD-1 (LMM Strategy), SD-2 (Historical Data Pipeline)
- **Downstream:** ISO 42001 certification readiness, EU AI Act Article 10 compliance, audit evidence for high-risk classification

**Impact if Not Built:**
- ISO 42001 certification blocked (Clause 7.5 documentation requirements unmet)
- EU AI Act Article 10 (data governance) non-compliance for high-risk systems
- Audit findings on data provenance and lineage
- Cannot demonstrate GDPR Article 17 (right to erasure) compliance for training data
- ~20% of governance framework remains as open gap

**Recommended Timing:** Draft these artifacts during Phase 1 (months 3–6) so they are ready when Phase 2 fine-tuning begins.

---

### SD-4: Phase 0 Decision Gate — Governance Readiness Checkpoint

**Job Statement:**
**When** the three Phase 0 validation spikes complete,
**I want to** include a governance readiness check as a mandatory gate criterion before Phase 1 kickoff,
**So I can** ensure that data protection, compliance, and documentation requirements are not deferred indefinitely.

**Current Status:** 🔴 Not yet defined — needs to be added to the decision gate

**Proposed Gate Criteria (add to Phase 0 decision gate):**

| # | Criterion | Evidence Required | Pass Condition |
|---|---|---|---|
| G1 | Data card template drafted | Template covering all identified data sources | Template exists and is reviewed by Governance |
| G2 | Lineage architecture scoped | Document describing planned data flow from source to model | Document exists with owner assigned |
| G3 | Training logging standard drafted | Standard specifying what must be logged per training run | Standard exists (can be Phase 2-only) |
| G4 | ITAR/EAR segregation approach confirmed | Legal opinion on controlled-data handling in training corpus | Approach documented and approved by CISO |
| G5 | GDPR erasure capability designed | Architecture for selective removal of customer data from training corpus | Design documented |

**Prerequisites:**
- **Upstream:** SD-1 spikes must be in progress or complete
- **Downstream:** Phase 1 kickoff approval

**Dependencies:**
- **Upstream:** SD-1, SD-2 (in progress)
- **Downstream:** Phase 1 kickoff, ISO 42001 readiness

**Impact if Skipped:**
- Phase 2 fine-tuning starts without governance guardrails
- Retroactive compliance work is 3–5× more expensive than proactive design
- Regulatory risk: training on customer data without documented controls

**Functional Requirements:**
- Capture 100% of AI system interactions
- Maintain tamper-evident audit trails with cryptographic hashing
- Support GDPR, CCPA, SOX, and ISO 27001 compliance requirements
- Enable forensic investigation and timeline reconstruction
- Provide automated compliance reporting
- Implement 7-year retention with integrity verification
- Support data subject rights (access, erasure, portability)

**Desired Outcomes:**
- 100% event capture rate (complete visibility)
- 100% tamper-evident verification (integrity assurance)
- <100ms logging latency (performance)
- 100% compliance report accuracy (audit readiness)
- <30 day DSR response time (regulatory compliance)

---

## Emotional Jobs (How Stakeholders Want to Feel)

### For Engineering Teams

**Job Statement:**
**When** I develop and deploy AI manufacturing systems,
**I want to** feel confident that security is built-in, not bolted-on,
**So I can** focus on innovation and manufacturing excellence without constant security firefighting.

**Emotional Outcomes:**
- Confidence in system security
- Pride in responsible AI development
- Reduced anxiety about security incidents
- Trust in security processes

### For Security Teams

**Job Statement:**
**When** I protect ProtoLabs AI systems and manufacturing data,
**I want to** have comprehensive visibility, detection, and response capabilities,
**So I can** proactively defend against threats and respond effectively to incidents.

**Emotional Outcomes:**
- Control over security posture
- Visibility into threats and risks
- Confidence in detection capabilities
- Pride in protective role

### For Executive Leadership

**Job Statement:**
**When** I make strategic decisions about AI security investments,
**I want to** understand risks, costs, and benefits clearly,
**So I can** make informed decisions that protect the business and enable growth.

**Emotional Outcomes:**
- Confidence in risk management
- Trust in security leadership
- Assurance of compliance posture
- Pride in industry leadership

### For Customers

**Job Statement:**
**When** I use ProtoLabs AI manufacturing services,
**I want to** trust that my designs and data are secure,
**So I can** confidently innovate and manufacture with ProtoLabs.

**Emotional Outcomes:**
- Trust in ProtoLabs security
- Confidence in data protection
- Peace of mind for IP safety
- Loyalty to secure provider

---

## Social Jobs (How Stakeholders Want to Be Perceived)

### Industry Leadership

**Job Statement:**
**When** industry peers and customers evaluate ProtoLabs,
**I want to** be perceived as a leader in secure AI manufacturing,
**So I can** attract top customers, talent, and partnerships.

**Social Outcomes:**
- Recognition as security leader
- Competitive differentiation
- Premium pricing justification
- Talent attraction advantage

### Responsible Innovation

**Job Statement:**
**When** regulators and civil society discuss AI governance,
**I want to** be recognized for responsible AI implementation,
**So I can** influence standards and build public trust.

**Social Outcomes:**
- Regulatory influence
- Public trust building
- Ethical brand reputation
- Standards leadership

### Trusted Partner

**Job Statement:**
**When** customers choose manufacturing partners,
**I want to** be perceived as the most trustworthy option,
**So I can** win business and build long-term relationships.

**Social Outcomes:**
- Customer trust and loyalty
- Long-term contracts
- Referral business
- Partnership opportunities

---

## Desired Outcomes Summary

### Business Outcomes
1. **Risk Reduction:** 80% reduction in security risk exposure
2. **Compliance Assurance:** 100% regulatory compliance (GDPR, CCPA, SOX, ISO 27001)
3. **IP Protection:** Zero loss of proprietary algorithms or customer data
4. **Operational Continuity:** 99.9% AI system availability
5. **Customer Trust:** Maintain 95%+ customer satisfaction and retention

### Technical Outcomes
1. **Security Coverage:** 100% of AI inputs and outputs protected
2. **Detection Accuracy:** >95% threat detection, <2% false positives
3. **Performance:** <10ms latency for input sanitization, <15ms per defense layer
4. **Observability:** 100% event capture, real-time monitoring
5. **Compliance:** Automated audit trails, 7-year retention

### Organizational Outcomes
1. **Security Culture:** Security-first mindset across engineering teams
2. **Governance Maturity:** Established AI Governance Committee with clear processes
3. **Risk Awareness:** Organization-wide understanding of AI security risks
4. **Compliance Readiness:** Always-ready posture for audits and assessments
5. **Industry Leadership:** Recognition as secure AI manufacturing leader

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | April 23, 2026 | AI Governance Team | Initial JTBD framework |

**Document Owner:** AI Governance Committee  
**Last Updated:** April 23, 2026  
**Next Review:** Monthly  
**Classification:** Internal Use - Strategic Planning
