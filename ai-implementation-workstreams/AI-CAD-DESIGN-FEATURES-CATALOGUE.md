# AI CAD Design Features Catalogue

## Executive Summary

This catalogue documents the comprehensive feature set for AI-powered CAD design evaluation and Design for Manufacturability (DFM) analysis at ProtoLabs. The system combines Vision-Language Models (VLMs), geometric feature recognition, and rule-based validation to automatically evaluate 3D CAD uploads against manufacturing constraints.

---

## 1. Core Feature Categories

### 1.1 CAD File Ingestion & Parsing

| Feature ID | Feature Name | Description | Benefits | AI/Data Components |
|------------|--------------|-------------|----------|------------------|
| CAD-001 | Multi-Format Parser | Parse STEP, STL, OBJ, 3MF, IGES files with precision handling | Universal compatibility; single entry point for all CAD uploads | OpenCASCADE/CadQuery for B-rep; Three.js for mesh formats |
| CAD-002 | Geometry Extraction | Extract bounding box, volume, surface area, center of mass | Immediate design metrics for initial assessment | Geometric algorithms; NURBS surface evaluation |
| CAD-003 | PMI Data Harvesting | Extract Product Manufacturing Information (PMI) from STEP: tolerances, materials, surface finish | Preserves design intent; captures engineering requirements | STEP AP242 parsing; GD&T interpretation |
| CAD-004 | Assembly Structure Parser | Parse multi-part assemblies, BOM relationships, component hierarchies | Enables complex product evaluation; supports assembly DFM | STEP assembly structures; OCC compound shapes |

### 1.2 Feature Recognition & Extraction

| Feature ID | Feature Name | Description | Benefits | AI/Data Components |
|------------|--------------|-------------|----------|------------------|
| FTR-001 | Hole Detection | Identify cylindrical holes: diameter, depth, position, axis direction, bottom type | Critical for machining access; drill sizing; tool selection | Cylindrical surface detection; aspect ratio analysis |
| FTR-002 | Pocket Recognition | Detect internal cavities: depth, corner radius, floor radius, draft angle | Essential for CNC toolpath planning; moldability assessment | Closed boundary detection; wall angle calculation |
| FTR-003 | Boss Identification | Find protrusions: height, diameter, draft angle | Critical for molding; structural integrity; assembly features | Protrusion detection; height measurement |
| FTR-004 | Fillet & Chamfer Detection | Recognize edge treatments: radius, angle, edge chain | Surface finish requirements; stress concentration analysis | Edge curvature analysis; adjacent face angles |
| FTR-005 | Thread Recognition | Detect threaded features: pitch, diameter, handedness | Critical for assembly; mating part requirements | Helix detection; pitch calculation |
| FTR-006 | Thin Wall Analysis | Identify thin sections: minimum/maximum thickness | Critical for molding flow; 3D print structural integrity | Thickness mapping; minimum distance calculation |
| FTR-007 | Undercut Detection | Find features requiring side actions: angle, depth | Essential for molding feasibility; side core requirements | Shadow analysis; accessibility checking |
| FTR-008 | Draft Angle Analysis | Calculate wall taper angles: positive/negative draft | Critical for mold release; injection molding feasibility | Surface normal analysis; taper calculation |

### 1.3 AI-Powered Visual Analysis (VLM Integration)

| Feature ID | Feature Name | Description | Benefits | AI/Data Components |
|------------|--------------|-------------|----------|------------------|
| VLM-001 | 2D View Generation | Auto-generate orthographic views (front, top, side) + isometric from 3D model | Standard engineering documentation; VLM input preparation | Three.js rendering; orthographic projection |
| VLM-002 | Section View Creation | Generate cross-sectional views at user-defined or auto-suggested planes | Internal feature visibility; DFM analysis of hidden geometry | CSG operations; clipping plane rendering |
| VLM-003 | Detail View Extraction | Auto-zoom to critical features (holes, thin walls, undercuts) | Focused analysis; issue highlighting | Feature bounding box; camera positioning |
| VLM-004 | Visual DFM Assessment | VLM analyzes 2D/3D views for manufacturability issues not captured by rules | Catches edge cases; qualitative reasoning; "manufacturing intuition" | GPT-4V/Claude 3.5 Sonnet/Gemini Pro Vision |
| VLM-005 | Design Comparison | Compare uploaded design against similar past projects using visual similarity | Pattern recognition; historical learning; trend identification | Vector embeddings; similarity search |
| VLM-006 | Anomaly Detection | Identify unusual design features that may indicate errors or innovation | Quality control; innovation spotting; risk flagging | Statistical outlier detection; VLM reasoning |
| VLM-007 | Natural Language Explanations | Generate human-readable explanations of DFM issues with visual annotations | Accessibility; education; customer communication | VLM captioning; structured output generation |
| VLM-008 | Multi-Modal Reasoning | Combine geometric data, visual analysis, and text prompts for holistic evaluation | Comprehensive assessment; context-aware decisions | Multi-modal LLM architectures |

