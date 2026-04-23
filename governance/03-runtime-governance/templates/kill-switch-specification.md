# Kill Switch Specification Template

## Purpose

This template defines the KILLSWITCH.md standard for per-agent and per-skill emergency stop procedures. Kill switches provide immediate, unambiguous mechanisms to halt agent execution when safety thresholds are breached, anomalies are detected, or human operators determine intervention is necessary. This specification maps the 3-level escalation model (Throttle/Pause/Full Stop) to the existing MI9 containment levels.

Kill switches are the last line of defense in agent governance. When automated safeguards fail or unexpected behavior emerges, kill switches ensure humans can immediately stop agent activity.

## When to Use

- When deploying any agent to production (kill switch is a pre-deployment requirement)
- When defining emergency response procedures for agent incidents
- When conducting kill switch testing (required quarterly for high-risk agents)
- When integrating with monitoring and alerting systems
- When training on-call engineers in agent emergency procedures
- When updating procedures after safety incidents

## Who Is Responsible

| Role | R/A/C/I | Responsibility |
|------|---------|---------------|
| **Model Owner** | Accountable | Owns the kill switch specification; approves trigger conditions |
| **MLOps / Platform Engineer** | Responsible | Implements kill switch mechanisms and monitoring integration |
| **Security Engineer** | Responsible | Ensures kill switches cannot be bypassed or disabled by agents |
| **On-Call Engineer** | Responsible | Executes kill switch procedures during incidents |
| **Compliance Officer (2nd Line)** | Reviewer | Validates kill switches meet regulatory requirements |
| **AI Governance Committee** | Approver | Approves kill switch specifications for high-risk agents |

## Regulatory Basis

- **EU AI Act Article 14** -- Human oversight including ability to interrupt AI system operation
- **EU AI Act Article 15** -- Accuracy and robustness; systems must fail safely
- **DORA Article 11** -- ICT-related incident management with immediate response capability
- **DORA Article 12** -- Business continuity including emergency procedures
- **SAFEST A-09** -- Kill switch mechanisms for AI systems
- **SAFEST S-13** -- Fallback procedures and emergency stop

---

## 1. Kill Switch Metadata

| Field | Value | Description |
|-------|-------|-------------|
| **Kill Switch ID** | `KS-[AGENT_ID]-v[VERSION]` | Unique identifier |
| **Agent/Skill** | `[AGENT_NAME]` / `[SKILL_NAME]` | Target of kill switch |
| **Specification Version** | `[SEMVER]` | Version of this document |
| **Effective Date** | `[YYYY-MM-DD]` | When this spec becomes active |
| **Last Tested** | `[YYYY-MM-DD]` | Last successful test date |
| **Next Test Due** | `[YYYY-MM-DD]` | Next required test |
| **Owner** | `[NAME, ROLE]` | Accountable individual |
| **Approved By** | `[NAME, ROLE]` | Approver signature |

---

## 2. Three-Level Kill Switch Model

The kill switch specification defines three escalation levels, each mapping to MI9 containment levels:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        KILL SWITCH ESCALATION LEVELS                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  LEVEL 1: THROTTLE (MI9-L1)                                                  │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  • Reduce execution rate by X%                                      │   │
│  │  • Queue new requests with delay                                    │   │
│  │  • Increase monitoring granularity                                  │   │
│  │  • Alert on-call engineer                                           │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                              ↓ Trigger: Anomaly detected                     │
│  LEVEL 2: PAUSE (MI9-L2)                                                     │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  • Stop accepting new execution requests                            │   │
│  │  • Complete in-flight executions with timeout                       │   │
│  │  • Preserve state for investigation                                 │   │
│  │  • Page on-call engineer                                            │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                              ↓ Trigger: Safety threshold breached            │
│  LEVEL 3: FULL STOP (MI9-L3/L4)                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  • Terminate all agent processes immediately                        │   │
│  │  • Revoke all active credentials                                    │   │
│  │  • Block all tool invocations                                       │   │
│  │  • Activate fallback procedures                                     │   │
│  │  • Emergency page + executive notification                          │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.1 Level 1: Throttle (MI9-L1)

**Purpose:** Reduce agent capacity when anomalies are detected while maintaining partial service.

| Aspect | Specification |
|--------|--------------|
| **Trigger Conditions** | • Error rate exceeds 10% over 5-minute window<br>• Latency P95 exceeds 2x baseline<br>• Unusual pattern in tool invocations<br>• Guardrail trigger rate exceeds threshold |
| **Action** | Reduce execution rate to 50% of normal capacity |
| **Queue Behavior** | New requests queued with 30-second delay |
| **Monitoring** | Increased log sampling, real-time metrics to dashboard |
| **Notification** | Slack alert to #agent-alerts channel |
| **Human Response** | On-call engineer acknowledges within 15 minutes |
| **Recovery** | Automatic after 10 minutes if metrics normalize |
| **Escalation** | Auto-escalate to PAUSE if conditions persist > 15 min |

