# Problem Statements for ProtoLabs AI Governance

## Executive Summary

This document defines the specific problems that the AI Governance implementation workstreams are designed to solve. Each problem statement follows the format: **Problem** → **Impact** → **Evidence** → **Success Criteria**.

---

## 🔴 P0 - Critical Problems (Must Resolve Immediately)

### P0-CAD-1: Manual DFM Analysis Bottleneck

**Problem Statement:**
ProtoLabs currently relies on manual engineering review for Design for Manufacturability (DFM) analysis of CAD uploads, creating a bottleneck that limits quote velocity, increases labor costs, and introduces inconsistency in evaluation quality across reviewers.

**Impact:**
- **Delayed Quotes:** Manual DFM review adds hours to quote turnaround, reducing win rates
- **Inconsistent Quality:** Different engineers apply DFM rules inconsistently
- **Scalability Limitation:** Linear relationship between volume and staffing costs
- **Knowledge Silos:** DFM expertise concentrated in senior engineers
- **24/7 Coverage Gaps:** No DFM review outside business hours
- **Customer Friction:** Slow feedback loop delays design iteration

**Evidence:**
- Average DFM review time: 2-4 hours per complex part
- Quote turnaround target: 24 hours; actual: 48-72 hours for complex parts
- Customer complaints about slow quotes: 15% of negative feedback
- Engineer turnover leads to DFM knowledge loss
- Peak upload times (evenings/weekends) have next-day delays
- Inconsistent DFM feedback documented in customer surveys

**Success Criteria:**
- ✅ <60 seconds automated DFM analysis for typical parts
- ✅ >95% accuracy vs. expert engineer review
- ✅ 100% consistency in rule application
- ✅ 24/7 availability with no coverage gaps
- ✅ 40% reduction in design iterations
- ✅ 50% reduction in quote turnaround time

**Related Work Package:** WP-CAD - CAD AI Evaluation System

---

### P0-CAD-2: No Automated CAD Feature Extraction

**Problem Statement:**
ProtoLabs lacks automated capability to extract manufacturing-relevant features (holes, pockets, bosses, threads, thin walls) from uploaded CAD files, requiring manual measurement and interpretation that is slow, error-prone, and inconsistent.

**Impact:**
- **Manual Measurement Overhead:** Engineers manually measure CAD features
- **Error-Prone Process:** Human measurement introduces errors
- **Incomplete Analysis:** Time constraints limit feature inspection depth
- **Inconsistent Documentation:** Feature lists vary by reviewer
- **Delayed Issue Detection:** Features causing issues discovered late
- **Missed Optimization:** Opportunities for design improvement overlooked

**Evidence:**
- Feature measurement takes 30-60 minutes per complex part
- Feature measurement errors found in 8% of reviewed quotes
- Incomplete feature lists in 25% of DFM reports
- Customer complaints about missed manufacturability issues
- Post-quote design changes due to late-discovered features
- No standardized feature extraction methodology

**Success Criteria:**
- ✅ 100% of relevant features automatically extracted
- ✅ >95% precision in feature detection
n- ✅ <5 second feature extraction time
- ✅ Standardized feature taxonomy across all processes
- ✅ Complete feature documentation for every upload
- ✅ Zero missed critical features

**Related Work Package:** WP-CAD - CAD AI Evaluation System

---

### P0-CAD-3: No Visual AI Understanding of CAD Designs

**Problem Statement:**
ProtoLabs AI systems cannot visually interpret CAD designs to assess manufacturability, missing nuanced issues that require human-like visual reasoning and preventing automated explanation generation that customers can understand.

**Impact:**
- **Missed Edge Cases:** Rule-based systems miss visual anomalies
- **Poor Explanation Quality:** Technical outputs not customer-friendly
- **High Support Burden:** Customers need help interpreting DFM reports
- **Slow Learning Curve:** New engineers need extensive training
- **Inconsistent Communication:** Different engineers explain issues differently
- **Accessibility Gap:** Non-experts cannot self-serve DFM understanding

**Evidence:**
- 30% of DFM issues caught by visual inspection, not rules
- Customer support tickets: 40% request DFM explanation help
- New engineer ramp-up time: 6 months to independent DFM review
- Customer survey: 60% want better DFM explanation clarity
- No automated explanation generation currently exists
- Inconsistent DFM report formats across engineers

