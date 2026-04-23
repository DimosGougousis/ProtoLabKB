# A/B Testing Frameworks for AI Feature Variants

> **AI Governance Framework for Agentic Workflows in Regulated FinTech**
>
> Version: 1.0.0 | Last Updated: 2026-02-28 | Owner: AI Governance Office

---

## 1. Purpose

This document establishes the methodology for running controlled experiments (A/B tests) on AI-powered features, including standalone model endpoints, single-agent experiences, and multi-agent orchestrations. It addresses the unique statistical, ethical, and regulatory challenges that arise when the "treatment" is a non-deterministic AI system rather than a static UI change.

**Cross-references:**

- [User Feedback as Evaluation](./user-feedback-as-evaluation.md) -- feedback signals feed into A/B metric design.
- [Guardrail Specification Template](../templates/guardrail-specification.yaml) -- guardrail variants are testable via A/B.
- [Safety Policy Checklist](../checklists/safety-policy-checklist.yaml) -- safety policies must hold across all test variants.

---

## 2. Why A/B Testing AI Is Different

Traditional A/B testing assumes deterministic treatments: a user sees button colour A or button colour B, and the experience is identical on every page load. AI systems violate this assumption in several ways.

### 2.1 Non-Deterministic Outputs

Even with the same input, a language model may produce different outputs across requests (unless temperature is set to zero and caching is enabled). This adds within-variant variance that inflates the sample size required to detect a given effect.

### 2.2 Higher Variance in Outcome Metrics

AI quality metrics (task completion rate, user satisfaction, hallucination rate) tend to have higher variance than traditional conversion metrics. A button-colour test might see 2-3 % conversion with low variance; an AI chatbot satisfaction score might range from 1 to 5 with high standard deviation.

### 2.3 Longer Convergence Times

Because of the above, experiments on AI features typically require longer run times or larger sample sizes to reach statistical significance. Premature stopping leads to unreliable conclusions.

### 2.4 Interaction Effects

An AI agent's behaviour depends on the user's input, which varies wildly. Two users in the same variant may have entirely different experiences. Stratification and blocking become more important than in traditional A/B testing.

### 2.5 Safety Asymmetry

In traditional testing, a "worse" variant might reduce conversion by a few percent. In AI testing, a worse variant could produce harmful content, violate compliance rules, or make incorrect financial recommendations. Safety must be monitored continuously, not just at experiment conclusion.

---

## 3. What to A/B Test

### 3.1 Prompt Versions

| Variable | Example |
|---|---|
| System prompt phrasing | "You are a helpful financial advisor" vs. "You are a cautious, regulation-aware financial advisor" |
| Few-shot examples | 3 examples vs. 5 examples vs. chain-of-thought examples |
| Instruction specificity | High-level instruction vs. step-by-step instruction |

### 3.2 Model Versions

| Variable | Example |
|---|---|
| Model family | GPT-4o vs. Claude Opus 4 vs. fine-tuned in-house model |
| Model size | Full model vs. distilled model (cost/quality trade-off) |
| Fine-tune iteration | Base model vs. RLHF iteration 3 vs. RLHF iteration 4 |

### 3.3 Guardrail Configurations

| Variable | Example |
|---|---|
| Strictness level | Conservative content filter vs. moderate content filter |
| PII handling | Mask-and-proceed vs. reject-and-ask-user-to-rephrase |
| Hallucination mitigation | RAG-only grounding vs. RAG + post-hoc fact-check |

### 3.4 Agent Configurations

| Variable | Example |
|---|---|
| Tool set | Agent with 3 tools vs. agent with 5 tools |
| Oversight model | HITL (human approves every action) vs. HOTL (human monitors, vetoes if needed) |
| Permission boundary | Read-only data access vs. read-write data access (with appropriate safeguards) |
| Delegation depth | Max 2 hops vs. max 4 hops in multi-agent chains |

---

## 4. Metrics

A well-designed AI A/B test tracks metrics across five categories.

### 4.1 Task Completion

- **Primary:** Task success rate (did the user achieve their goal?)
- **Secondary:** Steps to completion, time to completion, need for human escalation

