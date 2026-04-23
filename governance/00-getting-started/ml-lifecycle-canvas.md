# ML / AI Product Lifecycle Canvas — ProtoLabs Agentic DFM Edition

## Purpose

The Lifecycle Canvas is a one-page snapshot of your AI product's key dimensions -- from business value to governance profile. It forces you to think through the full lifecycle before committing resources, and it serves as the foundational reference document for all governance activities that follow.

This edition is tailored for the ProtoLabs Product Office agent system: LLM-based agents with RAG over manufacturing knowledge bases, multi-agent orchestration, tool-use capabilities, and regulated-mode compliance routing for aerospace, medical, and defense verticals.

## When to Use

- At the start of any new AI product initiative, before development begins
- When an existing AI product is being significantly redesigned or its scope is expanding
- During annual governance reviews to verify that the canvas still reflects reality
- When onboarding new team members who need to understand the product's governance context

## Who Is Responsible

| Role | Responsibility |
|------|---------------|
| Product Owner | Fills out Product Vision and Evaluation Strategy sections |
| ML/AI Engineer | Fills out AI/ML Approach and Deployment & Operations sections |
| Ethics/Risk Lead | Fills out Risk & Ethics section |
| Governance Lead | Fills out Governance Profile section and reviews the complete canvas |

## Regulatory Basis

EU AI Act Article 9 (Risk Management System) requires a systematic process to identify, analyze, and mitigate risks. This canvas serves as the initial risk identification and product scoping artifact. NIST AI RMF 1.0 and ISO/IEC 42001 expect documented understanding of AI system scope, purpose, and risk profile before development begins.

---

## Instructions

1. **Gather the right people.** This canvas works best as a collaborative exercise with the Product Owner, lead engineer, and risk/compliance representative.
2. **Fill out each section honestly.** Mark unknowns as "TBD -- to be determined by [date]" rather than guessing. Unknown risks are more dangerous than known ones.
3. **Keep it to one page.** The canvas is a summary, not a specification. Link to detailed documents where depth is needed.
4. **Review and update quarterly** or whenever the product scope changes significantly.
5. **Store the completed canvas** in the product's governance folder and reference it from all pillar-specific artifacts.

---

## Canvas Template

### Section 1: Product Vision

| Dimension | Your Product |
|-----------|-------------|
| **Problem Statement** | What specific problem does this AI product solve? For whom? |
| **Target Users** | Who interacts with or is affected by this AI system? (Direct users, indirect stakeholders, impacted populations) |
| **Value Proposition** | Why is AI the right approach? What does AI enable that was not possible or practical before? |
| **Success Criteria** | How will you know this product is successful? (Business metrics, user outcomes) |
| **Scope Boundaries** | What does this AI product explicitly NOT do? Where are the boundaries of its authority? |

### Section 2: AI/ML Approach

| Dimension | Your Product |
|-----------|-------------|
| **Model Type** | Foundation model (which?), fine-tuned model, custom-trained, hybrid, multi-agent system? |
| **Data Sources** | What training/grounding data is used? Where does it come from? How is it refreshed? |
| **Training Strategy** | Pre-trained + fine-tuned, RAG, prompt engineering, RLHF, or combination? |
| **Agent Architecture** | Single agent, multi-agent orchestration, tool-using agent? Describe the delegation chain. |
| **Skill Manifest** | Which skills does this agent load? Link to skill-manifest.yaml. |
| **Tool-Use Registry** | What tools can the agent invoke? (CAD parser, material database, quote API, etc.) |
| **KB Grounding Contract** | Which knowledge-base articles are loaded? How is source citation enforced? Link to source-grounding-data-contract.yaml. |
| **Capability Boundaries** | What can this agent NOT do? What actions are explicitly forbidden? (e.g., no binding quotes, no CAD file modification, no autonomous customer communication) |
| **Key Technical Decisions** | What are the most impactful technical choices (model selection, context window, temperature, etc.)? |
| **Known Limitations** | What does the model/system do poorly? Where are the known failure modes? |

### Section 3: Risk & Ethics