**Success Criteria:**
- ✅ VLM catches >25% of issues that rules miss
- ✅ DFM explanations rated >4.0/5.0 for clarity
- ✅ 50% reduction in DFM explanation support tickets
- ✅ New engineer ramp-up reduced to 2 months
- ✅ 100% consistent explanation format
- ✅ Self-service DFM understanding for non-experts

**Related Work Package:** WP-CAD - CAD AI Evaluation System

---

### P0-1: Unprotected AI Input Processing

**Problem Statement:**
ProtoLabs AI systems currently process user queries, CAD file uploads, and manufacturing parameters without comprehensive input validation or sanitization, creating a direct attack vector for prompt injection, data exfiltration, and system manipulation.

**Impact:**
- **Intellectual Property Theft:** Attackers could extract proprietary DFM algorithms through prompt injection
- **Data Exfiltration:** Customer CAD files and manufacturing data could be stolen
- **System Manipulation:** Manufacturing recommendations could be altered, leading to defective parts
- **Regulatory Violations:** GDPR, CCPA, and ISO 27001 require data protection controls
- **Reputational Damage:** Security breaches would erode customer trust and competitive position

**Evidence:**
- Current AI endpoints accept raw user input without validation
- No detection of prompt injection attempts in existing logs
- No sanitization of CAD file metadata before processing
- Security audit identified input validation as critical gap
- Industry reports show 73% of AI systems vulnerable to prompt injection

**Success Criteria:**
- ✅ 100% of AI inputs sanitized before processing
- ✅ <10ms processing latency (negligible user impact)
- ✅ Zero successful prompt injection attacks
- ✅ <1% false positive rate (minimal legitimate request blocking)
- ✅ Complete audit trail of all sanitization decisions
- ✅ CAD file metadata automatically sanitized

**Related Work Package:** WP01 - Input Sanitization Layer

---

### P0-2: No Adversarial Defense System

**Problem Statement:**
ProtoLabs AI systems lack comprehensive defense against adversarial attacks, including prompt injection, jailbreaks, data exfiltration attempts, and model manipulation, leaving manufacturing recommendations, proprietary algorithms, and customer data vulnerable to sophisticated attacks.

**Impact:**
- **Model Theft:** Attackers could reverse-engineer proprietary ML models
- **Algorithm Extraction:** DFM optimization algorithms could be stolen
- **Training Data Exposure:** Sensitive manufacturing data could be extracted
- **Recommendation Manipulation:** CNC parameters could be altered causing defects
- **Competitive Disadvantage:** Stolen IP could benefit competitors
- **Customer Data Breach:** CAD files and proprietary designs could be exfiltrated

**Evidence:**
- No multi-layer defense architecture in current systems
- No detection of jailbreak attempts or model extraction attacks
- Security testing demonstrated vulnerability to adversarial inputs
- Industry research shows 89% of AI systems lack adversarial defenses
- Competitor intelligence indicates active targeting of manufacturing AI

**Success Criteria:**
- ✅ >98% adversarial detection rate (comprehensive coverage)
- ✅ <1% false positive rate (minimal operational disruption)
- ✅ <15ms processing latency per layer (real-time performance)
- ✅ 100% explainability (transparent decision-making)
- ✅ Zero successful adversarial attacks (security assurance)
- ✅ 5-layer defense-in-depth architecture (defense in depth)

**Related Work Package:** WP02 - Adversarial Defense System

---

### P0-3: Audit and Compliance Gap

**Problem Statement:**
ProtoLabs lacks comprehensive, tamper-evident audit trails for AI system activities, decisions, and data access, creating regulatory compliance risks under GDPR, CCPA, SOX, and ISO 27001, and preventing effective incident investigation and customer data request fulfillment.

**Impact:**
- **Regulatory Fines:** GDPR fines up to 4% of annual revenue, CCPA fines up to $7,500 per violation
- **Legal Liability:** Inability to provide evidence in legal proceedings
- **Customer Trust Loss:** Customers cannot verify data handling practices
- **Audit Failures:** ISO 27001, SOX audits may fail without audit trails
- **Incident Investigation Failure:** Cannot reconstruct security incidents
- **Data Subject Rights Violations:** Cannot fulfill GDPR/CCPA access/erasure requests

