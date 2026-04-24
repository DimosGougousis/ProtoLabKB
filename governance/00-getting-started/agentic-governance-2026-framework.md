# Agentic AI Governance Framework 2026

> **Purpose:** Enhanced governance framework for ProtoLabs that bridges the gap between LLM-based agents and deterministic factory floor (OT) requirements. Incorporates NIST AI RMF Agentic Profile (April 2026), Singapore MGF for Agentic AI (January 2026), and Safety Agent architecture.

**Version:** 2.0 (Agentic Edition)  
**Last Updated:** 2026-04-24  
**Owner:** ProtoLabs AI Governance Office  
**Review Cycle:** Quarterly

---

## Executive Summary: The Shift from Copilots to Agents

The transition from "Copilots" (advisory AI) to "Agents" (action-taking AI) in manufacturing necessitates a fundamental shift in governance:

| Era | Risk Type | Governance Focus | Example |
|-----|-----------|------------------|---------|
| **Copilot (2023-2025)** | Content Risk | "What does the AI say?" | Chatbot gives wrong DFM advice |
| **Agent (2026+)** | Action Risk | "What can the AI DO?" | Agent autonomously adjusts CNC feed rates |

**Core Principle:** Agentic governance must control **actions**, not just **outputs**.

---

## Part 1: NIST AI RMF Agentic & Critical Infrastructure Profiles

### 1.1 The Action Risk Framework

Traditional NIST AI RMF manages "content risk" (hallucinations, bias). The **Agentic Profile** (April 2026) adds **"action risk"** management:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ACTION RISK vs CONTENT RISK                               │
├─────────────────────────────┬───────────────────────────────────────────────┤
│      CONTENT RISK           │           ACTION RISK                         │
│  (Traditional Governance)     │        (Agentic Governance)                   │
├─────────────────────────────┼───────────────────────────────────────────────┤
│ • Hallucinated text         │ • Unauthorized API calls                      │
│ • Biased recommendations    │ • Physical machine actuation                  │
│ • Incorrect calculations    │ • Supply chain order placement                │
│ • Unsafe suggestions        │ • Safety system bypass attempts               │
│ • IP leakage in output      │ • OT network traversal                        │
└─────────────────────────────┴───────────────────────────────────────────────┘
```

### 1.2 Autonomy Tiering (Mandatory Classification)

Every ProtoLabs agent MUST be classified into one of three tiers:

#### Tier 1: Advisory Agents (Read-Only)

| Attribute | Specification |
|-----------|---------------|
| **Capabilities** | Generate recommendations, analyze data, provide guidance |
| **Actions** | None — no API calls, no physical actuation |
| **Human Role** | Human decides and acts on recommendations |
| **Examples** | DFM Analysis Agent, Materials Selection Agent |
| **Governance** | Standard NIST AI RMF + content safety |
| **Kill Switch** | Not required (no physical risk) |

**Risk Level:** Low  
**EU AI Act:** Limited-Risk  
**OT Integration:** None

---

#### Tier 2: Conditional Autonomy Agents (Supervised Action)

| Attribute | Specification |
|-----------|---------------|
| **Capabilities** | Execute actions within defined boundaries, request human approval for exceptions |
| **Actions** | API calls to non-critical systems, data writes, scheduled tasks |
| **Human Role** | Supervises, approves exceptions, can override |
| **Examples** | Production Schedule Optimizer (with safety locks), Inventory Agent |
| **Governance** | NIST AI RMF Agentic Profile + Tool-Use Risk Modeling |
| **Kill Switch** | Required — 30-second activation |

**Risk Level:** Medium-High  
**EU AI Act:** High-Risk (if affects production)  
**OT Integration:** IT systems only (ERP, MES, not ICS)

**Hard Guardrails (Mandatory):**
- Cannot override safety-locked maintenance windows
- Cannot modify emergency stop logic
- Cannot bypass safety PLC code
- Cannot adjust parameters beyond defined safe ranges

---

#### Tier 3: High Autonomy Agents (Autonomous Action)

| Attribute | Specification |
|-----------|---------------|
| **Capabilities** | Autonomous decision-making and action within broad parameters |
| **Actions** | Real-time adjustments, multi-step workflows, physical system control |
| **Human Role** | Sets policy, monitors, intervenes only on exception |
| **Examples** | Real-time CNC parameter optimizer, Autonomous quality control |
| **Governance** | Full Agentic Profile + Critical Infrastructure Profile + Safety Agent |
| **Kill Switch** | Required — 5-second activation + automatic safe-state default |

**Risk Level:** Critical  
**EU AI Act:** High-Risk + Critical Infrastructure designation  
**OT Integration:** Direct ICS/SCADA integration

**Safety Agent Required:** Yes — All Tier 3 agents must route through Governor Agent

---

### 1.3 Tool-Use Risk Modeling

For Tier 2 and Tier 3 agents, governance must explicitly model **what tools the agent can invoke**:

```yaml
# Tool-Use Risk Model Template
agent_id: "cnc-parameter-optimizer-v1"
autonomy_tier: "Tier-3"