### 1.4 DFM Rule Engine & Validation

| Feature ID | Feature Name | Description | Benefits | AI/Data Components |
|------------|--------------|-------------|----------|------------------|
| DFM-001 | Rulebook Codification | Structured DFM rules as machine-readable YAML/JSON (min hole size, max aspect ratio, draft angles) | Automated validation; consistent application; version control | Rule engine; JSON Schema validation |
| DFM-002 | Geometric Constraint Checking | Validate extracted features against process-specific constraints (CNC, molding, 3D printing) | Process feasibility; early issue detection | Constraint solver; geometric algorithms |
| DFM-003 | Tolerance Stack-Up Analysis | Calculate cumulative tolerances across part features and assemblies | Quality prediction; fit verification; GD&T compliance | Statistical tolerance analysis; Monte Carlo simulation |
| DFM-004 | Material-Process Compatibility | Check if selected material is compatible with chosen manufacturing process | Feasibility validation; cost optimization; quality assurance | Material database; process compatibility matrix |
| DFM-005 | Cost Estimation Integration | Link DFM scores to cost drivers (setup time, tooling, scrap rate) | Business impact quantification; design optimization | Cost models; regression analysis |
| DFM-006 | Manufacturability Scoring | Generate composite score (0-100) based on rule compliance and VLM assessment | Quantified assessment; benchmarking; improvement tracking | Weighted scoring algorithm; ML-based calibration |
| DFM-007 | Issue Prioritization | Rank DFM issues by severity (Critical/Warning/Note) and fix effort | Actionable guidance; resource allocation; quick wins | Risk matrix; effort estimation |
| DFM-008 | Fix Recommendation Engine | Suggest specific design modifications to resolve DFM issues | Guided improvement; education; automation potential | Rule-based suggestions; VLM-generated alternatives |

### 1.5 Historical Comparison & Learning

| Feature ID | Feature Name | Description | Benefits | AI/Data Components |
|------------|--------------|-------------|----------|------------------|
| HST-001 | Project Vector Database | Store embeddings of past CAD designs for similarity search | Institutional memory; pattern recognition; trend analysis | Vector DB (Pinecone/Weaviate); embedding models |
| HST-002 | Geometry Fingerprinting | Generate compact signatures of CAD geometry for efficient comparison | Fast similarity search; duplicate detection; versioning | Shape descriptors; perceptual hashing |
| HST-003 | Historical Issue Mapping | Link past DFM issues to design patterns for predictive flagging | Proactive warning; learning from mistakes; risk prevention | Pattern matching; association rule mining |
| HST-004 | Similar Project Retrieval | Find past projects similar to uploaded design for reference | Benchmarking; lessons learned; design inspiration | Similarity search; k-NN algorithms |
| HST-005 | Success Pattern Learning | Identify design patterns that consistently yield good outcomes | Best practice extraction; design guidance; training data | Supervised learning; pattern recognition |
| HST-006 | Failure Mode Database | Catalog historical manufacturing failures with root causes | Risk awareness; prevention; institutional knowledge | Root cause analysis; knowledge graph |
| HST-007 | Cross-Project Analytics | Aggregate insights across projects for trend identification | Strategic insights; process improvement; forecasting | Time series analysis; statistical modeling |
| HST-008 | Continuous Learning Loop | Feedback from manufacturing outcomes improves DFM models | Model improvement; accuracy enhancement; adaptation | Reinforcement learning; online learning |

---

## 2. Integration Features

### 2.1 API & Service Integration