**Evidence:**
- No comprehensive audit logging in current AI systems
- No tamper-evident log storage or integrity verification
- Cannot demonstrate compliance with GDPR Article 30 (Records of Processing)
- No automated compliance reporting capability
- Security incidents cannot be fully reconstructed
- Customer data requests require manual log searches

**Success Criteria:**
- ✅ 100% event capture rate (complete visibility)
- ✅ 100% tamper-evident verification (integrity assurance)
- ✅ <100ms logging latency (performance)
- ✅ 100% compliance report accuracy (audit readiness)
- ✅ <30 day DSR response time (regulatory compliance)
- ✅ 7-year retention with automated lifecycle management

**Related Work Package:** WP04 - Audit & Compliance Logging

---

### P0-4: Runtime Monitoring Blind Spot

**Problem Statement:**
ProtoLabs has no real-time visibility into AI system behavior, user activity patterns, or anomalous operations, preventing early detection of insider threats, external attacks, system malfunctions, or data exfiltration that could impact manufacturing quality and security.

**Impact:**
- **Delayed Threat Detection:** Attacks go undetected for weeks or months
- **Insider Threats:** Malicious or negligent employees can exfiltrate data undetected
- **System Failures:** AI model drift or errors not caught until quality issues arise
- **Data Exfiltration:** Gradual data theft through seemingly normal queries
- **Compliance Violations:** Undetected unauthorized data access
- **Reputation Damage:** Public disclosure of undetected breaches

**Evidence:**
- No real-time monitoring of AI service behavior
- No user behavior analytics or profiling
- No anomaly detection for unusual access patterns
- Security incidents discovered weeks after occurrence
- No alerting for suspicious activity
- Industry average breach detection time: 287 days

**Success Criteria:**
- ✅ 100% of AI services monitored (complete coverage)
- ✅ <30 second alert latency (rapid response)
- ✅ >90% anomaly detection rate (effective detection)
- ✅ <5% false positive rate (operational efficiency)
- ✅ 99.9% monitoring uptime (reliability)
- ✅ Behavioral baselines for 100% of active users

**Related Work Package:** WP03 - Runtime Monitoring & Behavioral Analysis

---

## 🟡 P1 - High Priority Problems

### P1-1: Flat Network Architecture

**Problem Statement:**
ProtoLabs' current network architecture lacks segmentation between AI services, manufacturing systems, and corporate networks, allowing attackers who compromise any single component to move laterally and access sensitive systems and data.

**Impact:**
- **Expanded Breach Impact:** Single compromise leads to widespread access
- **Compliance Violations:** PCI DSS, ISO 27001 require network segmentation
- **Insider Threat Amplification:** Employees can access systems beyond their role
- **Ransomware Propagation:** Malware spreads easily across flat network
- **Data Exfiltration:** Attackers can reach sensitive data from any entry point

**Evidence:**
- No micro-segmentation between AI services
- Manufacturing systems on same network as corporate IT
- No zero-trust access controls
- Security audit identified network segmentation as critical gap
- Industry best practice: zero-trust architecture for AI systems

**Success Criteria:**
- ✅ Zero-trust architecture implemented
- ✅ Micro-segmentation between all services
- ✅ mTLS for all service-to-service communication
- ✅ Identity-based access controls
- ✅ Network policies enforcing least privilege
- ✅ 80% reduction in blast radius of breaches

**Related Agenda:** Zero-Trust Architecture Implementation

---

### P1-2: Insider Threat Blindness

**Problem Statement:**
ProtoLabs lacks capability to detect malicious or negligent insider activity, leaving proprietary DFM algorithms, customer CAD files, and manufacturing data vulnerable to theft, sabotage, or accidental exposure by employees, contractors, or partners.

**Impact:**
- **IP Theft:** Employees can steal proprietary algorithms undetected
- **Data Exfiltration:** Customer CAD files can be copied without detection
- **Sabotage:** Manufacturing parameters could be altered to cause defects
- **Competitive Intelligence:** Departing employees can take trade secrets
- **Regulatory Violations:** Undetected unauthorized data access
- **Reputation Damage:** Insider breaches are highly publicized

**Evidence:**
- No user behavior analytics (UBA) capability
- No data loss prevention (DLP) monitoring
- No privileged access monitoring
- Security incidents involving insiders discovered after departure
- Industry statistics: 60% of data breaches involve insiders

