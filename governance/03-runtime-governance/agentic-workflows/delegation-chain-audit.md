# Delegation Chain Audit

## Purpose

This document defines how to trace, audit, and reconstruct autonomous decision chains in multi-agent systems. When an orchestrator agent delegates tasks to sub-agents, and those sub-agents invoke tools or make decisions, the resulting delegation chain must be fully auditable -- from the initial customer request to the final action. Without structured delegation chain auditing, accountability gaps emerge: no one can explain why a decision was made, who (or what) made it, or whether the chain of authority was valid.

Delegation chain auditing is the forensic backbone of multi-agent governance. It answers the question: "When something goes wrong in a multi-agent workflow, can we reconstruct exactly what happened, why, and who was responsible?"

## When to Use

- When designing multi-agent orchestration architectures
- When implementing audit logging for agent-to-agent delegation
- When investigating incidents involving multi-agent decision chains
- When preparing for regulatory audits of automated decision-making
- When defining chain depth limits and permission inheritance rules
- When conducting post-incident forensic reconstruction

## Who Is Responsible

| Role | R/A/C/I | Responsibility |
|------|---------|---------------|
| **Model Owner** | Accountable | Owns delegation chain integrity for their agent(s) |
| **AI/ML Engineer** | Responsible | Implements delegation logging, chain validation, and audit trail |
| **MLOps / Platform Engineer** | Responsible | Builds audit log infrastructure, ensures log integrity and retention |
| **Compliance Officer (2nd Line)** | Reviewer | Validates delegation chains meet regulatory requirements |
| **Internal Audit (3rd Line)** | Reviewer | Independently audits delegation chain completeness and correctness |

## Regulatory Basis

- **EU AI Act Article 12** -- Record-keeping obligations for high-risk AI systems, including logs of delegation and decision events
- **EU AI Act Article 14** -- Human oversight, including ability to reconstruct decision chains
- **DORA Article 9** -- ICT risk management, including audit trails for automated processes
- **SAFEST A-01** (board-level accountability for AI decisions), **A-11** (complete audit trail)
- **GDPR Article 22** -- Right to explanation requires reconstructable decision chains

---

## 1. Delegation Chain Structure

### 1.1 What Is a Delegation Chain?

A delegation chain is the sequence of agent-to-agent task delegations that occurs when a complex request is processed. Each link in the chain represents a delegation event: one agent assigning a task to another.

```
Customer Request
  |
  v
[Link 0] Orchestrator Agent receives request
  |
  +--[Link 1] Orchestrator delegates "verify identity" to KYC Agent
  |    |
  |    +--[Link 1.1] KYC Agent invokes Identity Verification Service (tool call)
  |    +--[Link 1.2] KYC Agent invokes Document Checker (tool call)
  |    |
  |    +--[Return] KYC Agent returns verification result to Orchestrator
  |
  +--[Link 2] Orchestrator delegates "assess risk" to Risk Scoring Agent
  |    |
  |    +--[Link 2.1] Risk Scoring Agent reads credit bureau data (tool call)
  |    +--[Link 2.2] Risk Scoring Agent invokes risk model (tool call)
  |    |
  |    +--[Return] Risk Scoring Agent returns risk score to Orchestrator
  |
  +--[Link 3] Orchestrator delegates "screen compliance" to Compliance Agent
  |    |
  |    +--[Link 3.1] Compliance Agent invokes sanctions screening (tool call)
  |    +--[Return] Compliance Agent returns screening result to Orchestrator
  |
  v
[Decision Point] Orchestrator aggregates results and recommends approval
  |
  v
[HITL] Human reviewer approves/rejects
```

### 1.2 Chain Metadata

Every delegation chain must carry the following metadata:

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `chain_id` | string | Globally unique identifier for the entire chain | `chain:onb-2026-03-01-a7f3c` |
| `trace_id` | string | Links to the observability trace (LangSmith/Langfuse) | `trace-2026-03-01-b8e4d` |
| `customer_id` | string (hashed) | Pseudonymized customer identifier | `cust:hash:9f8a2b` |
| `initiated_at` | datetime | When the chain started | `2026-03-01T14:22:05.123Z` |
| `completed_at` | datetime | When the chain completed (or failed) | `2026-03-01T14:23:18.456Z` |
| `chain_depth` | integer | Maximum depth of delegation in this chain | `2` |
| `chain_status` | enum | `completed`, `failed`, `timeout`, `escalated` | `completed` |
| `final_outcome` | string | Result of the chain | `application_approved` |
| `hitl_involved` | boolean | Whether a human was involved in the chain | `true` |

