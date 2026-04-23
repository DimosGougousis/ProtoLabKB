# LLM Observability and Decision Audit Trails

## Purpose

This guide defines how to implement observability and traceability for LLM-based and agentic AI systems in regulated FinTech environments. It covers the setup and governance use of four observability platforms -- LangSmith, Arize Phoenix, Opik, and Langfuse -- and explains the core concept of "Spans" as the fundamental unit of traceable reasoning. For FinTech organizations, observability is not just an engineering convenience -- it is a regulatory obligation. SAFEST item A-05 (traceability) and A-11 (decision audit trail) require the ability to reconstruct any AI-influenced decision after the fact. SAFEST item T-17 requires production monitoring dashboards.

This guide shows how to build an observability architecture that satisfies these regulatory requirements while providing the engineering team with the debugging and monitoring capabilities needed to operate AI systems responsibly.

## When to Use

- When setting up observability infrastructure for new AI systems
- When instrumenting existing AI systems to meet traceability requirements
- When investigating an AI incident that requires reasoning trace reconstruction
- When preparing audit evidence demonstrating decision traceability
- When evaluating observability tool options for procurement
- When designing the monitoring pipeline for agent systems with tool use and delegation

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **MLOps / Platform Engineer** | **Responsible** -- instruments systems with tracing, maintains observability infrastructure, manages data retention |
| **ML Engineer** | **Responsible** -- adds trace annotations to agent code, defines meaningful span boundaries, tags traces with governance metadata |
| **Model Owner** | **Accountable** -- ensures traceability requirements are met for their system; defines what must be traced |
| **Compliance Officer (2nd Line)** | **Reviewer** -- validates that traces provide sufficient evidence for regulatory audit; reviews PII handling in traces |
| **DPO** | **Consulted** -- ensures that trace data collection complies with GDPR; approves PII redaction policies |
| **Internal Audit (3rd Line)** | **Consumer** -- uses traces during audit to verify decision-making processes |

## Regulatory Basis

- **SAFEST item A-05** -- Model ownership with documented accountability for traceability
- **SAFEST item A-11** -- Decision audit trail: every AI-assisted decision logged with input data, model version, output, confidence level, human reviewer, and final action
- **SAFEST item T-16** -- Decision traceability: any AI-influenced decision can be reconstructed after the fact
- **SAFEST item T-17** -- Monitoring dashboards: real-time visibility into AI system performance
- **EU AI Act Article 12** -- Record-keeping: high-risk AI systems shall technically allow for automatic recording of events (logs)
- **EU AI Act Article 14(4)(d)** -- Human oversight: ability to understand the capacities and limitations of the AI system and monitor its operation
- **DORA Article 10** -- Detection: arrangements to promptly detect anomalous activities in ICT systems

---

## 1. The Spans Concept: Reasoning Steps as Traceable Units

### 1.1 What Is a Span?

A **Span** is a single traceable unit of work within an AI system's execution. Borrowed from distributed systems observability (OpenTelemetry), a Span represents one step in the agent's reasoning or action chain. Spans are hierarchical: a parent span can contain child spans, forming a **trace tree** that represents the complete decision-making process.

For agentic AI systems, spans capture:
- **LLM calls:** The prompt sent, the model version used, the completion received, token counts, latency
- **Tool invocations:** Which tool was called, what parameters were passed, what result was returned
- **Retrieval operations:** What query was sent to the retrieval system, what documents were returned, relevance scores
- **Guardrail checks:** Which guardrails were evaluated, whether they passed or failed, what action was taken
- **Delegation events:** Which sub-agent was invoked, what task was delegated, what result was returned
- **Human decisions:** When a human-in-the-loop reviewed an output, what decision they made, any modifications

### 1.2 Trace Tree Example: Customer Service Agent

