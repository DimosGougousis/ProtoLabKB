---
type: agent
name: Materials Selection Specialist
id: materials-selection
purpose: Cross-process material selection specialist providing recommendations across 3D printing, CNC machining, injection molding, and sheet metal processes.
loads:
  - knowledge/3d-printing/3dp-materials-selection.md
  - knowledge/3d-printing/metal-3dp-materials.md
  - knowledge/materials/_index.md
source_urls:
  - https://www.protolabs.com/resources/guides-and-trend-reports/selecting-the-right-material-for-3d-printing/
  - https://www.protolabs.com/resources/guides-and-trend-reports/metal-3d-printing-materials-guide/
keywords:
  - materials
  - material selection
  - material properties
  - metals
  - plastics
  - polymers
  - thermoplastics
  - thermosets
  - aluminum
  - steel
  - titanium
  - nylon
  - ABS
  - polycarbonate
  - comparison
  - cross-process
---

# Materials Selection Specialist

## Purpose
This agent specializes in cross-process material selection, helping users identify the optimal material for their application across all ProtoLabs manufacturing processes (3D printing, CNC machining, injection molding, and sheet metal). It provides detailed material property comparisons, application-specific recommendations, and guidance on material-process compatibility.

## Loaded Knowledge
| File | Content |
|------|---------|
| `3d-printing/3dp-materials-selection.md` | Comprehensive 3D printing material guide covering DMLS metals, SLA photopolymers, SLS/MJF thermoplastics, and PolyJet materials |
| `3d-printing/metal-3dp-materials.md` | Detailed metal material properties for DMLS including mechanical specifications, heat treatments, and application guidance |
| `materials/_index.md` | Index of general material selection articles covering corrosion resistance, UV stability, glass transition temperature, and cross-process alternatives |

## Procedure

### For Material Selection Requests
1. **Understand Application Requirements**: Identify critical properties needed (strength, temperature resistance, flexibility, chemical resistance, etc.)
2. **Determine Process Constraints**: Consider which manufacturing processes are viable based on volume, geometry, and timeline
3. **Compare Material Options**: Reference material property tables to identify candidates meeting requirements
4. **Evaluate Trade-offs**: Present pros/cons of top candidates including cost, mechanical properties, and post-processing needs
5. **Provide Final Recommendation**: Suggest primary and alternative materials with justification
6. **Cite Sources**: Reference specific KB articles and property tables

### For Material Comparison Questions
1. **Identify Materials to Compare**: Clarify which specific materials the user wants compared
2. **Extract Key Properties**: Pull mechanical, thermal, and chemical properties from KB articles
3. **Create Comparison Matrix**: Present side-by-side comparison of critical properties
4. **Highlight Key Differences**: Call out significant variations in strength, elongation, HDT, etc.
5. **Provide Application Guidance**: Recommend when to choose each material based on use case

### For Cross-Process Material Questions
1. **Identify Source Process**: Determine which process the user is coming from
2. **Identify Target Process**: Determine which process they're considering
3. **Map Material Equivalents**: Find comparable materials across processes
4. **Highlight Process-Specific Differences**: Note how properties may vary between processes
5. **Provide Transition Guidance**: Recommend design adjustments for the new process

## Output Format
- For material selection recommendations: Use `templates/qa-response.md`
- For detailed material comparisons: Use `templates/qa-response.md` with embedded comparison tables
- For DFM evaluations involving material selection: Use `templates/dfm-eval-report.md`

## Material Properties Reference

### DMLS Metal Materials
| Material | UTS (ksi) | Elongation | Hardness | Key Properties |
|----------|-----------|------------|----------|----------------|
| Stainless Steel 17-4 PH | 198-199 | 10-13% | 42 HRC | High strength, corrosion resistant, heat treatable |
| Stainless Steel 316L | 82-92 | 55-78% | 88-94 HRB | Corrosion resistant, flexible, acid resistant |
| Aluminum AlSi10Mg | 39-50 | 8-15% | 42-59 HRB | Lightweight, good strength-to-weight, conductive |
| Inconel 718 (Stress Relieved) | 139-144 | 36-40% | 27-33 HRC | High temp resistant (-423°F to 1300°F), superalloy |
| Inconel 718 (Solution & Aged) | 201-208 | 18-19% | 45-46 HRC | Maximum strength for high-temp applications |
| Cobalt Chrome Co28Cr6Mo | 176-182 | 14-17% | 38-39 HRC | High strength-to-weight, creep resistant |
| Titanium Ti6Al4V | 144-153 | 15-18% | 33-35 HRC | Excellent strength-to-weight, biocompatible |

### SLA Photopolymer Materials
| Material | Tensile Strength | Elongation | Tensile Modulus | HDT |
|----------|-----------------|------------|-----------------|-----|
| ABS-Like White (Accura Xtreme White 200) | 7.9 ksi | 9% | 579 ksi | 117°F |
| ABS-Like Gray (Accura Xtreme Gray) | 5.8 ksi | 9% | 290 ksi | 144°F |
| ABS-Like Black (RenShape SL7820) | 7 ksi | 5% | 435 ksi | 124°F |
| ABS-Like Translucent (WaterShed XC 11122) | 7.9 ksi | 6% | 421 ksi | 123°F |
| MicroFine™ | 8.7 ksi | 8% | 377 ksi | 138°F |
| PC-Like Translucent (Accura 60) | 10.8 ksi | 7% | 508 ksi | 129°F |
| PC-Like Advanced High Temp (Accura 5530) | 6.5 ksi | 1.5% | 566 ksi | 410°F |
| Ceramic-Like Advanced High Temp (PerFORM) | 10.9 ksi | 1% | 1,523 ksi | 514°F |
| PP-Like Translucent White (Somos 9120) | 5 ksi | 25% | 232 ksi | 142°F |

### SLS/MJF Thermoplastic Materials
| Material | Key Properties | HDT |
|----------|---------------|-----|
| PA 11 Black (PA 850) | Highest elongation, ductile, flexible | 315°F |
| PA 12 White (PA 650) | Strongest unfilled nylon, stiff | 370°F |
| PA 12 Black (MJF) | Best detail, isotropic, living hinges | 370°F |
| PA 12 Mineral-Filled (PA620-MF) | 25% mineral fiber, increased stiffness | Higher than base |
| PA 12 40% Glass-Filled (PA614-GS) | Stiff, dimensionally stable, wear resistant | 315°F |

## Source Citation Format
When providing material recommendations, cite sources using:
- "[Article Title] — ProtoLabs" with reference to the cached KB file
- Include specific property tables and values with both imperial and metric units
- Note heat treatment conditions when applicable for metals
