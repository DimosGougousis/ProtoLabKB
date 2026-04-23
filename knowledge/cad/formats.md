---
type: knowledge-article
category: cad
source_url: https://www.cax-if.org/joint_testing_info.html
fetched_at: 2026-04-22
summary: CAD file format specifications for STEP, STL, OBJ, and 3MF formats used in manufacturing analysis.
---

# CAD File Formats

## Overview

CAD files store 3D geometry data in various formats, each with different capabilities for manufacturing analysis. Understanding format characteristics is essential for effective DFM evaluation.

## Format Comparison

| Format | Type | Precision | Features | Manufacturing Use |
|--------|------|-----------|----------|-------------------|
| **STEP** | B-rep (Boundary Representation) | High | Full parametric history, assemblies | Design intent, tolerances, features |
| **STL** | Mesh (Tessellated) | Medium | Triangular facets only | 3D printing, rapid prototyping |
| **OBJ** | Mesh + Materials | Medium | UV mapping, materials | Visualization, rendering |
| **3MF** | Mesh + Metadata | Medium | Color, material, lattice | 3D printing with metadata |
| **IGES** | B-rep (Legacy) | High | Surfaces, curves | Legacy system interchange |

## STEP Format (ISO 10303)

### Characteristics
- **File Extensions**: `.step`, `.stp`
- **Data Model**: Boundary representation (B-rep) with precise geometry
- **Topology**: Solids, shells, faces, loops, edges, vertices
- **Geometry**: NURBS surfaces, curves, points
- **Metadata**: Product structure, tolerances, materials, approvals

### Manufacturing Relevance
| STEP Entity | DFM Application |
|-------------|-----------------|
| `ADVANCED_FACE` | Surface finish requirements |
| `CLOSED_SHELL` | Part volume, enclosed geometry |
| `CYLINDRICAL_SURFACE` | Hole detection, diameter analysis |
| `CONICAL_SURFACE` | Draft angle analysis |
| `PLANE` | Flatness, reference surfaces |
| `EDGE_LOOP` | Feature boundaries |
| `VERTEX_POINT` | Critical point locations |
| `DIMENSIONAL_LOCATION` | Tolerance specifications |

### Parsing Approach
```python
# Using pythonOCC (OpenCASCADE Python bindings)
from OCC.Core.STEPControl import STEPControl_Reader
from OCC.Core.IFSelect import IFSelect_RetDone

reader = STEPControl_Reader()
status = reader.ReadFile('part.step')
if status == IFSelect_RetDone:
    reader.TransferRoots()
    shape = reader.Shape()
    # Extract topology, geometry, features
```

## STL Format (Stereolithography)

### Characteristics
- **File Extensions**: `.stl`
- **Data Model**: Triangular mesh (tessellated surface)
- **Structure**: List of triangular facets with normals and vertices
- **Types**: ASCII (human-readable) or Binary (compact)
- **Precision**: Determined by tessellation density

### File Structure (ASCII)
```
solid part_name
  facet normal nx ny nz
    outer loop
      vertex x1 y1 z1
      vertex x2 y2 z2
      vertex x3 y3 z3
    endloop
  endfacet
  ... (repeated for each triangle)
endsolid part_name
```

### Manufacturing Relevance
| Property | DFM Application |
|----------|-----------------|
| Triangle count | Mesh quality, file size |
| Aspect ratio | Mesh uniformity (affects slicing) |
| Normal consistency | Surface orientation (3D printing) |
| Watertight check | Valid solid for manufacturing |
| Volume | Material estimation |
| Bounding box | Build envelope fit |

### Parsing Approach
```javascript
// Using Three.js
import * as THREE from 'three';
import { STLLoader } from 'three/examples/jsm/loaders/STLLoader';

const loader = new STLLoader();
const geometry = loader.parse(fileBuffer);

// Extract properties
const volume = calculateVolume(geometry);
const boundingBox = new THREE.Box3().setFromObject(mesh);
const surfaceArea = calculateSurfaceArea(geometry);
```

## OBJ Format (Wavefront)

### Characteristics
- **File Extensions**: `.obj`
- **Data Model**: Polygonal mesh with support for curves and surfaces
- **Structure**: Vertex coordinates, texture coordinates, vertex normals, faces
- **Companion File**: `.mtl` (material definitions)
- **Types**: Points, lines, polygons, free-form curves/surfaces

### File Structure
```
# OBJ file
v x1 y1 z1          # Vertex coordinates
v x2 y2 z2
...
vt u1 v1            # Texture coordinates
vt u2 v2
...
vn nx1 ny1 nz1      # Vertex normals
vn nx2 ny2 nz2
...
f v1/vt1/vn1 v2/vt2/vn2 v3/vt3/vn3  # Face definition
...
```

### Manufacturing Relevance
| Property | DFM Application |
|----------|-----------------|
| Vertex groups | Part assemblies, multi-body parts |
| Material groups | Multi-material considerations |
| Smoothing groups | Surface finish requirements |
| Free-form surfaces | Complex geometry analysis |

## Format Selection Guide

### For Design Intent Analysis
**Use STEP** when you need:
- Precise dimensions and tolerances
- Feature recognition (holes, pockets, bosses)
- Manufacturing feature analysis
- Design parameter extraction
- Assembly structure

### For 3D Printing Analysis
**Use STL or 3MF** when you need:
- Build volume check
- Support structure analysis
- Layer height optimization
- Mesh quality assessment
- Print time estimation

### For Visualization
**Use OBJ** when you need:
- High-quality rendering
- Material appearance
- Texture mapping
- Presentation graphics

## Implementation Notes

### Performance Considerations
| Format | Parse Time | Memory Usage | Complexity |
|--------|------------|--------------|------------|
| STEP | Slow | High | High |
| STL | Fast | Medium | Low |
| OBJ | Medium | Medium | Medium |
| 3MF | Fast | Low | Low |

### Recommended Libraries
| Language | STEP | STL/OBJ | 3MF |
|----------|------|---------|-----|
| Python | pythonOCC, CadQuery | numpy-stl, trimesh | python-3mf |
| JavaScript | (limited) | Three.js | Three.js |
| C++ | OpenCASCADE | Assimp | lib3mf |

### Error Handling
Common parsing failures and solutions:

| Error | Cause | Solution |
|-------|-------|----------|
| "Invalid STEP format" | Schema version mismatch | Try different STEP schema (AP203, AP214, AP242) |
| "Non-manifold mesh" | STL has holes or self-intersections | Repair mesh with MeshLab or similar |
| "Missing normals" | OBJ without vn lines | Calculate normals from face geometry |
| "Out of memory" | Large file >100MB | Stream parsing or simplify geometry |