### 4.2 User Satisfaction

- **Primary:** CSAT score, thumbs-up/thumbs-down ratio
- **Secondary:** NPS delta, qualitative feedback themes

### 4.3 Safety Incidents

- **Primary:** Guardrail trigger rate, harmful-output rate, compliance-violation count
- **Secondary:** Escalation rate, human-takeover rate
- **Monitoring:** These metrics must be tracked in real time with automatic experiment-halt triggers (see Section 7)

### 4.4 Cost

- **Primary:** Cost per conversation (tokens consumed, tool invocations, infrastructure)
- **Secondary:** Cost per successful task completion (efficiency metric)

### 4.5 Latency

- **Primary:** End-to-end response time (p50, p95, p99)
- **Secondary:** Time-to-first-token, guardrail evaluation latency

---

## 5. Experimental Design

### 5.1 Sample Size Calculation

Use power analysis with the following adjustments for AI experiments:

1. **Estimate variance from pilot data**, not from traditional web experiments.
2. **Inflate the minimum detectable effect (MDE)** -- AI metrics are noisier, so aim for larger MDE or accept longer run times.
3. **Account for within-variant variance** -- non-deterministic outputs mean two requests from the same user in the same variant may differ. Use per-user aggregation (e.g., average satisfaction across all conversations) rather than per-request metrics.

**Rule of thumb:** For AI chatbot experiments, expect to need 2-5x the sample size of a traditional UI A/B test for the same MDE and power.

### 5.2 Duration

- **Minimum duration:** 2 weeks (captures weekday/weekend patterns).
- **Recommended duration:** 4 weeks for agent-level experiments where user behaviour evolves over repeated interactions.
- **No peeking rule:** Do not make go/no-go decisions before the pre-committed analysis date unless a safety trigger fires.

### 5.3 Randomisation Unit

- **User-level** (preferred): Each user is assigned to one variant for the entire experiment. Avoids within-user contamination.
- **Session-level:** Acceptable only for stateless, one-off interactions. Avoid for agents where multi-turn context matters.

### 5.4 Holdout Groups

Maintain a persistent holdout group (5-10 % of traffic) that always sees the current production configuration. This provides a stable baseline for long-term trend monitoring, independent of any single experiment.

### 5.5 Stratification

Stratify on key confounders:

- **User segment:** New vs. returning, high-value vs. standard
- **Channel:** Mobile vs. desktop vs. API
- **Geography / language:** Regulatory environment may differ

---

## 6. Agent-Specific Testing Considerations

### 6.1 Testing Permission Boundaries

When comparing agents with different permission scopes (e.g., read-only vs. read-write), ensure:

- Both variants operate within approved safety policies.
- The broader-permission variant has additional monitoring and tighter escalation triggers.
- An independent safety reviewer approves the experiment design before launch.

### 6.2 Testing Oversight Models

Comparing HITL vs. HOTL vs. HOTA oversight models requires careful control:

- Measure both user-facing metrics (satisfaction, completion) and governance metrics (error rate, compliance violations).
- The less-supervised variant must have automatic safety stops: if the compliance-violation rate exceeds a threshold, halt the experiment and revert to the more-supervised model.

### 6.3 Testing Tool Configurations

When agents in different variants have access to different tool sets:

- Ensure all tool sets are approved in the tool manifest.
- Log tool invocations per variant to detect unexpected tool-use patterns.
- Monitor for tool-use loops or excessive invocations in the broader tool-set variant.

### 6.4 Multi-Agent Orchestration Variants

Testing changes to delegation chains (e.g., 2-agent pipeline vs. 3-agent pipeline):

- Track per-span latency and accuracy across the chain using reasoning traces.
- Monitor delegation depth and inter-agent message volume.
- Cross-reference with [Delegation Chain Audit](../agentic-workflows/delegation-chain-audit.md) to ensure traceability.

---

## 7. Safety Guardrails for Experiments

Every AI A/B test must have pre-defined automatic halt criteria.