**Success Criteria:**
- ✅ User behavior analytics for 100% of users
- ✅ Behavioral baselines established for all users
- ✅ DLP monitoring for sensitive data
- ✅ Privileged access monitoring for admins
- ✅ >85% insider threat detection rate
- ✅ <24 hour detection time for insider activity

**Related Agenda:** Insider Threat Program Implementation

---

### P1-3: Nation-State Exposure

**Problem Statement:**
ProtoLabs lacks countermeasures against advanced persistent threat (APT) groups and nation-state actors targeting manufacturing intellectual property, exposing critical DFM algorithms, material databases, and supply chain to economic espionage and strategic compromise.

**Impact:**
- **Algorithm Theft:** Nation-states can steal proprietary ML models
- **Economic Espionage:** Competitor nations can benefit from stolen IP
- **Supply Chain Compromise:** Adversaries can infiltrate through vendors
- **Strategic Disadvantage:** Loss of competitive manufacturing capabilities
- **National Security:** Critical manufacturing technology exposed
- **Long-term Competitiveness:** Irreversible loss of IP advantage

**Evidence:**
- No threat intelligence integration
- No APT detection capabilities
- No air-gapped systems for critical IP
- Industry reports of manufacturing IP theft by nation-states
- FBI warnings about APT targeting of manufacturing sector

**Success Criteria:**
- ✅ Threat intelligence integration (commercial and government feeds)
- ✅ APT detection capabilities with behavioral analysis
- ✅ Air-gapped systems for critical algorithms (if approved)
- ✅ Supply chain security program
- ✅ Personnel security enhancements
- ✅ Government coordination (if required)

**Related Agenda:** Nation-State Countermeasures Implementation

---

## 🟢 P2 - Medium Priority Problems

### P2-1: Manual Compliance Reporting

**Problem Statement:**
ProtoLabs compliance teams manually compile reports for GDPR, CCPA, SOX, and ISO 27001, creating delays, errors, resource waste, and audit inefficiencies that increase compliance risk and operational cost.

**Impact:**
- **Delayed Audits:** Manual compilation takes weeks, delaying audit schedules
- **Compliance Gaps:** Manual processes prone to errors and omissions
- **Resource Waste:** Senior staff spend time on manual report generation
- **Audit Inefficiencies:** Auditors wait for reports, increasing audit costs
- **Delayed Response:** Slow response to regulatory inquiries

**Evidence:**
- Compliance reports take 2-3 weeks to compile manually
- Errors discovered in past compliance submissions
- Staff complaints about repetitive manual work
- Audit delays due to report preparation time
- Industry best practice: automated compliance reporting

**Success Criteria:**
- ✅ Automated GDPR Article 30 reports
- ✅ Automated CCPA consumer rights tracking
- ✅ Automated SOX IT general controls evidence
- ✅ Automated ISO 27001 audit evidence collection
- ✅ <24 hour report generation time
- ✅ 100% report accuracy

**Related Work Package:** WP04 - Audit & Compliance (enhancement)

---

### P2-2: Siloed Security Tools

**Problem Statement:**
ProtoLabs security capabilities are fragmented across multiple disconnected tools and manual processes, creating visibility gaps, operational inefficiencies, slow incident response, and high operational costs.

**Impact:**
- **Visibility Gaps:** Disconnected tools create blind spots in security posture
- **Slow Response:** Manual correlation between tools delays incident response
- **Operational Inefficiency:** Security team context switches between tools
- **High Cost:** Multiple tool licenses, training, and maintenance
- **Alert Fatigue:** Duplicate alerts from different tools overwhelm analysts

**Evidence:**
- Security team uses 8+ different tools with no integration
- Incident response requires manual log correlation across tools
- Duplicate alerts from different security tools
- Security analyst complaints about tool fragmentation
- Industry trend: integrated security platforms (XDR, SIEM)

**Success Criteria:**
- ✅ Unified security dashboard
- ✅ Integrated threat detection and response
- ✅ Single pane of glass for security operations
- ✅ Automated alert correlation and deduplication
- ✅ Unified reporting across security domains
- ✅ 50% reduction in security tool count

**Related Agenda:** Security Platform Integration (future initiative)

---

## 🔴 P0-STRATEGIC - Blocking Strategic Decisions

