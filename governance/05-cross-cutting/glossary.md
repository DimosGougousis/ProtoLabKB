# Unified Glossary

## Purpose

This glossary provides consistent definitions for terminology used across the governance framework. It bridges the vocabulary gaps between governance, AI/ML engineering, LLM operations, regulatory compliance, evaluation, and agentic AI workflows.

## When to Use

Reference this glossary when encountering unfamiliar terms in any framework artifact, or when writing new artifacts to ensure consistent terminology.

## Who Is Responsible

The Governance Lead maintains this glossary. All contributors are expected to use terms consistently with these definitions and to propose additions when new terminology is introduced.

## Regulatory Basis

Best practice -- consistent terminology reduces misunderstanding and improves compliance accuracy. EU AI Act Article 3 establishes key definitions for regulatory purposes; this glossary extends those definitions into practical governance context.

---

## Governance Terms

**Three Lines of Defense**
A risk governance model where the first line (business operations) owns and manages risk, the second line (risk management and compliance) provides oversight and frameworks, and the third line (internal audit) provides independent assurance.

**RACI Matrix**
A responsibility assignment chart that defines who is Responsible (does the work), Accountable (makes the final decision), Consulted (provides input), and Informed (is kept updated) for each governance activity.

**Quality Gate**
A mandatory checkpoint in the AI product lifecycle where predefined criteria must be met before proceeding to the next phase. Gates require evidence, not just assertions.

**Governance Profile**
A product-level document that defines the governance intensity, applicable checkpoints, accountable roles, and regulatory requirements for a specific AI system, based on its risk tier and use case.

**Governance Intensity**
The level of rigor applied to governance activities for a given AI product. Ranges from Light (minimal-risk systems) through Standard (limited-risk) to Intensive (high-risk). Determined by the EU AI Act risk tier and organizational risk appetite.

**Discovery Gate**
The governance checkpoint at the end of the Discovery phase. Validates that the AI product opportunity has been assessed for risk, ethics, feasibility, and alignment with organizational strategy before development begins.

**Deployment Gate**
The governance checkpoint before an AI system enters production. Validates that development governance requirements (evals, bias testing, documentation) are satisfied and runtime governance controls are in place.

**Evidence Reference**
A pointer to a concrete artifact (document, test result, tool output, signed approval) that demonstrates a governance requirement has been met. Governance without evidence is governance theater.

**Governance Theater**
The practice of having governance processes on paper without meaningful implementation or enforcement. Characterized by unchecked checkboxes, rubber-stamp approvals, and missing evidence.

**Risk Appetite**
The level and type of risk an organization is willing to accept in pursuit of its objectives. Defines the boundary between acceptable and unacceptable risk for AI deployments.

**Risk Register**
A structured record of identified risks, their likelihood, impact, mitigation strategies, and current status. Maintained throughout the AI product lifecycle.

---

## AI / ML Terms

**Model Card**
A standardized document that describes a machine learning model's intended use, performance characteristics, limitations, ethical considerations, and evaluation results. Originated from Google's "Model Cards for Model Reporting" paper.

**Data Sheet (for Datasets)**
A standardized document describing a dataset's motivation, composition, collection process, preprocessing, intended uses, distribution, and maintenance. Analogous to a model card but for data.

**Model Drift**
A degradation in model performance over time caused by changes in the underlying data distribution (data drift), changes in the relationship between inputs and outputs (concept drift), or changes in the real-world context the model operates in.

**Data Drift**
A change in the statistical distribution of input data compared to the data the model was trained on. Detected through monitoring input feature distributions over time.

**Concept Drift**
A change in the relationship between input features and the target variable. The world has changed in a way that makes the model's learned patterns less accurate.

**Bias (in AI)**
Systematic and unfair discrimination in AI system outputs, often reflecting or amplifying biases present in training data, feature selection, or model design. Can manifest as disparate impact across demographic groups.

**Fairness**
The principle that an AI system's predictions or decisions should not systematically disadvantage individuals or groups based on protected attributes (race, gender, age, etc.). Multiple mathematical definitions exist (demographic parity, equalized odds, calibration), and they can conflict.

