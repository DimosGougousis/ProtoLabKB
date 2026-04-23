# Fallback Procedure Template

## Purpose

This template defines the fallback and graceful degradation procedure for an AI agent. Fallback procedures ensure that when an agent cannot operate normally -- due to model failure, tool unavailability, safety threshold breach, or infrastructure outage -- it degrades through a series of controlled levels rather than failing silently, producing unsafe outputs, or leaving the customer stranded.

This template implements SAFEST item S-13 (fallback procedures) and aligns with the degradation hierarchy defined in [Customer-Facing Agent Safety](../agentic-workflows/customer-facing-agent-safety.md) Section 6 and [Multi-Agent Governance Framework](../agentic-workflows/multi-agent-governance-framework.md) Section 8.1. The Agent Fleet Command Dashboard monitors each agent's current degradation level and displays it alongside the health state.

## When to Use

- When deploying a new agent to production (fallback procedure is a pre-deployment gate requirement)
- When an agent's infrastructure, model, or tool dependencies change
- When a safety incident reveals gaps in the existing fallback procedure
- When conducting fallback testing (required quarterly for high-risk agents)
- When reviewing agent resilience as part of DORA compliance

## Who Is Responsible

| Role | R/A/C/I | Responsibility |
|------|---------|---------------|
| **Model Owner** | Accountable | Owns the fallback procedure; approves trigger conditions and customer communication |
| **AI/ML Engineer** | Responsible | Implements automated fallback transitions and recovery detection |
| **MLOps / Platform Engineer** | Responsible | Implements infrastructure-level fallback (circuit breakers, failover, static pages) |
| **Product Manager** | Consulted | Defines customer experience at each degradation level; approves communication templates |
| **Customer Operations Lead** | Consulted | Staffs manual fallback capacity; defines handoff procedures |
| **Compliance Officer (2nd Line)** | Reviewer | Validates regulatory compliance at each degradation level |
| **On-Call Engineer** | Responsible | Executes manual escalation actions during incidents; monitors recovery |

## Regulatory Basis

- **EU AI Act Article 14** -- Human oversight measures including ability to interrupt AI system operation
- **EU AI Act Article 15** -- Accuracy and robustness; systems must fail gracefully
- **DORA Article 11** -- ICT-related incident management and business continuity
- **DORA Article 12** -- ICT business continuity policy, including fallback arrangements
- **SAFEST S-13** -- Fallback procedures for AI systems
- **SAFEST A-07** -- Override capability for AI system decisions
- **SAFEST A-09** -- Kill switch mechanisms for AI systems
- **DNB Good Practice** -- Business continuity and operational resilience for automated systems

---

## Fallback Procedure Document

### 1. Procedure Metadata

| Field | Value |
|-------|-------|
| **Procedure ID** | `FB-[AGENT_PREFIX]-v[version]` (e.g., FB-PAYMENTS-v2.3) |
| **Agent** | `<agent_name>` (`<agent_id>`) |
| **Procedure Version** | `<semver>` |
| **Effective Date** | `<YYYY-MM-DD>` |
| **Last Tested Date** | `<YYYY-MM-DD>` |
| **Next Test Date** | `<YYYY-MM-DD>` |
| **Procedure Owner** | `<Name, Role>` (Model Owner) |
| **Approved By** | `<Name, Role>` |

---

### 2. Five Degradation Levels

```
Level 0: NORMAL
  Agent operates at full capability with full autonomy
  All tools, models, and services available
  Health state: HEALTHY
       |
       v (trigger condition met)
Level 1: REDUCED
  Agent operates with reduced autonomy or limited capabilities
  Some non-critical tools may be unavailable
  Health state: DEGRADED
       |
       v (further degradation)
Level 2: ASSISTED
  Agent operates only with human co-pilot assistance
  All consequential actions require human approval
  Health state: DEGRADED
       |
       v (further degradation)
Level 3: MANUAL
  Agent is suspended; human agents handle all interactions
  Agent provides context and suggestions to human agents (not to customers)
  Health state: CRITICAL
       |
       v (complete system failure)
Level 4: EMERGENCY
  All AI systems offline; static fallback content displayed
  IVR / static web page / emergency contact information
  Health state: CRITICAL
```

---

## 3. Circuit Breaker Integration

The fallback procedure integrates with the circuit breaker and kill switch systems for automated degradation triggers:

| Circuit State | Kill Switch Level | Fallback Level | Action |
|---------------|-------------------|----------------|--------|
| CLOSED | None | Level 0 | Normal operation |
| HALF_OPEN | THROTTLE | Level 1 | Reduced capacity with queue |
| OPEN | PAUSE | Level 2 | Stop new requests, complete in-flight |
| OPEN (extended) | FULL STOP | Level 3-4 | Terminate and activate manual fallback |

