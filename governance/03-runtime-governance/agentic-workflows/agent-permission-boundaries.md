# Agent Permission Boundaries

## Purpose

This document defines how to establish, enforce, and audit the permission boundaries for customer-facing AI agents and autonomous decision-makers. It introduces the **Agentic Tool Sovereignty** model -- a three-layer architecture for governing what tools an agent can discover, select, and execute -- and the **Machine Identity / Non-Human Identity (NHI)** model for treating agents as first-class identity citizens in your IAM infrastructure.

Every AI agent operates within a permission boundary: the complete set of actions it is authorized to perform, data it can access, and tools it can invoke. Without explicit, enforced boundaries, agents become uncontrolled software actors with implicit access to everything their runtime environment provides.

## When to Use

- When designing a new AI agent before it enters development
- When deploying an agent to production (defining its runtime permission scope)
- When adding new tools or capabilities to an existing agent
- When auditing agent permissions as part of periodic revalidation
- When investigating a security incident involving agent actions
- When an agent needs to escalate permissions (dynamic permission elevation)

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **Model Owner** | **Accountable** -- defines the agent's permission boundary; approves changes |
| **Security Engineer** | **Responsible** -- implements NHI credentials, configures IAM policies, manages credential rotation |
| **MLOps / Platform Engineer** | **Responsible** -- implements the tool sovereignty layers, sandboxing, and rate limiting |
| **AI/ML Engineer** | **Responsible** -- configures tool registrations, capability manifests, and policy rules |
| **Compliance Officer (2nd Line)** | **Reviewer** -- validates that permission boundaries meet regulatory requirements |
| **AI Governance Committee** | **Approver** -- approves permission boundaries for high-risk agents |

## Regulatory Basis

- **EU AI Act Article 9** -- Risk management must address risks arising from the AI system's interaction with other systems
- **EU AI Act Article 14** -- Human oversight measures, including ability to interrupt or override
- **EU AI Act Article 15** -- Accuracy, robustness, and cybersecurity requirements for high-risk AI
- **DORA Article 9** -- ICT risk management framework, including access management and identity controls
- **SAFEST items A-06** (human-in-the-loop), **A-07** (override capabilities), **A-09** (kill switch), **S-08** (access controls), **S-09** (data protection)
- **GDPR Article 25** -- Data protection by design and by default (data minimization for agent access)

---

## 1. Machine Identity / Non-Human Identity (NHI)

AI agents are autonomous software actors that authenticate to APIs, access databases, invoke tools, and make decisions. They require identity management equivalent to human users -- not shared service accounts or hardcoded API keys.

### 1.1 Agents as First-Class IAM Citizens

| Principle | What It Means for Agents | Implementation |
|-----------|-------------------------|----------------|
| **Unique Identity** | Every agent instance has a unique, distinguishable identity | Assign each agent a unique NHI identifier in your IAM system (e.g., `agent:onboarding-agent-prod-01`) |
| **Authentication** | Agents prove their identity before accessing any resource | Use short-lived tokens (OAuth 2.0 client credentials, workload identity federation), not long-lived API keys |
| **Authorization** | Agents are granted only the permissions required for their specific role | Define agent-specific IAM roles with granular permission scopes |
| **Least Privilege** | Agents receive the minimum permissions necessary for their current task | Scope permissions to specific resources, actions, and time windows |
| **Audit Trail** | Every action taken by an agent is logged with its NHI identity | All API calls, tool invocations, and data accesses are attributable to a specific agent identity |
| **Credential Rotation** | Agent credentials are rotated automatically on a defined schedule | Rotate tokens every 24 hours for production agents; every 1 hour for high-risk agents |

### 1.2 NHI Credential Management

| Credential Type | Use Case | Rotation Policy | Storage |
|----------------|----------|-----------------|---------|
| **OAuth 2.0 Client Credentials** | API-to-API authentication for tool calls | Token lifetime <= 1 hour; client secret rotation every 90 days | Secrets vault (HashiCorp Vault, AWS Secrets Manager, Azure Key Vault) |
| **Workload Identity Tokens** | Cloud-native service authentication | Auto-rotated by platform (e.g., GCP Workload Identity, AWS IAM Roles) | Managed by cloud provider |
| **Signed JWTs** | Inter-service communication within agent orchestration | Token lifetime <= 15 minutes | Generated at runtime; signing keys rotated every 30 days |
| **Database Credentials** | Direct database access (when necessary) | Rotation every 24 hours via vault dynamic secrets | Secrets vault with dynamic credential generation |

