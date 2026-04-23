# Output Validation Patterns

## Purpose

This guide catalogs common patterns for validating LLM outputs in regulated FinTech agentic workflows. LLM outputs are probabilistic, and in financial services, every output carries potential regulatory, financial, and reputational risk. Output validation is the final line of defense before an agent's response reaches a customer, triggers a transaction, or feeds into a downstream system.

This guide provides a taxonomy of validation types, concrete implementation patterns, a decision tree for selecting the right validation strategy, and guidance on combining multiple validators into a coherent validation pipeline. It complements the tool-specific integration guides for [Guardrails AI](integrating-guardrails-ai.md) and [NeMo Guardrails](integrating-nemo-guardrails.md) by providing the conceptual framework that informs which validators to apply and when.

## When to Use

- When designing the output validation pipeline for a new agent
- When selecting validators for a specific agent action or response type
- When reviewing the completeness of an existing validation pipeline
- When a validation gap is discovered through a safety incident or red-team exercise
- When building custom validators and needing to classify their validation type
- When training new engineers on output validation best practices

## Who Is Responsible

| Role | R/A/C/I | Responsibility |
|------|---------|---------------|
| **AI/ML Engineer** | Responsible | Selects and implements validation patterns per agent |
| **Model Owner** | Accountable | Approves the validation strategy and coverage for each agent |
| **MLOps / Platform Engineer** | Responsible | Deploys validation pipeline; monitors validation performance metrics |
| **Compliance Officer (2nd Line)** | Reviewer | Validates that regulatory validation patterns are in place |
| **Product Manager** | Consulted | Defines quality requirements that validation patterns enforce |
| **AI Governance Committee** | Approver | Approves validation strategies for high-risk agents |

## Regulatory Basis

- **EU AI Act Article 15** -- Accuracy, robustness, and cybersecurity for high-risk AI
- **EU AI Act Article 9** -- Risk management measures including output controls
- **EU AI Act Article 13** -- Transparency requirements influencing output format
- **MiFID II Articles 24-25** -- Accuracy and appropriateness of financial information
- **PSD2 Article 97** -- Transaction integrity and authentication
- **GDPR Article 25** -- Data protection by design (output-level PII controls)
- **SAFEST T-01** -- Transparency; output must be interpretable and verifiable
- **SAFEST S-13** -- Fallback when output validation fails
- **DNB Good Practice** -- Output quality monitoring for AI/ML systems

---

## 1. Validation Type Taxonomy

### 1.1 Six Validation Types

| # | Validation Type | What It Checks | Risk If Missing | Tools |
|---|----------------|---------------|-----------------|-------|
| 1 | **Structural** | Output conforms to expected format and schema (JSON, fields, types) | Downstream system failures; parsing errors; data corruption | Guardrails AI (Pydantic), JSON Schema, custom parsers |
| 2 | **Semantic** | Output meaning aligns with the user's intent and the agent's task | Irrelevant responses; customer frustration; task failure | LLM-as-judge, intent classifiers, embedding similarity |
| 3 | **Factual** | Output claims are grounded in authoritative data sources | Hallucination; misinformation; wrong account data; regulatory breach | Knowledge base lookup, RAG verification, fact-checking models |
| 4 | **Safety** | Output does not contain harmful, offensive, or prohibited content | Customer harm; regulatory violation; reputational damage | Content classifiers, NeMo Guardrails, toxicity models |
| 5 | **Regulatory** | Output complies with applicable regulations (disclaimers, advice boundaries, data protection) | Regulatory sanctions; fines; licence revocation | Pattern matching, compliance rules engine, Guardrails AI custom validators |
| 6 | **Format** | Output meets presentation requirements (length, tone, language, style) | Poor customer experience; brand inconsistency | Length validators, language detection, style classifiers |

---

## 2. Structural Validation

### 2.1 Pattern: JSON Schema Validation

**Problem:** Agent returns a structured response (payment confirmation, balance inquiry, transaction list) but the output is malformed, missing required fields, or contains invalid data types.

**Solution:** Define a JSON schema or Pydantic model. Validate every structured output against it before delivery.