**Implementation:**
```yaml
throttle_config:
  trigger:
    error_rate_threshold: 0.10
    error_rate_window: "5m"
    latency_p95_multiplier: 2.0
  action:
    capacity_reduction_percent: 50
    queue_delay_seconds: 30
  notification:
    channels: ["slack:#agent-alerts", "pagerduty:low"]
  auto_recovery:
    enabled: true
    duration_minutes: 10
  escalation:
    to_pause_after_minutes: 15
```

### 2.2 Level 2: Pause (MI9-L2)

**Purpose:** Halt new executions while preserving in-flight operations for investigation.

| Aspect | Specification |
|--------|--------------|
| **Trigger Conditions** | • Safety threshold breached (confidence < minimum)<br>• Unauthorized action attempted<br>• Circuit breaker threshold exceeded<br>• Manual trigger by on-call engineer<br>• THROTTLE conditions persist > 15 minutes |
| **Action** | Stop accepting new requests; complete in-flight with 60s timeout |
| **Queue Behavior** | New requests rejected with "Service temporarily unavailable" |
| **State Preservation** | Full state snapshot saved for forensic analysis |
| **Notification** | Page on-call engineer; Slack #incident-response |
| **Human Response** | Engineer investigates within 30 minutes |
| **Recovery** | Manual only after root cause addressed |
| **Escalation** | Auto-escalate to FULL STOP if in-flight executions fail |

**Implementation:**
```yaml
pause_config:
  trigger:
    manual: true
    from_throttle_escalation: true
    safety_threshold_breach: true
    unauthorized_action: true
  action:
    accept_new_requests: false
    in_flight_timeout_seconds: 60
    state_preservation: true
  notification:
    channels: ["pagerduty:high", "slack:#incident-response"]
    page_on_call: true
  auto_recovery:
    enabled: false  # Manual only
  escalation:
    to_full_stop_on_in_flight_failure: true
```

### 2.3 Level 3: Full Stop (MI9-L3/L4)

**Purpose:** Immediate termination of all agent activity in emergency situations.

| Aspect | Specification |
|--------|--------------|
| **Trigger Conditions** | • Confirmed safety incident (bias, harmful output)<br>• Security breach detected<br>• Regulatory violation in progress<br>• Cascade failure affecting other systems<br>• Manual trigger by senior engineer or compliance<br>• PAUSE escalation conditions met |
| **Action** | Immediate process termination; credential revocation |
| **Tool Invocation** | All pending tool calls cancelled; connections closed |
| **Fallback Activation** | Customer-facing fallback procedures activated |
| **Notification** | Emergency page; executive notification; compliance alert |
| **Human Response** | Incident commander assigned; post-mortem initiated |
| **Recovery** | Requires formal review and explicit restart authorization |

**Implementation:**
```yaml
full_stop_config:
  trigger:
    manual:
      authorized_roles: ["senior_engineer", "compliance_officer", "incident_commander"]
    automatic:
      safety_incident_confirmed: true
      security_breach: true
      regulatory_violation: true
      cascade_failure: true
      from_pause_escalation: true
  action:
    terminate_processes: true
    revoke_credentials: true
    cancel_tool_invocations: true
    activate_fallback: true
  notification:
    channels: ["pagerduty:critical", "slack:#incident-command", "email:executive"]
    page_on_call: true
    notify_executive: true
  recovery:
    manual_only: true
    requires_review: true
    restart_authorization: ["ai_governance_committee", "ciso"]
```

---

## 3. Kill Switch Mechanisms

### 3.1 Automated Triggers

| Mechanism | Description | Response Time |
|-----------|-------------|---------------|
| **Circuit Breaker Trip** | Error rate/latency threshold exceeded | < 1 second |
| **Guardrail Violation** | Safety policy breach detected | < 100ms |
| **Loop Detection** | Recursive execution detected | < 500ms |
| **Budget Exhaustion** | Cost/token limit reached | < 100ms |
| **Anomaly Detection** | ML-based behavior anomaly | < 5 seconds |

### 3.2 Manual Triggers

| Mechanism | Access Level | Response Time |
|-----------|--------------|---------------|
| **Dashboard Button** | On-call engineer | < 5 seconds |
| **CLI Command** | Platform engineer | < 10 seconds |
| **Emergency API** | Authorized systems | < 2 seconds |
| **Physical/Virtual Big Red Button** | Operations center | < 1 second |

