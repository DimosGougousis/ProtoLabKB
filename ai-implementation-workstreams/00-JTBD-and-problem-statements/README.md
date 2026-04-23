# Jobs to be Done (JTBD) & Problem Statements

## Primary Job Statement

**When** ProtoLabs engineers and customers use AI-powered manufacturing tools to design and produce parts,
**I want to** ensure these AI systems are secure, compliant, and trustworthy throughout the entire manufacturing lifecycle,
**So I can** protect intellectual property, maintain customer trust, meet regulatory requirements, and deliver high-quality manufacturing outcomes without security incidents.

---

## Functional Jobs (What Users Need to Accomplish)

### F1: Secure AI Input Processing
**When** I submit manufacturing queries, CAD files, or design parameters to AI systems,
**I want to** ensure all inputs are validated and sanitized before processing,
**So I can** prevent prompt injection attacks, data exfiltration, and system manipulation.

**Success Metrics:**
- 100% of AI inputs sanitized
- <10ms processing latency
- Zero successful prompt injections
- <1% false positive rate

---

### F2: Defend Against Adversarial Attacks
**When** AI systems process manufacturing data and generate recommendations,
**I want to** detect and block adversarial inputs across multiple attack vectors,
**So I can** maintain system integrity, prevent IP theft, and ensure safe manufacturing outcomes.

**Success Metrics:**
- >98% adversarial detection rate
- <1% false positive rate
- <15ms processing per layer
- 100% explainability coverage

---

### F3: Monitor System Behavior
**When** AI systems operate in production manufacturing environments,
**I want to** continuously monitor behavior, detect anomalies, and track user activity,
**So I can** identify insider threats, external attacks, and system malfunctions in real-time.

**Success Metrics:**
- 100% system coverage
- <30 second alert latency
- >90% anomaly detection rate
- <5% false positive rate

---

### F4: Maintain Audit Compliance
**When** Regulators, auditors, or customers request compliance evidence,
**I want to** provide complete, tamper-evident audit trails of all AI system activities,
**So I can** demonstrate regulatory compliance (GDPR, CCPA, SOX, ISO 27001), avoid fines, and maintain customer trust.

**Success Metrics:**
- 100% event capture
- 100% tamper-evident verification
- 7-year retention compliance
- <100ms logging latency

---

## Emotional Jobs (How Users Want to Feel)

### E1: Confidence in Security
**When** I use AI manufacturing tools,
**I want to** feel confident that my intellectual property and data are secure,
**So I can** focus on innovation without worrying about security breaches.

### E2: Trust in Compliance
**When** regulators audit our AI systems,
**I want to** feel assured that we meet all compliance requirements,
**So I can** demonstrate our commitment to ethical AI and data protection.

### E3: Control Over Risk
**When** managing AI security risks,
**I want to** feel in control with clear visibility and actionable insights,
**So I can** make informed decisions and respond quickly to threats.

---

## Social Jobs (How Users Want to Be Perceived)

### S1: Industry Leadership
**When** customers evaluate our AI manufacturing capabilities,
**I want to** be perceived as a security and compliance leader,
**So I can** win business against competitors and build long-term trust.

### S2: Responsible Innovation
**When** industry peers discuss AI governance,
**I want to** be recognized for responsible AI implementation,
**So I can** influence industry standards and attract top talent.

---

## Problem Statements by Priority

### 🔴 P0 - Critical Problems (Must Resolve Immediately)

| ID | Problem Statement | Impact | Evidence | Success Criteria |
|----|-------------------|--------|----------|------------------|
| P0-1 | **Unprotected AI Inputs:** ProtoLabs AI systems currently process user inputs without validation, making them vulnerable to prompt injection attacks that could exfiltrate proprietary DFM algorithms or manipulate manufacturing recommendations. | Loss of IP, production errors, regulatory violations | No input validation on current AI endpoints | 100% input sanitization, <10ms latency, zero successful injections |
| P0-2 | **No Adversarial Defense:** Manufacturing AI systems lack multi-layer defense against adversarial attacks, leaving them exposed to jailbreaks, data exfiltration, and model manipulation that could compromise part quality or steal customer CAD data. | IP theft, data breaches, safety incidents | No adversarial detection in current systems | >98% detection rate, <1% false positives, <15ms per layer |
| P0-3 | **Audit Compliance Gap:** ProtoLabs cannot demonstrate comprehensive audit trails for AI system decisions, creating regulatory compliance risks under GDPR, CCPA, and ISO 27001, and inability to investigate security incidents or respond to customer data requests. | Regulatory fines, legal liability, customer trust loss | No comprehensive audit logging | 100% event capture, 7-year retention, tamper-evident |
| P0-4 | **Monitoring Blind Spot:** No real-time monitoring of AI system behavior, user activity, or anomalous patterns, preventing early detection of insider threats, external attacks, or system malfunctions that could impact manufacturing quality. | Delayed threat detection, insider threats, system failures | No runtime monitoring | 100% coverage, <30s alert latency, >90% detection |

