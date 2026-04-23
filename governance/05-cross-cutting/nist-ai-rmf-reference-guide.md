# NIST AI Risk Management Framework (AI RMF 1.0) — ProtoLabs Reference Guide

> **Purpose:** Comprehensive guide to implementing NIST AI RMF 1.0 across the ProtoLabs AI Governance Framework. Establishes the seven characteristics of trustworthy AI as mandatory assessment dimensions for every new AI project.

**Version:** 1.0  
**Last Updated:** 2026-04-23  
**Owner:** ProtoLabs AI Governance Office  
**Review Cycle:** Quarterly, or upon NIST updates

---

## Regulatory Basis

- **NIST AI RMF 1.0** — Artificial Intelligence Risk Management Framework (January 2023)
- **NIST AI RMF Playbook** — Implementation guidance
- **EO 14110** — Executive Order on Safe, Secure, and Trustworthy AI (October 2023)
- **Cross-reference:** EU AI Act Article 9 (Risk Management System), ISO/IEC 42001 Clause 6 (Planning)

---

## The Four Functions of NIST AI RMF

NIST AI RMF organizes AI risk management into four core functions, each containing categories and subcategories:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         NIST AI RMF 1.0 CORE FUNCTIONS                       │
├───────────────┬───────────────┬───────────────┬───────────────────────────────┤
│    GOVERN     │     MAP       │    MEASURE    │           MANAGE              │
│    (GV)       │    (MP)       │    (MS)       │           (MG)                │
├───────────────┼───────────────┼───────────────┼───────────────────────────────┤
│ Establish     │ Establish     │ Identify      │ Respond to                  │
│ organizational│ context to    │ appropriate   │ identified risks              │
│ culture,      │ frame risks   │ metrics &     │ once evaluated                │
│ structures,   │ related to    │ methods to    │                               │
│ processes,    │ an AI system  │ assess,       │                               │
│ & workforce   │               │ analyze, &    │                               │
│ competencies  │               │ track AI risk │                               │
│               │               │ & related     │                               │
│               │               │ impacts       │                               │
└───────────────┴───────────────┴───────────────┴───────────────────────────────┘
```

---

## The Seven Characteristics of Trustworthy AI

Every AI system at ProtoLabs must be assessed against these seven characteristics before proceeding through governance gates.

### 1. Valid and Reliable (V&R)

**Definition:** The AI system correctly achieves its intended purpose (validity) and performs consistently over time without failing (reliability).

**Key Questions:**
- Does the system achieve its intended purpose in real-world conditions, not just controlled environments?
- Does performance remain consistent across different inputs, times, and operational conditions?
- Are failure modes identified and documented?

**ProtoLabs Implementation:**
| Assessment Area | Evidence Required | Governance Artifact |
|-----------------|-------------------|---------------------|
| Accuracy validation | Eval results against golden dataset | `dfm-accuracy-eval-suite.yaml` |
| Consistency testing | Statistical variance across test runs | `test-plan-for-ai.md` |
| Failure mode analysis | Documented edge cases and limitations | `model-card.md` |
| Real-world validation | Production pilot results | `acceptance-criteria.md` |

**Risk if Missing:** Incorrect DFM recommendations, customer dissatisfaction, liability exposure

---

### 2. Safe

**Definition:** The AI system does not put people, property, or the environment in danger. Requires rigorous pre-deployment testing, clear guidance for safe use, and thorough risk documentation.

**Key Questions:**
- What are the worst-case failure scenarios?
- Has the system been tested for safety-critical edge cases?
- Are there clear kill-switch procedures?
- Is safety documentation complete and accessible?

**ProtoLabs Implementation:**
| Assessment Area | Evidence Required | Governance Artifact |
|-----------------|-------------------|---------------------|
| Harm scenario analysis | Top 3 harm scenarios documented | `risk-management-plan.md` |
| Safety testing | Red team results, adversarial testing | `red-teaming-ai-systems.md` |
| Emergency procedures | Kill switch specification | `KILLSWITCH.md` (per agent) |
| Safety documentation | User warnings and limitations | `transparency-controls.md` |

**Risk if Missing:** Physical harm from faulty manufacturing advice, regulatory violations, reputational damage

---

### 3. Secure and Resilient (S&R)

**Definition:** The system is **secure** (protected against adversarial attacks, data poisoning, model theft) and **resilient** (can recover gracefully from unexpected events).

**Key Questions:**
- What adversarial attacks has the system been tested against?
- How does the system handle anomalous inputs?
- Are there graceful degradation procedures?
- Is the system protected against prompt injection and jailbreaks?

**ProtoLabs Implementation:**
| Assessment Area | Evidence Required | Governance Artifact |
|-----------------|-------------------|---------------------|
| Adversarial testing | Jailbreak resistance scores | `red-teaming-ai-systems.md` |
| Input validation | Sanitization test results | `input-sanitization.md` |
| Resilience testing | Chaos engineering results | `resilience-test-plan.md` |
| Security controls | NIST CSF 2.0 alignment | `nist-cybersecurity-framework.md` |

**Risk if Missing:** Data breaches, IP theft, adversarial manipulation of DFM outputs

---

### 4. Accountable and Transparent (A&T)

**Definition:** **Accountability** ensures clear responsibility for outcomes. **Transparency** guarantees users understand when AI is being used and how decisions are made.

**Key Questions:**
- Who is accountable for AI system outcomes?
- Do users know when they are interacting with AI?
- Can decisions be audited and explained?
- Is there a clear chain of responsibility?

**ProtoLabs Implementation:**
| Assessment Area | Evidence Required | Governance Artifact |
|-----------------|-------------------|---------------------|
| Accountability matrix | RACI for AI decisions | `governance-roles-raci.md` |
| AI disclosure | User notification mechanisms | `transparency-controls.md` |
| Audit trail | Complete decision logging | `audit-record-schema.yaml` |
| Source citation | KB grounding with source URLs | `source-grounding-data-contract.yaml` |

**Risk if Missing:** Regulatory violations (EU AI Act Art 52), loss of customer trust, inability to audit

---

### 5. Explainable and Interpretable (E&I)

**Definition:** **Explainability** details *how* a system reached a decision. **Interpretability** clarifies *why* that specific decision was made and what it means in context.

**Key Questions:**
- Can engineers explain how the model arrived at a recommendation?
- Can users understand why a specific DFM suggestion was made?
- Are there tools for inspecting model behavior?
- Is there documentation of model logic?

**ProtoLabs Implementation:**
| Assessment Area | Evidence Required | Governance Artifact |
|-----------------|-------------------|---------------------|
| Model documentation | Architecture and training description | `model-card.md` |
| Explanation generation | RAG context display | `transparency-controls.md` |
| Decision tracing | Full delegation chain audit | `delegation-chain-audit.md` |
| Interpretability tools | Attention visualization, SHAP values | `eval-driven-development.md` |

**Risk if Missing:** Inability to debug, regulatory non-compliance, user confusion

---

### 6. Privacy-Enhanced

**Definition:** AI safeguards individuals' autonomy, dignity, and control over personal information through data minimization and privacy-enhancing technologies.

**Key Questions:**
- Is personal data collection minimized?
- Are privacy-enhancing technologies (PETs) used?
- Is customer CAD/IP data protected?
- Are anonymization/pseudonymization techniques applied?

**ProtoLabs Implementation:**
| Assessment Area | Evidence Required | Governance Artifact |
|-----------------|-------------------|---------------------|
| Data minimization | DPIA documentation | `dpia-template.md` |
| IP protection | CAD/IP handling procedures | `customer-cad-ip-protection-guardrail.md` |
| Access controls | Per-skill RBAC configuration | `skill-manifest.yaml` |
| Data retention | Retention and deletion policies | `data-governance-plan.md` |

**Risk if Missing:** GDPR violations, IP theft, loss of customer trust, regulatory penalties

---

### 7. Fair with Harmful Bias Managed

**Definition:** The system treats individuals and groups equitably, with active management of systemic, computational, and human cognitive biases.

**Key Questions:**
- Has the system been tested for demographic bias?
- Are fairness metrics defined and monitored?
- Is there a process for handling bias reports?
- Are training data biases documented?

**ProtoLabs Implementation:**
| Assessment Area | Evidence Required | Governance Artifact |
|-----------------|-------------------|---------------------|
| Bias testing | Fairness eval results | `bias-and-fairness-evals.md` |
| Demographic parity | Protected group analysis | `defining-acceptance-criteria.md` |
| Data bias audit | Training data bias report | `data-governance-plan.md` |
| Fairness monitoring | Continuous fairness metrics | `continuous-monitoring-plan.md` |

**Risk if Missing:** Discriminatory outcomes, regulatory violations (Colorado AI Act), reputational damage

---

## NIST AI RMF → ProtoLabs Four-Pillar Mapping

| NIST AI RMF Function | ProtoLabs Governance Pillar | Key Artifacts |
|---------------------|----------------------------|---------------|
| **GOVERN** | 01-Discovery Governance + 06-Executive | `governance-charter.md`, `ethical-use-policy.md`, `governance-roles-raci.md` |
| **MAP** | 01-Discovery Governance | `ml-lifecycle-canvas.md`, `risk-management-plan.md`, `eu-ai-act-risk-classification.yaml` |
| **MEASURE** | 02-Development Governance + 04-Operational Governance | `dfm-accuracy-eval-suite.yaml`, `test-plan-for-ai.md`, `periodic-revalidation-schedule.yaml` |
| **MANAGE** | 03-Runtime Governance + 04-Operational Governance | `kill-switch-specification.md`, `ai-incident-report.md`, `drift-detection-runbook.md` |

---

## Seven Characteristics → Governance Gate Mapping

| Characteristic | Discovery Gate | Development Gate | Deployment Gate | Periodic Review |
|----------------|---------------|------------------|-----------------|-----------------|
| **Valid & Reliable** | Intended purpose defined | Eval suite validates accuracy | Production monitoring | Drift detection |
| **Safe** | Harm scenarios identified | Safety testing complete | Kill switch active | Incident tracking |
| **Secure & Resilient** | Threat model created | Adversarial testing passed | Runtime guardrails active | Security audits |
| **Accountable & Transparent** | RACI defined | Audit logging implemented | User disclosure active | Accountability review |
| **Explainable & Interpretable** | Explanation requirements set | Model documentation complete | Explanation features live | Interpretability audits |
| **Privacy-Enhanced** | DPIA completed | PETs implemented | Data handling verified | Privacy audits |
| **Fair** | Fairness criteria defined | Bias testing passed | Fairness monitoring active | Bias re-evaluation |

---

## Mandatory Assessment Template

Every new AI project must complete this assessment:

```yaml
# NIST AI RMF Seven Characteristics Assessment
# File: nist-ai-rmf-assessment.yaml

