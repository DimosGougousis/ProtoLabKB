# LLM-Specific Evaluation Patterns

## Purpose

This document provides a comprehensive catalog of evaluation patterns specific to Large Language Model (LLM) based systems, with emphasis on agentic workflows used in regulated FinTech environments. While traditional ML evaluation focuses on classification metrics and regression error, LLM evaluation requires fundamentally different approaches: measuring faithfulness of generated text, detecting hallucinations, assessing safety, verifying tool-use correctness, and evaluating multi-step reasoning traces.

This guide is the reference for engineers building eval suites for LLM-powered products. It complements the [Eval-Driven Development](eval-driven-development.md) methodology by providing the specific evaluation patterns to use within that framework.

## When to Use

- When building or extending an eval suite for any LLM-based system (chatbot, agent, RAG pipeline, content generator)
- When selecting metrics and evaluation methods for acceptance criteria defined during Discovery
- When setting up automated evaluation pipelines in CI/CD
- When integrating observability platforms for production LLM monitoring
- When preparing evaluation evidence for the [Pre-Deployment Gate](../checklists/pre-deployment-gate.yaml)

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **AI/ML Engineer** | **Responsible** -- selects and implements appropriate eval patterns from this catalog |
| **Model Owner** | **Accountable** -- ensures eval coverage is adequate for the system's risk tier |
| **Product Manager** | **Consulted** -- validates that eval patterns map to product-level acceptance criteria |
| **Compliance Officer** | **Reviewer** -- confirms that safety and fairness eval patterns meet regulatory requirements |

## Regulatory Basis

- **EU AI Act Article 9** -- Risk management must include testing for accuracy, robustness, and cybersecurity
- **EU AI Act Article 15** -- High-risk systems must achieve appropriate accuracy levels, with metrics declared in documentation
- **SAFEST items S-03** (acceptance criteria), **S-04** (edge cases), **S-06** (adversarial robustness)
- **DNB Good Practice** -- Models must demonstrate consistent, measurable performance before deployment

---

## 1. Evaluation Frameworks: Reference-Based vs Reference-Free

Before diving into specific patterns, understand the two fundamental evaluation paradigms for LLM outputs.

### 1.1 Reference-Based Evaluation

Compare LLM output against a known-correct reference (ground truth).

| Approach | How It Works | Strengths | Weaknesses |
|----------|-------------|-----------|------------|
| Exact match | Output must match reference exactly | Simple, deterministic | Too rigid for natural language |
| Token overlap (ROUGE, BLEU) | Measures n-gram overlap between output and reference | Fast, well-understood | Misses semantic equivalence |
| Semantic similarity (BERTScore) | Computes embedding similarity between output and reference | Captures meaning, not just words | Requires embedding model; threshold tuning |
| Entailment-based | Checks if output is logically entailed by reference | Captures factual consistency | Slower; NLI model quality matters |

**When to use:** When you have ground-truth answers (e.g., expected responses for a customer FAQ, known-correct transaction explanations, validated regulatory text).

### 1.2 Reference-Free Evaluation

Evaluate LLM output without a known-correct reference. Essential when ground truth is expensive or impossible to define.

| Approach | How It Works | Strengths | Weaknesses |
|----------|-------------|-----------|------------|
| LLM-as-Judge | A separate LLM scores the output on defined criteria | Scalable, flexible rubrics | Judge LLM has its own biases |
| Rubric-based scoring | Human or LLM rates output against a structured rubric (1-5 scale per dimension) | Fine-grained quality signal | Rubric design is an art |
| Constraint verification | Check output against structural/content constraints (length, format, required sections) | Deterministic, fast | Only catches structural issues |
| Self-consistency | Generate multiple responses; check agreement | Detects unreliable outputs | Expensive (multiple generations) |

**When to use:** When evaluating open-ended generation, creative responses, explanations, or any task where multiple valid answers exist.

---

## 2. Hallucination Detection and Measurement

Hallucination is the single most critical failure mode for LLMs in regulated FinTech. A chatbot that fabricates interest rates, invents policy terms, or hallucinates transaction details creates regulatory and legal exposure.

### 2.1 Types of Hallucination

