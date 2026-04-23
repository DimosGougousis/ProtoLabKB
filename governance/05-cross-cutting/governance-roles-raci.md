# Governance Roles and RACI Matrix

> **Purpose:** Provide a comprehensive RACI matrix for AI governance across the entire lifecycle, defining the CAIO role, the federated governance model, and tiered governance mapping. This is the authoritative reference for who does what, at what governance tier, and with what autonomy.
>
> **When to Use:** During project kickoff, organizational design, role assignment, governance disputes, and DNB licensing preparation. Reference this document whenever role clarity is needed at any governance tier.
>
> **Who Is Responsible:** The CAIO owns this document and ensures it reflects the current organizational reality. The AI Governance Committee reviews and approves updates annually. Each model owner uses it to confirm role assignments for their specific system.
>
> **Regulatory Basis:** SAFEST item A-04 (RACI matrix for AI lifecycle); DNB Good Practice for AI in the Financial Sector (clear accountability structures); EU AI Act Articles 14, 17, 72-73 (human oversight, quality management, governance); Wft Section 3:17 (sound business operations); ISO/IEC 42001 Section 5.1 (leadership and commitment).

---

## 1. The CAIO Role: Chief AI Officer

### 1.1 Why a CAIO

The EU AI Act, DNB Good Practice, and ISO/IEC 42001 converge on a single requirement: someone at the executive level must own enterprise AI risk end-to-end. This person is not the CTO (who owns technology delivery) or the CRO (who owns enterprise risk broadly). The CAIO is the executive who bridges technology, risk, ethics, and business strategy for AI specifically.

In smaller FinTechs (under 50 employees), the CAIO function may be combined with the CTO or CRO role, but the mandate and accountability described below must still be explicitly assigned and documented. DNB will test this during licensing.

### 1.2 CAIO Mandate

| Dimension | Mandate |
|-----------|---------|
| **Authority** | Board-delegated authority to approve or block AI system deployments based on governance readiness |
| **Reporting Line** | Reports directly to the CEO or Board; not subordinate to the CTO |
| **Scope** | All AI and ML systems across the enterprise, including third-party AI components |
| **Budget** | Owns the AI governance budget (tooling, training, external validation, audit support) |
| **Regulatory Interface** | Primary point of contact for DNB, ECB, and EBA on AI-related supervisory inquiries |

### 1.3 CAIO Responsibilities

| Category | Responsibility | SAFEST Ref |
|----------|---------------|-----------|
| **Strategy** | Define and maintain the enterprise AI strategy aligned with business objectives | A-01 |
| **Risk Appetite** | Propose AI risk appetite to the board; enforce it across the portfolio | A-03 |
| **Portfolio Oversight** | Maintain the AI system inventory; review new systems and retirements | S-01 |
| **Standards** | Approve governance standards, evaluation thresholds, and deployment criteria | A-04 |
| **Ethics** | Chair or sponsor the AI Ethics Board; ensure ethical review for high-risk systems | E-01, E-02 |
| **Talent** | Ensure AI literacy across the organization; sponsor training programs | K-09, K-11 |
| **Incident Ownership** | Own the escalation path for Severity 1 AI incidents | A-15 |
| **Board Reporting** | Deliver quarterly AI governance reports to the board | K-02 |
| **Regulatory Readiness** | Ensure the organization can demonstrate AI governance to supervisors on demand | All |

### 1.4 CAIO Success Metrics

| Metric | Target | Measurement Frequency |
|--------|--------|----------------------|
| AI system inventory completeness | 100% of production systems registered | Monthly |
| Governance gate pass rate (first attempt) | > 85% | Per deployment |
| Mean time from model change to governance approval | < 5 business days | Monthly |
| AI incidents without root cause analysis within SLA | 0 | Quarterly |
| Board AI governance report delivered on schedule | 100% | Quarterly |
| AI literacy training completion rate | > 95% of relevant staff | Annual |
| Regulatory findings related to AI governance | 0 critical findings | Annual |

---

## 2. Federated Governance Model

### 2.1 The Principle: Central Rules, Local Execution

Governance does not scale if every decision flows through a central committee. The federated model splits governance into two domains:

