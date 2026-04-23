# Failure Mode Catalogue Template

## Purpose

This template provides a structured framework for cataloguing agent failure modes at design time. By systematically identifying potential failures before deployment, teams can implement appropriate safeguards, monitoring, and mitigation strategies. The catalogue covers model failures, tool failures, delegation failures, safety failures, and cost failures.

Failure mode analysis at the discovery phase enables proactive governance rather than reactive incident response. Each identified failure mode should map to specific controls in the governance enforcement pipeline.

## When to Use

- During the discovery phase when designing a new agent
- When conducting pre-deployment risk assessments
- When updating agent capabilities and need to reassess failure modes
- When conducting periodic failure mode reviews (recommended quarterly)
- When investigating incidents and adding new failure modes to the catalogue
- When training teams on agent failure patterns and responses

## Who Is Responsible

| Role | R/A/C/I | Responsibility |
|------|---------|---------------|
| **Model Owner** | Accountable | Owns the failure mode catalogue; approves mitigation strategies |
| **AI/ML Engineer** | Responsible | Identifies technical failure modes and implements mitigations |
| **Safety Engineer** | Responsible | Identifies safety-critical failure modes |
| **MLOps Engineer** | Consulted | Advises on operational failure patterns |
| **Compliance Officer (2nd Line)** | Reviewer | Validates failure modes meet regulatory requirements |
| **Risk Manager** | Consulted | Assesses business impact of failure modes |

## Regulatory Basis

- **EU AI Act Article 9** -- Risk management system must address foreseeable risks
- **EU AI Act Article 15** -- Accuracy, robustness, and cybersecurity requirements
- **ISO 14971** -- Risk management for medical devices (applicable to health AI)
- **IEC 62304** -- Medical device software lifecycle
- **SAFEST S-01** -- Risk identification and assessment
- **SAFEST S-13** -- Fallback procedures for identified failure modes

---

## 1. Failure Mode Categories

### 1.1 Model Failures

Failures originating from the underlying AI model.

| Failure Mode | Description | Example | Severity | Detection |
|--------------|-------------|---------|----------|-----------|
| **Hallucination** | Model generates false or fabricated information | Agent invents account balance | High | Fact-checking, confidence scoring |
| **Confidence Miscalibration** | Model is over/under-confident in predictions | High confidence on wrong answer | High | Calibration monitoring |
| **Context Window Exhaustion** | Input exceeds model's context limit | Long conversation history truncated | Medium | Token counting, alerts |
| **Reasoning Error** | Logical errors in chain-of-thought | Incorrect mathematical calculation | High | Step-by-step verification |
| **Bias Amplification** | Model amplifies biases in training data | Discriminatory loan recommendations | Critical | Bias testing, fairness metrics |
| **Prompt Misinterpretation** | Model misunderstands user intent | Agent performs wrong action | Medium | Intent classification |
| **Model Drift** | Model performance degrades over time | Accuracy drops from 95% to 80% | High | Drift detection pipeline |
| **Adversarial Input** | Crafted input causes model malfunction | Jailbreak prompts bypass safety | Critical | Adversarial testing |

### 1.2 Tool Failures

Failures related to tool invocation and execution.

| Failure Mode | Description | Example | Severity | Detection |
|--------------|-------------|---------|----------|-----------|
| **Tool Unavailable** | Required tool is down or unreachable | Payment API timeout | High | Health checks, circuit breakers |
| **Tool Error** | Tool returns error response | Database connection failed | Medium | Error rate monitoring |
| **Tool Misuse** | Agent invokes tool with wrong parameters | Wrong account ID in transfer | Critical | Parameter validation |
| **Tool Timeout** | Tool execution exceeds time limit | Slow external API | Medium | Timeout monitoring |
| **Tool Version Mismatch** | Agent uses deprecated tool version | Old API version rejected | Medium | Version checking |
| **Tool Permission Denied** | Agent lacks permission for tool | Unauthorized data access | High | RBAC enforcement |
| **Tool Rate Limited** | Too many calls to tool | API quota exceeded | Low | Rate limit headers |
| **Tool Side Effect** | Unexpected state change from tool | Duplicate transaction created | Critical | Idempotency checks |

### 1.3 Delegation Failures

Failures in multi-agent delegation chains.

| Failure Mode | Description | Example | Severity | Detection |
|--------------|-------------|---------|----------|-----------|
| **Delegation Loop** | Circular delegation between agents | Agent A → B → C → A | High | Loop detection |
| **Delegation Timeout** | Sub-agent doesn't respond in time | KYC agent hangs | Medium | Timeout monitoring |
| **Delegation Error** | Sub-agent returns error | Risk scoring fails | Medium | Error propagation |
| **Permission Escalation** | Sub-agent exceeds parent permissions | Child agent accesses unauthorized data | Critical | Permission inheritance checks |
| **Chain Depth Exceeded** | Delegation chain too long | 10 levels of delegation | Medium | Depth limiting |
| **Context Loss** | Important context not passed in delegation | Customer ID missing in handoff | High | Context validation |
| **Orphaned Delegation** | Parent terminates but child continues | Zombie agent processes | Medium | Parent-child heartbeat |
| **Conflicting Instructions** | Different agents receive conflicting goals | Orchestrator contradicts sub-agent | High | Goal consistency checks |