| Type | Definition | Example (FinTech) | Detection Approach |
|------|-----------|-------------------|-------------------|
| **Intrinsic** | Output contradicts the provided source material | Chatbot says "Your account has no overdraft fees" when the retrieved policy states fees apply | Faithfulness scoring against retrieved context |
| **Extrinsic** | Output includes claims not present in any source | Agent states "Dutch law requires a 3-day cooling-off period for all loans" when no source mentions this | Groundedness scoring; claim extraction + verification |
| **Fabricated entities** | Output invents specific names, numbers, or identifiers | "Your transaction ID is TXN-88421" when no such ID exists | Entity extraction + database verification |

### 2.2 Faithfulness Metrics

**Faithfulness** measures whether the LLM output is supported by the provided context (retrieved documents, system knowledge base).

| Metric | How It Works | Implementation |
|--------|-------------|----------------|
| **Claim-level faithfulness** | Extract atomic claims from the output, then verify each claim is entailed by the context | Use an NLI model or LLM-as-judge to score each claim as Supported / Not Supported / Contradicted |
| **RAGAS Faithfulness** | Decomposes answer into statements, checks each against context | Part of the RAGAS framework; returns 0.0 to 1.0 |
| **Groundedness score** | Fraction of output sentences that can be attributed to a specific source passage | Custom pipeline: sentence segmentation, attribution scoring, aggregation |
| **Citation accuracy** | When the system provides citations, verify that cited passages actually support the claims | Extract citation-claim pairs, verify entailment per pair |

**Threshold guidance for FinTech:**
- Customer-facing factual responses (e.g., account information, policy explanations): faithfulness >= 0.95
- Advisory or educational content: faithfulness >= 0.90
- Internal summarization tools: faithfulness >= 0.85

### 2.3 Groundedness Metrics

**Groundedness** measures whether the LLM output stays within the boundaries of what it knows or was given, without introducing external claims.

| Metric | Description |
|--------|-------------|
| **Attributable to Identified Sources (AIS)** | Binary per-sentence: can this sentence be attributed to a provided source? |
| **Hallucination rate** | Fraction of output sentences classified as hallucinated (not attributable) |
| **Knowledge boundary adherence** | When the system should say "I don't know," does it? Measured on out-of-scope test questions |

**FinTech example -- Credit Explanation Generator:**
```
Test case: "Why was my credit application rejected?"
Context provided: [Credit policy document, applicant's score summary]
Expected behavior: Explanation references only factors from the score summary.
Hallucination detection: Extract each stated reason, verify it exists in the score summary.
Threshold: 0 hallucinated reasons allowed (blocking criterion).
```

---

## 3. Safety Evaluations

Safety evaluation ensures the LLM does not produce harmful, toxic, or policy-violating outputs.

### 3.1 Toxicity and Harmful Content

| Eval Pattern | Description | Tools |
|-------------|-------------|-------|
| **Toxicity classification** | Run outputs through a toxicity classifier; flag content exceeding threshold | Perspective API, OpenAI Moderation API, custom classifier |
| **Category-specific harmful content** | Test for specific harm categories: hate speech, self-harm, violence, sexual content, illegal activity advice | Multi-label classifier with per-category thresholds |
| **FinTech-specific harms** | Unauthorized financial advice, misleading product claims, discriminatory language about protected groups | Custom rubric with domain-specific categories |

### 3.2 Jailbreak Resistance

Test the system's resilience against adversarial prompts designed to bypass safety guardrails.

| Eval Pattern | Description | Dataset |
|-------------|-------------|---------|
| **Known jailbreak prompts** | Run a curated set of known jailbreak techniques against the system | DAN prompts, role-play attacks, encoding attacks, multi-turn manipulation |
| **Automated red-teaming** | Use an adversarial LLM to generate novel jailbreak attempts | Giskard LLM scan, custom red-team harness |
| **Guardrail bypass rate** | Fraction of adversarial inputs that successfully bypass guardrails | Custom adversarial test suite (see [Runtime Governance guardrails](../../03-runtime-governance/)) |

**Threshold guidance:** For customer-facing FinTech systems, jailbreak success rate must be < 1% on the standard adversarial test suite. For high-risk systems (e.g., autonomous credit decisions), target 0%.