```
Trace: customer-query-2026-03-01-14:32:05 (trace_id: abc123)
|
+-- Span: Input Processing (12ms)
|   |-- Input text: "I was charged twice for my subscription"
|   |-- PII detected: false
|   |-- Guardrail check: PASS
|
+-- Span: LLM Call - Intent Classification (340ms)
|   |-- Model: gpt-4o-2024-08-06
|   |-- Prompt tokens: 420
|   |-- Completion tokens: 35
|   |-- Intent: "billing_dispute"
|   |-- Confidence: 0.94
|
+-- Span: Tool Call - Fetch Account History (180ms)
|   |-- Tool: get_transaction_history
|   |-- Parameters: {customer_id: "CUST-9821", days: 30}
|   |-- Result: [2 subscription charges found]
|   |-- Permission check: PASS (read-only access)
|
+-- Span: LLM Call - Generate Response (520ms)
|   |-- Model: gpt-4o-2024-08-06
|   |-- Prompt tokens: 890
|   |-- Completion tokens: 145
|   |-- Response: "I can see you were indeed charged twice..."
|   |-- Confidence: 0.91
|
+-- Span: Output Guardrail (8ms)
|   |-- PII redaction: no PII in output
|   |-- Financial advice check: PASS
|   |-- Compliance check: PASS
|
+-- Span: Tool Call - Create Support Ticket (95ms)
    |-- Tool: create_ticket
    |-- Parameters: {type: "billing_dispute", priority: "medium"}
    |-- Result: ticket_id: "TKT-44201"
    |-- Permission check: PASS (write access to tickets)
```

### 1.3 Why Spans Matter for Governance

| Governance Need | How Spans Address It |
|----------------|---------------------|
| **Decision reconstruction** (SAFEST A-11, T-16) | The full trace tree shows exactly how the agent reached its decision, including what data it retrieved, what tools it used, and what reasoning steps it took |
| **Incident investigation** | When something goes wrong, the trace pinpoints exactly which span failed and why |
| **Permission boundary audit** | Tool call spans include permission checks, enabling verification that agents stayed within boundaries |
| **Performance monitoring** (SAFEST T-17) | Span latencies and token counts enable monitoring of system health |
| **Fairness analysis** | Traces can be analyzed in aggregate to detect whether reasoning patterns differ across customer demographics |
| **Regulatory evidence** (EU AI Act Art. 12) | Immutable trace logs provide the automatic recording of events required for high-risk AI |

---

## 2. Observability Platforms

### 2.1 LangSmith

| Attribute | Details |
|-----------|---------|
| **What it does** | Full-lifecycle LLM application platform by LangChain: tracing, evaluation, monitoring, and prompt management |
| **Tracing capability** | Automatic trace capture for LangChain/LangGraph applications; manual SDK for non-LangChain systems; hierarchical span trees with metadata |
| **Governance strengths** | Trace search and filtering; annotation and feedback workflows; side-by-side trace comparison; dataset creation from production traces for regression testing |
| **FinTech considerations** | Cloud-hosted by default (data residency considerations); on-premise option available for sensitive deployments; PII in traces requires redaction policy |
| **Integration** | Native LangChain/LangGraph; Python SDK for custom; REST API for non-Python |
| **Best for** | Teams using LangChain/LangGraph; organizations that want integrated tracing + evaluation + prompt management |

**Setup for governance tracing:**
- Tag every trace with: `model_version`, `system_id`, `risk_tier`, `customer_segment` (anonymized)
- Configure retention aligned with regulatory requirements (minimum 5 years for Wwft; 10 years for EU AI Act)
- Enable PII redaction before trace storage if traces may contain customer data
- Create evaluation datasets from production traces for regression testing

### 2.2 Arize Phoenix

| Attribute | Details |
|-----------|---------|
| **What it does** | Open-source AI observability platform for production monitoring, tracing, evaluation, and experimentation |
| **Tracing capability** | OpenTelemetry-based tracing; supports any LLM framework; embedding drift detection; trace analytics |
| **Governance strengths** | Embedding-level drift monitoring; production performance dashboards; trace clustering for anomaly detection; open-source with self-hosted option |
| **FinTech considerations** | Self-hosted deployment keeps all data on-premises; OpenTelemetry compatibility enables integration with existing enterprise observability stacks; no vendor lock-in |
| **Integration** | OpenTelemetry SDK; Python; integrates with LangChain, LlamaIndex, DSPy, and custom frameworks |
| **Best for** | Production monitoring and drift detection; organizations with existing OpenTelemetry infrastructure; teams needing embedding-level analysis |

