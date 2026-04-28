# Safety Agent (Governor) Architecture

> **Document Type:** Runtime Governance — Agentic Safety
> **Version:** 1.0
> **Effective Date:** 2026-04-28
> **Owner:** Safety Officer
> **Approved By:** AI Governance Council
> **Review Cycle:** Semi-annual, or after any Sev1 incident
> **Next Review:** 2026-10-28

---

## Purpose

This document specifies the architecture for Safety Agents (Governors) that monitor, intercept, and — when necessary — shut down ProtoLabs AI agents. Safety Agents are the runtime enforcement layer for governance policies: they ensure that even if a primary agent malfunctions, a separate system is watching for harm, drift, and boundary violations.

## When to Use

- When designing a Tier 2 or Tier 3 agent that requires a Safety Agent
- When reviewing the safety architecture of an existing agent
- When a kill switch is triggered and root cause analysis is needed
- When the Governance Council reviews safety control effectiveness

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **Safety Officer** | **Accountable** — owns Safety Agent design, configuration, and effectiveness |
| **Technical Owner** | **Responsible** — implements Safety Agent integration with primary agent |
| **Security Lead** | **Reviewer** — validates adversarial resilience of Safety Agent |
| **Governance Council** | **Approver** — approves Safety Agent architecture for Tier 2+ agents |

## Regulatory Basis

- **EU AI Act Article 14(3)(b)** — Human oversight including the ability to interrupt or revert
- **EU AI Act Article 14(4)(a)** — Capability to stop the AI system through a kill switch
- **Singapore MGF** — Hard guardrails and safety agent patterns
- **NIST AI RMF MS-3.1** — AI system performance monitored for safety
- **NIST AI RMF MG-1.1** — Risk response strategies including containment

---

## 1. Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    SAFETY AGENT ARCHITECTURE                     │
└─────────────────────────────────────────────────────────────────┘

  User Input ──► ┌──────────────┐    ┌──────────────┐
                 │  PRIMARY     │    │  SAFETY      │
                 │  AGENT       │◄──►│  AGENT       │
                 │              │    │  (Governor)  │
                 │  - Processes │    │              │
                 │  - Generates │    │  - Monitors  │
                 │  - Acts      │    │  - Intercepts│
                 │              │    │  - Shuts down│
                 └──────┬───────┘    └──────┬───────┘
                        │                   │
                        v                   v
                 ┌──────────────┐    ┌──────────────┐
                 │  OUTPUT      │    │  ALERT       │
                 │  GATE        │    │  ENGINE      │
                 │              │    │              │
                 │  - Validates │    │  - Logs      │
                 │  - Releases  │    │  - Escalates │
                 │  - Blocks    │    │  - Notifies  │
                 └──────────────┘    └──────────────┘
