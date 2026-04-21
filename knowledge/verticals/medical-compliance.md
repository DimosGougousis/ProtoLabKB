---
type: knowledge-article
category: compliance
source_url: https://www.protolabs.com/resources/guides-and-trend-reports/prototyping-and-low-volume-production-for-medical-applications/
fetched_at: 2026-04-21
summary: Medical device manufacturing compliance including FDA 21 CFR 820, ISO 13485, EU MDR, UDI requirements, biocompatibility standards (ISO 10993), and sterilization validation for 3D printed and machined medical components.
---

# Medical Device Compliance Requirements

## Overview

Medical device manufacturing requires strict adherence to regulatory requirements to ensure patient safety and product efficacy. ProtoLabs maintains comprehensive quality management systems and certifications to support medical device development from prototyping through production.

---

## FDA 21 CFR 820 Quality System Regulation

### Overview

The FDA's Quality System Regulation (QSR) under 21 CFR Part 820 establishes requirements for medical device design, manufacturing, and distribution. All medical devices marketed in the United States must comply with these regulations.

### Key Subparts

| Subpart | Title | Key Requirements |
|---------|-------|------------------|
| A | General Provisions | Scope, definitions, quality system |
| B | Quality System Requirements | Management responsibility, quality audit |
| C | Design Controls | Design planning, inputs, outputs, review, verification, validation, transfer, changes, history file |
| D | Document Controls | Document approval, distribution, changes |
| E | Purchasing Controls | Supplier evaluation, purchasing data |
| F | Identification and Traceability | Device identification, traceability |
| G | Production and Process Controls | Process validation, personnel, contamination, buildings, equipment, manufacturing material |
| H | Acceptance Activities | Receiving, in-process, finished device acceptance |
| I | Nonconforming Product | Control, review, disposition |
| J | Corrective and Preventive Action | CAPA procedures, complaint handling |
| K | Labeling and Packaging Control | Label integrity, inspection, storage |
| L | Handling, Storage, Distribution | Procedures, stock rotation, distribution |
| M | Records | General requirements, device master record, device history record, complaint files |
| N | Servicing | Service procedures, reports |
| O | Statistical Techniques | Statistical process control, sampling plans |

### Design Controls (Subpart C)

Design controls are critical for medical device development:

1. **Design Planning**: Project plan with milestones and responsibilities
2. **Design Inputs**: User needs, intended use, regulatory requirements
3. **Design Outputs**: Specifications, drawings, manufacturing procedures
4. **Design Review**: Formal reviews at key milestones
5. **Design Verification**: Objective evidence that outputs meet inputs
6. **Design Validation**: Evidence that device meets user needs and intended use
7. **Design Transfer**: Transition to production
8. **Design Changes**: Controlled change process
9. **Design History File (DHF)**: Compilation of all design records

### Device Master Record (DMR) Requirements

Per 21 CFR 820.181, the DMR must include:

1. Device specifications
2. Production process specifications
3. Quality assurance procedures and specifications
4. Packaging and labeling specifications
5. Installation, maintenance, and servicing procedures

### Device History Record (DHR) Requirements

Per 21 CFR 820.184, the DHR must include:

1. Manufacturing dates
2. Quantity manufactured
3. Quantity released for distribution
4. Acceptance records
5. Primary identification label and labeling
6. Device serial number or control number
7. Production records
8. Traceability records

---

## ISO 13485:2016 Medical Device Quality Management

### Overview

ISO 13485:2016 is the international standard for quality management systems specific to the medical device industry. It provides a framework for organizations to establish, implement, and maintain a quality management system.

### Key Differences from ISO 9001

| Aspect | ISO 13485:2016 | ISO 9001:2015 |
|--------|----------------|---------------|
| Primary focus | Medical device safety and efficacy | Customer satisfaction |
| Risk management | Required throughout QMS | Risk-based thinking |
| Regulatory requirements | Explicit requirements | Not addressed |
| Documentation | More prescriptive | Less prescriptive |
| Validation | Required for processes | Not required |
| Traceability | Required for all devices | Not required |
| Post-market surveillance | Required | Not required |

### Key Clauses