**Setup for governance tracing:**
- Deploy self-hosted for FinTech data sovereignty requirements
- Configure embedding drift monitors for each production model
- Set up automated alerts for performance degradation and anomalous trace patterns
- Export trace data to governance evidence repository on defined cadence

### 2.3 Opik

| Attribute | Details |
|-----------|---------|
| **What it does** | Open-source LLM evaluation and experiment tracking platform by Comet |
| **Tracing capability** | Trace capture with hierarchical spans; experiment tracking with baseline comparison; LLM-as-judge evaluation |
| **Governance strengths** | Experiment tracking creates a versioned history of model behavior changes; baseline comparison supports regression detection; LLM-as-judge enables scalable output quality evaluation |
| **FinTech considerations** | Self-hosted option available; experiment history provides evidence of systematic evaluation over time |
| **Integration** | Python SDK; integrates with LangChain, LlamaIndex, and custom frameworks; supports major LLM providers |
| **Best for** | Experiment tracking and baseline comparison; teams that want versioned evaluation history; development-to-production evaluation continuity |

**Setup for governance tracing:**
- Use experiment tracking to maintain a versioned record of all model evaluations
- Configure baseline experiments for each deployment to enable regression comparison
- Integrate LLM-as-judge evaluations for output quality scoring in production
- Export experiment results as governance evidence for pre-deployment gate documentation

### 2.4 Langfuse

| Attribute | Details |
|-----------|---------|
| **What it does** | Open-source LLM engineering and observability platform; tracing, prompt management, evaluation, and analytics |
| **Tracing capability** | Hierarchical trace capture with custom span types; prompt versioning and A/B testing; cost tracking per trace; user-level analytics |
| **Governance strengths** | Cost tracking per trace enables cost governance; prompt versioning creates an audit trail for prompt changes; self-hosted with full data control; user-level analytics support fairness analysis |
| **FinTech considerations** | Self-hosted deployment is mature and well-documented; cost tracking is essential for FinTech cost governance; prompt versioning supports the model change log requirement (SAFEST A-12) |
| **Integration** | Python and JavaScript SDKs; integrates with LangChain, LlamaIndex, Vercel AI SDK, and custom frameworks; REST API |
| **Best for** | Teams wanting full data sovereignty with open-source; cost-conscious organizations needing per-trace cost tracking; prompt management with version control |

**Setup for governance tracing:**
- Deploy self-hosted for complete data sovereignty
- Enable prompt versioning to create an immutable audit trail of all prompt changes
- Configure cost tracking to monitor per-system and per-interaction costs
- Set up user-level analytics (anonymized) for fairness monitoring across customer segments
- Configure data retention aligned with regulatory requirements

---

## 3. Reconstructing Agent Decision Chains for Audit

### 3.1 Decision Reconstruction Process

When a regulator, auditor, or compliance officer asks "Why did the system make this decision?", the answer must be reconstructable from traces:

**Step 1: Identify the decision**
- Obtain the decision identifier (transaction ID, ticket ID, case ID)
- Map it to the trace ID in the observability platform

**Step 2: Retrieve the full trace**
- Load the complete trace tree including all spans
- Verify that no spans are missing (check for span count consistency)

**Step 3: Reconstruct the reasoning chain**
- Walk through spans in chronological order
- For each LLM call: what prompt was sent? What was the model's response?
- For each tool call: what data was retrieved or what action was taken?
- For each guardrail check: did it pass or fail? If it failed, what happened?
- For each delegation: which sub-agent was invoked and what did it decide?

**Step 4: Produce the audit narrative**
- Translate the technical trace into a human-readable narrative
- Include: input received, data retrieved, reasoning steps, tools used, output produced, human involvement (if any)
- Attach the raw trace as supporting evidence

### 3.2 Audit-Ready Trace Requirements

For every trace to be audit-ready, it must include:

