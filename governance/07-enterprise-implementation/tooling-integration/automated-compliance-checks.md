# Automated Compliance Checks

## Purpose

This document identifies which governance checklist items from the Master AI Governance Framework can be automated, how to automate them, and what the expected return on investment is. Governance works only when it is executed consistently. Manual governance processes are expensive, error-prone, and create bottlenecks. Automation transforms governance from a periodic compliance exercise into a continuous assurance system -- running checks every deployment, every commit, every hour, not just before each quarterly audit.

This document serves as the automation roadmap: for each YAML checklist, it identifies the automation candidates, recommends specific tools, defines implementation patterns, addresses false positive management, and specifies which items must remain under human review regardless of automation capability.

## When to Use

- When planning the CI/CD governance integration (see [Governance in CI/CD](../../07-enterprise-implementation/process-integration/governance-in-cicd.md))
- When evaluating tooling investments for AI governance automation
- When assessing the cost-benefit of automating specific governance activities
- When designing the evidence collection pipeline for GRC platform integration (see [GRC Platform Integration](./grc-platform-integration.md))
- When determining which governance gate checks can run without human intervention vs. which require manual review

## Who Is Responsible

| Role | R | A | C | I |
|------|---|---|---|---|
| **MLOps / Platform Engineer** | X | | | | Implements automation pipelines, maintains CI/CD hooks, monitors automation health |
| **AI Governance PM** | | X | | | Defines automation priorities; validates that automated checks meet governance intent |
| **ML Engineer** | X | | | | Implements model-specific automated evaluations (bias, performance, drift) |
| **Security Engineer** | X | | | | Implements security-focused automation (prompt injection testing, vulnerability scanning) |
| **Compliance Officer (2nd Line)** | | | X | | Consulted on whether automated evidence meets regulatory standards; approves automation scope |
| **CAIO** | | | | X | Informed of automation coverage and residual manual governance burden |

## Regulatory Basis

- **EU AI Act Article 17** -- Quality management system; automation demonstrates systematic, repeatable quality processes
- **EU AI Act Article 72** -- Post-market monitoring; automated monitoring is the only scalable approach
- **DORA Article 10** -- Detection mechanisms; automated detection is required for timely anomaly identification
- **SAFEST item T-15** -- AI performance dashboards; automated metric collection enables real-time dashboards
- **ISO/IEC 42001 Clause 9.1** -- Monitoring, measurement, analysis, and evaluation; automation enables continuous evaluation
- **Best practice** -- Manual-only governance does not scale beyond a handful of AI systems

---

## 1. Automation Maturity Levels

| Level | Name | Description | Governance Impact |
|-------|------|-------------|------------------|
| **L0** | Manual | Human performs the check, documents the result | High cost, inconsistent, bottleneck |
| **L1** | Tool-Assisted | Human runs a tool, interprets the result, makes the decision | Reduced effort, consistent methodology |
| **L2** | Semi-Automated | Tool runs automatically, human reviews the result and approves | Fast execution, human judgment retained |
| **L3** | Fully Automated** | Tool runs automatically, result auto-feeds into governance workflow, human reviews exceptions only | Continuous assurance, minimal human cost |
| **L4** | Autonomous with Override | Tool runs automatically and takes action (block deployment, trigger alert); human can override | Real-time enforcement, governance at machine speed |

**Target:** Most checklist items should reach at least L2. Security and safety-critical items should reach L4 (automated enforcement with human override).

---

## 2. Automation Candidates by Checklist

### 2.1 Pre-Deployment Gate (`pre-deployment-gate.yaml`)

