# Husqvarna 701 Titanium Clutch Lever - CAD Models

This folder contains the 3D CAD models and design specifications for a titanium clutch lever designed for the Husqvarna 701 motorcycle.

## Files

| File | Description | Format |
|------|-------------|--------|
| `husqvarna-701-lever-realistic.stp` | **RECOMMENDED** - Realistic curved geometry with ball end | STEP |
| `husqvarna-701-clutch-lever.stp` | Alternative STEP file | STEP |
| `clutch-lever-fusion360.py` | Fusion 360 parametric design script | Python |
| `clutch-lever-design-spec.md` | Detailed design specification document | Markdown |

## Quick Import Instructions

### STEP File (Recommended)
The `husqvarna-701-lever-realistic.stp` file contains a realistic clutch lever with curved profile and ball end:

**SolidWorks:**
- File > Open > Select `.stp` file
- Set Options > STEP to "Automatic"

**Fusion 360:**
- File > Open > Select `.stp` file
- Choose "Open" to import as new design

**CATIA:**
- File > Open > Select STEP file type
- Import as new part

**AutoCAD:**
- INSERT > Import > Select `.stp` file

### Fusion 360 Script
Run `clutch-lever-fusion360.py` to generate a parametric model with editable dimensions.

## Quick Specifications

| Attribute | Value |
|-----------|-------|
| **Material** | Ti-6Al-4V (Grade 5) Titanium |
| **Process** | CNC Mill-Turn |
| **Length** | 155 mm |
| **Weight** | ~42g (30% lighter than OEM aluminum) |
| **Pivot Bore** | 8mm H7 (±0.025mm) |

## Key Design Features

1. **Pivot Boss** - 16mm OD cylindrical mounting interface with 8mm precision bore
2. **Tapered Blade** - 145mm lever arm tapering from 18mm to 12mm width
3. **Breakaway Notch** - Crash protection feature at 5mm from pivot
4. **Ball End Tip** - 6mm radius ergonomic finger contact
5. **Reach Adjuster** - Optional M5 threaded hole for adjustment screw

## DFM Compliance

This design follows ProtoLabs CNC machining DFM guidelines:

- ✓ Wall thickness: 4.5mm (exceeds 0.5mm minimum)
- ✓ Internal radii: 0.5mm minimum
- ✓ Hole depth ratios: Within 6:1 limit
- ✓ Thread size: M5 within automated range
- ✓ Tolerances: Appropriate for capabilities

## Usage

### Importing STEP Files

**SolidWorks:**
1. File > Open
2. Select `.step` file
3. Set Options > Import > STEP to "Automatic"

**Fusion 360:**
1. File > Open
2. Select `.step` file
3. Choose "Open" to import as new design

**CATIA:**
1. File > Open
2. Select `.step` file type
3. Import as new part

### Running Fusion 360 Script

1. Open Fusion 360
2. Go to **Utilities** > **Add-ins** > **Scripts and Add-ins**
3. Click **Create** > **New Script**
4. Name it "ClutchLever"
5. Replace the default code with the contents of `clutch-lever-fusion360.py`
6. Click **Run**

## Manufacturing Notes

### Material: Ti-6Al-4V Titanium

| Property | Value |
|----------|-------|
| Density | 4.43 g/cm³ |
| Yield Strength | 880 MPa |
| Ultimate Tensile | 950 MPa |
| Hardness | 36 HRC |

### CNC Machining Process

1. **OP10** - Turn pivot boss (OD and bore)
2. **OP20** - Mill blade profile (tapered shape)
3. **OP30** - Form breakaway notch
4. **OP40** - Drill/tap reach adjuster (optional)
5. **OP50** - Finish ball end tip

### Surface Finish

- **As-machined**: Acceptable for most surfaces
- **Bead blast**: Optional for grip texture on finger contact area
- **Pivot bore**: Smooth finish (Ra 1.6 μm) for smooth rotation

## References

- ProtoLabs CNC Machining Design Guide
- Ti-6Al-4V Material Properties (ASTM F136)
- Husqvarna 701 OEM Specifications
- ProtoLabs DFM Guidelines for Titanium

---

**Design Date:** 2026-04-22  
**Designer:** ProtoLabKB System  
**Version:** 1.0  
**Status:** Ready for Manufacturing Review
