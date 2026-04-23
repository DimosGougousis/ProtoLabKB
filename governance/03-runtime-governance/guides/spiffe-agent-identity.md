# SPIFFE Agent Identity Guide

## Purpose

This document provides implementation guidance for using SPIFFE (Secure Production Identity Framework For Everyone) workload identities for AI agents. SPIFFE enables cryptographically verifiable, short-lived identities that propagate through delegation chains, enabling granular permission matrices and strong authentication across multi-agent systems.

SPIFFE addresses the critical need for machine identity in agentic AI systems, where traditional service accounts and API keys are insufficient for the dynamic, delegated nature of agent workflows.

## When to Use

- When implementing production identity for AI agents in multi-tenant environments
- When designing secure delegation chains between agents
- When requiring cryptographic proof of identity for audit trails
- When implementing zero-trust architecture for agent infrastructure
- When automating credential rotation without service disruption
- When propagating identity through complex agent orchestration flows

## Who Is Responsible

| Role | R/A/C/I | Responsibility |
|------|---------|---------------|
| **Security Architect** | Accountable | Designs SPIFFE trust domain architecture |
| **Platform Engineer** | Responsible | Deploys and operates SPIRE (SPIFFE Runtime Environment) |
| **MLOps Engineer** | Responsible | Integrates agents with SPIFFE identities |
| **AI/ML Engineer** | Consulted | Implements identity-aware agent code |
| **Compliance Officer** | Reviewer | Validates identity meets audit requirements |

## Regulatory Basis

- **DORA Article 9** -- ICT risk management including strong authentication
- **NIST SP 800-207** -- Zero Trust Architecture
- **ISO 27001 A.9.2** -- Secure log-on procedures
- **SAFEST S-08** -- Access controls with strong identity
- **SAFEST A-11** -- Complete audit trail with authenticated identity

---

## 1. SPIFFE Fundamentals

### 1.1 Core Concepts

| Concept | Description | AI Agent Application |
|---------|-------------|---------------------|
| **SPIFFE ID** | Universal identity URI | `spiffe://trust-domain/agent/agent-id` |
| **SVID** | SPIFFE Verifiable Identity Document | X.509 certificate or JWT with embedded SPIFFE ID |
| **Trust Domain** | Administrative boundary for identities | Organization or tenant boundary |
| **SPIRE** | SPIFFE Runtime Environment | Issues and rotates SVIDs automatically |
| **Workload Attestation** | Process proving its identity | Agent pod proves identity to SPIRE agent |

### 1.2 SPIFFE ID Structure

```
spiffe://{trust-domain}/{workload-identifier}

Examples:
spiffe://fintech-corp.io/agent/payments-agent/prod/01
spiffe://tenant-a.fintech.io/skill/fraud-detection/v2
spiffe://fintech-corp.io/delegation/chain/onboarding-2026-03-26
```

| Component | Description | Governance Use |
|-----------|-------------|----------------|
| `trust-domain` | Organizational or tenant boundary | Multi-tenancy isolation |
| `agent` | Identity type | Distinguishes agents from services |
| `payments-agent` | Agent class | Permission matrix lookup |
| `prod` | Environment | Environment-scoped policies |
| `01` | Instance identifier | Specific agent instance |

---

## 2. SPIRE Architecture for Agentic AI

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SPIRE DEPLOYMENT FOR AI AGENTS                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                         SPIRE SERVER                               │   │
│  │  ┌───────────────┐  ┌───────────────┐  ┌───────────────────────┐  │   │
│  │  │   CA/Signing  │  │  Registration │  │   Policy Repository   │  │   │
│  │  │   Service     │  │    Database   │  │  (Agent identities)   │  │   │
│  │  └───────────────┘  └───────────────┘  └───────────────────────┘  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                              ▲                                              │
│                              │ gRPC (mTLS)                                  │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                      SPIRE AGENT (per node)                          │   │
│  │  ┌───────────────┐  ┌───────────────┐  ┌───────────────────────┐  │   │
│  │  │   Workload    │  │    SVID       │  │   Attestation Plugin  │  │   │
│  │  │   Attestation │  │   Cache       │  │   (K8s, AWS, etc.)    │  │   │
│  │  └───────────────┘  └───────────────┘  └───────────────────────┘  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                              ▲                                              │
│                              │ Unix socket / Workload API                   │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                      AI AGENT WORKLOAD                               │   │
│  │  ┌───────────────┐  ┌───────────────┐  ┌───────────────────────┐  │   │
│  │  │   Agent       │  │   SPIFFE      │  │   SVID (X.509/JWT)    │  │   │
│  │  │   Process     │◄─┤   Library     │◄─┤   Short-lived: 15min  │  │   │
│  │  │               │  │               │  │   Auto-rotated        │  │   │
│  │  └───────────────┘  └───────────────┘  └───────────────────────┘  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.1 SPIRE Server Configuration