### 🟡 P1 - High Priority Problems

| ID | Problem Statement | Impact | Evidence | Success Criteria |
|----|-------------------|--------|----------|------------------|
| P1-1 | **Flat Network Architecture:** Current network lacks segmentation between AI services, manufacturing systems, and corporate networks, allowing lateral movement for attackers who breach any single component. | Expanded breach impact, compliance violations | No micro-segmentation | Zero-trust architecture, micro-segmentation |
| P1-2 | **Insider Threat Blindness:** No capability to detect malicious or negligent insider activity, leaving proprietary DFM algorithms and customer data vulnerable to employee theft or accidental exposure. | IP theft, data breaches, sabotage | No UBA or insider threat detection | Behavioral analytics, anomaly detection |
| P1-3 | **Nation-State Exposure:** Advanced persistent threat (APT) groups targeting manufacturing IP have no countermeasures at ProtoLabs, exposing critical algorithms and supply chain to economic espionage. | Loss of competitive advantage, national security implications | No APT countermeasures | Threat intel, air-gapped systems, countermeasures |

### 🟢 P2 - Medium Priority Problems

| ID | Problem Statement | Impact | Evidence | Success Criteria |
|----|-------------------|--------|----------|------------------|
| P2-1 | **Manual Compliance Reporting:** Compliance reports for GDPR, CCPA, SOX, and ISO 27001 are manually compiled, creating delays, errors, and audit inefficiencies. | Delayed audits, compliance gaps, resource waste | Manual report generation | Automated compliance reports |
| P2-2 | **Siloed Security Tools:** Security capabilities are fragmented across multiple disconnected tools, creating visibility gaps and operational inefficiencies. | Visibility gaps, slow response, high operational cost | Disconnected tools | Integrated security platform |

---

## 📊 Objectives & Key Results (OKRs)

### Q2 2026 Objectives

**Objective 1: Deploy Foundation Security Controls**
- **KR1.1:** Deploy input sanitization (WP01) by Week 2
- **KR1.2:** Deploy adversarial defense (WP02) by Week 4
- **KR1.3:** Deploy runtime monitoring (WP03) by Week 6
- **KR1.4:** Deploy audit logging (WP04) by Week 8

**Objective 2: Achieve Security Baseline Metrics**
- **KR2.1:** 100% AI input coverage with sanitization
- **KR2.2:** <10ms average processing latency
- **KR2.3:** >95% threat detection rate
- **KR2.4:** <2% false positive rate

**Objective 3: Complete Strategic Decisions**
- **KR3.1:** Zero-trust architecture decision by Week 4
- **KR3.2:** Adversarial defense system decision by Week 6
- **KR3.3:** Insider threat program decision by Week 10
- **KR3.4:** Nation-state countermeasures decision by Week 14

---

## 🎯 Success Criteria

### Definition of "Done" for Agentic-Ready Work

A work package is truly **agentic-ready** when:

1. ✅ **Code Complete:** All code is implemented, not truncated
2. ✅ **Tested:** Unit tests and integration tests passing
3. ✅ **Documented:** API docs, runbooks, and deployment guides
4. ✅ **Infrastructure Defined:** Docker, K8s, CI/CD configurations
5. ✅ **Acceptance Criteria Met:** All measurable criteria validated
6. ✅ **Security Reviewed:** No hardcoded secrets, proper auth
7. ✅ **Performance Validated:** Latency claims benchmarked

### Current Status vs. Definition of Done

| Work Package | Code Complete | Tested | Infrastructure | Security | Performance | **Truly Ready?** |
|--------------|---------------|--------|----------------|----------|-------------|------------------|
| WP01 Input Sanitization | ❌ No | ❌ No | ❌ No | ⚠️ Partial | ❌ No | **🔴 NO** |
| WP02 Adversarial Defense | ❌ No | ❌ No | ❌ No | ⚠️ Partial | ❌ No | **🔴 NO** |
| WP03 Runtime Monitoring | ❌ No | ❌ No | ❌ No | ⚠️ Partial | ❌ No | **🔴 NO** |
| WP04 Audit & Compliance | ❌ No | ❌ No | ❌ No | ⚠️ Partial | ❌ No | **🔴 NO** |

**Verdict:** None of the work packages are truly agentic-ready in their current state. They require 2-3 weeks of engineering work to meet the definition of done.