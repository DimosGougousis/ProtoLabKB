# Physical Safety Lifecycle Management — Manufacturing AI Systems

> **Purpose:** Defines the lifecycle management process for ProtoLabs AI systems that interact with physical manufacturing environments, ensuring rigorous documentation, verification, validation, and continuous human oversight of safety-critical AI recommendations.

**Version:** 1.0  
**Date:** 2026-04-24  
**Owner:** Safety Officer  
**Classification:** Confidential — Internal Distribution  
**Regulatory Basis:** EU AI Act Articles 9, 14, 15; ISO 42001 Clauses 6.1, 8.3, 8.4; Machinery Directive 2006/42/EC (for Annex I systems)

---

## 1. Scope

This procedure applies to ProtoLabs AI systems that:
- Recommend or control physical manufacturing parameters (CNC feeds/speeds, tooling selection, material handling)
- Make quality control decisions affecting physical product safety
- Predict maintenance needs for safety-critical equipment
- Are embedded in or function as safety components of machinery (EU AI Act Annex I)

---

## 2. Safety Lifecycle Phases

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    PHYSICAL SAFETY LIFECYCLE                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐ │
│   │  DEFINE  │ → │ VERIFY   │ → │ VALIDATE │ → │ DEPLOY   │ → │ MONITOR  │ │
│   │          │   │          │   │          │   │          │   │          │ │
│   │ Document │   │ Simulate │   │ Controlled│   │ Gradual │   │ Near-    │ │
│   │ safety   │   │ test     │   │ environment│  │ rollout │   │ miss     │ │
│   │ reqs     │   │          │   │ test     │   │ with HITL│   │ logging  │ │
│   └──────────┘   └──────────┘   └──────────┘   └──────────┘   └──────────┘ │
│         ↑                                                            ↓     │
│         └──────────────────── CONTINUOUS IMPROVEMENT ←─────────────────┘     │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Phase 1: Define Safety Requirements

### 3.1 Safety Requirements Specification

| Requirement Category | Example for CNC Machining Agent | Owner |
|---------------------|--------------------------------|-------|
| **Functional Safety** | "Must recommend spindle speeds within machine's rated capacity" | Technical Owner |
| **Operational Safety** | "Must flag recommendations exceeding tool manufacturer's specifications" | Safety Officer |
| **Emergency Safety** | "Must recommend emergency stop if collision risk detected" | Safety Officer |
| **Environmental Safety** | "Must account for coolant flow requirements for recommended parameters" | Technical Owner |
| **Human Safety** | "Must require operator confirmation for speeds >80% of machine maximum" | Safety Officer |

### 3.2 Safety Requirements Template

```
SAFETY REQUIREMENT ID: SAF-REQ-[YYYY]-[NNN]

Description: [Clear, testable requirement]
Rationale: [Why this requirement exists]
Verification Method: [How to verify during testing]
Validation Method: [How to validate in real operation]
Acceptance Criteria: [Measurable criteria for pass/fail]
Risk if Not Met: [Description of potential harm]
Authority Level: [Who can approve deviation]
```

### 3.3 Safety Requirements for ProtoLabs Agents

| Agent | Safety-Critical Output | Safety Requirement Example |
|-------|----------------------|---------------------------|
| `{{cnc-machining}}` | Feed/speed recommendations | "Recommended feed rate shall not exceed 120% of tool manufacturer's specification" |
| `{{injection-molding}}` | Pressure/temperature settings | "Recommended injection pressure shall not exceed machine's rated clamping force safety margin" |
| `{{sheet-metal}}` | Bend radius recommendations | "Recommended bend radius shall not cause material fracture per material datasheet" |
| `{{3d-printing}}` | Support structure recommendations | "Support structure shall not compromise part structural integrity during removal" |
| Quality Control Vision | Pass/fail decisions | "False negative rate for safety-critical defects shall not exceed 0.1%" |
| Predictive Maintenance | Maintenance scheduling | "Critical safety component failure prediction shall have >99% recall" |

---

## 4. Phase 2: Verify in Simulation

### 4.1 Simulation Testing Requirements

| Test Type | Description | Evidence |
|-----------|-------------|----------|
| **Digital Twin Testing** | Test AI recommendations against digital twin of manufacturing equipment | Simulation report |
| **Edge Case Testing** | Test boundary conditions, extreme inputs, failure modes | Edge case test report |
| **Adversarial Safety Testing** | Test AI behavior under adversarial conditions affecting safety | Adversarial safety report |
| **Failure Mode Testing** | Test AI response to simulated sensor failures, data corruption | FMEA test report |

### 4.2 Simulation Verification Checklist

| Check | Requirement | Pass Criteria | Status |
|-------|-------------|---------------|--------|
| 4.2.1 | All safety requirements tested in simulation | 100% coverage | ☐ |
| 4.2.2 | Edge cases identified and tested | Documented edge cases | ☐ |
| 4.2.3 | Failure modes tested | FMEA complete | ☐ |
| 4.2.4 | Simulation validated against real equipment | Correlation report | ☐ |
| 4.2.5 | Safety margins verified | Margin analysis | ☐ |

---

## 5. Phase 3: Validate in Controlled Environment

### 5.1 Controlled Environment Testing

