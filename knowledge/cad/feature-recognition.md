---
type: knowledge-article
category: cad
source_url: internal
fetched_at: 2026-04-22
summary: Pattern matching algorithms for recognizing manufacturing features in CAD geometry - holes, pockets, bosses, fillets, chamfers, threads, and thin walls.
---

# Feature Recognition Patterns

## Overview

Feature recognition transforms raw CAD geometry into manufacturing semantics. This document defines the pattern matching algorithms used to identify common manufacturing features.

## 1. Hole Recognition

### Pattern Definition
```
HOLE := CYLINDRICAL_SURFACE + 
        (THROUGH_HOLE | BLIND_HOLE) +
        (SIMPLE | COUNTERBORE | COUNTERSINK | THREADED)
```

### Detection Algorithm
```python
def detect_holes(brep_geometry):
    holes = []
    
    for face in brep_geometry.faces:
        # Check if face is cylindrical
        if is_cylindrical_surface(face):
            cylinder = extract_cylinder_params(face)
            
            # Determine hole type
            hole_type = classify_hole_type(face, brep_geometry)
            
            # Measure depth
            depth = measure_hole_depth(face, brep_geometry)
            
            # Check for threading
            is_threaded = detect_threading(face, brep_geometry)
            
            holes.append({
                'id': generate_id(),
                'diameter': cylinder.diameter,
                'depth': depth,
                'type': hole_type,
                'is_threaded': is_threaded,
                'position': cylinder.axis.origin,
                'axis_direction': cylinder.axis.direction,
                'is_through': hole_type == 'through_hole'
            })
    
    return holes

def classify_hole_type(cylindrical_face, geometry):
    # Check if hole goes through entire part
    if is_through_hole(cylindrical_face, geometry):
        return 'through_hole'
    
    # Check for counterbore
    if has_counterbore(cylindrical_face, geometry):
        return 'counterbore'
    
    # Check for countersink
    if has_countersink(cylindrical_face, geometry):
        return 'countersink'
    
    return 'blind_hole'
```

### Hole Subtypes

| Subtype | Pattern | Manufacturing Implication |
|---------|---------|----------------------------|
| **Simple Through** | Cylinder through entire part | Standard drilling |
| **Simple Blind** | Cylinder with flat bottom | Drill + end mill for bottom |
| **Counterbore** | Large diameter + small diameter | Counterbore tool or mill |
| **Countersink** | Conical top + cylindrical | Countersink tool |
| **Tapered** | Conical hole | Tapered reamer or mill |
| **Threaded** | Helical surface on cylinder | Tap (internal) or die (external) |

### Critical Measurements

```python
# Aspect ratio check for deep holes
def check_aspect_ratio(hole):
    ratio = hole['depth'] / hole['diameter']
    
    if ratio > 20:
        return 'CRITICAL', 'Aspect ratio > 20:1 requires gun drilling'
    elif ratio > 10:
        return 'WARNING', 'Aspect ratio > 10:1 requires peck drilling'
    elif ratio > 3:
        return 'NOTE', 'Standard drilling with coolant recommended'
    else:
        return 'OK', 'Standard drilling'

# Minimum hole size check
def check_minimum_size(hole, process):
    min_sizes = {
        'cnc-machining': 0.5,  # mm
        '3d-printing-sla': 0.3,
        '3d-printing-sls': 0.8,
        '3d-printing-fdm': 1.0
    }
    
    min_size = min_sizes.get(process, 0.5)
    
    if hole['diameter'] < min_size:
        return 'CRITICAL', f"Hole diameter {hole['diameter']}mm below {process} minimum {min_size}mm"
    return 'OK', 'Within process capability'
```

## 2. Pocket Recognition

### Pattern Definition
```
POCKET := CLOSED_BOUNDARY + 
          DEPTH_EXTENT +
          (RECTANGULAR | CIRCULAR | IRREGULAR) +
          (FLAT_BOTTOM | ROUNDED_BOTTOM | TAPERED_BOTTOM) +
          (VERTICAL_WALLS | DRAFTED_WALLS)
```

