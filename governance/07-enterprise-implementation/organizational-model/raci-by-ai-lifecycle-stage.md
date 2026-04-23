# RACI Matrix by AI Lifecycle Stage

> **Purpose:** Define who is Responsible, Accountable, Consulted, and Informed for every governance activity at each stage of the AI lifecycle, providing a single reference for role clarity across the entire lifespan of an AI system.
>
> **When to Use:** During project kickoff for any new AI system, during organizational design for AI governance, and when resolving role ambiguity at any lifecycle stage. Reference this matrix when preparing for DNB licensing interviews to demonstrate clear accountability.
>
> **Who Is Responsible:** The CAIO (Chief AI Officer) owns this matrix organizationally. Each AI system's model owner uses it to confirm role assignments for their specific system. The AI Governance Committee reviews and approves updates to this matrix annually.
>
> **Regulatory Basis:** SAFEST item A-04 (RACI matrix for AI lifecycle); DNB Good Practice for AI (clear accountability structures); EU AI Act Articles 14, 17 (human oversight and quality management); Wft Section 3:17 (sound business operations).

---

## 1. How to Read This Matrix

Each cell contains one or more RACI designations:

| Code | Meaning | Rule |
|------|---------|------|
| **R** | Responsible -- does the work | At least one R per activity |
| **A** | Accountable -- owns the outcome, approves the work | Exactly one A per activity |
| **C** | Consulted -- provides input before the work is done | Two-way communication |
| **I** | Informed -- notified after the work is done | One-way communication |

**Key constraint:** Every activity has exactly one **A**. Having two accountable parties means no one is accountable.

---

## 2. Role Definitions

| Abbreviation | Role | Typical Reporting Line | Line of Defense |
|-------------|------|----------------------|-----------------|
| **PM** | Product Manager / Product Owner | Head of Product | 1st Line |
| **EL** | Engineering Lead / Tech Lead | CTO / VP Engineering | 1st Line |
| **DS** | Data Scientist | Head of AI/ML | 1st Line |
| **MLE** | ML Engineer / MLOps Engineer | Head of AI/ML | 1st Line |
| **CO** | Compliance Officer | Head of Compliance / CRO | 2nd Line |
| **RM** | Risk Manager / AI Risk Lead | CRO | 2nd Line |
| **CAIO** | Chief AI Officer | CEO / Board | Spans 1st-2nd Line |
| **DPO** | Data Protection Officer | Board (independent) | 2nd Line |
| **AIS** | AI Steward (governance coordinator per squad) | Product / Engineering | 1st Line |
| **AUD** | Internal Auditor | Board / Audit Committee | 3rd Line |

**Note on the CAIO role:** In smaller FinTechs, the CAIO function may be combined with the CTO or CRO role. Regardless of title, the accountability expectations in this matrix apply to whoever holds the CAIO function. DNB will assess whether the person exercising this function has the authority, competence, and independence required.

---

## 3. Tiered Governance Alignment

Each lifecycle stage maps to one or more governance tiers in the federated governance model. The central governance body (Tier 1-2) sets approximately 75% of rules; local teams (Tier 3-4) execute autonomously within those boundaries.

| Governance Tier | Scope | Primary Lifecycle Stages |
|----------------|-------|------------------------|
| **Tier 1: Strategic** | Board and C-suite; AI strategy, risk appetite, portfolio decisions | Ideation (go/no-go), Retirement (strategic decommission) |
| **Tier 2: Policy** | AI Governance Committee; policies, standards, approval thresholds | Design (policy compliance), Deployment (approval), Retraining (trigger criteria) |
| **Tier 3: Lifecycle** | Product and engineering leads; execution of governance within sprints | Data Preparation, Development, Testing, Monitoring |
| **Tier 4: Runtime** | On-call engineers, automated systems; real-time enforcement | Monitoring (live), Deployment (canary/rollback) |

---

## 4. RACI Matrix: Stage 1 -- Ideation

**Governance Tier:** Tier 1 (Strategic) + Tier 2 (Policy)

**Three Lines of Defense:** 1st Line proposes; 2nd Line challenges and advises; 3rd Line not typically involved.