```python
# Example: Payment confirmation schema
from pydantic import BaseModel, Field
from typing import Literal

class PaymentConfirmation(BaseModel):
    transaction_id: str = Field(min_length=10, max_length=30)
    amount: float = Field(gt=0, le=50000)
    currency: Literal["EUR", "USD", "GBP", "CHF"]
    beneficiary_name: str = Field(min_length=2, max_length=100)
    beneficiary_iban: str = Field(pattern=r"^[A-Z]{2}\d{2}[A-Z0-9]+$")
    status: Literal["pending", "processing", "completed", "failed"]
    timestamp: str  # ISO 8601
```

**When to use:** Every time the agent produces structured data that will be displayed to a customer or consumed by a downstream system.

**On failure:** Re-ask the LLM (max 2 attempts), then activate fallback.

### 2.2 Pattern: Field-Level Type Enforcement

**Problem:** LLM returns an amount as a string ("five hundred euros") instead of a number (500.00).

**Solution:** Type coercion layer that converts LLM outputs to expected types with validation.

| Field Type | Validation Rule | Example |
|-----------|----------------|---------|
| Currency amount | Numeric, > 0, max 2 decimal places | `500.00` not `"five hundred"` |
| IBAN | ISO 13616 format with check digit validation | `NL91ABNA0417164300` |
| Date | ISO 8601 format | `2026-03-01T10:00:00Z` |
| Currency code | ISO 4217, 3 uppercase letters | `EUR` not `euros` |
| Percentage | Numeric, 0-100, max 2 decimal places | `3.50` not `"three and a half percent"` |

---

## 3. Semantic Validation

### 3.1 Pattern: Intent Alignment Check

**Problem:** The user asks about their account balance, but the agent responds with information about loan products.

**Solution:** Compare the classified intent of the user's query with the content of the agent's response.

```python
def validate_intent_alignment(
    user_message: str,
    agent_response: str,
    intent_classifier
) -> bool:
    """Check that the response addresses the user's intent."""
    user_intent = intent_classifier.classify(user_message)
    response_topic = intent_classifier.classify(agent_response)

    alignment_score = compute_alignment(user_intent, response_topic)

    if alignment_score < 0.70:
        return False  # Response does not address the user's question
    return True
```

**When to use:** Conversational agents where responses are free-text (not structured data).

### 3.2 Pattern: Embedding Similarity Threshold

**Problem:** The agent's response drifts from the topic without being detectably off-topic by keyword analysis alone.

**Solution:** Embed both the user query and agent response. If cosine similarity falls below a threshold, flag for review.

| Threshold | Interpretation | Action |
|-----------|---------------|--------|
| > 0.80 | Strong alignment | Pass |
| 0.60 - 0.80 | Moderate alignment | Pass with monitoring flag |
| < 0.60 | Weak alignment | Trigger re-generation or escalation |

---

## 4. Factual Validation (Grounding)

### 4.1 Pattern: Source-Grounded Response Verification

**Problem:** Agent claims the customer's balance is EUR 5,230 without actually querying the account API.

**Solution:** Every factual claim in the output must be traceable to a data source accessed during the current interaction.

```python
def validate_grounding(
    response: str,
    retrieved_context: list[str],
    tool_results: dict
) -> dict:
    """Verify that factual claims in the response are grounded in sources."""
    claims = extract_factual_claims(response)

    grounded = []
    ungrounded = []

    for claim in claims:
        if is_supported_by(claim, retrieved_context) or \
           is_supported_by(claim, tool_results):
            grounded.append(claim)
        else:
            ungrounded.append(claim)

    return {
        "grounding_score": len(grounded) / max(len(claims), 1),
        "ungrounded_claims": ungrounded,
        "passed": len(ungrounded) == 0
    }
```

**When to use:** Any agent that provides account-specific data, financial figures, product details, or regulatory information.

### 4.2 Pattern: Freshness Validation

**Problem:** Agent provides interest rate data that is 48 hours old.

**Solution:** Attach freshness metadata to data sources. Validate that cited data is within freshness requirements.

| Data Type | Maximum Staleness | Source |
|-----------|------------------|--------|
| Account balance | 30 seconds | Core banking API |
| FX rate | 15 minutes | FX rate service |
| Interest rate | 24 hours | Product catalog |
| Product terms | 7 days | Document management system |
| Regulatory information | 30 days | Compliance knowledge base |

---

## 5. Safety Validation

### 5.1 Pattern: Multi-Layer Content Filtering

**Problem:** Agent generates content that is harmful, offensive, manipulative, or inappropriate.

