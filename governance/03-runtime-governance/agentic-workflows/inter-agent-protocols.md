# Inter-Agent Communication Protocols

## Purpose

This document defines the governance standards for communication between business AI agents in multi-agent architectures. When agents communicate with each other -- delegating tasks, passing data, negotiating capabilities, and sharing results -- every interaction must be authenticated, validated, isolated, and logged. Ungoverned inter-agent communication creates attack surfaces for prompt injection propagation, credential leakage, data contamination, and accountability gaps.

Inter-agent protocols ensure that agents interact with each other as securely and formally as microservices interact with APIs -- with authentication, authorization, schema validation, and audit trails at every boundary.

## When to Use

- When designing multi-agent architectures with agent-to-agent communication
- When implementing orchestrator-sub-agent delegation patterns
- When adding a new agent to an existing multi-agent fleet
- When auditing communication patterns between agents
- When investigating security incidents involving agent-to-agent interactions
- When establishing trust boundaries between agent domains

## Who Is Responsible

| Role | R/A/C/I | Responsibility |
|------|---------|---------------|
| **AI/ML Engineer** | Responsible | Implements communication protocols, message schemas, and validation logic |
| **Security Engineer** | Responsible | Implements NHI mutual authentication, trust boundary enforcement |
| **MLOps / Platform Engineer** | Responsible | Builds communication infrastructure, logging, and monitoring |
| **Model Owner** | Accountable | Owns the communication policies for their agent(s) |
| **Compliance Officer (2nd Line)** | Reviewer | Validates data isolation and privacy compliance in inter-agent communication |

## Regulatory Basis

- **EU AI Act Article 15** -- Accuracy, robustness, and cybersecurity requirements, including protection against unauthorized access
- **EU AI Act Article 9** -- Risk management for interactions between AI systems and other systems
- **DORA Article 9** -- ICT risk management, including secure communication protocols
- **GDPR Article 25** -- Data protection by design, including data minimization in inter-agent data flows
- **SAFEST S-08** (access controls), **S-09** (data protection), **A-11** (audit trail)

---

## 1. NHI-Based Mutual Authentication

### 1.1 Agent-to-Agent Authentication

Every inter-agent communication must be mutually authenticated using Machine Identity / Non-Human Identity (NHI) credentials. No agent may accept unauthenticated messages from another agent.

| Authentication Step | Description | Implementation |
|--------------------|-------------|----------------|
| **Identity assertion** | Sending agent presents its NHI identity token | Signed JWT with agent_id, nhi_identity, issued_at, expires_at |
| **Identity verification** | Receiving agent verifies the token against the IAM system | Token signature verification + IAM lookup to confirm active identity |
| **Mutual TLS** | Communication channel is encrypted and both endpoints verified | mTLS between agent runtimes; certificates issued per NHI identity |
| **Permission verification** | Receiving agent checks if sender is authorized to communicate | Allowlist of authorized sender agent IDs per receiving agent |
| **Session binding** | Communication is bound to a specific chain_id and trace_id | Prevents replay attacks; ensures messages belong to the correct workflow |

### 1.2 Authentication Failure Handling

| Failure Type | Agent Behavior | Logging |
|-------------|---------------|---------|
| Invalid token | Reject message; do not process | Log with sender identity (if available) and rejection reason |
| Expired token | Reject message; request token refresh | Log expiration details |
| Unknown sender | Reject message; alert security | Security alert: unknown agent attempting communication |
| Sender not in allowlist | Reject message; log violation | Log policy violation with full context |
| mTLS handshake failure | Drop connection | Log connection attempt with source details |

---

## 2. Message Format Standards

### 2.1 Inter-Agent Message Schema

All inter-agent messages must follow a structured schema. Free-text messages between agents are prohibited -- they create prompt injection vectors.