project_info:
  name: "[Project Name]"
  agent_id: "[Agent ID from registry]"
  assessment_date: "YYYY-MM-DD"
  assessed_by: "[Name + Role]"
  review_cadence: "quarterly"

# SEVEN CHARACTERISTICS ASSESSMENT
characteristics:
  valid_and_reliable:
    score: "[meets_exceeds | meets | partially_meets | does_not_meet]"
    evidence_ref: "[Link to eval results]"
    key_metrics:
      - metric: "Accuracy on golden dataset"
        value: "[X%]"
        threshold: "[Y%]"
      - metric: "Consistency variance"
        value: "[Z%]"
    limitations_documented: true|false
    real_world_validated: true|false
    
  safe:
    score: "[meets_exceeds | meets | partially_meets | does_not_meet]"
    evidence_ref: "[Link to harm scenarios]"
    top_harm_scenarios:
      - scenario: "[Description]"
        severity: "[critical | high | medium | low]"
        mitigation: "[Description]"
    safety_testing_complete: true|false
    kill_switch_configured: true|false
    safety_documentation_published: true|false
    
  secure_and_resilient:
    score: "[meets_exceeds | meets | partially_meets | does_not_meet]"
    evidence_ref: "[Link to security testing]"
    adversarial_tests_passed:
      - test_type: "jailbreak_resistance"
        result: "[pass | fail | partial]"
      - test_type: "prompt_injection"
        result: "[pass | fail | partial]"
    resilience_tested: true|false
    graceful_degradation_configured: true|false
    
  accountable_and_transparent:
    score: "[meets_exceeds | meets | partially_meets | does_not_meet]"
    evidence_ref: "[Link to RACI]"
    accountability_chain:
      - role: "Product Owner"
        name: "[Name]"
      - role: "AI Engineer"
        name: "[Name]"
      - role: "Governance Lead"
        name: "[Name]"
    ai_disclosure_implemented: true|false
    audit_trail_configured: true|false
    source_citation_enforced: true|false
    
  explainable_and_interpretable:
    score: "[meets_exceeds | meets | partially_meets | does_not_meet]"
    evidence_ref: "[Link to model card]"
    explanation_methods:
      - "RAG context display"
      - "Decision tracing"
      - "[Other]"
    interpretability_tools_available: true|false
    explanation_quality_validated: true|false
    
  privacy_enhanced:
    score: "[meets_exceeds | meets | partially_meets | does_not_meet]"
    evidence_ref: "[Link to DPIA]"
    pii_handling: "[minimized | anonymized | pseudonymized | other]"
    pets_implemented:
      - "[List PETs]"
    data_retention_policy_defined: true|false
    ip_protection_configured: true|false
    
  fair_with_bias_managed:
    score: "[meets_exceeds | meets | partially_meets | does_not_meet]"
    evidence_ref: "[Link to bias testing]"
    fairness_metrics:
      - metric: "[demographic_parity | equalized_odds | other]"
        result: "[value]"
        threshold: "[value]"
    bias_testing_complete: true|false
    fairness_monitoring_active: true|false
    bias_reporting_process_defined: true|false