**Solution:** Apply multiple safety filters in sequence, each targeting a different risk category.

```
Agent Output
    |
    v
Layer 1: Keyword blocklist (fast; catches obvious violations)
    |
    v
Layer 2: Toxicity classifier (model-based; catches nuanced violations)
    |
    v
Layer 3: Financial manipulation detector (domain-specific; catches pressure tactics)
    |
    v
Layer 4: PII leakage scanner (catches accidental data exposure)
    |
    v
Validated Output
```

**Latency budget:** Layer 1 (< 5 ms) + Layer 2 (50-200 ms) + Layer 3 (10-50 ms) + Layer 4 (5-15 ms) = total < 300 ms.

### 5.2 Pattern: Differential Safety for Action Types

Not all outputs carry equal risk. Apply safety validation proportional to the action type:

| Action Type | Safety Validation Level | Validators Applied |
|------------|------------------------|-------------------|
| Informational response | Standard | Content filter, PII scanner |
| Product comparison | Enhanced | Content filter, PII scanner, compliance checker, advice boundary |
| Transaction confirmation | Maximum | All validators + amount validation + IBAN validation + schema validation |
| Complaint response | Enhanced | Content filter, empathy check, escalation path validator |
| Regulatory disclosure | Maximum | Compliance checker, mandatory disclaimer verifier |

---

## 6. Regulatory Validation

### 6.1 Pattern: Mandatory Disclaimer Injection

**Problem:** Agent discusses a savings product but does not include the required risk disclaimer.

**Solution:** Topic-triggered disclaimer injection that appends required regulatory text.

| Trigger Topic | Required Disclaimer | Regulation |
|--------------|--------------------|-----------  |
| Any financial product | "This is general information and does not constitute personal financial advice." | MiFID II |
| Investment products | "Investments carry risk. You may lose some or all of your invested capital." | MiFID II Art 24 |
| Insurance products | "Please review the Key Information Document before making a decision." | PRIIPs |
| Conversation opening | "I am an AI assistant for [Company Name]." | EU AI Act Art 52 |
| Credit products | "Borrowing money costs money." | Consumer Credit Directive |

### 6.2 Pattern: Advice Boundary Enforcement

**Problem:** Agent inadvertently provides personalized financial advice.

**Solution:** Scan output for advisory language patterns before delivery.

```python
ADVICE_PATTERNS = [
    r"(I |we )?(recommend|suggest|advise)",
    r"you should (buy|sell|invest|open|close|switch)",
    r"based on your (profile|situation|circumstances|risk)",
    r"guaranteed (return|profit|income|yield)",
    r"(risk-free|no risk|cannot lose|completely safe)",
]

def check_advice_boundary(output: str) -> bool:
    for pattern in ADVICE_PATTERNS:
        if re.search(pattern, output, re.IGNORECASE):
            return False  # Contains advisory language
    return True
```

### 6.3 Pattern: Audit Trail Completeness Check

**Problem:** Agent completes a transaction but the audit trail is incomplete, creating a regulatory gap.

**Solution:** Validate that every consequential action has a complete audit record.

| Required Audit Field | Description | Validation |
|---------------------|-------------|-----------|
| `interaction_id` | Unique session identifier | Non-null, UUID format |
| `agent_id` | Agent that performed the action | Must match registry |
| `action_type` | What the agent did | From allowed actions list |
| `timestamp` | When the action was performed | ISO 8601, within last 60 seconds |
| `customer_id` | Who the action was performed for | Non-null, authenticated |
| `input_hash` | Hash of the user's request | SHA-256 |
| `output_hash` | Hash of the agent's response | SHA-256 |
| `model_version` | LLM model version used | Non-null, matches registry |
| `confidence_score` | Agent's confidence in the action | 0.0-1.0 |
| `approval_status` | HITL approval status if applicable | Approved / Auto / N/A |

---

## 7. Format Validation

### 7.1 Pattern: Response Length Control

**Problem:** Agent produces a 2,000-word response for a simple balance inquiry.

**Solution:** Enforce response length limits per response type.

| Response Type | Max Length | On Violation |
|--------------|-----------|-------------|
| Balance inquiry | 200 characters | Truncate with "Would you like more details?" |
| Transaction list | 1,000 characters | Paginate with "I can show more transactions. Continue?" |
| Product information | 500 characters | Summarize with link to full details |
| General conversation | 500 characters | Truncate naturally |
| Error / fallback | 200 characters | Hard limit |

