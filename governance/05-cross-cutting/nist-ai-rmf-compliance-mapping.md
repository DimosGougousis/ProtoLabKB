# NIST AI RMF Compliance Mapping

> **Purpose:** Cross-reference mapping between NIST AI RMF requirements and other regulatory frameworks (EU AI Act, ISO/IEC 42001, NIST CSF 2.0, Colorado AI Act). Enables multi-framework compliance demonstration.

**Version:** 1.0  
**Last Updated:** 2026-04-23  
**Owner:** ProtoLabs AI Governance Office  
**Review Cycle:** Quarterly, or upon regulatory updates

---

## Regulatory Basis

- **NIST AI RMF 1.0** — Artificial Intelligence Risk Management Framework
- **EU AI Act (Regulation 2024/1689)** — Risk Management System (Article 9)
- **ISO/IEC 42001:2023** — AI Management System (AIMS)
- **NIST CSF 2.0** — Cybersecurity Framework
- **Colorado AI Act (SB 24-205)** — Algorithmic discrimination prevention

---

## NIST AI RMF Functions → Multi-Framework Mapping

### GOVERN Function Cross-Mapping

| NIST AI RMF | EU AI Act | ISO/IEC 42001 | NIST CSF 2.0 | Colorado AI Act |
|-------------|-----------|---------------|--------------|-----------------|
| **GV-1.1** Legal requirements | Art 9(1) | Clause 4.1 | GV.PO | Section 6-1-1701(2) |
| **GV-1.2** Accountability | Art 14(1) | Clause 5.2 | GV.AT | Section 6-1-1701(3) |
| **GV-2.1** Risk culture | Art 9(2) | Clause 5.1 | GV.PO | — |
| **GV-3.1** Workforce diversity | — | Clause 7.1 | GV.PO | — |
| **GV-4.1** Risk tolerance | Art 9(1) | Clause 6.1 | GV.RR | — |
| **GV-5.1** Policy review | Art 9(3) | Clause 9.3 | GV.PO | — |
| **GV-6.1** Third-party risk | Art 25 | Clause 8.2 | GV.SC | — |
| **GV-7.1** Documentation | Art 11 | Clause 7.5 | ID.AM | Section 6-1-1701(4) |

---

### MAP Function Cross-Mapping

| NIST AI RMF | EU AI Act | ISO/IEC 42001 | NIST CSF 2.0 | Colorado AI Act |
|-------------|-----------|---------------|--------------|-----------------|
| **MP-1.1** Context of use | Art 6(2) | Clause 4.1 | ID.BE | — |
| **MP-2.1** AI categorization | Art 6 | Clause 6.1 | ID.AM | Section 6-1-1701(1) |
| **MP-3.1** Impacts | Art 9(2) | Clause 6.1 | ID.RA | Section 6-1-1701(2) |
| **MP-4.1** Likelihood/severity | Art 9(2) | Clause 6.1 | ID.RA | — |
| **MP-5.1** Risk tracking | Art 9(3) | Clause 9.1 | ID.RA | — |

---

### MEASURE Function Cross-Mapping

| NIST AI RMF | EU AI Act | ISO/IEC 42001 | NIST CSF 2.0 | Colorado AI Act |
|-------------|-----------|---------------|--------------|-----------------|
| **MS-1.1** Methods/metrics | Art 15 | Clause 9.1 | PR.DS | Section 6-1-1701(3) |
| **MS-2.1** Evaluation | Art 15 | Clause 9.2 | PR.DS | Section 6-1-1701(3) |
| **MS-3.1** Tracking | Art 72 | Clause 9.1 | DE.CM | — |
| **MS-4.1** Feedback | Art 52 | Clause 9.1 | RS.AN | Section 6-1-1701(4) |
| **MS-5.1** Assurance | Art 43 | Clause 9.3 | GV.PO | — |

---

### MANAGE Function Cross-Mapping

| NIST AI RMF | EU AI Act | ISO/IEC 42001 | NIST CSF 2.0 | Colorado AI Act |
|-------------|-----------|---------------|--------------|-----------------|
| **MG-1.1** Risk response | Art 9(4) | Clause 8.1 | RS.MI | — |
| **MG-2.1** Incident response | Art 53 | Clause 10.1 | RS.RP | Section 6-1-1701(5) |
| **MG-3.1** Review/update | Art 9(3) | Clause 10.2 | PR.IP | — |
| **MG-4.1** Communication | Art 52 | Clause 7.4 | RC.CO | Section 6-1-1701(4) |