| Dimension | Your Product |
|-----------|-------------|
| **EU AI Act Risk Tier** | Unacceptable / High / Limited / Minimal -- with justification. See `01-discovery-governance/eu-ai-act-risk-classification.yaml` |
| **Fairness Considerations** | Which populations could be disproportionately affected? What protected attributes are relevant? |
| **Transparency Requirements** | Must users know they are interacting with AI? What disclosure obligations apply? |
| **Autonomy Level** | Fully autonomous / Human-in-the-loop / Human-on-the-loop / Human-in-command? |
| **Harm Scenarios** | What is the worst thing this system could do? List the top 3 harm scenarios with severity and likelihood. |
| **Data Privacy** | What personal data is processed? GDPR basis? Data retention policy? |

### Section 4: Evaluation Strategy

| Dimension | Your Product |
|-----------|-------------|
| **Product Metrics** | Business KPIs (conversion, satisfaction, resolution rate, etc.) |
| **AI Quality Metrics** | Accuracy, precision/recall, hallucination rate, latency, consistency, etc. |
| **Agentic Metrics** | Tool-use correctness, delegation accuracy, KB citation accuracy, skill manifest compliance, prompt versioning coverage |
| **Safety Metrics** | Harmful output rate, guardrail trigger rate, escalation rate, jailbreak resistance, `{{#regulated}}` activation accuracy |
| **Fairness Metrics** | Demographic parity, equalized odds, or other fairness criteria across protected groups |
| **Acceptance Criteria** | What must be true before this product can go to production? Quantify the bar. |
| **Eval Cadence** | How often are evals run? (Every commit, daily, weekly, on-demand?) |

### Section 5: Governance Profile

| Dimension | Your Product |
|-----------|-------------|
| **Governance Intensity** | Light / Standard / Intensive -- based on risk tier (see table below) |
| **Key Checkpoints** | Which governance gates apply? (Discovery Gate, Development Gate, Deployment Gate, Periodic Review) |
| **Accountable Roles** | Who has final accountability for governance compliance? (Name + role) |
| **Regulatory Requirements** | Specific regulatory articles and obligations that apply |
| **Audit Frequency** | How often is a formal governance audit conducted? |

**Governance Intensity Guide:**

| Risk Tier | Governance Intensity | Required Gates | Audit Frequency |
|-----------|---------------------|----------------|-----------------|
| Minimal | Light | Discovery Gate, Deployment Gate | Annual |
| Limited | Standard | All four gates | Semi-annual |
| High | Intensive | All four gates + continuous monitoring + external audit | Quarterly |
| Unacceptable | Do not proceed | N/A -- system must be redesigned or abandoned | N/A |

### Section 6: Deployment & Operations

| Dimension | Your Product |
|-----------|-------------|
| **Deployment Strategy** | Canary, blue-green, shadow mode, gradual rollout? |
| **Monitoring Plan** | What is monitored in production? (Latency, error rate, guardrail triggers, drift indicators, KB freshness compliance) |
| **Rollback Procedure** | How do you revert to the previous version? What triggers a rollback? |
| **Escalation Path** | When the agent cannot handle a situation, what happens? (Human handoff, fallback system, graceful degradation) |
| **Regulatory Mode Triggers** | Which keywords activate `{{#regulated}}` and load compliance KBs? (ITAR, EAR, AS9100D, ISO 13485, etc.) |
| **KB Freshness SLA** | Maximum staleness for cached KB articles (e.g., 90 days). How is staleness detected and remediated? |
| **Decommissioning Plan** | When and how would this system be shut down? What happens to users? What happens to data, KB archives, and agent identities? |

---

## Example: CNC Machining DFM Analysis Agent

Below is a completed canvas for the CNC Machining DFM Analysis Agent, a ProtoLab agent that evaluates customer part designs against CNC manufacturability rules.

### Section 1: Product Vision