### Detection Algorithm
```python
def detect_pockets(brep_geometry):
    pockets = []
    
    for face in brep_geometry.faces:
        # Check if face is planar and accessible
        if is_planar_face(face) and is_accessible(face):
            # Find closed boundary
            boundary = find_closed_boundary(face)
            
            if boundary:
                # Measure pocket properties
                pocket = analyze_pocket(face, boundary, brep_geometry)
                
                if pocket['depth'] > 0:  # It's a pocket, not just a face
                    pockets.append(pocket)
    
    return pockets

def analyze_pocket(bottom_face, boundary, geometry):
    # Measure depth
    depth = measure_pocket_depth(bottom_face, geometry)
    
    # Analyze walls
    walls = extract_pocket_walls(bottom_face, boundary, geometry)
    
    # Check for draft
    draft_angles = [calculate_draft_angle(wall) for wall in walls]
    
    # Check bottom type
    bottom_type = classify_bottom(bottom_face)
    
    # Calculate corner radii
    corner_radii = measure_corner_radii(bottom_face, boundary)
    
    return {
        'id': generate_id(),
        'depth': depth,
        'area': calculate_area(bottom_face),
        'perimeter': calculate_perimeter(boundary),
        'wall_count': len(walls),
        'draft_angles': draft_angles,
        'min_draft': min(draft_angles) if draft_angles else 0,
        'max_draft': max(draft_angles) if draft_angles else 0,
        'bottom_type': bottom_type,
        'corner_radii': corner_radii,
        'min_corner_radius': min(corner_radii) if corner_radii else 0,
        'is_through': depth >= geometry.thickness,
        'complexity_score': calculate_complexity(depth, len(walls), len(corner_radii))
    }
```

### Pocket Types and Manufacturing Implications

| Type | Pattern | Manufacturing Method | Complexity |
|------|---------|---------------------|------------|
| **Open pocket** | Open on one side | Side milling, simple | Low |
| **Closed pocket** | Fully enclosed | Plunge rough + finish | Medium |
| **Island pocket** | Contains boss in center | Complex tool paths | High |
| **Stepped pocket** | Multiple depths | Multiple operations | High |
| **Tapered pocket** | Drafted walls | Tapered tool or 3D surfacing | Medium |
| **Circular pocket** | Round profile | Circular interpolation | Low |
| **Rectangular pocket** | Square/rectangular profile | Linear interpolation | Low |
| **Irregular pocket** | Complex profile | Full contouring | Medium |

### DFM Rules for Pockets

```python
# Critical pocket checks
def check_pocket_manufacturability(pocket, process):
    issues = []
    
    # Depth-to-width ratio
    width = math.sqrt(pocket['area'])
    aspect_ratio = pocket['depth'] / width
    
    if aspect_ratio > 3:
        issues.append({
            'severity': 'CRITICAL',
            'issue': 'Deep pocket',
            'message': f"Aspect ratio {aspect_ratio:.1f}:1 exceeds 3:1 limit",
            'recommendation': 'Consider through-pocket or multiple pockets'
        })
    elif aspect_ratio > 2:
        issues.append({
            'severity': 'WARNING',
            'issue': 'Moderately deep pocket',
            'message': f"Aspect ratio {aspect_ratio:.1f}:1 may require extended reach tools",
            'recommendation': 'Verify tool reach and rigidity'
        })
    
    # Corner radius
    if pocket['min_corner_radius'] < 0.5:
        issues.append({
            'severity': 'WARNING',
            'issue': 'Sharp internal corner',
            'message': f"Corner radius {pocket['min_corner_radius']}mm is very small",
            'recommendation': 'Increase to 0.5mm minimum or specify EDM'
        })
    
    # Draft angle (for molding)
    if process == 'injection-molding':
        min_draft = pocket['min_draft']
        if min_draft < 0.5:
            issues.append({
                'severity': 'CRITICAL',
                'issue': 'Insufficient draft',
                'message': f"Draft angle {min_draft}° below 0.5° minimum",
                'recommendation': 'Add 1-2° draft for mold release'
            })
    
    return issues
```

