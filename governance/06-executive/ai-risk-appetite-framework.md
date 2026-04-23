# AI Risk Appetite Framework

> **Purpose:** Board-level framework for defining and communicating the organization's appetite for AI-related risks. Establishes risk tolerance statements aligned with NIST AI RMF and business strategy.

**Version:** 1.0  
**Last Updated:** 2026-04-23  
**Owner:** Board of Directors / CAIO  
**Review Cycle:** Annual, or upon significant business changes

---

## Regulatory Basis

- **NIST AI RMF 1.0** — GV-4: Risk Tolerance ("Organizations should establish risk tolerance statements")
- **EU AI Act Article 9(1)** — Risk management system proportionate to risk level
- **ISO/IEC 42001 Clause 6.1** — Actions to address risks and opportunities
- **DORA Article 5(3)** — Risk appetite for ICT risk (archived reference for framework completeness)

---

## Risk Appetite Statement

> **ProtoLabs AI Risk Appetite:**
> 
> "ProtoLabs accepts AI-related risks that are:
> - **Managed** through systematic risk assessment and mitigation
> - **Transparent** to affected stakeholders
> - **Proportionate** to business value and strategic importance
> - **Compliant** with applicable regulations (EU AI Act, GDPR, NIST AI RMF)
> - **Reversible** with defined kill-switch procedures
> 
> We have **zero appetite** for:
> - Unacceptable risk AI systems (EU AI Act Article 5)
> - Discriminatory outcomes without mitigation
> - Safety-critical failures without human oversight
> - Regulatory violations in ITAR/EAR-controlled contexts"

---

## Risk Tolerance by Category

### 1. Valid and Reliable Risk Tolerance

| Risk Level | Tolerance | Threshold | Action Required |
|------------|-----------|-----------|-----------------|
| **Accuracy degradation** | Low | <5% drop from baseline | Immediate review |
| **Consistency variance** | Medium | <10% variance | Weekly monitoring |
| **Failure rate** | Very Low | >99% success rate | Blocking issue |

**Risk Appetite Statement:**
> "We have low tolerance for accuracy degradation and very low tolerance for failure rates below 99%. DFM recommendations must be demonstrably reliable before customer-facing deployment."

---

### 2. Safety Risk Tolerance

| Risk Level | Tolerance | Threshold | Action Required |
|------------|-----------|-----------|-----------------|
| **Harm scenario occurrence** | Zero | Any occurrence | Immediate kill switch |
| **Safety test failure** | Very Low | >95% pass rate | Blocking issue |
| **Kill switch activation** | Low | <1 per quarter | Root cause analysis |

**Risk Appetite Statement:**
> "We have zero tolerance for realized harm scenarios. All high-severity harm scenarios must have documented mitigations before deployment. Kill switches must activate within 30 seconds."

---

### 3. Security and Resilience Risk Tolerance

| Risk Level | Tolerance | Threshold | Action Required |
|------------|-----------|-----------|-----------------|
| **Jailbreak success rate** | Very Low | <1% | Blocking issue |
| **Prompt injection success** | Very Low | <1% | Blocking issue |
| **Data breach** | Zero | Any occurrence | Immediate response |
| **System downtime** | Low | <99.9% availability | Incident review |

**Risk Appetite Statement:**
> "We have zero tolerance for data breaches and very low tolerance for adversarial attack success rates above 1%. System availability must exceed 99.9% for production AI systems."

---

### 4. Accountability and Transparency Risk Tolerance

| Risk Level | Tolerance | Threshold | Action Required |
|------------|-----------|-----------|-----------------|
| **Unattributed AI output** | Zero | Any occurrence | Immediate fix |
| **Missing audit trail** | Zero | Any occurrence | Compliance violation |
| **Source citation failure** | Low | <5% of outputs | Weekly review |
| **RACI ambiguity** | Low | Any unresolved | Governance escalation |

**Risk Appetite Statement:**
> "We have zero tolerance for unattributed AI outputs and missing audit trails. Every AI decision must be traceable to an accountable individual. Source citation is mandatory for all knowledge-based outputs."

---

### 5. Explainability and Interpretability Risk Tolerance

| Risk Level | Tolerance | Threshold | Action Required |
|------------|-----------|-----------|-----------------|
| **Unexplained decision** | Low | <5% of high-stakes | Review required |
| **Model card missing** | Zero | Any production system | Blocking issue |
| **Explanation quality score** | Medium | >3/5 user rating | Monthly review |

