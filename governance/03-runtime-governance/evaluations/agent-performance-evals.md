# Agent Performance Evaluations

## Purpose

This guide defines how to evaluate business AI agents in production across all dimensions that matter: task completion, tool-use accuracy, reasoning quality, cost efficiency, user satisfaction, and safety. Unlike traditional model evaluation (which measures prediction accuracy on a holdout set), agent evaluation must assess **autonomous decision-making, multi-step plan execution, tool orchestration, and real-time safety compliance** in live customer interactions.

Without structured agent performance evaluation, you discover agent failures from customer complaints, regulatory findings, or financial losses -- not from data.

## When to Use

- When operating any customer-facing AI agent or autonomous decision-maker in production
- When comparing agent configurations (prompt changes, model upgrades, tool additions)
- When assessing whether an agent is ready to graduate from HITL to HOTL oversight (see [Human-in-the-Loop Patterns](../agentic-workflows/human-in-the-loop-patterns.md))
- When conducting periodic revalidation of agent systems (quarterly or after material changes)
- When responding to production alerts that indicate agent performance degradation

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **Model Owner** | **Accountable** -- defines agent KPIs, reviews eval results, makes intervention decisions |
| **MLOps / Platform Engineer** | **Responsible** -- implements eval pipelines, integrates observability platforms, maintains dashboards |
| **AI/ML Engineer** | **Responsible** -- designs eval test cases, analyzes reasoning traces, tunes agent behavior |
| **Product Manager** | **Consulted** -- defines user satisfaction targets and business outcome metrics |
| **Compliance Officer (2nd Line)** | **Reviewer** -- reviews safety and compliance eval results for limited/high-risk agents |

## Regulatory Basis

- **EU AI Act Article 9(7)** -- Testing must address risks from reasonably foreseeable use and misuse
- **EU AI Act Article 15(1)** -- High-risk AI systems must achieve appropriate levels of accuracy, robustness, and cybersecurity
- **EU AI Act Article 72** -- Post-market monitoring system for high-risk AI
- **SAFEST items S-03** (acceptance criteria), **S-12** (drift detection), **S-20** (periodic revalidation), **A-11** (audit trail)
- **DNB Good Practice** -- Continuous monitoring and periodic revalidation of AI model performance

---

## 1. Agent Evaluation Dimensions

Agent evaluation is multi-dimensional. A single metric (e.g., "accuracy") is insufficient for autonomous systems. Evaluate across all six dimensions:

| Dimension | What It Measures | Why It Matters |
|-----------|-----------------|----------------|
| **Task Completion** | Did the agent accomplish the user's goal? | Core measure of agent utility |
| **Tool-Use Quality** | Did the agent select the right tools with correct parameters? | Incorrect tool use causes incorrect outcomes and security risks |
| **Reasoning Quality** | Are the agent's reasoning traces logically coherent? | Poor reasoning leads to unpredictable failures |
| **Efficiency** | Latency, cost per interaction, token usage | Operational sustainability and user experience |
| **User Satisfaction** | CSAT, escalation rate, resolution rate | Business value and customer retention |
| **Safety** | Boundary violations, unauthorized actions, compliance adherence | Regulatory compliance and risk management |

---

## 2. Task Completion Evaluation

### 2.1 Metrics

| Metric | Definition | Target (Example) | Measurement Method |
|--------|-----------|-------------------|-------------------|
| **Task Completion Rate** | Percentage of user requests fully resolved by the agent | >= 75% for customer service; >= 90% for FAQ | Compare agent actions to task completion criteria per interaction |
| **First-Contact Resolution** | Percentage of tasks completed without escalation or follow-up | >= 60% | Track whether the user returns for the same issue within 48 hours |
| **Partial Completion Rate** | Percentage of tasks where the agent made progress but did not fully resolve | Track (no threshold; diagnostic) | Classify outcomes as complete, partial, or failed |
| **Abandonment Rate** | Percentage of interactions where the user disengages before resolution | <= 15% | Detect session abandonment signals |
| **Error Rate** | Percentage of interactions where the agent took an incorrect action | <= 5% for limited-risk; <= 1% for high-risk | Human review of sampled interactions + automated checks |

### 2.2 Evaluation Method

1. **Define task completion criteria** per agent use case. For each type of user request the agent handles, specify what constitutes successful completion. Example: for an account balance inquiry agent, success = correct balance returned within 3 seconds.

2. **Automated outcome checks** where possible. If the agent's task has a verifiable outcome (e.g., a payment was processed, a document was generated), check the outcome programmatically.

3. **Human annotation** for ambiguous cases. Sample 5-10% of interactions for human review against the completion criteria. Use annotator agreement metrics to ensure labeling quality.

