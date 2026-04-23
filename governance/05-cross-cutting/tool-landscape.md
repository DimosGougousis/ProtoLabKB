# AI Governance Tool Landscape

## Purpose

This document provides a comprehensive overview of the tools referenced throughout the governance framework. For each tool, it documents what it does, how it supports governance activities, when to choose it over alternatives, and how it integrates with the governance lifecycle. This is not a product recommendation -- it is a governance-oriented evaluation of the tool landscape to help organizations make informed selection decisions.

## When to Use

- When selecting tools to implement governance controls defined in this framework
- When building the governance technology stack for a new AI program
- When evaluating whether current tooling covers all governance requirements
- When responding to regulatory requests about governance tooling capabilities

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| **Engineering Lead** | **Responsible** -- evaluates and selects technical tools based on governance requirements |
| **AI Steward** | **Consulted** -- ensures selected tools cover governance requirements across all four pillars |
| **CAIO** | **Accountable** -- approves enterprise tool strategy at Tier 1 (Strategic) |
| **Compliance Officer** | **Consulted** -- validates that tools meet regulatory evidence requirements |
| **Procurement** | **Informed** -- handles vendor assessment and licensing |

## Regulatory Basis

- **ISO/IEC 42001 Clause 8** -- Operational planning and control require appropriate tooling
- **EU AI Act Article 9(7)** -- Testing procedures throughout the lifecycle require tooling support
- **EU AI Act Article 72** -- Post-market monitoring requires observability infrastructure
- **DORA Article 8** -- ICT risk management requires appropriate tools and systems

---

## 1. Evaluation and Testing Tools

These tools quantify AI system performance, safety, fairness, and reliability across the development and operational pillars.

### Giskard

| Attribute | Details |
|-----------|---------|
| **What it does** | Open-source AI testing framework that automatically generates test suites for ML models and LLMs. Detects performance issues, biases, hallucinations, and security vulnerabilities through automated test generation |
| **Governance use case** | Automates the creation and execution of eval suites required by the pre-deployment gate (DEV-EVAL-002). Generates bias test cases for fairness evaluation (DEV-FAIR-003). Supports SAFEST items S-03, F-03 |
| **Integration points** | CI/CD pipeline integration for automated eval gates; export results to governance evidence repositories; supports Python-based ML pipelines |
| **License** | Open source (Apache 2.0); enterprise features available |
| **When to choose** | When you need automated test generation for ML models and LLMs; when you want to shift-left bias testing into the development pipeline; when budget constrains use of commercial alternatives |
| **Pillar alignment** | Development Governance (primary), Operational Governance (periodic revalidation) |

### Microsoft Responsible AI (RAI) Toolbox

| Attribute | Details |
|-----------|---------|
| **What it does** | Collection of tools for responsible AI development: Fairlearn (fairness assessment), InterpretML (model interpretability), Error Analysis (failure mode identification), Counterfactual Analysis (what-if scenarios) |
| **Governance use case** | Provides the fairness metrics required by SAFEST F-03 and F-04. Supports explainability requirements (SAFEST T-01, T-02). Generates evidence for pre-deployment gate bias testing (DEV-FAIR-001 through DEV-FAIR-005) |
| **Integration points** | Azure ML integration; Jupyter notebook workflows; Python SDK for custom pipelines; can export fairness reports as governance evidence |
| **License** | Open source (MIT); supported by Microsoft |
| **When to choose** | When you need comprehensive fairness assessment across multiple metrics; when using Azure ML ecosystem; when explainability reports are required for regulatory documentation |
| **Pillar alignment** | Development Governance (primary), Discovery Governance (fairness metric selection) |

### DeepEval

| Attribute | Details |
|-----------|---------|
| **What it does** | Open-source LLM evaluation framework purpose-built for testing LLM applications. Provides metrics for hallucination, relevance, faithfulness, toxicity, and bias. Supports custom metric definitions |
| **Governance use case** | Implements the LLM-specific eval suite items required by the pre-deployment gate. Tests hallucination rates for customer-facing chatbots. Validates RAG pipeline quality. Supports SAFEST S-03 |
| **Integration points** | pytest integration for CI/CD; supports OpenAI, Anthropic, and open-source models; exports results as structured JSON for evidence repositories |
| **License** | Open source (Apache 2.0) |
| **When to choose** | When building eval suites for LLM-based agents; when you need LLM-specific metrics (hallucination, faithfulness, coherence) integrated into CI/CD; when you want a lightweight testing framework |
| **Pillar alignment** | Development Governance (primary) |