| Metadata | Description | Why Required |
|----------|-------------|-------------|
| **Trace ID** | Unique identifier for the complete interaction | Enables retrieval and cross-referencing |
| **Timestamp** | ISO 8601 timestamp for every span | Establishes chronological sequence |
| **Model version** | Exact model version and provider for every LLM call | SAFEST A-11 requires model version in audit trail |
| **System ID** | Which AI system produced the trace | Maps to AI system inventory (SAFEST S-01) |
| **Input data** | What the system received (with PII redacted) | SAFEST A-11 requires input data in audit trail |
| **Output data** | What the system produced (with PII redacted) | SAFEST A-11 requires output in audit trail |
| **Confidence** | Model confidence for each decision | SAFEST A-11 requires confidence level |
| **Human reviewer** | If a human reviewed the output, who and what they decided | SAFEST A-11 requires human reviewer identification |
| **Final action** | What ultimately happened (approved, rejected, escalated) | SAFEST A-11 requires final action taken |
| **Tool calls** | Complete record of all tool invocations with parameters and results | Permission boundary compliance evidence |
| **Guardrail results** | Which guardrails were evaluated and their outcomes | Safety control compliance evidence |

### 3.3 PII Handling in Traces

Traces will inevitably encounter customer PII (names, account numbers, transaction details). Governance requires:

1. **Redact PII before storage:** Configure the observability platform to redact PII patterns before traces are persisted
2. **Tokenize identifiers:** Replace customer IDs with pseudonymized tokens that can be de-tokenized only with authorization
3. **Classify trace data:** Mark traces with data classification labels (public, internal, confidential, restricted)
4. **Access control:** Restrict trace access to authorized personnel; log all trace access for audit
5. **Retention policy:** Align trace retention with regulatory requirements (5 years Wwft; 10 years EU AI Act); implement automated deletion after retention period

---

## 4. Production Monitoring Architecture

### 4.1 Monitoring Layers

```
Layer 1: Real-Time Alerting (seconds)
  - Latency spikes, error rate increases, circuit breaker activations
  - Tool: Application monitoring (Datadog, Grafana) + Observability platform alerts

Layer 2: Near-Real-Time Quality Monitoring (minutes-hours)
  - Output quality scores, guardrail trigger rates, trace anomalies
  - Tool: Arize Phoenix / Langfuse dashboards with automated scoring

Layer 3: Periodic Evaluation (daily-weekly)
  - Drift detection, regression testing, fairness monitoring
  - Tool: Scheduled eval pipelines + Opik experiment tracking

Layer 4: Strategic Review (monthly-quarterly)
  - Trend analysis, governance health, regulatory compliance
  - Tool: Eval Reporting Dashboard (eval-reporting-dashboard.md)
```

### 4.2 Key Monitoring Metrics Derived from Traces

| Metric | Computed From | Alert Threshold |
|--------|--------------|----------------|
| **LLM latency p50/p95/p99** | LLM call span durations | p95 > 2x baseline |
| **Tool call error rate** | Tool call span success/failure | > 5% failure rate |
| **Guardrail trigger rate** | Guardrail span outcomes | Sudden change > 20% from baseline |
| **Trace completeness** | Missing spans in expected trace structure | Any incomplete trace in high-risk system |
| **Token cost per interaction** | Sum of token counts across all LLM spans | > 2x expected cost |
| **Agent delegation depth** | Maximum span nesting depth in multi-agent traces | Exceeds configured maximum |
| **Permission boundary violations** | Tool call spans with failed permission checks | Any violation (zero tolerance) |
| **Reasoning coherence score** | LLM-as-judge evaluation of reasoning span chain | Score < threshold defined in model card |

---

## 5. FinTech-Specific Traceability Requirements

### 5.1 Payment Processing Traceability

For AI systems involved in payment processing (fraud detection, risk scoring, SCA exemption):
- Every payment decision trace must be linkable to the payment transaction ID
- Traces must capture the specific risk factors that influenced the decision
- Traces must be available for chargeback dispute resolution (minimum 540 days per card scheme rules)

### 5.2 AML/KYC Traceability

For AI systems involved in AML transaction monitoring or KYC:
- Traces must capture all data sources consulted and the search results obtained
- Traces must record the scoring logic that determined whether to alert or not
- Traces must be retained for 5 years per Wwft (10 years in some cases)
- Traces must be producible to FIU (Financial Intelligence Unit) on request

### 5.3 Credit Decision Traceability

