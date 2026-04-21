---
type: knowledge-article
category: compliance
source_url: https://www.protolabs.com/resources/guides-and-trend-reports/reducing-component-weight-for-automotive-applications/
fetched_at: 2026-04-21
summary: Automotive and EV manufacturing compliance including IATF 16949, UNECE R100 for battery safety, RoHS/REACH environmental regulations, Production Part Approval Process (PPAP), and Advanced Product Quality Planning (APQP) for automotive suppliers.
---

# Automotive and EV Compliance Requirements

## Overview

Automotive manufacturing requires compliance with stringent quality standards, environmental regulations, and safety requirements. Electric vehicle (EV) manufacturing adds additional requirements for battery safety and high-voltage systems. ProtoLabs supports automotive and EV customers with certified manufacturing processes and comprehensive quality systems.

---

## IATF 16949:2016 Automotive Quality Management

### Overview

IATF 16949:2016 is the international automotive quality management system standard, developed by the International Automotive Task Force (IATF). It is based on ISO 9001:2015 with additional automotive-specific requirements.

### Key Automotive Requirements

| Requirement Area | IATF 16949 Specifics | ISO 9001 Base |
|-----------------|----------------------|---------------|
| Customer-Specific Requirements | Mandatory implementation | Not required |
| Embedded Software | Software development requirements | Not addressed |
| Product Safety | Specific safety requirements | General safety |
| Manufacturing Feasibility | Feasibility analysis required | Not required |
| Control Plan | Mandatory for all processes | Not required |
| Traceability | Retrospective and prospective | Not required |
| Supplier Quality | Specific supplier requirements | Basic purchasing |
| Change Control | Enhanced change management | Basic change control |
| Problem Solving | Specific methodologies required | Not required |
| Warranty Management | Specific requirements | Not required |

### Customer-Specific Requirements (CSRs)

IATF 16949 requires organizations to implement customer-specific requirements from OEMs:

| OEM | Document | Key Requirements |
|-----|----------|-------------------|
| General Motors | GM 1927 | APQP, PPAP, control plans |
| Ford | Ford Q1 | Quality system requirements |
| Stellantis | SQ.00001 | Supplier quality requirements |
| Volkswagen | Formel Q | Quality capability requirements |
| BMW | QSB | Quality standards BMW |
| Mercedes | MQAS | Mercedes quality assurance |
| Toyota | Toyota SQ | Toyota supplier quality |
| Honda | Honda SQ | Honda supplier quality |

### Core Tools Requirements

IATF 16949 mandates the use of five core quality tools:

1. **APQP** (Advanced Product Quality Planning)
2. **PPAP** (Production Part Approval Process)
3. **FMEA** (Failure Mode and Effects Analysis)
4. **MSA** (Measurement System Analysis)
5. **SPC** (Statistical Process Control)

### Embedded Software Requirements

For devices with embedded software:

- Software development process per Automotive SPICE or CMMI
- Software validation and verification
- Cybersecurity management (ISO/SAE 21434)
- Software version control and traceability

### Product Safety Requirements

IATF 16949 requires specific product safety processes:

1. **Safety Characteristics Identification**: Critical safety features
2. **Safety-Related FMEA**: Specific FMEA for safety
3. **Safety Control Plans**: Controls for safety characteristics
4. **Safety Training**: Personnel training on safety
5. **Safety Incident Management**: Process for safety issues

### ProtoLabs IATF 16949 Status

ProtoLabs facilities maintain ISO 9001:2015 certification and implement automotive quality practices. For full IATF 16949 compliance requirements, ProtoLabs works with customers to:

- Implement customer-specific requirements
- Provide PPAP documentation
- Support APQP activities
- Maintain traceability records
- Execute control plans

---

## UNECE R100 (Battery Safety for EVs)

### Overview

UNECE Regulation No. 100 (R100) establishes uniform provisions for the approval of vehicles with regard to specific requirements for the electric power train. Part II specifically addresses battery safety for electric vehicles.

### Scope

R100 applies to:
- Battery electric vehicles (BEVs)
- Hybrid electric vehicles (HEVs)
- Fuel cell vehicles with rechargeable energy storage

### R100 Part II Requirements

#### 1. Vibration Test

**Purpose**: Verify battery integrity under vehicle vibration conditions

**Test Conditions**:
- Random vibration profile per ISO 12405 or OEM specification
- Duration: Typically 3 hours per axis (X, Y, Z)
- Temperature: Ambient or specified operating temperature

**Acceptance Criteria**:
- No leakage of electrolyte
- No rupture of battery container
- No fire or explosion
- Voltage and internal resistance within specification

#### 2. Thermal Shock and Cycling Test

**Purpose**: Verify battery integrity under thermal stress

**Test Conditions**:
- Temperature cycling between extremes (e.g., -40°C to +85°C)
- Number of cycles: Typically 50-200 cycles
- Dwell time at temperature extremes: Specified duration

**Acceptance Criteria**:
- No leakage of electrolyte
- No rupture of battery container
- No fire or explosion
- Capacity retention within specification

#### 3. Mechanical Shock Test

**Purpose**: Verify battery integrity under mechanical impact

**Test Conditions**:
- Half-sine shock pulse
- Acceleration: Typically 25g-50g
- Duration: 6-11ms
- Directions: ±X, ±Y, ±Z axes

**Acceptance Criteria**:
- No leakage of electrolyte
- No rupture of battery container
- No fire or explosion
- Voltage and internal resistance within specification

#### 4. External Fire Test

**Purpose**: Verify battery safety in fire conditions

**Test Conditions**:
- Exposure to fuel fire (gasoline or propane)
- Direct flame exposure for specified duration
- Observation period after flame removal

**Acceptance Criteria**:
- No explosion
- No projection of cells outside test area
- Fire must not spread beyond battery pack

#### 5. Overcharge Protection Test

**Purpose**: Verify protection against overcharging

**Test Conditions**:
- Charge at 2x normal charge current
- Continue until 200% of rated capacity or protection activation

**Acceptance Criteria**:
- Protection circuit activates
- No fire or explosion
- No leakage

#### 6. Over-discharge Protection Test

**Purpose**: Verify protection against over-discharging

**Test Conditions**:
- Discharge at specified current
- Continue until 0V or protection activation

**Acceptance Criteria**:
- Protection circuit activates
- No fire or explosion
- Cell remains functional after test

#### 7. Short Circuit Protection Test

**Purpose**: Verify protection against external short circuit

**Test Conditions**:
- Short circuit at specified resistance
- Duration: 24 hours or until protection activation

**Acceptance Criteria**:
- Protection circuit activates
- No fire or explosion
- Temperature within limits

### Battery Cell Requirements

R100 also references UN 38.3 (UN Manual of Tests and Criteria) for lithium cell and battery transport safety:

| Test | Description |
|------|-------------|
| T.1 | Altitude simulation |
| T.2 | Thermal test |
| T.3 | Vibration |
| T.4 | Shock |
| T.5 | External short circuit |
| T.6 | Impact/Crush |
| T.7 | Overcharge |
| T.8 | Forced discharge |

### ProtoLabs EV Battery Component Support

ProtoLabs supports EV battery manufacturing with:

- **Housings and Enclosures**: CNC machined and 3D printed battery housings
- **Connectors and Terminals**: Precision machined electrical components
- **Thermal Management**: Heat sinks, cooling plates
- **Structural Components**: Brackets, mounts, supports
- **Testing Fixtures**: Custom test fixtures for R100 testing

