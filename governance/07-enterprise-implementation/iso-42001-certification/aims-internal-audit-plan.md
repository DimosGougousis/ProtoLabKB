# AIMS Internal Audit Plan — ISO/IEC 42001 Clause 9.2

> **Purpose:** Defines the annual internal audit program for the ProtoLabs AI Management System, ensuring ISO/IEC 42001 Clause 9.2 compliance and certification readiness.

**Version:** 1.0  
**Last Updated:** 2026-04-24  
**Owner:** Internal Audit (independent of AIMS operations)  
**Review Cycle:** Annual  
**Next Audit Cycle:** Q3 2026  

---

## Audit Program Overview

### Audit Objectives

1. Verify AIMS conforms to ISO/IEC 42001:2023 requirements
2. Verify AIMS is effectively implemented and maintained
3. Identify nonconformities and opportunities for improvement
4. Provide assurance to management and certification body

### Audit Principles

| Principle | Application |
|-----------|-------------|
| **Independence** | Internal Audit reports to Board Audit Committee, not CAIO |
| **Competence** | Auditors trained in ISO 42001, AI systems, and manufacturing |
| **Objectivity** | Auditors have no operational responsibility for audited areas |
| **Evidence-based** | Findings supported by documented, verifiable evidence |
| **Risk-based** | Audit focus aligned with AIMS risk register |

### Audit Schedule (Annual Cycle)

| Quarter | Audit Focus | Clauses | Auditor | Duration |
|---------|-------------|---------|---------|----------|
| Q1 | Planning and Context (Clause 4-6) | 4, 5, 6 | Internal Audit | 3 days |
| Q2 | Operations and Support (Clause 7-8) | 7, 8 | Internal Audit + Technical SME | 5 days |
| Q3 | Performance and Improvement (Clause 9-10) | 9, 10 | Internal Audit | 3 days |
| Q4 | Follow-up and closure | All | Internal Audit | 2 days |

---

## Audit Scope

### In Scope

- All AI agents in the ProtoLabs fleet (Tier 1, 2, and 3)
- All stages of the AI system lifecycle (discovery through retirement)
- All governance pillars (discovery, development, runtime, operational, executive)
- All supporting processes (risk management, documentation control, training)

### Out of Scope

- Non-AI manufacturing processes (unless AI-influenced)
- Third-party AI tools not integrated into ProtoLabs agent fleet
- General IT infrastructure not supporting AIMS

---

## Audit Team

| Role | Name | Competence | Independence |
|------|------|------------|--------------|
| **Lead Auditor** | [TBD — Internal Audit Manager] | ISO 42001 Lead Auditor, 5+ years audit experience | Reports to Board Audit Committee |
| **Technical Auditor** | [TBD — External contractor or trained internal] | AI/ML background, ISO 42001 training | No operational AI responsibility |
| **Manufacturing SME** | [TBD — Rotating manufacturing engineer] | Manufacturing processes, safety systems | Not involved in AI agent development |
| **Observer (Q3)** | [TBD — Certification body representative] | Certification audit experience | N/A (observational only) |

---

## Audit Methodology

### Evidence Collection Methods

| Method | Application | Evidence Type |
|--------|-------------|---------------|
| **Document review** | Policies, procedures, records | Written evidence |
| **Interviews** | Key personnel, process owners | Testimonial evidence |
| **Observation** | Processes in operation | Observational evidence |
| **System inspection** | Agent behavior, logs, configurations | Technical evidence |
| **Sampling** | Audit logs, eval results, decisions | Statistical evidence |

### Sampling Approach

| Population | Sample Size | Basis |
|------------|-------------|-------|
| Agent decisions (audit logs) | 100 per agent per quarter | Random sampling |
| Eval results | All results from last quarter | 100% review |
| Incident reports | All incidents from last year | 100% review |
| Training records | 20% of all records | Stratified by role |
| Model cards | All active + 2 retired | 100% of active |

---

## Audit Criteria

### Clause-by-Clause Audit Focus

#### Clause 4: Context of the Organisation

| Audit Question | Evidence Sought | Finding Criteria |
|----------------|-----------------|------------------|
| Is the AIMS scope clearly defined and documented? | Scope statement, exclusions justified | Major if scope undefined; Minor if exclusions not justified |
| Are internal and external issues identified? | Issue registers, SWOT analysis | Major if no issue identification; Minor if incomplete |
| Are interested parties and their needs identified? | Stakeholder register, client requirements | Major if no stakeholder analysis; Minor if gaps |

#### Clause 5: Leadership