**Demographic Parity**
A fairness criterion requiring that the positive prediction rate is equal across all demographic groups. Simple to understand but does not account for legitimate differences in base rates.

**Equalized Odds**
A fairness criterion requiring that true positive rates and false positive rates are equal across demographic groups. Stronger than demographic parity but harder to achieve.

**Feature Importance**
A measure of how much each input feature contributes to a model's predictions. Used for explainability and for identifying potential proxy variables for protected attributes.

**Ground Truth**
The correct or actual outcome used to evaluate model predictions. The quality of ground truth labels directly determines the reliability of evaluation metrics.

**Overfitting**
When a model learns the noise in its training data rather than the underlying patterns, resulting in strong performance on training data but poor generalization to new data.

**Training-Serving Skew**
A discrepancy between the data or feature engineering used during model training and what is available during production inference. A common and often subtle source of model failures.

---

## Agentic AI Terms (New)

**SPIFFE (Secure Production Identity Framework For Everyone)**
A standard for securely identifying software systems in dynamic and orchestrated environments. SPIFFE provides short-lived, automatically rotated, cryptographically verifiable identities for workloads such as AI agents.

**SPIRE (SPIFFE Runtime Environment)**
The reference implementation of SPIFFE. SPIRE issues SPIFFE Verifiable Identity Documents (SVIDs) to workloads and automatically rotates them based on configured time-to-live (TTL) policies.

**SVID (SPIFFE Verifiable Identity Document)**
A document that proves a workload's identity in a SPIFFE system. SVIDs can be X.509 certificates or JWT tokens containing the workload's SPIFFE ID.

**OPA (Open Policy Agent)**
An open-source, general-purpose policy engine that enables unified, context-aware policy enforcement across the entire stack. Used for compliance-as-configuration in the governance enforcement pipeline.

**Cedar**
An open-source policy language and evaluation engine developed by AWS. Cedar is designed for authorization use cases and can express policies for who can do what to which resources in an application.

**Rego**
The policy language used by Open Policy Agent (OPA). Rego is a declarative language for expressing policy over complex hierarchical data structures.

**Skill Manifest**
A YAML document that declares per-skill metadata including permissions, budget constraints, model routing preferences, HITL configuration, and circuit breaker settings. Enables granular governance at the skill level.

**Circuit Breaker**
A design pattern that prevents cascade failures by automatically stopping requests to failing components. In agent governance, circuit breakers implement the Throttle/Pause/Full Stop escalation model mapped to MI9 containment levels.

**Bulkhead Pattern**
A design pattern that isolates failures to prevent them from spreading. In multi-agent systems, bulkheads ensure that stopping one agent does not affect others.

**Semantic Deduplication**
A technique for identifying and removing semantically similar content from RAG indices or training data to improve quality and reduce redundancy.

**Compliance-as-Configuration**
The practice of defining compliance rules in machine-readable format (YAML) that are evaluated by policy engines (OPA/Cedar) at runtime, transforming compliance from documentation into executable code.

**Shadow AI**
Unauthorized AI agents operating outside governance oversight, without proper registration, safety controls, or audit logging. Shadow AI detection is a critical governance activity.

**Context Isolation**
One of the 6 layers of multi-tenant isolation ensuring that RAG indices, vector stores, and conversation history are scoped to individual tenants and cannot leak between them.

**Reasoning Isolation**
One of the 6 layers of multi-tenant isolation ensuring that agent reasoning traces, chain-of-thought, and intermediate outputs are isolated per tenant.

**Audit vs Observability**
The critical distinction between audit logs (compliance evidence, 7+ year retention, cryptographic integrity) and observability telemetry (operational health, 30-90 day retention, no integrity guarantees).

**Integrity Chain**
A cryptographic mechanism where each audit record includes a hash of the previous record, creating a tamper-evident chain. Any modification to historical records breaks the chain and is detectable.

