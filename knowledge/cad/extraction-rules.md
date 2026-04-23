---
type: knowledge-article
category: cad
source_url: internal
fetched_at: 2026-04-22
summary: Rules for extracting Design for Manufacturing (DFM) relevant features and specifications from CAD geometry.
---

# CAD Feature Extraction Rules for DFM

## Overview

This document defines the rules for extracting manufacturing-relevant features from CAD files. These rules enable automated DFM analysis by identifying features that impact manufacturability, cost, and quality.

## Extraction Pipeline

```
CAD File → Parse Geometry → Identify Features → Measure Properties → DFM Analysis
```

## Feature Categories

### 1. Holes

#### Detection Criteria
A hole is detected when:
- Cylindrical surface with 360° revolution
- Axis is straight (linear)
- Diameter is consistent along axis
- One or both ends are open (not capped)

#### Extracted Properties
| Property | Method | Unit | DFM Relevance |
|----------|--------|------|---------------|
| Diameter | Measure cylindrical surface | mm | Tool size, tolerance |
| Depth | Measure along axis | mm | Aspect ratio, drill reach |
| Position | Coordinates relative to origin | mm | Tolerance stack-up |
| Axis direction | Vector [x, y, z] | - | Machining access |
| Bottom type | Flat, conical, spherical | - | Drill point match |
| Tolerance | From STEP PMI if available | mm | Quality requirement |

#### DFM Rules for Holes

| Issue | Rule | Check | Source |
|-------|------|-------|--------|
| Deep hole | Depth > 3× diameter | Flag for gun drilling | CNC KB |
| Small hole | Diameter < 1mm | Flag for micro-machining | CNC KB |
| Off-axis | Hole axis not aligned with setup | Flag for 4th/5th axis | CNC KB |
| Tight tolerance | Tolerance < 0.05mm | Flag for grinding required | CNC KB |

### 2. Pockets (Internal Cavities)

#### Detection Criteria
A pocket is detected when:
- Closed boundary of edges on a face
- Depth extends inward from face
- Bottom surface is parallel or angled to top face
- Walls may be vertical or drafted

#### Types of Pockets
| Type | Description | Manufacturing Method |
|------|-------------|---------------------|
| Closed pocket | Fully enclosed bottom | End mill, plunge rough + finish |
| Open pocket | Open on one or more sides | End mill, side milling |
| Island pocket | Contains protrusion in center | Complex tool paths |
| Tapered pocket | Drafted walls | Tapered end mill or 3D surfacing |

#### Extracted Properties
| Property | Method | Unit | DFM Relevance |
|----------|--------|------|---------------|
| Pocket depth | Measure from top to bottom | mm | Tool length, aspect ratio |
| Corner radius | Measure internal corner | mm | Tool size constraint |
| Floor radius | Measure bottom fillet | mm | Tool geometry |
| Draft angle | Calculate wall taper | degrees | Moldability |
| Surface finish | From STEP PMI | Ra μm | Machining strategy |
| Tolerance | From STEP PMI | mm | Inspection method |

#### DFM Rules for Pockets

| Issue | Rule | Check | Source |
|-------|------|-------|--------|
| Deep pocket | Depth > 2× tool diameter | Flag for extended reach tool | CNC KB |
| Sharp corner | Internal radius < 0.5mm | Flag for EDM or corner relief | CNC KB |
| Thin floor | Floor thickness < 1mm | Flag for deflection risk | CNC KB |
| Tight tolerance | Pocket tolerance < ±0.05mm | Flag for finish machining | CNC KB |

### 3. Bosses (Protrusions)

#### Detection Criteria
A boss is detected when:
- Protrusion from main body surface
- Typically cylindrical or prismatic
- Height is significant relative to base

#### Extracted Properties
| Property | Method | Unit | DFM Relevance |
|----------|--------|------|---------------|
| Boss height | Measure from base to top | mm | Machining access |
| Boss diameter | Measure at base | mm | Tool size |
| Draft angle | Calculate taper | degrees | Moldability |
| Position | Coordinates | mm | Tolerance stack |
| Top type | Flat, radiused, spherical | - | Finish requirement |

#### DFM Rules for Bosses

| Issue | Rule | Check | Source |
|-------|------|-------|--------|
| Tall boss | Height > 3× diameter | Flag for vibration risk | CNC KB |
| Thin boss | Wall thickness < 1mm | Flag for molding defect | IM KB |
| No draft | Draft angle < 0.5° | Flag for mold release issue | IM KB |

### 4. Fillets and Radii

#### Detection Criteria
- Rounded internal or external edges
- Constant radius along edge

#### Extracted Properties
| Property | Method | Unit | DFM Relevance |
|----------|--------|------|---------------|
| Radius value | Measure curvature | mm | Tool size, stress concentration |
| Edge length | Measure along curve | mm | Machining time |
| Edge type | Internal (fillet) or external (round) | - | Tool access |
| Tangent continuity | G1 or G2 | - | Surface quality |

#### DFM Rules for Fillets

| Issue | Rule | Check | Source |
|-------|------|-------|--------|
| Sharp internal | Radius < 0.5mm | Flag for stress riser | CNC KB |
| Large radius | Radius > 10mm | Flag for special tool | CNC KB |
| Inconsistent | Varying radii on similar features | Flag for design standardization | CNC KB |

### 5. Chamfers

#### Detection Criteria
- Beveled edges at constant angle
- Typically 45° but can vary

