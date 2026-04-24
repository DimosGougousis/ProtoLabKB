# AIMS Competence Matrix — ISO/IEC 42001 Clause 7.2

> **Purpose:** Defines competence requirements for all roles involved in the ProtoLabs AI Management System (AIMS), tracks training completion, and ensures ISO/IEC 42001 Clause 7.2 compliance.

**Version:** 1.0  
**Last Updated:** 2026-04-24  
**Owner:** Chief AI Officer (AIMS Owner)  
**Review Cycle:** Quarterly  
**Next Review:** 2026-07-24  

---

## Competence Framework

### Role Categories

| Category | Roles | AIMS Involvement |
|----------|-------|------------------|
| **Executive** | Board, CAIO, VPs | Policy, governance, accountability |
| **Technical** | ML Engineers, AI Engineers, MLOps | Agent development, deployment, monitoring |
| **Safety** | Safety Officer, Manufacturing Safety | Physical safety validation, kill switch |
| **Compliance** | Compliance Officer, DPO, Internal Audit | Regulatory, audit, data protection |
| **Operational** | Production Managers, Account Managers, PEs | Day-to-day AI system operation |
| **Quality** | Quality Engineers, Quality Managers | Quality agent oversight, anomaly handling |

---

## Competence Requirements by Role

### Executive Roles

#### Chief AI Officer (AIMS Owner)

| Competence Area | Required Knowledge | Required Skills | Evidence | Training | Status |
|-----------------|-------------------|-----------------|----------|----------|--------|
| AI Governance | NIST AI RMF, ISO 42001, EU AI Act | Framework implementation | `board-resolution-aims.md` | ISO 42001 Lead Auditor (planned) | ⏳ |
| Risk Management | AI risk taxonomy, risk appetite | Risk assessment, mitigation | `ai-risk-appetite-framework.md` | NIST AI RMF training | ✅ |
| Agentic AI | Tier classification, Safety Agent | Architecture decisions | `agentic-governance-2026-framework.md` | Agentic AI workshop | ✅ |
| Manufacturing AI | DFM processes, manufacturing systems | Domain application | Industry experience | ProtoLabs onboarding | ✅ |

#### VP of Product (Policy Owner)

| Competence Area | Required Knowledge | Required Skills | Evidence | Training | Status |
|-----------------|-------------------|-----------------|----------|----------|--------|
| AI Policy | Policy development, regulatory mapping | Policy authoring, review | `governance-charter.md` | AI Policy Design course | ✅ |
| Product Ethics | Ethical AI, fairness, bias | Impact assessment | `ai-ethics-impact-assessment.md` | Ethics in AI Product | ✅ |
| Client Requirements | Aerospace, medical, automotive standards | Requirement translation | Vertical agent knowledge | Industry seminars | ✅ |

#### VP of Engineering (Technical Owner)

| Competence Area | Required Knowledge | Required Skills | Evidence | Training | Status |
|-----------------|-------------------|-----------------|----------|----------|--------|
| ML Systems | Model development, evaluation, deployment | MLOps, eval suites | `eval-driven-development.md` | Advanced MLOps | ✅ |
| AI Security | Adversarial ML, prompt injection | Defense implementation | `red-teaming-ai-systems.md` | AI Security certification | ⏳ |
| Agent Architecture | Multi-agent systems, orchestration | System design | `multi-agent-governance-framework.md` | Agent architecture workshop | ✅ |
| OT/ICS Security | IEC 62443, safety systems | Network segmentation | `nist-cybersecurity-framework.md` | ICS Security fundamentals | ⏳ |

### Technical Roles

#### ML Engineer

| Competence Area | Required Knowledge | Required Skills | Evidence | Training | Status |
|-----------------|-------------------|-----------------|----------|----------|--------|
| Model Development | LLMs, RAG, fine-tuning | Model training, evaluation | `model-card.md` | LLM Engineering | ✅ |
| Evaluation Methods | Accuracy, precision, recall, F1 | Eval suite design | `dfm-accuracy-eval-suite.yaml` | ML Evaluation Design | ✅ |
| Bias & Fairness | Fairness metrics, demographic parity | Bias testing | `bias-and-fairness-evals.md` | Fairness in ML | ⏳ |
| Model Documentation | Model cards, data sheets | Documentation authoring | `model-card.md` | Responsible AI Documentation | ✅ |

#### AI Engineer (Agent Development)

| Competence Area | Required Knowledge | Required Skills | Evidence | Training | Status |
|-----------------|-------------------|-----------------|----------|----------|--------|
| Agent Frameworks | LangChain, AutoGen, custom | Agent implementation | Agent codebase | Agent Development Bootcamp | ✅ |
| Tool Use & APIs | REST, SCPI, MES/ERP APIs | API integration | `tool-use-risk-model.yaml` | API Security for AI | ✅ |
| Guardrails | Input validation, output filtering | Guardrail implementation | `output-validation-patterns.md` | AI Guardrails Design | ✅ |
| Safety Integration | Safety Agent protocols | Safety validation | `safety-agent-config.yaml` | Safety-Critical AI Systems | ⏳ |