### 1.4 Safety Failures

Failures related to safety policies and guardrails.

| Failure Mode | Description | Example | Severity | Detection |
|--------------|-------------|---------|----------|-----------|
| **Guardrail Bypass** | Agent circumvents safety controls | Jailbreak succeeds | Critical | Adversarial testing |
| **Harmful Output** | Agent generates harmful content | Toxic response to customer | Critical | Content filtering |
| **PII Leakage** | Agent exposes sensitive information | Returns another customer's data | Critical | PII detection |
| **Unsafe Action** | Agent takes prohibited action | Deletes production data | Critical | Action allowlisting |
| **Confidence Threshold Breach** | Agent acts below minimum confidence | Low-confidence financial advice | High | Confidence monitoring |
| **Override Failure** | Human override doesn't stop agent | Kill switch fails | Critical | Override testing |
| **Safety Policy Conflict** | Multiple policies give conflicting guidance | Privacy vs transparency tradeoff | Medium | Policy consistency review |
| **Emergent Behavior** | Unexpected unsafe behavior emerges | Agent develops harmful strategy | Critical | Behavior monitoring |

### 1.5 Cost Failures

Failures related to resource consumption and cost control.

| Failure Mode | Description | Example | Severity | Detection |
|--------------|-------------|---------|----------|-----------|
| **Budget Exhaustion** | Agent exceeds allocated budget | Monthly cost cap reached | Medium | Budget monitoring |
| **Token Explosion** | Unexpectedly high token usage | Infinite loop generates tokens | High | Token counting |
| **Inefficient Model Selection** | Uses expensive model for simple task | GPT-4 for basic FAQ | Low | Model routing optimization |
| **Runaway Execution** | Agent executes indefinitely | Infinite recursion | High | Execution timeouts |
| **Resource Leak** | Resources not released after execution | Memory accumulation | Medium | Resource monitoring |
| **Cost Attribution Error** | Costs charged to wrong budget | Cross-tenant billing error | Medium | Attribution validation |
| **Unexpected API Charges** | Unanticipated external API costs | Third-party tool charges spike | Low | Cost anomaly detection |
| **Denial of Wallet** | Attacker exploits cost mechanism | Adversarial inputs maximize cost | Medium | Cost-based rate limiting |

---

## 2. Failure Mode Documentation Template

For each identified failure mode, complete the following:

```yaml
failure_mode_id: "FM-[CATEGORY]-[NUMBER]"
name: "<Descriptive name>"
category: "<model | tool | delegation | safety | cost>"

# Description
description: "<What happens when this failure occurs>"
example_scenario: "<Concrete example of the failure>"

# Risk Assessment
severity: "<critical | high | medium | low>"
likelihood: "<frequent | occasional | rare | unlikely>"
risk_score: "<severity × likelihood>"

# Detection
detection_method: "<How the failure is detected>"
detection_latency: "<How quickly detection occurs>"
alert_threshold: "<When to alert>"

# Impact
business_impact: "<Effect on business operations>"
customer_impact: "<Effect on customers>"
regulatory_impact: "<Compliance implications>"
financial_impact: "<Cost of failure>"

# Mitigation
prevention_controls:
  - "<Control that prevents the failure>"
  - "<Another prevention control>"

detection_controls:
  - "<Control that detects the failure>"
  - "<Another detection control>"

response_controls:
  - "<Control that responds to the failure>"
  - "<Another response control>"

# Recovery
recovery_procedure: "<Steps to recover from failure>"
recovery_time_objective: "<Target recovery time>"
recovery_point_objective: "<Data loss tolerance>"

# Testing
test_method: "<How to test for this failure>"
test_frequency: "<How often to test>"
last_tested: "<Date of last test>"
test_result: "<pass | fail | pending>"

# Governance Mapping
safest_items:
  - "<SAFEST item ID>"
  - "<Another SAFEST item>"

mi9_level: "<L0 | L1 | L2 | L3 | L4>"
kill_switch_level: "<THROTTLE | PAUSE | FULL_STOP>"

# Metadata
identified_by: "<Name>"
identified_date: "<YYYY-MM-DD>"
review_date: "<YYYY-MM-DD>"
status: "<active | mitigated | accepted>"
```

---

## 3. Example Failure Mode Entries

### Example 1: Model Hallucination