tool_registry:
  - tool_name: "mes_api_read"
    capability: "Read production schedule from MES"
    risk_level: "low"
    approval_required: false
    scpi_commands: []
    
  - tool_name: "cnc_feed_rate_adjust"
    capability: "Adjust CNC feed rate in real-time"
    risk_level: "critical"
    approval_required: false  # Autonomous, but bounded
    bounds:
      min_feed_rate: "10% of nominal"
      max_feed_rate: "120% of nominal"
      max_adjustment_delta: "5% per minute"
    safety_checks:
      - "spindle_load < 90%"
      - "tool_wear < threshold"
      - "no_collision_detected"
    scpi_commands:
      - "FEED:ADJUST"
      - "SPINDLE:LOAD:CHECK"
    
  - tool_name: "emergency_stop"
    capability: "Trigger emergency stop"
    risk_level: "critical"
    approval_required: false
    conditions: "Automatic on safety anomaly"
    scpi_commands:
      - "ESTOP:TRIGGER"
    
  - tool_name: "safety_plc_modify"
    capability: "Modify safety PLC logic"
    risk_level: "unacceptable"
    approval_required: "board_resolution"
    scpi_commands: []
    allowed: false  # NEVER ALLOWED
    
prohibited_actions:
  - "Modify emergency stop logic"
  - "Bypass safety interlocks"
  - "Override maintenance lockouts"
  - "Access safety PLC code"
  - "Modify robot safety zones (ISO 10218)"
```

**Governance Rule:** Every tool must have explicit risk classification and bounds. "Safety PLC Modify" is **unacceptable risk** — never allowed.

---

## Part 2: Singapore MGF for Agentic AI (January 2026)

### 2.1 Hard Guardrails for Physical Actions

Singapore's Model AI Governance Framework mandates **"Hard Guardrails"** — technical controls that physically prevent unsafe actions:

| Guardrail Type | Implementation | Example |
|----------------|----------------|---------|
| **Temporal** | Time-based restrictions | Agent cannot schedule production during maintenance windows |
| **Spatial** | Physical zone restrictions | Robot agent cannot enter human-occupied zones without escort |
| **Parametric** | Value range restrictions | Feed rate cannot exceed 120% of nominal |
| **Functional** | Capability restrictions | Agent cannot modify safety PLC logic |
| **Dependency** | Pre-condition checks | Production agent cannot run without confirmed material availability |

**ProtoLabs Implementation:**

```yaml
# Hard Guardrails Configuration
hard_guardrails:
  temporal:
    - rule: "No production scheduling during maintenance"
      maintenance_windows: "02:00-06:00 daily"
      enforcement: "MES API blocks requests"
      
  spatial:
    - rule: "Robot agents require human escort in Zone A"
      zones: ["A"]
      enforcement: "RFID badge check + motion sensors"
      
  parametric:
    - rule: "CNC feed rate bounded"
      min: "10% nominal"
      max: "120% nominal"
      enforcement: "Safety Agent validates before SCPI command"
      
  functional:
    - rule: "Safety PLC read-only"
      enforcement: "Network segmentation + firewall rules"
      
  dependency:
    - rule: "Material confirmation required"
      check: "Inventory API confirms stock > safety_stock"
      enforcement: "Production Agent cannot start without confirmation"
```

### 2.2 Meaningful Human Accountability (MHA)

Singapore MGF replaces "Human-in-the-Loop" (HITL) with **"Meaningful Human Accountability" (MHA)**:

| Model | Human Role | Problem | MHA Solution |
|-------|------------|---------|--------------|
| **HITL** | Click "OK" on every decision | Alert fatigue, rubber-stamping | Policy-level accountability |
| **MHA** | Define and own the policy that governs agent actions | Humans accountable for rules, not individual actions | Clear policy ownership |

**ProtoLabs MHA Implementation:**

```yaml
# Meaningful Human Accountability Registry
agent_id: "production-scheduler-v2"