---

## 2. Audit vs Observability Separation

This document addresses the critical distinction between **audit logs** and **observability telemetry**:

| Aspect | Audit Logs | Observability Telemetry |
|--------|------------|------------------------|
| **Purpose** | Compliance, forensic investigation, regulatory evidence | System health, performance monitoring, debugging |
| **Retention** | 7+ years (regulatory requirement) | 30-90 days (operational need) |
| **Integrity** | Cryptographically protected (hash chain) | No integrity guarantees |
| **Content** | Decisions, authorizations, outcomes | Latency, throughput, error rates |
| **Access** | Restricted (compliance, legal, audit) | Broad (engineering, operations) |
| **Standard** | Audit Record Schema (20+ fields) | OpenTelemetry gen_ai.* conventions |

**Key Principle:** Audit logs are the "source of truth" for compliance; observability is for operational health. Never rely on observability data for regulatory evidence.

**Cross-Reference:** [Audit Record Schema](../../04-operational-governance/templates/audit-record-schema.yaml) for full audit schema specification.

---

## 3. Integrity Chain for Delegation Audit

Every delegation chain participates in the integrity chain mechanism:

```
Record 1 (Chain Start):
  record_id: "rec-001"
  prev_record_hash: "0x0000..." (genesis)
  current_hash: "0xa1b2..."
  
Record 2 (First Delegation):
  record_id: "rec-002"
  prev_record_hash: "0xa1b2..." (hash of rec-001)
  current_hash: "0xc3d4..."
  
Record 3 (Second Delegation):
  record_id: "rec-003"
  prev_record_hash: "0xc3d4..." (hash of rec-002)
  current_hash: "0xe5f6..."
```

Any tampering with historical delegation records breaks the chain and is immediately detectable.

**Implementation Requirements:**
- Each delegation record includes `prev_record_hash` field
- Hash covers all record fields except `current_hash` itself
- SHA-256 hashing algorithm
- Append-only storage (no updates, only inserts)
- Regular chain integrity verification (daily)

---

## 4. Audit Log Schema for Delegations

### 4.1 Delegation Event Schema

Every delegation event in the chain must be logged with the following fields (extending the base [Audit Record Schema](../../04-operational-governance/templates/audit-record-schema.yaml)):

```yaml
delegation_event:
  event_id: "del-2026-03-01-001"          # Unique event identifier
  chain_id: "chain:onb-2026-03-01-a7f3c"  # Parent chain identifier
  timestamp: "2026-03-01T14:22:06.234Z"   # When this delegation occurred

  delegator:
    agent_id: "agent:onboarding-orchestrator-prod-01"
    agent_name: "Onboarding Orchestrator"
    nhi_identity: "nhi:onboarding-orchestrator-prod-01"
    permission_boundary_ref: "PB-ONBOARDING-v1.2"

  delegate:
    agent_id: "agent:kyc-agent-prod-01"
    agent_name: "KYC Verification Agent"
    nhi_identity: "nhi:kyc-agent-prod-01"
    permission_boundary_ref: "PB-KYC-v2.1"

  task:
    task_description: "Verify customer identity using provided documents"
    task_type: "identity_verification"
    inputs_provided:
      - "document_type: passport"
      - "document_country: NL"
      - "customer_reference: cust:hash:9f8a2b"
    expected_output_type: "verification_result"

  permissions:
    delegator_permissions_at_time: ["read:customer_data", "invoke:kyc_tools"]
    delegate_permissions_granted: ["read:customer_documents", "invoke:id_verification"]
    permission_escalation_detected: false

  chain_position:
    depth: 1                               # How deep in the chain
    parent_event_id: null                   # null for first-level delegations
    sequence_number: 1                      # Order within this depth level

  result:
    status: "completed"                     # completed | failed | timeout | escalated
    output_summary: "identity_verified, confidence: 0.94"
    duration_ms: 4521
    tools_invoked: ["identity-verify-v2", "document-checker-v1"]
    errors: []
```