| Activity | PM | EL | DS | MLE | CO | RM | CAIO | DPO | AIS | AUD |
|----------|----|----|----|----|----|----|------|-----|-----|-----|
| Identify AI opportunity and business case | **R** | C | C | I | I | I | I | I | I | -- |
| Conduct initial risk classification (EU AI Act) | **R** | C | C | -- | **A** | C | I | C | I | -- |
| Screen against prohibited AI uses list (E-03) | **R** | I | I | -- | **A** | C | I | C | -- | -- |
| Assess ethical implications (E-02) | C | I | C | -- | C | C | **A** | **R** | I | -- |
| Evaluate data availability and privacy impact | C | C | **R** | I | I | I | I | **A** | I | -- |
| Submit ideation proposal to Governance Committee | **R** | C | C | -- | C | C | **A** | I | I | -- |
| Go/no-go decision | I | I | I | -- | C | C | **A** | C | I | I |

**Agent-specific activities at Ideation:**
- Define agent autonomy boundaries (what the agent may decide vs. what requires human approval)
- Map delegation chains for multi-agent systems
- Identify tool-use permissions and data access scope

---

## 5. RACI Matrix: Stage 2 -- Design

**Governance Tier:** Tier 2 (Policy) + Tier 3 (Lifecycle)

**Three Lines of Defense:** 1st Line designs; 2nd Line reviews design against policy; 3rd Line not typically involved.

| Activity | PM | EL | DS | MLE | CO | RM | CAIO | DPO | AIS | AUD |
|----------|----|----|----|----|----|----|------|-----|-----|-----|
| Define acceptance criteria and evaluation strategy | **R** | C | **R** | C | C | I | **A** | I | C | -- |
| Select algorithm approach and document rationale (S-02) | I | C | **R** | C | I | I | **A** | I | I | -- |
| Design human-in-the-loop mechanism (A-06, A-07) | **R** | **R** | C | C | C | C | **A** | I | I | -- |
| Design fallback and kill-switch mechanism (S-13, A-09) | I | **R** | C | **R** | I | C | **A** | I | I | -- |
| Design explainability approach (T-01) | I | C | **R** | C | I | I | **A** | I | I | -- |
| Plan customer transparency mechanism (T-06, T-07) | **R** | C | I | I | **R** | I | **A** | C | I | -- |
| Conduct DPIA if personal data involved (T-10) | C | C | C | I | C | I | I | **A** | I | -- |
| Design audit trail and logging architecture (A-11) | I | **R** | I | **R** | C | I | **A** | C | I | I |
| Create initial model card (T-12) | I | I | **R** | C | I | I | **A** | I | C | -- |

**Agent-specific activities at Design:**
- Design agent permission boundaries and escalation triggers
- Architect multi-agent communication governance (message logging, delegation approval)
- Design guardrail configuration approach (input/output filtering, tool-use constraints)

---

## 6. RACI Matrix: Stage 3 -- Data Preparation

**Governance Tier:** Tier 3 (Lifecycle)

**Three Lines of Defense:** 1st Line executes; 2nd Line sets data quality standards; 3rd Line audits data governance.

| Activity | PM | EL | DS | MLE | CO | RM | CAIO | DPO | AIS | AUD |
|----------|----|----|----|----|----|----|------|-----|-----|-----|
| Source and acquire training data | I | I | **R** | C | I | I | **A** | C | I | -- |
| Verify data lineage and legal basis for use | I | I | **R** | I | C | I | I | **A** | I | -- |
| Conduct proxy variable analysis (F-02) | I | I | **R** | I | C | **A** | I | C | I | -- |
| Document data quality metrics and thresholds | I | I | **R** | C | I | C | **A** | I | C | -- |
| Implement data quality checks | I | C | **R** | **R** | I | I | **A** | I | I | -- |
| Complete data sheet documentation | I | I | **R** | I | I | I | **A** | C | C | -- |
| Review data for protected characteristics (F-01) | I | I | **R** | I | C | **A** | I | C | I | -- |

---

## 7. RACI Matrix: Stage 4 -- Development

**Governance Tier:** Tier 3 (Lifecycle)

**Three Lines of Defense:** 1st Line builds; 2nd Line validates (high-risk only); 3rd Line not typically involved.