# OVERALL ASSESSMENT
overall_score: "[meets_exceeds | meets | partially_meets | does_not_meet]"
blockers: "[List any characteristics scoring 'does_not_meet']"
mitigation_plan: "[Required if any characteristic is 'partially_meets' or below]"
approval:
  product_owner: "[Name]"
  governance_lead: "[Name]"
  date: "YYYY-MM-DD"
```

---

## Cross-References

- [ML Lifecycle Canvas](../00-getting-started/ml-lifecycle-canvas.md) — Updated with NIST AI RMF section
- [SAFEST to NIST AI RMF Mapping](../protolabs/nist-ai-rmf-safest-mapping.md) — Crosswalk between methodologies
- [Regulatory Reference Index](./regulatory-reference-index.md) — Complete regulatory mapping
- [Governance Roles RACI](./governance-roles-raci.md) — Accountability definitions
- [EU AI Act Risk Classification](../01-discovery-governance/checklists/eu-ai-act-risk-classification.yaml) — Complementary risk assessment

---

## Related External Resources

- [NIST AI RMF 1.0](https://www.nist.gov/itl/ai-risk-management-framework) — Official NIST publication
- [NIST AI RMF Playbook](https://www.nist.gov/itl/ai-risk-management-framework) — Implementation guidance
- [NIST AI RMF Roadmap](https://www.nist.gov/itl/ai-risk-management-framework) — Future developments

---

*Last updated: 2026-04-23 / Version: 1.0 / Classification: Internal*