**Hard rule:** No agent may use hardcoded credentials, shared service accounts, or long-lived API keys. Any discovery of such credentials in an agent configuration triggers an immediate security incident.

### 1.3 SPIFFE Workload Identity

For enhanced security in multi-tenant and high-risk deployments, agents should use SPIFFE (Secure Production Identity Framework For Everyone) workload identities. SPIFFE provides short-lived, automatically rotated identities that are cryptographically verifiable.

**SPIFFE Identity Format:**
```
spiffe://[trust-domain]/agent/[agent-id]/[environment]/[instance]

Example:
spiffe://fintech-corp.io/agent/payments-agent/prod/01
```

**SPIFFE Benefits for Agent Governance:**

| Feature | Benefit | Implementation |
|---------|---------|----------------|
| **Short-Lived Credentials** | Reduced blast radius if compromised | 15-minute TTL for high-risk agents (reduced from 1 hour) |
| **Automatic Rotation** | No manual credential management | SPIRE agent handles rotation |
| **Cryptographic Identity** | Verifiable proof of identity | X.509 SVIDs with embedded SPIFFE ID |
| **Delegation Chain** | Propagate identity through agent chains | Each delegation carries full identity chain |
| **Multi-Tenant Isolation** | Tenant-scoped trust domains | `spiffe://tenant-a.fintech.io/...` vs `spiffe://tenant-b.fintech.io/...` |

**TTL Policy by Risk Tier:**

| Risk Tier | TTL | Rationale |
|-----------|-----|-----------|
| High-Risk | 15 minutes | Minimize exposure window for financial/customer-impact agents |
| Limited-Risk | 1 hour | Balance security with operational overhead |
| Minimal-Risk | 4 hours | Reduced rotation for low-impact internal tools |

**Cross-Reference:** [SPIFFE Agent Identity Guide](../guides/spiffe-agent-identity.md)

### 1.4 NHI Lifecycle

```
  +------------------+     +------------------+     +------------------+
  | 1. PROVISION     |     | 2. ACTIVATE      |     | 3. OPERATE       |
  |                  | --> |                  | --> |                  |
  | Create NHI in    |     | Assign roles and |     | Agent runs with  |
  | IAM system.      |     | permissions.     |     | scoped creds.    |
  | Generate initial |     | Configure vault  |     | All actions      |
  | credentials.     |     | access. Enable   |     | logged under     |
  | Register in      |     | audit logging.   |     | NHI identity.    |
  | agent registry.  |     | Deploy to env.   |     | Creds rotated    |
  |                  |     |                  |     | automatically.   |
  +------------------+     +------------------+     +------------------+
           |                                                 |
           |                                                 v
  +------------------+     +------------------+     +------------------+
  | 6. DECOMMISSION  |     | 5. REVOKE        |     | 4. REVIEW        |
  |                  | <-- |                  | <-- |                  |
  | Archive audit    |     | Revoke all creds |     | Periodic review  |
  | logs. Remove     |     | and tokens.      |     | of permissions   |
  | NHI from active  |     | Disable IAM      |     | (quarterly or    |
  | registry. Retain |     | roles. Block     |     | after incidents).|
  | records per      |     | all access.      |     | Verify least     |
  | retention policy.|     |                  |     | privilege.       |
  +------------------+     +------------------+     +------------------+
```

---

## 2. Per-Skill RBAC

In addition to agent-level permissions, modern agentic systems implement **per-skill RBAC** -- granular permission control at the skill level. A skill is a discrete capability within an agent (e.g., "process_payment" or "verify_identity"), each with its own permission matrix, budget constraints, and safety configuration.

### 2.1 Skill-Level Permission Matrix

Each skill has its own permission boundary that is more granular than the agent-level boundary:

```yaml
skill_id: "skill:payments-agent:process-payment:v1.0.0"
parent_agent: "agent:payments-agent-prod-01"

permission_matrix:
  allowed_actions:
    - action: "initiate_payment"
      resource_type: "payment_transaction"
      scope: "own_tenant_only"
      max_amount: 10000  # EUR
      conditions:
        - "customer_authenticated"
        - "sufficient_funds_verified"
    
    - action: "check_payment_status"
      resource_type: "payment_transaction"
      scope: "own_tenant_only"
      # No conditions for read-only access
  
  denied_actions:
    - action: "modify_payment_rails"
      reason: "Infrastructure changes require human approval"
    - action: "delete_transaction_history"
      reason: "Audit trail must be immutable"
  
  delegation:
    can_delegate: false  # This skill cannot delegate to other agents
```