For AI systems involved in credit decisions:
- Traces must capture all features used in the credit assessment
- Traces must record the explanation generated for the customer (EU AI Act Art. 86(1) for right to explanation)
- Traces must be linkable to the adverse action notice if credit was denied
- Traces must support the customer's right to request human review (GDPR Art. 22)

---

## 6. OpenTelemetry gen_ai.* Semantic Conventions

### 6.1 Overview

The OpenTelemetry community has defined semantic conventions specifically for generative AI operations (`gen_ai.*`). These standardized attributes enable consistent observability across different LLM providers and frameworks, making traces portable and comparable across tools.

### 6.2 Key Semantic Attributes

| Attribute | Description | Example Value |
|-----------|-------------|---------------|
| `gen_ai.system` | The AI system/provider name | "openai", "anthropic", "azure_openai" |
| `gen_ai.request.model` | Model identifier sent in request | "gpt-4o-2024-08-06" |
| `gen_ai.response.model` | Actual model used for response | "gpt-4o-2024-08-06" |
| `gen_ai.usage.input_tokens` | Input/prompt tokens consumed | 420 |
| `gen_ai.usage.output_tokens` | Output/completion tokens consumed | 145 |
| `gen_ai.usage.total_tokens` | Total tokens consumed | 565 |
| `gen_ai.response.finish_reason` | Reason generation stopped | "stop", "length", "content_filter" |
| `gen_ai.request.temperature` | Sampling temperature used | 0.7 |
| `gen_ai.request.max_tokens` | Maximum tokens requested | 2048 |
| `gen_ai.request.top_p` | Nucleus sampling parameter | 0.95 |

### 6.3 7 Key Operational Metrics from Research

Based on industry research on LLM observability and governance, the following operational metrics are critical for production monitoring:

| Metric | Semantic Convention | Governance Purpose |
|--------|---------------------|-------------------|
| **1. Token Efficiency Ratio** | `gen_ai.usage.output_tokens / gen_ai.usage.input_tokens` | Cost governance; identifies inefficient prompt patterns |
| **2. Latency per Token** | `span.duration_ms / gen_ai.usage.total_tokens` | Performance monitoring; capacity planning |
| **3. Completion Rate** | Traces where `gen_ai.response.finish_reason = "stop"` / Total traces | Quality indicator; high truncation rates signal issues |
| **4. Error Rate by Model** | Failed spans grouped by `gen_ai.response.model` | Reliability tracking; model-specific issue detection |
| **5. Temperature-Adjusted Variance** | Output variance across different `gen_ai.request.temperature` values | Determinism assessment; reproducibility for audit |
| **6. Prompt Injection Detection** | Guardrail spans with `security.check_type = "prompt_injection"` | Security monitoring; attack surface measurement |
| **7. Cost per Decision** | Sum of token costs across all spans in a decision trace | Financial governance; per-decision cost attribution |

### 6.4 Implementation with OpenTelemetry SDK

```python
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

# Configure OpenTelemetry with gen_ai conventions
tracer_provider = TracerProvider()
otlp_exporter = OTLPSpanExporter(endpoint="https://your-collector")
tracer_provider.add_span_processor(BatchSpanProcessor(otlp_exporter))
trace.set_tracer_provider(tracer_provider)

tracer = trace.get_tracer("ai-governance")

# Example: Instrumented LLM call with gen_ai attributes
with tracer.start_as_current_span("llm.completion") as span:
    span.set_attribute("gen_ai.system", "openai")
    span.set_attribute("gen_ai.request.model", "gpt-4o-2024-08-06")
    span.set_attribute("gen_ai.request.temperature", 0.7)
    
    # ... make LLM call ...
    
    span.set_attribute("gen_ai.response.model", response.model)
    span.set_attribute("gen_ai.usage.input_tokens", response.usage.prompt_tokens)
    span.set_attribute("gen_ai.usage.output_tokens", response.usage.completion_tokens)
    span.set_attribute("gen_ai.response.finish_reason", response.choices[0].finish_reason)
```

### 6.5 Integration with Governance Tools

