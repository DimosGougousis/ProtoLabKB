# ProtoLabs AI Policy — Client Summary

> **Purpose:** One-page summary of ProtoLabs' AI governance policy for client RFP responses, procurement questionnaires, and supplier qualification processes. Derived from the full `governance-charter.md`.

**Version:** 1.0  
**Last Updated:** 2026-04-24  
**Owner:** VP of Product (Policy Owner)  
**Classification:** Public — Client Distribution  

---

## ProtoLabs AI Governance at a Glance

ProtoLabs operates a fleet of AI-powered agents that assist in Design for Manufacturing (DFM) analysis, materials selection, production scheduling, and quality control. Our AI governance framework ensures these systems are **valid, safe, secure, accountable, explainable, privacy-enhanced, and fair**.

---

## Our Commitments

### 1. Valid and Reliable AI
- All DFM recommendations validated against golden datasets with >90% accuracy
- Continuous monitoring for model drift with quarterly revalidation
- Human expert review for complex or borderline cases

### 2. Safety-First Design
- **Tier 1 (Advisory)** agents provide recommendations only — humans decide and act
- **Tier 2 (Conditional)** agents operate within strict guardrails with human approval for exceptions
- **Tier 3 (High Autonomy)** agents validated by a Safety Agent (Governor) before any physical system action
- Kill switches: 30-second activation for Tier 2, 5-second for Tier 3 + automatic safe-state

### 3. Security and Resilience
- 5-layer adversarial defense (WP02): Input → Pattern → Semantic → Behavioral → Output validation
- <1% tolerance for prompt injection and jailbreak success
- Network segmentation between IT and OT (ICS/SCADA) systems
- Compliance with NIST CSF 2.0 and IEC 62443

### 4. Accountability and Transparency
- Every AI decision traceable to an accountable individual via RACI matrix
- Complete audit trails with tamper-evident logging
- Source citations for all knowledge-based recommendations (KB article + original URL)
- Clients notified when AI is involved in their service delivery

### 5. Explainability
- RAG context displayed for all knowledge-based outputs
- Quote breakdowns show AI-calculated vs. human-validated components
- Schedule rationales available to production operators
- Anomaly explanations provided to quality engineers

### 6. Privacy and IP Protection
- Client CAD files encrypted at rest and in transit
- Access controlled via role-based permissions
- Client data never used for model training without explicit consent
- 7-year retention with secure deletion procedures
- GDPR, ITAR, and EAR compliance for regulated industries

### 7. Fairness
- Bias testing conducted quarterly for all recommendation agents
- No discriminatory pricing or scheduling
- Fairness metrics monitored continuously

---

## Certifications and Standards

| Standard | Status | Scope |
|----------|--------|-------|
| **ISO/IEC 42001:2023** | In Progress (Target: Q1 2027) | AI Management System |
| **NIST AI RMF 1.0** | Implemented | Risk management framework |
| **EU AI Act** | Compliant | Risk-tiered obligations |
| **GDPR** | Compliant | Data protection |
| **ISO 9001** | [Existing certification] | Quality management |
| **AS9100D** | [If applicable] | Aerospace quality |

---

## Governance Structure

```
┌─────────────────────────────────────────┐
│      Board of Directors                 │
│      (AI Policy Approval)               │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│      Chief AI Officer (CAIO)            │
│      AIMS Owner                         │
└─────────────────┬───────────────────────┘
                  │
    ┌─────────────┼─────────────┐
    ▼             ▼             ▼
┌───────┐    ┌───────┐    ┌───────┐
│Policy  │    │Technical│   │Safety │
│Owner   │    │Owner   │    │Officer│
│(VP     │    │(VP Eng)│    │(Dir.  │
│Product)│    │        │    │Safety)│
└───────┘    └───────┘    └───────┘
```

---

## Client Assurance

### For Aerospace Clients (AS9100D)
- AI agents do not modify safety-critical parameters without Safety Agent validation
- Complete traceability for all AI-influenced manufacturing decisions
- ITAR/EAR-controlled data handled with enhanced protection

### For Medical Device Clients (ISO 13485)
- AI recommendations validated against biocompatibility and regulatory requirements
- Full audit trail for FDA 510(k) / MDR technical documentation support
- No AI system classified as "high-risk" under EU AI Act Article 6

### For Automotive Clients (IATF 16949)
- AI scheduling respects production part approval process (PPAP) requirements
- Statistical process control (SPC) integration for quality agents
- FMEA-aligned risk management for all AI systems

---

## Contact

For AI governance inquiries, procurement questionnaires, or audit requests:

| Inquiry Type | Contact | Email |
|--------------|---------|-------|
| General AI Governance | AI Governance Office | ai-governance@protolabs.com |
| Certification Status | Chief AI Officer | caio@protolabs.com |
| Security & Compliance | Data Protection Officer | dpo@protolabs.com |
| Technical Architecture | VP of Engineering | vp-eng@protolabs.com |

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-24 | ProtoLabs AI Governance Office | Initial client-facing policy summary |

---

## See Also

- `governance/00-getting-started/governance-charter.md` — Full governance charter (internal)
- `governance/07-enterprise-implementation/iso-42001-certification/board-resolution-aims.md` — Board resolution
- `docs/iso-42001-gap-analysis.md` — Certification roadmap