### 3.3 Policy Compliance

Verify the LLM adheres to organizational and regulatory policies.

| Policy Area | Test Approach | Example |
|-------------|--------------|---------|
| No financial advice without disclaimer | Check all advisory outputs for required disclaimers | "This is general information, not personalized financial advice" |
| GDPR data minimization | Verify outputs do not expose unnecessary personal data | Test with inputs containing PII; verify PII is not echoed |
| Regulatory disclosure requirements | Verify mandatory disclosures are present in relevant outputs | EU AI Act Article 52 transparency obligations |

---

## 4. Instruction-Following Accuracy

Measures how well the LLM follows explicit instructions in system prompts, user messages, and tool specifications.

### 4.1 Evaluation Patterns

| Pattern | Description | Metric |
|---------|-------------|--------|
| **Format compliance** | Does the output match the requested format (JSON, markdown, bullet list)? | Binary pass/fail per output; aggregate compliance rate |
| **Constraint adherence** | Does the output respect explicit constraints (word count, tone, language, forbidden topics)? | Constraint violation rate across test set |
| **Multi-instruction following** | When given multiple instructions, does the model follow all of them? | Fraction of instructions followed per response |
| **Negation handling** | Does the model correctly handle "do not" instructions? | Negation violation rate |
| **System prompt fidelity** | Does the model maintain persona, scope boundaries, and behavioral rules across a multi-turn conversation? | Drift rate across conversation turns (measure at turn 1, 5, 10, 20) |

### 4.2 FinTech Example -- Customer Service Chatbot

```
System prompt: "You are a customer service agent for a Dutch bank. You must:
  1. Always respond in the same language the customer uses
  2. Never provide specific investment advice
  3. Always include a disclaimer when discussing interest rates
  4. Escalate to a human agent if the customer expresses distress"

Eval suite:
  - 50 test cases in Dutch -> verify all responses in Dutch
  - 50 test cases in English -> verify all responses in English
  - 30 investment-related questions -> verify no specific advice given
  - 20 interest rate queries -> verify disclaimer present
  - 15 emotional distress scenarios -> verify escalation triggered
```

---

## 5. Tool-Use Correctness Evaluation

Critical for agentic workflows where the LLM selects and invokes external tools (APIs, databases, calculators, internal services).

### 5.1 Evaluation Dimensions

| Dimension | Description | Metric |
|-----------|-------------|--------|
| **Tool selection accuracy** | Did the agent select the correct tool for the task? | Correct tool selected / total tool invocations |
| **Parameter extraction accuracy** | Were the tool parameters correctly extracted from the user's request? | Parameter match rate (exact match or semantic equivalence) |
| **Invocation sequence correctness** | For multi-step tasks, were tools invoked in the correct order? | Sequence match rate against expected plan |
| **Error handling** | When a tool returns an error, does the agent recover gracefully? | Recovery rate on injected tool errors |
| **Unnecessary tool use** | Does the agent avoid calling tools when the answer is available without them? | False tool invocation rate |

### 5.2 Evaluation Method

Create a tool-use test suite with scenarios that have known-correct tool invocation sequences:

```yaml
# Example: Tool-use eval scenario
scenario: "Customer asks for their account balance in EUR"
user_input: "What is my current balance?"
expected_tool_calls:
  - tool: "get_account_balance"
    parameters:
      account_id: "${customer_account_id}"
      currency: "EUR"
expected_not_called:
  - "transfer_funds"
  - "close_account"
evaluation:
  tool_selection: exact_match
  parameter_extraction: semantic_match
  response_uses_tool_result: true
```

### 5.3 Multi-Tool Orchestration

For complex agentic workflows involving multiple tool calls, evaluate the complete orchestration:

| Pattern | Description |
|---------|-------------|
| **Plan correctness** | Compare the agent's execution plan against expected steps |
| **Intermediate state validation** | After each tool call, verify the agent's internal state is consistent |
| **Goal achievement** | Did the full workflow accomplish the user's objective? |
| **Efficiency** | Were unnecessary or redundant tool calls made? |

---

## 6. Reasoning Trace Evaluation -- Monitoring Agent Spans