#### Extracted Properties
| Property | Method | Unit | DFM Relevance |
|----------|--------|------|---------------|
| Chamfer width | Measure along face | mm | Tool size |
| Chamfer angle | Measure from base | degrees | Tool angle |
| Edge length | Total length | mm | Machining time |

#### DFM Rules for Chamfers

| Issue | Rule | Check | Source |
|-------|------|-------|--------|
| Small chamfer | Width < 0.5mm | Flag for deburring | CNC KB |
| Inconsistent angle | Non-standard angle | Flag for tool change | CNC KB |

### 6. Threads

#### Detection Criteria
- Helical surface on cylindrical feature
- Internal (hole) or external (boss)

#### Extracted Properties
| Property | Method | Unit | DFM Relevance |
|----------|--------|------|---------------|
| Thread diameter | Major or minor diameter | mm | Tap/die size |
| Thread pitch | Distance between threads | mm | Thread class |
| Thread length | Engaged length | mm | Tool reach |
| Thread standard | UNC, UNF, Metric, etc. | - | Tool selection |
| Handedness | Right or left hand | - | Tool rotation |
| Thread class | 2B, 3B, etc. | - | Tolerance |

#### DFM Rules for Threads

| Issue | Rule | Check | Source |
|-------|------|-------|--------|
| Small thread | Diameter < M3 (#5) | Flag for thread forming | CNC KB |
| Deep thread | Length > 3× diameter | Flag for tap breakage | CNC KB |
| Blind hole | No through-hole | Flag for bottom tap | CNC KB |
| External thread | On boss | Flag for die access | CNC KB |

### 7. Thin Walls

#### Detection Criteria
- Wall thickness below threshold
- Uniform or varying thickness

#### Extracted Properties
| Property | Method | Unit | DFM Relevance |
|----------|--------|------|---------------|
| Minimum thickness | Thinnest section | mm | Process capability |
| Maximum thickness | Thickest section | mm | Cooling/warping |
| Thickness ratio | Max/min | - | Uniformity |
| Wall area | Total thin wall area | mm² | Deflection risk |

#### DFM Rules for Thin Walls

| Issue | Rule | Check | Source |
|-------|------|-------|--------|
| Too thin (CNC) | Thickness < 0.5mm | Flag for vibration | CNC KB |
| Too thin (IM) | Thickness < 0.5mm | Flag for filling | IM KB |
| Too thin (3DP) | Thickness < 0.8mm | Flag for fragility | 3DP KB |
| Non-uniform | Ratio > 2:1 | Flag for warping | IM KB |

## Extraction Pipeline

### Step 1: File Loading
```python
def load_cad_file(filepath):
    ext = Path(filepath).suffix.lower()
    
    if ext in ['.step', '.stp']:
        return load_step(filepath)
    elif ext == '.stl':
        return load_stl(filepath)
    elif ext == '.obj':
        return load_obj(filepath)
    elif ext == '.3mf':
        return load_3mf(filepath)
    else:
        raise ValueError(f"Unsupported format: {ext}")
```

### Step 2: Geometry Normalization
Convert all formats to internal representation:
- **B-rep**: For STEP (faces, edges, topology)
- **Mesh**: For STL/OBJ (vertices, triangles)
- **Hybrid**: For 3MF (mesh + metadata)

### Step 3: Feature Detection
Apply recognition algorithms:
```python
def detect_features(geometry):
    features = {
        'holes': detect_holes(geometry),
        'pockets': detect_pockets(geometry),
        'bosses': detect_bosses(geometry),
        'fillets': detect_fillets(geometry),
        'chamfers': detect_chamfers(geometry),
        'threads': detect_threads(geometry),
        'thin_walls': detect_thin_walls(geometry)
    }
    return features
```

### Step 4: DFM Pre-Analysis
Run preliminary checks before routing:
```python
def pre_dfm_analysis(geometry, features):
    issues = []
    
    # Check minimum feature sizes
    for hole in features['holes']:
        if hole['diameter'] < 1.0:
            issues.append({
                'type': 'warning',
                'feature': 'hole',
                'message': f"Hole diameter {hole['diameter']}mm may require special tooling"
            })
    
    # Check thin walls
    for wall in features['thin_walls']:
        if wall['thickness'] < 0.5:
            issues.append({
                'type': 'critical',
                'feature': 'thin_wall',
                'message': f"Wall thickness {wall['thickness']}mm below minimum for most processes"
            })
    
    return issues
```

### Step 5: Visualization Generation
```python
def generate_visualizations(geometry, output_dir):
    visualizations = {}
    
    # 2D views
    visualizations['front'] = render_orthographic(geometry, 'front', output_dir)
    visualizations['top'] = render_orthographic(geometry, 'top', output_dir)
    visualizations['side'] = render_orthographic(geometry, 'side', output_dir)
    visualizations['iso'] = render_isometric(geometry, output_dir)
    
    # 3D viewer
    visualizations['viewer'] = generate_three_js_viewer(geometry, output_dir)
    
    return visualizations
```

## Source Citation Format

When providing CAD analysis, cite sources as:
- CAD Format Specification — [source_url]
- Feature Recognition Rules — `knowledge/cad/feature-recognition.md`
- Visualization Standards — `knowledge/cad/visualization-best-practices.md`

---
*CAD Feature Extraction Rules for ProtoLabs Product Office*