| Metric | Threshold | Action |
|---|---|---|
| Harmful output rate | > 0.1 % in any variant | Halt experiment, revert variant to control |
| Compliance violation count | > 0 critical violations | Halt experiment, escalate to compliance |
| Guardrail trigger rate | > 2x baseline for 24 hours | Alert on-call; halt if persists 48 hours |
| User escalation rate | > 1.5x control for 48 hours | Alert experiment owner; consider halting |
| Latency p99 | > SLA threshold for 4 hours | Alert SRE; halt variant if infrastructure-related |

These thresholds must be documented in the experiment plan before launch and approved by the AI Governance Lead.

---

## 8. Ethical Considerations

### 8.1 Fairness Across Test Groups

- No variant should expose users to materially worse safety outcomes.
- If a variant degrades service quality for a protected demographic, the experiment must halt.
- Analyse results disaggregated by demographic segments (where data is available and permitted).

### 8.2 Informed Consent

- Users must be informed that AI-assisted features may vary as part of ongoing improvement.
- This disclosure can be general (in Terms of Service) rather than per-experiment, per regulatory guidance.
- Users must always have the option to opt out of AI-assisted features entirely.

### 8.3 Regulatory Constraints on Experimentation

- In regulated FinTech, certain decisions (credit, insurance pricing) may not be subject to unconstrained experimentation. Verify with Compliance that the experiment does not constitute an unauthorized change to a regulated decision process.
- EU AI Act Article 9(7) requires that testing does not affect users negatively.

---

## 9. FinTech Case Study: A/B Testing Chatbot Configurations

### Scenario

A consumer lending platform wants to test two configurations of its customer-service chatbot:

- **Control (A):** Current production prompt with HITL oversight for all loan-related queries.
- **Treatment (B):** Revised prompt with improved few-shot examples and HOTL oversight (human monitors but does not gate every response).

### Design

| Parameter | Value |
|---|---|
| Randomisation unit | User ID |
| Traffic split | 50/50 |
| Duration | 4 weeks |
| Primary metric | Task completion rate (user's question resolved without escalation) |
| Secondary metrics | CSAT, escalation rate, compliance-violation count, cost per conversation |
| Safety halt | Compliance violation > 0, escalation rate > 2x control |

### Analysis

1. Compare task completion rate using a two-proportion z-test, corrected for multiple comparisons.
2. Compute confidence intervals for CSAT difference.
3. Review compliance-violation logs (expect zero in both variants).
4. Calculate cost savings from reduced human-in-the-loop overhead in Treatment B.
5. Perform subgroup analysis by loan product type and user tenure.

### Decision Framework

- If Treatment B achieves higher task completion **and** zero compliance violations **and** acceptable escalation rate: promote to production.
- If Treatment B achieves higher task completion but elevated escalation rate: iterate on the prompt to improve edge-case handling.
- If any compliance violation occurs: halt, root-cause, and redesign.

---

## 10. Tooling Recommendations

| Capability | Example Tools |
|---|---|
| Experiment assignment | LaunchDarkly, Statsig, Eppo, custom feature-flag service |
| Statistical analysis | Statsig, Eppo, internal Bayesian analysis pipeline |
| Real-time safety monitoring | Datadog, Grafana with custom AI safety dashboards |
| Trace analysis | OpenTelemetry + Jaeger, LangSmith, Arize Phoenix |
| Feedback collection | See [User Feedback as Evaluation](./user-feedback-as-evaluation.md) |

---

## 11. Experiment Lifecycle Summary

```
1. Hypothesis     Define what you expect to change and why
2. Design         Sample size, duration, metrics, halt criteria
3. Review         AI Governance Lead + Compliance approval
4. Instrument     Feature flags, logging, monitoring dashboards
5. Launch         Begin traffic split
6. Monitor        Real-time safety checks; daily metric reviews
7. Analyse        Statistical tests at pre-committed analysis date
8. Decide         Promote, iterate, or revert
9. Document       Record findings in experiment registry
```

---

## 12. Document Control

| Field | Value |
|---|---|
| Classification | Internal -- AI Governance |
| Review cycle | Every 6 months or after material regulatory change |
| Approved by | AI Governance Lead, Chief Compliance Officer |
| Next review | 2026-08-28 |