| Tool | OpenTelemetry Support | gen_ai Conventions |
|------|----------------------|-------------------|
| **Langfuse** | Native OTLP ingestion | Full support; custom dashboards for gen_ai metrics |
| **Arize Phoenix** | Native OpenTelemetry | Native gen_ai semantic convention support |
| **Braintrust** | OTLP export available | Custom attributes mapped to gen_ai conventions |
| **LangSmith** | Proprietary format | Limited; requires adapter for OTel conventions |

**Recommendation for FinTech:** Use OpenTelemetry with gen_ai semantic conventions as the primary instrumentation layer. This ensures vendor portability and aligns with enterprise observability standards while satisfying SAFEST traceability requirements.

---

## 7. Tool Selection Decision Guide

| Criterion | LangSmith | Arize Phoenix | Opik | Langfuse |
|-----------|----------|---------------|------|---------|
| **Self-hosted option** | Yes (enterprise) | Yes (open source) | Yes (open source) | Yes (open source) |
| **Data sovereignty** | Cloud by default; on-prem available | Full control (self-hosted) | Full control (self-hosted) | Full control (self-hosted) |
| **Cost tracking** | Basic | Basic | Basic | Native per-trace |
| **Prompt versioning** | Yes | No | No | Yes (native) |
| **Drift detection** | Via evals | Native (embeddings) | Via baselines | Via custom scoring |
| **Experiment tracking** | Yes | Yes | Yes (primary) | Basic |
| **LangChain integration** | Native | Via OpenTelemetry | Via SDK | Via SDK |
| **Framework agnostic** | SDK available | OpenTelemetry (any) | SDK available | SDK available |
| **FinTech recommendation** | Best for LangChain-native teams with prompt management needs | Best for production monitoring with embedding drift | Best for systematic experiment tracking with baselines | Best for cost governance with full data sovereignty |

**Recommendation:** Most FinTech organizations will benefit from combining two platforms -- one for development/evaluation (LangSmith or Opik) and one for production monitoring (Arize Phoenix or Langfuse). All four support self-hosted deployment, which is essential for FinTech data sovereignty.

---

## Cross-References

- **Drift Detection Evals:** [../../04-operational-governance/evaluations/drift-detection-evals.md](../evaluations/drift-detection-evals.md) -- drift detection uses trace data from observability platforms
- **Model Monitoring Dashboard:** [../templates/model-monitoring-dashboard.md](../templates/model-monitoring-dashboard.md) -- operational dashboard consuming observability data
- **Eval Reporting Dashboard:** [../evaluations/eval-reporting-dashboard.md](../evaluations/eval-reporting-dashboard.md) -- evaluation dashboard sourcing trace-derived metrics
- **AI Incident Report Template:** [../templates/ai-incident-report.md](../templates/ai-incident-report.md) -- incident investigation relies on trace reconstruction (Section 4)
- **Red-Teaming Guide:** [red-teaming-ai-systems.md](red-teaming-ai-systems.md) -- red-team exercises capture traces for attack analysis
- **Continuous Online Evaluation:** [../../03-runtime-governance/evaluations/continuous-online-evaluation.md](../../03-runtime-governance/evaluations/continuous-online-evaluation.md) -- production monitoring that sources from observability data
- **Agent Permission Boundaries:** [../../03-runtime-governance/agentic-workflows/agent-permission-boundaries.md](../../03-runtime-governance/agentic-workflows/agent-permission-boundaries.md) -- traces verify permission boundary compliance
- **SAFEST Checklist:** [../regulatory/safest-checklist-detailed.md](../regulatory/safest-checklist-detailed.md) -- A-05 (traceability), A-11 (audit trail), T-16 (decision traceability), T-17 (monitoring)
- **Tool Landscape:** [../../05-cross-cutting/tool-landscape.md](../../05-cross-cutting/tool-landscape.md) -- observability tool evaluations
- **RACI Matrix:** [../../05-cross-cutting/governance-roles-raci.md](../../05-cross-cutting/governance-roles-raci.md) -- traceability role assignments
- **Three Lines of Defense:** [../../07-enterprise-implementation/organizational-model/three-lines-of-defense-for-ai.md](../../07-enterprise-implementation/organizational-model/three-lines-of-defense-for-ai.md) -- 3rd line uses traces for independent assurance

---

*Last updated: 2026-03-01*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
