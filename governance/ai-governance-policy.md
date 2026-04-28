# ProtoLabs AI Governance Policy

> **Document Type:** Enterprise AI Governance Policy (One-Page Entry Point)
> **Version:** 1.0
> **Effective Date:** 2026-04-28
> **Owner:** Chief AI Officer (CAIO)
> **Approved By:** Board of Directors
> **Review Cycle:** Annual, or upon material regulatory, model, or organizational change
> **Next Review:** 2027-04-28
> **Classification:** Internal — Board Distribution; Client Summary Available

---

## 1. Policy Statement

ProtoLabs designs, deploys, and operates AI systems — including autonomous and semi-autonomous agents — to deliver manufacturing intelligence across CNC machining, injection molding, sheet metal fabrication, and 3D printing. This policy governs the full AI lifecycle: discovery, development, deployment, monitoring, and retirement.

AI systems must align with ProtoLabs' business objectives (faster quoting, higher DFM accuracy, scalable engineering expertise), comply with applicable regulations (EU AI Act, GDPR, ITAR/EAR, NIST AI RMF 1.0, ISO/IEC 42001), and uphold the trust of clients whose proprietary designs and manufacturing data flow through our systems.

**This policy is not optional.** No AI system — internal or customer-facing — may enter production without satisfying the controls defined herein.

---

## 2. Definitions and Scope

| Term | Definition |
|------|------------|
| **AI System** | Any software component that uses machine learning, large language models, or statistical inference to generate outputs that influence user-facing or business decisions. |
| **Agentic AI** | An AI system that can invoke tools, delegate to other agents, or take actions with reduced human intervention. |
| **Generative AI** | AI that produces text, code, CAD suggestions, or manufacturing instructions from prompts or inputs. |
| **High-Risk Use** | Any AI output that materially affects pricing, lead-time commitments, structural design validity, regulatory compliance, or customer safety. |
| **Third-Party AI** | External foundation models (e.g., Claude, GPT-4V), AI-enabled SaaS tools, or vendor APIs integrated into ProtoLabs workflows. |

**Scope:** This policy applies to all AI systems built by ProtoLabs, all third-party AI integrated into ProtoLabs workflows, and all teams (engineering, product, operations, compliance) that design, deploy, or operate AI. It covers every lifecycle stage from discovery through retirement.

**Exclusions:** Third-party AI tools used by individual employees for personal productivity (e.g., standalone code assistants not connected to ProtoLabs systems) are excluded but subject to acceptable-use policies.

---

## 3. Governance Bodies and Roles

### AI Governance Council

| Attribute | Detail |
|-----------|--------|
| **Charter** | [AI Governance Council Charter](05-cross-cutting/ai-governance-council-charter.md) |
| **Composition** | CAIO (Chair), Head of Engineering, Data Protection Officer, Legal Counsel, Head of Internal Audit, Security Lead, VP Product |
| **Quorum** | Minimum 5 of 7 members |
| **Cadence** | Monthly; emergency sessions within 24 hours for Sev1 incidents |
| **Authority** | Approve Tier 2 deployments, review Tier 3 (escalate to Board), adjudicate governance disputes, update this policy |

### Accountability

| Role | Responsibility | Reference |
|------|---------------|-----------|
| **CAIO** | Enterprise AI risk ownership, board reporting, regulatory interface | [Governance Roles & RACI](05-cross-cutting/governance-roles-raci.md) |
| **Policy Owner** (per agent) | Business outcomes, risk management, compliance for a specific AI system | [RACI by Lifecycle Stage](05-cross-cutting/governance-roles-raci.md) |
| **Technical Owner** (per agent) | Model development, evaluation, deployment, monitoring | [RACI by Lifecycle Stage](05-cross-cutting/governance-roles-raci.md) |
| **Safety Officer** | Harm scenario analysis, kill-switch oversight, incident response | [Safety Agent Architecture](03-runtime-governance/agentic-workflows/customer-facing-agent-safety.md) |
| **Operational Owner** | Day-to-day operations, data handling, client interaction | [RACI by Lifecycle Stage](05-cross-cutting/governance-roles-raci.md) |

Every AI system must have a **named Policy Owner and Technical Owner** recorded in the agent registry before development begins.

---

## 4. Risk Classification

All AI use cases must be classified before development or procurement. Classification determines approval thresholds, required controls, and review intensity.

| Tier | Autonomy Level | Description | Examples | Approval Required |
|------|---------------|-------------|----------|-------------------|
| **Tier 1** | Advisory | Read-only recommendations; no actions; human decides | DFM analysis agents, router classifier | Technical Owner + Security |
| **Tier 2** | Conditional Autonomy | Can invoke tools/APIs; human approval for exceptions | Quote generation, production scheduling | Governance Council |
| **Tier 3** | High Autonomy | Acts independently within defined boundaries; human oversight by exception | Parameter optimization, autonomous quality control | Governance Council + Board |

**EU AI Act mapping:** Tier 1 → Limited-risk; Tier 2 → Limited-to-High-risk (re-assess per Annex III); Tier 3 → High-risk (assumed until proven otherwise).

**Classification is mandatory and non-negotiable.** An unclassified agent is an ungoverned agent.

Full classification methodology: [Agent Tier Classification](01-discovery-governance/templates/agent-tier-classification.yaml) · [EU AI Act Risk Classification](01-discovery-governance/checklists/eu-ai-act-risk-classification.yaml)

---

## 5. Control Requirements by Tier