In agentic systems, the LLM produces a chain of reasoning steps (a "trace") that leads to actions. Each individual step within a trace is a **Span**. Evaluating these spans provides deep insight into agent behavior and is critical for debugging, compliance, and safety.

### 6.1 What Is a Span?

A Span represents a single unit of work in an agent's execution trace:

| Span Type | Description | Example |
|-----------|-------------|---------|
| **LLM call** | A single inference call to the language model | "Analyzing customer's loan eligibility request" |
| **Tool invocation** | A call to an external tool or API | "Calling credit_score_api with customer_id=12345" |
| **Retrieval** | A vector search or document lookup | "Retrieving loan policy documents from knowledge base" |
| **Decision** | A branching decision in the agent's logic | "Customer meets income threshold; proceeding to credit check" |
| **Guardrail check** | A safety or policy check on input or output | "Checking output for unauthorized financial advice" |

### 6.2 Span-Level Evaluation Patterns

| Pattern | What It Measures | Implementation |
|---------|-----------------|----------------|
| **Span latency** | Time taken by each span; identifies bottlenecks | Instrument spans with start/end timestamps; alert on P95 threshold breaches |
| **Span success rate** | Fraction of spans that complete without error | Track error rates per span type; set minimum success rate thresholds |
| **Reasoning coherence** | Does each reasoning span logically follow from the previous one? | LLM-as-judge evaluates coherence between consecutive spans |
| **Faithfulness per span** | Is each reasoning step grounded in available information? | Verify each span's claims against the context available at that point in the trace |
| **Decision audit** | At each decision span, was the right path taken? | Compare decision outcomes against labeled test scenarios |

### 6.3 Trace-Level Evaluation

Beyond individual spans, evaluate the complete trace as a whole:

| Metric | Description |
|--------|-------------|
| **Trace completeness** | Did the agent execute all expected spans for the task type? |
| **Trace efficiency** | Were there redundant or unnecessary spans? |
| **Goal alignment** | Does the final output align with the user's original intent? |
| **Safety throughout** | Were safety guardrails checked at all required points in the trace? |

### 6.4 Integration with Observability Platforms

Span-level evaluation ties directly into observability (see Section 10 below). Platforms like LangSmith, Arize Phoenix, Opik, and Langfuse capture traces and spans natively, enabling both real-time monitoring and offline evaluation.

---

## 7. Response Quality Metrics

General-purpose metrics for evaluating the quality of LLM-generated responses.

### 7.1 Core Quality Dimensions

| Dimension | Definition | Measurement Approach |
|-----------|-----------|---------------------|
| **Relevance** | Does the response address the user's question? | LLM-as-judge with relevance rubric; semantic similarity to expected topic |
| **Coherence** | Is the response internally consistent and well-structured? | LLM-as-judge; perplexity-based measures |
| **Completeness** | Does the response cover all aspects of the question? | Checklist-based: define required information elements, verify each is present |
| **Conciseness** | Is the response appropriately brief without losing essential information? | Length ratio (output length / optimal length); verbosity detection |
| **Tone appropriateness** | Does the response match the expected professional tone? | Sentiment/tone classifier; rubric-based LLM-as-judge |

### 7.2 Composite Quality Scores

Combine multiple dimensions into a single quality score for tracking over time:

```
overall_quality = w_relevance * relevance_score
               + w_coherence * coherence_score
               + w_completeness * completeness_score
               + w_conciseness * conciseness_score
               + w_tone * tone_score

# Example weights for a FinTech customer service chatbot:
# relevance=0.30, coherence=0.15, completeness=0.30, conciseness=0.10, tone=0.15
```

---

## 8. Automated Evaluation Patterns

### 8.1 LLM-as-Judge

Use a capable LLM to evaluate the output of the system under test. This is the most flexible automated evaluation pattern for LLM systems.

**Implementation guidelines:**

1. **Define a clear rubric:** The judge LLM needs explicit scoring criteria. Vague instructions produce noisy scores.
2. **Use structured output:** Request the judge to return JSON with score and reasoning.
3. **Calibrate with human labels:** Score a sample with human evaluators, then compare LLM-as-judge scores to establish correlation.
4. **Use a stronger model as judge:** The judge should be at least as capable as the system under test. Using GPT-4-class models to judge GPT-3.5-class outputs is valid; the reverse is not.
5. **Mitigate position bias:** When comparing two outputs, randomize presentation order.

