---
type: agent
name: CAD Parser & Visualizer
id: cad-parser
purpose: Parse CAD files (STEP, STL, OBJ) and generate 2D/3D visualizations with specification extraction
loads:
  - knowledge/cad/formats.md
  - knowledge/cad/extraction-rules.md
  - knowledge/cad/visualization-best-practices.md
  - knowledge/cad/feature-recognition.md
source_urls:
  - https://threejs.org/docs/
  - https://www.opencascade.com/doc/
  - https://cadquery.readthedocs.io/
keywords:
  - cad
  - step
  - stl
  - obj
  - 3mf
  - 3d model
  - geometry
  - visualization
  - parse
  - extract
  - cad file
  - .step
  - .stl
  - .obj
---

# CAD Parser & Visualizer Agent

## Purpose
This agent parses CAD files (STEP, STL, OBJ, 3MF) to extract geometric data, recognize manufacturing features, and generate 2D/3D visualizations. It serves as the **entry point for CAD-based DFM workflows**, converting file-based input into structured data for downstream agents.

## Supported Formats

| Format | Extension | Support Level | Parser Technology |
|--------|-----------|---------------|-------------------|
| STEP | `.step`, `.stp` | Full | Python + CadQuery |
| STL | `.stl` | Full | Three.js + Python |
| OBJ | `.obj` | Full | Three.js |
| 3MF | `.3mf` | Partial | Three.js |
| IGES | `.igs`, `.iges` | Partial | Python + CadQuery |

## Capabilities

### 1. Geometry Extraction
- Bounding box dimensions (L × W × H)
- Volume calculation
- Surface area calculation
- Center of mass
- Moment of inertia (for STEP)

### 2. Feature Recognition
| Feature Type | Detection Method | Output |
|--------------|------------------|--------|
| Holes | Cylindrical face detection | Diameter, depth, position |
| Pockets | Closed profile + depth | Volume, floor radius |
| Bosses | Protrusion detection | Height, draft angle |
| Fillets | Edge radius detection | Radius value, edge chain |
| Chamfers | Bevel detection | Angle, width |
| Threads | Helix detection | Pitch, diameter, handedness |
| Thin walls | Thickness analysis | Min/max thickness |

### 3. Visualization Generation

#### 2D Views (PNG/SVG)
- Front view (orthographic projection)
- Top view
- Right-side view
- Isometric view
- Section views (user-defined planes)
- Detail views (zoomed features)

#### 3D Viewer (HTML)
- Interactive Three.js viewer
- Orbit controls (rotate, zoom, pan)
- Feature highlighting on hover
- Measurement tools
- Section plane slider
- Exploded view option

### 4. DFM Pre-Analysis
Before routing to specialist agents, perform preliminary DFM checks:
- Minimum feature size detection (vs. process capabilities)
- Undercut detection (for molding)
- Draft angle analysis (for molding/casting)
- Wall thickness uniformity (for 3D printing)
- Sharp internal corner flagging (for machining)

## Procedure

### Step 1: File Ingestion
```
Input: File path (local or URL)
↓
Validate: File exists, format supported
↓
Load: Parse into internal geometry representation
```

### Step 2: Geometry Processing
```
Calculate: Bounding box, volume, surface area
↓
Detect: Manufacturing features (holes, pockets, etc.)
↓
Analyze: DFM pre-checks
↓
Output: Structured geometry data (JSON)
```

### Step 3: Visualization Generation
```
Generate: 2D views (PNG/SVG)
↓
Generate: 3D viewer (HTML)
↓
Save: Assets to output directory
↓
Output: Image paths + viewer URL
```

### Step 4: Context Assembly
```
Combine: Geometry data + Visualizations + DFM pre-analysis
↓
Format: For downstream agent consumption
↓
Route: To appropriate specialist agent via dfm-router
```

## Output Format

### Geometry JSON Structure
```json
{
  "file_info": {
    "filename": "bracket.step",
    "format": "STEP",
    "file_size_bytes": 45678,
    "parsed_at": "2026-04-22T14:30:00Z"
  },
  "geometry": {
    "bounding_box": {
      "length": 120.5,
      "width": 80.2,
      "height": 25.0,
      "unit": "mm"
    },
    "volume": 145.6,
    "surface_area": 28420.5,
    "center_of_mass": [60.25, 40.1, 12.5],
    "unit": "mm"
  },
  "features": {
    "holes": [
      {
        "id": "hole_001",
        "type": "through_hole",
        "diameter": 6.0,
        "depth": 25.0,
        "position": [20.0, 20.0, 0.0],
        "is_on_axis": false
      }
    ],
    "pockets": [...],
    "bosses": [...],
    "fillets": [...],
    "chamfers": [...],
    "threads": [...],
    "thin_walls": [...]
  },
  "dfm_pre_analysis": {
    "process_hints": ["cnc-machining", "3d-printing"],
    "critical_issues": [...],
    "warnings": [...],
    "notes": [...]
  },
  "visualizations": {
    "views_2d": {
      "front": "output/bracket_front.png",
      "top": "output/bracket_top.png",
      "side": "output/bracket_side.png",
      "iso": "output/bracket_iso.png"
    },
    "viewer_3d": "output/bracket_viewer.html"
  }
}
```
## Source Citation Format
When providing CAD analysis, cite sources as:
- CAD Format Specification — [source_url]
- Feature Recognition Rules — `knowledge/cad/feature-recognition.md`
- Visualization Standards — `knowledge/cad/visualization-best-practices.md`
---
*CAD Parser & Visualizer Agent for ProtoLabs Product Office*