```hcl
# spire-server.conf
server {
    trust_domain = "fintech-corp.io"
    
    // CA configuration
    ca_key_type = "ec-p256"
    ca_ttl = "24h"
    
    // SVID defaults
    default_svid_ttl = "15m"  // Short-lived for high-risk agents
    
    // Registration entries for agents
    entry {
        spiffe_id = "spiffe://fintech-corp.io/agent/payments-agent/prod"
        parent_id = "spiffe://fintech-corp.io/node/k8s-cluster-01"
        selector {
            type = "k8s"
            value = "pod-label:app:payments-agent"
        }
        selector {
            type = "k8s"
            value = "pod-label:env:prod"
        }
        // TTL for this agent class
        ttl = "15m"
    }
    
    // Multi-tenant trust domains
    entry {
        spiffe_id = "spiffe://tenant-a.fintech.io/agent/namespace/*"
        parent_id = "spiffe://fintech-corp.io/node/k8s-cluster-01"
        selector {
            type = "k8s"
            value = "namespace:tenant-a"
        }
        ttl = "15m"
    }
}
```

### 2.2 Agent Integration

```python
# Agent code with SPIFFE identity
import spiffe

class SPIFFEAgent:
    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self.spiffe_id = f"spiffe://fintech-corp.io/agent/{agent_id}"
        
        # Fetch SVID from SPIRE agent via workload API
        self.svid = spiffe.fetch_svid()
        
        # Auto-rotation callback
        spiffe.on_rotation(self._handle_rotation)
    
    def _handle_rotation(self, new_svid):
        """Handle SVID rotation seamlessly"""
        self.svid = new_svid
        # Update any cached credentials
        self._refresh_tool_credentials()
    
    def invoke_tool(self, tool_endpoint: str, request: dict):
        """Invoke tool with SPIFFE-authenticated mTLS"""
        
        # Use SVID for mutual TLS authentication
        response = requests.post(
            tool_endpoint,
            json=request,
            cert=self.svid.certificate,
            key=self.svid.private_key,
            verify=self.svid.trust_bundle
        )
        
        # Tool receives our SPIFFE ID for authorization
        return response
```

---

## 3. Per-Skill Permission Matrices

### 3.1 Skill-Level SPIFFE IDs

Each skill within an agent can have its own SPIFFE identity for fine-grained authorization:

```
Agent SPIFFE ID:
  spiffe://fintech-corp.io/agent/payments-agent/prod/01

Skill SPIFFE IDs:
  spiffe://fintech-corp.io/skill/payments-agent/process-payment/prod/01
  spiffe://fintech-corp.io/skill/payments-agent/verify-identity/prod/01
  spiffe://fintech-corp.io/skill/payments-agent/check-fraud/prod/01
```

**Benefits:**
- Compromised skill credential doesn't expose entire agent
- Skill-level revocation without agent restart
- Fine-grained audit trails
- Delegation authorization at skill level

### 3.2 Permission Matrix with SPIFFE

```yaml
# Permission matrix using SPIFFE identities
permission_matrix:
  agent_identity: "spiffe://fintech-corp.io/agent/payments-agent/prod/01"
  
  skills:
    - skill_id: "process-payment"
      spiffe_id: "spiffe://fintech-corp.io/skill/payments-agent/process-payment/prod/01"
      allowed_actions:
        - action: "initiate_payment"
          resource_pattern: "account:{tenant_id}:*"
          max_amount: 10000
          conditions:
            - "identity_verified"
            - "fraud_check_passed"
      
    - skill_id: "verify-identity"
      spiffe_id: "spiffe://fintech-corp.io/skill/payments-agent/verify-identity/prod/01"
      allowed_actions:
        - action: "query_identity_service"
          resource_pattern: "identity:{tenant_id}:{user_id}"
          conditions:
            - "customer_consent"
```

---

## 4. Delegation Chain Propagation

### 4.1 Delegation Identity Stack

When agents delegate to sub-agents, the full identity chain is propagated:

```python
# Delegation with SPIFFE identity propagation
class OrchestratorAgent:
    def delegate_task(self, task: Task, sub_agent_id: str):
        # Current identity: spiffe://fintech-corp.io/agent/orchestrator/prod/01
        
        # Create delegation context
        delegation_context = {
            # Original caller
            'root_identity': self.svid.spiffe_id,
            
            # Delegation chain
            'delegation_chain': [
                self.svid.spiffe_id,
                # Next will be added by sub-agent
            ],
            
            # Delegation-specific claims
            'delegated_permissions': task.required_permissions,
            'delegation_depth': 1,
            'max_delegation_depth': 5,
            'expiry': time.now() + timedelta(minutes=15)
        }
        
        # Sub-agent receives this context and can verify:
        # 1. Root identity is authorized to delegate
        # 2. Chain depth hasn't been exceeded
        # 3. Permissions are within scope
        
        return sub_agent.execute(task, delegation_context)


class SubAgent:
    def execute(self, task: Task, delegation_context: dict):
        # Verify delegation chain
        root_id = delegation_context['root_identity']
        chain = delegation_context['delegation_chain']
        
        # Add our identity to chain
        my_id = self.svid.spiffe_id
        chain.append(my_id)
        
        # Check authorization
        if not self._verify_delegation_authorization(root_id, task):
            raise UnauthorizedDelegationError()
        
        # Execute with full chain in audit log
        self._execute_with_audit(task, chain)
```