## 3. Boss Recognition

### Pattern Definition
```
BOSS := PROTRUSION_FROM_BASE +
        (CYLINDRICAL | PRISMATIC) +
        HEIGHT_SIGNIFICANT +
        (FLAT_TOP | RADIUSED_TOP | SPHERICAL_TOP)
```

### Detection Algorithm
```python
def detect_bosses(brep_geometry):
    bosses = []
    
    for face in brep_geometry.faces:
        # Find protrusions
        if is_protrusion(face, brep_geometry):
            # Measure boss properties
            boss = analyze_boss(face, brep_geometry)
            
            # Only significant protrusions
            if boss['height'] > 2.0:  # mm threshold
                bosses.append(boss)
    
    return bosses

def analyze_boss(protrusion_face, geometry):
    # Measure height from base
    height = measure_protrusion_height(protrusion_face, geometry)
    
    # Measure diameter/width at base
    base_dimensions = measure_base(protrusion_face, geometry)
    
    # Analyze top face
    top_face = find_top_face(protrusion_face, geometry)
    top_type = classify_top(top_face)
    
    # Check for draft
    draft_angle = calculate_draft(protrusion_face, geometry)
    
    # Check for holes in boss (common for mounting)
    has_hole = detect_center_hole(protrusion_face, geometry)
    
    return {
        'id': generate_id(),
        'height': height,
        'base_diameter': base_dimensions['diameter'],
        'base_width': base_dimensions.get('width'),
        'top_type': top_type,
        'draft_angle': draft_angle,
        'has_center_hole': has_hole,
        'aspect_ratio': height / base_dimensions['diameter'],
        'is_circular': base_dimensions.get('is_circular', True)
    }
```

### DFM Rules for Bosses

```python
def check_boss_manufacturability(boss, process):
    issues = []
    
    # Aspect ratio (height to diameter)
    if boss['aspect_ratio'] > 3:
        issues.append({
            'severity': 'WARNING',
            'issue': 'Tall boss',
            'message': f"Aspect ratio {boss['aspect_ratio']:.1f}:1 may cause vibration",
            'recommendation': 'Add ribs or reduce height'
        })
    
    # Draft angle for molding
    if process == 'injection-molding':
        if boss['draft_angle'] < 0.5:
            issues.append({
                'severity': 'CRITICAL',
                'issue': 'Insufficient draft on boss',
                'message': f"Draft angle {boss['draft_angle']}° below 0.5° minimum",
                'recommendation': 'Add 1-2° draft for mold release'
            })
        
        # Wall thickness at boss base
        if boss.get('base_wall_thickness', 1.0) < 0.5:
            issues.append({
                'severity': 'WARNING',
                'issue': 'Thin wall at boss base',
                'message': 'Boss base may be too thin for molding',
                'recommendation': 'Increase wall thickness or add gussets'
            })
    
    return issues
```

## 4. Thread Recognition

### Pattern Definition
```
THREAD := HELICAL_SURFACE +
          CONSTANT_PITCH +
          (INTERNAL | EXTERNAL) +
          (METRIC | UNIFIED | ACME | NPT | etc.)
```

### Detection Algorithm
```python
def detect_threads(brep_geometry):
    threads = []
    
    for face in brep_geometry.faces:
        # Check for helical surface
        if is_helical_surface(face):
            # Extract thread parameters
            thread = analyze_thread(face, brep_geometry)
            
            if thread:
                threads.append(thread)
    
    return threads

def analyze_thread(helical_face, geometry):
    # Extract helix parameters
    helix = extract_helix_params(helical_face)
    
    # Calculate pitch
    pitch = calculate_pitch(helix)
    
    # Determine internal/external
    is_internal = classify_thread_type(helical_face, geometry)
    
    # Identify standard
    standard = identify_thread_standard(
        major_diameter=helix.diameter,
        pitch=pitch,
        is_internal=is_internal
    )
    
    # Measure length
    length = measure_thread_length(helical_face)
    
    return {
        'id': generate_id(),
        'major_diameter': helix.diameter,
        'pitch': pitch,
        'threads_per_inch': 25.4 / pitch if pitch > 0 else 0,
        'is_internal': is_internal,
        'standard': standard,
        'length': length,
        'handedness': helix.handedness,  # 'right' or 'left'
        'class': infer_thread_class(pitch, helix.diameter)
    }
```