### RAGAS (Retrieval-Augmented Generation Assessment)

| Attribute | Details |
|-----------|---------|
| **What it does** | Framework for evaluating RAG (Retrieval-Augmented Generation) pipelines. Measures context relevance, answer faithfulness, answer relevance, and context recall. Designed specifically for RAG quality assessment |
| **Governance use case** | Validates the quality of RAG-based agent responses -- critical for FinTech agents that retrieve financial documents, regulations, or customer data. Ensures grounding quality required for factual accuracy. Supports SAFEST S-03 |
| **Integration points** | LangChain and LlamaIndex integration; supports all major LLM providers; CI/CD integration via Python |
| **License** | Open source (Apache 2.0) |
| **When to choose** | When your AI system uses RAG architecture; when you need to validate that agent responses are grounded in retrieved documents (not hallucinated); complements DeepEval for RAG-specific metrics |
| **Pillar alignment** | Development Governance (primary), Runtime Governance (continuous evaluation of RAG quality) |

---

## 2. Runtime Guardrail Tools

These tools implement the controls defined in Runtime Governance (Pillar 3), enforcing behavioral boundaries at inference time.

### NVIDIA NeMo Guardrails

| Attribute | Details |
|-----------|---------|
| **What it does** | Programmable guardrail framework for LLM applications. Uses Colang (a custom DSL) to define conversational flows, topic restrictions, safety rails, and output constraints. Can intercept and modify LLM interactions in real time |
| **Governance use case** | Implements the runtime safety rails and permission boundaries required for agentic systems. Enforces topic restrictions (agent stays within its domain), action restrictions (agent cannot perform unauthorized operations), and output filtering (PII redaction, safety content filtering). Supports SAFEST S-07, A-06, A-09 |
| **Integration points** | LangChain integration; standalone server deployment; supports any LLM backend; Kubernetes deployment for production |
| **License** | Open source (Apache 2.0); NVIDIA supported |
| **When to choose** | When you need programmable, declarative guardrails with fine-grained control over conversational flows; when building complex agentic systems that need multi-turn safety enforcement; when you want guardrails as code (version-controlled, testable) |
| **Pillar alignment** | Runtime Governance (primary) |

### Guardrails AI

| Attribute | Details |

---

## 3. Policy-as-Code Engines

These tools enable compliance-as-configuration by evaluating governance rules at runtime.

### Open Policy Agent (OPA)

| Attribute | Details |
|-----------|---------|
| **What it does** | General-purpose policy engine that uses the Rego language to express policy over hierarchical data. Evaluates policies for microservices, Kubernetes, CI/CD pipelines, and API gateways |
| **Governance use case** | Implements Layer 1 (Compliance Check) of the governance enforcement pipeline. Evaluates YAML compliance rules for jurisdiction, data classification, and regulatory requirements. Supports EU AI Act, GDPR, DORA compliance |
| **Integration points** | Sidecar deployment, standalone service, or embedded library. gRPC/REST APIs for policy queries. Bundle-based policy distribution from Git |
| **License** | Open source (Apache 2.0); commercial support available |
| **When to choose** | When you need a mature, widely-adopted policy engine with broad ecosystem support; when policies need to span multiple systems (not just AI); when Rego language meets your needs |
| **Pillar alignment** | Runtime Governance (Layer 1: Compliance) |

### Cedar

| Attribute | Details |
|-----------|---------|
| **What it does** | Policy language and evaluation engine designed specifically for authorization. Developed by AWS with formal verification properties. Uses intuitive permit/unless syntax |
| **Governance use case** | Implements fine-grained authorization for agent actions, skill permissions, and resource access. Formal verification ensures policies behave as intended. Supports per-skill RBAC |
| **Integration points** | Rust SDK, Java SDK, or standalone server. Policy validation and testing tools. AWS integration for Verified Permissions service |
| **License** | Open source (Apache 2.0) |
| **When to choose** | When you need formally verifiable authorization policies; when AWS ecosystem integration is important; when Cedar's simpler syntax is preferred over Rego; when authorization (not general policy) is the primary use case |
| **Pillar alignment** | Runtime Governance (Layer 3: RBAC) |