#### MLOps Engineer

| Competence Area | Required Knowledge | Required Skills | Evidence | Training | Status |
|-----------------|-------------------|-----------------|----------|----------|--------|
| CI/CD for AI | Model versioning, A/B testing | Pipeline design | `governance-in-cicd.md` | MLOps Fundamentals | ✅ |
| Monitoring | Drift detection, performance tracking | Dashboard creation | `model-monitoring-dashboard.md` | AI Monitoring & Observability | ✅ |
| Infrastructure | Kubernetes, GPU clusters, cloud | Infrastructure management | Infrastructure config | Cloud AI Infrastructure | ✅ |
| Incident Response | AI incident triage, rollback | Rapid response | `ai-incident-report.md` | AI Incident Response | ⏳ |

### Safety Roles

#### Director of Manufacturing Safety (Safety Officer)

| Competence Area | Required Knowledge | Required Skills | Evidence | Training | Status |
|-----------------|-------------------|-----------------|----------|----------|--------|
| Safety Standards | ISO 10218, ISO/TS 15066, IEC 62443 | Safety validation | `safety-validation-report.md` | Robot Safety Certification | ✅ |
| Safety Agent Design | Governor patterns, kill switches | Safety system design | `kill-switch-specification.md` | Safety Agent Architecture | ⏳ |
| Risk Assessment | HAZOP, FMEA, risk matrices | Safety risk analysis | `risk-management-plan.md` | Manufacturing Risk Assessment | ✅ |
| Emergency Response | E-stop procedures, incident command | Emergency coordination | Emergency response drills | Incident Command System | ✅ |

### Compliance Roles

#### Compliance Officer

| Competence Area | Required Knowledge | Required Skills | Evidence | Training | Status |
|-----------------|-------------------|-----------------|----------|----------|--------|
| AI Regulations | EU AI Act, NIST AI RMF, Colorado AI Act | Regulatory mapping | `regulatory-reference-index.md` | AI Regulation Certification | ⏳ |
| Audit Management | ISO 42001, ISO 27001 audit processes | Audit preparation, evidence | Audit experience | Lead Auditor ISO 27001 | ✅ |
| Documentation Control | Version control, retention policies | Document management | `audit-record-schema.yaml` | Document Control Systems | ✅ |
| Incident Reporting | Breach notification, regulatory reporting | Report authoring | `ai-incident-report.md` | Regulatory Reporting | ✅ |

#### Data Protection Officer (DPO)

| Competence Area | Required Knowledge | Required Skills | Evidence | Training | Status |
|-----------------|-------------------|-----------------|----------|----------|--------|
| GDPR | Data subject rights, DPIA, breach notification | Privacy compliance | `dpia-template.md` | CIPP/E Certification | ✅ |
| Data Governance | Data minimization, retention, deletion | Policy implementation | `data-governance-plan.md` | Data Governance Certification | ✅ |
| IP Protection | ITAR, EAR, trade secrets | Export control | `customer-cad-ip-protection-guardrail.md` | Export Control Compliance | ✅ |
| PETs | Encryption, anonymization, pseudonymization | Technical implementation | Encryption configs | Privacy-Enhancing Technologies | ✅ |

### Operational Roles

#### Production Manager (Operational Owner)

| Competence Area | Required Knowledge | Required Skills | Evidence | Training | Status |
|-----------------|-------------------|-----------------|----------|----------|--------|
| AI Scheduling | Production scheduler agent, MES | Schedule oversight | `scheduler-eval-results.yaml` | AI in Manufacturing | ✅ |
| Safety Protocols | Kill switch activation, emergency stop | Emergency response | Kill switch training | Safety Protocol Training | ✅ |
| Anomaly Response | Quality alerts, drift notifications | Triage, escalation | `drift-detection-runbook.md` | Anomaly Response Training | ✅ |
| Human Override | Tier 2 approval, exception handling | Decision authority | `policy-ownership-registry.yaml` | AI Oversight Training | ✅ |

#### Account Manager

| Competence Area | Required Knowledge | Required Skills | Evidence | Training | Status |
|-----------------|-------------------|-----------------|----------|----------|--------|
| AI Transparency | AI disclosure, quote explanation | Client communication | `transparency-controls.md` | AI Client Communication | ✅ |
| Pricing Guardrails | Margin checks, approval thresholds | Quote validation | `financial-guardrails-config.yaml` | AI Pricing Oversight | ✅ |
| Escalation | Pricing disputes, AI errors | Issue resolution | Escalation playbook | Client Issue Resolution | ✅ |

#### Process Engineer (PE)

| Competence Area | Required Knowledge | Required Skills | Evidence | Training | Status |
|-----------------|-------------------|-----------------|----------|----------|--------|
| DFM Validation | Manufacturing processes, tolerances | DFM review, validation | DFM expertise | Manufacturing Engineering | ✅ |
| AI Limitations | Agent capabilities, edge cases | Override decisions | `model-card.md` | AI System Limitations | ✅ |
| KB Maintenance | Knowledge base articles, source citations | Content curation | KB articles | Knowledge Management | ✅ |