**Note**: ProtoLabs manufactures battery components, not complete battery packs. Battery pack manufacturers are responsible for R100 compliance testing and certification.

---

## RoHS/REACH Environmental Compliance

### Overview

RoHS (Restriction of Hazardous Substances) and REACH (Registration, Evaluation, Authorization and Restriction of Chemicals) are European Union regulations governing chemical substances in products.

### RoHS Directive (2011/65/EU)

**Scope**: Electrical and electronic equipment (EEE)

**Restricted Substances and Limits**:

| Substance | CAS Number | Maximum Concentration |
|-----------|------------|----------------------|
| Lead (Pb) | 7439-92-1 | 0.1% (1000 ppm) |
| Mercury (Hg) | 7439-97-6 | 0.1% (1000 ppm) |
| Cadmium (Cd) | 7440-43-9 | 0.01% (100 ppm) |
| Hexavalent Chromium (CrVI) | 18540-29-9 | 0.1% (1000 ppm) |
| Polybrominated Biphenyls (PBB) | Various | 0.1% (1000 ppm) |
| Polybrominated Diphenyl Ethers (PBDE) | Various | 0.1% (1000 ppm) |
| Bis(2-ethylhexyl) phthalate (DEHP) | 117-81-7 | 0.1% (1000 ppm) |
| Butyl benzyl phthalate (BBP) | 85-68-7 | 0.1% (1000 ppm) |
| Dibutyl phthalate (DBP) | 84-74-2 | 0.1% (1000 ppm) |
| Diisobutyl phthalate (DIBP) | 84-69-5 | 0.1% (1000 ppm) |

**RoHS Exemptions**:
Certain applications may qualify for temporary exemptions. Check current EU exemptions list for applicability.

**RoHS Compliance Verification**:
- Supplier declarations
- Material declarations (IPC-1752A)
- Testing (XRF, chemical analysis)
- Technical documentation

### REACH Regulation (EC 1907/2006)

**Scope**: All substances manufactured or imported into EU in quantities ≥ 1 ton/year

**Key REACH Components**:

#### 1. Registration

| Tonnage Band | Data Requirements |
|--------------|-------------------|
| 1-10 tons/year | Annex VII (basic data) |
| 10-100 tons/year | Annex VIII (extended data) |
| 100-1000 tons/year | Annex IX (comprehensive data) |
| 1000+ tons/year | Annex X (full data) |

#### 2. Evaluation

- **Dossier Evaluation**: ECHA reviews registration dossiers
- **Substance Evaluation**: In-depth assessment of substances of concern

#### 3. Authorization

**Substances of Very High Concern (SVHCs)** require authorization for use:

| SVHC Category | Criteria |
|---------------|----------|
| CMR | Carcinogenic, Mutagenic, toxic to Reproduction (Categories 1A/1B) |
| PBT | Persistent, Bioaccumulative, Toxic |
| vPvB | very Persistent, very Bioaccumulative |
| Endocrine Disruptors | Scientific evidence of endocrine disruption |

**Current SVHC Threshold**: 0.1% w/w (1000 ppm) in article

#### 4. Restriction

Annex XVII of REACH lists restricted substances with specific conditions:

| Substance | Restriction | Application |
|-----------|-------------|-------------|
| Asbestos | Prohibited | All applications |
| Cadmium | Restricted | Plastics, paints |
| Lead | Restricted | Various applications |
| Mercury | Restricted | Batteries, switches |
| Phthalates | Restricted | Toys, childcare articles |
| PFOS | Restricted | Various applications |

### SCIP Database (Waste Framework Directive)

**Requirement**: Notify ECHA of SVHCs in articles (>0.1% w/w)

**SCIP Information**:
- Article identification
- SVHC name and CAS number
- Concentration range
- Safe use instructions

### REACH Compliance Verification

1. **Supplier Communication**: Request material composition data
2. **SCIP Screening**: Check against SVHC candidate list
3. **Concentration Assessment**: Calculate SVHC concentrations
4. **SCIP Notification**: Submit to ECHA database (if required)
5. **Documentation**: Maintain compliance records

### RoHS/REACH Documentation

| Document | Purpose | Source |
|----------|---------|--------|
| Material Declaration | Substance composition | Supplier |
| Supplier Declaration | Compliance attestation | Supplier |
| Test Reports | Analytical verification | Testing lab |
| SCIP Notification | SVHC disclosure | ECHA |
| Technical File | Compliance evidence | Manufacturer |

### ProtoLabs Environmental Compliance

ProtoLabs maintains compliance with environmental regulations:

| Facility | RoHS | REACH | Environmental Certifications |
|----------|------|-------|-------------------------------|
| North Carolina | ✅ | ✅ | ISO 9001, AS9100D, ISO 13485 |
| Minnesota | ✅ | ✅ | ISO 9001, AS9100D, ISO 13485 |
| New Hampshire | ✅ | ✅ | ISO 9001, AS9100D |
| England (Telford) | ✅ | ✅ | ISO 9001, AS9100D, ISO 14001, ISO 45001 |
| Germany (Putzbrunn) | ✅ | ✅ | ISO 9001, ISO 14001, RoHS, REACH |

**Material Compliance**: ProtoLabs provides material declarations and supplier certifications for environmental compliance upon request.

---

## Production Part Approval Process (PPAP)

### Overview

PPAP is a standardized process in the automotive industry to ensure suppliers meet all customer engineering design record and specification requirements. While primarily an automotive standard, PPAP principles are applicable to aerospace and medical as well.

### PPAP Levels

| Level | Submission Requirements | Application |
|-------|------------------------|-------------|
| Level 1 | Part Submission Warrant (PSW) only | Low risk, mature processes |
| Level 2 | PSW + product samples + limited supporting data | Moderate risk |
| Level 3 | PSW + product samples + complete supporting data | Standard submission |
| Level 4 | PSW + other requirements as defined by customer | Customer-defined |
| Level 5 | PSW + product samples + complete supporting data available for review at supplier | High risk, new processes |

### PPAP Elements

#### 1. Design Records

- Customer engineering drawings
- CAD models (if specified)
- Material specifications
- Design FMEA (if responsible for design)

#### 2. Authorized Engineering Change Documents

- Engineering Change Notices (ECNs)
- Change authorization
- Implementation records

#### 3. Customer Engineering Approval

- Customer sign-off on design
- Engineering trial approval
- Production trial run approval

#### 4. Design FMEA

- Failure Mode and Effects Analysis
- Risk Priority Number (RPN) calculations
- Risk mitigation actions

#### 5. Process Flow Diagram

- Manufacturing process flow
- Process steps and sequence
- Inspection points

#### 6. Process FMEA

- Process failure analysis
- Control methods
- Risk mitigation

#### 7. Control Plan

- Process controls
- Inspection methods
- Reaction plans
- Sample sizes and frequencies

#### 8. Measurement System Analysis (MSA)

- Gage R&R studies
- Bias and linearity studies
- Stability studies
- Calibration records

#### 9. Dimensional Results

- Dimensional inspection results
- Comparison to drawing requirements
- Statistical analysis

#### 10. Records of Material/Performance Test Results

- Material test reports
- Mechanical testing results
- Functional testing results
- Special process certifications

#### 11. Initial Process Studies

- Process capability studies (Ppk/Cpk)
- Statistical process control charts
- Process performance indices