---

## 4. Identity and Security Tools

### SPIFFE/SPIRE

| Attribute | Details |
|-----------|---------|
| **What it does** | SPIFFE defines a standard for workload identity; SPIRE is the reference implementation that issues short-lived, automatically rotated cryptographic identities (SVIDs) to workloads |
| **Governance use case** | Provides machine identity for AI agents with 15-minute TTL for high-risk systems. Enables cryptographically verifiable delegation chains. Supports zero-trust architecture |
| **Integration points** | Kubernetes, AWS, GCP, Azure workload attestation. Unix socket or TCP for SVID retrieval. Envoy integration for automatic mTLS |
| **License** | Open source (Apache 2.0); CNCF incubating project |
| **When to choose** | When you need strong workload identity with automatic rotation; when implementing zero-trust for agent infrastructure; when delegation chains need cryptographic proof of identity |
| **Pillar alignment** | Runtime Governance (Layer 3: RBAC, Identity) |

---

## 5. Observability and Evaluation Platforms

### Langfuse

| Attribute | Details |
|-----------|---------|
| **What it does** | Open-source LLM engineering platform for observability, evaluations, and prompt management. Provides tracing, metrics, and experimentation for LLM applications |
| **Governance use case** | Implements traceability requirements for agent execution. Captures full request/response cycles for audit. Supports eval tracking and prompt versioning |
| **Integration points** | Python/JS SDK, OpenTelemetry integration, LangChain/LlamaIndex native support. Self-hosted or cloud deployment |
| **License** | Open source (MIT); commercial cloud offering |
| **When to choose** | When you need comprehensive LLM observability with self-hosting option; when eval tracking and prompt management are priorities; when cost-effective alternative to commercial platforms is needed |
| **Pillar alignment** | Development Governance (evals), Operational Governance (monitoring) |

### Arize Phoenix

| Attribute | Details |
|-----------|---------|
| **What it does** | Open-source AI observability and evaluation platform. Provides tracing, evaluation, and drift detection for LLM and ML applications |
| **Governance use case** | Supports drift detection requirements (SAFEST S-12). Provides evaluation frameworks for agent performance. Enables prompt engineering workflows |
| **Integration points** | Python SDK, OpenTelemetry, LlamaIndex, LangChain. Notebook-based experimentation. Cloud or self-hosted |
| **License** | Open source (Apache 2.0); commercial Arize platform available |
| **When to choose** | When you need unified ML and LLM observability; when drift detection is critical; when notebook-based experimentation fits your workflow |
| **Pillar alignment** | Development Governance (evals), Operational Governance (drift detection) |

### Braintrust

| Attribute | Details |
|-----------|---------|
| **What it does** | Enterprise-grade platform for AI evaluation and experimentation. Provides eval frameworks, dataset management, and performance tracking for AI applications |
| **Governance use case** | Implements comprehensive eval suites required for deployment gates. Tracks eval results over time for regression detection. Supports A/B testing of agent configurations |
| **Integration points** | Python/JS SDK, CI/CD integration, API access. Cloud-hosted with enterprise features |
| **License** | Commercial (SaaS); free tier available |
| **When to choose** | When you need enterprise-grade eval management; when eval result tracking and regression detection are critical; when budget allows for commercial solution |
| **Pillar alignment** | Development Governance (primary), Operational Governance (continuous eval) |

---

## 6. Previous Tool Categories

### Guardrails AI

| Attribute | Details |
|-----------|---------|
| **What it does** | Framework for adding structural, type, and quality validation to LLM outputs. Defines "guards" that validate LLM responses against schemas, custom validators, and quality checks. Automatically re-prompts the LLM if output fails validation |
| **Governance use case** | Implements output validation required by insecure output handling mitigations (OWASP LLM02). Ensures structured outputs conform to expected schemas before being passed to tools or APIs. Supports SAFEST S-03 for output quality |
| **Integration points** | Python SDK; supports OpenAI, Anthropic, and open-source models; LangChain integration; validator marketplace (community validators for PII, toxicity, etc.) |
| **License** | Open source (Apache 2.0) |
| **When to choose** | When you need structured output validation (JSON schema, type checking); when LLM output feeds into downstream APIs or databases; when you want automatic re-prompting for failed validations |
| **Pillar alignment** | Runtime Governance (primary), Development Governance (output testing) |

