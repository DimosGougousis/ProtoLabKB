# AIMS Infrastructure Inventory — ISO/IEC 42001 Clause 7.1

> **Purpose:** Documents all infrastructure resources supporting the ProtoLabs AI Management System, ensuring ISO/IEC 42001 Clause 7.1 (Resources) compliance.

**Version:** 1.0  
**Last Updated:** 2026-04-24  
**Owner:** VP of Engineering (Technical Owner)  
**Review Cycle:** Quarterly  

---

## Infrastructure Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    AIMS INFRASTRUCTURE ARCHITECTURE                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐         │
│  │   DEVELOPMENT   │    │    TESTING      │    │   PRODUCTION    │         │
│  │   ENVIRONMENT   │    │   ENVIRONMENT   │    │   ENVIRONMENT   │         │
│  │                 │    │                 │    │                 │         │
│  │ • GPU clusters  │    │ • Eval runners  │    │ • Agent fleet   │         │
│  │ • Model repos   │    │ • Golden datasets│   │ • Safety Agent  │         │
│  │ • Dev tools     │    │ • Red team env  │    │ • MES/ERP APIs  │         │
│  └────────┬────────┘    └────────┬────────┘    └────────┬────────┘         │
│           │                      │                      │                   │
│           └──────────────────────┼──────────────────────┘                   │
│                                  │                                          │
│                    ┌─────────────▼─────────────┐                           │
│                    │    GOVERNANCE LAYER       │                           │
│                    │  • Audit logging          │                           │
│                    │  • Monitoring (Grafana)   │                           │
│                    │  • Document control       │                           │
│                    │  • Access control (RBAC)  │                           │
│                    └───────────────────────────┘                           │
│                                  │                                          │
│                    ┌─────────────▼─────────────┐                           │
│                    │    SECURITY LAYER         │                           │
│                    │  • Network segmentation   │                           │
│                    │  • Encryption (rest/trans)│                           │
│                    │  • DLP / IP protection    │                           │
│                    │  • SIEM / threat detection│                           │
│                    └───────────────────────────┘                           │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Compute Infrastructure

### Development Environment

| Resource | Specification | Purpose | Owner | Cost/Month |
|----------|--------------|---------|-------|------------|
| GPU Cluster (Dev) | 4× NVIDIA A100 80GB | Model training, fine-tuning | ML Team | $8,000 |
| CPU Cluster (Dev) | 16× 64-core VMs | Data processing, eval pipelines | MLOps | $4,000 |
| Storage (Dev) | 500TB NVMe | Dataset storage, model checkpoints | MLOps | $3,000 |
| Development Workstations | 20× high-end workstations | Engineer development | IT | $2,000 |

### Testing Environment

| Resource | Specification | Purpose | Owner | Cost/Month |
|----------|--------------|---------|-------|------------|
| Eval Cluster | 8× 32-core VMs | Automated eval suite execution | MLOps | $2,500 |
| Red Team Environment | Isolated sandbox | Adversarial testing, security research | Security | $1,500 |
| Golden Dataset Storage | 50TB encrypted | Reference datasets, benchmarks | ML Team | $500 |
| Chaos Engineering | Fault injection tools | Resilience testing | MLOps | $500 |

### Production Environment

| Resource | Specification | Purpose | Owner | Cost/Month |
|----------|--------------|---------|-------|------------|
| Agent Fleet (Tier 1) | 8× 16-core VMs | DFM analysis, materials selection | MLOps | $3,000 |
| Agent Fleet (Tier 2) | 4× 32-core VMs | Quote bot, production scheduler | MLOps | $2,500 |
| Agent Fleet (Tier 3) | 2× 64-core VMs + edge | Parameter optimizer, quality agent | MLOps | $4,000 |
| Safety Agent (Governor) | 2× 16-core VMs (HA) | Validate all Tier 2/3 actions | Safety | $1,500 |
| Orchestration Agent | 2× 8-core VMs (HA) | Multi-agent coordination | MLOps | $800 |
| Inference Cache | Redis cluster | Response caching, rate limiting | MLOps | $600 |

---

## Software and Platform Infrastructure

### AI/ML Platforms

| Platform | Version | Purpose | License | Owner |
|----------|---------|---------|---------|-------|
| Azure OpenAI Service | Latest | LLM inference for agents | Enterprise | Technical Owner |
| Azure ML | Latest | Model training, experiment tracking | Enterprise | ML Lead |
| LangChain | 0.1.x | Agent framework, tool orchestration | MIT | AI Engineer |
| Hugging Face Transformers | Latest | Model hosting, fine-tuning | Apache 2.0 | ML Engineer |
| Weights & Biases | Latest | Experiment tracking, model registry | Enterprise | MLOps |
| MLflow | Latest | Model versioning, deployment | Apache 2.0 | MLOps |

### Governance and Monitoring

| Platform | Version | Purpose | License | Owner |
|----------|---------|---------|---------|-------|
| Grafana | Latest | Metrics dashboards, alerting | AGPL | MLOps |
| Prometheus | Latest | Metrics collection | Apache 2.0 | MLOps |
| ELK Stack | Latest | Log aggregation, search | Elastic License | Security |
| Langfuse | Latest | LLM tracing, cost monitoring | MIT | MLOps |
| NeMo Guardrails | Latest | Input/output validation | Apache 2.0 | AI Engineer |
| Giskard | Latest | Bias testing, model quality | Apache 2.0 | ML Engineer |

### Security and Compliance

