---
type: knowledge-article
category: compliance
source_url: https://www.fda.gov/medical-devices/medical-device-biocompatibility
fetched_at: 2026-04-21
summary: FDA biocompatibility requirements for 3D printed medical devices including ISO 10993 testing, USP Class VI certifications, sterilization compatibility, and biocompatible materials for MJF, SLS, and SLA processes.
---

# FDA Biocompatibility for 3D Printed Medical Devices

## Overview

Medical devices manufactured via additive manufacturing (3D printing) must meet stringent biocompatibility requirements to ensure patient safety. The FDA recognizes ISO 10993 as the primary framework for biological evaluation of medical devices.

## ISO 10993 Testing Requirements

### Biological Evaluation Framework

ISO 10993 consists of 20+ parts covering various biological tests:

| Test Category | ISO 10993 Part | Purpose | Typical For 3D Printed Parts |
|---------------|----------------|---------|------------------------------|
| Cytotoxicity | Part 5 | Cell viability assessment | All patient-contacting devices |
| Sensitization | Part 10 | Allergic response potential | Implantables, prolonged contact |
| Irritation | Part 10 | Skin/mucosal irritation | External devices, short-term contact |
| Systemic Toxicity | Part 11 | Whole-body toxicity | Implantables, blood contact |
| Hemocompatibility | Part 4 | Blood interaction | Cardiovascular devices |
| Implantation | Part 6 | Local tissue response | Permanent implants |
| Genotoxicity | Part 3 | DNA damage potential | Long-term implants |
| Carcinogenicity | Part 3 | Cancer risk assessment | Permanent implants (>30 days) |

### Testing Considerations for 3D Printed Devices

**Surface Characteristics:**
- Layer lines and surface roughness may affect cell attachment
- Post-processing (polishing, coating) can alter biocompatibility
- Test on finished parts, not raw material

**Material Anisotropy:**
- Mechanical properties vary by build orientation
- Biological response may differ by surface orientation
- Test samples should represent actual build orientation

**Residual Materials:**
- Unreacted monomers (SLA/DLP)
- Powder residue (SLS/MJF)
- Support material traces
- Cleaning validation required

## USP Class VI Certifications

### Overview

USP Class VI testing is a comprehensive biological reactivity test for plastics used in medical devices. It is more stringent than ISO 10993-5 cytotoxicity testing alone.

### Test Components

| Test | Description | Acceptance Criteria |
|------|-------------|-------------------|
| Systemic Injection | Mouse intravenous injection | No significant biological reaction |
| Intracutaneous | Rabbit skin injection | Non-irritant response |
| Implantation | Rabbit muscle implant (7 days) | Non-toxic tissue response |

### USP Class VI Materials for 3D Printing

| Process | Material | USP Class VI Status | Typical Applications |
|---------|----------|---------------------|---------------------|
| **SLA** | Accura® ClearVue | ✅ Certified | Microfluidics, surgical guides |
| **SLA** | Accura® 25 | ✅ Certified | Medical models, devices |
| **SLA** | Accura® 60 | ✅ Certified | Rigid medical components |
| **MJF** | PA 12 (Nylon) | ✅ Certified | Surgical instruments, housings |
| **MJF** | PA 12 GB (Glass Bead) | ✅ Certified | Structural medical parts |
| **SLS** | PA 12 (Nylon) | ✅ Certified | Prosthetics, orthotics |
| **SLS** | TPU (Thermoplastic Polyurethane) | ✅ Certified | Flexible medical devices |

**Note:** Material certifications are batch-specific. Always verify current certification status with ProtoLabs before production.

## Biocompatible Materials by Process

### Multi Jet Fusion (MJF) - Medical Grade

| Material | Biocompatibility | Sterilization | Key Properties | Applications |
|----------|------------------|---------------|----------------|--------------|
| **PA 12 (Nylon)** | USP Class VI | Autoclave, Gamma, EtO | Chemical resistant, durable | Surgical instruments, housings |
| **PA 12 GB** | USP Class VI | Autoclave, Gamma, EtO | Rigid, dimensionally stable | Structural components, fixtures |
| **PP (Polypropylene)** | USP Class VI | Autoclave, Gamma, EtO | Flexible, chemical resistant | Fluid handling, containers |

### Selective Laser Sintering (SLS) - Medical Grade

| Material | Biocompatibility | Sterilization | Key Properties | Applications |
|----------|------------------|---------------|----------------|--------------|
| **PA 12 (Nylon)** | USP Class VI | Autoclave, Gamma, EtO | Durable, wear resistant | Prosthetics, orthotics, braces |
| **TPU** | USP Class VI | Gamma, EtO (caution: autoclave) | Flexible, rubber-like | Seals, gaskets, cushioning |
| **PA 11** | USP Class VI | Autoclave, Gamma, EtO | Bio-based, impact resistant | Surgical guides, housings |

### Stereolithography (SLA) - Medical Grade

| Material | Biocompatibility | Sterilization | Key Properties | Applications |
|----------|------------------|---------------|----------------|--------------|
| **Accura ClearVue** | USP Class VI | Limited (surface degradation) | Transparent, rigid | Microfluidics, visualization |
| **Accura 25** | USP Class VI | Limited | ABS-like, durable | Medical models, prototypes |
| **Accura 60** | USP Class VI | Limited | Rigid, high detail | Surgical planning models |

**Important:** SLA materials have limited sterilization compatibility due to potential surface degradation. Verify specific application requirements.