**Kill Switch**
An emergency mechanism to immediately halt agent execution. The 3-level model (Throttle/Pause/Full Stop) maps to MI9 containment levels for graduated safety response.

**HITL Confidence Scoring**
A composite formula combining log probability (40%), self-assessment (40%), and semantic distance (20%) to determine when human oversight is required and at what authority level (A1-A4).

---

## LLM-Specific Terms

**Hallucination**
When a large language model generates text that is fluent and confident but factually incorrect, fabricated, or unsupported by any source. Distinct from errors of reasoning -- hallucinations present fiction as fact.

**Prompt Injection**
An attack where malicious input is crafted to override, bypass, or manipulate an LLM's system instructions or safety controls. Analogous to SQL injection but targeting natural language interfaces.

**Direct Prompt Injection**
A prompt injection attack delivered directly by the user through the primary input channel (e.g., typing adversarial text into a chatbot).

**Indirect Prompt Injection**
A prompt injection attack delivered through secondary data sources that the LLM processes (e.g., malicious instructions hidden in a document, email, or web page that the agent retrieves).

**Guardrail**
A programmatic control that constrains an AI system's behavior at runtime. Guardrails can operate on inputs (filtering harmful prompts), outputs (blocking harmful responses), or actions (preventing unauthorized operations).

**Safety Rail**
A subset of guardrails specifically designed to prevent harmful, dangerous, or illegal outputs. Safety rails address content safety (violence, self-harm, illegal activity), factual grounding (preventing hallucinations), and behavioral boundaries (preventing manipulation).

**System Prompt**
The initial set of instructions given to an LLM that define its role, personality, boundaries, and behavioral constraints. The system prompt is the primary governance interface for LLM-based agents.

**Grounding**
The practice of connecting an LLM's responses to verified factual sources (databases, documents, APIs) to reduce hallucination. RAG (Retrieval-Augmented Generation) is the most common grounding technique.

**Retrieval-Augmented Generation (RAG)**
An architecture pattern where an LLM retrieves relevant documents from a knowledge base before generating a response, grounding its output in specific source material.

**Temperature**
A parameter controlling the randomness of an LLM's output. Lower temperatures produce more deterministic, focused responses. Higher temperatures produce more creative, varied (and potentially less reliable) responses.

**Token**
The basic unit of text processing for an LLM. Roughly corresponds to a word or word fragment. Token counts determine cost, context window limits, and latency.

**Context Window**
The maximum number of tokens an LLM can process in a single interaction (including system prompt, conversation history, retrieved documents, and the response). Exceeding the context window causes information loss.

**Fine-Tuning**
Adapting a pre-trained LLM to a specific domain or task by training it on additional, targeted data. Produces a specialized model that retains the base model's general capabilities.

**RLHF (Reinforcement Learning from Human Feedback)**
A training technique where human evaluators rate model outputs, and these ratings are used to train a reward model that guides further model optimization. Central to aligning LLMs with human preferences.

**Jailbreak**
A specific type of prompt injection designed to make an LLM bypass its safety training and produce outputs it was designed to refuse (harmful content, policy violations, etc.).

---

## Regulatory Terms

**EU AI Act**
The European Union's comprehensive regulation on artificial intelligence (Regulation (EU) 2024/1689). Establishes a risk-based regulatory framework with obligations scaled to the level of risk an AI system poses.

**EU AI Act Risk Tiers**
Four levels of risk classification under the EU AI Act: (1) Unacceptable risk -- prohibited practices (e.g., social scoring, real-time biometric surveillance); (2) High risk -- systems requiring full compliance regime (e.g., AI in credit decisions, recruitment, critical infrastructure); (3) Limited risk -- transparency obligations only (e.g., chatbots must disclose they are AI); (4) Minimal risk -- no specific obligations beyond voluntary codes of practice.

**High-Risk AI System**
Under the EU AI Act, an AI system that falls within the categories listed in Annex III (biometrics, critical infrastructure, education, employment, essential services, law enforcement, migration, justice) or is a safety component of a product covered by EU harmonization legislation.