### 3.1 Automated Trigger Mapping

```
Circuit Breaker Metrics
         │
         ▼
┌─────────────────┐
│ Error Rate > 10%│──┐
│ Latency > 2x    │  │
│ Loop Detected   │  │
└─────────────────┘  │
         │           │
         ▼           │
┌─────────────────┐  │
│  THROTTLE (L1)  │  │
│  Capacity -50%  │  │
└─────────────────┘  │
         │           │
         ▼           │
┌─────────────────┐  │
│  PAUSE (L2)     │◄─┘
│  No new requests│
└─────────────────┘
         │
         ▼
┌─────────────────┐
│ FULL STOP (L3)  │
│ Terminate all   │
└─────────────────┘
```

### 3.2 MI9-to-Paper Mapping Table

| MI9 Level | Paper Concept | Kill Switch | Circuit State | Fallback Level | Customer Impact |
|-----------|---------------|-------------|---------------|----------------|-----------------|
| L0 | Normal Operation | None | CLOSED | Level 0 | Full service |
| L1 | Reduced Capacity | THROTTLE | HALF_OPEN | Level 1 | Slower service, queueing |
| L2 | Suspended | PAUSE | OPEN | Level 2 | New requests blocked |
| L3 | Terminated | FULL STOP | OPEN (extended) | Level 3 | Human handoff |
| L4 | Emergency | FULL STOP + Fallback | N/A | Level 4 | Static fallback page |

**Cross-Reference:** [Kill Switch Specification](kill-switch-specification.md), [Circuit Breaker Config](circuit-breaker-config.yaml)

---

## 4. Level Definitions and Trigger Conditions

#### Level 0: Normal

| Aspect | Specification |
|--------|--------------|
| **Description** | Agent is fully operational. All KPIs within SLA targets. All tools, model endpoints, and data sources are available and responsive. |
| **Oversight Model** | As configured in registry (HITL/HOTL/HOTA) |
| **Customer Experience** | Full self-service capability |
| **Trigger to Enter** | All systems operational; all health checks passing; no active alerts |
| **Trigger to Leave** | Any Level 1 trigger condition met |

#### Level 1: Reduced

| Aspect | Specification |
|--------|--------------|
| **Description** | Agent operates with reduced capability. One or more non-critical tools or features are unavailable, or a KPI has entered the warning zone. Agent can still resolve most customer requests but may not be able to perform certain actions. |
| **Trigger Conditions** | |
| - KPI warning threshold breached for > 5 minutes | |
| - Non-critical tool unavailable (e.g., product recommendation engine) | |
| - LLM latency P95 > warning threshold | |
| - Drift detected but performance still within acceptable range | |
| **Automated Responses** | |
| - Disable affected capabilities; route affected requests to alternative flow | |
| - Increase monitoring frequency to every 15 seconds | |
| - Log degradation event with timestamp and cause | |
| **Human Notification** | Alert Model Owner via Slack/email within 5 minutes |
| **Customer Communication** | No explicit notification unless customer encounters missing capability. If encountered: "This feature is temporarily unavailable. I can help you with [alternative], or I can connect you with a team member." |
| **Recovery Condition** | All trigger conditions resolved for > 15 minutes; auto-transition to Level 0 |

#### Level 2: Assisted

| Aspect | Specification |
|--------|--------------|
| **Description** | Agent requires human assistance for all consequential actions. The agent continues to interact with customers but cannot execute transactions, modify accounts, or provide financial information without human review and approval. Effectively forced into HITL mode regardless of configured oversight model. |
| **Trigger Conditions** | |
| - Critical KPI breached (e.g., payment accuracy < 98%) | |
| - Safety metric violation detected | |
| - Model confidence consistently below threshold (> 20% of interactions) | |
| - Critical tool unavailable (e.g., payment gateway, identity verification) | |
| - Level 1 persists for > 30 minutes without recovery | |
| **Automated Responses** | |
| - Override oversight model to HITL for all actions | |
| - Queue all consequential actions for human approval | |
| - Continue handling informational queries autonomously | |
| - Activate circuit breaker on affected tools | |
| **Human Notification** | Alert Model Owner + Fleet Operations Lead + On-Call Engineer immediately (SMS + Slack + PagerDuty) |
| **Customer Communication** | "To ensure accuracy, a team member will review this action before I proceed. This may take a moment." |
| **Recovery Condition** | All critical triggers resolved; Model Owner explicitly approves return to Level 1 or Level 0 |

#### Level 3: Manual