## Sterilization Compatibility

### Autoclave (Steam Sterilization)

**Compatible Materials:**
- PA 12 (MJF, SLS)
- PA 12 GB (MJF)
- PA 11 (SLS)
- PP (MJF)

**Parameters:**
- Temperature: 121°C (250°F) or 134°C (273°F)
- Pressure: 15-30 psi
- Cycle time: 15-30 minutes
- Considerations: May cause slight dimensional changes (<0.5%)

### Gamma Sterilization

**Compatible Materials:**
- PA 12 (MJF, SLS)
- PA 12 GB (MJF)
- PA 11 (SLS)
- TPU (SLS) - limited cycles
- PP (MJF)
- Accura ClearVue (SLA) - limited

**Parameters:**
- Dose: Typically 25-50 kGy
- Penetration: Excellent (through packaging)
- Effects: May cause slight yellowing in some polymers
- Validation: Required per ISO 11137

### Ethylene Oxide (EtO) Sterilization

**Compatible Materials:**
- All MJF materials (PA 12, PA 12 GB, PP)
- All SLS materials (PA 12, PA 11, TPU)
- SLA materials with aeration considerations

**Parameters:**
- Concentration: 450-1200 mg/L
- Temperature: 40-60°C
- Humidity: 60-90% RH
- Aeration: Required post-cycle (8-12 hours minimum)
- Validation: Required per ISO 11135

### Sterilization Method Selection Guide

| Application | Recommended Method | Rationale |
|-------------|-------------------|-----------|
| Surgical instruments (reusable) | Autoclave | Cost-effective, validated |
| Implantables (single-use) | Gamma or EtO | Terminal sterilization, packaging integrity |
| Diagnostic housings | Gamma | Through-package penetration |
| Flexible components (TPU) | EtO or Gamma | Temperature sensitivity |
| Microfluidics (ClearVue) | EtO only | Temperature/material sensitivity |

## FDA Master File References

### Type III Drug Master Files (DMF)

Device manufacturers may reference ProtoLabs' material suppliers' DMFs in their 510(k) or PMA submissions:

| Material | DMF Type | Typical Holder | Purpose |
|----------|----------|----------------|---------|
| PA 12 | Type III | Evonik, Arkema | Material composition, biocompatibility |
| PP | Type III | Various | Polypropylene resin data |
| TPU | Type III | Lubrizol, BASF | Thermoplastic polyurethane data |

### 510(k) Submission Support

ProtoLabs can provide the following for medical device 510(k) submissions:

- **Material Certificates**: Lot-specific material data
- **Process Documentation**: Manufacturing process descriptions
- **Dimensional Reports**: As-built dimensional verification
- **Sterilization Validation**: Compatibility data (customer-validated)
- **Biocompatibility**: USP Class VI certificates (material-level)

**Important**: ProtoLabs provides manufacturing services and material data. The device manufacturer retains responsibility for:
- Device design validation
- Final biocompatibility assessment per ISO 10993
- Clinical evaluation (if required)
- Regulatory submission and clearance

## Compliance Verification Checklist

### Pre-Production Compliance Review

```markdown
## Medical Device (ISO 13485/FDA)
- [ ] Material biocompatibility verified (USP Class VI or ISO 10993)
- [ ] Sterilization method validated for material
- [ ] DMLS process selected (only ISO 13485 certified process)
- [ ] NC facility specified (only ISO 13485 certified facility)
- [ ] Material certificates requested
- [ ] Dimensional tolerances appropriate for medical grade
- [ ] Surface finish requirements documented
- [ ] FDA Master File references identified (if applicable)

## Aerospace (AS9100)
- [ ] AS9100D certification confirmed for process
- [ ] NADCAP heat treatment identified (if required)
- [ ] Material traceability requirements documented
- [ ] First Article Inspection (FAI) requested
- [ ] Chemical composition certificates requested
- [ ] DMLS, SLS, or MJF selected (AS9100 certified)
- [ ] NC facility specified for flight-critical parts

## Defense/ITAR
- [ ] ITAR registration confirmed (DMLS at NC facility)
- [ ] End-use certificate obtained (if required)
- [ ] Foreign national access restrictions implemented
- [ ] Technical data handling procedures followed
- [ ] Design files marked and controlled per ITAR
- [ ] CMMC readiness confirmed (if applicable)
```

### Documentation Requirements by Industry

| Industry | Required Documents | Optional but Recommended |
|----------|-------------------|-------------------------|
| Medical | Material cert, dimensional report | Sterilization validation, biocompatibility summary |
| Aerospace | Material cert, CoC, FAI | NADCAP cert, chemical analysis |
| Defense | ITAR compliance letter, CoC | End-use cert, CMMC attestation |
| General | CoC | Dimensional report, material cert |

## Summary

This compliance framework ensures ProtoLabs' 3D printing services meet the stringent requirements of regulated industries. Always verify:
1. **Process Certification**: Confirm the selected process has required certifications
2. **Facility Compliance**: Ensure correct facility for ITAR/ISO 13485 requirements
3. **Material Suitability**: Verify material meets biocompatibility and sterilization needs
4. **Documentation**: Request appropriate certificates and inspection reports
5. **Regulatory Responsibility**: Understand ProtoLabs provides manufacturing; customer retains regulatory responsibility

For complex compliance questions, escalate to ProtoLabs' compliance team via the appropriate channels.