#### 12. Qualified Laboratory Documentation

- Laboratory accreditation (ISO/IEC 17025)
- Laboratory scope of accreditation
- Test method validation

#### 13. Appearance Approval Report (AAR)

- Visual appearance standards
- Color, texture, finish requirements
- Customer approval

#### 14. Sample Production Parts

- Production representative samples
- Number per customer requirements
- Retention samples

#### 15. Master Sample

- Golden sample for comparison
- Signed by customer and supplier
- Retained for production life

#### 16. Checking Aids

- Inspection fixtures
- Gages and tooling
- Calibration records

#### 17. Customer-Specific Requirements

- OEM-specific requirements
- Supplier quality manuals
- Special characteristics

#### 18. Part Submission Warrant (PSW)

- Summary of PPAP submission
- Customer and supplier signatures
- Submission level indication

### PPAP Submission and Approval

| Status | Meaning | Action Required |
|--------|---------|-----------------|
| Approved | Meets all requirements | Proceed to production |
| Interim | Conditional approval | Address issues, limited production |
| Rejected | Does not meet requirements | Correct and resubmit |

### ProtoLabs PPAP Support

ProtoLabs supports automotive customer PPAP requirements:

- **Level 3 PPAP**: Standard submission with complete documentation
- **Dimensional Reports**: CMM inspection reports with statistical analysis
- **Material Certifications**: Mill test reports and material certifications
- **Process Documentation**: Manufacturing process descriptions
- **Test Reports**: Mechanical testing and special process certifications
- **PSW**: Part Submission Warrant completion

**Note**: ProtoLabs does not perform process capability studies (Ppk/Cpk) or MSA studies in-house. These may be provided by the customer or performed in collaboration with ProtoLabs.

---

## Advanced Product Quality Planning (APQP)

### Overview

APQP is a structured method for product and process development in the automotive industry. It ensures that products meet customer requirements and that quality is built into the product from the beginning.

### APQP Phases

#### Phase 1: Planning and Definition

**Inputs**:
- Customer voice (market research, warranty data, field data)
- Business plan and marketing strategy
- Product/process benchmarks
- Product/process assumptions
- Customer requirements

**Outputs**:
- Design goals
- Reliability and quality goals
- Initial material list
- Initial process flow diagram
- Special product characteristics list
- Product assurance plan
- Management support

#### Phase 2: Product Design and Development

**Design Activities**:
- Design FMEA
- Design for manufacturability (DFM)
- Design for assembly (DFA)
- Design verification planning
- Design reviews
- Prototype build control
- Engineering drawings and specifications
- Material specifications
- Drawing and specification changes

**ProtoLabs Role in Phase 2**:
- Rapid prototyping for design verification
- Design for manufacturability feedback
- Material selection guidance
- Process capability input
- Prototype dimensional reports

#### Phase 3: Process Design and Development

**Process Activities**:
- Packaging standards and specifications
- Product/process quality system review
- Process flow diagram
- Floor plan layout
- Characteristics matrix
- Process FMEA
- Pre-launch control plan
- Process instructions
- Measurement system analysis plan
- Initial process capability study plan
- Packaging specifications
- Management support

**ProtoLabs Role in Phase 3**:
- Process flow documentation
- Manufacturing process descriptions
- Control plan input
- Measurement system recommendations
- Process capability data

#### Phase 4: Product and Process Validation

**Validation Activities**:
- Significant production run
- Measurement system evaluation
- Initial process capability study
- Production part approval (PPAP)
- Production validation testing
- Packaging evaluation
- Production control plan
- Quality planning sign-off
- Management support

**ProtoLabs Role in Phase 4**:
- Production part manufacturing
- PPAP documentation (Level 3)
- Dimensional inspection reports
- Material certifications
- Process validation support

#### Phase 5: Feedback, Assessment and Corrective Action

**Ongoing Activities**:
- Reduced variation
- Customer satisfaction
- Delivery and service
- Effective use of lessons learned

### APQP Timing Chart

```
Phase 1    Phase 2    Phase 3    Phase 4    Phase 5
Planning   Product    Process    Product    Feedback
           Design     Design     & Process  & Corrective
                      & Dev      Validation Action

Concept → Design → Prototype → Pilot → Production
Approval   Freeze     Build      Build      Launch

Key Milestones:
├── Phase 1: Project Kickoff, Voice of Customer
├── Phase 2: Design Review, Design Freeze
├── Phase 3: Process Design Review, Control Plan
├── Phase 4: PPAP Approval, Production Launch
└── Phase 5: Continuous Improvement, Lessons Learned
```

### ProtoLabs APQP Integration

ProtoLabs integrates with customer APQP processes:

| APQP Phase | ProtoLabs Activities | Deliverables |
|------------|---------------------|--------------|
| Phase 1 | Feasibility review, capability assessment | Feasibility report |
| Phase 2 | Prototype manufacturing, DFM feedback | Prototypes, DFM report |
| Phase 3 | Process development, control plan input | Process documentation |
| Phase 4 | PPAP production, validation support | PPAP package |
| Phase 5 | Ongoing production, continuous improvement | Production parts |

---

## Failure Mode and Effects Analysis (FMEA)

### Overview

FMEA is a systematic method for identifying potential failure modes in a product or process and assessing their effects. It is a core tool in automotive quality management.

### Types of FMEA

| Type | Timing | Focus | Standard |
|------|--------|-------|----------|
| Design FMEA (DFMEA) | Design phase | Product design | AIAG/VDA FMEA |
| Process FMEA (PFMEA) | Process development | Manufacturing process | AIAG/VDA FMEA |
| Supplemental FMEA | As needed | Software, system | AIAG guidelines |

### AIAG/VDA FMEA Methodology

The AIAG/VDA FMEA Handbook (2019) provides a harmonized approach:

#### 7-Step Approach

1. **Planning and Preparation**: Scope, team, timeline
2. **Structure Analysis**: System, subsystem, component structure
3. **Function Analysis**: Functions, requirements, failure effects
4. **Failure Analysis**: Failure chains (FE, FM, FC)
5. **Risk Analysis**: Current prevention/detection, AP ranking
6. **Optimization**: Risk reduction actions
7. **Results Documentation**: FMEA report

#### Severity (S) Rating

| Rating | Effect on Product | Effect on Process |
|--------|-------------------|-------------------|
| 10 | Safety hazard without warning | May endanger operator |
| 9 | Safety hazard with warning | May endanger operator with warning |
| 8 | Loss of primary function | 100% scrap, line stop |
| 7 | Degradation of primary function | Partial line stop, rework |
| 6 | Loss of secondary function | 100% rework |
| 5 | Degradation of secondary function | Partial rework |
| 4 | Minor defect noticed by customer | Minor rework |
| 3 | Minor defect not noticed | Minor rework |
| 2 | Very minor defect | Very minor rework |
| 1 | No effect | No effect |

#### Occurrence (O) Rating

| Rating | Likelihood | PPM | Cpk |
|--------|------------|-----|-----|
| 10 | Very high | >100,000 | <0.55 |
| 9 | High | 50,000-100,000 | 0.55-0.67 |
| 8 | High | 20,000-50,000 | 0.67-0.83 |
| 7 | Moderate | 10,000-20,000 | 0.83-1.00 |
| 6 | Moderate | 2,000-10,000 | 1.00-1.17 |
| 5 | Low | 500-2,000 | 1.17-1.33 |
| 4 | Low | 100-500 | 1.33-1.50 |
| 3 | Low | 20-100 | 1.50-1.67 |
| 2 | Very low | ≤20 | 1.67-2.00 |
| 1 | Remote | ≤0.1 | >2.00 |