### LlamaGuard (Meta)

| Attribute | Details |
|-----------|---------|
| **What it does** | Safety classifier model (based on Llama) that classifies LLM inputs and outputs for safety violations. Detects harmful content, unsafe prompts, and policy violations. Provides a configurable safety taxonomy |
| **Governance use case** | Implements content safety filtering for customer-facing FinTech chatbots. Classifies both inputs (detecting harmful user intent) and outputs (catching unsafe agent responses). Supports SAFEST S-06 adversarial robustness |
| **Integration points** | Deployable as a standalone classification service; integrates with any LLM pipeline as a pre/post-processing filter; supports custom safety taxonomies |
| **License** | Open source (Llama license); self-hosted |
| **When to choose** | When you need ML-based safety classification rather than rule-based filtering; when regulatory requirements demand content safety for customer-facing AI (EU AI Act Art. 50); when you want to customize the safety taxonomy for FinTech-specific risks |
| **Pillar alignment** | Runtime Governance (primary) |

---

## 3. Observability and Tracing Tools

These tools provide the monitoring infrastructure required by Operational Governance (Pillar 4) and the continuous evaluation requirements of Runtime Governance. Each records agent reasoning as structured "Spans" -- individual steps in the agent's reasoning and action chain -- enabling trace-level governance.

### LangSmith (LangChain)

| Attribute | Details |
|-----------|---------|
| **What it does** | Full-lifecycle LLM application platform: tracing, evaluation, monitoring, and debugging. Records every LLM call, tool invocation, and retrieval step as structured spans. Provides evaluation framework for scoring runs against criteria |
| **Governance use case** | Primary tracing platform for agent reasoning audit trails (SAFEST A-11). Records the complete delegation chain in multi-agent systems. Supports continuous online evaluation by running evals against production traces. Provides evidence for incident investigations (trace analysis). Supports SAFEST T-16 decision traceability |
| **Integration points** | Native LangChain/LangGraph integration; REST API for non-LangChain systems; annotation queues for human review; dataset management for eval suites; webhook alerts |
| **License** | Commercial SaaS (free tier available); self-hosted option for enterprise |
| **When to choose** | When using LangChain/LangGraph as the agent framework; when you need tight integration between tracing, evaluation, and agent development; when you need annotation workflows for human review of agent traces |
| **Pillar alignment** | Operational Governance (primary), Development Governance (eval management), Runtime Governance (continuous monitoring) |

### Arize Phoenix

| Attribute | Details |
|-----------|---------|
| **What it does** | Open-source observability platform for LLMs and ML models. Provides trace visualization, embedding drift detection, retrieval quality analysis, and performance monitoring. Specializes in production monitoring with drift detection |
| **Governance use case** | Implements drift detection required by SAFEST S-12. Provides the embedding-level monitoring needed for RAG quality degradation detection. Supports the periodic revalidation triggers (OPS-REVAL-E01) by generating drift alerts. Visualizes agent spans for incident investigation |
| **Integration points** | OpenTelemetry-based (vendor-agnostic); integrates with LangChain, LlamaIndex, OpenAI, Anthropic; self-hosted or cloud; supports export to data warehouses for long-term retention |
| **License** | Open source (BSD-3-Clause) with commercial cloud option |
| **When to choose** | When drift detection is a primary governance concern (high-risk ML models, production RAG systems); when you need open-source observability you can self-host; when you want embedding-level analysis for RAG quality |
| **Pillar alignment** | Operational Governance (primary), Runtime Governance (drift monitoring) |

### Opik (Comet)

| Attribute | Details |
|-----------|---------|
| **What it does** | LLM evaluation and observability platform focused on experiment tracking and production monitoring. Provides trace recording, automated evaluation metrics, A/B test management, and prompt versioning |
| **Governance use case** | Supports eval-driven development by tracking experiment results across prompt iterations (SAFEST S-03). Records production traces for audit trail (SAFEST A-11). Provides the A/B testing infrastructure referenced in continuous online evaluation |
| **Integration points** | Python SDK; integrates with OpenAI, Anthropic, LangChain; experiment tracking and comparison dashboards; supports custom evaluation metrics |
| **License** | Open source with commercial cloud option |
| **When to choose** | When experiment tracking and prompt versioning are governance priorities; when running A/B tests between agent variants; when you want combined experiment management and production monitoring |
| **Pillar alignment** | Development Governance (experiment tracking), Operational Governance (production monitoring) |

