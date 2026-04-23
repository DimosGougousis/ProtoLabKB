# Governance Enforcement Pipeline

## Purpose

This document defines the 7-layer governance enforcement pipeline that wraps every agent execution. The pipeline ensures that governance policies are enforced at infrastructure level before any agent action can occur, implementing a "fail-closed" default where execution is blocked unless all governance checks pass. This is the single most impactful architectural addition for infrastructure-grade AI agent security.

The pipeline integrates with existing framework concepts (SAFEST, ARI, MI9, C1-C7) while adding granular runtime enforcement capabilities from the research paper's governance architecture.

## When to Use

- When designing agent runtime infrastructure and execution environments
- When implementing policy-as-code enforcement with OPA/Cedar
- When configuring multi-tenant agent deployments with isolation requirements
- When setting up circuit breakers, kill switches, and automated safety controls
- When auditing agent execution flows for compliance verification
- When implementing HITL (Human-in-the-Loop) gates at infrastructure level

## Who Is Responsible

| Role | R/A/C/I | Responsibility |
|------|---------|---------------|
| **Platform Architect** | Accountable | Designs and maintains the enforcement pipeline architecture |
| **MLOps / Platform Engineer** | Responsible | Implements pipeline components, configures policy engines |
| **Security Engineer** | Responsible | Implements RBAC, identity verification, and audit logging layers |
| **Compliance Officer (2nd Line)** | Reviewer | Validates pipeline meets regulatory requirements |
| **AI/ML Engineer** | Consulted | Integrates agents with pipeline SDK/API |
| **Internal Audit (3rd Line)** | Reviewer | Independently audits pipeline effectiveness |

## Regulatory Basis

- **EU AI Act Article 9** -- Risk management system including runtime monitoring and control
- **EU AI Act Article 14** -- Human oversight measures including ability to interrupt
- **EU AI Act Article 15** -- Accuracy, robustness, and cybersecurity requirements
- **DORA Article 9** -- ICT risk management framework with access controls
- **DORA Article 11** -- ICT-related incident management with automated detection
- **SAFEST S-08** -- Access controls and permission boundaries
- **SAFEST A-09** -- Kill switch mechanisms for AI systems
- **SAFEST A-06** -- Human-in-the-loop controls

---

## 1. The 7-Layer Pipeline Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         GOVERNANCE ENFORCEMENT PIPELINE                      │
│                    (Fail-Closed Default: Block Unless Pass)                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐  │
│  │   LAYER 1   │───>│   LAYER 2   │───>│   LAYER 3   │───>│   LAYER 4   │  │
│  │ COMPLIANCE  │    │   BUDGET    │    │    RBAC     │    │    HITL     │  │
│  │    CHECK    │    │    CHECK    │    │    CHECK    │    │    GATE     │  │
│  └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘  │
│         │                  │                  │                  │         │
│         v                  v                  v                  v         │
│    [BLOCK/PASS]       [BLOCK/PASS]       [BLOCK/PASS]       [BLOCK/PASS]   │
│                                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐                     │
│  │   LAYER 5   │───>│   LAYER 6   │───>│   LAYER 7   │                     │
│  │   CIRCUIT   │    │    AUDIT    │    │  EXECUTION  │                     │
│  │   BREAKER   │    │    LOG      │    │   WRAPPER   │                     │
│  └─────────────┘    └─────────────┘    └─────────────┘                     │
│         │                  │                  │                            │
│         v                  v                  v                            │
│    [THROTTLE/          [APPEND]          [AGENT                           │
│     PAUSE/STOP]                          EXECUTES]                         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 1.1 Layer 1: Compliance Check

**Purpose:** Verify the execution context complies with all applicable regulatory and policy constraints.

| Check | Description | Failure Action |
|-------|-------------|----------------|
| Jurisdiction Validation | Verify execution is permitted in the data residency zone | Block with compliance violation error |
| Regulatory Status | Check if agent is approved for the target use case per EU AI Act, DORA, etc. | Block with regulatory reference |
| Data Classification | Verify data sensitivity level matches agent authorization | Block with data classification mismatch |
| Time-Based Rules | Enforce time-of-day, day-of-week restrictions | Block with policy violation |
| Volume Limits | Check per-period execution limits (hourly/daily) | Queue or block with rate limit error |

**Implementation:** OPA (Open Policy Agent) or Cedar policy engine evaluating YAML compliance rules.

**Cross-Reference:** [Compliance-as-Configuration](../templates/compliance-as-configuration.md)

### 1.2 Layer 2: Budget Check

**Purpose:** Enforce hierarchical budget caps before execution consumes resources.

| Check | Description | Failure Action |
|-------|-------------|----------------|
| Tenant Cap | Organization-level budget consumption | Block with budget exceeded error |
| User Cap | Per-user budget allocation | Block or request budget increase |
| Agent Cap | Per-agent budget limit | Block with agent budget exhausted |
| Skill Cap | Per-skill budget allocation | Block or downgrade to cheaper model |
| Run Cap | Per-execution token/cost limit | Block with run limit exceeded |