### 7.2 Pattern: Language and Tone Validation

**Problem:** Agent responds in a language the customer did not request, or uses an inappropriate tone.

**Solution:** Validate output language matches the session language, and tone matches brand guidelines.

| Check | Validation | Action |
|-------|-----------|--------|
| Language match | Detect output language; compare to session language | Re-generate if mismatch |
| Formality level | Classify tone (formal/informal/neutral) | Must match brand guidelines (formal for banking) |
| Empathy in complaints | Detect whether complaint responses show empathy | Flag for review if empathy score < threshold |
| Clarity score | Readability analysis (Flesch-Kincaid or equivalent) | Flag if reading level > grade 10 |

---

## 8. Decision Tree: Selecting Validation Strategy

Use this decision tree to determine which validation patterns to apply for a given agent output:

```
START: What type of output is the agent producing?
  |
  +-- Structured data (JSON, records, confirmations)
  |     |
  |     +-> Apply: Structural + Factual + Regulatory + Safety
  |     |   Tools: Guardrails AI (Pydantic schema), custom validators
  |     |
  |     +-- Does it contain financial amounts?
  |           +-- Yes -> Add: Amount validator, currency validator
  |           +-- No  -> Standard schema validation sufficient
  |
  +-- Free-text response (conversational)
  |     |
  |     +-> Apply: Semantic + Safety + Regulatory + Format
  |     |   Tools: NeMo Guardrails (topical/safety), content classifier
  |     |
  |     +-- Does it discuss financial products?
  |     |     +-- Yes -> Add: Advice boundary check, mandatory disclaimers
  |     |     +-- No  -> Standard content safety sufficient
  |     |
  |     +-- Is it responding to a complaint?
  |           +-- Yes -> Add: Empathy validation, escalation path check
  |           +-- No  -> Standard format validation sufficient
  |
  +-- Action / Transaction trigger
        |
        +-> Apply: ALL validation types (Structural + Semantic + Factual
        |          + Safety + Regulatory + Format)
        |   Tools: Guardrails AI + NeMo Guardrails + custom validators
        |
        +-- Is the transaction value above the HITL threshold?
              +-- Yes -> Add: Human approval gate before execution
              +-- No  -> Automated validation sufficient
```

### 8.1 Minimum Validation by Risk Tier

| Risk Tier | Minimum Required Validation Types | Example Agent |
|-----------|----------------------------------|---------------|
| **High** | All 6 types (Structural + Semantic + Factual + Safety + Regulatory + Format) | Payments Agent, KYC Agent, Treasury Agent |
| **Limited** | Safety + Regulatory + Format + (Structural or Semantic based on output type) | Cash Flow Agent, FAQ Bot |
| **Minimal** | Safety + Format | Internal analytics summarizer |

---

## 9. Validation Pipeline Architecture

### 9.1 Pipeline Stages

```
LLM Output
    |
    v
+-------------------------------+
| STAGE 1: STRUCTURAL           |
| - JSON schema validation      |
| - Type enforcement            |
| - Required field check        |
| Latency: < 10 ms             |
+-------------------------------+
    | (pass)
    v
+-------------------------------+
| STAGE 2: SAFETY               |
| - Content filter (toxicity)   |
| - PII leakage scan           |
| - Prohibited language check   |
| Latency: < 200 ms            |
+-------------------------------+
    | (pass)
    v
+-------------------------------+
| STAGE 3: FACTUAL              |
| - Grounding verification     |
| - Source freshness check      |
| - Hallucination detection     |
| Latency: < 300 ms            |
+-------------------------------+
    | (pass)
    v
+-------------------------------+
| STAGE 4: REGULATORY           |
| - Disclaimer injection       |
| - Advice boundary check      |
| - Audit trail completeness   |
| Latency: < 50 ms             |
+-------------------------------+
    | (pass)
    v
+-------------------------------+
| STAGE 5: FORMAT               |
| - Length enforcement          |
| - Language validation         |
| - Tone check                 |
| Latency: < 20 ms             |
+-------------------------------+
    | (pass)
    v
Validated Output -> Deliver to Customer

    | (any stage fails)
    v
Failure Handler:
  - Re-ask LLM (max 2 attempts)
  - If still fails: activate fallback (see fallback-procedure.md)
  - Log failure to observability platform
  - Alert if failure rate > threshold
```