| Clause | Title | Key Requirements |
|--------|-------|------------------|
| 4 | Quality Management System | Documentation, quality manual, control of documents and records |
| 5 | Management Responsibility | Management commitment, customer focus, quality policy, planning, responsibility/authority, management review |
| 6 | Resource Management | Provision of resources, human resources, infrastructure, work environment, contamination control |
| 7 | Product Realization | Planning, customer-related processes, design/development, purchasing, production/service provision, control of monitoring/measuring equipment |
| 8 | Measurement, Analysis and Improvement | General, monitoring/measurement, control of nonconforming product, analysis of data, improvement |

### Risk Management Integration

ISO 13485 requires risk management throughout the quality management system:

- **Design and Development**: Risk analysis per ISO 14971
- **Production Processes**: Risk-based process validation
- **Post-Market Surveillance**: Risk monitoring and feedback
- **CAPA**: Risk-based corrective and preventive actions

### ProtoLabs ISO 13485 Certification

| Facility | Scope | Certification |
|----------|-------|---------------|
| North Carolina (Morrisville) | DMLS 3D Printing | ISO 13485:2016 |
| Minnesota (Plymouth/Rosemount) | Injection Molding | ISO 13485:2016 |

---

## EU MDR (Medical Device Regulation 2017/745)

### Overview

The EU Medical Device Regulation (MDR) 2017/745 replaced the Medical Device Directive (MDD) 93/42/EEC and became fully applicable in May 2021. It establishes stricter requirements for medical devices placed on the European market.

### Key Changes from MDD

| Aspect | MDR 2017/745 | MDD 93/42/EEC |
|--------|--------------|---------------|
| Scope | Broader, includes aesthetic devices | Narrower scope |
| Classification | Stricter classification rules | Less stringent |
| Clinical evidence | More rigorous requirements | Less stringent |
| Post-market surveillance | Enhanced requirements | Basic vigilance |
| UDI | Mandatory | Not required |
| Notified Bodies | Stricter designation | Less stringent |
| Person Responsible | Required | Not required |

### Device Classification

MDR establishes four risk classes based on intended use and duration:

| Class | Risk Level | Examples | Conformity Route |
|-------|------------|----------|------------------|
| Class I | Low | Non-invasive devices, stethoscopes | Self-declaration |
| Class IIa | Low-Medium | Short-term invasive devices | Notified Body |
| Class IIb | Medium-High | Long-term invasive, active devices | Notified Body |
| Class III | High | Implantable, life-supporting | Notified Body + Clinical |

### General Safety and Performance Requirements (GSPRs)

Annex I of MDR establishes GSPRs covering:

1. **General Requirements** (Ch. I)
   - Risk management
   - Safety principles
   - Performance characteristics
   - Lifetime and shelf life

2. **Requirements Regarding Design and Manufacture** (Ch. II)
   - Chemical/physical/biological properties
   - Infection and microbial contamination
   - Construction and environmental properties
   - Devices with measuring function
   - Protection against radiation
   - Electronic programmable systems
   - Active devices and connected devices
   - Particular requirements for implants

3. **Information Supplied by the Manufacturer** (Ch. III)
   - Labeling requirements
   - Instructions for use
   - Technical documentation

### Economic Operators

MDR defines four economic operators with specific obligations:

| Operator | Role | Key Obligations |
|----------|------|-----------------|
| Manufacturer | Produces/devices | CE marking, technical documentation, UDI, vigilance |
| Authorized Representative | EU representative for non-EU manufacturers | Legal representative in EU, documentation access |
| Importer | Imports into EU | Verification of compliance, labeling check |
| Distributor | Makes available in EU | Storage, transport, traceability |

### ProtoLabs EU MDR Support

ProtoLabs supports EU MDR compliance through:

1. **Technical Documentation Support**: Providing material and process documentation
2. **Quality Agreements**: Defining responsibilities between parties
3. **Change Control**: Formal process for design and process changes
4. **Traceability**: Lot tracking and serialization capabilities
5. **Post-Market Surveillance**: Support for vigilance reporting

---

## UDI (Unique Device Identification) Requirements

### Overview

UDI is a system to identify medical devices through their distribution and use, required by FDA (21 CFR 830) and EU MDR.

### UDI Components

| Component | Description | Example |
|-----------|-------------|---------|
| UDI-DI | Device identifier (static) | Model/version |
| UDI-PI | Production identifier (dynamic) | Lot, serial, expiry, MFG date |
| AIDC | Automatic identification | Barcode, RFID |
| HRI | Human readable interpretation | Plain text |

### UDI Carrier Requirements