```
+======================================================+
|             CENTRAL GOVERNANCE (~75%)                 |
|                                                       |
|  Owned by: CAIO, AI Ethics Board, CoE                |
|                                                       |
|  - Governance policies and standards                  |
|  - Risk classification criteria                       |
|  - Evaluation thresholds and methodology              |
|  - Deployment gate criteria                           |
|  - Incident response framework                        |
|  - Regulatory compliance mapping                      |
|  - Training curricula                                 |
|  - Tool and platform standards                        |
|  - Audit and revalidation schedules                   |
+======================================================+
                        |
                        | Standards, templates, thresholds
                        v
+==========================+  +==========================+
|   LOCAL TEAM A (~25%)    |  |   LOCAL TEAM B (~25%)    |
|                          |  |                          |
|  Owned by: Squad Lead,   |  |  Owned by: Squad Lead,  |
|  Model Owner, AI Steward |  |  Model Owner, AI Steward |
|                          |  |                          |
|  - Model card authoring   |  |  - Model card authoring  |
|  - Eval suite design      |  |  - Eval suite design     |
|  - Sprint-level governance |  |  - Sprint-level governance|
|  - Monitoring config       |  |  - Monitoring config     |
|  - Incident first response |  |  - Incident first response|
|  - Local tooling choices   |  |  - Local tooling choices  |
|    (within CoE standards)  |  |    (within CoE standards) |
+==========================+  +==========================+
```

### 2.2 What the Central Body Controls (the ~75%)

| Area | Central Governance Sets | Local Teams Execute |
|------|------------------------|-------------------|
| **Risk Classification** | Classification criteria, decision tree, threshold definitions | Classify their own systems using the criteria |
| **Evaluation Standards** | Minimum eval types per risk tier, pass/fail thresholds, methodology standards | Design and run eval suites for their models within those standards |
| **Deployment Gates** | Required artifacts per risk tier, approval authority matrix | Prepare deployment packages, pass through gates |
| **Monitoring** | Required metrics, alert thresholds, dashboard templates | Configure monitoring for their systems, respond to alerts |
| **Incident Response** | Severity classification, escalation paths, SLAs, reporting templates | Execute first response, classify incidents, escalate per framework |
| **Documentation** | Model card template, data sheet template, required sections | Fill in templates for their systems |
| **Training** | Training curriculum, certification requirements, delivery schedule | Complete training, maintain certifications |
| **Tooling** | Approved tool list, integration standards, security requirements | Select tools from the approved list, configure for their use case |
| **Revalidation** | Revalidation frequency per risk tier, trigger criteria | Execute revalidations on schedule or when triggered |

### 2.3 What Local Teams Own (the ~25%)

Local teams have autonomy over implementation decisions that do not affect governance consistency:

- **Which evaluation metrics** to use beyond the mandatory set (e.g., a fraud detection team may add domain-specific precision metrics)
- **How to structure their model card** content beyond the required sections
- **Which monitoring tools** to use from the approved list
- **Sprint-level planning** of governance work (when within the sprint to complete governance tasks)
- **Technical architecture** of their AI system (within security and data governance standards)
- **Local escalation** for incidents below the central escalation threshold

### 2.4 Conflict Resolution

When a local team disagrees with a central governance standard:

1. Local team documents the objection with a rationale and proposed alternative.
2. The AI Steward submits the objection to the CoE.
3. The CoE reviews within 5 business days and either (a) grants a time-limited exception with conditions, or (b) explains why the standard must hold.
4. If the local team still disagrees, the CAIO makes the final decision.
5. All exceptions are logged in the governance exception register and reviewed quarterly.

---

## 3. Tiered Governance Model

### 3.1 Four Tiers of Governance

Governance decisions occur at different levels of the organization. Not every decision needs to reach the board, and not every decision can be made by an on-call engineer. The tiered model maps decisions to the appropriate level.

| Tier | Name | Decision Scope | Decision Makers | Frequency |
|------|------|---------------|-----------------|-----------|
| **Tier 1** | Strategic | AI strategy, risk appetite, portfolio-level decisions, high-risk system go/no-go | Board, CEO, CAIO | Quarterly + ad hoc |
| **Tier 2** | Policy | Governance policies, standards, evaluation thresholds, deployment approval for high-risk | CAIO, AI Governance Committee, AI Ethics Board | Monthly + per deployment |
| **Tier 3** | Lifecycle | Sprint-level governance execution, model development, testing, documentation | Product Manager, Engineering Lead, Model Owner, AI Steward | Per sprint |
| **Tier 4** | Runtime | Real-time monitoring, incident response, automated guardrail enforcement | MLOps Engineer, On-Call Engineer, Automated Systems | Continuous |