#### Detection (D) Rating

| Rating | Detection Likelihood | Detection Method |
|--------|---------------------|------------------|
| 10 | No detection capability | None |
| 9 | Very remote | Indirect detection only |
| 8 | Remote | Visual detection only |
| 7 | Very low | Double visual inspection |
| 6 | Low | Basic manual inspection |
| 5 | Moderate | Manual inspection with gages |
| 4 | Moderately high | SPC with manual inspection |
| 3 | High | Automated detection |
| 2 | Very high | Automated detection with SPC |
| 1 | Almost certain | Error-proofing (poka-yoke) |

#### Action Priority (AP)

The AIAG/VDA FMEA replaces RPN with Action Priority:

| Priority | Description | Action Required |
|----------|-------------|-----------------|
| H (High) | Team must identify appropriate action to improve prevention and/or detection controls or justify current controls and document rationale | Mandatory action |
| M (Medium) | Team should identify appropriate actions to improve prevention and/or detection controls or justify current controls and document rationale | Recommended action |
| L (Low) | Team could identify actions to improve prevention controls | Low priority |

### ProtoLabs FMEA Support

ProtoLabs supports customer FMEA activities:

1. **DFMEA Input**: Manufacturing feasibility, design for manufacturability feedback
2. **PFMEA Input**: Process capabilities, failure mode data from similar processes
3. **Detection Methods**: Inspection capabilities, measurement systems
4. **Prevention Controls**: Process controls, error-proofing
5. **Risk Reduction**: Process improvements, inspection enhancements

---

## Statistical Process Control (SPC)

### Overview

SPC is a method of quality control using statistical methods to monitor and control manufacturing processes. It is a core requirement in automotive quality management.

### SPC Fundamentals

#### Common Cause vs. Special Cause Variation

| Type | Description | Action |
|------|-------------|--------|
| Common Cause | Inherent process variation | Process improvement |
| Special Cause | Assignable, non-random variation | Immediate corrective action |

#### Process Capability

**Cp (Process Capability Index)**:
$$Cp = \frac{USL - LSL}{6\sigma}$$

**Cpk (Process Capability Index - Centered)**:
$$Cpk = \min\left(\frac{USL - \mu}{3\sigma}, \frac{\mu - LSL}{3\sigma}\right)$$

**Pp (Process Performance Index)**:
$$Pp = \frac{USL - LSL}{6s}$$

**Ppk (Process Performance Index - Centered)**:
$$Ppk = \min\left(\frac{USL - \bar{X}}{3s}, \frac{\bar{X} - LSL}{3s}\right)$$

Where:
- USL = Upper Specification Limit
- LSL = Lower Specification Limit
- μ = Process mean
- σ = Process standard deviation (short-term)
- s = Sample standard deviation (long-term)
- X̄ = Sample mean

#### Capability Interpretation

| Cpk Value | Interpretation | Action |
|-----------|----------------|--------|
| Cpk < 1.0 | Process not capable | Immediate action required |
| 1.0 ≤ Cpk < 1.33 | Process marginally capable | Improvement needed |
| 1.33 ≤ Cpk < 1.67 | Process capable | Monitor and maintain |
| Cpk ≥ 1.67 | Process highly capable | Standard monitoring |

**Automotive Industry Standard**: Cpk ≥ 1.33 for critical characteristics, Cpk ≥ 1.67 for safety-critical characteristics

### Control Charts

#### Variable Data Control Charts

**X̄-R Chart (Average and Range)**:
- Use for: Subgrouped continuous data
- Subgroup size: Typically 2-10
- Application: Dimensional measurements

**X̄-S Chart (Average and Standard Deviation)**:
- Use for: Subgrouped continuous data
- Subgroup size: Typically >10
- Application: Precision measurements

**X-MR Chart (Individuals and Moving Range)**:
- Use for: Individual measurements
- Subgroup size: 1
- Application: Low volume, slow processes

#### Attribute Data Control Charts

**p-Chart (Proportion)**:
- Use for: Proportion defective
- Variable subgroup size
- Application: Pass/fail data

**np-Chart (Number Defective)**:
- Use for: Number of defectives
- Constant subgroup size
- Application: Pass/fail data

**c-Chart (Count)**:
- Use for: Count of defects
- Constant opportunity area
- Application: Defects per unit

**u-Chart (Unit Count)**:
- Use for: Count of defects per unit
- Variable opportunity area
- Application: Defects per unit

### Control Chart Interpretation

#### Western Electric Rules (Control Chart Signals)

| Rule | Pattern | Interpretation |
|------|---------|----------------|
| 1 | Point beyond 3σ | Special cause present |
| 2 | 9 points same side of center line | Shift in process mean |
| 3 | 6 points steadily increasing/decreasing | Trend in process |
| 4 | 14 points alternating up/down | Over-control or sampling issue |
| 5 | 2 of 3 points beyond 2σ | Process shift |
| 6 | 4 of 5 points beyond 1σ | Process shift |
| 7 | 15 points within 1σ | Stratification or reduced variation |
| 8 | 8 points beyond 1σ (both sides) | Bimodal distribution |

### Process Performance Monitoring

#### Key Performance Indicators (KPIs)

| KPI | Formula | Target |
|-----|---------|--------|
| Cp | (USL - LSL) / 6σ | ≥ 1.33 |
| Cpk | min[(USL-μ)/3σ, (μ-LSL)/3σ] | ≥ 1.33 |
| Pp | (USL - LSL) / 6s | ≥ 1.33 |
| Ppk | min[(USL-X̄)/3s, (X̄-LSL)/3s] | ≥ 1.33 |
| PPM | Defective parts per million | < 100 |
| Yield | Good parts / Total parts | > 99% |
| Scrap Rate | Scrap / Total production | < 1% |

### ProtoLabs SPC Capabilities

ProtoLabs implements SPC for critical manufacturing processes:

| Capability | Description |
|------------|-------------|
| Dimensional SPC | Critical dimension monitoring |
| Process Parameter Monitoring | Machine parameter tracking |
| Statistical Sampling | AQL-based sampling plans |
| Capability Studies | Cpk/Ppk analysis |
| Control Charts | X̄-R, X̄-S, p-charts |
| Trend Analysis | Process performance trending |

**Note**: ProtoLabs maintains SPC for manufacturing processes. Customers are responsible for:
- Defining critical characteristics
- Specifying capability requirements
- Reviewing SPC data
- Approving process changes

---

## Measurement System Analysis (MSA)

### Overview

MSA evaluates the measurement system's ability to produce reliable data. It is a critical component of automotive quality management and PPAP requirements.

### MSA Studies

#### 1. Bias Study

**Purpose**: Determine systematic error (difference between measured value and reference value)

**Procedure**:
1. Measure reference standard multiple times
2. Calculate average
3. Bias = Average - Reference value

**Acceptance**: Bias < 10% of tolerance (typically)

#### 2. Linearity Study

**Purpose**: Determine if bias changes across the measurement range

**Procedure**:
1. Measure multiple reference standards across range
2. Calculate bias at each point
3. Perform linear regression

**Acceptance**: Linearity < 10% of tolerance (typically)

#### 3. Stability Study

**Purpose**: Determine if measurement system changes over time