**Budget Hierarchy:**
```
Tenant Budget (Org Level)
    └── User Budget
            └── Agent Budget
                    └── Skill Budget
                            └── Run Budget (Current Execution)
```

**Cross-Reference:** [Budget Cap Configuration](../templates/budget-cap-config.yaml), [Cost Attribution Dashboard](../../06-executive/financial-governance/cost-attribution-dashboard.md)

### 1.3 Layer 3: RBAC Check

**Purpose:** Verify the agent/skill has permission to perform the requested action.

| Check | Description | Failure Action |
|-------|-------------|----------------|
| Identity Verification | Validate SPIFFE workload identity | Block with authentication error |
| Permission Matrix | Check skill-level permission grants | Block with authorization error |
| Delegation Chain | Verify delegation authorization is valid | Block with invalid delegation |
| TTL Validation | Check identity token has not expired (15-min TTL for high-risk) | Block with expired credentials |
| Scope Validation | Verify requested action is within granted scope | Block with scope violation |

**Cross-Reference:** [Agent Permission Boundaries](agent-permission-boundaries.md), [SPIFFE Agent Identity](../guides/spiffe-agent-identity.md)

### 1.4 Layer 4: HITL Gate

**Purpose:** Route execution through human approval based on confidence scoring and risk thresholds.

| Check | Description | Action |
|-------|-------------|--------|
| Confidence Score | Calculate composite confidence: log-prob (40%) + self-assessment (40%) + semantic distance (20%) | Route to appropriate authority level |
| Threshold Band | Compare against 4 threshold bands (Critical/High/Medium/Low) | A1-A4 authority routing |
| Authority Level | A1: Full Autonomy, A2: Notify & Execute, A3: Decide & Confirm, A4: Recommend Only | Enforce HITL/HOTL/HOTA model |
| Queue Position | If human approval required, check queue depth and SLA | Queue with estimated wait time |

**Confidence Formula:**
```
Composite Confidence = (0.40 × Log Probability) + 
                       (0.40 × Self-Assessment) + 
                       (0.20 × Semantic Distance)
```

**Cross-Reference:** [Human-in-the-Loop Patterns](human-in-the-loop-patterns.md), [Autonomous Decision Governance](autonomous-decision-governance.md)

### 1.5 Layer 5: Circuit Breaker

**Purpose:** Prevent cascade failures and protect system stability.

| Check | Description | Action |
|-------|-------------|--------|
| Error Rate | Monitor error percentage over time window | Throttle → Pause → Full Stop |
| Latency Threshold | Check P95/P99 latency against SLA | Throttle with backoff |
| Loop Detection | Detect recursive agent loops or circular delegations | Pause for investigation |
| Bulkhead Status | Check resource pool availability | Reject or queue |
| Dependency Health | Verify downstream services are healthy | Fail fast with dependency error |

**Circuit Breaker States:**
```
CLOSED: Normal operation, requests pass through
    │
    ▼ (error threshold exceeded)
OPEN: Block requests immediately, return fallback
    │
    ▼ (timeout elapsed)
HALF-OPEN: Allow limited test requests
    │
    ▼ (test success)
CLOSED: Resume normal operation
```

**MI9 Mapping:**
| Circuit State | MI9 Level | Description |
|---------------|-----------|-------------|
| Throttle | MI9-L1 | Reduced capacity, queue requests |
| Pause | MI9-L2 | Stop new executions, complete in-flight |
| Full Stop | MI9-L3/L4 | Terminate all agent activity |

**Cross-Reference:** [Circuit Breaker Configuration](../templates/circuit-breaker-config.yaml), [Kill Switch Specification](../templates/kill-switch-specification.md)

### 1.6 Layer 6: Audit Log

**Purpose:** Create immutable, append-only audit records for every execution attempt.

| Field | Description | Integrity Mechanism |
|-------|-------------|---------------------|
| Record ID | Unique identifier for this audit record | UUID v4 |
| Timestamp | Precise execution time (UTC) | NTP-synchronized |
| Chain ID | Links to delegation chain | Foreign key to chain audit |
| Previous Hash | SHA-256 hash of previous record | Integrity chain |
| Agent/Skill IDs | Identifiers for executing entities | SPIFFE identity |
| Policy Decisions | Results from Layers 1-5 | Structured JSON |
| Input/Output | Request and response (sanitized) | Encrypted at rest |
| Outcome | Success, failure, or blocked | Enum with reason code |

**Integrity Chain:**
```
Record N: { data..., prev_hash: Hash(Record N-1) }
Record N+1: { data..., prev_hash: Hash(Record N) }
```

Any tampering with historical records breaks the chain and is detectable.

