---
type: knowledge-article
category: compliance
source_url: https://www.astm.org/committee/f42
fetched_at: 2026-04-21
summary: Additive manufacturing quality standards including ASTM F42 and ISO/ASTM 52900 family, AS9100 for AM, process and material qualification standards, post-processing requirements, and non-destructive testing protocols for aerospace and medical applications.
---

# Additive Manufacturing Quality Standards

## Overview

Additive manufacturing (AM) quality standards ensure that 3D printed parts meet the stringent requirements of regulated industries including aerospace, medical, and defense. This article covers the key standards families and their application to AM processes.

## ASTM F42 Committee on Additive Manufacturing

### Committee Structure

ASTM Committee F42 is the primary standards body for additive manufacturing technologies. The committee is organized into subcommittees:

| Subcommittee | Scope | Key Standards |
|--------------|-------|---------------|
| F42.01 | Test Methods | Terminology, test piece geometries |
| F42.04 | Design | Design guidelines, file formats |
| F42.05 | Materials and Processes | Material specifications, process parameters |
| F42.06 | Environment, Health, Safety | Safety guidelines, handling procedures |
| F42.07 | Applications | Industry-specific standards |
| F42.08 | Data | Data formats, traceability |
| F42.09 | AM Systems | Machine qualification, calibration |

### Key ASTM F42 Standards

| Standard | Title | Application |
|----------|-------|-------------|
| **F2792** | Standard Terminology for AM | Universal terminology reference |
| **F2924** | Standard for Powder Bed Fusion Ti-6Al-4V | DMLS titanium specification |
| **F3055** | Standard for Powder Bed Fusion Nickel Alloy 718 | DMLS Inconel specification |
| **F3056** | Standard for Powder Bed Fusion Cobalt Chrome | DMLS CoCr specification |
| **F3122** | Guide for Evaluating Mechanical Properties | Testing methodology |
| **F3213** | Standard for Powder Bed Fusion AlSi10Mg | DMLS aluminum specification |
| **F3318** | Standard for Powder Bed Fusion 316L Stainless | DMLS stainless steel specification |
| **F3533** | Standard for Directed Energy Deposition | DED process specification |

## ISO/ASTM 52900 Family of AM Standards

### Joint Standards Development

ISO and ASTM collaborate through the ISO/ASTM Joint Group to develop harmonized international standards for AM. The ISO/ASTM 52900 series provides comprehensive coverage:

| Standard | Title | Scope |
|----------|-------|-------|
| **ISO/ASTM 52900** | Additive manufacturing – General principles – Fundamentals and vocabulary | Terminology and concepts |
| **ISO/ASTM 52901** | Additive manufacturing – General principles – Requirements for purchased AM parts | Buyer requirements |
| **ISO/ASTM 52902** | Additive manufacturing – Quality assurance – Quality characteristic indicators | Quality metrics |
| **ISO/ASTM 52903** | Additive manufacturing – Material extrusion – Specifications for test artifacts | FDM testing |
| **ISO/ASTM 52904** | Additive manufacturing – Powder bed fusion – Specifications for test artifacts | PBF testing |
| **ISO/ASTM 52910** | Additive manufacturing – Design – Data quality | Design data requirements |
| **ISO/ASTM 52911** | Additive manufacturing – Design – Part orientation, supports, and post-processing | Design guidelines |
| **ISO/ASTM 52915** | Additive manufacturing – File format – AMF (Additive Manufacturing File Format) | File format spec |
| **ISO/ASTM 52950** | Additive manufacturing – Post-processing – Methods and categories | Post-processing |

## AS9100 for Additive Manufacturing

### AS9100D and AM

AS9100D is the aerospace quality management standard that includes specific considerations for additive manufacturing:

| AS9100 Clause | AM Application | Requirements |
|---------------|--------------|--------------|
| **8.4 (External Providers)** | AM material suppliers | Supplier approval, powder certification |
| **8.5.1 (Production Control)** | AM process control | Parameter control, build monitoring |
| **8.5.2 (Identification)** | AM part traceability | Serial numbers, build records |
| **8.6 (Release)** | AM part acceptance | Inspection, testing, documentation |
| **9.1 (Monitoring)** | AM process monitoring | SPC, build data analysis |