| Dimension | CNC Machining DFM Agent |
|-----------|------------------------|
| **Problem Statement** | Customers submit part designs that may contain manufacturability issues (tight tolerances, thin walls, deep holes). Manual DFM review by applications engineers is slow and inconsistent. The agent provides instant, consistent DFM feedback grounded in ProtoLabs manufacturing guidance. |
| **Target Users** | Direct: Customer engineers uploading CAD files or part descriptions. Indirect: ProtoLabs applications engineers who review agent output before quoting. |
| **Value Proposition** | AI-driven DFM review reduces quote turnaround time from hours to minutes, improves consistency across reviewers, and catches manufacturability issues early -- before they reach the shop floor. |
| **Success Criteria** | DFM accuracy > 95% on golden fixture (4-defect bracket), quote turnaround time reduced by 70%, customer satisfaction score > 4.2/5.0 on DFM feedback usefulness. |
| **Scope Boundaries** | The agent evaluates manufacturability and recommends design changes. It does NOT generate binding quotes, modify customer CAD files, or make go/no-go production decisions. All recommendations are advisory; human engineers validate before quoting. |

### Section 2: AI/ML Approach

| Dimension | CNC Machining DFM Agent |
|-----------|------------------------|
| **Model Type** | LLM-based agent (Claude Sonnet 4) with RAG over ProtoLabs CNC machining knowledge base |
| **Data Sources** | Cached ProtoLabs KB articles (59 articles across CNC, injection molding, sheet metal, 3D printing, materials, compliance), customer part descriptions, optional CAD file metadata |
| **Training Strategy** | Prompt engineering + RAG retrieval; no model fine-tuning. KB articles refreshed quarterly via `pl-refresh-kb` command. |
| **Agent Architecture** | Multi-agent orchestration: `dfm-router` classifies intent → `cnc-machining` agent loads skill manifest → RAG retrieves relevant KB articles → agent generates DFM evaluation with source citations |
| **Skill Manifest** | `cnc-machining-dfm` skill with capability boundaries: advisory only, no binding quotes, no CAD modification. See `protolabs/agents/cnc-machining/skill-manifest.yaml` |
| **Tool-Use Registry** | CAD parser (read-only metadata extraction), material database lookup, KB retrieval. No write access to customer data or quote systems. |
| **KB Grounding Contract** | 14 CNC machining KB articles + 3 compliance KBs (ITAR/EAR, AS9100D, ISO 9001) when regulated keywords detected. Source citation enforced: every claim cites `knowledge/<folder>/<article>.md` + original ProtoLabs URL. See `protolabs/source-grounding-data-contract.yaml` |
| **Capability Boundaries** | Advisory only -- cannot generate binding quotes, modify CAD files, or communicate directly with customers. Cannot override human engineering judgment. Cannot process classified or export-controlled data without compliance guardrail activation. |
| **Key Technical Decisions** | Temperature 0.3 for consistency; max 5 KB articles retrieved per query; source citation enforced via `source-grounding-data-contract.yaml`; `{{#regulated}}` pattern activates compliance KB loading for ITAR/EAR/aerospace/medical keywords |
| **Known Limitations** | Cannot interpret actual CAD geometry (only metadata); may hallucinate DFM rules not present in KB; limited to English-language queries; does not account for ProtoLabs real-time capacity or material availability |

### Section 3: Risk & Ethics

| Dimension | CNC Machining DFM Agent |
|-----------|------------------------|
| **EU AI Act Risk Tier** | **Limited** -- Advisory system for manufacturing design review. Does not make binding decisions affecting legal/financial rights. Would escalate to **High** if autonomy extended to binding quote generation. |
| **Fairness Considerations** | DFM rules may not account for all customer design contexts (prototyping vs. production volumes). Small customers may receive same guidance as large enterprise customers without volume-based nuance. |
| **Transparency Requirements** | Users must know they are interacting with AI (EU AI Act Art. 52). Every DFM claim must cite the KB source article and original ProtoLabs URL. Agent must disclose it is advisory, not a substitute for human engineering review. |
| **Autonomy Level** | Human-in-the-loop -- all agent output is reviewed by applications engineers before customer communication. Agent cannot autonomously send recommendations to customers. |
| **Harm Scenarios** | (1) Agent misses a critical manufacturability issue, leading to scrap or rework. Severity: Medium; Likelihood: Low (human review catches most). (2) Agent cites stale KB article with outdated design rule, misleading customer. Severity: Medium; Likelihood: Low (KB freshness SLA: 90 days). (3) Customer uploads ITAR-controlled CAD file; agent processes without compliance guardrail. Severity: High; Likelihood: Very Low (regulated keyword detection + `{{#regulated}}` pattern). |
| **Data Privacy** | Processes customer part descriptions and optional CAD metadata (GDPR Art. 6(1)(b) -- contractual necessity). No personal data retained beyond session context. CAD files processed in-memory, not stored. |