### 2.2 Skill Permission Inheritance

Skill permissions are constrained by the parent agent's permission boundary:

```
Agent Permission Boundary (Outer Boundary)
    │
    ├── Skill A Permission Matrix (Subset of Agent)
    │       └── Can only use actions allowed by Agent
    │
    └── Skill B Permission Matrix (Subset of Agent)
            └── Can only use actions allowed by Agent
```

**Key Principle:** A skill cannot have permissions that exceed its parent agent's permission boundary.

### 2.3 Runtime Permission Enforcement

At runtime, the governance enforcement pipeline checks permissions at both levels:

1. **Agent-Level Check:** Does the agent have permission to execute this skill?
2. **Skill-Level Check:** Does the skill have permission to perform this action?

Both must pass for execution to proceed.

**Cross-Reference:** [Skill Manifest](../templates/skill-manifest.yaml), [Governance Enforcement Pipeline](governance-enforcement-pipeline.md)

---

## 3. Agentic Tool Sovereignty -- Three-Layer Model

Agentic Tool Sovereignty governs the complete lifecycle of agent-tool interaction through three distinct layers. Each layer enforces a different aspect of control.

### 3.1 Configuration Layer: Tool Discovery and Registration

The Configuration Layer governs **which tools exist in the agent's universe** and what each tool can do.

| Component | Description | Governance Requirement |
|-----------|-------------|----------------------|
| **Tool Registry** | Central catalog of all tools available to agents | Every tool must be registered before any agent can invoke it. Unregistered tools are blocked at the Network Layer. |
| **Capability Manifest** | Machine-readable description of each tool's inputs, outputs, side effects, and risk classification | Every registered tool has a manifest. Manifests are versioned and reviewed. |
| **Tool Risk Classification** | Each tool is classified by its potential impact: read-only, state-modifying, financial, PII-accessing, external-calling | Risk classification determines which Policy Layer rules apply. |
| **Tool Versioning** | Tools are versioned; agents are pinned to specific tool versions | Prevent unexpected behavior changes. New tool versions require re-evaluation before agent access. |

**Capability Manifest Template:**

```yaml
tool_id: "payment-initiate-v2"
tool_name: "Initiate Payment"
version: "2.1.0"
risk_classification: "financial"  # read-only | state-modifying | financial | pii-accessing | external
description: "Initiates a payment transfer between accounts"
inputs:
  - name: "source_account"
    type: "string"
    required: true
    sensitive: true
  - name: "destination_account"
    type: "string"
    required: true
    sensitive: true
  - name: "amount"
    type: "decimal"
    required: true
    constraints:
      max_value: 50000  # EUR; above this requires human approval
  - name: "currency"
    type: "string"
    required: true
    allowed_values: ["EUR", "USD", "GBP"]
outputs:
  - name: "transaction_id"
    type: "string"
  - name: "status"
    type: "enum"
    values: ["pending", "completed", "failed"]
side_effects:
  - "Moves funds between accounts"
  - "Creates transaction record in ledger"
requires_human_approval_above:
  amount: 50000
rate_limit: "10 calls per minute per agent"
```

### 2.2 Policy Layer: Context-Based Tool Selection

The Policy Layer governs **which tools an agent is allowed to select** given its identity, the user's context, and the current interaction state.

| Policy Type | What It Controls | Example |
|-------------|-----------------|---------|
| **Role-Based Access** | Which tools are available to which agent roles | Customer service agent: read-only tools + limited state-modifying tools. Trading agent: read + trade execution tools. |
| **Context-Based Restrictions** | Tool availability based on interaction context | Payment tool only available after customer identity is verified. Loan approval tool only available during business hours. |
| **Value-Based Escalation** | Automatic human escalation when parameters exceed thresholds | Payment > EUR 10,000 requires HITL approval. Account closure requires HITL regardless of amount. |
| **Temporal Policies** | Time-based restrictions on tool availability | Trading tools disabled outside market hours. Batch processing tools only available during maintenance windows. |
| **Geographic Policies** | Location-based restrictions | Cross-border payment tools restricted based on sanctioned jurisdictions. |
| **Sequential Policies** | Tool X can only be invoked after tool Y | Credit check must precede loan offer. Identity verification must precede account access. |

**Policy Definition Example:**

