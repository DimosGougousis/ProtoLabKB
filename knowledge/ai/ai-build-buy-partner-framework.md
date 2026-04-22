---
type: knowledge-article
category: ai
source_url: https://hbr.org/2023/10/build-buy-or-partner-for-ai-capabilities
fetched_at: 2026-04-22
summary: Strategic framework for AI capability sourcing decisions - build internally, buy from vendors, or partner with specialists based on strategic importance, capability uniqueness, and time-to-market requirements.
---

# AI Build/Buy/Partner Framework

## Overview

Organizations face critical decisions about how to acquire AI capabilities. This framework provides structured guidance for choosing between building internally, buying from vendors, or partnering with specialists.

## The Three Sourcing Strategies

| Strategy | Definition | Best For | Risk Level |
|----------|------------|----------|------------|
| **Build** | Develop AI capabilities in-house | Core differentiators, proprietary data | High |
| **Buy** | Purchase off-the-shelf AI solutions | Commodity capabilities, speed | Low |
| **Partner** | Collaborate with AI specialists | Complex needs, hybrid approach | Medium |

## Decision Framework

### Strategic Importance Axis

**Core to Competitive Advantage**
- Proprietary algorithms
- Unique data assets
- Customer-facing differentiators
- → **BUILD**

**Important but Not Differentiating**
- Operational efficiency
- Cost reduction
- Standard use cases
- → **BUY**

**Complex or Novel Requirements**
- Cutting-edge research
- Specialized domains
- Rapid experimentation
- → **PARTNER**

### Capability Uniqueness Axis

**Highly Proprietary**
- Custom manufacturing processes
- Unique compliance requirements
- Proprietary design methodologies
- → **BUILD**

**Industry Standard**
- Document processing
- Customer service chatbots
- Generic analytics
- → **BUY**

**Emerging/Specialized**
- Novel AI architectures
- Domain-specific models
- Research collaborations
- → **PARTNER**

### Time-to-Market Axis

**Long-term Investment OK**
- 12-24 month timeline acceptable
- Strategic capability building
- → **BUILD**

**Immediate Need**
- 0-3 month requirement
- Competitive pressure
- → **BUY**

**Medium-term with Flexibility**
- 3-12 month timeline
- Iterative development
- → **PARTNER**

## Build Strategy

### When to Build
- AI is core to competitive advantage
- Proprietary data provides unique advantage
- Regulatory requirements demand control
- Long-term capability building prioritized

### Requirements for Success
- **Talent**: ML engineers, data scientists, AI researchers
- **Data**: High-quality, proprietary datasets
- **Infrastructure**: Compute resources, MLOps platforms
- **Time**: 12-24 months to production
- **Budget**: $2M-$10M+ annual investment

### Protolabs Examples
- **DFM Engine**: Proprietary design-for-manufacturability algorithms
- **Pricing Optimization**: Unique cost modeling based on internal data
- **Quality Prediction**: Custom models trained on production data

### Risks
- Talent acquisition and retention
- Technical debt accumulation
- Opportunity cost of delayed deployment
- Maintenance burden

## Buy Strategy

### When to Buy
- Commodity AI capabilities
- Speed to market critical
- Limited internal AI expertise
- Standard use cases

### Vendor Categories

| Category | Examples | Use Cases |
|----------|----------|-----------|
| **Cloud AI Services** | AWS Bedrock, Azure OpenAI, GCP Vertex | General-purpose LLMs, embeddings |
| **Vertical SaaS** | Salesforce Einstein, ServiceNow AI | CRM, ERP, workflow automation |
| **Specialized Tools** | Gong, Moveworks, Ada | Sales, IT, customer service |
| **Model Providers** | OpenAI, Anthropic, Cohere | API access to foundation models |

### Evaluation Criteria
- **Performance**: Accuracy, latency, throughput
- **Security**: Data handling, compliance certifications
- **Integration**: APIs, SDKs, existing stack compatibility
- **Support**: SLAs, customer success, documentation
- **Cost**: Per-token, per-request, or subscription pricing

### Protolabs Examples
- **Document Processing**: AWS Textract for PO processing
- **Customer Support**: Zendesk AI for ticket routing
- **Code Generation**: GitHub Copilot for development

### Risks
- Vendor lock-in
- Limited customization
- Data privacy concerns
- Pricing changes

## Partner Strategy

### When to Partner
- Complex requirements spanning build and buy
- Access to specialized expertise
- Risk sharing for novel applications
- Accelerated development timeline

### Partnership Models

| Model | Structure | Best For |
|-------|-----------|----------|
| **Joint Development** | Co-create custom solution | Unique requirements, shared IP |
| **System Integrator** | Implementation partner | Deployment, integration |
| **Research Collaboration** | University/industry lab | Cutting-edge research |
| **Managed Service** | Outsourced AI operations | Ongoing operations, maintenance |

### Partnership Evaluation
- **Alignment**: Strategic fit, cultural compatibility
- **Capability**: Technical expertise, domain knowledge
- **Track Record**: Past successes, references
- **Terms**: IP ownership, exclusivity, exit clauses

### Protolabs Examples
- **University Research**: Collaboration on novel manufacturing AI
- **SI Partnership**: Implementation of ERP AI modules
- **Startup Collaboration**: Pilot of emerging AI technologies

### Risks
- Dependency on partner
- IP and data sharing concerns
- Misaligned incentives
- Integration complexity

## Canonical AI Axes

### Sourcing Axis
```
Build ←————————————————→ Buy
  ↑                        ↑
Core diff.              Commodity
Proprietary data        Standard use cases
Long timeline           Speed critical
```

### Topology Axis
```
Single-Agent ←——————————→ Graph
     ↑                      ↑
Simple tasks          Complex workflows
Low cost              High reliability
Fast deployment       Audit requirements
```

### Model Sourcing Axis
```
Closed SaaS ←———————————→ Open Self-Hosted
      ↑                        ↑
Ease of use              Control
Managed infra            Customization
Standard models          Fine-tuning
```

### Data Strategy Axis
```
RAG ←——————————————————→ Fine-tune
  ↑                        ↑
Dynamic data             Static knowledge
No retraining            Custom behavior
Lower cost             Higher accuracy
```

## Implementation Decision Matrix

| Scenario | Strategy | Example |
|----------|----------|---------|
| Core DFM algorithm | Build | Proprietary manufacturability engine |
| Customer chatbot | Buy | Zendesk AI integration |
| Novel quality prediction | Partner | University research collaboration |
| Document processing | Buy | AWS Textract API |
| Pricing optimization | Build | Internal cost models |
| Compliance checking | Partner | Legal tech vendor + customization |

## Governance Model

### Decision Authority
- **CTO/CIO**: Strategic sourcing decisions
- **VP Engineering**: Technical feasibility assessment
- **CFO**: Budget and ROI approval
- **Legal**: IP, data, compliance review

### Review Cadence
- **Quarterly**: Sourcing strategy review
- **Annually**: Vendor/partner performance evaluation
- **Ad-hoc**: New capability needs assessment

### Documentation Requirements
- Business case for build decisions
- Vendor evaluation for buy decisions
- Partnership agreements for partner decisions

## References
- Harvard Business Review. (2023). Build, Buy, or Partner for AI.
- McKinsey. (2024). AI sourcing strategies for enterprises.
- MIT Sloan Management Review. (2024). The new AI capability stack.
