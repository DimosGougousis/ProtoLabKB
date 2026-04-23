---
type: work-package
wp_id: WP-CAD
name: CAD AI Evaluation System
priority: P0
status: planning
owner: Director of AI Products
created: 2026-04-23
---

# Work Package: CAD AI Evaluation System (WP-CAD)

## Executive Summary

Build an AI-powered CAD evaluation system that automatically parses 3D CAD uploads, extracts manufacturing features, evaluates Design for Manufacturability (DFM) using Vision-Language Models (VLMs) and rule-based validation, and compares designs against historical projects for completeness and manufacturability scoring.

**Strategic Alignment:** This work package directly addresses the strategic initiative to "Use AI to Evaluate 3D CAD file uploads for manufacturability" by implementing the complete technical architecture from CAD parsing through VLM-powered analysis to historical comparison.

---

## Objectives

### Primary Objective
Enable automated, AI-powered DFM evaluation of CAD uploads that matches or exceeds expert engineer assessment quality while operating 24/7 with sub-60-second turnaround.

### Key Results

| KR ID | Key Result | Target | Measurement |
|-------|------------|--------|-------------|
| KR-CAD-1 | CAD file parsing success rate | >99% | Successful parses / total uploads |
| KR-CAD-2 | Feature detection precision | >95% | True positives / (true positives + false positives) |
| KR-CAD-3 | Feature detection recall | >90% | True positives / (true positives + false negatives) |
| KR-CAD-4 | End-to-end analysis time | <60 seconds | Upload to report delivery |
| KR-CAD-5 | DFM score accuracy vs experts | ±10 points | Correlation with expert ratings (0-100) |
| KR-CAD-6 | VLM explanation helpfulness | >4.0/5.0 | User satisfaction survey |
| KR-CAD-7 | Historical similarity accuracy | Top-5 >90% | Relevant similar projects in top 5 |
| KR-CAD-8 | System uptime | 99.9% | Availability excluding planned maintenance |

---

## Scope

### In Scope

1. **CAD File Parsing (CAD-001 to CAD-004)**
   - STEP (AP214/AP242) with PMI support
   - STL (binary and ASCII)
   - OBJ with materials
   - 3MF with metadata
   - IGES (legacy support)

2. **Feature Recognition (FTR-001 to FTR-008)**
   - Holes (diameter, depth, position, type)
   - Pockets (depth, corners, floor)
   - Bosses (height, diameter, draft)
   - Fillets and chamfers
   - Threads (pitch, diameter, handedness)
   - Thin walls (thickness mapping)
   - Undercuts (side action requirements)
   - Draft angles (wall taper analysis)

3. **VLM Integration (VLM-001 to VLM-008)**
   - 2D view generation for VLM input
   - Visual DFM assessment
   - Design comparison against historical projects
   - Anomaly detection
   - Natural language explanation generation
   - Fix suggestion visualization
   - Multi-modal reasoning

4. **DFM Rule Engine (DFM-001 to DFM-008)**
   - Machine-readable rule codification
   - Geometric constraint checking
   - Tolerance stack-up analysis
   - Material-process compatibility
   - Cost estimation integration
   - Manufacturability scoring
   - Issue prioritization
   - Fix recommendation engine

5. **Historical Comparison (HST-001 to HST-008)**
   - Vector database for design embeddings
   - Geometry fingerprinting
   - Historical issue mapping
   - Similar project retrieval
   - Success pattern learning
   - Failure mode database
   - Cross-project analytics
   - Continuous learning loop

6. **Integration & APIs (INT-001 to INT-008)**
   - REST API for CAD evaluation
   - GraphQL endpoint
   - Webhook support
   - Batch processing
   - SDK distribution
   - PLM integration
   - CAD plugin development
   - MES/ERP integration

### Out of Scope (Future Phases)

1. **Real-time Collaboration** - Multi-user simultaneous editing
2. **Generative Design** - AI-generated design alternatives
3. **Physics Simulation** - Full FEA/CFD analysis
4. **Supply Chain Integration** - Supplier capability matching
5. **AR/VR Visualization** - Immersive design review

---

## Technical Architecture