These problems are **upstream blockers** — they prevent governance artifacts, data pipelines, and Phase 2 model development from proceeding. They are higher priority than P1 because P1 items depend on them.

---

### P0-STRAT-1: LMM Buy/Build Strategy Undecided

**Problem Statement:**
ProtoLabs has not yet made a formal decision on how to power its multimodal RFQ extraction and manufacturing intelligence capabilities — whether to buy commodity LLM APIs, fine-tune open-source models, or build a proprietary foundation model. The strategy is drafted (`docs/proprietary-manufacturing-model-strategy.md`) but not approved, and the three Phase 0 validation spikes have not started.

**Impact:**
- **Governance Gaps:** Cannot create data card templates, automated lineage specs, or training run logging standards (don't know what to template)
- **Model Card Ambiguity:** Bought API vs. fine-tuned model vs. foundation model require fundamentally different documentation
- **Budget Uncertainty:** Cannot forecast Phase 2/3 infrastructure costs without a decision
- **Vendor Lock-in Risk:** Every month of indecision deepens dependency on commodity LLM providers
- **Competitive Delay:** Competitors with proprietary manufacturing models gain advantage

**Evidence:**
- Strategy doc marked "Draft — for workshop discussion"
- Three validation spikes (quote join key, contract NDA review, ML platform readiness) not started
- Governance framework has 3 documented gaps traceable to this decision
- No approved budget for Phase 2/3 infrastructure

**Success Criteria:**
- ✅ Phase 0 validation spike #1 complete (quote-to-outcome join validated)
- ✅ Phase 0 validation spike #2 complete (contract NDA/legal review done)
- ✅ Phase 0 validation spike #3 complete (ML platform readiness confirmed)
- ✅ Formal go/no-go decision documented and approved
- ✅ Phase 1 vendor selection finalized (if go)

**Related JTBD:** SD-1 (LMM Buy/Build Strategy Decision)

---

### P0-STRAT-2: Historical Data Pipeline Not Built

**Problem Statement:**
ProtoLabs possesses 20 years of valuable manufacturing data (quotes, DFM outcomes, pricing signals, conversion data) but has no pipeline to load, clean, label, and certify this data into a structured training corpus. The data exists in semi-structured form across CRM, ERP, and ProDesk but cannot be used for model training without curation.

**Impact:**
- **Phase 2 Blocked:** Fine-tuning requires 500–2,000 labeled pairs — none exist yet
- **No Ground Truth:** Drift detection has no baseline to measure against
- **No Golden Eval Set:** Pre-deployment gates cannot validate model accuracy
- **Lost Training Signals:** Every quote processed without logging is a permanently lost data point
- **Data Flywheel Delayed:** The compounding advantage never starts

**Evidence:**
- Strategy doc explicitly lists 4 data gaps as "Needs curation" or "Needs build"
- Funnel intake marks NDA review and ITAR classification as 🔴 Blocked
- No ERP integration scope defined
- No engineer override UI instrumentation planned

**Success Criteria:**
- ✅ Legal review of training-data permissions complete
- ✅ ITAR/EAR segregation approach confirmed
- ✅ ERP integration scope defined
- ✅ Engineer override logging instrumented in review UI
- ✅ First 500 labeled (input → Order Object) pairs curated
- ✅ Data pipeline architecture documented

**Related JTBD:** SD-2 (Historical Data Loading & Curation Pipeline)

---

### P0-STRAT-3: Governance Artifacts Cannot Be Created (Data Cards, Lineage, Training Logging)

**Problem Statement:**
Three governance artifacts required for ISO 42001 and EU AI Act Article 10 compliance cannot be meaningfully created because the underlying data pipeline and model strategy are undefined: data card templates, automated lineage specifications, and training run logging standards.

**Impact:**
- **ISO 42001 Blocked:** Clause 7.5 documentation requirements unmet
- **EU AI Act Non-Compliance:** Article 10 (data governance) cannot be demonstrated for high-risk systems
- **Audit Risk:** No data provenance or lineage evidence for auditors
- **GDPR Risk:** Cannot demonstrate Article 17 (right to erasure) capability for training data
- **~20% Governance Gap:** Framework coverage stuck at ~80% until resolved

**Evidence:**
- Governance assessment identified 3 specific gaps
- Model card template exists but data card template does not
- Lineage is documented manually, not automated
- No training run logging standard exists

**Success Criteria:**
- ✅ Data card template drafted and reviewed by Governance
- ✅ Automated lineage architecture scoped with owner assigned
- ✅ Training run logging standard drafted (can be Phase 2-only)
- ✅ ISO 42001 gap assessment refreshed to reflect LMM-specific requirements
- ✅ GDPR erasure capability designed

**Related JTBD:** SD-3 (Governance Gap Resolution)

---

### P0-STRAT-4: Phase 0 Decision Gate Missing Governance Criteria

**Problem Statement:**
The Phase 0 decision gate (which green-lights Phase 1 kickoff) currently validates only technical and legal spikes but does not include governance readiness criteria. Without this, Phase 2 fine-tuning could start without governance guardrails, creating retroactive compliance work that is 3–5× more expensive than proactive design.

**Impact:**
- **Retroactive Compliance Cost:** Fixing governance gaps after Phase 2 starts is 3–5× more expensive
- **Regulatory Risk:** Training on customer data without documented controls
- **Audit Findings:** Auditors will flag absence of governance gate criteria
- **Process Integrity:** Decision gate should be holistic, not just technical

**Evidence:**
- Current gate criteria cover only 3 validation spikes (technical/legal)
- No governance readiness check in the gate
- Industry best practice: governance gates embedded in ML lifecycle

**Success Criteria:**
- ✅ Governance readiness criteria added to Phase 0 decision gate
- ✅ Gate includes: data card template, lineage scope, training logging standard, ITAR approach, GDPR erasure design
- ✅ Gate criteria reviewed and approved by AI Governance Committee

**Related JTBD:** SD-4 (Phase 0 Decision Gate — Governance Readiness Checkpoint)

---

## Summary: Problem Priority Matrix

| Priority | Problem ID | Problem Statement | Business Impact | Technical Complexity | Timeline |
|----------|------------|-------------------|-----------------|---------------------|----------|
| **P0-STRAT** | P0-STRAT-1 | LMM Buy/Build Strategy Undecided | Critical | High | Immediate |
| **P0-STRAT** | P0-STRAT-2 | Historical Data Pipeline Not Built | Critical | High | Immediate |
| **P0-STRAT** | P0-STRAT-3 | Governance Artifacts Blocked | Critical | Low | Immediate |
| **P0-STRAT** | P0-STRAT-4 | Decision Gate Missing Governance Criteria | Critical | Low | Immediate |
| **P0** | P0-1 | Unprotected AI Inputs | Critical | Low | Immediate |
| **P0** | P0-2 | No Adversarial Defense | Critical | Medium | Immediate |
| **P0** | P0-3 | Audit & Compliance Gap | Critical | Low | Immediate |
| **P0** | P0-4 | Runtime Monitoring Blind Spot | Critical | Medium | Immediate |
| **P1** | P1-1 | Flat Network Architecture | High | High | 30 days |
| **P1** | P1-2 | Insider Threat Blindness | High | Medium | 60 days |
| **P1** | P1-3 | Nation-State Exposure | High | High | 90 days |
| **P2** | P2-1 | Manual Compliance Reporting | Medium | Low | 90 days |
| **P2** | P2-2 | Siloed Security Tools | Medium | Medium | 120 days |

---

## Dependency Chain

```
P0-STRAT-1 (LMM Strategy Decision)
    │
    ├──► P0-STRAT-2 (Historical Data Pipeline)
    │        │
    │        ├──► P0-STRAT-3 (Governance Artifacts)
    │        │        │
    │        │        └──► ISO 42001 / EU AI Act Art 10 compliance
    │        │
    │        └──► Phase 2 Fine-Tuning (500-2000 labeled pairs)
    │
    └──► P0-STRAT-4 (Decision Gate Update)
             │
             └──► Phase 1 Kickoff Approval
```

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | April 23, 2026 | AI Governance Team | Initial problem statements |
| 1.1 | April 28, 2026 | AI Governance Team | Added P0-STRAT-1 through P0-STRAT-4 (strategic decision blockers) |

**Document Owner:** AI Governance Committee  
**Last Updated:** April 28, 2026  
**Next Review:** Bi-weekly during implementation  
**Classification:** Internal Use - Strategic Planning