```yaml
policy_id: "payment-agent-policy-v3"
agent_role: "payment-processing-agent"
tool_permissions:
  - tool_id: "account-balance-read"
    permission: "allow"
    conditions: []
  - tool_id: "payment-initiate-v2"
    permission: "conditional"
    conditions:
      - type: "value_threshold"
        parameter: "amount"
        threshold: 10000
        action: "require_human_approval"
      - type: "prerequisite"
        required_tool: "customer-identity-verify"
        required_status: "verified"
      - type: "rate_limit"
        max_calls: 50
        window: "1 hour"
  - tool_id: "account-close"
    permission: "deny"  # This agent cannot close accounts
escalation_rules:
  - trigger: "tool_denied"
    action: "escalate_to_human"
    message: "This action requires a human operator."
```

### 2.3 Network Layer: Execution Sandboxing and Rate Limiting

The Network Layer governs **how tool calls are executed** at the infrastructure level, regardless of what the agent or Policy Layer decided.

| Control | What It Does | Implementation |
|---------|-------------|----------------|
| **Execution Sandboxing** | Each tool call executes in an isolated environment with no access to other tools' data or state | Container-based isolation; separate network namespaces per tool call |
| **Rate Limiting** | Limits the number and frequency of tool calls per agent per time window | API gateway rate limiting at the NHI identity level |
| **Blast Radius Containment** | Limits the maximum impact of a single tool call or a series of tool calls | Transaction amount caps, row-level data access limits, time-bounded operations |
| **Timeout Enforcement** | Hard timeout on all tool calls to prevent hanging operations | Tool-specific timeouts (e.g., 5 seconds for reads, 30 seconds for writes) |
| **Circuit Breaker** | Automatically disables a tool if its error rate exceeds a threshold | If tool failure rate > 50% in a 5-minute window, disable for 10 minutes and alert |
| **Network Segmentation** | Agent tool calls are routed through a controlled network path with logging | All tool traffic through an API gateway with full request/response logging |
| **Egress Control** | Agents cannot make arbitrary outbound network calls | Whitelist of allowed external endpoints per agent role |

```
  Agent Reasoning
       |
       v
  +-------------------+
  | POLICY LAYER      |  "Is this tool allowed for this agent in this context?"
  | Check permissions |
  | Apply conditions  |
  +-------------------+
       |
       v (if allowed)
  +-------------------+
  | NETWORK LAYER     |  "Execute safely with containment"
  | Rate limit check  |
  | Sandbox creation  |
  | Timeout enforcement|
  | Audit logging     |
  +-------------------+
       |
       v
  +-------------------+
  | TOOL EXECUTION    |  Isolated, monitored, time-bounded
  +-------------------+
       |
       v
  +-------------------+
  | RESPONSE HANDLING |  Validate output, log result, return to agent
  +-------------------+
```

---

## 3. Permission Boundary Definition Framework

### 3.1 Steps to Define an Agent's Permission Boundary

1. **Identify the agent's purpose.** What tasks must this agent accomplish? What user problems does it solve?

2. **List all required capabilities.** For each task, what data access, tool invocations, and actions are necessary?

3. **Apply least privilege.** For each capability, grant the minimum permission scope. Read-only where possible. Specific resources, not wildcards. Time-bounded where applicable.

4. **Classify each permission by risk.** Use the tool risk classification from the Configuration Layer.

5. **Define escalation triggers.** For which actions or parameter values must the agent escalate to a human?

6. **Document the boundary.** Use the Permission Boundary Template (Section 3.2).

7. **Review and approve.** 1st line review for minimal/limited-risk agents. AI Governance Committee approval for high-risk agents.

8. **Enforce at all three layers.** Configure the Configuration Layer (tool registry), Policy Layer (access rules), and Network Layer (sandboxing, rate limits).

9. **Audit periodically.** Review permission boundaries quarterly. Revoke unused permissions. Verify least privilege.

### 3.2 Permission Boundary Template