policy_ownership:
  policy_name: "Production Scheduling Safety Policy"
  owner_role: "VP of Manufacturing"
  owner_name: "[Name]"
  approval_date: "2026-04-01"
  review_cadence: "quarterly"
  
  policy_scope:
    - "Defines safe operating windows"
    - "Sets maintenance lockout rules"
    - "Establishes material confirmation requirements"
    - "Specifies exception handling procedures"
    
  agent_constraints:
    - "Agent cannot override policy parameters"
    - "Agent must log all policy deviations"
    - "Agent must escalate exceptions to human"
    
  accountability_chain:
    - level: "Policy Owner"
      role: "VP of Manufacturing"
      accountable_for: "Policy correctness, safety outcomes"
      
    - level: "Technical Owner"
      role: "Manufacturing Engineering Lead"
      accountable_for: "Agent implementation, constraint enforcement"
      
    - level: "Operational Owner"
      role: "Production Manager"
      accountable_for: "Day-to-day monitoring, exception handling"
```

**Key Principle:** The VP of Manufacturing is accountable for the **policy**, not for clicking "approve" on every schedule change.

### 2.3 Multi-Agent Coordination & Error Escalation

Singapore MGF specifically addresses **cascading failures** between agents:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    MULTI-AGENT ERROR ESCALATION                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌─────────────────┐         ┌─────────────────┐         ┌──────────────┐ │
│   │  Supply Chain   │         │   Production    │         │   Quality    │ │
│   │     Agent       │────────▶│     Agent       │────────▶│    Agent     │ │
│   │                 │         │                 │         │              │ │
│   │ • Orders raw    │         │ • Schedules     │         │ • Inspects   │ │
│   │   materials     │         │   production    │         │   output     │ │
│   │ • Tracks        │         │ • Adjusts       │         │ • Flags      │ │
│   │   inventory     │         │   parameters    │         │   defects    │ │
│   └─────────────────┘         └─────────────────┘         └──────────────┘ │
│            │                           │                           │        │
│            │                           │                           │        │
│            ▼                           ▼                           ▼        │
│   ┌─────────────────────────────────────────────────────────────────────┐ │
│   │                    ORCHESTRATION AGENT                                │ │
│   │  • Monitors inter-agent dependencies                                │ │
│   │  • Detects cascading error conditions                               │ │
│   │  • Coordinates safe shutdown sequences                              │ │
│   └─────────────────────────────────────────────────────────────────────┘ │
│                                    │                                        │
│                                    ▼                                        │
│   ┌─────────────────────────────────────────────────────────────────────┐ │
│   │                    SAFETY AGENT (Governor)                          │ │
│   │  • Validates all cross-agent actions                                │ │
│   │  • Enforces global safety invariants                              │ │
│   │  • Triggers emergency stop if cascade detected                      │ │
│   └─────────────────────────────────────────────────────────────────────┘ │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Cascading Failure Example:**

1. **Supply Chain Agent** detects material shortage → reduces production target
2. **Production Agent** compensates by increasing line speed (unsafe)
3. **Quality Agent** detects defect rate increase → flags issue
4. **Orchestration Agent** detects conflict: "Supply down, speed up, quality down"
5. **Safety Agent** intervenes: "Speed increase violates safety policy" → triggers hold

**Governance Requirement:** All multi-agent systems must have:
- **Orchestration Agent** for dependency management
- **Safety Agent** for global safety enforcement
- **Cascading failure detection** in error handling

---

## Part 3: Meta-Governance Architecture (Safety Agent Pattern)

### 3.1 The Governor Agent Concept

The most advanced 2026 manufacturing governance is **technical**, not just procedural. The **Safety Agent** (or Governor Agent) architecture deploys a supervisory AI that validates all agent actions before execution.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SAFETY AGENT ARCHITECTURE                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌─────────────────┐    Validation Request    ┌──────────────────────┐   │
│   │   Worker Agent  │─────────────────────────▶│     Safety Agent     │   │
│   │                 │                          │     (Governor)       │   │
│   │ • Proposes CNC  │                          │                      │   │
│   │   path          │◀─────────────────────────│ • Validates against  │   │
│   │ • Requests      │    Validation Response     │   ISO 10218          │   │
│   │   schedule      │                          │ • Checks IEC 62443   │   │
│   │   change        │                          │ • Confirms safe      │   │
│   │                 │                          │   state              │   │
│   └─────────────────┘                          │ • Approves/Rejects   │   │
│            │                                   └──────────────────────┘   │
│            │                                            │                  │
│            │         If Approved                        │                  │
│            │◀──────────────────────────────────────────┘                  │
│            │                                                               │
│            ▼                                                               │
│   ┌─────────────────┐                                                      │
│   │   ICS/SCADA     │                                                      │
│   │   Execution     │                                                      │
│   │                 │                                                      │
│   │ • CNC Machine   │                                                      │
│   │ • Robot         │                                                      │
│   │ • Conveyor      │                                                      │
│   └─────────────────┘                                                      │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3.2 Safety Agent Validation Process

Every action from a Tier 2 or Tier 3 agent must pass through the Safety Agent:

```yaml
# Safety Agent Validation Workflow
validation_request:
  agent_id: "cnc-optimizer-v1"
  action_type: "adjust_feed_rate"
  proposed_parameters:
    machine_id: "CNC-05"
    new_feed_rate: "450 mm/min"
    current_feed_rate: "400 mm/min"
    tool_id: "T-203"
    