---

## Seven Characteristics → Multi-Framework Mapping

| NIST AI RMF Characteristic | EU AI Act | ISO/IEC 42001 | NIST CSF 2.0 | Colorado AI Act |
|---------------------------|-----------|---------------|--------------|-----------------|
| **Valid and Reliable** | Art 15 | Clause 8.2 | PR.DS | Section 6-1-1701(3) |
| **Safe** | Art 9 | Clause 6.1 | PR.DS | Section 6-1-1701(2) |
| **Secure and Resilient** | Art 15 | Clause 8.2 | PR.DS, RS.RP | — |
| **Accountable and Transparent** | Art 14, 52 | Clause 5.2, 7.4 | GV.AT | Section 6-1-1701(3)(a) |
| **Explainable and Interpretable** | Art 13 | Clause 8.2 | ID.AM | Section 6-1-1701(3)(b) |
| **Privacy-Enhanced** | — (GDPR) | Clause 8.2 | PR.DS | Section 6-1-1701(2) |
| **Fair with Harmful Bias Managed** | Art 10 | Clause 6.1 | GV.PO | Entire Act |

---

## Common Controls Matrix

Controls that satisfy multiple frameworks simultaneously:

| Control | NIST AI RMF | EU AI Act | ISO 42001 | NIST CSF 2.0 | Colorado AI Act |
|---------|-------------|-----------|-----------|---------------|-----------------|
| Risk Management Plan | GV, MP | Art 9 | Clause 6.1 | ID.RA | Section 6-1-1701(2) |
| Model Documentation | GV-7.1 | Art 11 | Clause 7.5 | ID.AM | Section 6-1-1701(4) |
| Human Oversight | GV-1.2 | Art 14 | Clause 5.2 | GV.AT | Section 6-1-1701(3)(a) |
| Bias Testing | MS-2.1 | Art 10 | Clause 9.2 | GV.PO | Section 6-1-1701(3) |
| Incident Response | MG-2.1 | Art 53 | Clause 10.1 | RS.RP | Section 6-1-1701(5) |
| Audit Logging | GV-7.1 | Art 12 | Clause 7.5 | DE.CM | Section 6-1-1701(4) |
| Transparency Controls | MP-1.1 | Art 52 | Clause 7.4 | RC.CO | Section 6-1-1701(4) |
| Third-Party Assessment | GV-6.1 | Art 25 | Clause 8.2 | GV.SC | — |

---

## Implementation Priority

### Tier 1: Critical (All Frameworks)
- Risk Management Plan (NIST AI RMF MP, EU AI Act Art 9)
- Human Oversight Protocol (NIST AI RMF GV, EU AI Act Art 14)
- Bias Testing (NIST AI RMF MS, Colorado AI Act)
- Incident Response (NIST AI RMF MG, EU AI Act Art 53)

### Tier 2: High (Multiple Frameworks)
- Model Documentation (NIST AI RMF GV, EU AI Act Art 11)
- Audit Logging (NIST AI RMF GV, NIST CSF 2.0)
- Transparency Controls (NIST AI RMF MP, EU AI Act Art 52)
- Third-Party Assessment (NIST AI RMF GV, EU AI Act Art 25)

### Tier 3: Medium (Single Framework)
- Workforce Diversity (NIST AI RMF GV-3)
- Risk Tolerance Statements (NIST AI RMF GV-4)
- Assurance Processes (NIST AI RMF MS-5)

---

## Cross-References

- [NIST AI RMF Reference Guide](./nist-ai-rmf-reference-guide.md) — Complete NIST AI RMF guidance
- [Regulatory Reference Index](./regulatory-reference-index.md) — All regulations index
- [SAFEST to NIST AI RMF Mapping](../protolabs/nist-ai-rmf-safest-mapping.md) — SAFEST crosswalk
- [Expanded Regulatory Mapping](../04-operational-governance/regulatory/expanded-regulatory-mapping.md) — SOC 2, HIPAA, PCI DSS

---

*Last updated: 2026-04-23 / Version: 1.0 / Classification: Internal*