### 3.2 Tier-to-RACI Mapping

Each RACI activity in this document is tagged with its governance tier. This allows teams to quickly identify which activities they own autonomously (Tier 3-4) versus which require central approval (Tier 1-2).

```
Tier 1 (Strategic)     --> Board, CAIO approve
Tier 2 (Policy)        --> CAIO, Committee approve; CoE sets standards
Tier 3 (Lifecycle)     --> Local team executes within standards
Tier 4 (Runtime)       --> Automated systems + on-call execute
```

---

## 4. Role Definitions

| Abbreviation | Full Role | Reporting Line | Line of Defense | Governance Tier |
|-------------|-----------|---------------|-----------------|-----------------|
| **CAIO** | Chief AI Officer | CEO / Board | Spans 1st-2nd Line | Tier 1-2 |
| **AEB** | AI Ethics Board | Advisory to CAIO | 2nd Line | Tier 1-2 |
| **PM** | Product Manager / Product Owner | Head of Product | 1st Line | Tier 3 |
| **MLE** | ML Engineer / MLOps Engineer | Head of AI/ML | 1st Line | Tier 3-4 |
| **DS** | Data Scientist | Head of AI/ML | 1st Line | Tier 3 |
| **MO** | Model Owner | Product / Engineering | 1st Line | Tier 3 |
| **SEC** | Security Engineer | CISO | 1st Line | Tier 3-4 |
| **CO** | Compliance Officer | CRO / Head of Compliance | 2nd Line | Tier 2 |
| **RM** | Risk Manager / AI Risk Lead | CRO | 2nd Line | Tier 2 |
| **AUD** | Internal Auditor | Board / Audit Committee | 3rd Line | Tier 1-2 |
| **BOD** | Board of Directors | Shareholders | Oversight | Tier 1 |

---

## 5. Comprehensive RACI Matrix

### 5.1 Discovery Phase

**Governance Tier:** Tier 1 (Strategic) + Tier 2 (Policy)

| Activity | CAIO | AEB | PM | MLE | DS | MO | SEC | CO | RM | AUD | BOD | Tier |
|----------|------|-----|----|-----|----|----|----|----|----|-----|-----|------|
| Identify AI opportunity | I | I | **R** | C | C | -- | -- | I | I | -- | -- | T3 |
| Risk classification (EU AI Act) | **A** | C | **R** | C | C | -- | -- | C | C | -- | I | T2 |
| Ethics screening | **A** | **R** | C | I | C | -- | -- | C | C | -- | I | T2 |
| Prohibited uses check (E-03) | I | C | **R** | -- | -- | -- | -- | **A** | C | -- | -- | T2 |
| Data privacy impact | I | C | C | I | **R** | -- | C | C | I | -- | -- | T2 |
| Go/no-go decision (high-risk) | **A** | C | I | I | I | -- | -- | C | C | I | I | T1 |
| Go/no-go decision (limited/min) | **A** | I | I | I | I | -- | -- | C | C | -- | -- | T2 |
| Stakeholder impact assessment | I | C | **R** | I | C | -- | -- | C | I | -- | -- | T2 |

### 5.2 Design Phase

**Governance Tier:** Tier 2 (Policy) + Tier 3 (Lifecycle)

| Activity | CAIO | AEB | PM | MLE | DS | MO | SEC | CO | RM | AUD | BOD | Tier |
|----------|------|-----|----|-----|----|----|----|----|----|-----|-----|------|
| Define acceptance criteria | **A** | I | **R** | C | **R** | C | -- | C | I | -- | -- | T3 |
| Design HITL mechanism (A-06) | **A** | C | **R** | **R** | C | C | -- | C | C | -- | -- | T2 |
| Design fallback / kill switch | **A** | I | I | **R** | C | C | C | I | C | -- | -- | T3 |
| Design explainability approach | **A** | C | I | C | **R** | C | -- | I | I | -- | -- | T3 |
| Design audit trail architecture | **A** | I | I | **R** | I | C | **R** | C | I | I | -- | T3 |
| Plan customer transparency | **A** | C | **R** | I | I | C | -- | **R** | I | -- | -- | T2 |
| Conduct DPIA (if personal data) | I | I | C | I | C | I | C | C | I | -- | -- | T2 |
| Create initial model card (T-12) | **A** | I | I | C | **R** | C | -- | I | I | -- | -- | T3 |

### 5.3 Development Phase