| Aspect | Specification |
|--------|--------------|
| **Description** | Agent is suspended from customer interaction. All customer requests are routed to human agents. The AI agent may continue operating in the background to provide suggestions and context to human agents, but never communicates directly with customers. |
| **Trigger Conditions** | |
| - Multiple safety violations in a short window (> 3 in 1 hour) | |
| - Model endpoint completely unavailable | |
| - Security incident affecting the agent (data breach, unauthorized access) | |
| - Compliance Officer or AI Governance Committee orders suspension | |
| - Level 2 persists for > 1 hour without recovery | |
| **Automated Responses** | |
| - Route all new customer conversations to human queue | |
| - Active conversations: agent says farewell and transfers to human | |
| - Agent continues logging for post-incident analysis | |
| - Incident automatically created in incident management system | |
| **Human Notification** | Alert all stakeholders: Model Owner, Fleet Ops Lead, On-Call Engineer, Compliance Officer, Customer Operations Lead |
| **Customer Communication** | "I'm transferring you to a team member who will be able to help you directly. Thank you for your patience." For new sessions: "You're being connected with a team member. Please hold." |
| **Recovery Condition** | Root cause identified and resolved; Model Owner + Compliance Officer explicitly approve return to Level 2 or higher; mandatory post-incident review scheduled |

#### Level 4: Emergency

| Aspect | Specification |
|--------|--------------|
| **Description** | Complete AI system failure. No AI agent capability available. Static fallback content is served to customers. This level represents infrastructure-level failure where even the agent runtime is unavailable. |
| **Trigger Conditions** | |
| - Complete infrastructure outage (cloud region, network failure) | |
| - Critical security event requiring immediate shutdown (kill switch activated) | |
| - Regulatory authority orders immediate cessation of AI operations | |
| - Manual trigger by Fleet Operations Lead or authorized incident commander | |
| **Automated Responses** | |
| - Activate static fallback page / IVR message | |
| - DNS failover to static content (if configured) | |
| - All agent processes terminated | |
| - Incident severity automatically set to P1 | |
| **Human Notification** | P1 incident protocol activated: all on-call staff, engineering management, customer operations management, compliance, and executive sponsor notified |
| **Customer Communication** | Static message: "Our AI assistant is currently unavailable. For immediate assistance, please call [phone number] or email [email address]. We apologize for the inconvenience." |
| **Recovery Condition** | Infrastructure restored; system health verified; Model Owner + Fleet Ops Lead + Compliance Officer explicitly approve staged recovery (Level 4 to Level 3 to Level 2 to Level 1 to Level 0). No direct jump from Level 4 to Level 0. |

---

### 4. Customer Communication Templates

Pre-approved templates for each degradation level. These must be reviewed by Compliance and Product before deployment.

| Level | Channel | Template |
|-------|---------|----------|
| **Level 1** (feature unavailable) | Chat | "This feature is temporarily unavailable. I can help you with [alternative], or I can connect you with a team member. What would you prefer?" |
| **Level 2** (assisted mode) | Chat | "To ensure everything is accurate, a team member will review this action before I proceed. This may take a moment longer than usual." |
| **Level 3** (transfer to human) | Chat | "I'm connecting you with a team member who can assist you directly. They will have the context of our conversation. Thank you for your patience." |
| **Level 3** (new session) | Chat | "You're being connected with a team member. Our AI assistant is undergoing maintenance to improve service quality. A team member will be with you shortly." |
| **Level 4** (static) | Web | "Our AI assistant is currently unavailable. For immediate assistance, please call [phone number] during business hours ([hours]), or email [email address]. We apologize for any inconvenience." |
| **Level 4** (static) | IVR | "Our automated assistant is temporarily unavailable. Please hold for the next available representative, or call back during business hours." |

---

### 5. Recovery Procedures

#### 5.1 Recovery Sequence

Recovery must follow the degradation levels in reverse order. No skipping levels.

```
Level 4 (Emergency)
    |
    v  Infrastructure restored; health checks passing
Level 3 (Manual)
    |
    v  Root cause confirmed resolved; Model Owner approves
Level 2 (Assisted)
    |
    v  Agent performing correctly in HITL mode for > 30 minutes
Level 1 (Reduced)
    |
    v  All KPIs return to green for > 15 minutes
Level 0 (Normal)
```

#### 5.2 Recovery Approval Matrix

| Recovery Transition | Approval Required | Evidence Required |
|--------------------|-------------------|-------------------|
| Level 4 to Level 3 | Fleet Ops Lead + On-Call Engineer | Infrastructure health checks passing; system logs clean |
| Level 3 to Level 2 | Model Owner + Compliance Officer | Root cause identified; fix deployed; regression tests passing |
| Level 2 to Level 1 | Model Owner | Agent performance in HITL mode matches expectations; no new issues for 30 min |
| Level 1 to Level 0 | Auto-approved (with logging) | All KPIs in green for 15 minutes; no active alerts |