| Activity | PM | EL | DS | MLE | CO | RM | CAIO | DPO | AIS | AUD |
|----------|----|----|----|----|----|----|------|-----|-----|-----|
| Implement model / agent logic | I | C | **R** | **R** | -- | -- | I | -- | I | -- |
| Build evaluation pipeline | I | C | **R** | **R** | I | I | **A** | -- | I | -- |
| Run pre-deployment evaluations (S-03) | I | I | **R** | **R** | I | I | **A** | -- | C | -- |
| Conduct bias and fairness testing (F-03) | I | I | **R** | C | C | **A** | I | C | I | -- |
| Perform stress testing (S-05) | I | C | **R** | **R** | I | C | **A** | -- | I | -- |
| Perform adversarial robustness testing (S-06) | I | C | **R** | **R** | I | C | **A** | -- | I | -- |
| Implement guardrails for agents (input/output filters) | I | **R** | C | **R** | I | C | **A** | I | I | -- |
| Complete model card with development details (T-12) | I | I | **R** | C | I | I | **A** | I | C | -- |
| Peer review of model and code | I | **R** | C | C | -- | -- | I | -- | I | -- |
| Independent model validation -- high risk only (S-19) | -- | I | I | I | I | **R** | **A** | -- | I | I |

**Agent-specific activities at Development:**
- Implement tool-use permission enforcement
- Build agent delegation chain logging
- Test agent behavior under adversarial prompts (prompt injection, jailbreak)
- Validate agent boundary adherence (does it stay within defined permissions?)

---

## 8. RACI Matrix: Stage 5 -- Testing

**Governance Tier:** Tier 3 (Lifecycle) + Tier 2 (Policy, for approval gates)

**Three Lines of Defense:** 1st Line tests; 2nd Line reviews test adequacy and results; 3rd Line may audit test processes.

| Activity | PM | EL | DS | MLE | CO | RM | CAIO | DPO | AIS | AUD |
|----------|----|----|----|----|----|----|------|-----|-----|-----|
| Execute integration and system testing | I | **R** | C | **R** | I | I | I | -- | I | -- |
| Execute end-to-end evaluation suite | I | I | **R** | **R** | I | I | **A** | -- | C | -- |
| Conduct user acceptance testing (UAT) | **R** | C | I | I | I | I | **A** | I | I | -- |
| Validate fallback and kill-switch functionality (S-13, A-09) | I | **R** | I | **R** | I | C | **A** | -- | I | -- |
| Review test coverage against governance requirements | I | I | I | I | C | **R** | **A** | C | C | I |
| Prepare deployment approval package | I | C | **R** | C | C | C | **A** | I | **R** | -- |
| Submit package to AI Governance Committee | I | I | I | I | C | C | **A** | I | **R** | I |

---

## 9. RACI Matrix: Stage 6 -- Deployment

**Governance Tier:** Tier 2 (Policy, for approval) + Tier 4 (Runtime, for execution)

**Three Lines of Defense:** 1st Line deploys; 2nd Line approves (per risk tier); 3rd Line audits deployment process.

| Activity | PM | EL | DS | MLE | CO | RM | CAIO | DPO | AIS | AUD |
|----------|----|----|----|----|----|----|------|-----|-----|-----|
| Obtain deployment approval (risk-tier dependent) | I | I | I | I | C | C | **A** | I | **R** | I |
| Execute production deployment (canary/blue-green) | I | C | I | **R** | I | I | I | -- | I | -- |
| Verify production health checks post-deployment | I | C | I | **R** | I | I | **A** | -- | I | -- |
| Activate monitoring dashboards and alerts | I | C | I | **R** | I | I | **A** | -- | I | -- |
| Update AI system inventory (S-01) | I | I | I | C | I | I | I | -- | **R** | **A** |
| Notify customers of AI interaction (T-06, if applicable) | **R** | I | I | I | **A** | I | I | C | I | -- |
| Record deployment in model change log (A-12) | I | I | I | **R** | I | I | **A** | -- | C | -- |
| Conduct post-deployment verification (smoke tests) | I | C | **R** | **R** | I | I | **A** | -- | I | -- |

**Agent-specific activities at Deployment:**
- Verify agent permission boundaries are enforced in production
- Confirm guardrail configurations are active
- Validate agent escalation paths route to correct human reviewers

---

## 10. RACI Matrix: Stage 7 -- Monitoring