| Checklist Item Category | Automation Level | Tool / Method | What Gets Automated | What Remains Manual |
|------------------------|-----------------|---------------|---------------------|-------------------|
| **Model performance metrics** | L4 | CI/CD eval pipeline (Giskard, custom eval suite) | Run eval suite against acceptance criteria; block deployment if below threshold | Setting acceptance criteria; interpreting edge case results |
| **Bias testing** | L3 | Fairlearn, Aequitas, Giskard | Run bias evaluation against protected group dimensions; generate report | Reviewing bias report for contextual fairness; deciding on acceptable trade-offs |
| **Data quality validation** | L4 | Great Expectations, Pandera, dbt tests | Validate data schemas, distributions, completeness, freshness against defined expectations | Defining data quality expectations; investigating unexpected distributions |
| **Security scanning** | L3 | Garak, custom prompt injection tests | Run adversarial test suite; report vulnerabilities found | Assessing severity and deciding on remediation approach |
| **Documentation completeness** | L2 | Custom CI check (file existence + section validation) | Verify model card, data sheet, test plan exist and contain required sections | Reviewing content quality and accuracy |
| **Guardrail configuration** | L3 | Infrastructure-as-code validation (OPA, custom) | Verify guardrails are configured per specification; validate against schema | Reviewing guardrail policy design decisions |
| **Dependency audit** | L4 | pip-audit, npm audit, Snyk, Dependabot | Scan for known vulnerabilities in AI dependencies | Evaluating vulnerability severity in AI context |
| **License compliance** | L3 | scancode-toolkit, FOSSA | Check model and data licenses for compliance | Evaluating novel license terms |
| **Approval signatures** | L1 | Jira workflow (digital approval) | Track who approved and when; enforce approval order | Actual human decision to approve/reject |

### 2.2 Bias Testing Checklist (`bias-testing-checklist.yaml`)

| Checklist Item Category | Automation Level | Tool / Method | What Gets Automated | What Remains Manual |
|------------------------|-----------------|---------------|---------------------|-------------------|
| **Demographic parity check** | L4 | Fairlearn MetricFrame, Aequitas | Calculate parity metrics across protected groups; flag violations | Defining protected groups and acceptable disparity thresholds |
| **Equal opportunity check** | L4 | Fairlearn, custom eval | Calculate TPR/FPR by group; compare against thresholds | Contextual interpretation (is disparity justified by legitimate factor?) |
| **Calibration analysis** | L3 | Custom calibration scripts, reliability diagrams | Generate calibration curves per group; flag miscalibration | Interpreting whether miscalibration is material |
| **Intersectional analysis** | L3 | Fairlearn (intersectional groups) | Run metrics for intersectional groups (e.g., age x gender) | Defining which intersections to test; interpreting sparse-data results |
| **Historical bias assessment** | L1 | Manual with tool support | N/A -- requires domain expertise | Assessing whether training data encodes historical discrimination |
| **Proxy variable detection** | L2 | Custom feature correlation analysis | Flag features highly correlated with protected attributes | Deciding whether correlated features are legitimate |

### 2.3 Monitoring Setup Checklist (`monitoring-setup-checklist.yaml`)

| Checklist Item Category | Automation Level | Tool / Method | What Gets Automated | What Remains Manual |
|------------------------|-----------------|---------------|---------------------|-------------------|
| **Metric instrumentation** | L3 | CI/CD check + integration test | Verify all required metrics are emitting data; test metric values are non-null | Defining metric thresholds; configuring alert routing |
| **Alert configuration** | L2 | Infrastructure-as-code validation | Validate alert rules exist for all required metrics; check threshold values | Tuning thresholds based on operational experience |
| **Dashboard existence** | L3 | API check against Grafana/Datadog | Verify dashboard exists and contains required panels | Reviewing dashboard layout and usability |
| **On-call rotation** | L2 | PagerDuty/OpsGenie API check | Verify on-call rotation has minimum 4 members; rotation is active | Selecting on-call team members |
| **Log retention** | L3 | Infrastructure audit script | Verify log retention policies match requirements (90d hot, 2y cold) | Defining retention requirements per regulation |
| **Drift detection** | L4 | Evidently, NannyML, custom drift pipeline | Run drift detection on production data; auto-alert on threshold breach | Investigating drift root cause; deciding on remediation |

