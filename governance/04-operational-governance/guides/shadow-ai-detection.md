# Shadow AI Detection Guide

## Purpose

This document provides a systematic process for detecting unauthorized AI agents ("Shadow AI") operating within the organization. Shadow AI refers to AI systems deployed without proper governance oversight, outside the approved agent registry, and potentially bypassing safety controls, audit logging, and compliance requirements.

Early detection of Shadow AI is critical for maintaining governance integrity, preventing compliance violations, and ensuring all AI systems meet organizational safety standards.

## When to Use

- During quarterly governance audits to identify unregistered agents
- When investigating anomalous API usage patterns
- After mergers/acquisitions to assess AI footprint
- When responding to security incidents involving potential AI systems
- When onboarding new business units or teams
- As part of continuous governance monitoring

## Who Is Responsible

| Role | R/A/C/I | Responsibility |
|------|---------|---------------|
| **Security Engineer** | Accountable | Leads Shadow AI detection efforts |
| **MLOps / Platform Engineer** | Responsible | Implements detection tools and scanning |
| **Compliance Officer (2nd Line)** | Responsible | Validates governance onboarding process |
| **AI Governance Committee** | Informed | Reviews findings and approves remediation |
| **Internal Audit (3rd Line)** | Reviewer | Independently validates detection effectiveness |

## Regulatory Basis

- **EU AI Act Article 12** -- Record-keeping obligations for all AI systems
- **EU AI Act Article 72** -- Post-market monitoring requires complete system inventory
- **DORA Article 9** -- ICT risk management including asset inventory
- **SAFEST T-15** -- AI system inventory requirements
- **SOC 2 CC6.1** -- Logical access controls and asset management

---

## 1. Detection Process Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SHADOW AI DETECTION PROCESS                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  PHASE 1: DISCOVERY                                                          │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  1. Network traffic analysis                                        │   │
│  │  2. API key auditing                                                │   │
│  │  3. Cloud resource scanning                                         │   │
│  │  4. Code repository scanning                                          │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                              │                                              │
│                              ▼                                              │
│  PHASE 2: CLASSIFICATION                                                     │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  • Identify potential AI endpoints                                  │   │
│  │  • Cross-reference with approved registry                             │   │
│  │  • Categorize: Shadow, Unregistered, Orphaned                      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                              │                                              │
│                              ▼                                              │
│  PHASE 3: INVESTIGATION                                                      │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  • Determine owner/team                                             │   │
│  │  • Assess risk tier and business purpose                              │   │
│  │  • Evaluate safety/compliance status                                  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                              │                                              │
│                              ▼                                              │
│  PHASE 4: GOVERNANCE ONBOARDING                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  • Register in agent registry                                         │   │
│  │  • Apply appropriate risk tier governance                             │   │
│  │  • Implement monitoring and audit logging                             │   │
│  │  • Retroactive compliance review                                      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Detection Methods

### 2.1 Network Traffic Analysis

**Objective:** Identify API calls to known AI model providers (OpenAI, Anthropic, Azure OpenAI, etc.) from unauthorized sources.

| Detection Technique | Implementation | Coverage |
|---------------------|----------------|----------|
| **DNS Query Monitoring** | Log queries to ai.*, api.openai.com, anthropic.com | All egress traffic |
| **TLS SNI Inspection** | Identify TLS handshakes to AI endpoints | Encrypted traffic |
| **Flow Analysis** | Baseline normal traffic, flag AI-related volumes | Network patterns |
| **Proxy Logs** | Deep inspection of proxied AI API calls | Configured clients |

**Indicators of Shadow AI:**
- API calls to AI endpoints from non-approved IP ranges
- Unusual volume patterns (weekend spikes, off-hours usage)
- Traffic from business units without registered AI projects
- Multiple API keys from same source

**Tools:**
- Zeek/Bro for network analysis
- Splunk/ELK for log correlation
- Custom Python scripts for pattern detection

### 2.2 API Key Auditing

**Objective:** Discover and inventory all AI provider API keys in use.