### AM-Specific AS9100 Requirements

**Process Qualification:**
- Machine qualification per ASTM F3055/F3122
- Material qualification with full traceability
- Operator certification and training records
- Build parameter documentation and control

**Documentation Requirements:**
- Build logs with machine parameters
- Powder lot traceability
- Heat treatment records (NADCAP if required)
- Inspection reports (CMM, DIR)
- First Article Inspection (FAI) for new designs

## Process Qualification Standards

### ASTM F3055 - Process Qualification

ASTM F3055 provides the framework for qualifying powder bed fusion processes:

**Qualification Elements:**
1. **Machine Qualification:** Demonstrate machine capability
2. **Material Qualification:** Verify material properties
3. **Process Qualification:** Validate process parameters
4. **Personnel Qualification:** Certify operators

**Test Requirements:**
| Test | Standard | Purpose |
|------|----------|---------|
| Tensile Testing | ASTM E8/E8M | Mechanical properties |
| Density | ASTM B311 | Part density measurement |
| Chemical Analysis | ASTM E1479 | Material composition |
| Microstructure | ASTM E3 | Metallographic examination |
| Surface Roughness | ASTM D7127 | Surface finish |

### ASTM F3122 - Mechanical Property Evaluation

ASTM F3122 provides guidelines for evaluating mechanical properties of AM materials:

**Key Considerations:**
- **Orientation Effects:** Test specimens in multiple orientations (X, Y, Z, XY, XZ, YZ)
- **Location Effects:** Test from different build locations
- **Build-to-Build Variation:** Multiple builds for statistical validity
- **Post-Processing Effects:** Test in as-built and post-processed conditions

**Minimum Test Matrix:**
| Orientation | Tensile | Fatigue | Creep |
|-------------|---------|---------|-------|
| Horizontal (XY) | Required | Recommended | If applicable |
| Vertical (Z) | Required | Recommended | If applicable |
| 45° Diagonal | Recommended | Optional | If applicable |

## Material Qualification Standards

### Powder Characterization

| Property | Test Method | Requirement |
|----------|-------------|-------------|
| Chemistry | ASTM E1479 | Within specification |
| Particle Size Distribution | ASTM B214 | D10, D50, D90 within spec |
| Apparent Density | ASTM B212 | Minimum density |
| Tap Density | ASTM B527 | Maximum packing |
| Flow Rate | ASTM B213 | Hall flow time |
| Morphology | SEM analysis | Spherical, minimal satellites |
| Moisture Content | Karl Fischer | Below maximum limit |
| Contamination | ASTM E1479 | Within specification |

### Material Specification Standards

| Material | ASTM Standard | ISO Standard |
|----------|---------------|--------------|
| Ti-6Al-4V | ASTM F2924 | ISO 5832-3 |
| Inconel 718 | ASTM F3055 | - |
| Cobalt Chrome | ASTM F3056 | ISO 5832-12 |
| AlSi10Mg | ASTM F3213 | - |
| 316L Stainless | ASTM F3318 | ISO 5832-1 |
| PA 12 (Nylon) | - | ISO 1874 |
| TPU | ASTM F2921 | - |

## Post-Processing Requirements

### Heat Treatment Standards

| Process | Standard | Application |
|---------|----------|-------------|
| Stress Relief | ASTM F3055 | All metal AM parts |
| Hot Isostatic Pressing (HIP) | ASTM B672 | Critical aerospace parts |
| Solution Treatment | AMS 5662 | Inconel 718 |
| Aging | AMS 5663 | Inconel 718 |
| Annealing | ASTM A480 | Stainless steels |

**NADCAP Certification:**
- Required for flight-critical aerospace parts
- Covers heat treatment, chemical processing, NDT
- ProtoLabs NC facility: NADCAP certified

### Surface Finishing Standards