**Governance Tier:** Tier 4 (Runtime) + Tier 3 (Lifecycle, for response)

**Three Lines of Defense:** 1st Line monitors and responds; 2nd Line oversees thresholds and escalations; 3rd Line audits monitoring adequacy.

| Activity | PM | EL | DS | MLE | CO | RM | CAIO | DPO | AIS | AUD |
|----------|----|----|----|----|----|----|------|-----|-----|-----|
| Monitor model performance metrics (S-03) | I | I | C | **R** | I | I | **A** | -- | I | -- |
| Monitor data drift indicators (S-12) | I | I | C | **R** | I | C | **A** | -- | I | -- |
| Monitor fairness metrics in production (F-11) | I | I | C | **R** | C | **A** | I | I | I | -- |
| Review monitoring dashboards (T-17) | I | I | C | C | C | **R** | **A** | I | I | -- |
| Triage and respond to alerts | I | C | C | **R** | I | C | **A** | -- | I | -- |
| Execute incident response if triggered (A-15) | I | **R** | C | **R** | **R** | C | **A** | C | I | I |
| Produce periodic monitoring reports | I | I | I | **R** | I | C | **A** | -- | C | -- |
| Maintain audit trail integrity (A-11) | I | C | I | **R** | I | I | **A** | C | I | C |

**Agent-specific activities at Monitoring:**
- Monitor agent decision patterns for scope creep (agent taking actions beyond defined boundaries)
- Track delegation chain execution and failure rates
- Monitor guardrail trigger rates (are guardrails firing too often or too rarely?)
- Review agent-to-agent communication logs for anomalies

---

## 11. RACI Matrix: Stage 8 -- Retraining

**Governance Tier:** Tier 2 (Policy, for trigger criteria) + Tier 3 (Lifecycle, for execution)

**Three Lines of Defense:** 1st Line retrains; 2nd Line validates retraining triggers and results; 3rd Line audits retraining governance.

| Activity | PM | EL | DS | MLE | CO | RM | CAIO | DPO | AIS | AUD |
|----------|----|----|----|----|----|----|------|-----|-----|-----|
| Identify retraining trigger (drift, performance, schedule) | I | I | **R** | **R** | I | C | **A** | -- | I | -- |
| Prepare and validate new training data | I | I | **R** | C | I | I | **A** | C | I | -- |
| Execute retraining pipeline | I | I | **R** | **R** | I | I | **A** | -- | I | -- |
| Run regression evaluations (S-03) | I | I | **R** | **R** | I | I | **A** | -- | C | -- |
| Run champion-challenger comparison (S-22) | I | I | **R** | **R** | I | C | **A** | -- | I | -- |
| Conduct independent re-validation -- high risk (S-19) | -- | I | I | I | I | **R** | **A** | -- | I | I |
| Approve retraining deployment (CAB process) | I | I | I | I | C | C | **A** | I | **R** | I |
| Update model card and change log (T-12, A-12) | I | I | **R** | C | I | I | **A** | I | C | -- |

---

## 12. RACI Matrix: Stage 9 -- Retirement

**Governance Tier:** Tier 1 (Strategic, for portfolio impact) + Tier 2 (Policy, for process)

**Three Lines of Defense:** 1st Line executes; 2nd Line ensures compliance; 3rd Line audits completeness.

| Activity | PM | EL | DS | MLE | CO | RM | CAIO | DPO | AIS | AUD |
|----------|----|----|----|----|----|----|------|-----|-----|-----|
| Identify retirement trigger (obsolescence, risk, regulation) | **R** | C | C | I | C | C | **A** | I | I | -- |
| Assess impact on dependent systems and agents | C | **R** | C | **R** | I | C | **A** | I | I | -- |
| Plan customer communication (if applicable) | **R** | I | I | I | **A** | I | I | C | I | -- |
| Execute data retention and deletion per GDPR | I | C | I | **R** | C | I | I | **A** | I | I |
| Archive model artifacts, model card, and audit trail | I | I | **R** | **R** | I | I | **A** | I | C | -- |
| Update AI system inventory (mark as retired) | I | I | I | I | I | I | I | -- | **R** | **A** |
| Deactivate monitoring and alerting | I | C | I | **R** | I | I | **A** | -- | I | -- |
| Confirm retirement completeness | I | I | I | I | C | C | **A** | C | **R** | I |
| Produce retirement summary for Governance Committee | I | I | C | I | C | C | **A** | I | **R** | I |

