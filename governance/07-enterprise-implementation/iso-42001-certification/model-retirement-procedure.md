# Model Retirement Procedure — ISO/IEC 42001 Clause 8.4

> **Purpose:** Defines the systematic process for decommissioning AI models and agents, ensuring safe retirement, knowledge preservation, and client notification per ISO/IEC 42001 Clause 8.4 (AI System Lifecycle).

**Version:** 1.0  
**Last Updated:** 2026-04-24  
**Owner:** VP of Engineering (Technical Owner)  
**Review Cycle:** Per retirement event  

---

## Retirement Triggers

A model or agent may be retired when one or more of the following conditions are met:

| Trigger | Description | Authority Required |
|---------|-------------|-------------------|
| **Performance degradation** | Accuracy falls below threshold for 2 consecutive quarters | Technical Owner |
| **Technology obsolescence** | Underlying framework or dependency no longer supported | Technical Owner |
| **Business discontinuation** | Product line or service discontinued | Policy Owner |
| **Regulatory change** | New regulation makes agent non-compliant | Compliance Officer + Policy Owner |
| **Security vulnerability** | Unpatchable vulnerability identified | Security Engineer + Safety Officer |
| **Replacement available** | New model demonstrates superior performance | Technical Owner |
| **Cost optimization** | Agent no longer cost-effective to maintain | Technical Owner + Policy Owner |

---

## Retirement Process

### Phase 1: Retirement Decision (Week 1)

| Step | Activity | Owner | Evidence |
|------|----------|-------|----------|
| 1.1 | Document retirement trigger and rationale | Technical Owner | `model-retirement-request.md` |
| 1.2 | Assess impact on clients, services, and dependencies | Product Manager | Impact assessment |
| 1.3 | Review alternative solutions (replacement, downgrade, manual process) | Technical Owner | Options analysis |
| 1.4 | Obtain approval per `aims-signing-authority-matrix.md` | Appropriate authority | Approval signature |
| 1.5 | Create retirement project plan with timeline | Project Manager | `model-retirement-plan.md` |

### Phase 2: Client and Stakeholder Notification (Week 1-2)

| Step | Activity | Owner | Evidence |
|------|----------|-------|----------|
| 2.1 | Identify all affected clients | Account Manager | Client impact list |
| 2.2 | Prepare client notification (30-day notice minimum) | Account Manager + Compliance | Notification letter |
| 2.3 | Send client notification with migration path | Account Manager | Delivery confirmation |
| 2.4 | Notify internal stakeholders (operations, support, sales) | Product Manager | Stakeholder notification log |
| 2.5 | Update client-facing documentation and portals | Technical Writer | Documentation update log |

**Client Notification Template:**

```
Subject: Service Update — Retirement of [Agent/Model Name]

Dear [Client Name],

We are writing to inform you that ProtoLabs will retire [Agent/Model Name] 
effective [Retirement Date], which is [30/60/90] days from today.

Reason for retirement: [Performance / Technology / Business / Regulatory / Security]

Impact to your service: [None / Alternative agent / Manual process / Service discontinuation]

Migration path: [Description of alternative solution, if applicable]

Timeline:
• [Date]: Final recommendations from [Agent]
• [Date]: Alternative solution available (if applicable)
• [Date]: [Agent] retired

Your data: All data associated with [Agent] will be [archived / deleted per retention policy].

For questions, contact your Account Manager or ai-governance@protolabs.com.

ProtoLabs AI Governance Office
```

### Phase 3: Knowledge Preservation (Week 2-3)

| Step | Activity | Owner | Evidence |
|------|----------|-------|----------|
| 3.1 | Archive model artifacts (weights, config, training data) | MLOps Engineer | Archive manifest |
| 3.2 | Document lessons learned and performance history | ML Engineer | `model-retirement-report.md` |
| 3.3 | Extract and preserve critical knowledge (rules, patterns, insights) | Knowledge Manager | Knowledge extraction report |
| 3.4 | Update knowledge base with retirement information | Knowledge Manager | KB update log |
| 3.5 | Archive evaluation results and benchmarks | ML Engineer | Eval archive |

### Phase 4: Dependency Management (Week 2-3)