### 2.4 Security Threat Model Checklist (`security-threat-model.yaml`)

| Checklist Item Category | Automation Level | Tool / Method | What Gets Automated | What Remains Manual |
|------------------------|-----------------|---------------|---------------------|-------------------|
| **Prompt injection testing** | L3 | Garak, custom adversarial prompts | Run prompt injection test suite against AI endpoints | Writing new attack prompts; assessing novel attack vectors |
| **Output sanitization** | L4 | CI/CD output validation pipeline | Verify all outputs pass through sanitization; test for PII leakage | Defining sanitization rules |
| **API authentication** | L4 | CI/CD security check (ZAP, Burp Suite) | Verify API endpoints require authentication; test for auth bypass | Designing authentication architecture |
| **Rate limiting** | L3 | Load testing tool (k6, Locust) | Verify rate limits are enforced at expected thresholds | Setting rate limit values |
| **Input validation** | L4 | Schema validation in CI/CD | Verify input schemas are enforced; test malformed inputs | Defining input schemas |
| **Agent permission verification** | L3 | Custom permission boundary test suite | Verify agent cannot invoke unauthorized tools; test escalation paths | Defining permission boundaries |

### 2.5 Incident Response Checklist (`incident-response-checklist.yaml`)

| Checklist Item Category | Automation Level | Tool / Method | What Gets Automated | What Remains Manual |
|------------------------|-----------------|---------------|---------------------|-------------------|
| **Incident detection** | L4 | Monitoring alerts (see [monitoring dashboard](../../04-operational-governance/templates/model-monitoring-dashboard.md)) | Auto-detect anomalies; auto-create Jira ticket | N/A -- detection is fully automated |
| **Severity classification** | L3 | Rule-based classification engine | Auto-classify based on impact metrics (users affected, financial impact) | Overriding classification for complex incidents |
| **Notification routing** | L4 | PagerDuty/OpsGenie rules | Auto-notify correct responders based on severity and system | N/A -- routing is fully automated |
| **DORA timeline tracking** | L3 | Jira automation (see [Jira workflows](./jira-governance-workflows.md)) | Calculate DORA reporting deadlines; send deadline reminders | Writing the actual incident report content |
| **Root cause analysis** | L0 | Manual | N/A -- requires human investigation | Full RCA process |
| **Corrective action tracking** | L2 | Jira workflow automation | Track corrective action tickets; auto-remind on deadlines | Defining and executing corrective actions |

---

## 3. Implementation Patterns

### 3.1 CI/CD Pipeline Integration

```
Git Push / PR Created
        |
        v
+------------------+     +------------------+     +------------------+
| Stage 1:         |     | Stage 2:         |     | Stage 3:         |
| Code Quality     |---->| Governance       |---->| Deployment       |
| (lint, test,     |     | Checks           |     | (if all pass)    |
|  security scan)  |     | (eval suite,     |     |                  |
|                  |     |  bias check,     |     |                  |
|                  |     |  security test,  |     |                  |
|                  |     |  doc validation) |     |                  |
+------------------+     +------------------+     +------------------+
                                |
                                v
                    +------------------+
                    | Evidence         |
                    | Collection       |
                    | (push to GRC,    |
                    |  update Jira)    |
                    +------------------+
```

### 3.2 Governance Gate Automation Pattern