| Environment Type | Purpose | Duration | Evidence |
|-----------------|---------|----------|----------|
| **Laboratory Test** | Validate AI recommendations on test equipment | 1-2 weeks | Lab test report |
| **Pilot Production Run** | Validate in limited production with full supervision | 2-4 weeks | Pilot report |
| **Shadow Mode** | Run AI in parallel with human operators, compare outputs | 4-8 weeks | Shadow mode report |
| **Graduated Autonomy** | Gradually increase AI autonomy with human oversight | 4-12 weeks | Graduation report |

### 5.2 Controlled Environment Validation Checklist

| Check | Requirement | Pass Criteria | Status |
|-------|-------------|---------------|--------|
| 5.2.1 | Human operators trained on AI capabilities and limitations | Training records | ☐ |
| 5.2.2 | Override mechanisms tested and functional | Override test log | ☐ |
| 5.2.3 | Emergency stop procedures tested | E-stop test log | ☐ |
| 5.2.4 | Near-miss reporting system active | Near-miss log | ☐ |
| 5.2.5 | Safety metrics meet acceptance criteria | Metrics report | ☐ |
| 5.2.6 | No safety incidents during validation period | Incident log (zero) | ☐ |

---

## 6. Phase 4: Deploy with Human-in-the-Loop

### 6.1 Deployment Safety Controls

| Control | Implementation | Owner |
|---------|---------------|-------|
| **Tier 2 Conditional Autonomy** | AI recommends, human confirms before execution | Safety Officer |
| **Tier 3 High Autonomy with Kill Switch** | AI executes with 5-second kill switch for safety-critical actions | Safety Officer |
| **Real-time Safety Monitoring** | Continuous monitoring of AI outputs against safety bounds | MLOps Engineer |
| **Automatic Safety Shutdown** | Automatic halt if AI output exceeds safety parameters | MLOps Engineer |
| **Human Override** | Operator can override any AI recommendation at any time | Operator |

### 6.2 Deployment Safety Matrix

| Agent | Autonomy Tier | Kill Switch | Human Confirmation | Safety Monitoring |
|-------|--------------|-------------|-------------------|-------------------|
| `{{cnc-machining}}` | Tier 2 (Conditional) | 30s | Required for speeds >80% max | Real-time |
| `{{injection-molding}}` | Tier 2 (Conditional) | 30s | Required for pressures >80% max | Real-time |
| `{{sheet-metal}}` | Tier 2 (Conditional) | 30s | Required for bends <1.5× thickness | Real-time |
| Quality Control Vision | Tier 2 (Conditional) | 30s | Required for safety-critical pass decisions | Real-time |
| Predictive Maintenance | Tier 1 (Advisory) | N/A | N/A | Periodic |

---

## 7. Phase 5: Monitor and Log Near-Misses

### 7.1 Near-Miss Definition

A near-miss is any event where:
- An AI recommendation approached but did not exceed safety limits
- An AI recommendation was overridden by a human operator for safety reasons
- An AI system exhibited unexpected behavior that could have led to harm
- A safety monitoring alert was triggered

### 7.2 Near-Miss Logging

| Field | Description | Example |
|-------|-------------|---------|
| Near-Miss ID | Unique identifier | NM-2026-001 |
| Date/Time | When the near-miss occurred | 2026-04-24 14:32:00 |
| Agent | Which AI system was involved | `{{cnc-machining}}` |
| Description | What happened | "AI recommended feed rate at 118% of tool spec; operator reduced to 95%" |
| Safety Parameter | Which safety limit was approached | "Feed rate / tool spec" |
| Proximity to Limit | How close to the safety limit | "118% of limit (margin: 2%)" |
| Human Action | What the human operator did | "Reduced feed rate to 95%" |
| Root Cause | Why the AI approached the limit | "Training data included aggressive parameters from high-performance applications" |
| Corrective Action | Action taken to prevent recurrence | "Updated training data filtering to exclude parameters >110% of manufacturer spec" |

### 7.3 Near-Miss Review Process

| Frequency | Participants | Output |
|-----------|------------|--------|
| Weekly | Safety Officer, Technical Owner | Weekly near-miss summary |
| Monthly | Safety Officer, CAIO, Technical Owner | Monthly safety review |
| Quarterly | Full governance committee | Quarterly safety report to board |

---

## 8. Continuous Improvement

### 8.1 Safety Performance Metrics

| Metric | Target | Measurement Frequency |
|--------|--------|----------------------|
| Near-miss rate | <1 per 1,000 recommendations | Weekly |
| Human override rate | <5% of safety-critical recommendations | Weekly |
| Safety limit approach rate | <0.1% of recommendations | Weekly |
| Safety incident rate | Zero | Continuous |
| Kill switch activation rate | <0.01% of Tier 2/3 operations | Weekly |

### 8.2 Improvement Triggers

| Trigger | Action |
|---------|--------|
| Near-miss rate exceeds target | Immediate safety review, potential system pause |
| Human override rate exceeds target | Review AI training data, update safety margins |
| Safety incident occurs | Immediate system halt, full investigation, authority notification |
| New safety hazard identified | Update safety requirements, re-verify in simulation |

---

## 9. Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-24 | ProtoLabs AI Governance Office | Initial physical safety lifecycle management procedure |

---

## See Also

- `eu-ai-act-conformity-assessment-procedure.md` — Conformity assessment
- `eu-ai-act-incident-reporting-procedure.md` — Incident reporting
- `governance/03-runtime-governance/agentic-workflows/human-in-the-loop-patterns.md` — HITL patterns
- `agent-tier-classification.yaml` — Agent autonomy tiers