**Risk Appetite Statement:**
> "We have zero tolerance for production AI systems without model cards. High-stakes decisions must be explainable. We accept medium tolerance for explanation quality, with continuous improvement expected."

---

### 6. Privacy Risk Tolerance

| Risk Level | Tolerance | Threshold | Action Required |
|------------|-----------|-----------|-----------------|
| **PII exposure** | Zero | Any occurrence | Incident response |
| **CAD/IP leakage** | Zero | Any occurrence | Immediate kill switch |
| **DPIA missing** | Zero | Any high-risk system | Blocking issue |
| **Retention policy violation** | Low | <1% of records | Compliance review |

**Risk Appetite Statement:**
> "We have zero tolerance for PII exposure and CAD/IP leakage. Customer data protection is non-negotiable. All high-risk systems require completed DPIAs before deployment."

---

### 7. Fairness Risk Tolerance

| Risk Level | Tolerance | Threshold | Action Required |
|------------|-----------|-----------|-----------------|
| **Disparate impact** | Low | <0.8 four-fifths rule | Mitigation required |
| **Demographic parity gap** | Low | <10% difference | Review required |
| **Bias test failure** | Very Low | >95% pass rate | Blocking issue |
| **Fairness monitoring gap** | Low | <24 hours detection | Process review |

**Risk Appetite Statement:**
> "We have very low tolerance for bias test failures and low tolerance for disparate impact below the four-fifths rule. Fairness monitoring must detect issues within 24 hours."

---

## Risk Appetite by EU AI Act Risk Tier

| Risk Tier | Overall Appetite | Key Constraints |
|-----------|-----------------|-----------------|
| **Unacceptable** | **Zero** — Prohibited | No deployment under any circumstances |
| **High** | **Very Low** | Board approval required, independent validation, continuous monitoring |
| **Limited** | **Low to Medium** | Governance lead approval, periodic review, transparency controls |
| **Minimal** | **Medium** | Standard governance, annual review |

---

## Risk Appetite Governance

### Roles and Responsibilities

| Role | Responsibility |
|------|---------------|
| **Board of Directors** | Approve risk appetite framework annually |
| **CAIO** | Operationalize risk appetite, report exceptions |
| **AI Governance Committee** | Review risk tolerance breaches, recommend adjustments |
| **Risk Manager** | Monitor risk indicators, escalate breaches |
| **Product Owner** | Ensure AI systems operate within risk appetite |

### Exception Process

1. **Identify Exception** — Product Owner identifies potential risk appetite breach
2. **Document Justification** — Business value, mitigation measures, timeline
3. **Risk Assessment** — Risk Manager evaluates residual risk
4. **Escalation** — CAIO reviews; Board approval for high-risk exceptions
5. **Conditional Approval** — Time-bound with monitoring requirements
6. **Review** — Post-implementation review at exception expiry

### Monitoring and Reporting

| Metric | Frequency | Owner | Report To |
|--------|-----------|-------|-----------|
| Risk appetite adherence | Monthly | Risk Manager | CAIO |
| Exception log | Quarterly | AI Governance Committee | Board |
| Risk tolerance breaches | Immediate | CAIO | Board |
| Risk appetite framework review | Annual | Board | — |

---

## Risk Appetite Statements by Stakeholder

### For the Board
> "Our AI risk appetite prioritizes safety, compliance, and transparency. We accept managed risks that drive business value while maintaining zero tolerance for regulatory violations and customer harm."

### For Product Teams
> "Build AI systems that are valid, safe, secure, accountable, explainable, privacy-enhanced, and fair. Escalate when tradeoffs between these characteristics are required."

### For Customers
> "ProtoLabs AI systems are designed with your safety and privacy in mind. We maintain human oversight for high-stakes decisions and provide transparency about AI use."

### For Regulators
> "ProtoLabs maintains a documented AI risk management system aligned with NIST AI RMF and EU AI Act requirements. Risk tolerance is proportionate to risk tier and business context."

---

## Cross-References

- [NIST AI RMF Reference Guide](../05-cross-cutting/nist-ai-rmf-reference-guide.md) — NIST AI RMF GV-4 guidance
- [Quarterly Governance Report](./quarterly-governance-report.md) — Risk appetite reporting template
- [Governance Maturity Roadmap](../07-enterprise-implementation/risk-based-adoption/governance-maturity-roadmap.md) — Risk-based adoption
- [EU AI Act Risk Classification](../01-discovery-governance/checklists/eu-ai-act-risk-classification.yaml) — Risk tier determination

---

*Last updated: 2026-04-23 / Version: 1.0 / Classification: Board Level*