| Step | Activity | Owner | Evidence |
|------|----------|-------|----------|
| 4.1 | Identify all upstream/downstream dependencies | Technical Owner | Dependency map |
| 4.2 | Update or remove agent from orchestration workflows | AI Engineer | Workflow update |
| 4.3 | Reconfigure router to exclude retired agent | AI Engineer | Router config update |
| 4.4 | Update tool-use risk models | Security Engineer | Risk model update |
| 4.5 | Remove agent from monitoring dashboards | MLOps Engineer | Dashboard update |

### Phase 5: Data Handling (Week 3-4)

| Step | Activity | Owner | Evidence |
|------|----------|-------|----------|
| 5.1 | Export client data per data portability requirements | DPO | Data export log |
| 5.2 | Transfer active conversations/history to replacement agent (if applicable) | MLOps Engineer | Transfer log |
| 5.3 | Archive audit logs per `aims-document-retention-schedule.md` | Compliance Officer | Archive confirmation |
| 5.4 | Securely delete model weights and training data (post-retention) | MLOps Engineer | Deletion certificate |
| 5.5 | Verify no residual data in caches, backups, or logs | Security Engineer | Verification report |

### Phase 6: System Decommissioning (Week 4)

| Step | Activity | Owner | Evidence |
|------|----------|-------|----------|
| 6.1 | Gracefully shutdown agent (drain requests, complete in-flight) | MLOps Engineer | Shutdown log |
| 6.2 | Remove agent from production environment | MLOps Engineer | Environment update |
| 6.3 | Revoke API keys and access credentials | Security Engineer | Credential revocation log |
| 6.4 | Remove agent from agent registry | Technical Owner | Registry update |
| 6.5 | Update `agent-tier-classification.yaml` | Technical Owner | Classification update |
| 6.6 | Release compute resources | MLOps Engineer | Resource release confirmation |

### Phase 7: Verification and Closure (Week 4-5)

| Step | Activity | Owner | Evidence |
|------|----------|-------|----------|
| 7.1 | Verify no production traffic routed to retired agent | MLOps Engineer | Traffic verification |
| 7.2 | Confirm all client notifications acknowledged | Account Manager | Acknowledgment log |
| 7.3 | Complete `model-retirement-checklist.md` | Project Manager | Completed checklist |
| 7.4 | Conduct post-retirement review | Technical Owner | Review meeting minutes |
| 7.5 | Archive retirement documentation | Compliance Officer | Archive confirmation |
| 7.6 | Close retirement project | Project Manager | Project closure report |

---

## Emergency Retirement

In cases of critical security vulnerability or safety issue requiring immediate retirement:

| Step | Activity | Owner | Timing |
|------|----------|-------|--------|
| E.1 | Immediate shutdown (kill switch if Tier 2/3) | Safety Officer / Security Engineer | Immediate |
| E.2 | Emergency client notification | Account Manager | Within 4 hours |
| E.3 | Incident report per `ai-incident-report.md` | Safety Officer / Security Engineer | Within 24 hours |
| E.4 | Accelerated knowledge preservation | ML Engineer | Within 48 hours |
| E.5 | Full retirement process (Phases 3-7) | Project Manager | Within 2 weeks |

---

## Retirement Checklist

- [ ] Retirement trigger documented and approved
- [ ] Client impact assessment completed
- [ ] All affected clients notified (30-day minimum notice)
- [ ] Internal stakeholders notified
- [ ] Model artifacts archived
- [ ] Lessons learned documented
- [ ] Knowledge extracted and preserved
- [ ] Dependencies updated/removed
- [ ] Router reconfigured
- [ ] Client data exported (if requested)
- [ ] Audit logs archived
- [ ] Model weights securely deleted (post-retention)
- [ ] Agent gracefully shutdown
- [ ] API keys revoked
- [ ] Agent removed from registry
- [ ] Compute resources released
- [ ] Traffic verification completed
- [ ] Post-retirement review conducted
- [ ] Retirement documentation archived

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-24 | ProtoLabs AI Governance Office | Initial retirement procedure |

---

## See Also

- `governance/07-enterprise-implementation/iso-42001-certification/aims-document-retention-schedule.md` — Retention schedule
- `governance/07-enterprise-implementation/iso-42001-certification/aims-signing-authority-matrix.md` — Signing authority
- `governance/04-operational-governance/templates/ai-incident-report.md` — Incident reporting
- `docs/iso-42001-gap-analysis.md` — Gap analysis (Clause 8.4)