### Quality Roles

#### Quality Engineer

| Competence Area | Required Knowledge | Required Skills | Evidence | Training | Status |
|-----------------|-------------------|-----------------|----------|----------|--------|
| Quality Metrics | CMM, SPC, tolerance analysis | Measurement, analysis | `quality-agent-eval-results.yaml` | Quality Engineering | ✅ |
| AI Quality Systems | Quality agent, anomaly detection | System oversight | `anomaly-explanation-module.md` | AI Quality Systems | ⏳ |
| Defect Analysis | Root cause analysis, corrective action | Investigation | `ai-incident-report.md` | Root Cause Analysis | ✅ |

---

## Training Program

### Required Training by Role

| Training Course | Target Roles | Duration | Frequency | Delivery | Status |
|-----------------|--------------|----------|-----------|----------|--------|
| ISO 42001 Fundamentals | All AIMS roles | 4 hours | Annual | E-learning | 🔄 Rolling |
| AI Governance for Leaders | Executive | 8 hours | Annual | Workshop | 🔄 Rolling |
| Agentic AI Safety | Technical, Safety | 16 hours | Annual | Hands-on | 🔄 Rolling |
| AI Security & Adversarial Defense | Technical, Security | 12 hours | Annual | Workshop | 🔄 Rolling |
| Bias & Fairness in AI | Technical, Product | 8 hours | Annual | E-learning | 🔄 Rolling |
| AI Incident Response | Technical, Operational | 4 hours | Semi-annual | Drill | 🔄 Rolling |
| Kill Switch & Emergency Procedures | Operational, Safety | 2 hours | Quarterly | Drill | 🔄 Rolling |
| Data Protection & IP Handling | All client-facing | 4 hours | Annual | E-learning | 🔄 Rolling |
| AI Explainability & Transparency | All client-facing | 2 hours | Annual | E-learning | 🔄 Rolling |

### Training Completion Tracking

| Role | Required Courses | Completed | Completion Rate | Next Due |
|------|-----------------|-----------|-----------------|----------|
| CAIO | 3 | [TBD] | [TBD]% | [TBD] |
| VP Product | 3 | [TBD] | [TBD]% | [TBD] |
| VP Engineering | 4 | [TBD] | [TBD]% | [TBD] |
| Safety Officer | 4 | [TBD] | [TBD]% | [TBD] |
| Compliance Officer | 3 | [TBD] | [TBD]% | [TBD] |
| DPO | 3 | [TBD] | [TBD]% | [TBD] |
| ML Engineer | 4 | [TBD] | [TBD]% | [TBD] |
| AI Engineer | 4 | [TBD] | [TBD]% | [TBD] |
| MLOps Engineer | 4 | [TBD] | [TBD]% | [TBD] |
| Production Manager | 3 | [TBD] | [TBD]% | [TBD] |
| Account Manager | 3 | [TBD] | [TBD]% | [TBD] |
| PE | 3 | [TBD] | [TBD]% | [TBD] |
| Quality Engineer | 3 | [TBD] | [TBD]% | [TBD] |

---

## Competence Assessment

### Assessment Methods

| Method | Frequency | Applied To | Evidence |
|--------|-----------|------------|----------|
| Training completion verification | Per course | All roles | LMS records |
| Practical demonstration | Annual | Technical, Safety | Eval suite results, kill switch tests |
| Knowledge test | Annual | All roles | Quiz scores |
| Peer review | Quarterly | Technical | Code review, architecture review |
| Incident response drill | Semi-annual | Operational, Safety | Drill observation notes |

### Competence Gaps and Actions

| Role | Gap Identified | Action | Target Date | Owner |
|------|---------------|--------|-------------|-------|
| CAIO | ISO 42001 Lead Auditor certification | Enroll in certification course | Q3 2026 | CAIO |
| VP Engineering | AI Security certification | Complete AI Security certification | Q3 2026 | VP Engineering |
| VP Engineering | ICS Security fundamentals | Complete ICS Security course | Q3 2026 | VP Engineering |
| ML Engineer | Fairness in ML training | Complete Fairness in ML course | Q2 2026 | ML Lead |
| AI Engineer | Safety-Critical AI Systems | Complete Safety Agent training | Q2 2026 | Safety Officer |
| Safety Officer | Safety Agent Architecture | Complete Safety Agent design course | Q2 2026 | Safety Officer |
| Compliance Officer | AI Regulation Certification | Complete AI Regulation course | Q3 2026 | Compliance Officer |
| Quality Engineer | AI Quality Systems | Complete AI Quality Systems training | Q2 2026 | Quality Manager |

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-24 | ProtoLabs AI Governance Office | Initial competence matrix |

---

## See Also

- `governance/05-cross-cutting/governance-roles-raci.md` — RACI matrix
- `governance/07-enterprise-implementation/organizational-model/three-lines-of-defense-for-ai.md` — Three Lines of Defense
- `governance/07-enterprise-implementation/training-and-awareness-plan.md` — Training program
- `docs/iso-42001-gap-analysis.md` — Gap analysis (Clause 7.2)