**Governance Tier:** Tier 3 (Lifecycle)

| Activity | CAIO | AEB | PM | MLE | DS | MO | SEC | CO | RM | AUD | BOD | Tier |
|----------|------|-----|----|-----|----|----|----|----|----|-----|-----|------|
| Build model / agent logic | I | -- | I | **R** | **R** | C | -- | -- | -- | -- | -- | T3 |
| Build evaluation pipeline | **A** | -- | I | **R** | **R** | C | -- | I | I | -- | -- | T3 |
| Run pre-deployment evals (S-03) | **A** | -- | I | **R** | **R** | C | -- | I | I | -- | -- | T3 |
| Bias and fairness testing (F-03) | I | C | I | C | **R** | C | -- | C | **A** | -- | -- | T3 |
| Stress testing (S-05) | **A** | -- | I | **R** | **R** | C | C | I | C | -- | -- | T3 |
| Adversarial testing (S-06) | **A** | -- | I | **R** | **R** | C | **R** | I | C | -- | -- | T3 |
| Implement guardrails | **A** | I | I | **R** | C | C | **R** | I | C | -- | -- | T3 |
| Independent validation (high-risk) | **A** | -- | -- | I | I | I | -- | I | **R** | I | -- | T2 |
| Complete model card | **A** | I | I | C | **R** | C | -- | I | I | -- | -- | T3 |

### 5.4 Testing Phase

**Governance Tier:** Tier 3 (Lifecycle) + Tier 2 (Policy)

| Activity | CAIO | AEB | PM | MLE | DS | MO | SEC | CO | RM | AUD | BOD | Tier |
|----------|------|-----|----|-----|----|----|----|----|----|-----|-----|------|
| Integration / system testing | I | -- | I | **R** | C | C | C | I | I | -- | -- | T3 |
| Full eval suite execution | **A** | -- | I | **R** | **R** | C | -- | I | I | -- | -- | T3 |
| UAT with governance criteria | **A** | I | **R** | I | I | C | -- | I | I | -- | -- | T3 |
| Validate fallback / kill switch | **A** | -- | I | **R** | I | C | C | I | C | -- | -- | T3 |
| Review test coverage vs. governance | **A** | I | I | I | I | C | C | C | **R** | I | -- | T2 |
| Prepare deployment package | I | -- | I | C | C | **R** | I | C | C | -- | -- | T3 |

### 5.5 Deployment Phase

**Governance Tier:** Tier 2 (Policy) + Tier 4 (Runtime)

| Activity | CAIO | AEB | PM | MLE | DS | MO | SEC | CO | RM | AUD | BOD | Tier |
|----------|------|-----|----|-----|----|----|----|----|----|-----|-----|------|
| Deployment approval (high-risk) | **A** | C | I | I | I | **R** | I | C | C | I | I | T2 |
| Deployment approval (limited/min) | I | -- | I | I | I | **R** | I | I | I | -- | -- | T3 |
| Execute production deployment | I | -- | I | **R** | I | C | I | -- | -- | -- | -- | T4 |
| Post-deployment health checks | **A** | -- | I | **R** | C | C | I | -- | -- | -- | -- | T4 |
| Activate monitoring and alerts | **A** | -- | I | **R** | I | C | I | -- | -- | -- | -- | T4 |
| Update AI system inventory | I | -- | I | C | I | **R** | -- | I | I | C | -- | T3 |
| Record deployment in change log | **A** | -- | I | **R** | I | C | -- | I | I | -- | -- | T3 |

### 5.6 Monitoring Phase

**Governance Tier:** Tier 4 (Runtime) + Tier 3 (Lifecycle)

| Activity | CAIO | AEB | PM | MLE | DS | MO | SEC | CO | RM | AUD | BOD | Tier |
|----------|------|-----|----|-----|----|----|----|----|----|-----|-----|------|
| Monitor performance metrics | **A** | -- | I | **R** | C | C | -- | I | I | -- | -- | T4 |
| Monitor data drift (S-12) | **A** | -- | I | **R** | C | C | -- | I | C | -- | -- | T4 |
| Monitor fairness metrics (F-11) | I | I | I | **R** | C | C | -- | C | **A** | -- | -- | T4 |
| Triage and respond to alerts | **A** | -- | I | **R** | C | C | C | I | C | -- | -- | T4 |
| Incident response (Sev 1-2) | **A** | I | I | **R** | C | C | **R** | **R** | C | I | I | T2 |
| Incident response (Sev 3-4) | I | -- | I | **R** | C | C | C | I | I | -- | -- | T3 |
| Periodic monitoring reports | **A** | -- | I | **R** | I | C | -- | I | C | -- | -- | T3 |
| Audit trail integrity check | **A** | -- | -- | **R** | -- | C | C | I | I | C | -- | T3 |