| Audit Question | Evidence Sought | Finding Criteria |
|----------------|-----------------|------------------|
| Is there board-level commitment to AIMS? | Board resolution, meeting minutes | Major if no board involvement; Minor if weak evidence |
| Is the AI policy established and communicated? | Policy document, communication records | Major if no policy; Minor if not communicated |
| Are roles and responsibilities defined? | RACI matrix, job descriptions | Major if no RACI; Minor if gaps |

#### Clause 6: Planning

| Audit Question | Evidence Sought | Finding Criteria |
|----------------|-----------------|------------------|
| Are risks and opportunities assessed? | Risk register, risk assessments | Major if no risk assessment; Minor if outdated |
| Are AI objectives established and measurable? | `aims-objectives-and-kpis.md` | Major if no objectives; Minor if not measurable |
| Are changes planned systematically? | Change records, impact assessments | Major if uncontrolled changes; Minor if gaps |

#### Clause 7: Support

| Audit Question | Evidence Sought | Finding Criteria |
|----------------|-----------------|------------------|
| Are resources adequate? | Budget, infrastructure inventory | Major if critical resource gaps; Minor if planning gaps |
| Is competence verified? | Training records, competence matrix | Major if untrained personnel in critical roles; Minor if gaps |
| Is awareness demonstrated? | Training completion, interview responses | Major if no awareness program; Minor if incomplete |
| Is documented information controlled? | Version control, retention schedule | Major if no document control; Minor if gaps |

#### Clause 8: Operation

| Audit Question | Evidence Sought | Finding Criteria |
|----------------|-----------------|------------------|
| Are AI lifecycle processes followed? | Lifecycle records, gate approvals | Major if gates bypassed; Minor if documentation gaps |
| Is risk treatment implemented? | Guardrail configs, Safety Agent logs | Major if treatment not implemented; Minor if evidence gaps |
| Is safety validation conducted? | Safety reports, test records | Major if no safety validation for Tier 2/3; Minor if incomplete |

#### Clause 9: Performance Evaluation

| Audit Question | Evidence Sought | Finding Criteria |
|----------------|-----------------|------------------|
| Is monitoring conducted? | Dashboards, metrics, review records | Major if no monitoring; Minor if gaps |
| Are internal audits conducted? | Audit plans, reports, corrective actions | Major if no internal audit program; Minor if scheduling gaps |
| Are management reviews conducted? | Review minutes, action items | Major if no management review; Minor if incomplete |

#### Clause 10: Improvement

| Audit Question | Evidence Sought | Finding Criteria |
|----------------|-----------------|------------------|
| Are nonconformities identified and corrected? | Nonconformity records, corrective actions | Major if no nonconformity process; Minor if delayed closure |
| Is continual improvement demonstrated? | Improvement register, evidence of results | Major if no improvement activity; Minor if weak evidence |

---

## Audit Reporting

### Finding Classification

| Severity | Definition | Response Time | Escalation |
|----------|------------|---------------|------------|
| **Critical** | AIMS failure, safety risk, regulatory violation | Immediate | CAIO + Board within 24 hours |
| **Major** | Nonconformity with ISO 42001 requirement | 30 days | CAIO within 1 week |
| **Minor** | Partial conformity, improvement opportunity | 90 days | Process owner |
| **Observation** | Potential issue, no immediate action required | Next audit | None |

### Report Distribution

| Report | Recipients | Timing |
|--------|------------|--------|
| Draft report | Audited process owners | Within 5 days of audit completion |
| Final report | CAIO, Board Audit Committee, Process Owners | Within 10 days of audit completion |
| Management summary | Board of Directors | Next board meeting |
| Certification body (if requested) | Certification body | Per agreement |

---

## Corrective Action Tracking

| Finding ID | Description | Severity | Owner | Target Date | Status | Verification |
|------------|-------------|----------|-------|-------------|--------|--------------|
| [Example] | Safety Agent logs incomplete for Tier 3 actions | Major | Safety Officer | 2026-08-15 | Open | Pending |

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-24 | ProtoLabs AI Governance Office | Initial internal audit plan |

---

## See Also

- `governance/07-enterprise-implementation/iso-42001-certification/aims-internal-audit-checklist.md` — Detailed audit checklist
- `governance/07-enterprise-implementation/iso-42001-certification/aims-internal-audit-report-template.md` — Report template
- `governance/07-enterprise-implementation/organizational-model/three-lines-of-defense-for-ai.md` — Three Lines of Defense
- `docs/iso-42001-gap-analysis.md` — Gap analysis (Clause 9.2)