### System Components

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           CAD AI Evaluation System                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────┐    ┌─────────────────────────────────────────────────┐  │
│  │   CAD Upload    │───▶│         CAD Parser Service                      │  │
│  │  (STEP/STL/OBJ) │    │  • Format detection & validation               │  │
│  └─────────────────┘    │  • Geometry extraction (B-rep & mesh)            │  │
│                         │  • PMI harvesting (STEP AP242)                   │  │
│                         │  • 2D view generation (ortho + isometric)        │  │
│                         └────────────────────┬────────────────────────────┘  │
│                                                │                             │
│                         ┌──────────────────────┼────────────────────────────┐  │
│                         │                      ▼                             │  │
│                         │  ┌─────────────────────────────────────────────┐ │  │
│                         │  │        Feature Recognition Service            │ │  │
│                         │  │  • Hole detection (diameter, depth, type)      │ │  │
│                         │  │  • Pocket recognition (depth, corners)         │ │  │
│                         │  │  • Boss identification (height, draft)         │ │  │
│                         │  │  • Thread detection (pitch, handedness)        │ │  │
│                         │  │  • Thin wall analysis (thickness mapping)      │ │  │
│                         │  │  • Undercut detection (side actions)         │ │  │
│                         │  │  • Draft angle calculation (wall taper)        │ │  │
│                         │  └─────────────────────┬───────────────────────┘ │  │
│                         │                        │                       │  │
│                         │    ┌───────────────────┼───────────────────┐   │  │
│                         │    │                   ▼                   │   │  │
│                         │    │  ┌─────────────────────────────────┐  │   │  │
│                         │    │  │      DFM Rule Engine            │  │   │  │
│                         │    │  │  • Machine-readable rulebook    │  │   │  │
│                         │    │  │  • Geometric constraint checks  │  │   │  │
│                         │    │  │  • Tolerance stack-up analysis  │  │   │  │
│                         │    │  │  • Material-process compatibility│  │   │  │
│                         │    │  │  • Manufacturability scoring    │  │   │  │
│                         │    │  │  • Issue prioritization         │  │   │  │
│                         │    │  │  • Fix recommendation engine    │  │   │  │
│                         │    │  └──────────────┬──────────────────┘  │   │  │
│                         │    │                 │                     │   │  │
│                         │    │  ┌──────────────┼──────────────────┐  │   │  │
│                         │    │  │              ▼                  │  │   │  │
│                         │    │  │  ┌─────────────────────────────┐│  │   │  │
│                         │    │  │  │   VLM Analysis Service      ││  │   │  │
│                         │    │  │  │  • Visual DFM assessment    ││  │   │  │
│                         │    │  │  │  • Design comparison        ││  │   │  │
│                         │    │  │  │  • Anomaly detection        ││  │   │  │
│                         │    │  │  │  • Natural language output  ││  │   │  │
│                         │    │  │  │  • Fix visualization        ││  │   │  │
│                         │    │  │  │  • Multi-modal reasoning    ││  │   │  │
│                         │    │  │  └──────────────┬─────────────┘│  │   │  │
│                         │    │  │                 │              │  │   │  │
│                         │    │  │  ┌──────────────┼──────────────┐  │   │  │
│                         │    │  │  │              ▼               │  │   │  │
│                         │    │  │  │  ┌──────────────────────────┐  │  │   │  │
│                         │    │  │  │  │ Historical Comparison  │  │  │   │  │
│                         │    │  │  │  │  • Vector database      │  │  │   │  │
│                         │    │  │  │  │  • Geometry fingerprints  │  │  │   │  │
│                         │    │  │  │  │  • Issue pattern mapping  │  │  │   │  │
│                         │    │  │  │  │  • Similar project search   │  │  │   │  │
│                         │    │  │  │  │  • Success pattern learning │  │  │   │  │
│                         │    │  │  │  │  • Failure mode catalog     │  │  │   │  │
│                         │    │  │  │  │  • Cross-project analytics    │  │  │   │  │
│                         │    │  │  │  │  • Continuous learning loop     │  │  │   │  │
│                         │    │  │  │  └──────────────┬─────────────┘  │  │   │  │
│                         │    │  │  │                 │                │  │   │  │
│                         │    │  │  │  ┌──────────────┼────────────────┐  │  │   │  │
│                         │    │  │  │  │              ▼                 │  │  │   │  │
│                         │    │  │  │  │  ┌──────────────────────────┐   │  │  │   │  │
│                         │    │  │  │  │  │   Report Generation      │   │  │  │   │  │
│                         │    │  │  │  │  │  • Annotated 2D/3D views  │   │  │  │   │  │
│                         │    │  │  │  │  │  • Scorecard dashboard    │   │  │  │   │  │
│                         │    │  │  │  │  │  • Issue prioritization     │   │  │  │   │  │
│                         │    │  │  │  │  │  • Fix recommendations      │   │  │  │   │  │
│                         │    │  │  │  │  │  • Historical comparison      │   │  │  │   │  │
│                         │    │  │  │  │  │  • Export (PDF, share link)   │   │  │  │   │  │
│                         │    │  │  │  │  └───────────────────────────────┘   │  │  │   │  │
│                         │    │  │  │  │                                    │  │  │   │  │
│                         │    │  │  │  └────────────────────────────────────┘  │  │   │  │
│                         │    │  │  └─────────────────────────────────────────┘  │   │  │
│                         │    │  └─────────────────────────────────────────────────┘   │  │
│                         │  └───────────────────────────────────────────────────────────┘   │
│                         └───────────────────────────────────────────────────────────────────┘
│                                                                                              │
└──────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Dependencies & Integration Points