```yaml
boundary_id: "PB-[AGENT-ID]-[VERSION]"
agent_id: "[AGENT-ID]"
agent_name: "[FILL IN: Human-readable agent name]"
agent_purpose: "[FILL IN: One-sentence description of what this agent does]"
risk_tier: "[minimal | limited | high]"
oversight_model: "[HITL | HOTL | HOTA]"  # See human-in-the-loop-patterns.md
nhi_identity: "[FILL IN: Agent's NHI identifier in IAM]"

data_permissions:
  - resource: "[FILL IN: Data resource name]"
    access_level: "[read | write | read-write]"
    scope: "[FILL IN: Specific scope, e.g., 'own customer records only']"
    pii_access: "[true | false]"
    retention: "[FILL IN: How long agent can hold data in memory]"

tool_permissions:
  - tool_id: "[FILL IN: Tool identifier from registry]"
    permission: "[allow | conditional | deny]"
    conditions: "[FILL IN: Conditions for conditional access]"
    max_calls_per_hour: "[FILL IN: Rate limit]"
    requires_human_approval: "[true | false]"
    approval_threshold: "[FILL IN: Value above which human approval required]"

action_permissions:
  - action: "[FILL IN: Action the agent can take]"
    scope: "[FILL IN: Constraints on the action]"
    reversible: "[true | false]"
    max_impact: "[FILL IN: Maximum impact of this action, e.g., 'EUR 10,000']"

prohibited_actions:
  - "[FILL IN: Actions this agent must never take]"

escalation_triggers:
  - trigger: "[FILL IN: Condition that triggers escalation]"
    action: "[escalate_to_human | block_and_notify | log_and_continue]"
    response_time: "[FILL IN: Required response time for escalation]"

review_schedule:
  frequency: "[quarterly | monthly | after-each-incident]"
  reviewer: "[FILL IN: Role responsible for review]"
  last_reviewed: "[FILL IN: Date]"
  next_review: "[FILL IN: Date]"
```

---

## 4. Dynamic Permission Escalation

Some agent tasks require temporary elevation of permissions beyond the agent's base boundary. This must be governed, not ad hoc.

### 4.1 Escalation Flow

```
  Agent encounters task requiring elevated permissions
       |
       v
  Agent requests escalation (logged with reason and context)
       |
       v
  +---------------------------+
  | APPROVAL WORKFLOW         |
  | - Sync (real-time):       |
  |   Human approves in-line  |
  |   (for HITL agents)       |
  | - Async (queued):         |
  |   Request queued for      |
  |   human review            |
  |   (for HOTL agents)       |
  +---------------------------+
       |
       v (if approved)
  Temporary elevated permissions granted
  - Time-bounded (max 15 minutes or single-task)
  - Fully logged (every action under elevated permissions)
  - Auto-revoke after task completion or timeout
       |
       v (if denied)
  Agent informs user that the action requires human assistance
  Escalation to human operator
```

### 4.2 Escalation Governance Rules

- Elevated permissions are always time-bounded. Maximum duration: 15 minutes or until the specific task completes, whichever comes first.
- Every action taken under elevated permissions is logged separately in the audit trail with an escalation reference ID.
- Elevated permissions cannot be self-approved by the agent. A human must approve.
- Repeated escalation requests for the same permission type may indicate the base permission boundary should be revised.

---

## 5. Tool-Use Permissions Matrix

Use this matrix to define and communicate agent-tool permissions across the organization.

| Tool | Customer Service Agent | Payment Agent | Onboarding Agent | Trading Agent | Compliance Agent |
|------|----------------------|---------------|-------------------|---------------|-----------------|
| Account Balance (read) | Allow | Allow | Allow | Allow | Allow |
| Transaction History (read) | Allow | Allow | Deny | Allow | Allow |
| Initiate Payment | Deny | Conditional (< EUR 10K) | Deny | Deny | Deny |
| Execute Trade | Deny | Deny | Deny | Conditional (< EUR 50K) | Deny |
| KYC Verification | Deny | Deny | Allow | Deny | Allow |
| Account Open | Deny | Deny | Allow | Deny | Deny |
| Account Close | Deny | Deny | Deny | Deny | Deny (human-only) |
| Credit Check | Deny | Deny | Conditional (with consent) | Deny | Allow |
| Customer PII (read) | Conditional (own session) | Conditional (own session) | Allow (during onboarding) | Deny | Allow |
| Suspicious Activity Report | Deny | Deny | Deny | Deny | Allow |

**Legend:**
- **Allow** = Agent can invoke without additional approval
- **Conditional** = Agent can invoke under specified conditions (value limits, prerequisites, time windows)
- **Deny** = Agent cannot invoke under any circumstances

---

## 6. Sandboxing and Isolation Patterns

### 6.1 Execution Isolation