### Section 4: Evaluation Strategy

| Dimension | CNC Machining DFM Agent |
|-----------|------------------------|
| **Product Metrics** | Quote turnaround time, customer satisfaction score, applications engineer review time, DFM issue catch rate |
| **AI Quality Metrics** | Hallucination rate < 2%, source citation accuracy > 98%, latency P99 < 15s per DFM evaluation, KB retrieval relevance score > 4.0/5.0 |
| **Safety Metrics** | Guardrail trigger rate (regulated keyword detection), `{{#regulated}}` activation accuracy, human escalation rate, adversarial prompt bypass rate < 0.5% |
| **Agentic Metrics** | Tool-use correctness (CAD parser invocation accuracy), delegation accuracy (router → correct specialist agent), KB freshness compliance (articles within 90-day SLA) |
| **Fairness Metrics** | Consistency score across customer segments (small vs. enterprise), geographic region coverage of DFM rules |
| **Acceptance Criteria** | All quality metrics met on golden fixture (4-defect bracket) AND 2-week shadow mode with zero critical safety violations AND 100% `{{#regulated}}` activation accuracy on compliance test set |
| **Eval Cadence** | Full eval suite on every prompt/system prompt change. Continuous monitoring of production metrics (real-time). Quarterly KB accuracy audit. |

### Section 5: Governance Profile

| Dimension | CNC Machining DFM Agent |
|-----------|------------------------|
| **Governance Intensity** | **Standard** -- Limited-risk AI system under EU AI Act with manufacturing compliance overlays (ITAR, EAR, AS9100D, ISO 13485 when regulated keywords fire) |
| **Key Checkpoints** | Discovery Gate (completed), Development Gate (per prompt change), Deployment Gate (per release), Monthly Periodic Review |
| **Accountable Roles** | Head of Product Office (ultimate accountability), Lead DFM Engineer (operational), AI Engineering Lead (technical), Compliance Officer (regulatory) |
| **Regulatory Requirements** | EU AI Act Art. 52 (transparency). ITAR 22 CFR 120-130 (when defense keywords detected). EAR 15 CFR 730-774 (when dual-use keywords detected). AS9100D (when aerospace keywords detected). ISO 13485/FDA 21 CFR 820 (when medical keywords detected). |
| **Audit Frequency** | Internal: Semi-annual. External: Annual (by independent auditor for ITAR/EAR compliance). |

### Section 6: Deployment & Operations

| Dimension | CNC Machining DFM Agent |
|-----------|------------------------|
| **Deployment Strategy** | Shadow mode (2 weeks, parallel with human reviewers) then canary (10% of new intake for 1 week) then full rollout |
| **Monitoring Plan** | Real-time: latency, error rate, guardrail triggers, `{{#regulated}}` activations. Daily: hallucination rate (sampled), source citation accuracy (sampled). Weekly: KB freshness compliance, applications engineer override rate. |
| **Rollback Procedure** | Automated rollback if hallucination rate exceeds 5% or `{{#regulated}}` activation accuracy drops below 100% for 1 hour. Manual rollback via deployment pipeline. Rollback target: previous prompt version (always versioned in git). |
| **Escalation Path** | Regulated keyword detected: immediate human review + compliance KB loaded. High-confidence DFM issue: flag for applications engineer review within 15 minutes. Low-confidence or ambiguous query: graceful degradation to "please contact applications engineering." |
| **Decommissioning Plan** | If decommissioned, revert to human-only DFM review process. Customer data retained per GDPR retention policy (7 years for business records). KB articles archived. Agent skill manifest and prompt versions retained for audit (7 years). NHI deprovisioned per `machine-identity-nhi.md`. |

---

*After completing this canvas, proceed to the relevant governance pillar based on your product's lifecycle phase. For new products, start with [Discovery Governance](../01-discovery-governance/). For products already in development, jump to [Development Governance](../02-development-governance/).*
