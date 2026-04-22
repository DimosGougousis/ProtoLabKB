---
type: knowledge-article
category: ai
source_url: https://www.anthropic.com/research
fetched_at: 2026-04-22
summary: Agentic architecture patterns for AI systems - single-agent, supervisor-worker, swarm, and graph topologies with selection criteria and implementation guidance.
---

# Agentic Architecture Patterns

## Overview

Agentic architectures define how AI agents are organized to accomplish tasks. The choice of topology impacts scalability, reliability, cost, and complexity.

## The Four Topologies

| Pattern | Structure | Best For | Complexity | Cost |
|---------|-----------|----------|------------|------|
| **Single-Agent** | One agent handles all tasks | Simple workflows, prototyping | Low | Low |
| **Supervisor-Worker** | Coordinator delegates to specialists | Multi-step workflows, clear hand-offs | Medium | Medium |
| **Swarm** | Peer agents collaborate emergently | Exploration, creativity, consensus | High | High |
| **Graph** | Agents as nodes in directed graph | Complex dependencies, conditional routing | High | Medium |

## Single-Agent Pattern

### Structure
```
User Request → Single Agent → Response
```

### Characteristics
- **Simplicity**: Easy to implement and debug
- **Cost**: Lowest token usage
- **Latency**: Fastest response time
- **Limitations**: Context window constraints, no specialization

### When to Use
- Simple Q&A tasks
- Prototyping
- Low-complexity workflows
- Cost-sensitive applications

### Protolabs Example
DFM Router: Single agent classifies intent and routes to specialist.

## Supervisor-Worker Pattern

### Structure
```
User Request → Supervisor → Worker A → Worker B → Response
                     ↓
              Worker C (if needed)
```

### Characteristics
- **Coordination**: Centralized control
- **Specialization**: Workers can be optimized for specific tasks
- **Reliability**: Supervisor can retry failed workers
- **Scalability**: Add workers as needed

### When to Use
- Multi-step workflows
- Clear task decomposition
- Need for retry/error handling
- Different capabilities required

### Protolabs Example
Sloan Strategy Pipeline: Coordinator dispatches to 5 lens analysts in parallel, then synthesizes results.

## Swarm Pattern

### Structure
```
User Request → Agent A → Agent B → Agent C → Consensus → Response
                ↓         ↓         ↓
              Shared State / Message Bus
```

### Characteristics
- **Emergence**: Collective intelligence
- **Redundancy**: Multiple agents explore solution space
- **Creativity**: Diverse perspectives
- **Cost**: Highest token usage

### When to Use
- Creative tasks
- Exploration problems
- Consensus building
- High-stakes decisions

### Protolabs Example
Design optimization: Multiple agents propose solutions, vote on best approach.

## Graph Pattern

### Structure
```
User Request → Node A → [Condition] → Node B → Node D → Response
                     ↘
                      [Alt] → Node C → Node E
```

### Characteristics
- **Flexibility**: Conditional routing
- **Visibility**: Clear workflow visualization
- **Reusability**: Nodes can be reused across workflows
- **Complexity**: Requires workflow engine

### When to Use
- Complex conditional logic
- Multi-path workflows
- Need for audit trails
- Regulatory compliance requirements

### Protolabs Example
Compliance checking: Different paths based on ITAR, ISO, or standard requirements.

## Selection Framework

### Decision Tree

```
Is task simple and well-defined?
├── YES → Single-Agent
└── NO → Does it require multiple distinct capabilities?
    ├── YES → Supervisor-Worker
    └── NO → Does it benefit from multiple perspectives?
        ├── YES → Swarm
        └── NO → Complex conditional logic?
            ├── YES → Graph
            └── NO → Re-evaluate requirements
```

### Criteria Matrix

| Criterion | Single | Supervisor | Swarm | Graph |
|-----------|--------|------------|-------|-------|
| Implementation Speed | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐ |
| Debugging Ease | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| Scalability | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Cost Efficiency | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| Fault Tolerance | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Flexibility | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

## Implementation Guidance

### Single-Agent
- Use function calling for tool access
- Implement retry logic for failures
- Monitor context window usage

### Supervisor-Worker
- Define clear hand-off contracts
- Implement worker health checks
- Use parallel dispatch where possible

### Swarm
- Implement consensus mechanism
- Set maximum iteration limits
- Track individual agent contributions

### Graph
- Use workflow engine (e.g., LangGraph, Temporal)
- Implement state management
- Add observability at each node

## References
- Anthropic. (2024). Building effective agents.
- Google. (2024). Agentic AI patterns.
- Microsoft. (2024). Autogen multi-agent framework.