safety_agent_checks:
  check_1:
    name: "ISO 10218 Robotic Safety"
    standard: "ISO 10218-1:2011"
    query: "Does feed rate exceed safe limits for current tool and material?"
    result: "PASS"
    details: "450 mm/min < max 500 mm/min for T-203 on aluminum"
    
  check_2:
    name: "IEC 62443 Industrial Security"
    standard: "IEC 62443-3-3"
    query: "Is agent authorized to modify CNC-05 parameters?"
    result: "PASS"
    details: "Agent cnc-optimizer-v1 in authorized agents list for CNC-05"
    
  check_3:
    name: "Safe State Verification"
    query: "Is machine in safe state for parameter adjustment?"
    result: "PASS"
    details: "Spindle load 45%, no alarms, tool wear within limits"
    
  check_4:
    name: "Hard Guardrail Compliance"
    query: "Does adjustment violate temporal/spatial/parametric guardrails?"
    result: "PASS"
    details: "Within 120% nominal bound, not in maintenance window"
    
  check_5:
    name: "Multi-Agent Conflict"
    query: "Does this action conflict with other active agents?"
    result: "PASS"
    details: "No conflicts detected with maintenance-agent or quality-agent"
    
final_decision:
  status: "APPROVED"
  execution_token: "TOK-2026-0424-001"
  expires: "2026-04-24T14:30:00Z"  # 5-minute expiry
  
  conditions:
    - "Execute within 5 minutes or re-validate"
    - "Abort if spindle load exceeds 80%"
    - "Log all telemetry for audit"
```

### 3.3 Safety Agent Standards Integration

The Safety Agent validates against manufacturing-specific standards:

| Standard | Domain | Validation Check |
|----------|--------|------------------|
| **ISO 10218** | Robotic Safety | Robot speed, zone intrusion, collaborative operation |
| **IEC 62443** | Industrial Security | Network segmentation, authorized access, secure communication |
| **ISO/IEC 42001** | AI Management | Model validity, bias, explainability |
| **IEC 61508** | Functional Safety | Safety integrity levels (SIL), failure modes |
| **NFPA 79** | Electrical Safety | Machine electrical systems, emergency stops |
| **OSHA 1910** | Workplace Safety | Machine guarding, lockout/tagout |

---

## Part 4: Manufacturing-Specific Implementation Matrix

### 4.1 Governance by Function

| NIST AI RMF Function | Action for Manufacturing Agents | Recommended Standards/Tools |
|---------------------|----------------------------------|----------------------------|
| **GOVERN** | Define "No-Go" zones (agents cannot modify emergency stop logic or safety PLC code) | ISO/IEC 42001 (AIMS), Company Safety Policy |
| **MAP** | Map "Agent-to-Machine" dependencies. Identify what happens if agent loses connectivity during physical task | NIST AI RMF 1.0 + Agentic Profile, Network topology maps |
| **MEASURE** | Use Red-Teaming to see if agent can be "tricked" into violating safety protocols via prompt injection | OWASP Top 10 for LLM/Agents, Safety Agent validation logs |
| **MANAGE** | Implement "Kill-Switch" APIs. If agent's drift exceeds 5% in quality metrics, revert to last "Known Good" human baseline | Siemens Industrial Grade AI, Safety Agent orchestration |

### 4.2 Agentic Governance Checklist

```yaml
# Agentic Governance Requirements (2026)
# File: agentic-governance-checklist.yaml