**Cross-Reference:** [Audit Record Schema](../templates/audit-record-schema.yaml), [Delegation Chain Audit](delegation-chain-audit.md)

### 1.7 Layer 7: Execution Wrapper

**Purpose:** Execute the agent with runtime monitoring and safety controls.

| Function | Description |
|----------|-------------|
| Sandbox Isolation | Execute in isolated compute environment |
| Resource Limits | Enforce CPU, memory, and time limits |
| Model Routing | Route to appropriate model based on complexity and budget |
| Tool Interception | Intercept and log all tool calls |
| Output Validation | Validate outputs against safety policies |
| Telemetry Emission | Emit OpenTelemetry spans for observability |

---

## 2. Infrastructure-Layer Enforcement Principles

### 2.1 Fail-Closed Default

The pipeline operates on a "fail-closed" principle: **execution is blocked unless all checks explicitly pass**. This is the opposite of "fail-open" systems where lack of policy decision allows execution.

| Scenario | Fail-Open (Dangerous) | Fail-Closed (Secure) |
|----------|----------------------|----------------------|
| Policy engine unavailable | Allow execution | Block execution |
| RBAC service timeout | Allow with default perms | Block with auth error |
| Audit log full | Continue without logging | Block until resolved |
| Circuit breaker malfunction | Assume healthy | Assume tripped |

### 2.2 Latency Budget

Each layer consumes part of the total latency budget. Design targets:

| Layer | Target Latency | Max Latency |
|-------|---------------|-------------|
| Compliance Check | < 5ms | 20ms |
| Budget Check | < 2ms | 10ms |
| RBAC Check | < 5ms | 20ms |
| HITL Gate | < 10ms (if automated) | 50ms |
| Circuit Breaker | < 1ms | 5ms |
| Audit Log | Async (< 1ms blocking) | 5ms |
| **Total Pipeline** | **< 25ms** | **100ms** |

### 2.3 Policy Engine Integration

The pipeline integrates with policy-as-code engines:

**OPA (Open Policy Agent):**
```rego
package agent.execution

import future.keywords.if
import future.keywords.in

default allow := false

allow if {
    input.compliance.jurisdiction in input.agent.authorized_jurisdictions
    input.budget.remaining > input.request.estimated_cost
    input.rbac.permissions[_] == input.request.action
    input.circuit_breaker.state == "CLOSED"
}
```

**Cedar:**
```cedar
permit (
    principal == Agent::"onboarding-agent-prod",
    action == Action::"verify_identity",
    resource == Customer::"*"
)
when {
    context.compliance_approved &&
    context.budget_available &&
    context.circuit_closed
};
```

---

## 3. Cross-Reference to Existing Framework

| Pipeline Layer | SAFEST Items | ARI | MI9 | Data Contracts |
|----------------|--------------|-----|-----|----------------|
| Layer 1: Compliance | S-01, S-02, S-08 | Risk classification input | - | C1 (Purpose) |
| Layer 2: Budget | S-10, S-11 | Cost risk dimension | - | C4 (Cost) |
| Layer 3: RBAC | S-08, S-09, A-07 | Agency risk scoring | L0-L4 containment | C2 (Permissions) |
| Layer 4: HITL | A-06, A-07 | Override triggers | L1-L2 escalation | C7 (Decisions) |
| Layer 5: Circuit Breaker | A-09, S-13 | Failure mode containment | L1-L4 levels | C6 (Safety) |
| Layer 6: Audit | A-01, A-11, S-12 | Audit trail | - | C7 (Decisions) |
| Layer 7: Execution | S-03, S-14 | Runtime validation | L0 baseline | C3 (Quality) |

---

## 4. Implementation Checklist

- [ ] Policy engine deployed (OPA/Cedar) with high availability
- ] Budget service integrated with cost attribution system
- [ ] SPIFFE/SPIRE infrastructure for workload identity
- [ ] HITL queue system with SLA monitoring
- [ ] Circuit breaker library integrated with MI9 containment
- [ ] Audit log storage with integrity chain verification
- [ ] Pipeline SDK for agent integration
- [ ] Monitoring dashboards for pipeline health
- [ ] Runbook for pipeline failure scenarios

---

## 5. Related Artifacts

- [Skill Manifest](../templates/skill-manifest.yaml) -- Per-skill configuration for pipeline
- [Agent Registry Entry](../templates/agent-registry-entry.yaml) -- Agent-level pipeline configuration
- [Circuit Breaker Config](../templates/circuit-breaker-config.yaml) -- Circuit breaker thresholds
- [Kill Switch Specification](../templates/kill-switch-specification.md) -- Emergency stop procedures
- [Audit Record Schema](../templates/audit-record-schema.yaml) -- Audit log format
- [Compliance-as-Configuration](../templates/compliance-as-configuration.md) -- Policy engine setup

---

*Last updated: 2026-03-26 / Version: 1.0 / Classification: Internal*