### Thread Standards Reference

| Standard | Application | Identification |
|----------|-------------|----------------|
| **Metric (M)** | International | M{diameter}×{pitch} (e.g., M6×1) |
| **Unified Coarse (UNC)** | US general | {size}-UNC (e.g., 1/4-20) |
| **Unified Fine (UNF)** | US precision | {size}-UNF (e.g., 1/4-28) |
| **NPT** | Pipe threads | NPT {size} (e.g., NPT 1/8) |
| **BSPT** | British pipe | R{size} (e.g., R1/4) |
| **ACME** | Power transmission | {size}-ACME |

### DFM Rules for Threads

```python
def check_thread_manufacturability(thread, process):
    issues = []
    
    # Standard thread check
    if thread['standard'] == 'non_standard':
        issues.append({
            'severity': 'WARNING',
            'issue': 'Non-standard thread',
            'message': f"Custom {thread['pitch']}mm pitch on M{thread['major_diameter']}",
            'recommendation': 'Use standard thread for lower cost'
        })
    
    # Small thread check
    if thread['major_diameter'] < 3.0:  # M3 or #5
        issues.append({
            'severity': 'WARNING',
            'issue': 'Small thread',
            'message': f"M{thread['major_diameter']} may be difficult to machine",
            'recommendation': 'Consider thread forming or larger size'
        })
    
    # Deep thread check
    if thread['length'] > 3 * thread['major_diameter']:
        issues.append({
            'severity': 'WARNING',
            'issue': 'Deep thread',
            'message': f"Thread length {thread['length']}mm exceeds 3× diameter",
            'recommendation': 'Use thread relief or reduce engagement length'
        })
    
    # Process-specific checks
    if process == 'cnc-machining':
        # Check for thread milling vs tapping
        if thread['is_internal'] and thread['length'] > 20:
            issues.append({
                'severity': 'NOTE',
                'issue': 'Long internal thread',
                'message': 'Consider thread milling instead of tapping',
                'recommendation': 'Thread mill for better control and chip evacuation'
            })
    
    elif process == 'injection-molding':
        # Threads in molded parts
        if thread['is_internal']:
            issues.append({
                'severity': 'CRITICAL',
                'issue': 'Internal thread in molded part',
                'message': 'Internal threads require collapsible cores or secondary operation',
                'recommendation': 'Consider external thread on mating part, or plan for unscrewing mechanism'
            })
    
    return issues
```

## 5. Thin Wall Detection

### Pattern Definition
```
THIN_WALL := SURFACE_PAIR +
             SMALL_SEPARATION +
             PARALLEL_OR_NEAR_PARALLEL +
             EXTENDED_AREA
```