**Procedure**:
1. Measure reference standard over time (e.g., daily for a month)
2. Plot results on control chart
3. Evaluate for special causes

**Acceptance**: Process in statistical control

#### 4. Gage Repeatability and Reproducibility (Gage R&R)

**Purpose**: Quantify measurement system variation

**Components**:
- **Repeatability**: Variation when same operator measures same part multiple times (equipment variation)
- **Reproducibility**: Variation when different operators measure same parts (appraiser variation)

**Study Types**:

| Type | Application | Parts | Operators | Trials |
|------|-------------|-------|-----------|--------|
| Variable (ANOVA) | Continuous data | 10 | 3 | 3 |
| Variable (Range) | Continuous data | 10 | 3 | 3 |
| Attribute | Pass/fail data | 50 | 3 | 3 |
| Destructive | Destructive testing | Special design | 3 | 3 |

**Acceptance Criteria**:

| Metric | Acceptable | Marginal | Unacceptable |
|--------|------------|----------|--------------|
| % GRR (of tolerance) | < 10% | 10-30% | > 30% |
| % GRR (of process variation) | < 10% | 10-30% | > 30% |
| Number of Distinct Categories (ndc) | ≥ 5 | 2-4 | < 2 |
| Attribute Agreement | ≥ 90% | 80-90% | < 80% |

**Gage R&R Interpretation**:

| Component | Acceptable | Action if Unacceptable |
|-------------|------------|------------------------|
| Repeatability | < 10% | Repair/replace gage, improve procedure |
| Reproducibility | < 10% | Train operators, improve procedure |
| Total GRR | < 10% | Improve measurement system |

### Attribute MSA (Attribute Agreement Analysis)

**Purpose**: Evaluate inspection system for pass/fail decisions

**Study Design**:
- 50 parts (including some near specification limits)
- 3 appraisers
- 3 trials per appraiser
- Reference values known for all parts

**Metrics**:

| Metric | Description | Target |
|--------|-------------|--------|
| Within Appraiser | Consistency of each appraiser | ≥ 90% |
| Between Appraisers | Agreement among appraisers | ≥ 90% |
| Each Appraiser vs. Standard | Accuracy of each appraiser | ≥ 90% |
| All Appraisers vs. Standard | Overall system accuracy | ≥ 90% |
| Miss Rate | False accepts (Type II error) | < 2% |
| False Alarm Rate | False rejects (Type I error) | < 5% |

### MSA Best Practices

1. **Measurement System Selection**: Choose appropriate resolution (≤ 10% of tolerance)
2. **Calibration**: Ensure all equipment calibrated and traceable
3. **Standard Selection**: Use certified reference standards
4. **Sample Selection**: Select samples representing process variation
5. **Operator Training**: Ensure operators trained on measurement procedures
6. **Environment Control**: Control temperature, humidity, vibration
7. **Documentation**: Document procedures, results, and actions

### ProtoLabs MSA Capabilities

ProtoLabs maintains calibrated measurement systems and can support customer MSA requirements:

| Equipment | Calibration | MSA Support |
|-----------|-------------|-------------|
| CMM (Coordinate Measuring Machine) | Annual, NIST traceable | Gage R&R studies |
| Optical Comparators | Annual, NIST traceable | Gage R&R studies |
| Height Gages | Annual, NIST traceable | Gage R&R studies |
| Micrometers/Calipers | Annual, NIST traceable | Gage R&R studies |
| Surface Finish Equipment | Annual, NIST traceable | Gage R&R studies |

**Note**: ProtoLabs maintains calibrated measurement equipment. Customers are responsible for:
- Defining critical characteristics requiring MSA
- Specifying MSA requirements (Gage R&R, attribute study, etc.)
- Reviewing and approving MSA results
- Conducting MSA studies (if required beyond ProtoLabs scope)

---

## Control Plans

### Overview

A Control Plan is a written description of the system for controlling parts and processes. It is a key deliverable in APQP and required for PPAP.

### Control Plan Structure

| Section | Content |
|---------|---------|
| Header | Part number, revision, customer, supplier, date |
| Contact Information | Team members, phone numbers |
| Part/Process Description | Description of part and process steps |
| Machine/Tooling | Equipment, fixtures, tooling |
| Characteristics | Product and process characteristics |
| Methods | Evaluation/measurement technique |
| Reaction Plan | Actions for out-of-control conditions |

### Characteristics Classification

| Classification | Symbol | Description | Control Method |
|----------------|--------|-------------|----------------|
| Critical | [CC] | Affects safety or compliance | 100% inspection, SPC |
| Significant | [SC] | Affects function or fit | SPC, sampling |
| Major | [M] | Affects appearance or minor function | Sampling |
| Minor | [m] | Minimal impact | Audit |
| Critical to Quality | [CTQ] | Customer-defined critical | Per customer requirements |

### Control Methods

| Method | Description | Application |
|--------|-------------|-------------|
| X̄-R Chart | Average and range control chart | Variable data, high volume |
| X̄-S Chart | Average and standard deviation | Variable data, high precision |
| X-MR Chart | Individuals and moving range | Variable data, low volume |
| p-Chart | Proportion defective | Attribute data, variable n |
| np-Chart | Number defective | Attribute data, constant n |
| c-Chart | Count of defects | Defects per unit, constant area |
| u-Chart | Unit count of defects | Defects per unit, variable area |
| Check Sheet | Data collection form | Manual data collection |
| Poka-Yoke | Error-proofing | Prevention of defects |
| Automated Inspection | Machine vision, sensors | 100% inspection |

### Reaction Plan

The Control Plan must include a reaction plan for out-of-control conditions:

| Condition | Action | Responsibility |
|-----------|--------|----------------|
| Out-of-control point | Stop production, quarantine product | Operator |
| Out-of-specification | 100% sort, root cause analysis | Quality |
| Trending | Preventive action, process adjustment | Engineering |
| Measurement error | Recalibrate, re-inspect | Quality |

### Control Plan Types

| Type | Timing | Purpose |
|------|--------|---------|
| Prototype | Development | Control during prototyping |
| Pre-Launch | Pilot production | Control during ramp-up |
| Production | Full production | Ongoing production control |

### ProtoLabs Control Plan Support

ProtoLabs supports customer Control Plan requirements:

| Element | ProtoLabs Capability |
|---------|---------------------|
| Process Flow | Documented manufacturing processes |
| Characteristics | Critical dimension identification |
| Measurement Methods | CMM, optical inspection, gages |
| Sample Size | Per customer requirements |
| Frequency | Per customer requirements |
| Control Method | SPC, 100% inspection, sampling |
| Reaction Plan | Non-conforming product procedures |

---

## Measurement System Analysis (MSA)

### Overview

MSA evaluates the measurement system's ability to produce reliable data. It is a core tool in automotive quality management and required for PPAP.

### MSA Studies

#### 1. Bias Study

**Purpose**: Determine systematic error

**Procedure**:
1. Measure reference standard multiple times
2. Calculate average
3. Bias = Average - Reference value

**Acceptance**: Bias < 10% of tolerance

#### 2. Linearity Study

**Purpose**: Determine if bias changes across measurement range

**Procedure**:
1. Measure multiple reference standards across range
2. Calculate bias at each point
3. Perform linear regression

**Acceptance**: Linearity < 10% of tolerance

#### 3. Stability Study

**Purpose**: Determine if measurement system changes over time