### Langfuse

| Attribute | Details |
|-----------|---------|
| **What it does** | Open-source LLM engineering platform: tracing, analytics, evaluation, and prompt management. Records LLM calls as spans with cost tracking. Provides evaluation scoring, user feedback collection, and prompt versioning |
| **Governance use case** | Records agent traces for audit compliance (SAFEST A-11). Tracks per-system and per-user costs for cost governance. Collects user feedback signals for continuous online evaluation (Section 4 of continuous-online-evaluation.md). Supports PII redaction policies for trace data privacy. Supports SAFEST T-16, A-13 |
| **Integration points** | OpenAI, Anthropic, LangChain, LlamaIndex integration via SDKs; REST API; self-hosted (Docker) or cloud; integrates with evaluation frameworks (OpenAI Evals, custom) |
| **License** | Open source (MIT); self-hosted available; commercial cloud option |
| **When to choose** | When you need open-source tracing with self-hosting for data sovereignty (important for FinTech with strict data residency requirements); when cost tracking per agent is a governance priority; when PII redaction in traces is required for GDPR compliance |
| **Pillar alignment** | Operational Governance (primary), Development Governance (prompt management) |

### Observability Platform Selection Guide

| Criterion | LangSmith | Arize Phoenix | Opik | Langfuse |
|-----------|-----------|--------------|------|----------|
| **Best for** | LangChain/LangGraph ecosystems | Drift detection, RAG monitoring | Experiment tracking, A/B testing | Self-hosted, cost tracking, data sovereignty |
| **Self-hosted** | Enterprise only | Yes (open source) | Yes (open source) | Yes (open source) |
| **Drift detection** | Basic | Advanced (embeddings) | Basic | Basic |
| **Cost tracking** | Yes | Limited | Yes | Yes (detailed) |
| **PII redaction** | Yes | Yes | Limited | Yes (configurable) |
| **Eval integration** | Native | OpenTelemetry-based | Native | API-based |
| **Multi-agent tracing** | Excellent (LangGraph) | Good | Good | Good |
| **DORA evidence suitability** | High | High | Medium | High |

---

## 4. Automated Red-Teaming Tools

These tools provide continuous security testing beyond what manual red-teaming can achieve, proactively identifying vulnerabilities.

### Noma AI

| Attribute | Details |
|-----------|---------|
| **What it does** | Continuous AI security platform that automatically tests LLM applications for vulnerabilities. Runs automated prompt injection campaigns, jailbreak attempts, data extraction tests, and policy violation probes. Provides vulnerability classification aligned with OWASP Top 10 for LLMs |
| **Governance use case** | Implements the automated red-teaming required by the OWASP guide (owasp-top10-llm-guide.md). Runs continuously against staging environments to detect new vulnerabilities. Integrates into the revalidation schedule as evidence for security evaluation. Supports SAFEST S-06, EU AI Act Art. 15(4) |
| **Integration points** | CI/CD pipeline integration; scheduled scan campaigns; webhook alerts for critical findings; vulnerability reporting compatible with AVID format |
| **License** | Commercial |
| **When to choose** | When you need continuous, automated security testing for LLM applications; when regulatory requirements demand evidence of ongoing adversarial testing (DORA Art. 25); when manual red-teaming cadence is insufficient for the threat landscape |
| **Pillar alignment** | Operational Governance (continuous testing), Development Governance (pre-deployment security gates) |

### Straiker

| Attribute | Details |
|-----------|---------|
| **What it does** | Agent-specific security testing platform. Tests tool-use vulnerabilities, permission boundary violations, delegation chain exploits, and agent-specific attack vectors. Specializes in adversarial testing of agentic AI architectures |
| **Governance use case** | Validates agent permission boundaries (DEV-SEC-004). Tests for excessive agency risks (OWASP LLM08). Verifies delegation chain integrity in multi-agent systems. Provides evidence for the periodic revalidation security evaluation (OPS-REVAL-E05). Supports SAFEST A-06, A-09 |
| **Integration points** | Staging environment deployment; supports LangChain, LangGraph, AutoGen agent architectures; structured vulnerability reports |
| **License** | Commercial |
| **When to choose** | When deploying agentic AI systems with tool use and autonomous actions; when you need agent-specific security testing beyond general LLM testing; when multi-agent governance requires delegation chain security validation |
| **Pillar alignment** | Operational Governance (primary), Runtime Governance (permission boundary validation) |