### 2.2 Tool Invocation Sub-Events

Each tool call within a delegated task is also logged:

```yaml
tool_invocation:
  event_id: "tool-2026-03-01-001"
  parent_delegation_event_id: "del-2026-03-01-001"
  chain_id: "chain:onb-2026-03-01-a7f3c"
  timestamp: "2026-03-01T14:22:07.001Z"

  agent_id: "agent:kyc-agent-prod-01"
  tool_id: "identity-verify-v2"
  tool_version: "2.1.0"

  input_parameters:
    document_type: "passport"
    document_country: "NL"

  output:
    status: "verified"
    confidence: 0.94
    verification_method: "biometric_match + document_validation"

  permission_check:
    authorized: true
    policy_ref: "payment-agent-policy-v3"

  execution:
    duration_ms: 2103
    sandbox_id: "sandbox-kyc-001"
    network_segment: "internal-kyc"
```

---

## 3. Chain Depth Limits

### 3.1 Maximum Delegation Depth

| Risk Tier | Maximum Chain Depth | Rationale |
|-----------|-------------------|-----------|
| Minimal | 2 (agent + one tool layer) | Simple workflows; minimal compound error risk |
| Limited | 3 (orchestrator + sub-agent + tool) | Standard multi-agent workflows |
| High | 3 (strictly enforced) | Deep chains become unauditable; compound error risk is too high |

### 3.2 Depth Enforcement

```
Agent A attempts to delegate to Agent B
  |
  v
Check current chain depth
  |
  +-- depth < max_allowed --> Allow delegation; increment depth counter
  |
  +-- depth = max_allowed --> BLOCK delegation; log violation
       |
       v
       Agent A must either:
       (a) Handle the task directly using its own tools
       (b) Escalate to a human with context
       (c) Return an error to the parent agent
```

### 3.3 Chain Depth Violation Handling

When a chain depth limit is reached:
1. Log the violation with full chain context
2. Alert the Model Owner
3. The agent at the depth limit must not delegate further
4. Review the workflow design -- persistent depth violations indicate an architecture problem

---

## 4. Permission Inheritance Rules

### 4.1 Core Rules

| Rule | Description | Example |
|------|-------------|---------|
| **No escalation** | A delegate agent cannot have broader permissions than its delegator | If Orchestrator cannot access credit limits, neither can any agent it delegates to |
| **Intersection model** | Delegate permissions = intersection of (delegator's permissions) AND (delegate's own boundary) | Orchestrator has [A, B, C]; Sub-agent has [B, C, D]; effective permissions for delegated task = [B, C] |
| **Task-scoped** | Permissions granted for delegation are scoped to the specific task, not the delegate's full boundary | KYC Agent has access to customer documents only for the specific customer in the delegation |
| **Time-bounded** | Delegated permissions expire when the task completes or times out | If delegation task has a 5-minute timeout, all granted permissions expire at timeout |
| **Non-transferable** | A delegate cannot further delegate the permissions it received via delegation without explicit allowance | KYC Agent cannot delegate its document access to another sub-agent unless the chain policy allows it |

### 4.2 Permission Inheritance Validation

At every delegation event, the system must validate:

```
BEFORE delegation executes:
  1. Verify delegator has the permissions it is granting
  2. Verify delegate's permission boundary includes the required permissions
  3. Compute effective permissions = intersection(delegator, delegate, task_scope)
  4. Log effective permissions in the delegation event
  5. If effective permissions are insufficient for the task, BLOCK and escalate

DURING delegation:
  6. Monitor delegate's tool invocations against effective permissions
  7. Block any tool call outside effective permissions
  8. Log all permission checks (pass and fail)

AFTER delegation:
  9. Revoke task-scoped permissions
  10. Verify no persistent permission elevation occurred
```

---

## 5. Break-the-Chain Patterns

### 5.1 When to Break the Chain

A delegation chain must be broken (halted and escalated) when:

| Trigger | Action | Escalation Target |
|---------|--------|-------------------|
| Chain depth limit reached | Block further delegation | Orchestrator handles directly or escalates to human |
| Permission escalation detected | Halt chain immediately | Security incident + Model Owner notification |
| Sub-agent returns error | Orchestrator evaluates: retry, alternative agent, or escalate | Model Owner if retries exhausted |
| Sub-agent confidence below threshold | Orchestrator does not use the result | Human reviewer for the specific task |
| Chain duration exceeds timeout | Halt all pending delegations | Customer notification + human takeover |
| Safety violation detected at any point | Kill switch: halt entire chain | Incident response team |
| Circular delegation detected | Block and log | Architecture review required |

### 5.2 Chain Break Audit Record

```yaml
chain_break:
  chain_id: "chain:onb-2026-03-01-a7f3c"
  break_timestamp: "2026-03-01T14:23:45.789Z"
  break_reason: "sub_agent_confidence_below_threshold"
  break_point:
    agent_id: "agent:risk-scoring-agent-prod-01"
    delegation_event_id: "del-2026-03-01-002"
    depth: 2

  context:
    chain_progress: "2/3 delegations completed"
    completed_results: ["identity_verified", "pending"]
    pending_tasks: ["compliance_screening"]

  resolution:
    action_taken: "escalated_to_human"
    human_reviewer: "analyst@company.com"
    resolution_timestamp: "2026-03-01T14:35:12.001Z"
    resolution_outcome: "human_completed_risk_assessment_manually"
```

---

## 6. Forensic Reconstruction

### 6.1 Reconstruction Process

When an incident requires investigation, the delegation chain must be fully reconstructable:

| Step | Action | Data Source |
|------|--------|-------------|
| 1 | Identify the chain ID from the incident report or customer complaint | Incident management system |
| 2 | Retrieve all delegation events for the chain | Audit log database |
| 3 | Retrieve all tool invocation events for the chain | Audit log database |
| 4 | Retrieve observability traces (reasoning spans) | LangSmith / Langfuse / Arize Phoenix |
| 5 | Reconstruct the chain chronologically | Automated reconstruction tool |
| 6 | Validate permission checks at each delegation | Permission validation replay |
| 7 | Identify the point of failure or incorrect decision | Root cause analysis |
| 8 | Generate forensic report | Governance reporting tool |

### 6.2 Forensic Report Template

```
DELEGATION CHAIN FORENSIC REPORT
=================================
Report ID:        FR-2026-03-01-001
Chain ID:         chain:onb-2026-03-01-a7f3c
Incident Ref:     INC-2026-003
Prepared By:      [Investigator name]
Date:             2026-03-01

1. SUMMARY
   A customer onboarding application was incorrectly approved despite
   a partial sanctions screening match. The delegation chain shows the
   Compliance Agent returned a "potential_match" result, but the
   Orchestrator incorrectly interpreted this as "clear" due to a
   prompt template error.

2. CHAIN TIMELINE
   14:22:05.123Z  Chain initiated (customer application received)
   14:22:06.234Z  Delegation 1: KYC Agent (identity verification) -- PASSED
   14:22:11.456Z  Delegation 2: Risk Scoring Agent -- PASSED (score: 72)
   14:22:16.789Z  Delegation 3: Compliance Agent -- RETURNED "potential_match"
   14:22:17.012Z  Orchestrator processed result as "clear" <-- ERROR POINT
   14:22:17.345Z  Orchestrator recommended approval
   14:22:18.456Z  HITL reviewer approved (did not see potential_match)

3. ROOT CAUSE
   Orchestrator prompt template mapped "potential_match" to the same
   handling as "clear" due to a missing conditional branch.

4. PERMISSION CHAIN ANALYSIS
   All permission boundaries were respected. No escalation violations.

5. RECOMMENDATIONS
   (a) Fix prompt template to route "potential_match" to HITL escalation
   (b) Add eval test case for "potential_match" handling
   (c) Enhance HITL review screen to highlight screening results
```

### 6.3 Reconstruction Retention