**Procedure**:
1. Measure reference standard over time
2. Plot results on control chart
3. Evaluate for special causes

**Acceptance**: Process in statistical control

#### 4. Gage Repeatability and Reproducibility (Gage R&R)

**Purpose**: Quantify measurement system variation

**Study Design**:
- 10 parts
- 3 appraisers
- 3 trials per appraiser

**Metrics**:

| Metric | Formula | Acceptable |
|--------|---------|------------|
| % Repeatability | (Equipment Variation / Tolerance) × 100 | < 10% |
| % Reproducibility | (Appraiser Variation / Tolerance) × 100 | < 10% |
| % GRR | (Total GRR / Tolerance) × 100 | < 10% |
| ndc | Number of distinct categories | ≥ 5 |

**Acceptance Criteria**:

| % GRR | Decision | Action |
|-------|----------|--------|
| < 10% | Acceptable | No action required |
| 10-30% | Marginal | Evaluate for improvement |
| > 30% | Unacceptable | Improvement required |

### Attribute MSA (Attribute Agreement Analysis)

**Purpose**: Evaluate inspection system for pass/fail decisions

**Study Design**:
- 50 parts (including some near specification limits)
- 3 appraisers
- 3 trials per appraiser
- Reference values known

**Metrics**:

| Metric | Target |
|--------|--------|
| Within Appraiser | ≥ 90% |
| Between Appraisers | ≥ 90% |
| Each Appraiser vs. Standard | ≥ 90% |
| All Appraisers vs. Standard | ≥ 90% |
| Miss Rate | < 2% |
| False Alarm Rate | < 5% |

### MSA Best Practices

1. **Measurement System Selection**: Choose appropriate resolution (≤ 10% of tolerance)
2. **Calibration**: Ensure all equipment calibrated and traceable
3. **Standard Selection**: Use certified reference standards
4. **Sample Selection**: Select samples representing process variation
5. **Operator Training**: Ensure operators trained on measurement procedures
6. **Environment Control**: Control temperature, humidity, vibration
7. **Documentation**: Document procedures, results, and actions

### ProtoLabs MSA Capabilities

ProtoLabs maintains calibrated measurement systems:

| Equipment | Calibration | MSA Support |
|-----------|-------------|-------------|
| CMM | Annual, NIST traceable | Gage R&R studies |
| Optical Comparators | Annual, NIST traceable | Gage R&R studies |
| Height Gages | Annual, NIST traceable | Gage R&R studies |
| Micrometers/Calipers | Annual, NIST traceable | Gage R&R studies |
| Surface Finish Equipment | Annual, NIST traceable | Gage R&R studies |

---

## Tier Supplier Requirements

### Overview

Automotive OEMs have specific requirements for tier suppliers. Understanding these requirements is essential for successful supplier relationships.

### Tier Structure

```
┌─────────────────────────────────────────────────────────────┐
│                    OEM (Tier 0)                               │
│         (Vehicle Manufacturer)                              │
│    GM, Ford, Stellantis, VW, Toyota, etc.                    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Tier 1 Suppliers                           │
│         (Direct OEM Suppliers)                              │
│    Bosch, Continental, Denso, Magna, etc.                    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Tier 2 Suppliers                         │
│         (Component Suppliers)                               │
│    ProtoLabs, Material Suppliers, Subcontractors            │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Tier 3+ Suppliers                        │
│         (Raw Material Suppliers)                            │
│    Metal Suppliers, Chemical Suppliers, etc.                │
└─────────────────────────────────────────────────────────────┘
```

### Tier Supplier Requirements

#### General Requirements

| Requirement | Description | Documentation |
|-------------|-------------|---------------|
| Quality System | ISO 9001 minimum, IATF 16949 preferred | Certificate |
| Financial Stability | Demonstrated financial health | Financial statements |
| Capacity | Ability to meet volume requirements | Capacity analysis |
| Technical Capability | Engineering and manufacturing capability | Capability studies |
| Traceability | Lot and serial number tracking | Traceability system |
| Change Control | Formal change notification process | Change procedure |
| Problem Solving | 8D or equivalent problem solving | 8D reports |
| Continuous Improvement | Demonstrated improvement activities | Improvement records |

#### Quality-Specific Requirements

| Requirement | Description | Typical Expectation |
|-------------|-------------|---------------------|
| APQP | Advanced Product Quality Planning | Full APQP for new parts |
| PPAP | Production Part Approval Process | Level 3 standard |
| FMEA | Failure Mode and Effects Analysis | DFMEA and PFMEA |
| Control Plans | Process control documentation | Approved control plan |
| MSA | Measurement System Analysis | GRR < 10% |
| SPC | Statistical Process Control | Cpk ≥ 1.33 |
| 8D Problem Solving | Corrective action methodology | 8D for significant issues |
| Layered Process Audits | Manufacturing audits | Weekly LPA |

#### Documentation Requirements

| Document | Purpose | Retention |
|----------|---------|-----------|
| Quality Agreement | Define quality responsibilities | Duration of relationship |
| Supplier Manual | OEM-specific requirements | Current version |
| PPAP Package | Production approval | Life + 15 years |
| APQP Records | Development records | Life + 15 years |
| FMEA | Risk analysis | Life + 15 years |
| Control Plan | Process control | Current version |
| MSA Studies | Measurement validation | Annual or change |
| SPC Records | Process monitoring | 2 years |
| Audit Records | Supplier audits | 3 years |
| CAPA Records | Corrective actions | 5 years |
| Change Records | Change notifications | Life + 15 years |

### ProtoLabs Tier Supplier Capabilities

ProtoLabs operates as a Tier 2 supplier to automotive and EV manufacturers:

| Capability | Status | Notes |
|------------|--------|-------|
| ISO 9001:2015 | ✅ Certified | All facilities |
| IATF 16949 | ⚠️ Customer-specific | ISO 9001 + automotive practices |
| PPAP | ✅ Level 3 | Full documentation package |
| APQP | ✅ Supported | Collaboration with customer |
| FMEA | ✅ Supported | DFMEA and PFMEA input |
| Control Plans | ✅ Supported | Customer-specific plans |
| MSA | ✅ Supported | Gage R&R studies |
| SPC | ✅ Supported | Critical characteristics |
| 8D Problem Solving | ✅ Supported | Corrective action reports |
| Traceability | ✅ Supported | Lot and serial tracking |
| Change Control | ✅ Supported | Formal change notification |

---

## OEM-Specific Standards

### Overview

Major automotive OEMs have specific quality requirements beyond IATF 16949. Understanding these requirements is essential for supplier qualification.

### General Motors (GM)

| Standard/Requirement | Description |
|---------------------|-------------|
| GM 1927 | Quality System Requirements |
| GM 1927-1 | PPAP Requirements |
| GM 1927-2 | APQP Requirements |
| GM 1927-3 | Control Plan Requirements |
| GM 1927-4 | FMEA Requirements |
| GM 1927-5 | MSA Requirements |
| GM 1927-6 | SPC Requirements |
| GM 1927-7 | Problem Solving Requirements |
| GM 1927-8 | Layered Process Audits |
| GM 1927-9 | Supplier Development |
| GM 1927-10 | Supplier Assessment |
| GM 1927-11 | Supplier Quality Manual |
| GM 1927-12 | Supplier Requirements |
| GM 1927-13 | Supplier Performance |
| GM 1927-14 | Supplier Improvement |
| GM 1927-15 | Supplier Corrective Action |
| GM 1927-16 | Supplier Containment |
| GM 1927-17 | Supplier Notification |
| GM 1927-18 | Supplier Change Management |
| GM 1927-19 | Supplier Documentation |
| GM 1927-20 | Supplier Records |