| Feature ID | Feature Name | Description | Benefits | AI/Data Components |
|------------|--------------|-------------|----------|------------------|
| INT-001 | REST API Gateway | HTTP/REST interface for CAD upload and DFM evaluation | Integration; automation; third-party access | FastAPI/Flask; OpenAPI spec |
| INT-002 | GraphQL Endpoint | Flexible query interface for complex DFM data retrieval | Efficient data fetching; client optimization | GraphQL; schema stitching |
| INT-003 | Webhook Support | Real-time notifications for DFM completion and issues | Event-driven integration; automation | Webhook handlers; event bus |
| INT-004 | Batch Processing API | Submit multiple CAD files for bulk DFM evaluation | Scale; efficiency; enterprise workflows | Job queue; Celery/RQ |
| INT-005 | SDK/Library Distribution | Client libraries (Python, JavaScript, C#) for easy integration | Developer experience; adoption | PyPI/npm/NuGet packages |
| INT-006 | PLM Integration | Connect to Siemens Teamcenter, PTC Windchill, Dassault ENOVIA | Enterprise workflow; design continuity | PLM APIs; connector framework |
| INT-007 | CAD Plugin Integration | Plugins for SolidWorks, Fusion 360, CATIA, NX | Designer workflow; real-time feedback | CAD APIs; plugin architecture |
| INT-008 | MES/ERP Integration | Connect to manufacturing execution and ERP systems | Production continuity; closed-loop feedback | MES APIs; ERP connectors |

### 2.2 User Interface Features

| Feature ID | Feature Name | Description | Benefits | AI/Data Components |
|------------|--------------|-------------|----------|------------------|
| UI-001 | Web Upload Portal | Drag-and-drop CAD file upload with progress indication | Ease of use; accessibility; customer self-service | React/Vue frontend; upload handlers |
| UI-002 | Interactive 3D Viewer | Browser-based 3D model viewing with rotation, zoom, section | Design review; issue visualization | Three.js/WebGL; CAD conversion |
| UI-003 | DFM Dashboard | Scorecard view of manufacturability with issue breakdown | At-a-glance assessment; prioritization | Data visualization; scoring engine |
| UI-004 | Annotated Issue Viewer | Highlight DFM issues directly on 2D/3D views | Clear communication; precise location | Annotation engine; overlay rendering |
| UI-005 | Recommendation Panel | Side-by-side design comparison with fix suggestions | Guided improvement; education | Diff viewer; suggestion engine |
| UI-006 | Historical Comparison Tool | Compare current design against similar past projects | Learning; benchmarking; trend analysis | Similarity search; comparison UI |
| UI-007 | Collaboration Workspace | Share DFM reports with team members, add comments | Team coordination; design review | Real-time collaboration; commenting |
| UI-008 | Mobile Responsive Design | Access DFM reports on mobile devices | Field access; executive review | Responsive design; mobile optimization |

---

## 3. Data & AI Infrastructure

### 3.1 Data Management

| Feature ID | Feature Name | Description | Benefits | AI/Data Components |
|------------|--------------|-------------|----------|------------------|
| DATA-001 | CAD File Repository | Secure storage for uploaded CAD files with versioning | Data retention; audit trail; re-analysis | S3/MinIO; Git LFS; encryption |
| DATA-002 | Feature Database | Structured storage for extracted geometric features | Queryable geometry; trend analysis | PostgreSQL/PostGIS; feature schema |
| DATA-003 | DFM Results Store | Historical DFM evaluations with scores and recommendations | Continuous improvement; reporting | Time-series DB; result schema |
| DATA-004 | Vector Database | Embeddings of CAD designs for similarity search | Fast retrieval; pattern matching | Pinecone/Weaviate/Milvus |
| DATA-005 | Knowledge Graph | Relationships between designs, issues, materials, processes | Semantic reasoning; root cause analysis | Neo4j/RDF store; ontology |
| DATA-006 | Training Data Pipeline | Curated datasets for model fine-tuning and validation | Model improvement; accuracy | Data labeling; version control |
| DATA-007 | Data Quality Monitoring | Automated checks for data completeness, consistency, accuracy | Reliable AI; garbage detection | Great Expectations; Soda |
| DATA-008 | Data Lineage Tracking | Trace data flow from CAD upload to DFM report | Auditability; debugging; compliance | Apache Atlas; OpenLineage |

### 3.2 AI/ML Infrastructure

| Feature ID | Feature Name | Description | Benefits | AI/Data Components |
|------------|--------------|-------------|----------|------------------|
| ML-001 | VLM Inference Service | Managed inference for GPT-4V, Claude 3.5, Gemini Pro Vision | Visual reasoning; DFM assessment | OpenAI API; Anthropic API; Vertex AI |
| ML-002 | Feature Recognition Model | ML model for detecting manufacturing features in CAD geometry | Accurate feature detection; automation | PointNet/Graph Neural Networks |
| ML-003 | Similarity Embedding Model | Generate vector embeddings of CAD geometry for comparison | Fast similarity search; clustering | 3D ShapeNet; Point Transformer |
| ML-004 | DFM Scoring Model | ML-based manufacturability scoring calibrated on historical data | Accurate predictions; continuous learning | Gradient boosting; Neural networks |
| ML-005 | Anomaly Detection Model | Unsupervised learning for unusual design patterns | Catch errors; identify innovation | Isolation Forest; Autoencoders |
| ML-006 | Recommendation Engine | Suggest design improvements based on successful past projects | Guided optimization; education | Collaborative filtering; Case-based reasoning |
| ML-007 | Model Versioning & Registry | Track model versions, performance, and lineage | Reproducibility; rollback; audit | MLflow; Weights & Biases |
| ML-008 | A/B Testing Framework | Compare model variants in production | Continuous improvement; validation | Split testing; statistical analysis |

---

## 4. Manufacturing Process Capabilities

### 4.1 CNC Machining DFM

| Feature ID | Feature Name | Description | DFM Rules | AI Components |
|------------|--------------|-------------|-----------|---------------|
| CNC-001 | Hole Machinability | Evaluate hole sizes, depths, aspect ratios | Min Ø0.5mm; Max depth 3×Ø standard, 20×Ø gun drilling | VLM visual assessment + geometric validation |
| CNC-002 | Pocket Analysis | Assess pocket depth, corner radii, floor thickness | Min corner radius 0.5mm; Max depth 2×tool Ø | Feature recognition + rule validation |
| CNC-003 | Wall Thickness Check | Evaluate thin wall sections for deflection risk | Min 0.5mm for metals; 1.0mm for plastics | Thickness analysis + FEA simulation |
| CNC-004 | Undercut Detection | Identify features requiring special tooling | Flag T-slots, dovetails, internal threads | Accessibility analysis + VLM confirmation |
| CNC-005 | Setup Analysis | Determine number of setups required | Minimize setups; identify 4th/5th axis needs | Orientation optimization + feature clustering |
| CNC-006 | Tool Accessibility | Check if standard tools can reach all features | Flag deep/narrow features; suggest tool lengths | Reach analysis + collision detection |
| CNC-007 | Surface Finish Prediction | Estimate achievable surface finish by feature | Ra 0.4-6.3 μm typical; flag tight requirements | Process knowledge base + feature mapping |
| CNC-008 | Tolerance Feasibility | Evaluate if tolerances are achievable | ±0.05mm standard; ±0.01mm precision | Capability analysis + Cpk estimation |

### 4.2 Injection Molding DFM

| Feature ID | Feature Name | Description | DFM Rules | AI Components |
|------------|--------------|-------------|-----------|---------------|
| MLD-001 | Wall Thickness Uniformity | Evaluate thickness variation across part | Target <15% variation; min 0.5mm, max 4mm | Thickness mapping + VLM assessment |
| MLD-002 | Draft Angle Analysis | Check all vertical surfaces for adequate draft | Min 0.5° per side; 1-2° recommended | Surface normal analysis + draft calculation |
| MLD-003 | Undercut Detection | Identify features requiring side actions or lifters | Flag internal snaps, threads, external undercuts | Accessibility analysis + mold split simulation |
| MLD-004 | Boss Design Evaluation | Assess boss height, diameter, and attachment | Height <3×diameter; adequate fillets | Feature recognition + structural analysis |
| MLD-005 | Rib Design Analysis | Evaluate rib height, thickness, and draft | Height <3×thickness; 0.5-1° draft | Rib detection + proportion validation |
| MLD-006 | Gate Location Suggestion | Recommend optimal gate placement | Consider flow path, weld lines, aesthetics | Flow simulation + VLM visual assessment |
| MLD-007 | Sink Mark Prediction | Identify locations prone to sink marks | Thick sections, boss attachments, rib intersections | Thickness analysis + cooling simulation |
| MLD-008 | Warp Analysis Flag | Highlight geometries prone to warpage | Large flat sections, asymmetric designs, varying thickness | FEA simulation + VLM assessment |

### 4.3 3D Printing DFM

| Feature ID | Feature Name | Description | DFM Rules | AI Components |
|------------|--------------|-------------|-----------|---------------|
| PRT-001 | Build Orientation Optimization | Suggest optimal part orientation for each technology | Minimize supports; optimize surface finish; reduce build time | VLM analysis + support simulation |
| PRT-002 | Support Structure Analysis | Evaluate support requirements and accessibility | Flag hard-to-remove supports; suggest self-supporting angles | Overhang detection + support generation |
| PRT-003 | Minimum Feature Size Check | Verify features are printable at requested resolution | Min wall 0.5-1mm; min hole Ø0.5-1mm; detail resolution | Feature measurement + process capability |
| PRT-004 | Layer Height Suitability | Match layer height to feature requirements and surface finish | Fine features need finer layers; balance quality vs speed | Feature analysis + parameter recommendation |
| PRT-005 | Part Nesting Efficiency | Evaluate how efficiently part fits in build envelope | Maximize build density; reduce cost per part | Packing algorithms + VLM assessment |
| PRT-006 | Surface Finish Prediction | Estimate achievable surface quality by technology and orientation | Set expectations; guide post-processing decisions | Process knowledge base + orientation analysis |
| PRT-007 | Material-Specific Constraints | Apply technology-specific rules (SLA vs SLS vs FDM vs DMLS) | Accurate DFM for each technology | Technology rule sets; material databases |
| PRT-008 | Post-Processing Requirements | Identify required post-processing steps | Cost estimation; lead time prediction; quality planning | Process planning knowledge; VLM assessment |

### 4.4 Sheet Metal DFM

| Feature ID | Feature Name | Description | DFM Rules | AI Components |
|------------|--------------|-------------|-----------|---------------|
| SHT-001 | Bend Radius Validation | Check inside bend radius against material thickness | Min radius = material thickness (typically) | Bend detection + thickness correlation |
| SHT-002 | Bend Relief Analysis | Evaluate need for bend relief cuts | Required when bend intersects edge | Feature detection + geometry analysis |
| SHT-003 | Hole-to-Bend Distance | Verify adequate distance between holes and bends | Min 2× material thickness + bend radius | Proximity analysis + rule validation |
| SHT-004 | Flat Pattern Generation | Create flat pattern for bend visualization | Manufacturing documentation; material estimation | Unfolding algorithms; bend deduction |
| SHT-005 | Hem Design Evaluation | Assess hems for feasibility and tooling | Min 4× material thickness for closed hem | Hem detection + dimension validation |
| SHT-006 | Lancing/Louver Analysis | Check formed features for tooling compatibility | Evaluate geometry against tooling constraints | Feature recognition + tooling database |
| SHT-007 | Material Utilization | Estimate nesting efficiency on standard sheet sizes | Cost optimization; waste reduction | Nesting algorithms; VLM assessment |
| SHT-008 | Weld/Join Design | Evaluate weld accessibility and joint design | Assembly feasibility; quality assurance | Joint detection + accessibility analysis |

---

## 2. AI & Data Capabilities

### 2.1 Vision-Language Model (VLM) Features

| Capability ID | Capability | Description | Model Requirements |
|---------------|------------|-------------|-------------------|
| VLM-CAP-001 | Visual Geometry Understanding | Interpret 2D engineering drawings and 3D renderings to understand part geometry | GPT-4V, Claude 3.5 Sonnet, or Gemini Pro Vision |
| VLM-CAP-002 | DFM Issue Detection | Identify manufacturability issues from visual inspection that rules might miss | Fine-tuned VLM on manufacturing dataset |
| VLM-CAP-003 | Design Comparison | Visually compare two designs and highlight differences relevant to manufacturing | Multi-image VLM input; difference highlighting |
| VLM-CAP-004 | Anomaly Explanation | Generate natural language explanations of why a feature is unusual or problematic | Chain-of-thought reasoning; structured output |
| VLM-CAP-005 | Fix Visualization | Suggest and visualize design modifications to resolve DFM issues | Generative capabilities; CAD manipulation guidance |
| VLM-CAP-006 | Material Appearance | Assess surface finish, texture, and appearance requirements from visual cues | Material knowledge; rendering understanding |
| VLM-CAP-007 | Assembly Visualization | Understand assembly relationships from exploded views or animations | Spatial reasoning; relationship extraction |
| VLM-CAP-008 | Tolerance Visualization | Interpret GD&T annotations and tolerance specifications from drawings | Symbol recognition; semantic understanding |

### 2.2 Machine Learning Models

| Model ID | Model Name | Purpose | Training Data | Performance Targets |
|----------|------------|---------|---------------|---------------------|
| ML-001 | Feature Recognition CNN | Detect manufacturing features in CAD geometry | 100K+ labeled CAD models | >95% precision, >90% recall |
| ML-002 | Similarity Embedding Model | Generate geometry fingerprints for comparison | 500K+ CAD models | Top-5 accuracy >90% |
| ML-003 | DFM Scoring Regressor | Predict manufacturability score from features | Historical DFM evaluations | RMSE <10 points (0-100 scale) |
| ML-004 | Anomaly Detection | Identify unusual design patterns | Normal design distribution | F1-score >0.85 |
| ML-005 | Cost Estimation | Predict manufacturing cost from geometry | Historical quotes | ±15% accuracy |
| ML-006 | Process Selection | Recommend optimal manufacturing process | Design-process-outcome data | Top-1 accuracy >85% |
| ML-007 | Lead Time Prediction | Estimate production lead time | Historical production data | ±20% accuracy |
| ML-008 | Quality Prediction | Predict defect probability | Historical quality data | AUC-ROC >0.85 |

### 2.3 Data Infrastructure

| Component ID | Component | Description | Technology Stack |
|--------------|-----------|-------------|----------------|
| DATA-001 | CAD File Store | Secure object storage for uploaded CAD files | S3/MinIO with encryption |
| DATA-002 | Feature Database | Relational store for extracted geometric features | PostgreSQL + PostGIS |
| DATA-003 | Vector Database | Embedding storage for similarity search | Pinecone/Weaviate/Milvus |
| DATA-004 | Time-Series DB | Metrics and monitoring data | InfluxDB/TimescaleDB |
| DATA-005 | Knowledge Graph | Relationships between designs, issues, materials | Neo4j/RDF store |
| DATA-006 | Audit Log Store | Immutable, tamper-evident audit records | Blockchain/WORM storage |
| DATA-007 | Cache Layer | Fast access to frequently requested data | Redis/Memcached |
| DATA-008 | Data Lake | Raw data storage for analytics and ML | Delta Lake/Iceberg |

---

## 3. DFM Capabilities by Manufacturing Process

### 3.1 CNC Machining DFM

| Capability ID | Capability | Description | Rule Source |
|---------------|------------|-------------|-------------|
| CNC-DFM-001 | Hole Machinability | Evaluate hole diameter, depth, aspect ratio | [knowledge/cnc-machining/mastering-complex-features.md](https://www.protolabs.com/resources/design-tips/mastering-complex-features-on-machined-parts/) |
| CNC-DFM-002 | Pocket Feasibility | Assess pocket depth, corner radius, accessibility | [knowledge/cnc-machining/mastering-complex-features.md](https://www.protolabs.com/resources/design-tips/mastering-complex-features-on-machined-parts/) |
| CNC-DFM-003 | Wall Thickness | Check minimum wall thickness for rigidity | [knowledge/cnc-machining/cnc-tolerances.md](https://www.protolabs.com/resources/design-tips/cnc-tolerances/) |
| CNC-DFM-004 | Setup Count | Estimate number of setups required | [knowledge/cnc-machining/cnc-for-prototypes.md](https://www.protolabs.com/resources/design-tips/cnc-machining-for-prototypes/) |
| CNC-DFM-005 | Tool Accessibility | Verify all features reachable with standard tools | [knowledge/cnc-machining/mastering-complex-features.md](https://www.protolabs.com/resources/design-tips/mastering-complex-features-on-machined-parts/) |
| CNC-DFM-006 | Surface Finish | Predict achievable surface finish by feature | [knowledge/cnc-machining/cnc-tolerances.md](https://www.protolabs.com/resources/design-tips/cnc-tolerances/) |
| CNC-DFM-007 | Tolerance Feasibility | Evaluate if specified tolerances are achievable | [knowledge/cnc-machining/cnc-tolerances.md](https://www.protolabs.com/resources/design-tips/cnc-tolerances/) |
| CNC-DFM-008 | Thread Machinability | Check thread specifications for feasibility | [knowledge/cnc-machining/cnc-threading.md](https://www.protolabs.com/resources/design-tips/cnc-threading/) |

### 3.2 Injection Molding DFM

| Capability ID | Capability | Description | Rule Source |
|---------------|------------|-------------|-------------|
| MLD-DFM-001 | Wall Thickness Uniformity | Evaluate thickness variation across part | [knowledge/injection-molding/wall-thickness.md](https://www.protolabs.com/resources/design-tips/injection-molding-wall-thickness/) |
| MLD-DFM-002 | Draft Angle Adequacy | Check all vertical surfaces for adequate draft | [knowledge/injection-molding/moldability-fundamentals.md](https://www.protolabs.com/resources/design-tips/injection-molding-design/) |
| MLD-DFM-003 | Undercut Identification | Find features requiring side actions or lifters | [knowledge/injection-molding/moldability-complex-features.md](https://www.protolabs.com/resources/design-tips/designing-for-complex-injection-molding/) |
| MLD-DFM-004 | Boss Design Validation | Assess boss geometry for strength and moldability | [knowledge/injection-molding/moldability-complex-features.md](https://www.protolabs.com/resources/design-tips/designing-for-complex-injection-molding/) |
| MLD-DFM-005 | Rib Design Check | Evaluate rib proportions and draft | [knowledge/injection-molding/moldability-fundamentals.md](https://www.protolabs.com/resources/design-tips/injection-molding-design/) |
| MLD-DFM-006 | Gate Location Analysis | Suggest optimal gate placement for flow | [knowledge/injection-molding/scientific-molding.md](https://www.protolabs.com/resources/design-tips/scientific-molding/) |
| MLD-DFM-007 | Sink Mark Prediction | Identify locations prone to sink marks | [knowledge/injection-molding/cosmetic-appearance.md](https://www.protolabs.com/resources/design-tips/cosmetic-appearances/) |
| MLD-DFM-008 | Weld Line Prediction | Predict knit line locations from flow simulation | [knowledge/injection-molding/scientific-molding.md](https://www.protolabs.com/resources/design-tips/scientific-molding/) |

### 3.3 3D Printing DFM

| Capability ID | Capability | Description | Rule Source |
|---------------|------------|-------------|-------------|
| PRT-DFM-001 | Build Orientation Optimization | Suggest optimal orientation for each technology | [knowledge/3d-printing/design-for-additive-manufacturing.md](https://www.protolabs.com/resources/design-tips/design-for-additive-manufacturing/) |
| PRT-DFM-002 | Support Structure Analysis | Evaluate support needs and accessibility | [knowledge/3d-printing/design-for-additive-manufacturing.md](https://www.protolabs.com/resources/design-tips/design-for-additive-manufacturing/) |
| PRT-DFM-003 | Minimum Feature Size | Verify features are printable at resolution | [knowledge/3d-printing/what-is-3d-printing.md](https://www.protolabs.com/resources/guides-and-trend-reports/what-is-3d-printing/) |
| PRT-DFM-004 | Overhang Angle Check | Identify overhangs requiring support | [knowledge/3d-printing/design-for-additive-manufacturing.md](https://www.protolabs.com/resources/design-tips/design-for-additive-manufacturing/) |
| PRT-DFM-005 | Part Nesting Efficiency | Evaluate build volume utilization | [knowledge/3d-printing/3dp-end-use-production.md](https://www.protolabs.com/resources/design-tips/3d-printing-for-end-use-production/) |
| PRT-DFM-006 | Surface Finish Prediction | Estimate surface quality by orientation | [knowledge/3d-printing/vapor-smoothing.md](https://www.protolabs.com/resources/design-tips/vapor-smoothing/) |
| PRT-DFM-007 | Material-Specific Rules | Apply constraints for SLA/SLS/MJF/FDM/DMLS | [knowledge/3d-printing/3dp-materials-selection.md](https://www.protolabs.com/resources/design-tips/3d-printing-materials-selection/) |
| PRT-DFM-008 | Post-Processing Needs | Identify required finishing operations | [knowledge/3d-printing/vapor-smoothing.md](https://www.protolabs.com/resources/design-tips/vapor-smoothing/) |

### 3.4 Sheet Metal DFM

| Capability ID | Capability | Description | Rule Source |
|---------------|------------|-------------|-------------|
| SHT-DFM-001 | Bend Radius Validation | Check inside bend radius vs material thickness | [knowledge/sheet-metal/designing-for-sheetmetal-fab-guide.md](https://www.protolabs.com/resources/design-tips/designing-for-sheet-metal-fabrication/) |
| SHT-DFM-002 | Bend Relief Analysis | Evaluate need for bend relief cuts | [knowledge/sheet-metal/designing-for-sheetmetal-fab-guide.md](https://www.protolabs.com/resources/design-tips/designing-for-sheet-metal-fabrication/) |
| SHT-DFM-003 | Hole-to-Bend Distance | Verify adequate spacing | [knowledge/sheet-metal/designing-for-sheetmetal-fab-guide.md](https://www.protolabs.com/resources/design-tips/designing-for-sheet-metal-fabrication/) |
| SHT-DFM-004 | Flat Pattern Generation | Create flat pattern for manufacturing | [knowledge/sheet-metal/designing-for-sheetmetal-fab-guide.md](https://www.protolabs.com/resources/design-tips/designing-for-sheet-metal-fabrication/) |
| SHT-DFM-005 | Hem Design Evaluation | Assess hem feasibility | [knowledge/sheet-metal/designing-for-sheetmetal-fab-guide.md](https://www.protolabs.com/resources/design-tips/designing-for-sheet-metal-fabrication/) |
| SHT-DFM-006 | Lancing/Louver Check | Verify formed features | [knowledge/sheet-metal/designing-for-sheetmetal-fab-guide.md](https://www.protolabs.com/resources/design-tips/designing-for-sheet-metal-fabrication/) |
| SHT-DFM-007 | Material Utilization | Estimate sheet nesting efficiency | [knowledge/sheet-metal/designing-for-sheetmetal-fab-guide.md](https://www.protolabs.com/resources/design-tips/designing-for-sheet-metal-fabrication/) |
| SHT-DFM-008 | Weld/Join Accessibility | Evaluate joint access | [knowledge/sheet-metal/designing-for-sheetmetal-fab-guide.md](https://www.protolabs.com/resources/design-tips/designing-for-sheet-metal-fabrication/) |

---

## 5. Benefits Summary

### 5.1 Operational Benefits

| Benefit Category | Specific Benefit | Quantified Impact |
|------------------|------------------|-------------------|
| **Time Savings** | Automated DFM analysis vs manual review | 80% reduction in design review time (from hours to minutes) |
| **Error Reduction** | Catch manufacturability issues before quoting | 60% reduction in design iterations |
| **Consistency** | Standardized DFM evaluation across all designs | 100% coverage vs. spot-checking |
| **Scalability** | Handle increasing design volume without linear staffing | 10× volume increase with same team |
| **Knowledge Retention** | Capture and reuse DFM expertise | Institutional memory preserved |

### 5.2 Business Benefits

| Benefit Category | Specific Benefit | Quantified Impact |
|------------------|------------------|-------------------|
| **Cost Reduction** | Fewer failed quotes, less rework | 25% reduction in quoting costs |
| **Revenue Growth** | Faster turnaround wins more business | 15% increase in quote-to-order conversion |
| **Customer Satisfaction** | Clear, actionable DFM feedback | NPS improvement of 20 points |
| **Competitive Advantage** | AI-powered DFM differentiation | Market leadership in digital manufacturing |
| **Risk Mitigation** | Catch issues before production | 90% reduction in production defects |

### 5.3 Technical Benefits

| Benefit Category | Specific Benefit | Implementation |
|------------------|------------------|----------------|
| **Integration** | Seamless CAD workflow | Plugins for SolidWorks, Fusion 360 |
| **Automation** | Hands-off DFM evaluation | API-first architecture |
| **Extensibility** | Add new processes easily | Modular agent architecture |
| **Intelligence** | Continuous improvement | Feedback loop from production |
| **Observability** | Full visibility into decisions | Comprehensive logging and tracing |

---

## 6. Implementation Roadmap

### Phase 1: Foundation (Months 1-3)
- CAD-001 through CAD-004: Multi-format parsing and geometry extraction
- FTR-001 through FTR-004: Core feature recognition (holes, pockets, bosses, fillets)
- VLM-001 through VLM-003: 2D view generation and visual analysis
- DFM-001 through DFM-003: Rule engine and basic constraint checking

### Phase 2: Intelligence (Months 4-6)
- FTR-005 through FTR-008: Advanced features (threads, thin walls, undercuts, draft)
- VLM-004 through VLM-008: Advanced VLM capabilities (comparison, anomaly detection, explanations)
- HST-001 through HST-004: Historical comparison and similarity search
- CNC-001 through CNC-004, MLD-001 through MLD-004: Process-specific DFM

### Phase 3: Scale (Months 7-12)
- Complete all remaining features
- Integration APIs and plugins
- Advanced analytics and reporting
- Continuous learning and model improvement

---

## 7. Success Metrics

| Metric Category | Metric | Target | Measurement |
|-----------------|--------|--------|-------------|
| **Accuracy** | Feature detection precision | >95% | Manual validation on test set |
| **Coverage** | DFM rule coverage | 100% of ProtoLabs guidelines | Audit against knowledge base |
| **Speed** | End-to-end analysis time | <60 seconds for typical part | Performance testing |
| **Quality** | VLM explanation helpfulness | >4.0/5.0 user rating | User feedback survey |
| **Adoption** | Customer usage rate | >50% of uploads use AI DFM | Analytics tracking |
| **Impact** | Design iteration reduction | 40% fewer design cycles | Before/after comparison |

---

## 8. Related Documents

- [Jobs to be Done Framework](./jobs-to-be-done-framework.md)
- [Problem Statements](./problem-statements.md)
- [Work Package 01 - Input Sanitization](../01-agentic-ready-implementations/work-package-01-input-sanitization.md)
- [Work Package 02 - Adversarial Defense](../01-agentic-ready-implementations/work-package-02-adversarial-defense.md)
- [CAD Parser Agent](../../agents/cad-parser.agent.md)
- [DFM Router Agent](../../agents/dfm-router.agent.md)

---

*Document Version: 1.0*  
*Last Updated: April 23, 2026*  
*Owner: ProtoLabs AI Product Office*