**Conformity Assessment**
The process by which it is verified that an AI system meets the requirements of the EU AI Act before it is placed on the market. For most high-risk systems, this is a self-assessment; for certain biometric systems, third-party assessment is required.

**DORA (Digital Operational Resilience Act)**
EU regulation (2022/2554) establishing requirements for ICT risk management, incident reporting, resilience testing, and third-party risk management for financial entities. Relevant because AI systems are ICT systems.

**DNB (De Nederlandsche Bank)**
The Dutch central bank, which acts as a prudential supervisor for financial institutions in the Netherlands. Publishes guidance on the responsible use of AI in financial services.

**SAFEST Framework**
A structured AI safety and governance framework organized around six pillars: Security, Accountability, Fairness, Explainability, Sustainability, and Transparency. Used in this repository as the basis for checklist structure and regulatory mapping.

**GDPR (General Data Protection Regulation)**
EU regulation on data protection and privacy (2016/679). Relevant to AI governance because AI systems process personal data. Key provisions include the right to explanation (Article 22), data minimization, and purpose limitation.

**Right to Explanation**
Under GDPR Article 22, individuals have the right to meaningful information about the logic involved when subject to automated decision-making. The scope and depth of explanation required is still debated legally.

**Supervisory Authority**
A public authority responsible for monitoring the application of the EU AI Act. Each EU member state designates one or more supervisory authorities.

**Technical Documentation**
Under the EU AI Act (Article 11), high-risk AI systems must be accompanied by technical documentation demonstrating compliance with all requirements. This documentation must be kept up-to-date throughout the system's lifecycle.

---

## Evaluation Terms

**Eval Suite**
A structured collection of test cases, benchmarks, and quality metrics used to systematically evaluate an AI system's performance, safety, fairness, and reliability. The AI equivalent of a test suite in traditional software.

**Acceptance Criteria**
Quantitative thresholds that define the minimum acceptable performance for an AI system. Must be defined before development begins and must be met before deployment is authorized.

**A/B Testing**
A controlled experiment comparing two versions of an AI system (A and B) to determine which performs better on specified metrics. Used in both development (comparing model versions) and production (measuring user impact).

**Benchmark**
A standardized dataset or task used to evaluate and compare AI system performance. Benchmarks enable apples-to-apples comparison but may not reflect real-world performance.

**Offline Evaluation**
Evaluation performed on historical or synthetic data before deployment. Includes holdout test sets, cross-validation, and benchmark evaluations. Necessary but not sufficient -- offline performance does not guarantee production performance.

**Online Evaluation**
Evaluation performed on live production traffic. Includes A/B testing, canary analysis, and continuous monitoring of production metrics. Captures real-world dynamics that offline evaluation misses.

**Shadow Mode**
A deployment strategy where the new AI system runs alongside the existing system, processing the same inputs, but its outputs are logged without being shown to users. Enables safe real-world evaluation before live deployment.

**Regression Testing**
Testing that verifies a new version of an AI system has not degraded on previously passing test cases. Prevents improvements in one area from causing regressions in another.

**Red Teaming**
Structured adversarial testing where human testers actively try to find failure modes, safety violations, and edge cases in an AI system. More creative and less predictable than automated testing.

**Golden Dataset**
A carefully curated, human-labeled dataset used as the authoritative reference for evaluation. Quality of the golden dataset determines the trustworthiness of evaluation results.

**Metric**
A quantitative measure used to assess a specific aspect of AI system performance. Good metrics are specific, measurable, aligned with business objectives, and resistant to gaming.

**Continuous Evaluation**
The practice of running evaluation checks against live AI system behavior on an ongoing basis, not just at deployment time. Detects drift, degradation, and emerging failure modes.

---

## Observability and MLOps Terms

**Span**
A unit of work in an LLM observability trace, representing a single step in an agent's reasoning or action pipeline. Spans capture inputs, outputs, latency, tokens consumed, and tool calls for each step. Named by analogy with distributed tracing spans (OpenTelemetry). Observability platforms (LangSmith, Arize Phoenix, Opik, Langfuse) organize agent execution as a tree of spans.