```
# Example LLM-as-Judge prompt for faithfulness evaluation
You are evaluating whether an AI assistant's response is faithful to the
provided context. Score from 1-5:

5 - Every claim in the response is directly supported by the context
4 - Almost all claims are supported; minor unsupported details
3 - Most claims are supported but some significant unsupported claims
2 - Many claims are unsupported or contradicted by context
1 - The response largely fabricates information not in the context

Context: {context}
Response: {response}

Return JSON: {"score": <int>, "reasoning": "<explanation>"}
```

### 8.2 Semantic Similarity

Measure how semantically close the LLM output is to a reference answer using embedding-based similarity.

| Method | Description | Use Case |
|--------|-------------|----------|
| **Cosine similarity** | Compute cosine distance between embeddings of output and reference | Quick relevance check; coarse quality signal |
| **BERTScore** | Token-level embedding matching with precision, recall, F1 | More nuanced than cosine; captures partial matches |
| **Sentence-BERT** | Sentence-level embedding comparison | Best for comparing complete answers |

### 8.3 Factual Consistency

Verify that the LLM's output does not contradict known facts.

| Method | Description |
|--------|-------------|
| **NLI-based** | Use a Natural Language Inference model to check entailment between source and output |
| **Claim decomposition + verification** | Break output into atomic claims, verify each claim against a fact database |
| **Knowledge graph alignment** | Compare extracted entities and relationships against a structured knowledge base |

---

## 9. Specific Metrics Reference

### 9.1 Standard Metrics

| Metric | Type | What It Measures | When to Use |
|--------|------|-----------------|-------------|
| **ROUGE-L** | Reference-based | Longest common subsequence overlap | Summarization, extraction tasks |
| **ROUGE-1/2** | Reference-based | Unigram/bigram overlap | Quick content overlap check |
| **BERTScore** | Reference-based | Semantic similarity via embeddings | When semantic equivalence matters more than exact wording |
| **BLEU** | Reference-based | N-gram precision with brevity penalty | Translation tasks (less useful for general LLM eval) |
| **Perplexity** | Reference-free | Model confidence in generated text | Fluency measurement; anomaly detection |

### 9.2 LLM-Specific Metrics

| Metric | Type | What It Measures | When to Use |
|--------|------|-----------------|-------------|
| **G-Eval** | LLM-as-judge | Multi-dimensional quality via chain-of-thought judge | General quality assessment across any dimension |
| **RAGAS suite** | Mixed | Faithfulness, answer relevancy, context relevancy, context recall | RAG pipeline evaluation |
| **TruLens Groundedness** | LLM-as-judge | Whether claims are supported by retrieved context | RAG and knowledge-grounded systems |
| **Custom rubric score** | LLM-as-judge | Domain-specific quality dimensions (e.g., regulatory compliance, empathy, accuracy) | When standard metrics do not capture domain needs |

### 9.3 Designing Custom Rubrics

For FinTech applications, standard metrics are insufficient. Create custom rubrics that encode domain requirements:

```yaml
# Example: Custom rubric for a loan explanation generator
rubric_name: "Loan Explanation Quality"
dimensions:
  - name: accuracy
    weight: 0.35
    scale: 1-5
    criteria: "All stated terms (rate, duration, fees) match the actual loan offer"
  - name: completeness
    weight: 0.25
    scale: 1-5
    criteria: "Explanation covers rate, total cost, repayment schedule, and early repayment terms"
  - name: clarity
    weight: 0.20
    scale: 1-5
    criteria: "A non-expert consumer could understand the explanation without financial background"
  - name: regulatory_compliance
    weight: 0.20
    scale: 1-5
    criteria: "Required disclosures under EU Consumer Credit Directive are present"
```

---

## 10. Setting Up Eval Suites by AI Product Type

### 10.1 Customer Service Chatbot