```yaml
# Example: Automated deployment gate check in CI/CD pipeline
# This runs as part of the deployment pipeline and blocks deployment
# if governance checks fail.

governance_gate:
  stage: governance
  script:
    # 1. Performance evaluation
    - python run_eval_suite.py --model $MODEL_ID --threshold-file acceptance-criteria.yaml

    # 2. Bias evaluation
    - python run_bias_eval.py --model $MODEL_ID --groups age,gender,ethnicity

    # 3. Security scan
    - garak --model $MODEL_ID --probes prompt-injection,jailbreak,data-extraction

    # 4. Documentation check
    - python check_documentation.py --model-card model-card.md --data-sheet data-sheet.md

    # 5. Guardrail configuration validation
    - python validate_guardrails.py --config guardrails.yaml --schema guardrail-schema.yaml

    # 6. Push evidence to GRC
    - python push_evidence.py --results ./results/ --grc-api $GRC_API_URL

    # 7. Update Jira governance gate ticket
    - python update_jira_gate.py --ticket $GATE_TICKET --status "Evidence Collected"

  allow_failure: false  # Block deployment on failure
  artifacts:
    paths:
      - results/
    expire_in: 2 years  # Regulatory retention requirement
```

### 3.3 Continuous Monitoring Automation Pattern

```
Scheduled Job (hourly/daily)
        |
        v
+------------------+     +------------------+     +------------------+
| Collect          |     | Compute          |     | Evaluate         |
| Production Data  |---->| Drift Metrics    |---->| Against          |
| (sample or full) |     | (PSI, KS, etc.)  |     | Thresholds       |
+------------------+     +------------------+     +------------------+
                                                          |
                                    +---------------------+---------------------+
                                    |                                           |
                                    v                                           v
                          +------------------+                        +------------------+
                          | Pass:            |                        | Fail:            |
                          | Update dashboard |                        | Create alert     |
                          | Push to GRC KRI  |                        | Create Jira      |
                          +------------------+                        | Notify on-call   |
                                                                      +------------------+
```

---

## 4. False Positive Management

### 4.1 The False Positive Problem

Automated governance checks will produce false positives -- flags that look like governance violations but are not. False positives erode trust in the automation system: if engineers learn that most automated governance failures are false positives, they will stop taking real failures seriously.

### 4.2 False Positive Mitigation Strategies

| Strategy | Description | When to Use |
|----------|-------------|-------------|
| **Threshold tuning** | Adjust detection thresholds to reduce false positives while maintaining true positive detection | After initial deployment; tune based on first 30 days of data |
| **Allowlisting** | Explicitly mark known acceptable patterns that trigger false positives | When a specific pattern is verified as acceptable and recurring |
| **Multi-signal confirmation** | Require multiple independent signals before raising an alert (e.g., both PSI and performance degradation) | For drift detection and anomaly alerts |
| **Confidence scoring** | Assign confidence to automated findings; only alert above a confidence threshold | For ML-based detection (bias, toxicity, hallucination) |
| **Human review queue** | Route low-confidence findings to a human review queue instead of blocking | For semi-automated checks (L2-L3) |
| **Feedback loop** | Engineers can mark findings as false positive; feed back into detection model | Ongoing improvement of automated checks |

### 4.3 False Positive Tracking

| Metric | Target | Measurement |
|--------|--------|-------------|
| **False positive rate per check** | < 10% of total findings | Monthly review of automated findings vs. confirmed issues |
| **Time to resolve false positive** | < 1 business day | Track from finding creation to false positive classification |
| **Repeat false positives** | < 5% of false positives recur after allowlisting | Monthly review of allowlisted patterns |
| **Engineer trust score** | > 80% of engineers trust automated findings | Quarterly survey |

---

## 5. Human Review Requirements

Some governance activities cannot and should not be fully automated, regardless of technical capability. These require human judgment, ethical reasoning, or regulatory interpretation that machines cannot reliably provide.

### 5.1 Mandatory Human Review Items