### Internal Dependencies
- **WP01 (Input Sanitization):** CAD file metadata sanitization before parsing
- **WP02 (Adversarial Defense):** VLM prompts sanitized to prevent injection
- **WP03 (Runtime Monitoring):** CAD evaluation metrics and anomaly detection
- **WP04 (Audit & Compliance):** All CAD evaluations logged for compliance

### External Dependencies
- **OpenCASCADE/CadQuery:** B-rep geometry processing
- **Three.js:** Web-based 3D visualization
- **VLM APIs:** GPT-4V, Claude 3.5 Sonnet, or Gemini Pro Vision
- **Vector Database:** Pinecone, Weaviate, or Milvus
- **ProtoLabs Knowledge Base:** DFM rules and guidelines

### Integration Points
- **Quote System:** DFM scores feed into pricing algorithms
- **CRM:** DFM reports attached to customer records
- **PLM:** Integration with Siemens, PTC, Dassault systems
- **CAD Plugins:** SolidWorks, Fusion 360, CATIA, NX integration
- **MES/ERP:** Feedback from production outcomes

---

## Resource Requirements

### Personnel (12 weeks)

| Role | Count | Duration | Effort |
|------|-------|----------|--------|
| ML Engineer | 2 | 12 weeks | 24 person-weeks |
| CAD/Geometry Engineer | 2 | 12 weeks | 24 person-weeks |
| Backend Engineer | 2 | 10 weeks | 20 person-weeks |
| Frontend Engineer | 1 | 8 weeks | 8 person-weeks |
| Manufacturing Engineer | 1 | 6 weeks | 6 person-weeks |
| DevOps Engineer | 1 | 4 weeks | 4 person-weeks |
| **Total** | **10** | | **110 person-weeks** |

### Infrastructure

| Component | Specification | Cost (12 weeks) |
|-----------|---------------|-----------------|
| Compute (GPU) | 4× A100 for VLM inference + training | $48,000 |
| Compute (CPU) | 8× c6i.2xlarge for API/services | $12,000 |
| Storage | 10TB S3 for CAD files + 2TB SSD for DB | $3,000 |
| Vector DB | Pinecone/Weaviate production tier | $6,000 |
| VLM API | GPT-4V + Claude 3.5 usage | $15,000 |
| Monitoring | Datadog/New Relic | $3,000 |
| **Total Infrastructure** | | **$90,000** |

### Total Budget: $600,000
- Personnel: $510,000 (110 weeks × $4,636/week blended rate)
- Infrastructure: $90,000

---

## Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| VLM hallucination produces incorrect DFM | Medium | High | Hybrid approach: VLM + rule validation; confidence scoring |
| CAD format complexity causes parsing failures | Medium | Medium | Start with STEP/STL; phased format support; graceful degradation |
| Feature recognition accuracy below target | Medium | High | Combine ML + geometric algorithms; human-in-the-loop validation |
| VLM API latency impacts user experience | Low | Medium | Caching; async processing; progress indicators |
| Historical data insufficient for similarity | Low | Medium | Bootstrap with synthetic data; accumulate over time |
| Integration complexity with existing systems | Medium | Medium | API-first design; phased rollout; backward compatibility |

---

## Success Metrics

### Technical Metrics

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| CAD parsing success rate | >99% | Automated testing on validation set |
| Feature detection precision | >95% | Manual validation on test set |
| Feature detection recall | >90% | Manual validation on test set |
| End-to-end latency | <60s | Performance monitoring |
| VLM inference time | <5s | API monitoring |
| System uptime | 99.9% | Infrastructure monitoring |
| API availability | 99.95% | Health check monitoring |