### 5.7 Revalidation Phase

**Governance Tier:** Tier 2 (Policy) + Tier 3 (Lifecycle)

| Activity | CAIO | AEB | PM | MLE | DS | MO | SEC | CO | RM | AUD | BOD | Tier |
|----------|------|-----|----|-----|----|----|----|----|----|-----|-----|------|
| Identify revalidation trigger | **A** | -- | I | **R** | **R** | C | -- | I | C | -- | -- | T3 |
| Execute revalidation evals | **A** | -- | I | **R** | **R** | C | -- | I | I | -- | -- | T3 |
| Independent re-validation (high-risk) | **A** | -- | -- | I | I | I | -- | I | **R** | I | -- | T2 |
| Champion-challenger comparison | **A** | -- | I | **R** | **R** | C | -- | I | C | -- | -- | T3 |
| Approve redeployment | **A** | I | I | I | I | **R** | I | C | C | I | -- | T2 |
| Update model card and change log | **A** | -- | I | C | **R** | C | -- | I | I | -- | -- | T3 |

### 5.8 Retirement Phase

**Governance Tier:** Tier 1 (Strategic) + Tier 2 (Policy)

| Activity | CAIO | AEB | PM | MLE | DS | MO | SEC | CO | RM | AUD | BOD | Tier |
|----------|------|-----|----|-----|----|----|----|----|----|-----|-----|------|
| Identify retirement trigger | **A** | I | **R** | I | C | C | -- | C | C | -- | I | T1 |
| Assess dependent system impact | **A** | -- | C | **R** | C | C | C | I | C | -- | -- | T2 |
| Plan customer communication | I | C | **R** | I | -- | C | -- | **A** | I | -- | -- | T2 |
| Execute data retention / deletion | I | -- | I | **R** | I | C | C | C | I | I | -- | T2 |
| Archive model artifacts | **A** | -- | I | **R** | **R** | C | -- | I | I | -- | -- | T3 |
| Update inventory (mark retired) | I | -- | I | I | I | **R** | -- | I | I | C | -- | T3 |
| Produce retirement summary | **A** | I | I | I | C | **R** | -- | C | C | I | -- | T2 |

---

## 6. Governance Activities Summary by Tier

### Tier 1: Strategic Governance

Activities requiring Board or C-suite involvement:

- AI strategy approval and annual review
- Enterprise AI risk appetite setting
- Portfolio-level go/no-go for high-risk AI systems
- Strategic retirement decisions with business impact
- Annual AI governance effectiveness assessment
- Regulatory engagement strategy (DNB SRE preparation)

### Tier 2: Policy Governance

Activities requiring CAIO, Committee, or CoE approval:

- Governance policy creation and updates
- Risk classification criteria changes
- Evaluation threshold adjustments
- Deployment approval for high-risk systems
- Incident classification and regulatory reporting
- Ethics review outcomes
- Independent model validation results
- Revalidation approval for high-risk systems

### Tier 3: Lifecycle Governance

Activities executed by local teams within central standards:

- Sprint-level governance planning and execution
- Model card creation and updates
- Eval suite design and execution
- Bias testing execution
- Deployment package preparation
- Monitoring configuration
- Documentation maintenance
- Deployment approval for limited/minimal risk systems

### Tier 4: Runtime Governance

Activities executed by automated systems and on-call engineers:

- Real-time performance monitoring
- Data drift detection and alerting
- Guardrail enforcement (input/output filtering)
- Automated kill switch activation
- Incident first response
- Automated rollback on health check failure
- Audit trail logging

---

## 7. FinTech Application Example

### Scenario: Mid-Size Dutch FinTech (60 staff, 15 AI models)

**Role mapping:**