---

## 5. Agent Frameworks

These frameworks are used to build the agentic AI systems that the governance framework governs. Each has different implications for governance implementation.

### LangChain / LangGraph

| Attribute | Details |
|-----------|---------|
| **What it does** | LangChain: framework for building LLM-powered applications with chains, agents, and retrieval. LangGraph: extension for building stateful, multi-actor agent workflows as graphs |
| **Governance implications** | LangGraph's graph-based architecture maps naturally to governance: each node can have permission boundaries, each edge can be an approval gate. Native LangSmith integration provides tracing. Agent state management supports audit trail requirements. Tool definitions can be governance-controlled |
| **When to choose** | When building complex multi-agent systems; when tracing and observability integration is a priority; when you need the LangSmith ecosystem for governance evidence |
| **License** | Open source (MIT) |

### AutoGen (Microsoft)

| Attribute | Details |
|-----------|---------|
| **What it does** | Framework for building multi-agent conversational systems. Agents communicate via messages, enabling human-in-the-loop patterns and agent collaboration |
| **Governance implications** | Message-passing architecture makes conversation logging straightforward for audit trails. Built-in human-in-the-loop patterns align with HITL governance requirements. Agent termination conditions can implement governance gates. Less native observability integration than LangChain -- requires additional tracing setup |
| **When to choose** | When building conversational multi-agent systems; when human-in-the-loop is a primary governance pattern; when using Azure ecosystem |
| **License** | Open source (MIT) |

### CrewAI

| Attribute | Details |
|-----------|---------|
| **What it does** | Framework for orchestrating role-playing AI agents. Agents have defined roles, goals, and backstories. Supports sequential and hierarchical task delegation |
| **Governance implications** | Role-based agent design maps to governance role definitions. Hierarchical process mode enforces a delegation structure that can be audited. Less mature observability and tracing integration -- requires external tracing setup. Tool permissions must be configured per-agent |
| **When to choose** | When building role-specialized agent teams; when task decomposition and sequential execution are important; when simplicity of agent definition is preferred over framework flexibility |
| **License** | Open source (MIT) |

---

## 6. GRC Platforms

These platforms provide enterprise-level governance, risk, and compliance infrastructure.

### ServiceNow GRC

| Attribute | Details |
|-----------|---------|
| **What it does** | Enterprise GRC platform with risk management, policy management, audit management, and regulatory change management modules. Workflow automation for governance processes |
| **Governance use case** | Maps the YAML checklists in this framework to automated workflow items. Tracks revalidation schedules (periodic-revalidation-schedule.yaml) as automated workflow triggers. Manages incident response workflows linked to ai-incident-report.md. Provides the enterprise governance dashboard for CAIO and board reporting |
| **Integration points** | REST API for YAML checklist import; ServiceNow Flow Designer for automated governance workflows; CMDB for AI system inventory; incident module for AI incidents |
| **When to choose** | When the organization already uses ServiceNow for IT governance; when you need enterprise-scale workflow automation for governance processes |

### RSA Archer

| Attribute | Details |
|-----------|---------|
| **What it does** | Integrated risk management platform covering operational risk, regulatory compliance, third-party risk, and audit management |
| **Governance use case** | Manages the AI risk register linked to the risk classification checklist. Tracks third-party AI vendor risks aligned with DORA requirements (S-19a). Provides regulatory compliance tracking for EU AI Act, DORA, and DNB obligations |
| **Integration points** | REST API; data import for YAML checklists; reporting integration for regulatory submissions |
| **When to choose** | When the organization already uses Archer for risk management; when third-party AI vendor risk is a primary concern (DORA compliance) |

### OneTrust

| Attribute | Details |
|-----------|---------|
| **What it does** | Privacy, security, and AI governance platform. Provides AI governance module, DPIA management, consent management, and third-party risk management |
| **Governance use case** | Manages Data Protection Impact Assessments for AI systems (GDPR Art. 35). Tracks AI system inventory required by EU AI Act. Provides privacy impact assessments that complement the governance framework's ethical review. Supports SAFEST T-10 privacy transparency |
| **Integration points** | REST API; privacy impact assessment templates; AI governance module for system registration and risk tracking |
| **When to choose** | When privacy governance is a primary concern alongside AI governance; when DPIA management needs to be integrated with AI risk assessment; when EU AI Act system registration needs centralized management |