| Pattern | When to Use | Implementation |
|---------|-------------|----------------|
| **Process Isolation** | Default for all tool calls | Each tool call executes in a separate process with its own memory space |
| **Container Isolation** | State-modifying and financial tool calls | Each tool call executes in a short-lived container with no persistent state |
| **Network Isolation** | External API calls | Tool calls to external services route through a dedicated network segment with egress filtering |
| **Data Isolation** | PII-accessing tools | Tool can only access data scoped to the current session; no cross-session data access |
| **Temporal Isolation** | All tool calls | Hard timeout on every tool call; circuit breaker on repeated failures |

### 6.2 Blast Radius Containment

Define maximum impact per agent interaction:

| Containment Dimension | Example Limit | Enforcement Point |
|-----------------------|--------------|-------------------|
| **Financial** | Max EUR 10,000 per interaction without human approval | Policy Layer + Network Layer |
| **Data Volume** | Max 100 records accessed per query | Database query limiter |
| **Records Modified** | Max 1 account modified per interaction | Tool execution guard |
| **External Calls** | Max 10 external API calls per interaction | API gateway counter |
| **Time** | Max 5 minutes total tool execution time per interaction | Network Layer timeout |

---

## 7. FinTech Permission Boundary Examples

### 7.1 Payment Agent Boundaries

**Purpose:** Processes customer payment requests, verifies accounts, initiates transfers.

**Key boundaries:**
- Can read account balances and transaction history for the authenticated customer only
- Can initiate payments up to EUR 10,000 without human approval
- Payments EUR 10,000-50,000 require HITL approval (see [Human-in-the-Loop Patterns](human-in-the-loop-patterns.md))
- Payments above EUR 50,000 are blocked; the agent escalates to a human operator
- Cannot close accounts, modify account settings, or access other customers' data
- Cross-border payments require additional jurisdiction check via policy layer
- All payment tool calls are logged with full request/response audit trail

### 7.2 Trading Agent Boundaries

**Purpose:** Executes trades on behalf of customers within pre-defined parameters.

**Key boundaries:**
- Can execute trades within customer-defined limits (e.g., max position size, allowed instruments)
- Exceeding customer-defined limits requires customer re-confirmation (real-time HITL)
- Market orders above EUR 50,000 require human trader review
- Cannot modify customer risk profiles or trading permissions
- Trading tools disabled outside market hours (temporal policy)
- Circuit breaker: if > 3 consecutive trade failures, disable trading tools and escalate
- All trades logged with reasoning trace for regulatory reporting

### 7.3 Customer Data Access Agent

**Purpose:** Retrieves and presents customer information during service interactions.

**Key boundaries:**
- Can access customer data only for the customer currently authenticated in the session
- PII data displayed to the customer is partially masked in logs (data isolation)
- Cannot export, download, or transmit customer data to external systems
- Session-scoped data access: all in-memory customer data is purged when the session ends
- Data access logged per field, per access, attributable to the agent's NHI identity

---

## Cross-References

- **Human-in-the-Loop Patterns:** [human-in-the-loop-patterns.md](human-in-the-loop-patterns.md) -- oversight models that permission boundaries interact with (HITL/HOTL/HOTA)
- **Customer-Facing Agent Safety:** [customer-facing-agent-safety.md](customer-facing-agent-safety.md) -- safety patterns that complement permission boundaries
- **Agent Performance Evaluations:** [../evaluations/agent-performance-evals.md](../evaluations/agent-performance-evals.md) -- metrics for evaluating permission boundary adherence
- **Safety Policy Definition Template:** [../templates/safety-policy-definition.md](../templates/safety-policy-definition.md) -- template for encoding permission policies
- **Continuous Online Evaluation:** [../evaluations/continuous-online-evaluation.md](../evaluations/continuous-online-evaluation.md) -- monitoring for permission boundary violations
- **Eval-Driven Development:** [../../02-development-governance/evaluations/eval-driven-development.md](../../02-development-governance/evaluations/eval-driven-development.md) -- eval suites for testing permission boundaries pre-deployment
- **Three Lines of Defense:** [../../07-enterprise-implementation/organizational-model/three-lines-of-defense-for-ai.md](../../07-enterprise-implementation/organizational-model/three-lines-of-defense-for-ai.md) -- organizational model for permission governance
- **Risk Tiering Model:** [../../07-enterprise-implementation/risk-based-adoption/risk-tiering-model.md](../../07-enterprise-implementation/risk-based-adoption/risk-tiering-model.md) -- risk tier determines permission review rigor
- **Glossary:** [../../05-cross-cutting/glossary.md](../../05-cross-cutting/glossary.md) -- definitions for permission boundary, NHI, tool use, delegation chain

---

*Last updated: 2026-02-28*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