### 4.2 Chain Validation

```python
def validate_delegation_chain(chain: list, policy: dict) -> bool:
    """
    Validate a delegation chain against policy.
    
    Checks:
    1. No cycles in chain
    2. Chain depth within limits
    3. Each link authorized to delegate
    4. Permissions don't escalate
    """
    
    # Check for cycles
    if len(chain) != len(set(chain)):
        raise DelegationCycleError("Duplicate identities in chain")
    
    # Check depth
    if len(chain) > policy['max_delegation_depth']:
        raise DelegationDepthError(f"Chain depth {len(chain)} exceeds limit")
    
    # Verify each link
    for i in range(len(chain) - 1):
        delegator = chain[i]
        delegate = chain[i + 1]
        
        if not is_authorized_to_delegate(delegator, delegate):
            raise UnauthorizedDelegationError(
                f"{delegator} cannot delegate to {delegate}"
            )
    
    return True
```

---

## 5. TTL and Rotation Policy

### 5.1 Time-To-Live (TTL) Configuration

| Risk Tier | SVID TTL | Rationale |
|-----------|----------|-----------|
| High-Risk | 15 minutes | Minimize exposure for financial/customer-impact agents |
| Limited-Risk | 1 hour | Balance security with operational overhead |
| Minimal-Risk | 4 hours | Reduced rotation for low-impact internal tools |

### 5.2 Rotation Handling

```python
class SVIDManager:
    """Manages SVID lifecycle with seamless rotation"""
    
    def __init__(self, ttl_minutes: int = 15):
        self.ttl = timedelta(minutes=ttl_minutes)
        self.svid = None
        self.rotation_callbacks = []
        
        # Start rotation loop
        self._start_rotation_monitor()
    
    def _start_rotation_monitor(self):
        """Monitor SVID and rotate before expiry"""
        while True:
            if self.svid:
                remaining = self.svid.expiry - datetime.now()
                
                # Rotate at 70% of TTL (e.g., 10.5 min for 15 min TTL)
                if remaining < self.ttl * 0.3:
                    self._rotate_svid()
            
            time.sleep(30)  # Check every 30 seconds
    
    def _rotate_svid(self):
        """Fetch new SVID and notify listeners"""
        new_svid = spiffe.fetch_svid()
        
        # Atomic swap
        old_svid = self.svid
        self.svid = new_svid
        
        # Notify callbacks
        for callback in self.rotation_callbacks:
            callback(new_svid)
        
        # Graceful cleanup of old SVID after grace period
        time.sleep(60)
        old_svid = None
```

---

## 6. Multi-Tenancy with SPIFFE

### 6.1 Tenant Trust Domains

```
Trust Domain per Tenant:
  spiffe://tenant-a.fintech.io/agent/onboarding-agent/prod/01
  spiffe://tenant-b.fintech.io/agent/support-agent/prod/03
  
Benefits:
  - Cryptographic tenant isolation
  - No identity spoofing between tenants
  - Per-tenant CA and revocation
```

### 6.2 Cross-Tenant Delegation

```python
# Secure cross-tenant delegation (if permitted)
def cross_tenant_delegate(
    source_tenant: str,
    target_tenant: str,
    task: Task
):
    source_id = f"spiffe://{source_tenant}.fintech.io/agent/{task.source_agent}"
    target_id = f"spiffe://{target_tenant}.fintech.io/agent/{task.target_agent}"
    
    # Verify cross-tenant delegation is permitted
    if not is_cross_tenant_delegation_allowed(source_tenant, target_tenant):
        raise CrossTenantDelegationForbidden()
    
    # Create attested delegation token
    delegation_token = create_delegation_token(
        source_id=source_id,
        target_id=target_id,
        permissions=task.permissions,
        ttl=timedelta(minutes=15)
    )
    
    return delegation_token
```

---

## 7. Related Artifacts

- [Agent Permission Boundaries](../agentic-workflows/agent-permission-boundaries.md) -- SPIFFE-based RBAC
- [Multi-Tenant Isolation](../agentic-workflows/multi-tenant-isolation.md) -- Trust domain architecture
- [Skill Manifest](../templates/skill-manifest.yaml) -- SPIFFE identity in skill configuration
- [Governance Enforcement Pipeline](../agentic-workflows/governance-enforcement-pipeline.md) -- Layer 3 (RBAC) integration

---

*Last updated: 2026-03-26 / Version: 1.0 / Classification: Internal*