| Finish Type | Standard | Typical Application |
|-------------|----------|---------------------|
| As-built | - | Non-critical surfaces |
| Media blasting | ASTM D7127 | Uniform matte finish |
| Machining | ASME Y14.5 | Precision surfaces |
| Polishing | ASTM D523 | Aesthetic surfaces |
| Coating | ASTM D7091 | Corrosion protection |
| Passivation | ASTM A967 | Stainless steel corrosion resistance |

## Non-Destructive Testing (NDT) for AM Parts

### NDT Methods for Additive Manufacturing

| Method | Standard | Application | AM-Specific Considerations |
|--------|----------|-------------|---------------------------|
| **X-Ray CT** | ASTM E1441 | Internal defects, porosity | Detects lack of fusion, keyholing |
| **Ultrasonic Testing** | ASTM E494 | Internal flaws, delamination | Surface finish affects coupling |
| **Penetrant Testing** | ASTM E165 | Surface cracks, porosity | Post-processing may mask defects |
| **Magnetic Particle** | ASTM E1444 | Surface/subsurface flaws in ferromagnetic materials | Limited to iron, nickel, cobalt alloys |
| **Eddy Current** | ASTM E690 | Surface defects, conductivity | Limited conductive materials |
| **Visual Inspection** | ASTM E1658 | Surface finish, obvious defects | First line of inspection |

### AM-Specific Defects to Detect

| Defect Type | Description | Criticality | Detection Method |
|-------------|-------------|-------------|------------------|
| **Porosity** | Gas pockets in material | High | X-Ray CT, UT |
| **Lack of Fusion** | Incomplete layer bonding | Critical | X-Ray CT, UT |
| **Keyholing** | Excessive penetration voids | High | X-Ray CT |
| **Balling** | Partially melted powder | Medium | Visual, PT |
| **Delamination** | Layer separation | Critical | UT, X-Ray CT |
| **Residual Stress Cracking** | Stress-induced cracks | Critical | PT, MT, UT |
| **Contamination** | Foreign material inclusion | High | X-Ray CT |

### NDT Acceptance Criteria

**Aerospace (AS9100) Typical Criteria:**
- Porosity: <0.5% by volume
- Lack of fusion: None allowed
- Crack-like indications: None allowed
- Surface roughness: Per drawing specification

**Medical (ISO 13485) Typical Criteria:**
- Porosity: <0.1% for implants
- Surface defects: None on patient-contacting surfaces
- Contamination: None allowed
- Dimensional: Per design specification

## Quality Documentation for AM

### Required Documentation by Industry

| Document | Description | Aerospace | Medical | General |
|----------|-------------|-----------|---------|---------|
| **Build Log** | Machine parameters, build time | Required | Required | Recommended |
| **Material Certificate** | Powder lot, chemistry | Required | Required | Available |
| **Powder Traceability** | Lot number, reuse cycles | Required | Required | Available |
| **Dimensional Report** | As-built measurements | Required | Required | Available |
| **NDT Report** | Inspection results | Required | Required | Available |
| **Heat Treatment Record** | Cycle parameters | Required | If applicable | Available |
| **FAI Report** | First article inspection | Required | Recommended | Available |
| **CoC** | Certificate of Conformance | Required | Required | Standard |

### AM-Specific Quality Records

**Build Data to Retain:**
- Machine ID and calibration status
- Build date and duration
- Layer thickness and orientation
- Laser/power parameters (DMLS)
- Fuse/scan settings (MJF, SLS)
- Support structure locations
- Powder lot numbers
- Powder refresh ratios
- Environmental conditions

**Traceability Requirements:**
- Part serial numbers linked to build
- Material lot traceability
- Operator identification
- Inspection records linkage
- Non-conformance records

## Summary

Additive manufacturing quality standards ensure that 3D printed parts meet the rigorous requirements of aerospace, medical, and other regulated industries. Key elements include:

1. **Process Qualification:** ASTM F3055, F3122 for machine and process validation
2. **Material Qualification:** Full characterization and traceability
3. **Post-Processing:** NADCAP heat treatment where required
4. **Non-Destructive Testing:** X-Ray CT, UT, PT for defect detection
5. **Documentation:** Comprehensive records for traceability and compliance

ProtoLabs maintains certifications and follows these standards to deliver production-quality 3D printed parts for critical applications.