### Business Metrics

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| Quote turnaround time | -50% | Before/after comparison |
| Design iteration reduction | -40% | Customer survey |
| DFM explanation satisfaction | >4.0/5.0 | User feedback survey |
| Customer adoption rate | >50% | Analytics tracking |
| Support ticket reduction | -30% | Support system metrics |
| Engineer time savings | 60% | Time tracking analysis |
| Win rate improvement | +15% | Sales metrics |

---

## Deliverables

### Code Deliverables

1. **CAD Parser Service** (`services/cad-parser/`)
   - Multi-format CAD parsing (STEP, STL, OBJ, 3MF, IGES)
   - Geometry extraction and normalization
   - PMI data harvesting
   - 2D view generation

2. **Feature Recognition Service** (`services/feature-recognition/`)
   - Hole detection and measurement
   - Pocket recognition
   - Boss identification
   - Thread detection
   - Thin wall analysis
   - Undercut detection
   - Draft angle calculation

3. **VLM Analysis Service** (`services/vlm-analysis/`)
   - Visual DFM assessment
   - Design comparison
   - Anomaly detection
   - Explanation generation
   - Fix suggestion

4. **DFM Rule Engine** (`services/dfm-engine/`)
   - Rule codification and versioning
   - Geometric constraint checking
   - Manufacturability scoring
   - Issue prioritization
   - Fix recommendation

5. **Historical Comparison Service** (`services/historical-comparison/`)
   - Vector database management
   - Geometry embedding generation
   - Similarity search
   - Pattern learning

6. **API Gateway** (`services/api-gateway/`)
   - REST API endpoints
   - Authentication and authorization
   - Rate limiting
   - Request routing

### Documentation Deliverables

1. **API Documentation** (`docs/api/`)
   - OpenAPI specification
   - Endpoint documentation
   - Authentication guide
   - SDK documentation

2. **Integration Guide** (`docs/integration/`)
   - PLM integration guide
   - CAD plugin development guide
   - MES/ERP integration
   - Webhook configuration

3. **User Guide** (`docs/user/`)
   - Upload portal guide
   - DFM report interpretation
   - Fix recommendation guide
   - FAQ

4. **Operations Guide** (`docs/ops/`)
   - Deployment guide
   - Monitoring and alerting
   - Troubleshooting
   - Disaster recovery

### Model Deliverables

1. **Feature Recognition Model** (`models/feature-recognition/`)
   - Trained model weights
   - Model card with performance metrics
   - Inference pipeline
   - Training data documentation

2. **Similarity Embedding Model** (`models/similarity-embedding/`)
   - Trained model weights
   - Model card
   - Embedding generation pipeline
   - Similarity calculation

3. **DFM Scoring Model** (`models/dfm-scoring/`)
   - Trained regression model
   - Model card
   - Scoring pipeline
   - Calibration data

---

## Testing Strategy

### Unit Testing
- Every service component has >80% code coverage
- Feature recognition models tested on validation set
- Rule engine tested against all DFM guidelines

### Integration Testing
- End-to-end CAD upload to report flow
- VLM integration with mock and real APIs
- Database integration and query performance

### Performance Testing
- Load testing: 100 concurrent uploads
- Latency testing: p50, p95, p99 response times
- Throughput testing: designs per minute

### Accuracy Testing
- Feature detection benchmark vs. manual annotation
- DFM score correlation with expert ratings
- Historical similarity relevance scoring

### User Acceptance Testing
- Beta testing with select customers
- Engineer validation of DFM accuracy
- UI/UX feedback on report clarity

---

## Deployment Plan

### Phase 1: Foundation (Weeks 1-3)
- Deploy CAD parser service
- Deploy feature recognition service
- Deploy basic DFM rule engine
- Set up development environment

### Phase 2: Intelligence (Weeks 4-6)
- Deploy VLM analysis service
- Deploy historical comparison service
- Integrate all services
- Deploy API gateway

### Phase 3: Scale (Weeks 7-12)
- Production deployment
- Load balancer and auto-scaling
- Monitoring and alerting
- Documentation and training

---

## Related Documents

- [AI CAD Design Features Catalogue](../AI-CAD-DESIGN-FEATURES-CATALOGUE.md)
- [Jobs to be Done Framework](../00-JTBD-and-problem-statements/jobs-to-be-done-framework.md)
- [Problem Statements](../00-JTBD-and-problem-statements/problem-statements.md)
- [CAD Parser Agent](../../agents/cad-parser.agent.md)
- [DFM Router Agent](../../agents/dfm-router.agent.md)

---

*Work Package Version: 1.0*  
*Last Updated: April 23, 2026*  
*Owner: Director of AI Products*  
*Status: Planning*