```yaml
inter_agent_message:
  # Header (mandatory)
  header:
    message_id: "msg-2026-03-01-a1b2c3"       # Unique message identifier
    chain_id: "chain:onb-2026-03-01-a7f3c"     # Delegation chain reference
    trace_id: "trace-2026-03-01-b8e4d"         # Observability trace reference
    timestamp: "2026-03-01T14:22:06.234Z"       # ISO 8601 with milliseconds
    message_type: "delegation_request"          # See 2.2 for types
    protocol_version: "1.0"                     # Schema version

  # Sender identity (mandatory)
  sender:
    agent_id: "agent:onboarding-orchestrator-prod-01"
    nhi_identity: "nhi:onboarding-orchestrator-prod-01"
    auth_token_ref: "jwt:tok-2026-03-01-xyz"   # Reference to auth token

  # Recipient identity (mandatory)
  recipient:
    agent_id: "agent:kyc-agent-prod-01"
    nhi_identity: "nhi:kyc-agent-prod-01"

  # Payload (schema depends on message_type)
  payload:
    task_description: "Verify customer identity"
    task_type: "identity_verification"
    inputs:
      document_type: "passport"
      document_country: "NL"
      customer_reference: "cust:hash:9f8a2b"
    expected_output_schema: "verification_result_v2"
    timeout_ms: 30000
    priority: "normal"

  # Permissions context (mandatory for delegation requests)
  permissions:
    granted_permissions:
      - "read:customer_documents"
      - "invoke:identity_verification_service"
    permission_expiry: "2026-03-01T14:52:06.234Z"  # 30 min from now
    scope: "task_scoped"
```

### 2.2 Message Types

| Message Type | Direction | Purpose |
|-------------|-----------|---------|
| `delegation_request` | Orchestrator to Sub-agent | Assign a task with inputs and permissions |
| `delegation_response` | Sub-agent to Orchestrator | Return task results |
| `capability_query` | Any agent to any agent | Ask what capabilities an agent offers |
| `capability_response` | Any agent to any agent | Respond with available capabilities |
| `permission_request` | Sub-agent to Orchestrator | Request elevated permissions for current task |
| `permission_response` | Orchestrator to Sub-agent | Grant or deny permission request |
| `status_update` | Sub-agent to Orchestrator | Report progress on a long-running task |
| `cancellation` | Orchestrator to Sub-agent | Cancel a delegated task |
| `error_report` | Any agent to any agent | Report an error condition |
| `heartbeat` | Any agent to any agent | Confirm liveness during long tasks |

---

## 3. Capability Negotiation

### 3.1 Capability Discovery

Before delegating a task, an orchestrator agent must verify that the target sub-agent has the required capabilities. This is analogous to API contract verification.

```
Orchestrator needs to delegate "verify identity"
  |
  v
Orchestrator sends capability_query to KYC Agent:
  { required_capabilities: ["identity_verification", "document_validation"] }
  |
  v
KYC Agent responds with capability_response:
  {
    available_capabilities: [
      { name: "identity_verification", version: "2.1", status: "available" },
      { name: "document_validation", version: "1.3", status: "available" },
      { name: "liveness_check", version: "1.0", status: "available" }
    ],
    current_load: "normal",
    estimated_response_time_ms: 5000
  }
  |
  v
Orchestrator validates: all required capabilities available?
  +-- YES --> Proceed with delegation
  +-- NO  --> Select alternative agent or escalate to human
```

### 3.2 Capability Registry

Each agent publishes a capability manifest that other agents can query:

| Field | Description | Example |
|-------|-------------|---------|
| `capability_name` | Machine-readable name | `identity_verification` |
| `capability_version` | Semantic version | `2.1.0` |
| `input_schema` | Expected input format | JSON Schema reference |
| `output_schema` | Guaranteed output format | JSON Schema reference |
| `max_concurrent_tasks` | Capacity limit | `50` |
| `avg_response_time_ms` | Typical response time | `4500` |
| `risk_classification` | Risk level of this capability | `high` |
| `required_permissions` | Permissions the caller must grant | `["read:customer_documents"]` |

---

