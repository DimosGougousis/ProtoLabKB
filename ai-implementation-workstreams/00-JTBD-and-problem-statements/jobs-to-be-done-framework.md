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
