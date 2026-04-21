---
type: intake
part_name: Example Complex Machined Part
process_hint: cnc-machining
material_hint: aluminum-6061
vertical: general
---

# Example Complex Machined Part — Intake Description

## Part Overview

This example part demonstrates several complex features that challenge CNC machining capabilities and require careful DFM review.

## Geometry Description

### Feature 1: Small On-Axis Hole
- **Type**: Through-hole
- **Diameter**: 0.5mm (0.020")
- **Orientation**: On-axis (aligned with main machining axis)
- **Depth**: Through 10mm thick section
- **Aspect ratio**: 20:1 (depth:diameter)

### Feature 2: Deep Narrow Groove
- **Type**: Internal groove/slot
- **Width**: 0.05" (1.27mm)
- **Depth**: 0.9" (22.86mm)
- **Aspect ratio**: 18:1 (depth:width)
- **Orientation**: Internal feature, perpendicular to main axis

### Feature 3: Internal Square Corner
- **Location**: Inside corner of pocket
- **Geometry**: 90° internal corner
- **Current state**: Sharp corner (R0)
- **Issue**: Square internal corners are not machinable with standard end mills

### Feature 4: Recessed Text
- **Type**: Engraved/recessed text
- **Font size**: 8pt
- **Depth**: 0.010" (0.25mm) recessed
- **Location**: Flat surface, visible face
- **Content**: Part number and revision

## Material Specification

- **Material**: Aluminum 6061-T6
- **Stock form**: Bar stock or plate
- **Finish**: As-machined (no secondary finishing specified)

## Tolerance Requirements

- **General tolerances**: ±0.005" (±0.13mm)
- **Critical hole diameter**: ±0.001" (±0.025mm)
- **Groove width**: ±0.002" (±0.05mm)

## Expected DFM Issues

Based on ProtoLabs CNC machining guidelines, this part should flag:

1. **Hole aspect ratio**: 0.5mm hole through 10mm = 20:1 ratio (limit ~10:1 for reliable drilling)
2. **Groove aspect ratio**: 0.05" × 0.9" = 18:1 (deep narrow grooves difficult with standard tools)
3. **Square internal corner**: Not machinable — requires corner radius ≥ 0.5mm (internal) or EDM
4. **Text size**: 8pt text may be too small for clean machining — recommend ≥ 12pt or laser marking

## Use Case

This intake file serves as the **golden test case** for the CNC machining agent. Running `/pl-dfm-review intake/_example-complex-machined.md` should produce a report that correctly identifies all four DFM issues above with specific references to the ProtoLabs "Mastering Complex Features" article.