| Packaging Level | UDI Carrier Required | Location |
|-----------------|----------------------|----------|
| Device itself | If device is reusable and >5cm | On device |
| Immediate packaging | Always | On package |
| Higher packaging | Always | On package |
| Shipping container | Optional | On package |

### FDA UDI Database (GUDID)

- **Requirement**: Submit UDI-DI to GUDID
- **Timeline**: Before commercial distribution
- **Updates**: Within 30 days of changes
- **Exceptions**: Class I devices exempt from UDI-PI

### EU UDI Database (EUDAMED)

- **Actor Registration**: Required for all economic operators
- **UDI/Devices Registration**: UDI-DI and UDI-PI data
- **Notified Bodies and Certificates**: Certificate data
- **Clinical Investigations**: Investigation data
- **Vigilance and Post-Market Surveillance**: Incident reports

### ProtoLabs UDI Support

ProtoLabs supports UDI implementation through:

1. **Serialization**: Part serialization capabilities for UDI-PI
2. **Lot Tracking**: Comprehensive lot traceability
3. **Labeling**: Custom labeling with UDI barcodes
4. **Data Exchange**: Electronic data interchange capabilities
5. **Documentation**: Certificates of conformance with UDI data

---

## Biocompatibility Standards Reminder

### Overview

Biocompatibility is critical for medical devices that contact the human body. ProtoLabs provides materials and processes that support biocompatibility requirements.

### ISO 10993 Series

The ISO 10993 series provides standards for biological evaluation of medical devices:

| Standard | Title | Application |
|----------|-------|-------------|
| ISO 10993-1 | Evaluation and testing within a risk management process | Framework for biological evaluation |
| ISO 10993-5 | Tests for in vitro cytotoxicity | Cell culture testing |
| ISO 10993-6 | Tests for local effects after implantation | Implantation studies |
| ISO 10993-10 | Tests for irritation and skin sensitization | Skin contact devices |
| ISO 10993-11 | Tests for systemic toxicity | Systemic exposure |
| ISO 10993-18 | Chemical characterization of materials | Material analysis |

### USP Class VI Testing

USP Class VI is a standard for biological reactivity testing of plastics:

| Class | Description | Application |
|-------|-------------|-------------|
| Class I | 3 extracts, intravenous | Limited exposure |
| Class II | 3 extracts, intracutaneous | External devices |
| Class III | 3 extracts, implant | Short-term implant |
| Class IV | 6 extracts, all routes | Extended exposure |
| Class V | 12 extracts, all routes | Permanent implant |
| Class VI | 50°C complete, all routes | Most stringent |

### Biocompatible Materials at ProtoLabs

For detailed information on biocompatible materials, see:
- [3D Printing Biocompatibility](../3d-printing/biocompatibility.md)
- [CNC Machining Medical Materials](../cnc-machining/medical-materials.md)
- [Injection Molding Medical Grades](../injection-molding/medical-grades.md)

### Biocompatibility Testing Considerations

**Manufacturer Responsibility**:
- ProtoLabs provides materials meeting material specifications
- Device manufacturer is responsible for final biocompatibility assessment
- Testing must consider final device design, processing, and intended use
- Risk assessment per ISO 10993-1 required

**Material Equivalence**:
- Same material from different suppliers may have different biocompatibility profiles
- Processing methods can affect biocompatibility
- Sterilization method must be considered in biocompatibility assessment

---

## Sterilization Validation Requirements

### Overview

Medical devices must be sterilized to ensure they are free from viable microorganisms. Sterilization validation confirms that the sterilization process consistently achieves the required sterility assurance level (SAL).

### Sterilization Methods

| Method | Mechanism | Compatible Materials | Typical SAL |
|--------|-----------|---------------------|-------------|
| Steam (Autoclave) | Heat and moisture | Metals, some plastics | 10⁻⁶ |
| Ethylene Oxide (EtO) | Alkylation | Most materials | 10⁻⁶ |
| Gamma Radiation | Ionizing radiation | Most materials | 10⁻⁶ |
| E-Beam | Ionizing radiation | Most materials | 10⁻⁶ |
| Hydrogen Peroxide (VHP) | Oxidation | Heat-sensitive materials | 10⁻⁶ |

### Sterility Assurance Level (SAL)

- **SAL 10⁻⁶**: One in one million probability of a viable microorganism (standard for medical devices)
- **SAL 10⁻³**: One in one thousand probability (acceptable for some non-implantable devices)

### Sterilization Validation Process