| Source | Detection Method | Sensitivity |
|--------|------------------|-------------|
| **Code Repositories** | Scan for hardcoded keys in Git | High |
| **Environment Variables** | Audit CI/CD and deployment configs | High |
| **Secret Managers** | Inventory Vault, AWS Secrets Manager, Azure Key Vault | Medium |
| **Browser Extensions** | Detect AI assistant extensions | Medium |
| **Developer Workstations** | Endpoint DLP scanning | Medium |

**Key Scanning Patterns:**
```regex
# OpenAI
sk-[a-zA-Z0-9]{48}

# Anthropic
sk-ant-[a-zA-Z0-9]{32}

# Azure OpenAI
[a-f0-9]{32}

# AWS Bedrock
AKIA[a-zA-Z0-9]{16}
```

**Action on Discovery:**
1. Revoke exposed keys immediately
2. Identify owner through commit history or deployment metadata
3. Determine if usage was authorized (but non-compliant) or truly shadow
4. Force key rotation and migration to approved governance

### 2.3 Cloud Resource Scanning

**Objective:** Identify cloud resources running AI workloads outside approved infrastructure.

| Cloud Service | Detection Target | Method |
|---------------|------------------|--------|
| **AWS** | SageMaker endpoints, Lambda with AI SDKs, EC2 with GPU | AWS Config, CloudTrail |
| **Azure** | Azure ML endpoints, Functions with OpenAI SDK | Azure Policy, Activity Log |
| **GCP** | Vertex AI endpoints, Cloud Functions with AI | Asset Inventory, Audit Logs |
| **Kubernetes** | Pods with AI model images, GPU nodes | Cluster scanning, admission controller logs |

**Resource Tag Compliance:**
- All AI resources must have `ai-governance:registered` tag
- Missing or `unregistered` tags trigger investigation
- Automated remediation: quarantine or alert

### 2.4 Code Repository Scanning

**Objective:** Find AI-related code in repositories outside approved AI projects.

**Patterns to Detect:**
| Pattern | Language/Framework | Example |
|---------|-------------------|---------|
| OpenAI SDK | Python | `import openai` |
| LangChain | Python | `from langchain import *` |
| LlamaIndex | Python | `from llama_index import *` |
| Transformers | Python | `from transformers import *` |
| Anthropic SDK | Python/JS | `import anthropic` |
| Azure OpenAI | Python/JS | `from openai import AzureOpenAI` |
| Vertex AI | Python | `from google.cloud import aiplatform` |

**Repository Scope:**
- Internal source control (GitHub Enterprise, GitLab)
- Public GitHub org repositories
- Personal repositories of employees (where policy permits)
- Third-party code in supply chain

**Detection Tools:**
- GitHub Code Search API
- Sourcegraph for cross-repo search
- Semgrep for pattern matching
- Custom AST analysis

---

## 3. Shadow AI Classification

### 3.1 Categories

| Category | Definition | Response |
|----------|------------|----------|
| **Shadow AI** | Unregistered AI systems operating outside governance | Immediate onboarding or shutdown |
| **Unregistered Agent** | Known but not formally registered agent | Register within 48 hours |
| **Orphaned Agent** | Registered but owner departed/missing | Reassign ownership or decommission |
| **Non-Compliant Agent** | Registered but missing required controls | Remediate within SLA |
| **Approved Shadow** | Authorized but using non-standard infrastructure | Document exception or migrate |

### 3.2 Risk Assessment Matrix

| Discovery Method | Shadow AI Likely? | Investigation Priority |
|------------------|-------------------|------------------------|
| Hardcoded API key in public repo | Very High | Critical |
| Unregistered production endpoint | Very High | Critical |
| API calls from unknown service | High | High |
| Personal dev environment | Medium | Medium |
| Approved but missing tags | Low | Low |

---

## 4. Governance Onboarding for Discovered Shadow AI

### 4.1 Rapid Onboarding Process

```
Discovery → Risk Assessment → Interim Controls → Full Onboarding
   (Day 0)      (Day 0-1)        (Day 1-2)         (Day 3-7)
```