agent_classification:
  - requirement: "Agent autonomy tier classified (Tier 1/2/3)"
    mandatory: true
    evidence: "agent-tier-classification.yaml"
    
  - requirement: "Tool-Use Risk Model completed"
    mandatory: true
    for_tiers: ["Tier-2", "Tier-3"]
    evidence: "tool-use-risk-model.yaml"
    
  - requirement: "Hard Guardrails configured"
    mandatory: true
    for_tiers: ["Tier-2", "Tier-3"]
    evidence: "hard-guardrails-config.yaml"
    
  - requirement: "Meaningful Human Accountability defined"
    mandatory: true
    evidence: "mha-registry.yaml"
    
  - requirement: "Safety Agent deployed (for Tier 3)"
    mandatory: true
    for_tiers: ["Tier-3"]
    evidence: "safety-agent-config.yaml"
    
  - requirement: "Multi-Agent Orchestration configured"
    mandatory: true
    when: "multiple_agents_interact"
    evidence: "orchestration-agent-config.yaml"
    
  - requirement: "Cascading failure detection implemented"
    mandatory: true
    when: "multiple_agents_interact"
    evidence: "cascade-detection-tests.yaml"
    
  - requirement: "Kill Switch tested"
    mandatory: true
    for_tiers: ["Tier-2", "Tier-3"]
    evidence: "kill-switch-test-log.yaml"
    sla: "Tier-2: 30s, Tier-3: 5s"
    
  - requirement: "OT/ICS integration security reviewed"
    mandatory: true
    for_tiers: ["Tier-2", "Tier-3"]
    evidence: "ics-security-assessment.pdf"
    
  - requirement: "ISO 10218 compliance verified"
    mandatory: true
    when: "robotic_systems_involved"
    evidence: "iso-10218-compliance-check.yaml"
    
  - requirement: "IEC 62443 compliance verified"
    mandatory: true
    for_tiers: ["Tier-2", "Tier-3"]
    evidence: "iec-62443-compliance-check.yaml"