**LangSmith**
An observability and evaluation platform by LangChain for tracing, testing, and monitoring LLM applications. Captures span-level execution traces, supports eval-driven development, and integrates with LangChain/LangGraph pipelines.

**Arize Phoenix**
An open-source observability platform for LLM applications. Provides trace visualization, span analysis, retrieval evaluation (for RAG), and production monitoring. Part of the Arize AI ecosystem.

**Opik**
An open-source LLM evaluation and observability platform by Comet. Supports experiment tracking, automated evaluation, and production trace analysis for LLM applications.

**Langfuse**
An open-source LLM engineering platform providing observability (traces, spans), prompt management, evaluation, and analytics. Self-hostable for regulated industries requiring data sovereignty.

**Data Drift Detection**
The automated process of comparing current input data distributions against training/baseline distributions using statistical tests (PSI, KL divergence, MMD). Triggers alerts when distributions diverge beyond configurable thresholds.

**Prompt Drift**
Behavioral divergence of an LLM agent from its intended prompt behavior over time, caused by model updates, context accumulation, or changing user patterns. Detected by running regression eval suites against the agent's prompt.

**Canary Deployment**
A deployment strategy where a new agent version receives a small percentage of production traffic (typically 5-10%) while the existing version handles the rest. Enables real-world validation with limited blast radius before full rollout.

---

## Agentic Workflow Terms

**Agent**
An AI system that can perceive its environment, make decisions, and take actions to achieve goals. In the context of this framework, an agent is typically an LLM-based system that can use tools, access data, and interact with users or other systems autonomously.

**Multi-Agent System**
An architecture where multiple AI agents collaborate, compete, or coordinate to accomplish tasks. Agents may have different specializations, permissions, and governance requirements.

**Orchestrator Agent**
The primary agent in a multi-agent system that coordinates task delegation, manages workflow, and synthesizes results from sub-agents. The orchestrator bears primary governance accountability for the system's behavior.

**Sub-Agent**
An agent that receives delegated tasks from an orchestrator agent. Sub-agents typically have narrower scope, specific tool access, and more constrained permissions than the orchestrator.

**Delegation Chain**
The sequence of task handoffs from an orchestrator agent through one or more sub-agents. Governance must track the entire chain to ensure accountability is maintained and permissions are not escalated at any link.

**Permission Boundary**
The set of actions an agent is authorized to perform. Defined at design time, enforced at runtime. Permission boundaries should follow the principle of least privilege -- an agent should have only the permissions necessary for its specific task.

**Tool Use**
The ability of an AI agent to invoke external tools (APIs, databases, calculators, code interpreters) to accomplish tasks. Each tool represents both a capability and a risk surface that must be governed.

**Human-in-the-Loop (HITL)**
A design pattern where a human must approve or validate an agent's decision before it is executed. Used for high-stakes decisions where autonomous action poses unacceptable risk.

**Human-on-the-Loop (HOTL)**
A design pattern where a human monitors an agent's decisions and can intervene, but the agent acts autonomously by default. Used for medium-stakes decisions where intervention is possible but not required for every action.

**Human-in-Command (HIC)**
A design pattern where a human retains full strategic control over the AI system's objectives and operational boundaries, but the system operates autonomously within those boundaries. The human can override, pause, or shut down the system at any time.

**Escalation**
The process by which an agent transfers a decision or interaction to a human operator when the agent determines it cannot handle the situation safely, correctly, or within its authorization scope.

**Graceful Degradation**
The ability of an AI system to reduce its functionality in a controlled manner when it encounters problems, rather than failing completely or producing harmful outputs. A well-governed agent degrades gracefully.

**Autonomous Decision-Making**
When an AI agent makes and executes a decision without human involvement. The governance framework must define which decisions can be made autonomously, which require human approval, and what evidence trail is maintained for each.

**Conversation Memory**
The agent's maintained context about prior interactions, including user preferences, previous decisions, and conversation history. Governance must address memory persistence, access controls, and data retention.