#### 1. Installation Qualification (IQ)

- Verify equipment installation per specifications
- Confirm utilities and environmental conditions
- Document calibration of monitoring equipment
- Establish maintenance procedures

#### 2. Operational Qualification (OQ)

- Demonstrate equipment operates within specified limits
- Identify worst-case operating conditions
- Establish process parameters
- Document process capability

#### 3. Performance Qualification (PQ)

- Demonstrate process consistently achieves SAL
- Typically requires three consecutive successful cycles
- Use biological indicators (BIs) with known population of resistant microorganisms
- Conduct sterility testing on product samples

### Biological Indicators (BIs)

| Sterilization Method | BI Organism | Typical Population |
|---------------------|-------------|------------------|
| Steam | Geobacillus stearothermophilus | 10⁶ CFU |
| EtO | Bacillus atrophaeus | 10⁶ CFU |
| Radiation | Bacillus pumilus | 10⁶ CFU |
| VHP | Geobacillus stearothermophilus | 10⁶ CFU |

### Chemical Indicators (CIs)

- **Type 1**: Process indicators (exposure to sterilization conditions)
- **Type 2**: Special test indicators (for specific tests)
- **Type 3**: Single variable indicators (respond to one parameter)
- **Type 4**: Multi-variable indicators (respond to multiple parameters)
- **Type 5**: Integrating indicators (respond to all critical parameters)
- **Type 6**: Emulating indicators (cycle-specific)

### Sterilization Validation Documentation

| Document | Description | Retention |
|----------|-------------|-----------|
| Validation Protocol | IQ/OQ/PQ procedures | Permanent |
| Validation Report | Results and conclusions | Permanent |
| Biological Indicator Records | Lot numbers, results | Permanent |
| Calibration Records | Equipment calibration | Life + 2 years |
| Sterilization Load Records | Cycle parameters | 3 years |
| Sterility Test Results | Product testing | Permanent |

### Material Considerations for Sterilization

| Material | Steam | EtO | Gamma | E-Beam | Notes |
|----------|-------|-----|-------|--------|-------|
| PEEK | ✅ | ✅ | ✅ | ✅ | Excellent stability |
| PEI (Ultem) | ✅ | ✅ | ✅ | ✅ | Good stability |
| PPSU | ✅ | ✅ | ✅ | ✅ | Excellent stability |
| PC | ⚠️ | ✅ | ⚠️ | ⚠️ | May yellow with radiation |
| ABS | ⚠️ | ✅ | ❌ | ❌ | Degrades with radiation |
| Nylon | ✅ | ✅ | ⚠️ | ⚠️ | May degrade with radiation |
| Acetal | ❌ | ✅ | ❌ | ❌ | Degrades with radiation |
| LSR | ✅ | ✅ | ✅ | ✅ | Excellent stability |

*Legend: ✅ = Compatible, ⚠️ = Caution/Testing Required, ❌ = Not Recommended*

### ProtoLabs Sterilization Support

ProtoLabs provides manufacturing services for sterilizable medical devices:

- **Material Selection Guidance**: Recommendations for sterilization-compatible materials
- **Design for Sterilization**: DfX feedback for sterilization considerations
- **Process Validation Support**: Documentation for sterilization validation
- **Clean Manufacturing**: Controlled environments for medical device production

**Note**: ProtoLabs does not perform sterilization. Customers are responsible for:
- Selecting appropriate sterilization methods
- Validating sterilization processes
- Conducting sterility testing
- Maintaining sterilization records

---

## Design History File (DHF) and Device Master Record (DMR)

### Design History File (DHF)

Per 21 CFR 820.30(j), the DHF contains records demonstrating the design was developed in accordance with approved design plans.

#### DHF Contents

| Section | Contents | Documentation |
|---------|----------|---------------|
| Design Plan | Project timeline, milestones, responsibilities | Project plan, Gantt charts |
| Design Inputs | User needs, regulatory requirements, standards | Requirements document |
| Design Outputs | Drawings, specifications, manufacturing procedures | CAD files, specs |
| Design Review | Review records, action items, approvals | Meeting minutes |
| Design Verification | Test protocols, results, analysis | Test reports |
| Design Validation | Clinical data, user studies, validation reports | Validation summary |
| Design Transfer | Production specifications, training records | Transfer checklist |
| Design Changes | Change requests, assessments, approvals | ECO records |
| Design Records | All supporting documentation | Complete file |