| Data Type | Retention Period | Justification |
|-----------|-----------------|---------------|
| Delegation events | 5 years (high-risk) / 3 years (limited) | DORA record-keeping requirements |
| Tool invocation events | 5 years (high-risk) / 3 years (limited) | Regulatory audit trail |
| Observability traces | 1 year full detail / 5 years summary | Storage cost vs. audit need |
| Permission validation logs | 5 years (all tiers) | Security audit |
| Forensic reports | Permanent | Institutional learning |

---

## 7. FinTech Example: Multi-Agent Onboarding Delegation Chain

### 7.1 Complete Chain Walkthrough

```
CHAIN: chain:onb-2026-03-01-a7f3c
Customer: cust:hash:9f8a2b (Jan de Vries, NL resident)
Application: Open personal checking account

LINK 0 - ORCHESTRATOR (Onboarding Orchestrator v1.3)
  Received: Customer application with passport scan and address proof
  Decision: Standard onboarding workflow (3 parallel delegations)
  Permissions: [read:application_data, delegate:kyc, delegate:risk, delegate:compliance]

LINK 1 - KYC AGENT (KYC Verification Agent v2.1)
  Task: Verify identity from passport scan
  Tools invoked:
    - identity-verify-v2: biometric match (confidence: 0.94) -- PASS
    - document-checker-v1: document validation (authentic: true) -- PASS
  Result: identity_verified (confidence: 0.94)
  Duration: 4.5 seconds
  Permission check: PASS (all tools within boundary)

LINK 2 - RISK SCORING AGENT (Risk Scoring Agent v1.8)
  Task: Assess customer risk profile
  Tools invoked:
    - credit-bureau-read-v1: retrieved credit history -- score: 720
    - risk-model-v3: computed risk score -- 72 (low-medium risk)
  Result: risk_score: 72, recommendation: standard_account
  Duration: 3.2 seconds
  Permission check: PASS

LINK 3 - COMPLIANCE AGENT (Compliance Screening Agent v1.5)
  Task: Screen against sanctions, PEP, and adverse media
  Tools invoked:
    - sanctions-screen-v2: no match -- CLEAR
    - pep-check-v1: no match -- CLEAR
    - adverse-media-v1: no significant hits -- CLEAR
  Result: screening_clear
  Duration: 5.1 seconds
  Permission check: PASS

DECISION POINT - ORCHESTRATOR
  Inputs: [identity_verified, risk_score: 72, screening_clear]
  Decision: Recommend approval for standard checking account
  Confidence: 0.96
  Action: Queue for HITL approval (per oversight model)

HITL REVIEW - Human Analyst (Sarah K., Senior Onboarding Analyst)
  Review time: 2 minutes 14 seconds
  Decision: APPROVED
  Notes: "All checks passed. Standard application."

CHAIN COMPLETE
  Total duration: 72.3 seconds
  Chain depth: 2 (orchestrator + sub-agents)
  Permission violations: 0
  Escalations: 0
  HITL involved: Yes (final approval)
```

---

## Cross-References

- **Agent Fleet Operations:** [agent-fleet-operations.md](agent-fleet-operations.md) -- registry and dashboard integration for delegation chain monitoring
- **Multi-Agent Governance Framework:** [multi-agent-governance-framework.md](multi-agent-governance-framework.md) -- delegation rules, permission model, and audit trail requirements
- **Agent Permission Boundaries:** [agent-permission-boundaries.md](agent-permission-boundaries.md) -- permission inheritance and tool sovereignty layers
- **Human-in-the-Loop Patterns:** [human-in-the-loop-patterns.md](human-in-the-loop-patterns.md) -- HITL decision points within delegation chains
- **Inter-Agent Protocols:** [inter-agent-protocols.md](inter-agent-protocols.md) -- communication standards between agents in a delegation chain
- **Autonomous Decision Governance:** [autonomous-decision-governance.md](autonomous-decision-governance.md) -- decision authority at each point in the chain
- **Continuous Online Evaluation:** [../evaluations/continuous-online-evaluation.md](../evaluations/continuous-online-evaluation.md) -- observability infrastructure for chain tracing
- **Three Lines of Defense:** [../../07-enterprise-implementation/organizational-model/three-lines-of-defense-for-ai.md](../../07-enterprise-implementation/organizational-model/three-lines-of-defense-for-ai.md) -- audit responsibilities across lines

---

*Last updated: 2026-03-01*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
