# Integrating Guardrails AI

## Purpose

This guide provides a practical, step-by-step approach to integrating [Guardrails AI](https://www.guardrailsai.com/) into FinTech agentic workflows for output validation. While NVIDIA NeMo Guardrails (see companion guide [integrating-nemo-guardrails.md](integrating-nemo-guardrails.md)) excels at conversational flow control and topical boundaries, Guardrails AI specializes in **structured output validation** -- ensuring that LLM-generated outputs conform to expected schemas, data types, content policies, and domain-specific rules.

In regulated financial services, LLM outputs that are structurally malformed, contain invalid financial data, or fail compliance checks can cause direct customer harm, regulatory violations, and financial loss. Guardrails AI provides a programmatic layer that validates, corrects, and enforces quality standards on every LLM output before it reaches the customer or downstream system.

## When to Use

- When an agent produces structured outputs (JSON, transaction records, compliance reports)
- When output must conform to a specific data schema (amount, currency, IBAN format)
- When content safety validation is needed on generated text
- When PII must be detected and handled in LLM outputs
- When domain-specific validation rules are needed (FinTech, regulatory)
- When building custom validators for business logic

## Who Is Responsible

| Role | R/A/C/I | Responsibility |
|------|---------|---------------|
| **AI/ML Engineer** | Responsible | Implements Guard definitions, validators, and pipeline integration |
| **Model Owner** | Accountable | Approves validator configuration and validation thresholds |
| **MLOps / Platform Engineer** | Responsible | Deploys and monitors Guardrails AI in the agent pipeline |
| **Compliance Officer (2nd Line)** | Reviewer | Validates that validators enforce regulatory requirements |
| **Product Manager** | Consulted | Defines quality requirements that validators must enforce |

## Regulatory Basis

- **EU AI Act Article 15** -- Accuracy requirements for high-risk AI systems
- **EU AI Act Article 9** -- Risk management measures including output controls
- **MiFID II Articles 24-25** -- Accuracy requirements for financial product information
- **PSD2 Article 97** -- Strong customer authentication and transaction integrity
- **GDPR Article 25** -- Data protection by design; output-level PII controls
- **SAFEST T-01** -- Transparency of AI system outputs to end users
- **SAFEST S-13** -- Fallback when output validation fails

---

## 1. What Guardrails AI Does

Guardrails AI provides three core capabilities:

| Capability | Description | FinTech Application |
|-----------|-------------|---------------------|
| **Guard** | A wrapper around LLM calls that intercepts outputs and runs validators | Wrap every agent LLM call with a Guard that validates before delivery |
| **Validators** | Reusable validation functions that check specific output properties | Schema validation, IBAN format, amount ranges, content safety |
| **Re-asking** | When validation fails, automatically re-prompts the LLM with correction guidance | Agent self-corrects invalid outputs without human intervention |

### Guardrails AI vs. NeMo Guardrails

| Dimension | Guardrails AI | NeMo Guardrails |
|-----------|--------------|-----------------|
| **Strength** | Structured output validation, schema enforcement | Conversational flow control, topical boundaries |
| **Rule language** | Python validators + RAIL XML/JSON specs | Colang (conversational DSL) |
| **Correction** | Re-asking with error context | Alternative response generation |
| **Best for** | Data validation, format compliance, PII detection | Jailbreak prevention, topic control, safety rails |
| **Use together** | NeMo for input/conversation rails; Guardrails AI for output validation |

---

## 2. Installation and Setup

### 2.1 Installation

```bash
pip install guardrails-ai
```

For production, pin the version:

```bash
pip install guardrails-ai==0.5.13
```

### 2.2 Install Validators from the Hub

Guardrails AI provides a hub of pre-built validators. Install validators relevant to FinTech:

```bash
guardrails hub install hub://guardrails/valid_json
guardrails hub install hub://guardrails/detect_pii
guardrails hub install hub://guardrails/toxic_language
guardrails hub install hub://guardrails/regex_match
guardrails hub install hub://guardrails/valid_length
```

### 2.3 Project Structure

```
guardrails_config/
  guards/
    payment_response_guard.py      # Guard for payment agent outputs
    balance_response_guard.py      # Guard for balance inquiry outputs
    general_response_guard.py      # Guard for general customer responses
  validators/
    iban_validator.py              # Custom: IBAN format validation
    amount_validator.py            # Custom: financial amount validation
    compliance_statement.py        # Custom: regulatory compliance checks
    financial_advice_detector.py   # Custom: detects unauthorized advice
  schemas/
    payment_confirmation.json      # JSON schema for payment responses
    balance_inquiry.json           # JSON schema for balance responses
    transaction_record.json        # JSON schema for transaction data
  tests/
    test_validators.py             # Unit tests for custom validators
    test_guards.py                 # Integration tests for guard definitions
```

---

## 3. Guard Definition

A Guard wraps an LLM call and applies validators to the output.

### 3.1 Basic Guard Structure

```python
from guardrails import Guard
from guardrails.hub import ValidJson, DetectPII, ToxicLanguage

# Define a Guard for general customer responses
general_guard = Guard(
    name="general_response_guard",
    description="Validates customer-facing agent responses for safety and quality",
).use_many(
    ValidJson(on_fail="reask"),
    DetectPII(
        pii_entities=["CREDIT_CARD", "IBAN", "EMAIL_ADDRESS", "PHONE_NUMBER"],
        on_fail="fix"  # Automatically mask detected PII
    ),
    ToxicLanguage(
        threshold=0.8,
        on_fail="reask"
    ),
)
```

### 3.2 Guard with JSON Schema Validation

For structured outputs (common in FinTech agents), define a JSON schema:

```python
from guardrails import Guard
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class PaymentConfirmation(BaseModel):
    """Schema for payment confirmation output."""
    transaction_id: str = Field(
        description="Unique transaction reference",
        min_length=10,
        max_length=30
    )
    amount: float = Field(
        description="Payment amount",
        gt=0,
        le=50000  # Maximum single payment limit
    )
    currency: str = Field(
        description="ISO 4217 currency code",
        pattern=r"^[A-Z]{3}$"
    )
    beneficiary_name: str = Field(
        description="Recipient name",
        min_length=2,
        max_length=100
    )
    beneficiary_iban: str = Field(
        description="Recipient IBAN",
        pattern=r"^[A-Z]{2}\d{2}[A-Z0-9]{4}\d{7}([A-Z0-9]?){0,16}$"
    )
    status: str = Field(
        description="Payment status",
        pattern=r"^(pending|processing|completed|failed)$"
    )
    timestamp: str = Field(description="ISO 8601 timestamp")
    disclaimer: Optional[str] = Field(
        default="This confirmation is for your records. "
        "Please contact us if you notice any discrepancies."
    )

# Create Guard with schema
payment_guard = Guard.from_pydantic(
    output_class=PaymentConfirmation,
    num_reasks=2,  # Maximum re-ask attempts before failing
)
```

### 3.3 Using the Guard in an LLM Call

```python
import openai

# Without Guardrails AI (no validation)
# response = client.chat.completions.create(...)

# With Guardrails AI (validated output)
result = payment_guard(
    llm_api=openai.chat.completions.create,
    model="gpt-4o",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ],
    temperature=0.1,
)

if result.validation_passed:
    # Safe to deliver to customer
    return result.validated_output
else:
    # Validation failed after all re-asks
    # Activate fallback procedure
    log_validation_failure(result.error)
    return fallback_response()
```

---

## 4. Validator Configuration

### 4.1 Built-in Validators for FinTech

| Validator | Purpose | Configuration | On-Fail Action |
|-----------|---------|---------------|---------------|
| `ValidJson` | Ensures output is valid JSON | -- | `reask` |
| `DetectPII` | Detects PII in outputs | Entity list: CREDIT_CARD, IBAN, SSN, EMAIL | `fix` (mask) |
| `ToxicLanguage` | Detects harmful or offensive content | Threshold: 0.8 | `reask` |
| `ValidLength` | Ensures response is within length limits | Min: 10, Max: 2000 characters | `reask` |
| `RegexMatch` | Validates format patterns | Pattern per field | `reask` |

### 4.2 On-Fail Actions

| Action | Behaviour | When to Use |
|--------|----------|-------------|
| `reask` | Re-prompts the LLM with the validation error and asks it to try again | When the LLM is likely to self-correct (format issues, minor content issues) |
| `fix` | Automatically corrects the output (e.g., masking PII) | When automated correction is safe and reliable |
| `exception` | Raises an exception; triggers fallback procedure | When validation failure is critical and output must not be delivered |
| `filter` | Removes the invalid field from the output | When the field is optional and the response is still useful without it |
| `noop` | Logs the violation but delivers the output anyway | Only for monitoring mode; never for production safety validators |

---

## 5. Custom Validators for FinTech

### 5.1 IBAN Validator

```python
from guardrails.validators import Validator, register_validator, PassResult, FailResult
import re

@register_validator(name="valid_iban", data_type="string")
class ValidIBAN(Validator):
    """Validates that a string is a properly formatted IBAN."""

    IBAN_LENGTHS = {
        "NL": 18, "DE": 22, "FR": 27, "GB": 22, "BE": 16,
        "ES": 24, "IT": 27, "AT": 20, "PT": 25, "IE": 22,
        # Add more country codes as needed
    }

    def validate(self, value, metadata=None):
        # Remove spaces and convert to uppercase
        iban = value.replace(" ", "").upper()

        # Check basic format
        if not re.match(r"^[A-Z]{2}\d{2}[A-Z0-9]+$", iban):
            return FailResult(
                error_message=f"IBAN '{value}' does not match the expected format "
                              f"(country code + check digits + account number)."
            )

        # Check country-specific length
        country = iban[:2]
        expected_length = self.IBAN_LENGTHS.get(country)
        if expected_length and len(iban) != expected_length:
            return FailResult(
                error_message=f"IBAN for {country} should be {expected_length} "
                              f"characters, but got {len(iban)}."
            )

        # Validate check digits (ISO 13616)
        rearranged = iban[4:] + iban[:4]
        numeric = ""
        for char in rearranged:
            if char.isdigit():
                numeric += char
            else:
                numeric += str(ord(char) - ord("A") + 10)

        if int(numeric) % 97 != 1:
            return FailResult(
                error_message=f"IBAN '{value}' has invalid check digits."
            )

        return PassResult()
```

### 5.2 Financial Amount Validator

```python
@register_validator(name="valid_financial_amount", data_type="float")
class ValidFinancialAmount(Validator):
    """Validates financial amounts are within acceptable ranges and precision."""

    def __init__(
        self,
        min_amount: float = 0.01,
        max_amount: float = 50000.00,
        max_decimal_places: int = 2,
        currency: str = "EUR",
        **kwargs
    ):
        super().__init__(**kwargs)
        self.min_amount = min_amount
        self.max_amount = max_amount
        self.max_decimal_places = max_decimal_places
        self.currency = currency

    def validate(self, value, metadata=None):
        if value < self.min_amount:
            return FailResult(
                error_message=f"Amount {value} {self.currency} is below "
                              f"minimum {self.min_amount} {self.currency}."
            )
        if value > self.max_amount:
            return FailResult(
                error_message=f"Amount {value} {self.currency} exceeds "
                              f"maximum {self.max_amount} {self.currency}. "
                              f"Transactions above this limit require manual processing."
            )

        # Check decimal precision
        str_value = str(value)
        if "." in str_value:
            decimals = len(str_value.split(".")[1])
            if decimals > self.max_decimal_places:
                return FailResult(
                    error_message=f"Amount has {decimals} decimal places. "
                                  f"Maximum allowed: {self.max_decimal_places}."
                )

        return PassResult()
```

### 5.3 Compliance Statement Validator

```python
@register_validator(name="compliance_statement_check", data_type="string")
class ComplianceStatementCheck(Validator):
    """Detects language that could constitute unauthorized financial advice."""

    PROHIBITED_PATTERNS = [
        (r"(I |we )?(recommend|suggest|advise)\b.*\b(buy|sell|invest)", "investment_advice"),
        (r"guaranteed\s+(return|profit|income|yield)", "guaranteed_returns"),
        (r"(risk-free|no risk|cannot lose|completely safe)", "risk_minimization"),
        (r"(act now|limited time|don't miss|hurry|urgent)", "pressure_tactics"),
        (r"you should\s+(open|close|switch|change)", "product_recommendation"),
        (r"based on your\s+(profile|situation|risk)", "personalized_advice"),
    ]

    def validate(self, value, metadata=None):
        import re
        for pattern, category in self.PROHIBITED_PATTERNS:
            match = re.search(pattern, value, re.IGNORECASE)
            if match:
                return FailResult(
                    error_message=f"Output contains prohibited language "
                                  f"(category: {category}): '{match.group()}'. "
                                  f"Remove or rephrase this content."
                )
        return PassResult()
```

---

## 6. LLM Pipeline Integration

### 6.1 Integration with LangChain

```python
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser
from guardrails import Guard

# Create the Guard
guard = Guard.from_pydantic(PaymentConfirmation, num_reasks=2)

# Integration pattern: Guard wraps the LLM call
def process_payment_request(user_message: str) -> dict:
    result = guard(
        llm_api=openai.chat.completions.create,
        model="gpt-4o",
        messages=[
            {"role": "system", "content": PAYMENT_SYSTEM_PROMPT},
            {"role": "user", "content": user_message}
        ],
        metadata={"user_id": current_user.id},
    )

    if result.validation_passed:
        return {
            "status": "success",
            "data": result.validated_output,
            "validation_log": result.validation_logs
        }
    else:
        # Log failure for monitoring
        log_to_observability(
            event="output_validation_failed",
            agent_id=AGENT_ID,
            error=str(result.error),
            reask_count=result.reask_count,
        )
        return {
            "status": "fallback",
            "message": "I was unable to process this request accurately. "
                       "Let me connect you with a team member.",
            "escalation_reason": "output_validation_failure"
        }
```

### 6.2 Integration with Observability Platforms

Log all validation events to your observability platform for monitoring and governance:

```python
from langsmith import Client as LangSmithClient

langsmith = LangSmithClient()

def log_validation_event(guard_result, agent_id: str, interaction_id: str):
    """Log validation result to LangSmith for tracing and monitoring."""
    langsmith.create_feedback(
        run_id=interaction_id,
        key="output_validation",
        score=1.0 if guard_result.validation_passed else 0.0,
        comment=str(guard_result.validation_logs),
    )

    # Also log to Arize Phoenix / Langfuse / Opik as configured
    # See: ../../04-operational-governance/guides/traceability-with-langchain.md
```

---

## 7. Performance Considerations

| Validator Type | Typical Latency | Optimization |
|---------------|----------------|-------------|
| JSON schema validation | 1-5 ms | Negligible |
| Regex pattern matching | 1-3 ms | Negligible |
| PII detection (regex-based) | 5-15 ms | Pre-compile patterns |
| PII detection (NER model) | 50-200 ms | Use batch processing where possible |
| Content safety (classifier) | 100-500 ms | Use lightweight model; cache frequent patterns |
| IBAN validation (with check digit) | 1-3 ms | Negligible |
| Financial amount validation | 1-2 ms | Negligible |
| Compliance language detection | 10-50 ms (regex) | Pre-compile; use rule-based first pass |
| Re-ask cycle (when validation fails) | + full LLM call latency | Limit re-asks to 2; set hard timeout |

**Performance budget:** Total output validation should add < 200 ms for rule-based validators, < 500 ms when model-based validators are included. Re-ask cycles may add 1-3 seconds per retry.

---

## 8. Testing Validators

### 8.1 Unit Testing Pattern

```python
import pytest
from validators.iban_validator import ValidIBAN

class TestIBANValidator:
    def setup_method(self):
        self.validator = ValidIBAN()

    def test_valid_dutch_iban(self):
        result = self.validator.validate("NL91ABNA0417164300")
        assert isinstance(result, PassResult)

    def test_valid_german_iban(self):
        result = self.validator.validate("DE89370400440532013000")
        assert isinstance(result, PassResult)

    def test_invalid_check_digits(self):
        result = self.validator.validate("NL00ABNA0417164300")
        assert isinstance(result, FailResult)
        assert "invalid check digits" in result.error_message

    def test_wrong_length(self):
        result = self.validator.validate("NL91ABNA041716430")  # 17 chars
        assert isinstance(result, FailResult)
        assert "should be 18 characters" in result.error_message

    def test_invalid_format(self):
        result = self.validator.validate("123456789")
        assert isinstance(result, FailResult)
```

### 8.2 Integration Testing

Test guards end-to-end with mock LLM responses to verify the full validation pipeline:

```python
def test_payment_guard_rejects_invalid_amount():
    mock_response = {
        "transaction_id": "TXN-2026-001",
        "amount": 999999.99,  # Exceeds maximum
        "currency": "EUR",
        "beneficiary_name": "Test User",
        "beneficiary_iban": "NL91ABNA0417164300",
        "status": "pending",
        "timestamp": "2026-03-01T10:00:00Z"
    }
    # Verify guard catches the invalid amount
    result = payment_guard.parse(json.dumps(mock_response))
    assert not result.validation_passed
```

---

## 9. Deployment Checklist

- [ ] All custom validators have unit tests with > 95% coverage
- [ ] Guard definitions match the safety policy (safety-policy-definition.md)
- [ ] PII detection covers all relevant entity types for the agent's jurisdiction
- [ ] Content safety validator tested with adversarial examples
- [ ] Financial advice detection patterns reviewed by compliance
- [ ] IBAN validator covers all supported countries
- [ ] Amount validator limits match the agent's permission boundaries
- [ ] Re-ask limits configured (maximum 2 for customer-facing agents)
- [ ] Fallback responses defined for all validation failure scenarios
- [ ] Validation events logged to observability platform
- [ ] Performance tested: total validation latency < 500 ms P95
- [ ] Guardrail specification YAML (guardrail-specification.yaml) updated to reference this configuration
- [ ] Red-team exercise completed against the validation pipeline

---

## Cross-References

- **Integrating NeMo Guardrails:** [integrating-nemo-guardrails.md](integrating-nemo-guardrails.md) -- companion guide for conversational flow control and input rails
- **Output Validation Patterns:** [output-validation-patterns.md](output-validation-patterns.md) -- decision framework for selecting validation strategies
- **Safety Policy Definition:** [../templates/safety-policy-definition.md](../templates/safety-policy-definition.md) -- policy that guardrail validators enforce
- **Guardrail Specification:** [../templates/guardrail-specification.yaml](../templates/guardrail-specification.yaml) -- YAML specification consumed by guardrail engines
- **Customer-Facing Agent Safety:** [../agentic-workflows/customer-facing-agent-safety.md](../agentic-workflows/customer-facing-agent-safety.md) -- safety patterns that validators implement
- **Agent Permission Boundaries:** [../agentic-workflows/agent-permission-boundaries.md](../agentic-workflows/agent-permission-boundaries.md) -- permission boundaries that amount validators enforce
- **Traceability with LangChain:** [../../04-operational-governance/guides/traceability-with-langchain.md](../../04-operational-governance/guides/traceability-with-langchain.md) -- observability platform integration for validation logging
- **Red-Teaming AI Systems:** [../../04-operational-governance/guides/red-teaming-ai-systems.md](../../04-operational-governance/guides/red-teaming-ai-systems.md) -- testing methodology for validator effectiveness
- **Glossary:** [../../05-cross-cutting/glossary.md](../../05-cross-cutting/glossary.md) -- definitions for guardrail, validator, re-asking, output validation

---

*Last updated: 2026-03-01* / *Version: 1.0* / *Classification: Internal / Regulatory Preparation*