### Device Master Record (DMR)

Per 21 CFR 820.181, the DMR contains records and procedures for device production.

#### DMR Contents

| Section | Contents | Documentation |
|---------|----------|---------------|
| Device Specifications | Drawings, component specs, software specs | Approved drawings |
| Production Process | Process specs, production procedures, equipment specs | Process instructions |
| Quality Assurance | Acceptance criteria, test procedures, inspection plans | QA procedures |
| Packaging & Labeling | Packaging specs, labeling specs, IFU | Label drawings |
| Installation/Maintenance | Installation procedures, maintenance procedures, service manuals | Service docs |

### Relationship Between DHF, DMR, and DHR

```
┌─────────────────────────────────────────────────────────────┐
│                    Design Phase                              │
│  ┌──────────────────────────────────────────────────────┐   │
│  │              Design History File (DHF)               │   │
│  │  (How the device was designed)                     │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   Production Phase                           │
│  ┌──────────────────────────────────────────────────────┐   │
│  │           Device Master Record (DMR)                 │   │
│  │  (How to build the device)                           │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Production Record                         │
│  ┌──────────────────────────────────────────────────────┐   │
│  │          Device History Record (DHR)                 │   │
│  │  (How this specific device was built)                │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### ProtoLabs Support for DHF/DMR

ProtoLabs provides documentation to support customer DHF and DMR requirements:

1. **Material Certifications**: Mill test reports, biocompatibility data
2. **Process Documentation**: Manufacturing process descriptions
3. **Inspection Records**: Dimensional inspection reports
4. **Test Reports**: Mechanical testing, special process certifications
5. **Certificates of Conformance**: Compliance declarations

**Note**: ProtoLabs maintains manufacturing records per ISO 13485. Customers are responsible for compiling and maintaining DHF and DMR for their specific devices.

---

## Risk Management (ISO 14971)

### Overview

ISO 14971 is the international standard for risk management of medical devices. It provides a framework for identifying, evaluating, and controlling risks throughout the device lifecycle.

### Risk Management Process

```
┌─────────────────────────────────────────────────────────────┐
│  1. Risk Analysis                                           │
│     • Intended use determination                             │
│     • Hazard identification                                  │
│     • Risk estimation                                        │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  2. Risk Evaluation                                          │
│     • Risk acceptability determination                       │
│     • Risk/benefit analysis                                  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  3. Risk Control                                             │
│     • Risk control option analysis                           │
│     • Implementation of risk control measures                │
│     • Residual risk evaluation                               │
│     • Risk/benefit analysis                                  │
│     • Completeness of risk control                           │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  4. Evaluation of Overall Residual Risk                      │
│     • Acceptability of overall residual risk                 │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  5. Risk Management Review                                   │
│     • Review of risk management process                      │
│     • Review of risk management report                       │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  6. Production and Post-Production Activities                │
│     • Information collection                                 │
│     • Risk management file updates                           │
│     • Risk management report updates                         │
└─────────────────────────────────────────────────────────────┘
```

### Risk Management File

The risk management file must include:

1. **Risk Management Plan**: Scope, risk acceptability criteria, evaluation methods
2. **Risk Analysis**: Hazard identification and risk estimation
3. **Risk Evaluation**: Risk acceptability determinations
4. **Risk Control**: Risk control measures and residual risk
5. **Risk Management Report**: Summary of risk management activities
6. **Post-Production Information**: Field data, complaints, vigilance reports

### Risk Acceptability Criteria

| Risk Level | Probability | Severity | Action Required |
|------------|-------------|----------|-----------------|
| Unacceptable | Any | Catastrophic | Risk must be reduced |
| Unacceptable | High | Serious | Risk must be reduced |
| ALARP | Medium | Serious | Risk reduction as low as reasonably practicable |
| Acceptable | Low | Serious | May be acceptable with justification |
| Acceptable | Any | Minor | Acceptable |

### Risk Control Hierarchy

1. **Inherent Safety by Design**: Eliminate hazards through design
2. **Protective Measures**: Safety features, guards, alarms
3. **Information for Safety**: Warnings, instructions, training

### ProtoLabs Risk Management Support

ProtoLabs supports customer risk management activities through:

1. **Material Information**: Biocompatibility data, material properties
2. **Process Information**: Manufacturing process details
3. **Quality Data**: Inspection results, process capability
4. **Change Notification**: Formal process for communicating changes
5. **Documentation**: Supporting documentation for risk management files

**Note**: ProtoLabs is responsible for manufacturing process risks. The device manufacturer retains responsibility for overall device risk management per ISO 14971.

---

## FDA 510(k) vs PMA Pathways

### Overview

The FDA regulates medical devices through two primary premarket pathways: 510(k) Premarket Notification and Premarket Approval (PMA).

### 510(k) Premarket Notification

**Purpose**: Demonstrate substantial equivalence to a legally marketed predicate device

**Substantial Equivalence Requirements**:
1. Same intended use as predicate
2. Same technological characteristics, OR
3. Different technological characteristics but:
   - Does not raise different safety/effectiveness questions
   - Substantially equivalent to predicate

**510(k) Types**:

| Type | Description | Timeline |
|------|-------------|----------|
| Traditional | Full submission with all data | 90 days |
| Special | Modifications to manufacturer's own device | 30 days |
| Abbreviated | Summary of safety/effectiveness | 90 days |

**510(k) Submission Contents**:

1. **Device Description**: Specifications, materials, design
2. **Indications for Use**: Intended use statement
3. **Predicate Device**: Legally marketed device comparison
4. **Substantial Equivalence Comparison**: Side-by-side table
5. **Proposed Labeling**: Labels and instructions for use
6. **Sterilization Information**: If applicable
7. **Biocompatibility Information**: Per ISO 10993
8. **Software Documentation**: If applicable
9. **Electrical Safety**: If applicable
10. **Performance Testing**: Bench, animal, clinical
11. **Financial Certification**: 21 CFR 54 (if clinical data)

**Timeline**:
- FDA has 90 days to review
- Clock stops for Additional Information (AI) requests
- Average review time: 3-6 months

### Premarket Approval (PMA)

**Purpose**: Demonstrate reasonable assurance of safety and effectiveness for high-risk devices

**PMA Applicability**:
- Class III devices (highest risk)
- No predicate device available
- Not substantially equivalent to any marketed device
- Life-supporting or life-sustaining devices

**PMA Application Contents**:

1. **Application Summary** (21 CFR 814.44)
2. **Table of Contents**
3. **Device Description** (detailed)
4. **Reference to Performance Standards**
5. **Proposed Labeling**
6. **Environmental Assessment**
7. **Relevant Information** (foreign marketing, bibliography)
8. **Financial Disclosure** (21 CFR 54)
9. **Clinical Investigations** (if applicable)
10. **Nonclinical Laboratory Studies** (if applicable)
11. **Manufacturing Information** (detailed)

**Clinical Data Requirements**:
- Typically required for PMA
- Must demonstrate reasonable assurance of safety and effectiveness
- Conducted under IDE (Investigational Device Exemption)
- Statistical analysis plan required

**Manufacturing Section**:

The PMA manufacturing section requires detailed information:

1. **Facility Information**: Location, size, layout
2. **Manufacturing Process**: Step-by-step description
3. **Quality System**: Compliance with 21 CFR 820
4. **Sterilization**: Validation if applicable
5. **Software**: Documentation if applicable
6. **Environmental Controls**: Clean room, contamination control

**Timeline**:
- FDA has 180 days to review (can be extended)
- Panel review may be required
- Manufacturing inspection required
- Average timeline: 12-18 months

### De Novo Pathway

**Purpose**: Novel low-to-moderate risk devices without predicate

**De Novo Process**:
1. Submit pre-submission to determine if De Novo appropriate
2. Submit De Novo request with:
   - Device description
   - Classification proposal
   - Risk/benefit analysis
   - Mitigation measures
3. FDA reviews and may grant De Novo
4. Device becomes predicate for future 510(k)s

**Timeline**: 120-150 days average

### Comparison Summary

| Aspect | 510(k) | PMA | De Novo |
|--------|--------|-----|---------|
| Device Risk | Low-Moderate | High | Low-Moderate (novel) |
| Predicate Required | Yes | No | No |
| Clinical Data | Sometimes | Usually | Sometimes |
| FDA Review Time | 90 days | 180+ days | 120-150 days |
| Panel Review | Rare | Common | Rare |
| Facility Inspection | Sometimes | Required | Sometimes |
| Cost | Lower | Higher | Moderate |

### ProtoLabs FDA Support

ProtoLabs supports customer FDA submissions through:

1. **Material Information**: Material specifications, biocompatibility data
2. **Manufacturing Documentation**: Process descriptions, quality system info
3. **Test Samples**: Prototypes for bench testing and validation
4. **Sterilization Compatibility**: Material compatibility information
5. **Change Control**: Formal process for manufacturing changes
6. **Quality Agreements**: Defining responsibilities for quality

**Note**: ProtoLabs provides manufacturing services and documentation. The device manufacturer retains responsibility for FDA submissions and regulatory compliance.

---

## Facility Certification Matrix for Medical

### United States Facilities

#### North Carolina (Morrisville) - 3D Printing
| Certification | Scope | Status | Medical Relevance |
|--------------|-------|--------|-------------------|
| ISO 9001:2015 | All Plastic 3D Printing | ✅ Active | Base QMS |
| AS9100D | DMLS, SLS, MJF 3D Printing | ✅ Active | Aerospace crossover |
| ISO 13485:2016 | DMLS 3D Printing | ✅ Active | Medical QMS |
| ITAR Registered | DMLS 3D Printing | ✅ Active | Defense crossover |

#### Minnesota (Plymouth/Rosemount) - Injection Molding & CNC
| Certification | Scope | Status | Medical Relevance |
|--------------|-------|--------|-------------------|
| ISO 9001:2015 | Injection Molding, CNC | ✅ Active | Base QMS |
| AS9100D | CNC Machining | ✅ Active | Aerospace crossover |
| ISO 13485:2016 | Injection Molding | ✅ Active | Medical QMS |
| ITAR Registered | CNC Machining, Molding | ✅ Active | Defense crossover |

### European Facilities

#### England (Telford)
| Certification | Scope | Status | Medical Relevance |
|--------------|-------|--------|-------------------|
| ISO 9001:2015 | Injection Molding, CNC | ✅ Active | Base QMS |
| AS9100D | CNC Machining | ✅ Active | Aerospace crossover |
| ISO 14001:2015 | Environmental | ✅ Active | Sustainability |
| ISO 45001:2018 | Safety | ✅ Active | Worker safety |
| JOSCAR | Defense Supply Chain | ✅ Active | UK defense |
| Cyber Essentials | Cybersecurity | ✅ Active | Data protection |

#### Germany (Putzbrunn)
| Certification | Scope | Status | Medical Relevance |
|--------------|-------|--------|-------------------|
| ISO 9001:2015 | 3D Printing | ✅ Active | Base QMS |
| ISO 14001:2015 | Environmental | ✅ Active | Sustainability |
| RoHS & REACH | Environmental | ✅ Active | EU compliance |

---

## Documentation Requirements for Medical Devices

### Overview

Medical device documentation must demonstrate compliance with regulatory requirements and ensure traceability throughout the product lifecycle. ProtoLabs maintains comprehensive documentation to support customer regulatory submissions.

### FDA Documentation Requirements (21 CFR 820)

#### Design Controls Documentation

| Document | Regulation | Description |
|----------|------------|-------------|
| Design Plan | 820.30(b) | Project plan with milestones |
| Design Inputs | 820.30(c) | Requirements specification |
| Design Outputs | 820.30(d) | Design specifications |
| Design Review Records | 820.30(e) | Review meeting minutes |
| Design Verification | 820.30(f) | Verification test results |
| Design Validation | 820.30(g) | Validation test results |
| Design Transfer | 820.30(h) | Transfer documentation |
| Design Changes | 820.30(i) | Change control records |
| Design History File | 820.30(j) | Complete design record |

#### Production Documentation

| Document | Regulation | Description |
|----------|------------|-------------|
| Device Master Record | 820.181 | Production specifications |
| Device History Record | 820.184 | Production records |
| Production Procedures | 820.70 | Manufacturing procedures |
| Process Validation | 820.75 | Validation records |
| Inspection Records | 820.80 | Inspection results |
| Test Records | 820.80 | Test results |
| Nonconforming Product | 820.90 | NCR records |
| CAPA Records | 820.100 | Corrective action records |

### ISO 13485:2016 Documentation Requirements

#### Mandatory Documents

| Clause | Required Document | Description |
|--------|-------------------|-------------|
| 4.2.1 | Quality Manual | QMS scope and structure |
| 4.2.2 | Medical Device File | Device-specific documentation |
| 4.2.3 | Document Control | Document control procedure |
| 4.2.4 | Record Control | Record control procedure |
| 5.3 | Quality Policy | Management commitment |
| 5.4.1 | Quality Objectives | Measurable objectives |
| 6.2.2 | Training Records | Personnel training |
| 7.1 | Risk Management File | ISO 14971 compliance |
| 7.3.10 | Design History File | Design and development records |
| 7.5.1 | Production Procedures | Controlled conditions |
| 7.5.3 | Traceability Records | Lot/serial tracking |
| 7.5.4 | Customer Property | Handling procedures |
| 7.5.6 | Validation Records | Process validation |
| 7.6 | Calibration Records | Equipment calibration |
| 8.2.2 | Internal Audit Records | Audit results |
| 8.2.4 | Inspection Records | Product inspection |
| 8.3 | Nonconforming Product | NCR records |
| 8.4 | CAPA Records | Corrective action |
| 8.5 | Improvement Records | Improvement activities |

### EU MDR Documentation Requirements

#### Technical Documentation (Annex II)

| Section | Contents |
|---------|----------|
| 1 | Device description and specifications |
| 2 | Information supplied by the manufacturer |
| 3 | Design and manufacturing information |
| 4 | General safety and performance requirements |
| 5 | Benefit-risk analysis and risk management |
| 6 | Product verification and validation |
| 7 | Post-market surveillance |

#### Post-Market Surveillance Documentation

| Document | Description | Frequency |
|----------|-------------|-----------|
| Post-Market Surveillance Plan | PMS strategy and procedures | Annual review |
| Periodic Safety Update Report (PSUR) | Safety and performance summary | Annual (Class IIa/IIb), Semi-annual (Class III) |
| Post-Market Clinical Follow-up (PMCF) | Clinical data collection | Per plan |
| Vigilance Reports | Incident reporting | As required |

### Documentation Retention Periods

| Document Type | FDA (21 CFR 820) | ISO 13485 | EU MDR |
|---------------|------------------|-----------|--------|
| Design History File | Life + 2 years | Life + 2 years | 15 years |
| Device Master Record | Life + 2 years | Life + 2 years | 15 years |
| Device History Record | Life + 2 years | Life + 2 years | 15 years |
| Quality Records | Life + 2 years | Life + 2 years | 15 years |
| Complaint Records | Life + 2 years | Life + 2 years | 15 years |
| CAPA Records | Life + 2 years | Life + 2 years | 15 years |
| Training Records | Life + 2 years | Life + 2 years | 10 years |
| Internal Audit Records | 2 years | 2 years | 5 years |
| Management Review Records | 2 years | 2 years | 5 years |
| Supplier Records | Life + 2 years | Life + 2 years | 10 years |
| Calibration Records | Life + 2 years | Life + 2 years | Life + 2 years |
| Process Validation Records | Life + 2 years | Life + 2 years | 15 years |

*Note: "Life" refers to the life of the device, not any particular unit*

### Electronic Records and Signatures (21 CFR Part 11)

When maintaining electronic records:

| Requirement | Implementation |
|-------------|------------------|
| Validation | System validation documentation |
| Audit Trails | Secure, computer-generated timestamps |
| Access Controls | Unique user IDs, password protection |
| Authority Checks | Role-based access permissions |
| Device Checks | Workstation validation |
| Documentation Controls | Version control, change management |
| Signature Manifestations | Printed name, date, meaning |
| Signature/Record Linking | Binding of signatures to records |

### ProtoLabs Documentation Services

ProtoLabs provides comprehensive documentation to support medical device compliance:

1. **Material Documentation**: Material certifications, biocompatibility data
2. **Process Documentation**: Manufacturing process descriptions
3. **Quality Documentation**: Inspection reports, test results
4. **Change Control**: Formal notification of process changes
5. **Traceability**: Lot tracking and serialization
6. **Certificates**: Certificates of Conformance

**Quality Agreements**: ProtoLabs enters into quality agreements with medical device customers to define:
- Quality responsibilities
- Documentation requirements
- Change notification procedures
- Complaint handling procedures
- Audit rights

---

## Cross-References

- See [regulatory-framework.md](../compliance/regulatory-framework.md) for general compliance overview
- See [medical-low-volume.md](./medical-low-volume.md) for medical manufacturing capabilities
- See [aerospace-compliance.md](./aerospace-compliance.md) for aerospace compliance
- See [automotive-ev-compliance.md](./automotive-ev-compliance.md) for automotive compliance
- See [3d-printing/biocompatibility.md](../3d-printing/biocompatibility.md) for biocompatibility details