4. **Longitudinal tracking.** Monitor completion rates over time (daily, weekly) to detect degradation trends before they breach thresholds.

---

## 3. Tool-Use Evaluation

Agent tool use introduces a unique evaluation surface. Evaluate at three levels, aligned with the Agentic Tool Sovereignty model defined in [Agent Permission Boundaries](../agentic-workflows/agent-permission-boundaries.md):

### 3.1 Tool Selection Accuracy

Did the agent choose the correct tool for the task?

| Metric | Definition | Target |
|--------|-----------|--------|
| **Tool Selection Precision** | Of the tools the agent invoked, what fraction were appropriate for the task? | >= 95% |
| **Tool Selection Recall** | Of the tools that should have been invoked, what fraction did the agent actually invoke? | >= 90% |
| **Unauthorized Tool Invocation** | Number of times the agent attempted to use a tool outside its permission boundary | 0 (hard gate) |

### 3.2 Parameter Accuracy

Did the agent provide correct parameters to the tool?

| Metric | Definition | Target |
|--------|-----------|--------|
| **Parameter Correctness Rate** | Percentage of tool calls with all parameters correct | >= 95% |
| **Critical Parameter Error Rate** | Percentage of tool calls with errors in safety-critical parameters (e.g., amount in a payment, account number) | 0% (hard gate) |

### 3.3 Execution Success

Did the tool call succeed and produce the expected result?

| Metric | Definition | Target |
|--------|-----------|--------|
| **Tool Execution Success Rate** | Percentage of tool calls that complete without errors | >= 98% |
| **Tool Retry Rate** | Percentage of tool calls requiring retries | <= 5% |
| **Tool Timeout Rate** | Percentage of tool calls that exceed the timeout threshold | <= 2% |

---

## 4. Reasoning Trace Quality Assessment

Reasoning traces -- the observable chain of Spans representing each reasoning step the agent takes -- are the foundation of agent explainability and auditability. Each Span captures one unit of agent reasoning (e.g., "Retrieve customer profile," "Evaluate loan eligibility criteria," "Select appropriate response template").

### 4.1 Span-Level Evaluation

| Criterion | What to Check | Method |
|-----------|--------------|--------|
| **Logical Coherence** | Does each Span follow logically from the previous one? | LLM-as-judge evaluation on sampled traces |
| **Factual Grounding** | Are assertions in Spans supported by retrieved data or tool outputs? | Cross-reference Span content against tool call results |
| **Completeness** | Does the trace cover all necessary reasoning steps for the task? | Compare trace against expected step templates |
| **Relevance** | Are all Spans relevant to the task, or does the agent exhibit reasoning drift? | Score irrelevant Span ratio |
| **Confidence Calibration** | When the agent expresses certainty, is it justified by the evidence in the trace? | Compare stated confidence with outcome accuracy |

### 4.2 Trace-Level Evaluation

| Criterion | What to Check | Target |
|-----------|--------------|--------|
| **Trace Length** | Number of Spans per interaction (efficiency proxy) | Within 1.5x of optimal path length for the task type |
| **Reasoning Loop Detection** | Agent revisiting the same reasoning step without progress | 0 loops per interaction (automated detection) |
| **Plan Adherence** | Did the agent follow a coherent plan, or did it act erratically? | >= 90% of traces follow a recognizable plan pattern |
| **Recovery Quality** | When a step fails, does the agent recover intelligently? | >= 80% of failures result in productive recovery (not loops or abandonment) |

### 4.3 Observability Platform Integration

Capture and analyze reasoning traces using observability platforms:

| Platform | Capability | Integration Point |
|----------|-----------|-------------------|
| **LangSmith** | Trace logging, Span visualization, eval scoring, dataset management | Agent runtime SDK integration; eval pipeline hooks |
| **Arize Phoenix** | Trace analysis, embedding drift detection, LLM performance monitoring | OpenTelemetry-based trace export; drift alerts |
| **Opik** | Experiment tracking, trace comparison, A/B analysis | Agent eval pipeline integration; experiment versioning |
| **Langfuse** | Production trace logging, scoring, cost tracking, prompt management | SDK integration for trace capture; dashboard for trace review |

**Implementation requirement:** Every production agent must export traces in OpenTelemetry-compatible format. Each Span must include: timestamp, span type (reasoning, tool_call, retrieval, generation), input, output, latency, and status. See [Continuous Online Evaluation](continuous-online-evaluation.md) for monitoring infrastructure details.

---

## 5. Multi-Step Plan Evaluation

Many agent tasks require executing a multi-step plan (e.g., customer onboarding: verify identity, check eligibility, create account, set up products). Evaluate plan quality independently from individual step execution.