**Key GM Requirements**:
- Cpk ≥ 1.67 for critical characteristics
- Cpk ≥ 1.33 for significant characteristics
- GRR < 10% for critical measurements
- Layered Process Audits (LPA) weekly
- Annual self-assessment per GM 1927

### Ford Motor Company

| Standard/Requirement | Description |
|---------------------|-------------|
| Ford Q1 | Quality System Requirements |
| Ford Q1-1 | PPAP Requirements |
| Ford Q1-2 | APQP Requirements |
| Ford Q1-3 | Control Plan Requirements |
| Ford Q1-4 | FMEA Requirements |
| Ford Q1-5 | MSA Requirements |
| Ford Q1-6 | SPC Requirements |
| Ford Q1-7 | Problem Solving Requirements |
| Ford Q1-8 | Layered Process Audits |
| Ford Q1-9 | Supplier Development |
| Ford Q1-10 | Supplier Assessment |
| Ford Q1-11 | Supplier Quality Manual |
| Ford Q1-12 | Supplier Requirements |
| Ford Q1-13 | Supplier Performance |
| Ford Q1-14 | Supplier Improvement |
| Ford Q1-15 | Supplier Corrective Action |
| Ford Q1-16 | Supplier Containment |
| Ford Q1-17 | Supplier Notification |
| Ford Q1-18 | Supplier Change Management |
| Ford Q1-19 | Supplier Documentation |
| Ford Q1-20 | Supplier Records |

**Key Ford Requirements**:
- Q1 Supplier status required for new business
- Cpk ≥ 1.67 for critical characteristics
- Cpk ≥ 1.33 for significant characteristics
- GRR < 10% for critical measurements
- 8D problem solving for significant issues
- Annual Q1 assessment

### Stellantis (Formerly FCA)

| Standard/Requirement | Description |
|---------------------|-------------|
| Stellantis SQ.00001 | Supplier Quality Requirements |
| Stellantis SQ.00002 | PPAP Requirements |
| Stellantis SQ.00003 | APQP Requirements |
| Stellantis SQ.00004 | Control Plan Requirements |
| Stellantis SQ.00005 | FMEA Requirements |
| Stellantis SQ.00006 | MSA Requirements |
| Stellantis SQ.00007 | SPC Requirements |
| Stellantis SQ.00008 | Problem Solving Requirements |
| Stellantis SQ.00009 | Layered Process Audits |
| Stellantis SQ.00010 | Supplier Development |
| Stellantis SQ.00011 | Supplier Assessment |
| Stellantis SQ.00012 | Supplier Quality Manual |
| Stellantis SQ.00013 | Supplier Requirements |
| Stellantis SQ.00014 | Supplier Performance |
| Stellantis SQ.00015 | Supplier Improvement |
| Stellantis SQ.00016 | Supplier Corrective Action |
| Stellantis SQ.00017 | Supplier Containment |
| Stellantis SQ.00018 | Supplier Notification |
| Stellantis SQ.00019 | Supplier Change Management |
| Stellantis SQ.00020 | Supplier Documentation |

**Key Stellantis Requirements**:
- Cpk ≥ 1.67 for critical characteristics
- Cpk ≥ 1.33 for significant characteristics
- GRR < 10% for critical measurements
- 8D problem solving for significant issues
- Annual supplier assessment

### Volkswagen Group

| Standard/Requirement | Description |
|---------------------|-------------|
| Volkswagen Formel Q | Quality Capability Requirements |
| Volkswagen Formel Q-1 | Quality Planning |
| Volkswagen Formel Q-2 | Quality Assurance in Production |
| Volkswagen Formel Q-3 | Quality Assurance in Logistics |
| Volkswagen Formel Q-4 | Quality Assurance in Development |
| Volkswagen Formel Q-5 | Supplier Management |
| Volkswagen Formel Q-6 | Quality Agreements |
| Volkswagen Formel Q-7 | Quality Audits |
| Volkswagen Formel Q-8 | Quality Improvement |
| Volkswagen Formel Q-9 | Quality Costs |
| Volkswagen Formel Q-10 | Quality Training |
| Volkswagen Formel Q-11 | Quality Documentation |
| Volkswagen Formel Q-12 | Quality Records |
| Volkswagen Formel Q-13 | Quality Planning |
| Volkswagen Formel Q-14 | Quality Assurance |
| Volkswagen Formel Q-15 | Quality Control |
| Volkswagen Formel Q-16 | Quality Improvement |
| Volkswagen Formel Q-17 | Quality Audits |
| Volkswagen Formel Q-18 | Quality Training |
| Volkswagen Formel Q-19 | Quality Documentation |
| Volkswagen Formel Q-20 | Quality Records |

**Key Volkswagen Requirements**:
- Formel Q capability assessment
- D/TLD (archive) documentation for critical parts
- Cpk ≥ 1.67 for critical characteristics
- Cpk ≥ 1.33 for significant characteristics
- GRR < 10% for critical measurements
- 8D problem solving for significant issues
- Annual Formel Q assessment

### Toyota

| Standard/Requirement | Description |
|---------------------|-------------|
| Toyota SQ (Supplier Quality) | Supplier Quality Requirements |
| Toyota SQ-1 | Quality Planning |
| Toyota SQ-2 | Quality Assurance |
| Toyota SQ-3 | Quality Control |
| Toyota SQ-4 | Quality Improvement |
| Toyota SQ-5 | Supplier Development |
| Toyota SQ-6 | Supplier Assessment |
| Toyota SQ-7 | Supplier Quality Manual |
| Toyota SQ-8 | Supplier Requirements |
| Toyota SQ-9 | Supplier Performance |
| Toyota SQ-10 | Supplier Improvement |
| Toyota SQ-11 | Supplier Corrective Action |
| Toyota SQ-12 | Supplier Containment |
| Toyota SQ-13 | Supplier Notification |
| Toyota SQ-14 | Supplier Change Management |
| Toyota SQ-15 | Supplier Documentation |
| Toyota SQ-16 | Supplier Records |
| Toyota SQ-17 | Supplier Audits |
| Toyota SQ-18 | Supplier Training |
| Toyota SQ-19 | Supplier Certification |
| Toyota SQ-20 | Supplier Recognition |

**Key Toyota Requirements**:
- Toyota Production System (TPS) alignment
- Jidoka (autonomation) principles
- Poka-yoke (error-proofing)
- Heijunka (level production)
- Genchi Genbutsu (go see)
- Kaizen (continuous improvement)
- Cpk ≥ 1.67 for critical characteristics
- Cpk ≥ 1.33 for significant characteristics
- GRR < 10% for critical measurements
- 5-Why problem solving for issues
- Annual supplier assessment

### ProtoLabs OEM Support

ProtoLabs supports automotive OEM requirements:

| OEM | Support Level | Key Deliverables |
|-----|---------------|------------------|
| General Motors | Full | PPAP Level 3, Control Plans, SPC |
| Ford | Full | PPAP Level 3, Q1 requirements |
| Stellantis | Full | PPAP Level 3, SQ.00001 compliance |
| Volkswagen | Full | Formel Q, D/TLD documentation |
| BMW | Full | QSB requirements, PPAP Level 3 |
| Mercedes | Full | MQAS requirements, PPAP Level 3 |
| Toyota | Full | TPS alignment, PPAP Level 3 |
| Honda | Full | SQ requirements, PPAP Level 3 |