| RACI Role | Person | Notes |
|-----------|--------|-------|
| CAIO | VP of AI (reports to CEO) | Dedicated role; not combined with CTO |
| AEB | 3-person advisory panel (external ethicist, Head of Compliance, CAIO) | Meets monthly |
| PM | 3 Product Managers (Payments, Lending, Compliance) | One per product area |
| MLE | 5 ML Engineers + 2 MLOps Engineers | Across 3 product squads |
| DS | 3 Data Scientists | Embedded in product squads |
| MO | 5 Model Owners (senior engineers or PMs) | One per AI model cluster |
| SEC | 1 Security Engineer | Shared across all squads |
| CO | 1 Compliance Officer | Reports to CRO |
| RM | 1 AI Risk Analyst | Reports to CRO, performs independent validation |
| AUD | External audit firm | Annual AI governance audit + quarterly check-ins |
| BOD | 3-person board | One member with AI competency (K-01) |

**Tier allocation for their 15 models:**

| Risk Tier | Number of Models | Governance Tier Focus | Example |
|-----------|-----------------|----------------------|---------|
| High Risk | 3 | Tier 1-2 (central approval) | Credit scoring, AML screening, fraud detection |
| Limited Risk | 7 | Tier 2-3 (CoE standards, local execution) | Customer chatbot, transaction categorization, KYC document extraction |
| Minimal Risk | 5 | Tier 3-4 (local autonomy) | Internal log anomaly detection, developer productivity tools, internal search |

**Federated governance in practice:**

- The CoE (CAIO + 1 AI Risk Analyst) sets the evaluation thresholds, model card template, and deployment criteria for all 15 models.
- Each product squad runs their own eval suites, writes their own model cards, and manages their own monitoring within those standards.
- The 3 high-risk models require Tier 2 deployment approval from the CAIO + Compliance Officer.
- The 7 limited-risk models follow a streamlined Tier 3 approval by the Model Owner + AI Steward.
- The 5 minimal-risk models are deployed by the team with post-deployment notification to the CAIO.

---

## 8. RACI Validation Checklist

Use this checklist to verify your RACI matrix is sound:

| # | Check | Status |
|---|-------|--------|
| 1 | Every activity has exactly one **A** (Accountable) | [ ] |
| 2 | Every activity has at least one **R** (Responsible) | [ ] |
| 3 | No role is both **R** and **A** for the same activity unless justified | [ ] |
| 4 | 2nd Line roles are never **R** for building or operating AI systems | [ ] |
| 5 | 3rd Line roles are never **R** for anything except audit and assurance | [ ] |
| 6 | The CAIO has **A** for all Tier 1-2 governance decisions | [ ] |
| 7 | Local teams have **R** for Tier 3-4 activities without central bottleneck | [ ] |
| 8 | Every role abbreviation maps to a named individual in the organization | [ ] |
| 9 | The matrix has been reviewed with all **R** and **A** role holders | [ ] |
| 10 | The matrix aligns with the 3LoD model documented in three-lines-of-defense-for-ai.md | [ ] |

---

## Cross-References

- **RACI by AI Lifecycle Stage:** [../07-enterprise-implementation/organizational-model/raci-by-ai-lifecycle-stage.md](../07-enterprise-implementation/organizational-model/raci-by-ai-lifecycle-stage.md) -- detailed per-stage RACI with all role abbreviations
- **Three Lines of Defense:** [../07-enterprise-implementation/organizational-model/three-lines-of-defense-for-ai.md](../07-enterprise-implementation/organizational-model/three-lines-of-defense-for-ai.md) -- how roles map to defense lines
- **AI Center of Excellence:** [../07-enterprise-implementation/organizational-model/ai-center-of-excellence.md](../07-enterprise-implementation/organizational-model/ai-center-of-excellence.md) -- the CoE that operationalizes federated governance
- **Risk Tiering Model:** [../07-enterprise-implementation/risk-based-adoption/risk-tiering-model.md](../07-enterprise-implementation/risk-based-adoption/risk-tiering-model.md) -- determines governance intensity per RACI activity
- **Governance in Agile Sprints:** [../07-enterprise-implementation/process-integration/governance-in-agile-sprints.md](../07-enterprise-implementation/process-integration/governance-in-agile-sprints.md) -- how Tier 3 RACI activities flow into sprints
- **SAFEST to Four Pillars Mapping:** [safest-to-four-pillars-mapping.yaml](safest-to-four-pillars-mapping.yaml) -- connects RACI activities to SAFEST checklist items
- **Glossary:** [glossary.md](glossary.md) -- definitions for all governance terms used in this document
- **Regulatory Reference Index:** [regulatory-reference-index.md](regulatory-reference-index.md) -- full regulatory citations

---

*Last updated: 2026-03-01*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