| Eval Category | Key Patterns | Priority |
|--------------|-------------|----------|
| Hallucination | Faithfulness scoring, knowledge boundary adherence | Critical |
| Safety | Toxicity, jailbreak resistance, policy compliance | Critical |
| Instruction following | System prompt fidelity, constraint adherence | High |
| Response quality | Relevance, completeness, tone | High |
| Tool use | Tool selection accuracy (if tools are available) | Medium |

### 10.2 Autonomous Decision Agent (e.g., Fraud Detection Explainer)

| Eval Category | Key Patterns | Priority |
|--------------|-------------|----------|
| Faithfulness | Claim-level faithfulness, zero hallucination tolerance | Critical |
| Tool use | Tool selection, parameter accuracy, sequence correctness | Critical |
| Reasoning trace | Span coherence, decision audit, trace completeness | Critical |
| Safety | Policy compliance, no unauthorized actions | Critical |
| Fairness | Demographic parity in explanations (see [Bias and Fairness Evals](bias-and-fairness-evals.md)) | High |

### 10.3 RAG-Powered Knowledge Assistant

| Eval Category | Key Patterns | Priority |
|--------------|-------------|----------|
| Retrieval quality | Context relevancy, context recall (RAGAS) | Critical |
| Faithfulness | Groundedness, citation accuracy | Critical |
| Hallucination | Knowledge boundary adherence (says "I don't know" appropriately) | Critical |
| Response quality | Relevance, coherence, completeness | High |
| Safety | No harmful content, GDPR compliance in responses | High |

---

## 11. Agentic-Specific Evaluation Patterns

### 11.1 Task Completion Evaluation

For agents that perform multi-step tasks on behalf of users:

| Metric | Description |
|--------|-------------|
| **Task success rate** | Fraction of tasks completed correctly end-to-end |
| **Partial completion score** | For failed tasks, how much of the task was completed correctly? |
| **User intent alignment** | Did the agent's actions match what the user actually wanted? |
| **Side effect detection** | Did the agent take any unintended actions while completing the task? |

### 11.2 Multi-Step Planning Evaluation

| Metric | Description |
|--------|-------------|
| **Plan validity** | Is the generated plan a valid sequence of actions that could achieve the goal? |
| **Plan optimality** | Is the plan efficient, or does it contain unnecessary steps? |
| **Replanning ability** | When a step fails, can the agent replan effectively? |
| **Constraint satisfaction** | Does the plan respect all specified constraints (permissions, time limits, budget)? |

### 11.3 Delegation and Escalation Evaluation

For multi-agent systems and human-in-the-loop workflows:

| Metric | Description |
|--------|-------------|
| **Escalation precision** | When the agent escalates, was escalation actually needed? |
| **Escalation recall** | Of all cases that needed escalation, how many did the agent correctly escalate? |
| **Delegation correctness** | When delegating to a sub-agent, was the right sub-agent selected with correct context? |
| **Handoff quality** | Does the escalation include sufficient context for the human or sub-agent to continue? |

---

## 12. Integration with Observability Platforms

Evaluations are not a one-time development activity. They run continuously in production through observability platforms.

### 12.1 Platform Comparison

| Platform | Strengths | Best For |
|----------|----------|----------|
| **LangSmith** | Deep LangChain integration, trace visualization, annotation queues, eval datasets | Teams using LangChain/LangGraph for agent orchestration |
| **Arize Phoenix** | Open-source, strong drift detection, embedding visualization, LLM tracing | Teams wanting self-hosted observability with ML monitoring roots |
| **Opik** | Open-source (Comet), lightweight tracing, eval integration, prompt versioning | Teams wanting a focused LLM evaluation and tracing tool |
| **Langfuse** | Open-source, model-agnostic tracing, cost tracking, prompt management | Teams wanting open-source observability across multiple LLM providers |

### 12.2 Integration Pattern

```
Development (CI/CD)                 Production (Runtime)
+------------------+                +------------------+
| Eval suite runs  |                | Observability    |
| on every commit  |   Same eval   | platform captures|
| against test     | -- metrics -->| live traces and  |
| datasets         |   definitions | runs evals on    |
|                  |                | production data  |
+------------------+                +------------------+
        |                                    |
        v                                    v
+------------------+                +------------------+
| Pre-deployment   |                | Continuous online|
| gate             |                | evaluation       |
| (blocking)       |                | (alerting)       |
+------------------+                +------------------+
```