```

---

## Part 5: ProtoLabs Agent Tier Classification

### 5.1 Current Agent Inventory

| Agent | Current Tier | Proposed Tier | Actions Allowed | Safety Agent Required |
|-------|--------------|---------------|-----------------|----------------------|
| **DFM Analysis** | Tier 1 | Tier 1 (no change) | Read-only recommendations | No |
| **CNC Machining** | Tier 1 | Tier 1 (no change) | Read-only DFM advice | No |
| **Injection Molding** | Tier 1 | Tier 1 (no change) | Read-only guidance | No |
| **Sheet Metal** | Tier 1 | Tier 1 (no change) | Read-only recommendations | No |
| **3D Printing** | Tier 1 | Tier 1 (no change) | Read-only guidance | No |
| **Materials Selection** | Tier 1 | Tier 1 (no change) | Read-only suggestions | No |
| **Quote Bot** (future) | — | Tier 2 | API calls to pricing system, ERP writes | Yes |
| **Production Scheduler** (future) | — | Tier 2 | MES API calls, schedule adjustments | Yes |
| **CNC Optimizer** (future) | — | Tier 3 | Real-time parameter adjustment, SCPI commands | Yes (Mandatory) |

### 5.2 Tier Upgrade Process

To upgrade an agent from Tier 1 to Tier 2 or 3:

1. **Complete Tool-Use Risk Model** — Document every API/tool the agent can invoke
2. **Define Hard Guardrails** — Technical constraints on agent actions
3. **Establish MHA** — Name the policy owner accountable for agent behavior
4. **Deploy Safety Agent** (Tier 3 only) — Governor agent validates all actions
5. **OT Security Review** — ICS/SCADA integration security assessment
6. **Kill Switch Implementation** — Tested and operational
7. **Governance Approval** — AI Governance Committee sign-off

---

## Part 6: Integration with Existing Framework

### 6.1 What Stays the Same

| Existing Element | Status |
|-----------------|--------|
| NIST AI RMF Four Functions | ✅ Retained — Foundation of governance |
| Seven Characteristics | ✅ Retained — Trustworthiness assessment |
| EU AI Act Risk Classification | ✅ Retained — Regulatory compliance |
| SAFEST Methodology | ✅ Retained — Internal governance rubric |
| Four-Pillar Structure | ✅ Retained — Discovery, Development, Runtime, Operational |

### 6.2 What's New (2026 Agentic Enhancements)

| New Element | Purpose |
|-------------|---------|
| **Autonomy Tiering** | Classify agents by capability (Tier 1/2/3) |
| **Tool-Use Risk Modeling** | Explicitly govern what agents can DO |
| **Hard Guardrails** | Technical constraints on physical actions |
| **Meaningful Human Accountability** | Policy-level ownership vs. rubber-stamp approval |
| **Safety Agent Architecture** | Governor agent validates all Tier 2/3 actions |
| **Multi-Agent Orchestration** | Prevent cascading failures between agents |
| **OT/ICS Integration** | Secure connection to factory floor systems |

### 6.3 Updated Artifact Mapping

| Artifact | Location | Purpose |
|----------|----------|---------|
| Agentic Governance Framework (this doc) | `00-getting-started/agentic-governance-2026-framework.md` | Master reference for agentic AI governance |
| Agent Tier Classification Template | `01-discovery-governance/templates/agent-tier-classification.yaml` | Classify agents by autonomy level |
| Tool-Use Risk Model Template | `03-runtime-governance/templates/tool-use-risk-model.yaml` | Document agent capabilities and bounds |
| Hard Guardrails Config Template | `03-runtime-governance/templates/hard-guardrails-config.yaml` | Technical constraints |
| MHA Registry Template | `05-cross-cutting/templates/mha-registry.yaml` | Policy ownership accountability |
| Safety Agent Specification | `03-runtime-governance/agentic-workflows/safety-agent-specification.md` | Governor agent architecture |
| Multi-Agent Orchestration Guide | `03-runtime-governance/agentic-workflows/multi-agent-orchestration.md` | Cascading failure prevention |

---

## Part 7: Summary — The 2026 Governance Stack

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    PROTOLABS 2026 GOVERNANCE STACK                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │  LAYER 4: EXECUTIVE GOVERNANCE                                       │  │
│  │  • AI Risk Appetite Framework                                        │  │
│  │  • Board Reporting (NIST AI RMF + SAFEST)                            │  │
│  │  • Regulatory Compliance (EU AI Act, Singapore MGF)                │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                    ▲                                        │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │  LAYER 3: SAFETY AGENT (Governor)                                    │  │
│  │  • Validates all Tier 2/3 actions                                    │  │
│  │  • Enforces ISO 10218, IEC 62443                                   │  │
│  │  • Global safety invariant enforcement                               │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                    ▲                                        │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │  LAYER 2: AGENTIC GOVERNANCE                                         │  │
│  │  • Autonomy Tiering (Tier 1/2/3)                                     │  │
│  │  • Tool-Use Risk Modeling                                            │  │
│  │  • Hard Guardrails (temporal, spatial, parametric)                   │  │
│  │  • Meaningful Human Accountability                                   │  │
│  │  • Multi-Agent Orchestration                                         │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                    ▲                                        │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │  LAYER 1: FOUNDATIONAL GOVERNANCE                                    │  │
│  │  • NIST AI RMF 1.0 (Four Functions)                                  │  │
│  │  • Seven Characteristics of Trustworthy AI                           │  │
│  │  • EU AI Act Risk Classification                                     │  │
│  │  • SAFEST Methodology                                                │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                    ▲                                        │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │  LAYER 0: TECHNICAL CONTROLS                                          │  │
│  │  • Kill Switches                                                     │  │
│  │  • Audit Trails                                                      │  │
│  │  • Network Segmentation (IT/OT)                                    │  │
│  │  • SCPI Command Filtering                                            │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Cross-References

- [NIST AI RMF Reference Guide](../05-cross-cutting/nist-ai-rmf-reference-guide.md) — Base framework
- [NIST AI RMF LMM Example](../nist-ai-rmf-lmm-example.md) — Complete assessment example
- [SAFEST to NIST AI RMF Mapping](../protolabs/nist-ai-rmf-safest-mapping.md) — Crosswalk
- [AI Risk Appetite Framework](../06-executive/ai-risk-appetite-framework.md) — Risk tolerance
- Singapore MGF: https://www.pdpc.gov.sg/help-and-resources/model-ai-governance-framework
- NIST AI RMF Agentic Profile: https://www.nist.gov/itl/ai-risk-management-framework

---

*This document represents the evolution of ProtoLabs AI governance from "Copilot" (content risk) to "Agent" (action risk) paradigms. All Tier 2 and Tier 3 agents must comply with this framework before deployment.*

**Last Updated:** 2026-04-24  
**Version:** 2.0 (Agentic Edition)  
**Classification:** Internal