## 4. Trust Boundaries Between Agents

### 4.1 Trust Boundary Definition

A trust boundary separates agents that operate in different security, data, or compliance domains. Communication across a trust boundary requires additional validation.

| Trust Domain | Agents | Data Classification | Boundary Controls |
|-------------|--------|--------------------|--------------------|
| **Customer Data Domain** | KYC Agent, Onboarding Orchestrator | PII, financial data | Full mTLS, field-level encryption, data minimization |
| **Financial Operations Domain** | Payments Agent, Treasury Agent | Transaction data, account data | mTLS, transaction signing, amount validation |
| **Analytics Domain** | Cash Flow Agent, Insights Agent | Aggregated data, anonymized | Standard TLS, aggregation validation |
| **Compliance Domain** | Compliance Agent, SAR Agent | Regulatory data, investigation data | mTLS, strict access control, no data sharing outside domain |

### 4.2 Cross-Boundary Communication Rules

| Rule | Description |
|------|-------------|
| **Data minimization** | Only the data strictly necessary for the delegated task crosses the boundary |
| **Field-level control** | PII fields are masked or encrypted when crossing boundaries unless explicitly required |
| **Audit logging** | Every cross-boundary message is logged with full payload hash for integrity verification |
| **Schema enforcement** | Cross-boundary messages are validated against strict schemas; no ad-hoc fields allowed |
| **Timeout enforcement** | Cross-boundary tasks have stricter timeouts (50% of same-domain timeouts) |
| **Fallback isolation** | Failure in one domain must not cascade to another domain's agents |

---

## 5. Data Isolation Between Agent Contexts

### 5.1 Context Isolation Principles

| Principle | Implementation |
|-----------|---------------|
| **Session isolation** | Each agent invocation operates in an isolated memory context; no shared state between invocations |
| **Customer isolation** | Agent processing Customer A's data cannot access Customer B's data, even within the same agent instance |
| **Task isolation** | Data received for Task 1 is not available when processing Task 2, even for the same customer |
| **Conversation isolation** | Sub-agents do not receive the full conversation history; only task-relevant context is passed |
| **Output isolation** | Sub-agent outputs are validated by the orchestrator before being incorporated into the main context |

### 5.2 Context Leakage Prevention

| Leakage Vector | Prevention |
|---------------|------------|
| Shared memory between agent instances | Container-level isolation; each invocation in a fresh container |
| LLM context window contamination | Clear context between tasks; do not carry sub-agent prompts in orchestrator context |
| Log contamination | Structured logging with agent_id tagging; no cross-agent log aggregation without anonymization |
| Cache poisoning | Agent-scoped caches; no shared cache between agents processing different customers |
| Tool state leakage | Stateless tool invocations; tool does not retain state between calls |

---

## 6. Shared State Governance

### 6.1 When Shared State Is Required

Some multi-agent workflows require shared state -- for example, an onboarding workflow where KYC results must be available to the Risk Scoring Agent. Shared state is permitted only under strict governance.

| Shared State Type | Governance Requirement | Example |
|-------------------|----------------------|---------|
| **Workflow state** | Managed by orchestrator; sub-agents read only | Onboarding status: `{kyc: completed, risk: pending, compliance: pending}` |
| **Intermediate results** | Stored in a governed data store with access control per agent | KYC verification result stored for Risk Agent to read |
| **Customer context** | Minimal subset, explicitly defined per workflow | Customer risk tier shared between agents processing the same application |

### 6.2 Shared State Rules

1. Shared state is **read-only** for sub-agents. Only the orchestrator or the producing agent can write.
2. Shared state access is **logged** with agent identity and timestamp.
3. Shared state is **scoped** to a single chain_id. It is not accessible across different workflows.
4. Shared state is **purged** when the chain completes or times out.
5. Shared state **never contains raw PII**. Use pseudonymized references with lookup only when needed.

---

## 7. Agent-to-Agent Permission Requests

### 7.1 Permission Request Protocol