---

## Facility Certification Matrix for Automotive

### United States Facilities

#### North Carolina (Morrisville) - 3D Printing
| Certification | Scope | Status | Automotive Relevance |
|--------------|-------|--------|----------------------|
| ISO 9001:2015 | All Plastic 3D Printing | ✅ Active | Base QMS |
| AS9100D | DMLS, SLS, MJF 3D Printing | ✅ Active | Aerospace crossover |
| ISO 13485:2016 | DMLS 3D Printing | ✅ Active | Medical crossover |
| ITAR Registered | DMLS 3D Printing | ✅ Active | Defense crossover |

#### Minnesota (Plymouth/Rosemount) - Injection Molding & CNC
| Certification | Scope | Status | Automotive Relevance |
|--------------|-------|--------|----------------------|
| ISO 9001:2015 | Injection Molding, CNC | ✅ Active | Base QMS |
| AS9100D | CNC Machining | ✅ Active | Aerospace crossover |
| ISO 13485:2016 | Injection Molding | ✅ Active | Medical crossover |
| ITAR Registered | CNC Machining, Molding | ✅ Active | Defense crossover |

#### New Hampshire (Nashua) - Sheet Metal & CNC
| Certification | Scope | Status | Automotive Relevance |
|--------------|-------|--------|----------------------|
| ISO 9001:2015 | Sheet Metal, CNC | ✅ Active | Base QMS |
| AS9100D | CNC Machining | ✅ Active | Aerospace crossover |

### European Facilities

#### England (Telford)
| Certification | Scope | Status | Automotive Relevance |
|--------------|-------|--------|----------------------|
| ISO 9001:2015 | Injection Molding, CNC | ✅ Active | Base QMS |
| AS9100D | CNC Machining | ✅ Active | Aerospace crossover |
| ISO 14001:2015 | Environmental | ✅ Active | Sustainability |
| ISO 45001:2018 | Safety | ✅ Active | Worker safety |
| JOSCAR | Defense Supply Chain | ✅ Active | UK defense |
| Cyber Essentials | Cybersecurity | ✅ Active | Data protection |

#### Germany (Putzbrunn)
| Certification | Scope | Status | Automotive Relevance |
|--------------|-------|--------|----------------------|
| ISO 9001:2015 | 3D Printing | ✅ Active | Base QMS |
| ISO 14001:2015 | Environmental | ✅ Active | Sustainability |
| RoHS & REACH | Environmental | ✅ Active | EU compliance |

---

## Documentation Requirements for Automotive Parts

### Overview

Automotive documentation requirements ensure traceability, quality, and compliance throughout the supply chain. ProtoLabs provides comprehensive documentation to support automotive customer requirements.

### PPAP Documentation Requirements

See [PPAP Section](#production-part-approval-process-ppap) for detailed PPAP documentation requirements.

### Core Tool Documentation

#### APQP Documentation

| Document | Timing | Retention |
|----------|--------|-----------|
| APQP Timing Chart | Planning | Project file |
| Design Reviews | Design phase | 15 years |
| Process Flow Diagram | Process design | 15 years |
| Floor Plan Layout | Process design | 15 years |
| Characteristics Matrix | Process design | 15 years |
| Management Reviews | Ongoing | 3 years |

#### FMEA Documentation

| Document | Timing | Retention |
|----------|--------|-----------|
| Design FMEA | Design phase | 15 years |
| Process FMEA | Process design | 15 years |
| FMEA Updates | As needed | 15 years |
| Risk Reduction Actions | Ongoing | 15 years |

#### Control Plan Documentation

| Document | Timing | Retention |
|----------|--------|-----------|
| Prototype Control Plan | Prototype | Project file |
| Pre-Launch Control Plan | Pilot | 15 years |
| Production Control Plan | Production | Current + 15 years |
| Control Plan Updates | As needed | 15 years |

#### MSA Documentation

| Document | Timing | Retention |
|----------|--------|-----------|
| MSA Plan | Planning | Project file |
| Gage R&R Studies | Validation | 15 years |
| Attribute Studies | Validation | 15 years |
| Bias/Linearity Studies | Validation | 15 years |
| Calibration Records | Ongoing | Life + 2 years |

#### SPC Documentation

| Document | Timing | Retention |
|----------|--------|-----------|
| SPC Plan | Planning | Project file |
| Control Charts | Ongoing | 2 years |
| Process Capability Studies | Validation | 15 years |
| Process Performance Studies | Ongoing | 2 years |
| Out-of-Control Action Plans | Ongoing | Current |

### Quality Records Retention

| Record Type | Retention Period | Reference |
|-------------|------------------|-----------|
| PPAP Records | 15 years | Customer requirement |
| APQP Records | 15 years | Customer requirement |
| FMEA Records | 15 years | Customer requirement |
| Control Plans | Current + 15 years | Customer requirement |
| MSA Records | 15 years | Customer requirement |
| SPC Records | 2 years | IATF 16949 |
| Calibration Records | Life + 2 years | IATF 16949 |
| Internal Audit Records | 3 years | IATF 16949 |
| Management Review Records | 3 years | IATF 16949 |
| Training Records | Current + 3 years | IATF 16949 |
| Nonconforming Product Records | 3 years | IATF 16949 |
| CAPA Records | 3 years | IATF 16949 |
| Customer Complaint Records | 3 years | IATF 16949 |
| Supplier Records | Current + 3 years | IATF 16949 |
| Traceability Records | 15 years | Customer requirement |
| Change Control Records | Life + 15 years | Customer requirement |

### Electronic Records

For electronic records maintained per 21 CFR Part 11 or equivalent:

| Requirement | Implementation |
|-------------|----------------|
| Validation | System validation documentation |
| Audit Trails | Secure, computer-generated timestamps |
| Access Controls | Unique user IDs, password protection |
| Authority Checks | Role-based access permissions |
| Device Checks | Workstation validation |
| Documentation Controls | Version control, change management |
| Signature Manifestations | Printed name, date, meaning |
| Signature/Record Linking | Binding of signatures to records |

### ProtoLabs Documentation Services

ProtoLabs provides comprehensive documentation for automotive customers:

| Service | Description |
|---------|-------------|
| PPAP Level 3 | Complete PPAP documentation package |
| Dimensional Reports | CMM inspection with statistical analysis |
| Material Certifications | Mill test reports, material specs |
| Process Documentation | Manufacturing process descriptions |
| Test Reports | Mechanical testing, special processes |
| Control Plans | Customer-specific control plans |
| FMEA Support | DFMEA and PFMEA input |
| MSA Studies | Gage R&R documentation |
| SPC Data | Process capability studies |
| Certificates of Conformance | Compliance declarations |
| Traceability Records | Lot tracking documentation |
| Change Notifications | Formal change communication |

---

## Cross-References

- See [regulatory-framework.md](../compliance/regulatory-framework.md) for general compliance overview
- See [reducing-automotive-weight.md](./reducing-automotive-weight.md) for automotive manufacturing capabilities
- See [ev-future.md](./ev-future.md) for EV-specific manufacturing
- See [aerospace-compliance.md](./aerospace-compliance.md) for aerospace compliance
- See [medical-compliance.md](./medical-compliance.md) for medical device compliance