---

## 7. Vulnerability Tracking

### AVID (AI Vulnerability Database)

| Attribute | Details |
|-----------|---------|
| **What it does** | Community-maintained database of AI system vulnerabilities, failures, and harms. Provides a structured taxonomy for classifying AI vulnerabilities. Analogous to CVE/NVD for traditional software but specific to AI systems |
| **Governance use case** | Provides the vulnerability classification taxonomy for red-teaming findings. Enables tracking of known AI vulnerabilities relevant to the organization's AI systems. Supports the security vulnerability trigger in the revalidation schedule (OPS-REVAL-E05). Feeds into the OWASP Top 10 mitigation monitoring |
| **Integration points** | Public database; structured data format for integration with vulnerability management tools; community contribution for discovered vulnerabilities |
| **License** | Open (community-maintained) |
| **When to choose** | Should be monitored by all organizations deploying AI systems; integrate AVID monitoring into the security operations workflow |

---

## 8. Tool Selection Matrix

The following matrix maps governance capabilities to tools, helping organizations identify coverage gaps and select tools based on governance requirements.

| Governance Capability | Giskard | MS RAI | DeepEval | RAGAS | NeMo | Guardrails AI | LlamaGuard | LangSmith | Arize | Opik | Langfuse | Noma AI | Straiker |
|----------------------|---------|--------|----------|-------|------|---------------|------------|-----------|-------|------|----------|---------|----------|
| Automated eval generation | X | | | | | | | | | | | | |
| Fairness testing | X | X | | | | | | | | | | | |
| Explainability | | X | | | | | | | | | | | |
| LLM output evaluation | | | X | | | | | | | | | | |
| RAG quality evaluation | | | X | X | | | | | X | | | | |
| Runtime input guardrails | | | | | X | | X | | | | | | |
| Runtime output validation | | | | | X | X | X | | | | | | |
| Content safety classification | | | | | | | X | | | | | | |
| Production tracing | | | | | | | | X | X | X | X | | |
| Drift detection | | | | | | | | | X | | | | |
| Cost monitoring | | | | | | | | X | | X | X | | |
| Prompt injection testing | | | | | | | | | | | | X | X |
| Agent permission testing | | | | | | | | | | | | | X |
| Tool-use vulnerability testing | | | | | | | | | | | | X | X |

---

## Cross-References

- **Eval-Driven Development:** [../02-development-governance/evaluations/eval-driven-development.md](../02-development-governance/evaluations/eval-driven-development.md) -- tools support the eval-driven methodology
- **Pre-Deployment Gate:** [../02-development-governance/checklists/pre-deployment-gate.yaml](../02-development-governance/checklists/pre-deployment-gate.yaml) -- tools generate evidence for gate items
- **Continuous Online Evaluation:** [../03-runtime-governance/evaluations/continuous-online-evaluation.md](../03-runtime-governance/evaluations/continuous-online-evaluation.md) -- observability tools implement production monitoring
- **Periodic Revalidation Schedule:** [../04-operational-governance/evaluations/periodic-revalidation-schedule.yaml](../04-operational-governance/evaluations/periodic-revalidation-schedule.yaml) -- tools execute scheduled revalidations
- **OWASP Top 10 LLM Guide:** [../04-operational-governance/guides/owasp-top10-llm-guide.md](../04-operational-governance/guides/owasp-top10-llm-guide.md) -- red-teaming tools address OWASP vulnerabilities
- **AI Incident Report:** [../04-operational-governance/templates/ai-incident-report.md](../04-operational-governance/templates/ai-incident-report.md) -- observability tools provide trace evidence for incidents
- **RACI Matrix:** [governance-roles-raci.md](governance-roles-raci.md) -- who selects and operates each tool category
- **SAFEST Compliance Tracker:** [../04-operational-governance/regulatory/safest-compliance-tracker.yaml](../04-operational-governance/regulatory/safest-compliance-tracker.yaml) -- maps tools to SAFEST items

---

*Last updated: 2026-02-28*
*Version: 1.0*
*Classification: Internal / Regulatory Preparation*