When a sub-agent determines it needs permissions beyond what was granted in the delegation, it must request them through a formal protocol.

```
Sub-agent needs permission not in its current task scope
  |
  v
Sub-agent sends permission_request to orchestrator:
  {
    requested_permission: "read:credit_bureau_data",
    reason: "Risk assessment requires credit history not in initial delegation",
    task_context: "Customer risk score cannot be computed without credit data",
    urgency: "normal"
  }
  |
  v
Orchestrator evaluates:
  |
  +-- Does orchestrator have this permission? --> NO: Deny; escalate to human
  |
  +-- YES: Is this permission appropriate for the task?
       |
       +-- YES: Grant with time-bound scope
       |    Log: permission_request_granted
       |    Notify: Model Owner (for audit)
       |
       +-- NO: Deny with explanation
            Log: permission_request_denied
            Reason: "Credit data access not justified for document-only KYC task"
```

### 7.2 Permission Request Governance

| Rule | Description |
|------|-------------|
| **Rate limiting** | Max 3 permission requests per delegation task; more indicates scope problem |
| **Audit trail** | Every permission request and response is logged in the delegation chain audit |
| **Human notification** | Permission grants for high-risk resources trigger human notification |
| **Automatic review** | Repeated permission requests for the same resource trigger architecture review |
| **Denial escalation** | If denied permission blocks task completion, escalate to human with context |

---

## 8. AutoGen-Compatible Patterns

### 8.1 AutoGen Group Chat Governance

For teams using Microsoft AutoGen or similar multi-agent frameworks, the following governance overlays apply:

| AutoGen Pattern | Governance Overlay |
|----------------|-------------------|
| **Group chat** | All messages in group chat must follow the inter-agent message schema; free-text inter-agent messaging is prohibited |
| **Agent selection** | Agent selection logic must be deterministic or governed by policy; random selection is not permitted for regulated workflows |
| **Function calling** | All function calls must pass through the Policy Layer (see [agent-permission-boundaries.md](agent-permission-boundaries.md)) |
| **Conversation history** | Group chat history must not contain PII from previous customer sessions; implement session-scoped history |
| **Termination conditions** | Define explicit termination conditions; prevent infinite agent conversation loops |
| **Human proxy** | Human-in-the-loop must be implemented via a formal HITL queue, not ad-hoc human proxy agents |

### 8.2 Framework-Agnostic Protocol Requirements

Regardless of the multi-agent framework used (AutoGen, CrewAI, LangGraph, custom), all inter-agent communication must satisfy:

1. Structured message format (no free-text between agents)
2. NHI-based authentication on every message
3. Permission validation before processing
4. Input and output schema validation
5. Full audit logging of every inter-agent interaction
6. Data isolation between agent contexts
7. Chain depth enforcement
8. Timeout and circuit breaker on every inter-agent call

---

## Cross-References

- **Agent Permission Boundaries:** [agent-permission-boundaries.md](agent-permission-boundaries.md) -- NHI identity management, Agentic Tool Sovereignty layers
- **Delegation Chain Audit:** [delegation-chain-audit.md](delegation-chain-audit.md) -- audit log schema for delegation events
- **Multi-Agent Governance Framework:** [multi-agent-governance-framework.md](multi-agent-governance-framework.md) -- delegation rules, communication standards
- **Human-in-the-Loop Patterns:** [human-in-the-loop-patterns.md](human-in-the-loop-patterns.md) -- escalation paths when inter-agent communication fails
- **Agent Fleet Operations:** [agent-fleet-operations.md](agent-fleet-operations.md) -- agent registry and fleet-wide monitoring
- **Customer-Facing Agent Safety:** [customer-facing-agent-safety.md](customer-facing-agent-safety.md) -- session context safety and data isolation
- **Safety Policy Definition:** [../templates/safety-policy-definition.md](../templates/safety-policy-definition.md) -- policy templates for inter-agent data handling

---

*Last updated: 2026-03-01*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