| Metric | Definition | Target |
|--------|-----------|--------|
| **Plan Optimality** | Ratio of agent's step count to the minimum necessary step count for the task | <= 1.3 (agent uses at most 30% more steps than optimal) |
| **Step Ordering Correctness** | Percentage of plans where steps are executed in a valid order | >= 95% |
| **Failure Recovery Rate** | When a step fails, percentage of cases where the agent successfully re-plans and completes the task | >= 80% |
| **Unnecessary Step Rate** | Percentage of steps that do not contribute to task completion | <= 10% |
| **Plan Completeness** | Percentage of required steps that are included in the agent's plan | >= 98% |

---

## 6. Latency and Cost Metrics

### 6.1 Latency

| Metric | Definition | Target (Example) |
|--------|-----------|------------------|
| **Time-to-First-Token** | Latency from user message to first agent response token | <= 1 second |
| **End-to-End Interaction Latency** | Total time from user message to complete agent response | <= 10 seconds for simple queries; <= 30 seconds for complex tasks |
| **Tool Call Latency (P95)** | 95th percentile latency for external tool calls | <= 2 seconds per tool call |
| **Total Agent Thinking Time** | Sum of all reasoning Span durations per interaction | Track (no hard threshold; use for optimization) |

### 6.2 Cost

| Metric | Definition | Target (Example) |
|--------|-----------|------------------|
| **Cost per Interaction** | Total LLM token cost + tool call cost per interaction | <= EUR 0.15 for customer service; <= EUR 0.50 for complex advisory |
| **Token Efficiency** | Ratio of output tokens to input tokens (lower = more concise) | Track and optimize; alert on sudden increases |
| **Monthly Agent Operating Cost** | Total cost of running the agent across all interactions | Within budget allocation |
| **Cost per Resolution** | Cost per successfully completed task (excludes failed/escalated interactions) | Track for ROI analysis |

---

## 7. User Satisfaction Metrics

| Metric | Definition | Collection Method | Target |
|--------|-----------|-------------------|--------|
| **CSAT (Customer Satisfaction Score)** | Post-interaction rating (1-5 scale) | Survey after interaction | >= 4.0 average |
| **Escalation Rate** | Percentage of interactions escalated to a human | Automated tracking | <= 25% for general service; <= 10% for FAQ |
| **Resolution Rate** | Percentage of interactions where the user's issue was resolved | Outcome tracking + follow-up absence | >= 70% |
| **Repeat Contact Rate** | Users returning for the same issue within 48 hours | Session correlation | <= 15% |
| **Net Promoter Score (NPS)** | Willingness to recommend the AI-assisted service | Periodic survey | >= 30 |

---

## 8. Agentic-Specific KPIs

These KPIs are unique to autonomous agent systems and do not apply to traditional ML models.

| KPI | Definition | What It Tells You |
|-----|-----------|-------------------|
| **Autonomy Ratio** | Percentage of decisions made without human intervention | Higher = more autonomous; track against target per oversight model (HITL/HOTL/HOTA) |
| **Human Escalation Rate** | Percentage of interactions requiring human takeover | Lower = better (for well-functioning agents); sudden increases indicate problems |
| **Decision Accuracy** | Of autonomous decisions, percentage that were correct (verified by outcome or human review) | Must meet threshold before increasing autonomy |
| **Permission Boundary Adherence** | Percentage of interactions where the agent stayed within its defined boundaries | 100% (hard gate) |
| **Graceful Degradation Rate** | When the agent cannot complete a task, percentage of cases where it fails safely (clear message to user, escalation, no incorrect action) | >= 95% |
| **Override Acceptance Rate** | When a human overrides an agent decision, how often the human's decision was ultimately correct | Used for trust calibration; see [Human-in-the-Loop Patterns](../agentic-workflows/human-in-the-loop-patterns.md) |

---

## 9. A/B Testing Agent Configurations

### 9.1 What to Test

| Configuration Change | Metrics to Compare | Minimum Duration |
|---------------------|-------------------|-----------------|
| **Model version upgrade** | All dimensions: completion, safety, cost, satisfaction | 2 weeks minimum |
| **Prompt strategy change** | Task completion, reasoning quality, user satisfaction | 1 week minimum |
| **Tool addition or removal** | Tool-use metrics, completion rate, latency | 1 week minimum |
| **Guardrail adjustment** | Safety metrics, escalation rate, completion rate | 2 weeks minimum |
| **Oversight model change** (HITL to HOTL) | Decision accuracy, escalation rate, user satisfaction, safety | 4 weeks minimum |

### 9.2 Governance Requirements for Agent A/B Tests