### Detection Algorithm
```python
def detect_thin_walls(brep_geometry, threshold=1.0):
    thin_walls = []
    
    # For B-rep: analyze face pairs
    faces = brep_geometry.faces
    
    for i, face1 in enumerate(faces):
        for face2 in faces[i+1:]:
            # Check if faces are parallel and close
            if are_parallel(face1, face2):
                distance = calculate_min_distance(face1, face2)
                
                if distance < threshold:
                    # Calculate wall area
                    area = calculate_overlap_area(face1, face2)
                    
                    if area > 100:  # Minimum area threshold
                        thin_walls.append({
                            'id': generate_id(),
                            'thickness': distance,
                            'area': area,
                            'face1_id': face1.id,
                            'face2_id': face2.id,
                            'is_vertical': is_vertical_wall(face1, face2),
                            'location': calculate_centroid(face1, face2)
                        })
    
    return thin_walls

# For mesh-based formats (STL/OBJ)
def detect_thin_walls_mesh(mesh_geometry, threshold=1.0):
    thin_walls = []
    
    # Use ray casting to find thin sections
    vertices = mesh_geometry.vertices
    
    for vertex in vertices:
        # Cast ray in normal direction
        ray = create_ray(vertex, vertex.normal)
        intersection = mesh_geometry.intersect(ray)
        
        if intersection and intersection.distance < threshold:
            thin_walls.append({
                'id': generate_id(),
                'thickness': intersection.distance,
                'location': vertex.position,
                'normal': vertex.normal
            })
    
    return thin_walls
```

### DFM Rules for Thin Walls

```python
def check_thin_wall_manufacturability(thin_walls, process, material):
    issues = []
    
    # Process-specific minimum thickness
    min_thickness = {
        'cnc-machining': {
            'aluminum': 0.5,
            'steel': 0.8,
            'titanium': 1.0,
            'plastic': 1.0
        },
        'injection-molding': {
            'abs': 0.5,
            'polycarbonate': 0.8,
            'nylon': 0.5,
            'polypropylene': 0.6
        },
        '3d-printing-sla': {
            'standard': 0.3,
            'tough': 0.5
        },
        '3d-printing-sls': {
            'nylon': 0.8,
            'tpu': 1.0
        },
        '3d-printing-fdm': {
            'pla': 1.0,
            'abs': 1.2,
            'nylon': 0.8
        }
    }
    
    process_mins = min_thickness.get(process, {})
    material_min = process_mins.get(material, process_mins.get('default', 0.5))
    
    for wall in thin_walls:
        thickness = wall['thickness']
        
        if thickness < material_min * 0.5:
            issues.append({
                'severity': 'CRITICAL',
                'feature': 'thin_wall',
                'location': wall['location'],
                'thickness': thickness,
                'message': f"Wall thickness {thickness:.2f}mm is critically thin",
                'recommendation': f"Increase to at least {material_min}mm for {process}"
            })
        elif thickness < material_min:
            issues.append({
                'severity': 'WARNING',
                'feature': 'thin_wall',
                'location': wall['location'],
                'thickness': thickness,
                'message': f"Wall thickness {thickness:.2f}mm below recommended {material_min}mm",
                'recommendation': 'Consider thickening or verify process capability'
            })
    
    return issues
```

## Feature Relationship Analysis

### Feature Interactions

| Feature Combination | Interaction | DFM Impact |
|---------------------|-------------|------------|
| Hole + Thin wall | Hole near thin wall | Wall distortion during machining |
| Pocket + Boss | Boss in pocket | Reduced tool access |
| Thread + Hole | Threaded hole | Tap breakage risk |
| Fillet + Sharp corner | Adjacent features | Stress concentration |
| Multiple holes | Hole pattern | Tolerance stack-up |

### Proximity Analysis
```python
def analyze_feature_proximity(features, threshold=2.0):
    """Check if features are too close together"""
    interactions = []
    
    for i, feat1 in enumerate(features):
        for feat2 in features[i+1:]:
            distance = calculate_distance(feat1, feat2)
            
            if distance < threshold:
                interactions.append({
                    'feature_1': feat1['id'],
                    'feature_2': feat2['id'],
                    'distance': distance,
                    'type': classify_interaction(feat1, feat2),
                    'severity': assess_interaction_risk(feat1, feat2, distance)
                })
    
    return interactions
```

## Source Citation Format

When providing feature recognition results, cite sources as:
- Feature Recognition Rules — `knowledge/cad/feature-recognition.md`
- Extraction Methodology — `knowledge/cad/extraction-rules.md`
- DFM Guidelines — `knowledge/{process}/{article}.md`

---
*CAD Feature Recognition Patterns for ProtoLabs Product Office*