| Phase | Activities | Responsible |
|-------|------------|-------------|
| **Discovery** | Identify owner, assess immediate risk | Security Engineer |
| **Risk Assessment** | Determine risk tier, business criticality | Model Owner + Compliance |
| **Interim Controls** | Enable basic monitoring, restrict if high-risk | MLOps Engineer |
| **Full Onboarding** | Complete registry entry, implement all controls | Model Owner |

### 4.2 Interim Controls (24-48 Hour Window)

For Shadow AI that cannot be immediately shut down:

| Control | Implementation | Duration |
|---------|----------------|----------|
| **Traffic Mirroring** | Copy logs to SIEM for analysis | Until full logging |
| **Rate Limiting** | Cap API calls to prevent runaway costs | Until budget controls |
| **Alerting** | Notify on-call of any anomalies | Permanent |
| **Kill Switch Standby** | Document shutdown procedure | Until formal kill switch |
| **Weekly Review** | Require owner attestation | Until full governance |

### 4.3 Retroactive Compliance Review

For Shadow AI discovered after operation:

| Review Area | Action | Timeline |
|-------------|--------|----------|
| **Safety Incidents** | Review past 90 days for guardrail violations | 1 week |
| **Bias/Fairness** | Conduct retroactive bias audit if customer-facing | 2 weeks |
| **Data Handling** | Verify no PII misuse or residency violations | 1 week |
| **Financial Audit** | Reconcile costs to appropriate budget | 2 weeks |
| **Decision Records** | Import available logs to audit system | 2 weeks |

---

## 5. Prevention

### 5.1 Preventive Controls

| Control | Implementation | Effectiveness |
|---------|----------------|---------------|
| **Pre-Commit Hooks** | Block commits with API keys | High |
| **GitHub Secret Scanning** | Automatic detection and alerting | High |
| **Network Segmentation** | Isolate AI workloads to approved subnets | High |
| **Egress Proxy Required** | All AI API traffic through monitored proxy | High |
| **Cloud Policy Enforcement** | Deny creation of unapproved AI resources | Medium |
| **Developer Training** | Onboarding includes AI governance requirements | Medium |
| **Self-Service Registry** | Easy registration reduces shadow motivation | High |

### 5.2 Continuous Monitoring

| Monitor | Frequency | Alert Threshold |
|---------|-----------|-----------------|
| New API key creation | Real-time | Any new key |
| Unregistered DNS queries | Hourly | >10 queries/hour |
| Cloud resource creation | Real-time | Missing governance tags |
| Code commits | Real-time | AI SDK imports |
| Cost anomalies | Daily | >200% of baseline |

---

## 6. Metrics and Reporting

### 6.1 Shadow AI KPIs

| Metric | Target | Measurement |
|--------|--------|-------------|
| Shadow AI Instances | 0 | Count of unregistered AI systems |
| Time to Discovery | <7 days | From deployment to detection |
| Time to Onboarding | <48 hours | From discovery to full governance |
| Prevention Rate | >95% | Shadow AI prevented / attempted |
| API Key Exposure Incidents | 0 | Keys found in code repos |

### 6.2 Quarterly Shadow AI Report

| Section | Content |
|---------|---------|
| **Executive Summary** | Count of discoveries, risk level, remediation status |
| **Detection Activity** | Methods used, coverage gaps, new detection patterns |
| **Discovery Details** | Each instance: category, owner, risk tier, status |
| **Trends** | Month-over-month shadow AI attempts |
| **Prevention Effectiveness** | Controls working, gaps identified |
| **Recommendations** | Process improvements, tool investments |

---

## 7. Related Artifacts

- [Agent Registry Entry](../../03-runtime-governance/templates/agent-registry-entry.yaml) -- Onboarding template
- [Governance Enforcement Pipeline](../../03-runtime-governance/agentic-workflows/governance-enforcement-pipeline.md) -- Preventive controls
- [Audit Record Schema](../templates/audit-record-schema.yaml) -- Logging requirements
- [Multi-Tenant Isolation](../../03-runtime-governance/agentic-workflows/multi-tenant-isolation.md) -- Network controls

---

*Last updated: 2026-03-26 / Version: 1.0 / Classification: Internal*