### 9.2 Pipeline Performance Budget

| Stage | Latency Target (P95) | Can Run Async? |
|-------|---------------------|----------------|
| Structural | < 10 ms | No (must complete before delivery) |
| Safety | < 200 ms | No (must complete before delivery) |
| Factual | < 300 ms | Partially (grounding check sync; detailed verification async) |
| Regulatory | < 50 ms | No (must complete before delivery) |
| Format | < 20 ms | No (must complete before delivery) |
| **Total pipeline** | **< 500 ms** | -- |

---

## 10. Monitoring Validation Effectiveness

### 10.1 Key Metrics

| Metric | Definition | Alert Threshold | Dashboard Location |
|--------|-----------|-----------------|-------------------|
| **Validation pass rate** | % of outputs passing all validators | < 95% over rolling 1h | Guardrail Health dashboard |
| **Per-stage failure rate** | % of outputs failing at each pipeline stage | Spike > 2x baseline | Guardrail Health dashboard |
| **Re-ask rate** | % of outputs requiring LLM re-generation | > 10% over rolling 1h | Agent KPI panel |
| **Fallback activation rate** | % of outputs that failed all re-asks and triggered fallback | > 2% over rolling 4h | Agent Health panel |
| **False positive rate** | % of blocked outputs that were actually valid (from human review) | > 5% in monthly sample | Monthly review report |
| **Validation latency P95** | 95th percentile total validation pipeline time | > 500 ms | Performance dashboard |
| **Bypass rate** | % of invalid outputs that passed all validators (from red-teaming) | Any non-zero | Red-team report |

### 10.2 Review Cadence

| Activity | Frequency | Owner | Output |
|----------|-----------|-------|--------|
| **Validation metrics dashboard review** | Daily | On-Call Engineer | Spot anomalies; investigate spikes |
| **False positive sample review** | Weekly | AI/ML Engineer | Tune validators to reduce false positives |
| **Validation coverage audit** | Monthly | Model Owner + Compliance | Verify all required validation types are active |
| **Validator performance optimization** | Monthly | MLOps Engineer | Identify slow validators; optimize latency |
| **Red-team bypass testing** | Quarterly | Security / AI Red Team | Identify validation gaps; add new test cases |
| **Validation strategy review** | Quarterly | Model Owner + AI Governance Committee | Assess whether validation patterns match current risk profile |

---

## Cross-References

- **Integrating Guardrails AI:** [integrating-guardrails-ai.md](integrating-guardrails-ai.md) -- implementation guide for structured output validation
- **Integrating NeMo Guardrails:** [integrating-nemo-guardrails.md](integrating-nemo-guardrails.md) -- implementation guide for conversational safety rails
- **Safety Policy Definition:** [../templates/safety-policy-definition.md](../templates/safety-policy-definition.md) -- safety policies that validation patterns enforce
- **Guardrail Specification:** [../templates/guardrail-specification.yaml](../templates/guardrail-specification.yaml) -- YAML specification for guardrail configuration
- **Customer-Facing Agent Safety:** [../agentic-workflows/customer-facing-agent-safety.md](../agentic-workflows/customer-facing-agent-safety.md) -- safety requirements that validation implements
- **Fallback Procedure:** [../templates/fallback-procedure.md](../templates/fallback-procedure.md) -- activated when validation fails beyond re-ask limits
- **Agent Fleet Operations:** [../agentic-workflows/agent-fleet-operations.md](../agentic-workflows/agent-fleet-operations.md) -- dashboard integration for validation metrics
- **Continuous Online Evaluation:** [../evaluations/continuous-online-evaluation.md](../evaluations/continuous-online-evaluation.md) -- monitoring infrastructure for validation metrics
- **Traceability with LangChain:** [../../04-operational-governance/guides/traceability-with-langchain.md](../../04-operational-governance/guides/traceability-with-langchain.md) -- observability platform for validation event logging
- **Glossary:** [../../05-cross-cutting/glossary.md](../../05-cross-cutting/glossary.md) -- definitions for structural validation, grounding, hallucination, semantic validation

---

*Last updated: 2026-03-01* / *Version: 1.0* / *Classification: Internal / Regulatory Preparation*