| Activity | Why Human Review Is Required | Minimum Reviewer Qualification |
|----------|----------------------------|-------------------------------|
| **Ethics impact assessment** | Requires contextual ethical judgment about societal impact | Ethics Lead or trained ethics reviewer |
| **Risk classification (EU AI Act)** | Legal interpretation of Annex III applicability | Compliance Officer with AI Act training |
| **Risk acceptance decisions** | Business judgment about residual risk tolerance | Model Owner + Compliance Officer; CAIO for Critical |
| **Bias remediation trade-offs** | Value judgment about fairness vs. performance trade-offs | Ethics Lead + Model Owner |
| **Incident root cause analysis** | Complex causal reasoning across systems | Model Owner + engineering team |
| **Regulatory notification decision** | Legal judgment about whether a threshold is crossed | Compliance Officer + Legal Counsel |
| **Model retirement decision** | Business impact assessment of removing a production system | Model Owner + Product Owner + CAIO |
| **Third-party risk assessment** | Strategic evaluation of vendor dependency and alternatives | CISO + CAIO |
| **Board governance reporting** | Strategic interpretation and narrative for board consumption | CAIO |

### 5.2 Human-in-the-Loop Pattern for Automated Checks

For items at automation level L3 or L4, implement a human override mechanism:

1. Automated check runs and produces a result (pass/fail/flag)
2. If **pass**: result auto-feeds into governance workflow; no human intervention needed
3. If **fail**: determine if the failure is blocking or advisory
   - **Blocking failure (L4):** Deployment halted; human must review and either fix or approve override
   - **Advisory failure (L3):** Finding documented; human reviews in next governance cycle
4. **Override path:** Authorized personnel (Model Owner + Compliance Officer) can override a blocking failure with documented justification
5. **Override audit trail:** All overrides are logged with justification, approver, timestamp, and expiration date

---

## 6. Cost-Benefit Analysis

### 6.1 Cost of Manual Governance

| Activity | Manual Effort (per AI system, per cycle) | Annual Cost (10 AI systems) |
|----------|----------------------------------------|---------------------------|
| Pre-deployment gate review | 3-5 days of preparation + 1 day review meeting | 40-60 person-days |
| Bias assessment | 2-3 days per assessment, quarterly | 80-120 person-days |
| Security assessment | 2-3 days per assessment, quarterly | 80-120 person-days |
| Monitoring verification | 1 day per system, monthly | 120 person-days |
| Drift investigation | 0.5-2 days per event (estimated 2 events/system/quarter) | 40-160 person-days |
| Compliance evidence assembly | 3-5 days per regulatory request | 30-50 person-days |
| **Total** | | **390-630 person-days/year** |

### 6.2 Cost of Automation

| Investment | One-Time Cost | Annual Maintenance |
|-----------|--------------|-------------------|
| CI/CD governance pipeline setup | 20-30 person-days | 10-15 person-days |
| Bias evaluation automation | 10-15 person-days | 5-10 person-days |
| Security testing automation | 15-20 person-days | 10-15 person-days |
| Monitoring automation | 10-15 person-days | 5-10 person-days |
| GRC integration | 15-25 person-days | 10-15 person-days |
| Tooling licenses | Variable (many open-source options) | Variable |
| **Total** | **70-105 person-days** | **40-65 person-days/year** |

### 6.3 ROI Calculation

| Metric | Manual | Automated (after Year 1) | Savings |
|--------|--------|-------------------------|---------|
| Annual person-days | 390-630 | 120-200 (residual manual + maintenance) | 60-70% reduction |
| Time to gate approval | 5-10 business days | 1-2 business days (blocking checks run in CI/CD) | 70-80% faster |
| Coverage consistency | Variable (depends on who reviews) | 100% consistent (same checks every time) | Elimination of human error |
| Evidence completeness | 60-80% (items missed, evidence not linked) | 95%+ (automated evidence collection) | Audit-ready always |
| Drift detection latency | Days to weeks (discovered in periodic review) | Minutes to hours (continuous monitoring) | 100x faster detection |

### 6.4 Automation Priority Ranking

Based on effort-to-impact ratio, automate in this order:

| Priority | Checklist / Activity | Justification |
|----------|---------------------|---------------|
| 1 | Monitoring and alerting (`monitoring-setup-checklist.yaml`) | Highest regulatory risk if manual; continuous monitoring is foundational |
| 2 | Drift detection (`drift-detection-evals.md`) | Silent degradation is the most common AI failure mode in production |
| 3 | Pre-deployment performance eval | Blocks the highest-frequency governance event (every deployment) |
| 4 | Security scanning (prompt injection, output validation) | Security vulnerabilities have highest blast radius |
| 5 | Bias evaluation | Regulatory requirement with clear automation path |
| 6 | Documentation completeness checks | Low effort, high consistency gain |
| 7 | GRC evidence collection | Reduces audit preparation from days to minutes |
| 8 | Incident detection and routing | Reduces MTTR and DORA compliance risk |

---

## 7. Tool Recommendations

| Category | Recommended Tools | License | Integration Method |
|----------|------------------|---------|-------------------|
| **Model evaluation** | Giskard, Evidently, custom eval suite | Open-source / commercial | CI/CD plugin / Python script |
| **Bias evaluation** | Fairlearn, Aequitas, AI Fairness 360 | Open-source | CI/CD Python script |
| **Drift detection** | Evidently, NannyML, WhyLabs | Open-source / commercial | Scheduled job / monitoring pipeline |
| **Security testing** | Garak, custom prompt injection suite | Open-source | CI/CD pipeline stage |
| **Dependency scanning** | pip-audit, Snyk, Dependabot | Open-source / commercial | CI/CD pipeline stage |
| **Data validation** | Great Expectations, Pandera, dbt tests | Open-source | Data pipeline integration |
| **Infrastructure validation** | OPA (Open Policy Agent), custom validators | Open-source | CI/CD policy check |
| **Monitoring** | Prometheus + Grafana, Datadog, New Relic | Open-source / commercial | Infrastructure deployment |
| **Alerting** | PagerDuty, OpsGenie, Alertmanager | Commercial / open-source | Monitoring integration |
| **Evidence management** | GRC platform API (see [GRC integration](./grc-platform-integration.md)) | Commercial | API integration |

See the [tool landscape](../../05-cross-cutting/tool-landscape.md) for the full tooling ecosystem used across the governance framework.

---

## Cross-References

- [Governance in CI/CD](../../07-enterprise-implementation/process-integration/governance-in-cicd.md) -- pipeline integration architecture for automated governance checks
- [Jira Governance Workflows](./jira-governance-workflows.md) -- Jira automation rules that consume automated check results
- [GRC Platform Integration](./grc-platform-integration.md) -- how automated evidence flows into enterprise GRC platforms
- [Model Monitoring Dashboard](../../04-operational-governance/templates/model-monitoring-dashboard.md) -- operational monitoring that runs continuous automated checks
- [Drift Detection Evaluations](../../04-operational-governance/evaluations/drift-detection-evals.md) -- statistical methodology for automated drift detection
- [Drift Detection Runbook](../../04-operational-governance/templates/drift-detection-runbook.md) -- human procedures triggered by automated drift alerts
- [Pre-Deployment Gate Checklist](../../02-development-governance/checklists/pre-deployment-gate.yaml) -- primary checklist for automated gate checks
- [Bias and Fairness Evals](../../02-development-governance/evaluations/bias-and-fairness-evals.md) -- evaluation methodology for automated bias checks
- [Red Teaming AI Systems](../../04-operational-governance/guides/red-teaming-ai-systems.md) -- adversarial testing methodology automated in security checks
- [Tool Landscape](../../05-cross-cutting/tool-landscape.md) -- comprehensive tooling overview for the governance framework
- [Eval-Driven Development](../../02-development-governance/evaluations/eval-driven-development.md) -- evaluation framework that underpins automated quality checks

---

*Last updated: 2026-03-01* / *Version: 1.0* / *Classification: Internal / Regulatory Preparation*