---

### 6. Testing Requirements

| Test Type | Description | Frequency | Owner |
|-----------|------------|-----------|-------|
| **Level 1 simulation** | Simulate tool unavailability; verify agent degrades gracefully and customer experience is acceptable | Quarterly | AI/ML Engineer |
| **Level 2 simulation** | Simulate critical KPI breach; verify agent transitions to HITL mode and human queue activates | Quarterly | MLOps Engineer |
| **Level 3 drill** | Simulate agent suspension; verify all traffic routes to human agents with context transfer | Semi-annually | Customer Operations Lead |
| **Level 4 drill** | Simulate complete outage; verify static fallback activates and P1 notification fires | Annually | Fleet Operations Lead |
| **Recovery test** | From Level 3, verify staged recovery through Level 2, Level 1, to Level 0 | Semi-annually | Model Owner |
| **Kill switch test** | Verify immediate transition from any level to Level 4 via kill switch | Quarterly | On-Call Engineer |

#### 6.1 Test Documentation

Each test must produce:

- Test date and participants
- Simulated failure scenario
- Observed degradation behaviour (pass/fail per expected behaviour)
- Customer communication delivered (screenshot or log)
- Notification delivery (confirmed recipients and timing)
- Recovery steps executed
- Issues discovered and remediation actions
- Sign-off by test owner

---

### 7. Kill Switch Protocol

Per SAFEST A-09, every agent must have a kill switch mechanism.

| Aspect | Specification |
|--------|--------------|
| **Activation method** | Dashboard button (Fleet Ops Lead or authorized On-Call Engineer) OR API call OR automated trigger |
| **Effect** | Immediate transition to Level 4 (Emergency). All agent processes terminated. Static fallback activated. |
| **Activation time** | < 30 seconds from trigger to full shutdown |
| **Authorization** | Pre-authorized for On-Call Engineer and Fleet Ops Lead. No approval chain required during emergencies. |
| **Audit log** | Kill switch activation logged with timestamp, activator identity, and reason |
| **Recovery from kill switch** | Requires Model Owner + Fleet Ops Lead + Compliance Officer approval for staged recovery |

---

### 8. Dependencies and Contact Information

| Dependency | Contact | Escalation |
|-----------|---------|------------|
| **LLM Provider** | `<provider support contact>` | `<escalation path>` |
| **Tool/API Provider** | `<tool provider contact>` | `<escalation path>` |
| **Cloud Infrastructure** | `<cloud provider support>` | `<escalation path>` |
| **Customer Operations (human queue)** | `<customer ops lead>` | `<escalation to management>` |
| **On-Call Engineering** | `<on-call rotation schedule>` | `<engineering management>` |
| **Compliance (for Level 3+ decisions)** | `<compliance officer>` | `<AI Governance Committee chair>` |

---

## Cross-References

- **Customer-Facing Agent Safety:** [../agentic-workflows/customer-facing-agent-safety.md](../agentic-workflows/customer-facing-agent-safety.md) -- degradation hierarchy and graceful degradation rules (Sec. 6)
- **Multi-Agent Governance Framework:** [../agentic-workflows/multi-agent-governance-framework.md](../agentic-workflows/multi-agent-governance-framework.md) -- five degradation levels (Sec. 8.1)
- **Agent Fleet Operations:** [../agentic-workflows/agent-fleet-operations.md](../agentic-workflows/agent-fleet-operations.md) -- health state mapping to degradation levels (Sec. 2); registry references this procedure
- **Human-in-the-Loop Patterns:** [../agentic-workflows/human-in-the-loop-patterns.md](../agentic-workflows/human-in-the-loop-patterns.md) -- HITL mode activated during Level 2
- **Safety Policy Definition:** [safety-policy-definition.md](safety-policy-definition.md) -- escalation triggers that may activate fallback
- **AI Incident Report:** [../../04-operational-governance/templates/ai-incident-report.md](../../04-operational-governance/templates/ai-incident-report.md) -- incidents triggered by Level 3+ transitions
- **Incident Response Checklist:** [../../04-operational-governance/checklists/incident-response-checklist.yaml](../../04-operational-governance/checklists/incident-response-checklist.yaml) -- operational checklist for incident handling
- **SAFEST Checklist:** [../../04-operational-governance/regulatory/safest-checklist-detailed.md](../../04-operational-governance/regulatory/safest-checklist-detailed.md) -- S-13 (fallback), A-07 (override), A-09 (kill switch)
- **Glossary:** [../../05-cross-cutting/glossary.md](../../05-cross-cutting/glossary.md) -- definitions for graceful degradation, circuit breaker, kill switch

---

*Last updated: 2026-03-01* / *Version: 1.0* / *Classification: Internal / Regulatory Preparation*