**CLI Command Example:**
```bash
# Throttle
agentctl kill-switch throttle --agent payments-agent-prod --reason "High error rate"

# Pause
agentctl kill-switch pause --agent payments-agent-prod --reason "Investigating anomaly"

# Full Stop
agentctl kill-switch stop --agent payments-agent-prod --reason "Safety incident"
```

### 3.3 Bulkhead Pattern Integration

Kill switches respect bulkhead boundaries—stopping one agent does not affect others:

```
┌─────────────────────────────────────────────────────────────────┐
│                      AGENT FLEET                                │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │ Agent A     │  │ Agent B     │  │ Agent C     │             │
│  │ [RUNNING]   │  │ [PAUSED]    │  │ [RUNNING]   │             │
│  │             │  │             │  │             │             │
│  │ Kill switch │  │ Kill switch │  │ Kill switch │             │
│  │ activated   │  │ activated   │  │ standby     │             │
│  │ → No effect │  │ → PAUSED    │  │             │             │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
│                                                                 │
│  Each agent has independent kill switch state                   │
│  Cascade failures prevented by bulkhead isolation               │
└─────────────────────────────────────────────────────────────────┘
```

---

## 4. Loop Detection

### 4.1 Detection Criteria

| Pattern | Description | Action |
|---------|-------------|--------|
| **Recursive Delegation** | Agent A → Agent B → Agent A | PAUSE after 3 cycles |
| **Infinite Loop** | Same tool invoked with identical parameters > N times | THROTTLE then PAUSE |
| **Chain Depth Exceeded** | Delegation chain longer than configured maximum | Reject new delegation |
| **Circular Dependency** | Detected via graph analysis of agent dependencies | Alert + THROTTLE |

### 4.2 Loop Prevention Configuration

```yaml
loop_detection:
  recursive_delegation:
    max_cycles: 3
    action: "PAUSE"
  
  tool_invocation:
    max_identical_calls: 5
    time_window: "1m"
    action: "THROTTLE"
  
  chain_depth:
    max_depth: 5
    action: "REJECT"
  
  circular_dependency:
    detection_interval: "5m"
    action: "ALERT"
```

---

## 5. MI9-to-Paper Mapping

| MI9 Level | Paper Concept | Kill Switch Level | Use Case |
|-----------|---------------|-------------------|----------|
| L0 | Normal Operation | None | Standard monitoring |
| L1 | Reduced Capacity | THROTTLE | Anomaly detected, maintain service |
| L2 | Suspended | PAUSE | Investigation required |
| L3 | Terminated | FULL STOP | Safety/security incident |
| L4 | Emergency | FULL STOP + Fallback | System-wide emergency |

---

## 6. Testing Requirements

### 6.1 Quarterly Kill Switch Test

| Test | Frequency | Success Criteria |
|------|-----------|------------------|
| THROTTLE activation | Quarterly | Capacity reduced within 5 seconds |
| PAUSE activation | Quarterly | New requests rejected within 3 seconds |
| FULL STOP activation | Quarterly | All processes terminated within 2 seconds |
| Manual trigger | Quarterly | All levels triggerable via CLI/dashboard |
| Auto-escalation | Quarterly | THROTTLE → PAUSE → FULL STOP chain works |
| Recovery procedure | Quarterly | Agent restarts successfully after each level |

### 6.2 Test Documentation

Each test must be documented with:
- Test date and time
- Tester name and role
- Kill switch level tested
- Trigger method (auto/manual)
- Response time measured
- Success/failure status
- Any issues observed

---

## 7. Integration with Fallback Procedures

Kill switches integrate with fallback procedures defined in `fallback-procedure.md`:

| Kill Switch Level | Fallback Activation |
|-------------------|---------------------|
| THROTTLE | Level 1 fallback (reduced capacity messaging) |
| PAUSE | Level 2 fallback (queue with wait time estimate) |
| FULL STOP | Level 3/4 fallback (human handoff or static page) |

**Cross-Reference:** [Fallback Procedure](fallback-procedure.md)

---

## 8. Related Artifacts

- [Fallback Procedure](fallback-procedure.md) -- Graceful degradation procedures
- [Circuit Breaker Config](circuit-breaker-config.yaml) -- Automated circuit breaker settings
- [Governance Enforcement Pipeline](../agentic-workflows/governance-enforcement-pipeline.md) -- Layer 5 (Circuit Breaker)
- [Agent Registry Entry](agent-registry-entry.yaml) -- Kill switch reference field
- [Skill Manifest](skill-manifest.yaml) -- Per-skill kill switch configuration

---

*Last updated: 2026-03-26 / Version: 1.0 / Classification: Internal*