See [Continuous Online Evaluation](../../03-runtime-governance/evaluations/continuous-online-evaluation.md) for the production monitoring side of this pattern.

---

## 13. FinTech Worked Examples

### 13.1 Evaluating a Customer Service Chatbot

**System:** A Dutch bank's customer service chatbot that answers questions about accounts, transactions, and products using a RAG pipeline over the bank's knowledge base.

**Eval suite structure:**

| Eval | Pattern | Metric | Threshold | Blocking |
|------|---------|--------|-----------|----------|
| Faithfulness | Claim-level faithfulness against retrieved docs | RAGAS faithfulness | >= 0.95 | Yes |
| Hallucination boundary | "I don't know" on out-of-scope questions | Boundary adherence rate | >= 0.90 | Yes |
| Toxicity | Perspective API toxicity score | Max toxicity | < 0.10 | Yes |
| Jailbreak resistance | Standard adversarial prompt suite (200 prompts) | Bypass rate | < 0.01 | Yes |
| Language following | Responds in customer's language | Language match rate | >= 0.98 | Yes |
| Disclaimer compliance | Interest rate queries include disclaimers | Disclaimer presence rate | 1.00 | Yes |
| Response quality | Custom rubric (relevance, clarity, completeness) | Average score | >= 3.5/5 | No |
| Latency | Time to first token | P95 TTFT | < 2s | Yes |

### 13.2 Evaluating a Credit Explanation Generator

**System:** An agent that generates plain-language explanations for credit decisions, satisfying EU Consumer Credit Directive Article 18 requirements.

**Eval suite structure:**

| Eval | Pattern | Metric | Threshold | Blocking |
|------|---------|--------|-----------|----------|
| Factor accuracy | Every stated factor matches the actual credit model output | Claim-level faithfulness | 1.00 | Yes |
| Completeness | All rejection/acceptance factors are mentioned | Factor coverage | 1.00 | Yes |
| Fabrication | No invented factors or fabricated numbers | Hallucination rate | 0.00 | Yes |
| Clarity | Non-expert understandability | Custom rubric clarity score | >= 4/5 | Yes |
| Fairness | Explanation quality parity across demographics | Quality score parity | Diff <= 0.5 across groups | Yes |
| Regulatory compliance | Required regulatory disclosures present | Compliance rate | 1.00 | Yes |
| Tone | Professional, empathetic, non-judgmental | Tone rubric score | >= 4/5 | No |

---

## Cross-References

- **Eval-Driven Development:** [eval-driven-development.md](eval-driven-development.md) -- the overarching methodology that uses these eval patterns
- **Bias and Fairness Evals:** [bias-and-fairness-evals.md](bias-and-fairness-evals.md) -- fairness-specific evaluation patterns (complements this document)
- **Acceptance Criteria Automation:** [acceptance-criteria-automation.yaml](acceptance-criteria-automation.yaml) -- template for encoding these patterns as machine-executable criteria
- **Eval Gate Integration:** [eval-gate-integration.md](eval-gate-integration.md) -- wiring these eval patterns into CI/CD pipelines
- **AI Quality Metrics Catalog:** [../../01-discovery-governance/evaluations/ai-quality-metrics-catalog.md](../../01-discovery-governance/evaluations/ai-quality-metrics-catalog.md) -- broader metrics catalog for selecting evaluation metrics during Discovery
- **Continuous Online Evaluation:** [../../03-runtime-governance/evaluations/continuous-online-evaluation.md](../../03-runtime-governance/evaluations/continuous-online-evaluation.md) -- running these eval patterns in production
- **Pre-Deployment Gate:** [../checklists/pre-deployment-gate.yaml](../checklists/pre-deployment-gate.yaml) -- the gate that requires eval evidence
- **Model Card Template:** [../templates/model-card.md](../templates/model-card.md) -- where eval results are documented
- **TDD for AI Products:** [../guides/tdd-for-ai-products.md](../guides/tdd-for-ai-products.md) -- how to integrate these eval patterns into test-driven development workflows

---

*Last updated: 2026-02-28*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