**Action Trace**
A detailed log of every action an agent takes, including the reasoning that led to the action, the tools invoked, the inputs provided, and the outputs received. The foundation of auditability for agentic systems.

**Feedback Loop**
A mechanism by which the outcomes of agent actions are fed back into the system to improve future behavior. Governance must ensure feedback loops do not amplify biases or create perverse incentives.

**Non-Human Identity (NHI) / Machine Identity**
The identity assigned to an AI agent in an organization's IAM (Identity and Access Management) system, treating agents as first-class citizens alongside human users. NHI enables least-privilege access control, credential rotation, audit trails, and lifecycle management (provision, activate, operate, review, revoke, decommission) for agents. Essential for regulated environments where every action must be attributable to a specific identity.

**Agentic Tool Sovereignty**
A three-layer governance model for controlling how agents discover, select, and execute tools:
- **Configuration Layer** -- Tool discovery and registration (what tools exist)
- **Policy Layer** -- Tool selection governance (which tools an agent may use, under what conditions)
- **Network Layer** -- Tool execution and sandboxing (how tools run, with what isolation)

**Human-out-of-the-Loop Autonomy (HOTA)**
A design pattern where an AI agent operates fully autonomously with no real-time human oversight. Humans audit retrospectively through logs and eval results. Reserved for minimal-risk, well-validated use cases where the cost of human involvement exceeds the risk of autonomous action (e.g., FAQ responses, information retrieval).

**Agent Fleet**
The collection of all AI agents operating within an organization, managed as a portfolio with centralized visibility into health, performance, compliance, and cost. Analogous to a fleet of vehicles -- each agent is individually managed but fleet-wide patterns and policies apply.

**Agent Registry**
A centralized inventory of all deployed agents containing their identity, capabilities, permissions, KPIs, SLA targets, ownership, risk tier, and compliance status. The single source of truth for what agents exist and who is responsible for them.

**SLA Governance**
The practice of defining, monitoring, and enforcing Service Level Agreements for AI agent performance metrics. Each KPI has a target, warning threshold, and critical threshold, with RACI ownership and escalation procedures for breaches.

---

## Enterprise Governance Terms

**CAIO (Chief AI Officer)**
A C-level executive role accountable for enterprise-wide AI strategy, risk, and governance. The CAIO owns the AI risk framework, chairs or sponsors the AI Governance Committee, reports to the board on AI risk posture, and ensures regulatory compliance across all AI systems.

**Federated Governance**
A governance model where a central governance body (AI Governance Committee, CAIO office) sets approximately 75% of governance standards, policies, and minimum requirements, while local teams (product teams, business units) retain approximately 25% autonomy to adapt governance to their specific context, risk profile, and operational needs.

**Tiered Governance Architecture**
A four-tier organizational model for AI governance:
- **Tier 1 (Strategic)** -- Board and CAIO: portfolio risk posture, regulatory compliance, material incidents
- **Tier 2 (Policy)** -- AI Ethics Board, Compliance: ethics reviews, bias audits, SAFEST completion, regulatory deadlines
- **Tier 3 (Lifecycle)** -- Product Teams: model-level evals, deployment gates, guardrail performance, drift alerts
- **Tier 4 (Runtime)** -- Automated systems: real-time guardrail triggers, boundary violations, escalation events

**ISO/IEC 42001**
An international standard for AI Management Systems (AIMS), based on a Plan-Do-Check-Act (PDCA) model. Specifies requirements for establishing, implementing, maintaining, and continually improving AI management within an organization. Useful for demonstrating governance maturity to regulators and auditors.

**AI Center of Excellence (CoE)**
An organizational unit that centralizes AI expertise, governance standards, and best practices. Can be structured as centralized (all AI governance flows through the CoE), federated (CoE sets standards, teams execute), or hybrid. The CoE typically houses or supports the CAIO function.

---

*This glossary is maintained as a living document. When introducing a new term in any framework artifact, add it here first to ensure consistency across the framework. Propose additions via pull request.*