| Platform | Version | Purpose | License | Owner |
|----------|---------|---------|---------|-------|
| HashiCorp Vault | Latest | Secret management | BSL | Security |
| SPIFFE/SPIRE | Latest | Agent identity, mTLS | Apache 2.0 | Security |
| Azure Key Vault | Latest | Key management, certificates | Enterprise | Security |
| Microsoft Purview | Latest | Data governance, DLP | Enterprise | DPO |
| SIEM (Sentinel) | Latest | Threat detection, incident response | Enterprise | Security |

### Data and Integration

| Platform | Version | Purpose | License | Owner |
|----------|---------|---------|---------|-------|
| Azure Cosmos DB | Latest | Agent state, conversation history | Enterprise | MLOps |
| Azure Blob Storage | Latest | Model artifacts, datasets | Enterprise | MLOps |
| PostgreSQL | Latest | Structured data, audit logs | PostgreSQL | MLOps |
| Redis | Latest | Caching, session state | BSD | MLOps |
| MES API | Proprietary | Production scheduling integration | Proprietary | Manufacturing |
| ERP API | Proprietary | Quote, inventory integration | Proprietary | Finance |

---

## Network Infrastructure

### Network Segmentation

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         NETWORK ZONES                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────────┐     ┌──────────────┐     ┌──────────────┐               │
│  │   DMZ        │     │   CORPORATE  │     │   MANUFACTURING│              │
│  │              │     │              │     │   (OT/ICS)     │              │
│  │ • Public APIs│◄───►│ • Agent Fleet│◄───►│ • MES/SCADA   │              │
│  │ • CDN        │     │ • Safety Agent│    │ • CNC Controllers│           │
│  │ • WAF        │     │ • Governance │     │ • Quality Systems│           │
│  └──────────────┘     └──────────────┘     └──────────────┘               │
│         ▲                    ▲                    ▲                         │
│         │                    │                    │                         │
│         └────────────────────┴────────────────────┘                         │
│                         │                                                    │
│              ┌──────────▼──────────┐                                        │
│              │   SECURITY ZONE     │                                        │
│              │ • SIEM, IDS/IPS     │                                        │
│              │ • Audit logging     │                                        │
│              │ • Certificate mgmt  │                                        │
│              └─────────────────────┘                                        │
│                                                                              │
│  FIREWALL RULES:                                                             │
│  • DMZ → Corporate: HTTPS only, authenticated                                │
│  • Corporate → Manufacturing: MES API only, Safety Agent validated           │
│  • Manufacturing → Corporate: Read-only telemetry, no inbound                │
│  • Any → Security Zone: Audit logs, alerts only                              │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

| Zone | Purpose | Access Control | Monitoring |
|------|---------|----------------|------------|
| DMZ | Public-facing APIs, CDN | WAF, rate limiting, API keys | DDoS detection, access logs |
| Corporate | Agent fleet, governance tools | RBAC, MFA, VPN | User behavior analytics |
| Manufacturing (OT) | MES, SCADA, CNC controllers | Air gap, Safety Agent, physical access | OT-specific IDS, anomaly detection |
| Security | SIEM, audit, certificates | Admin-only, MFA, jump boxes | Self-monitoring, tamper detection |

---

## Backup and Disaster Recovery

| System | Backup Frequency | Retention | DR Target | Owner |
|--------|-----------------|-----------|-----------|-------|
| Model artifacts | Daily | 30 days | 4-hour RTO | MLOps |
| Datasets | Weekly | 90 days | 24-hour RTO | MLOps |
| Audit logs | Real-time replication | 7 years | 1-hour RTO | Security |
| Agent configurations | On change | 30 versions | 2-hour RTO | MLOps |
| Governance documents | On change | 7 years | 4-hour RTO | Compliance |
| Safety Agent rules | On change | 30 versions | 1-hour RTO | Safety |

---

## Resource Capacity Planning

### Current Utilization (Q2 2026)

| Resource | Capacity | Utilization | Headroom | Planned Expansion |
|----------|----------|-------------|----------|-------------------|
| GPU (Dev) | 4× A100 | 75% | 25% | +2× A100 Q3 2026 |
| GPU (Prod) | Shared inference | 60% | 40% | Auto-scale enabled |
| Storage | 600TB total | 65% | 35% | +200TB Q4 2026 |
| Network (Corp) | 10Gbps | 45% | 55% | Monitor |
| Network (OT) | 1Gbps isolated | 30% | 70% | Monitor |

### Scaling Triggers

| Trigger | Action | Approval Required |
|---------|--------|-------------------|
| GPU utilization >85% for 7 days | Provision additional GPUs | Technical Owner |
| Storage >80% | Expand storage | Technical Owner |
| API latency >500ms p99 | Scale inference cluster | MLOps Lead |
| Safety Agent queue >100 | Scale Safety Agent | Safety Officer |
| New agent deployment | Provision dedicated resources | Technical Owner |

---

## Vendor and Third-Party Management

| Vendor | Service | Risk Level | Contract Review | Owner |
|--------|---------|------------|-----------------|-------|
| Microsoft Azure | Cloud infrastructure, OpenAI | High | Annual | Procurement |
| Weights & Biases | Experiment tracking | Medium | Annual | Technical Owner |
| TÜV SÜD / BSI | Certification body | Medium | Per engagement | CAIO |
| [Security Vendor] | Penetration testing | Medium | Annual | Security |
| [Training Vendor] | ISO 42001 training | Low | Per course | HR |

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-24 | ProtoLabs AI Governance Office | Initial infrastructure inventory |

---

## See Also

- `governance/05-cross-cutting/tool-landscape.md` — Governance tooling
- `governance/03-runtime-governance/agentic-workflows/agent-fleet-operations.md` — Fleet operations
- `docs/iso-42001-gap-analysis.md` — Gap analysis (Clause 7.1)