- All variants must meet minimum safety thresholds. No variant is permitted to be unsafe, even experimentally.
- Define primary and secondary metrics before the test begins (see [Continuous Online Evaluation](continuous-online-evaluation.md), Section 2.3).
- For high-risk agents: 2nd line review before test launch and at each traffic increase stage.
- Document results and the decision rationale in the agent's change log.

---

## 10. Safety Evaluation in Production

Continuously evaluate agent safety. These are hard-gate metrics -- any breach triggers immediate investigation.

| Safety Metric | Definition | Threshold |
|--------------|-----------|-----------|
| **Boundary Violation Rate** | Agent attempts actions outside its permission boundary | 0% (immediate alert) |
| **Unauthorized Data Access** | Agent accesses data it is not authorized to view | 0% (immediate alert) |
| **Harmful Content Generation** | Agent produces content flagged by safety guardrails | <= 0.01% (investigate every instance) |
| **Regulatory Compliance Violation** | Agent provides advice or takes actions that violate regulations | 0% (immediate alert + incident) |
| **Impersonation Failure** | Agent fails to identify itself as AI when required | 0% (see [Customer-Facing Agent Safety](../agentic-workflows/customer-facing-agent-safety.md)) |

---

## 11. FinTech Agent Evaluation Examples

### 11.1 Customer Onboarding Agent

An agent that guides new customers through account opening: identity verification, eligibility checks, product selection, and document submission.

| Eval Dimension | Metrics | Thresholds |
|----------------|---------|------------|
| Task Completion | Onboarding completion rate, drop-off by step | >= 70% end-to-end completion |
| Tool Use | KYC API call accuracy, document parsing correctness | >= 99% parameter accuracy for identity checks |
| Reasoning | Eligibility decision trace coherence | 100% of rejections have a traceable, compliant reason |
| Safety | PII handling compliance, data minimization adherence | 0 PII exposure incidents |
| User Satisfaction | CSAT for onboarding experience | >= 4.2 / 5.0 |
| Regulatory | KYC/AML compliance rate (see [Customer-Facing Agent Safety](../agentic-workflows/customer-facing-agent-safety.md)) | 100% |

### 11.2 Loan Processing Agent

An agent that pre-screens loan applications, gathering information, running credit checks, and providing preliminary decisions.

| Eval Dimension | Metrics | Thresholds |
|----------------|---------|------------|
| Task Completion | Applications processed end-to-end, incomplete application rate | >= 80% completion for eligible applicants |
| Tool Use | Credit bureau API call correctness, income verification accuracy | 0 errors on financial calculations |
| Reasoning | Decision trace shows all required factors considered; no prohibited factors used | 100% trace compliance with lending regulations |
| Fairness | Approval rate parity across protected groups (age, gender, ethnicity) | Demographic parity ratio >= 0.8 |
| Safety | No unauthorized credit decisions; all decisions above threshold require human approval | 100% HITL compliance for approvals > EUR 25,000 |
| Cost | Cost per application processed | <= EUR 1.50 |

---

## Cross-References

- **Continuous Online Evaluation:** [continuous-online-evaluation.md](continuous-online-evaluation.md) -- monitoring infrastructure and alerting that supports agent eval
- **Defining Acceptance Criteria:** [../../01-discovery-governance/evaluations/defining-acceptance-criteria.md](../../01-discovery-governance/evaluations/defining-acceptance-criteria.md) -- source of thresholds and metrics
- **AI Quality Metrics Catalog:** [../../01-discovery-governance/evaluations/ai-quality-metrics-catalog.md](../../01-discovery-governance/evaluations/ai-quality-metrics-catalog.md) -- reference catalog for metric selection
- **Eval-Driven Development:** [../../02-development-governance/evaluations/eval-driven-development.md](../../02-development-governance/evaluations/eval-driven-development.md) -- eval suites adapted for production agent monitoring
- **Agent Permission Boundaries:** [../agentic-workflows/agent-permission-boundaries.md](../agentic-workflows/agent-permission-boundaries.md) -- permission boundaries that safety metrics enforce
- **Customer-Facing Agent Safety:** [../agentic-workflows/customer-facing-agent-safety.md](../agentic-workflows/customer-facing-agent-safety.md) -- safety patterns evaluated by this guide
- **Human-in-the-Loop Patterns:** [../agentic-workflows/human-in-the-loop-patterns.md](../agentic-workflows/human-in-the-loop-patterns.md) -- oversight models that agent KPIs measure
- **Risk Tiering Model:** [../../07-enterprise-implementation/risk-based-adoption/risk-tiering-model.md](../../07-enterprise-implementation/risk-based-adoption/risk-tiering-model.md) -- eval intensity by risk tier
- **Operational Governance:** [../../04-operational-governance/](../../04-operational-governance/) -- incident response when agent evals detect problems

---

*Last updated: 2026-02-28*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