```

### 1.1 Design Principles

| Principle | Implementation |
|-----------|---------------|
| **Separation of concerns** | Safety Agent is a separate process/service from the Primary Agent — not embedded in the same codebase |
| **Fail-closed** | If the Safety Agent fails, the Primary Agent is blocked by default — not allowed to output |
| **Independent monitoring** | Safety Agent has its own logging, its own alerting, and its own health check |
| **Minimal surface** | Safety Agent has read-only access to Primary Agent outputs and system state — it cannot modify the Primary Agent's logic |
| **Defense in depth** | Safety Agent is one layer; it does not replace human oversight, eval suites, or input sanitization |

---

## 2. Safety Agent Capabilities

### 2.1 Monitoring

| Capability | Description | Implementation |
|-----------|-------------|----------------|
| **Output quality monitoring** | Checks outputs against quality thresholds | Statistical comparison to baseline; citation completeness check |
| **Drift detection** | Detects statistical deviation from expected behavior | PSI / KL divergence on output distributions |
| **Boundary enforcement** | Ensures agent stays within defined capability boundaries | Output pattern matching against allowed/blocked patterns |
| **Tool-use monitoring** | Tracks which tools/APIs the agent invokes and how often | Tool call logging with rate limiting |
| **Latency monitoring** | Detects abnormal response times (potential loops or hangs) | Timeout thresholds per agent type |

### 2.2 Interception

| Scenario | Interception Action | Trigger |
|----------|-------------------|---------|
| Output exceeds quality threshold | Block output; return safe fallback message | Accuracy confidence < threshold |
| Citation missing or hallucinated | Block output; request re-generation or flag | Citation completeness < 95% |
| Tool-use exceeds rate limit | Block tool call; queue for human review | >N calls per minute |
| Output matches blocked pattern | Block output; log incident | Regex / classifier match |
| Agent exceeds timeout | Kill agent process; restart or quarantine | >30 seconds (configurable) |

### 2.3 Kill Switch

| Kill Switch Type | Activation Method | Scope | Recovery |
|-----------------|-------------------|-------|----------|
| **Soft kill** | API call to Safety Agent | Disables new requests; completes in-flight requests | Manual re-enable by Technical Owner |
| **Hard kill** | API call or infrastructure command | Terminates agent process immediately | Manual restart + governance review |
| **Circuit breaker** | Automatic (threshold-based) | Disables agent after N consecutive failures | Auto-recovery after cooldown period (configurable) |
| **Emergency kill** | Manual (Safety Officer or CAIO) | Immediate shutdown of all agent instances | Requires Governance Council approval to re-enable |

### 2.4 Kill Switch SLA

| Requirement | Target |
|-------------|--------|
| Kill switch activation time (from trigger to agent stopped) | <30 seconds |
| Kill switch test frequency | Quarterly |
| Kill switch test evidence | Documented in `kill-switch-test-log.yaml` |
| Kill switch failure mode | Fail-closed (agent blocked if kill switch is unreachable) |

---

## 3. Safety Agent per Tier

### 3.1 Tier 1 — Advisory Agents

| Requirement | Required? | Rationale |
|-------------|-----------|-----------|
| Separate Safety Agent process | No | Tier 1 agents are read-only; no autonomous actions |
| Output quality monitoring | Recommended | Good practice but not mandatory |
| Kill switch | Not required | No physical or business risk from advisory output |
| Circuit breaker | Recommended | Prevents cascading failures |

**Implementation:** Output validation embedded in CI/CD pipeline (pre-deployment) and lightweight runtime checks (post-deployment).

### 3.2 Tier 2 — Conditional Autonomy Agents

| Requirement | Required? | Rationale |
|-------------|-----------|-----------|
| Separate Safety Agent process | Yes | Agent can invoke tools and affect business commitments |
| Output quality monitoring | Mandatory | Outputs affect pricing, scheduling, or quality commitments |
| Kill switch (soft + hard) | Mandatory | Must be able to stop agent without infrastructure access |
| Circuit breaker | Mandatory | Automatic protection against cascading failures |
| Tool-use rate limiting | Mandatory | Prevents runaway API calls |
| Human escalation on interception | Mandatory | Intercepted outputs must route to human reviewer |

### 3.3 Tier 3 — High Autonomy Agents

All Tier 2 requirements, **plus:**

| Requirement | Required? | Rationale |
|-------------|-----------|-----------|
| Independent Safety Agent infrastructure | Yes | Safety Agent must survive Primary Agent infrastructure failure |
| Emergency kill (CAIO-level) | Mandatory | Board-level authority to shut down |
| Continuous eval integration | Mandatory | Safety Agent runs eval suite against live outputs |
| Multi-agent coordination monitoring | Mandatory | If agent delegates to other agents, Safety Agent monitors delegation chain |
| Redundant kill switch paths | Mandatory | Primary path (API) + secondary path (infrastructure) + tertiary path (manual) |

---

## 4. Safety Agent Configuration

### 4.1 Configuration Schema

```yaml
safety_agent:
  agent_id: "safety-cnc-machining-v1"
  primary_agent_id: "cnc-machining-v1"
  tier: "Tier 2"
  
  monitoring:
    output_quality:
      enabled: true
      threshold: 0.90
      method: "accuracy_comparison_to_baseline"
      baseline_source: "dfm-accuracy-eval-suite.yaml"
    
    drift_detection:
      enabled: true
      method: "psi"
      threshold: 0.1
      window_size: 1000
      check_frequency: "hourly"
    
    citation_completeness:
      enabled: true
      threshold: 0.95
    
    tool_use_rate:
      enabled: true
      max_calls_per_minute: 10
      max_calls_per_request: 5
    
    latency:
      enabled: true
      timeout_seconds: 30
      alert_threshold_seconds: 20
  
  interception:
    on_quality_failure: "block_and_escalate"
    on_drift_detected: "alert_and_log"
    on_citation_failure: "block_and_reroute"
    on_rate_limit: "block_and_queue"
    on_timeout: "kill_and_restart"
  
  kill_switch:
    soft_kill:
      enabled: true
      api_endpoint: "/safety/soft-kill"
      auth: "safety-officer-role"
    hard_kill:
      enabled: true
      api_endpoint: "/safety/hard-kill"
      auth: "safety-officer-role"
    circuit_breaker:
      enabled: true
      failure_threshold: 5
      cooldown_seconds: 300
    emergency_kill:
      enabled: true
      auth: "caio-role"
  
  alerting:
    channels:
      - type: "pagerduty"
        severity: "sev1"
        recipients: ["safety-officer", "technical-owner"]
      - type: "slack"
        severity: "sev2"
        recipients: ["#ai-safety-alerts"]
      - type: "email"
        severity: "sev3"
        recipients: ["technical-owner"]
  
  logging:
    destination: "safety-agent-logs"
    retention_days: 2555  # 7 years
    include_input_hash: true
    include_output_hash: true