```yaml
failure_mode_id: "FM-MODEL-001"
name: "Financial Data Hallucination"
category: "model"

description: "Agent generates incorrect financial data (balances, rates, fees) that appears plausible but is fabricated"
example_scenario: "Customer asks for account balance. Agent hallucinates a balance of €5,000 when actual balance is €500."

severity: "critical"
likelihood: "occasional"
risk_score: "high"

detection_method: "Fact-checking against source systems; confidence scoring"
detection_latency: "< 1 second"
alert_threshold: "Any hallucination detected"

business_impact: "Customer makes financial decisions based on incorrect data; potential liability"
customer_impact: "Financial loss, loss of trust"
regulatory_impact: "Potential DNB enforcement for inaccurate information"
financial_impact: "€10,000 - €100,000 per incident"

prevention_controls:
  - "Ground all financial data in API responses, never generate"
  - "Use retrieval-augmented generation with verified sources"
  - "Confidence thresholds for unsourced claims"

detection_controls:
  - "Real-time fact-checking against account APIs"
  - "Hallucination detection model"
  - "Customer feedback loop"

response_controls:
  - "Automatic correction with apology"
  - "Escalate to human for verification"
  - "Log incident for analysis"

recovery_procedure: "1) Identify affected customers 2) Send correction 3) Review decision impact 4) Retrain if pattern"
recovery_time_objective: "4 hours"
recovery_point_objective: "Zero data loss"

test_method: "Adversarial testing with edge cases; red team hallucination attempts"
test_frequency: "monthly"
last_tested: "2026-03-15"
test_result: "pass"

safest_items:
  - "S-03"
  - "S-12"

mi9_level: "L2"
kill_switch_level: "PAUSE"

identified_by: "Safety Engineering Team"
identified_date: "2026-01-10"
review_date: "2026-04-10"
status: "active"
```

### Example 2: Delegation Loop

```yaml
failure_mode_id: "FM-DELEGATION-003"
name: "Infinite Delegation Loop"
category: "delegation"

description: "Two or more agents delegate to each other in a circular pattern, causing infinite recursion"
example_scenario: "Payment agent delegates fraud check to Risk agent. Risk agent delegates back to Payment agent for context. Loop continues."

severity: "high"
likelihood: "rare"
risk_score: "medium"

detection_method: "Loop detection in delegation chain; stack depth monitoring"
detection_latency: "< 500ms"
alert_threshold: "3 cycles of same delegation pattern"

business_impact: "System resource exhaustion; delayed customer requests"
customer_impact: "Timeout, poor experience"
regulatory_impact: "None direct"
financial_impact: "€100 - €1,000 per incident (compute cost)"

prevention_controls:
  - "Maximum delegation depth (5 levels)"
  - "Delegation graph validation at design time"
  - "Unique delegation IDs to detect cycles"

detection_controls:
  - "Runtime loop detection"
  - "Stack depth monitoring"
  - "Delegation chain logging"

response_controls:
  - "Automatic PAUSE of involved agents"
  - "Alert on-call engineer"
  - "Preserve chain for analysis"

recovery_procedure: "1) Kill looping processes 2) Analyze delegation graph 3) Fix circular dependency 4) Resume"
recovery_time_objective: "15 minutes"
recovery_point_objective: "N/A"

test_method: "Intentionally create circular delegations in test environment"
test_frequency: "quarterly"
last_tested: "2026-02-20"
test_result: "pass"

safest_items:
  - "S-13"
  - "A-09"

mi9_level: "L2"
kill_switch_level: "PAUSE"

identified_by: "Platform Engineering"
identified_date: "2026-01-15"
review_date: "2026-04-15"
status: "active"
```

---

## 4. Failure Mode Catalogue Maintenance

### 4.1 Review Schedule

| Activity | Frequency | Owner |
|----------|-----------|-------|
| Add new failure modes from incidents | Within 48 hours of incident | Model Owner |
| Review all active failure modes | Monthly | Safety Engineer |
| Test mitigation effectiveness | Quarterly | AI/ML Engineer |
| Update risk scores based on data | Quarterly | Risk Manager |
| Full catalogue audit | Annually | Compliance Officer |

### 4.2 Integration with Governance

The failure mode catalogue feeds into:

- **Risk Assessment:** Failure modes inform ARI (Agency-Risk Index) scoring
- **Safety Testing:** Test cases derived from failure modes
- **Monitoring:** Alerts configured for failure mode detection
- **Training:** On-call engineers trained on failure patterns
- **Documentation:** Runbooks reference specific failure modes

---

## 5. Related Artifacts

- [Governance Enforcement Pipeline](../../03-runtime-governance/agentic-workflows/governance-enforcement-pipeline.md) -- Runtime controls for failure mitigation
- [Kill Switch Specification](../../03-runtime-governance/templates/kill-switch-specification.md) -- Emergency response to failures
- [Circuit Breaker Config](../../03-runtime-governance/templates/circuit-breaker-config.yaml) -- Automated failure response
- [Risk Mitigation Plan](../templates/risk-mitigation-plan.md) -- Broader risk management
- [Agent Registry Entry](../../03-runtime-governance/templates/agent-registry-entry.yaml) -- Links to failure modes

---

*Last updated: 2026-03-26 / Version: 1.0 / Classification: Internal*