---

## 13. Three Lines of Defense Summary by Stage

| Lifecycle Stage | 1st Line (Build, Operate) | 2nd Line (Oversee, Challenge) | 3rd Line (Assure) |
|----------------|--------------------------|-------------------------------|-------------------|
| Ideation | Proposes use case, initial risk tier | Challenges risk classification, ethical review | -- |
| Design | Designs system, defines evals | Reviews against policy, approves DPIA | -- |
| Data Preparation | Sources and prepares data | Sets data quality standards, reviews proxy analysis | -- |
| Development | Builds and tests model/agent | Independent validation (high-risk) | -- |
| Testing | Executes test suites, prepares package | Reviews test adequacy, approves deployment | May audit test process |
| Deployment | Deploys to production | Approves per risk tier | Audits deployment process |
| Monitoring | Monitors and responds to alerts | Oversees thresholds, reviews dashboards | Audits monitoring adequacy |
| Retraining | Retrains and validates | Re-validates (high-risk), approves redeployment | Audits retraining governance |
| Retirement | Executes retirement plan | Ensures compliance | Audits completeness |

---

## 14. Customization Guide

This RACI matrix is a template. Adapt it to your organization:

### Step 1: Map Roles to People

Create a separate document mapping each RACI role abbreviation to named individuals in your organization. In smaller FinTechs, one person may hold multiple roles (e.g., the CTO may also serve as CAIO), but document this explicitly so DNB can assess whether conflicts of interest exist.

### Step 2: Adjust for Organizational Structure

| If your organization... | Then adjust... |
|------------------------|---------------|
| Has no dedicated Data Scientist role | Merge DS activities into MLE |
| Has a separate Model Validation team | Add MV column; move 2nd-line validation activities from RM to MV |
| Uses external auditors for 3rd line | AUD column maps to the external audit firm's engagement lead |
| Has a dedicated AI Ethics board | Add ETH column; move ethical review activities from DPO |
| Operates a central AI platform team | Split MLE into Platform Engineer and Application ML Engineer |

### Step 3: Validate with Stakeholders

Walk through each lifecycle stage with the people assigned to R and A roles. Confirm they understand their responsibilities and have the authority and resources to fulfil them. Document any gaps and address them before seeking regulatory approval.

### Step 4: Review and Update

| Review Trigger | Action |
|---------------|--------|
| New AI system enters the inventory | Verify RACI assignments for this system |
| Organizational restructuring | Update role mappings; revalidate RACI |
| Regulatory change (EU AI Act implementing acts) | Review whether new activities must be added |
| Annual governance review | Full RACI review at the AI Governance Committee |
| Audit finding related to role clarity | Address finding; update RACI |

---

## Cross-References

- **Three Lines of Defense:** [three-lines-of-defense-for-ai.md](three-lines-of-defense-for-ai.md) -- detailed 3LoD responsibilities that this RACI operationalizes
- **AI Governance Committee Charter:** [ai-governance-committee-charter.md](ai-governance-committee-charter.md) -- the body that approves and oversees this RACI
- **Board-Level AI Accountability:** [board-level-ai-accountability.md](board-level-ai-accountability.md) -- Tier 1 strategic governance that sits above this matrix
- **Governance in Agile Sprints:** [../process-integration/governance-in-agile-sprints.md](../process-integration/governance-in-agile-sprints.md) -- how RACI activities map into sprint ceremonies
- **Risk Tiering Model:** [../risk-based-adoption/risk-tiering-model.md](../risk-based-adoption/risk-tiering-model.md) -- determines which RACI activities apply per risk tier
- **Change Management for AI:** [../process-integration/change-management-for-ai.md](../process-integration/change-management-for-ai.md) -- CAB process that governs transitions between lifecycle stages
- **Full Governance Profile:** [../risk-based-adoption/full-governance-profile.md](../risk-based-adoption/full-governance-profile.md) -- complete artifact requirements for high-risk systems referenced in this RACI
- **SAFEST Checklist:** See the parent AIGovernance repository at `docs/06-licensing-preparation/safest-checklist-dnb-pre-application.md`

---

*Last updated: 2026-02-28*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