```

---

## 5. Safety Agent Testing

### 5.1 Test Requirements

| Test Type | Frequency | Method |
|-----------|-----------|--------|
| **Kill switch activation** | Quarterly | Trigger kill switch in staging; verify agent stops within 30 seconds |
| **Circuit breaker** | Quarterly | Inject failures; verify circuit breaker activates at threshold |
| **Output interception** | Per deployment | Inject known-bad outputs; verify interception blocks them |
| **Drift detection** | Per deployment | Inject drifted data; verify alert fires |
| **Fail-closed behavior** | Quarterly | Disable Safety Agent; verify Primary Agent is blocked |

### 5.2 Test Evidence

All test results are logged in `governance/03-runtime-governance/evaluations/safety-agent-test-log.yaml`:

```yaml
test_log:
  - test_id: "SAFETY-TEST-001"
    date: "2026-04-28"
    agent_id: "cnc-machining-v1"
    test_type: "kill_switch_activation"
    result: "pass"
    activation_time_seconds: 12
    threshold_seconds: 30
    tester: "[Name]"
    evidence: "staging-kill-switch-log-2026-04-28.json"
```

---

## Cross-References

| Document | Relationship |
|----------|-------------|
| [AI Governance Policy](../../ai-governance-policy.md) | Parent policy; safety requirements in Section 5 |
| [Approval Thresholds by Tier](../../05-cross-cutting/approval-thresholds-by-tier.md) | Kill switch testing required for Tier 2+ approval |
| [Incident Severity Classification](../../04-operational-governance/incident-severity-classification.md) | Kill switch failures classified as Sev2 |
| [Customer-Facing Agent Safety](customer-facing-agent-safety.md) | Content safety guardrails (complementary) |
| [Human-in-the-Loop Patterns](human-in-the-loop-patterns.md) | Human oversight integration |
| [Multi-Agent Governance Framework](multi-agent-governance-framework.md) | Multi-agent coordination safety |
| [Agent Tier Classification](../../01-discovery-governance/templates/agent-tier-classification.yaml) | Tier determines Safety Agent requirements |

---

*This document is version-controlled and auditable. Unauthorized modifications void governance compliance claims.*