| Control | Tier 1 | Tier 2 | Tier 3 |
|---------|--------|--------|--------|
| Model card | Required | Required | Required + external audit |
| Eval suite (accuracy, safety, fairness) | Required | Required | Required + red-team exercise |
| Input sanitization | Required | Required | Required |
| Human oversight plan | Advisory (override available) | Mandatory (approval gate) | Mandatory (exception-based review) |
| Kill switch | Not required | Required (<30s activation) | Required (<30s activation) |
| Source citation / audit trail | Required | Required | Required |
| Bias and fairness assessment | If demographic data involved | Required | Required + third-party review |
| Incident response plan | Required | Required | Required + board notification |
| Pre-deployment gate | Automated CI/CD | Council review | Board approval |
| Post-deployment monitoring | Performance KPIs | Performance + drift + misuse | Full spectrum + continuous eval |
| Legal review | Not required | If customer-facing | Required |
| PE validation (structural) | N/A | If structural output | Required |

Detailed checklists: [Discovery Governance](01-discovery-governance/) · [Development Governance](02-development-governance/) · [Runtime Governance](03-runtime-governance/)

---

## 6. Monitoring and Incidents

### Continuous Monitoring

All production AI systems must be monitored for:
- **Performance:** Accuracy, latency, throughput against baseline metrics
- **Drift:** Statistical deviation from training distribution (PSI, KL divergence)
- **Safety:** Harm scenario triggers, kill-switch activation frequency
- **Security:** Adversarial attack detection, prompt injection success rate
- **Compliance:** Citation completeness, audit trail integrity, data retention adherence

Monitoring plan: [Continuous Monitoring Plan](04-operational-governance/guides/continuous-monitoring-plan.md) · [Drift Detection](04-operational-governance/guides/drift-detection-runbook.md)

### Incident Severity and Response

| Severity | Definition | Response SLA | Escalation |
|----------|-----------|--------------|------------|
| **Sev1 — Critical** | Safety harm, data breach, regulatory violation | 15 minutes | CAIO + Board |
| **Sev2 — High** | Accuracy degradation >10%, customer-facing incorrect output | 2 hours | Governance Council |
| **Sev3 — Medium** | Non-critical drift, citation failures | 24 hours | Technical Owner |
| **Sev4 — Low** | Cosmetic issues, minor logging gaps | 1 week | Sprint backlog |

Incident response: [AI Incident Report Template](04-operational-governance/templates/ai-incident-report.md) · [Incident Severity Classification](04-operational-governance/incident-severity-classification.md)

---

## 7. Third-Party and Vendor Controls

No third-party AI model, API, or service may be integrated into ProtoLabs workflows without:

1. **Vendor risk assessment** — security, privacy, SLA, model update notification policy
2. **Data processing agreement** — explicit terms for customer data handling
3. **Model provenance registration** — which agent uses which vendor model and version
4. **Exit strategy** — documented plan for vendor lock-in, terms-of-service changes, or model deprecation
5. **Governance Council approval** — for any integration touching customer data or production decisions

Reference: [Third-Party AI Vendor Controls](05-cross-cutting/third-party-ai-vendor-controls.md) · [Regulatory Reference Index](05-cross-cutting/regulatory-reference-index.md)

---

## 8. Review and Updates

| Trigger | Action | Owner | SLA |
|---------|--------|-------|-----|
| Annual scheduled review | Full policy review and update | CAIO | Complete within 30 days of review date |
| Material regulatory change (EU AI Act amendment, new NIST guidance) | Impact assessment + targeted update | Compliance Lead | Assess within 15 days; update within 30 days |
| Sev1 incident | Root cause analysis → policy gap analysis → update if needed | CAIO | Complete within 30 days of incident closure |
| New risk tier or agent type | Classification review + control requirements update | Governance Council | Before deployment approval |
| ISO 42001 audit finding | Corrective action → policy update if systemic | CAIO | Per audit finding timeline |

**Governance framework changelog:** [Framework Changelog](05-cross-cutting/governance-framework-changelog.md)

---

## Supporting Artifact Map

| Artifact | Location |
|----------|----------|
| Governance Council Charter | `05-cross-cutting/ai-governance-council-charter.md` |
| Roles & RACI | `05-cross-cutting/governance-roles-raci.md` |
| Agent Tier Classification | `01-discovery-governance/templates/agent-tier-classification.yaml` |
| EU AI Act Risk Classification | `01-discovery-governance/checklists/eu-ai-act-risk-classification.yaml` |
| Model Card Template | `02-development-governance/templates/model-card.md` |
| Eval-Driven Development | `02-development-governance/guides/eval-driven-development.md` |
| Safety Agent Architecture | `03-runtime-governance/agentic-workflows/customer-facing-agent-safety.md` |
| Human Oversight Protocol | `03-runtime-governance/human-oversight-protocol.md` |
| Continuous Monitoring Plan | `04-operational-governance/guides/continuous-monitoring-plan.md` |
| Incident Response Playbook | `04-operational-governance/guides/incident-response-playbook.md` |
| Third-Party Vendor Controls | `05-cross-cutting/third-party-ai-vendor-controls.md` |
| Regulatory Reference Index | `05-cross-cutting/regulatory-reference-index.md` |
| ISO 42001 Gap Analysis | `../docs/iso-42001-gap-analysis.md` |
| Governance by Stage Framework | `../docs/governance-by-stage-framework.md` |
| AI Risk Appetite Framework | `06-executive/ai-risk-appetite-framework.md` |
| Quarterly Governance Report | `06-executive/quarterly-governance-report.md` |

---

## Approval Record

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Board Sponsor** | _________________ | _________________ | ____-__-__ |
| **CAIO** | _________________ | _________________ | ____-__-__ |
| **Head of Legal** | _________________ | _________________ | ____-__-__ |
| **Head of Engineering** | _________________ | _________________ | ____-__-__ |
| **Data Protection Officer** | _________________ | _________________ | ____-__-__ |

---

*This policy is a living document. It is version-controlled and auditable. Unauthorized modifications void governance compliance claims.*
