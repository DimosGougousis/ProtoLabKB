---
type: knowledge-index
folder: cad
description: CAD file formats, parsing rules, and visualization standards for manufacturing analysis
---

# CAD Knowledge Base Index

## Articles

| Article | File | Source URL | Description |
|---------|------|------------|-------------|
| CAD Formats | `formats.md` | https://www.cax-if.org/joint_testing_info.html | STEP, STL, OBJ, 3MF format specifications |
| Feature Extraction Rules | `extraction-rules.md` | Internal | Rules for extracting DFM-relevant features from CAD |
| Feature Recognition | `feature-recognition.md` | Internal | Pattern matching for holes, pockets, bosses, etc. |
| Visualization Best Practices | `visualization-best-practices.md` | Internal | Standards for 2D/3D rendering |

## External Resources

- [Three.js Documentation](https://threejs.org/docs/)
- [OpenCASCADE Documentation](https://www.opencascade.com/doc/)
- [CadQuery Documentation](https://cadquery.readthedocs.io/)
- [STEP File Format (ISO 10303)](https://www.iso.org/standard/63141.html)
- [STL Specification](https://www.fabbers.com/tech/STL_Format.html)

## Format Support Matrix

| Format | Read | Write | 2D Views | 3D Viewer | Feature Extraction |
|--------|------|-------|----------|-----------|-------------------|
| STEP (.step, .stp) | ✅ | ❌ | ✅ | ✅ | Full B-rep |
| STL (.stl) | ✅ | ❌ | ✅ | ✅ | Mesh analysis |
| OBJ (.obj) | ✅ | ❌ | ✅ | ✅ | Mesh + materials |
| 3MF (.3mf) | ✅ | ❌ | ✅ | ✅ | Mesh + metadata |
| IGES (.igs, .iges) | ⚠️ Partial | ❌ | ✅ | ✅ | Limited B-rep |

Legend: ✅ Full support | ⚠️ Partial | ❌ Not supported
