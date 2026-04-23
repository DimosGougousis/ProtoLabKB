---
type: knowledge-article
category: cad
source_url: https://threejs.org/docs/
fetched_at: 2026-04-22
summary: Best practices for generating 2D and 3D visualizations from CAD geometry for manufacturing analysis and documentation.
---

# CAD Visualization Best Practices

## Overview

This document defines standards for generating high-quality 2D and 3D visualizations from CAD files. These visualizations support DFM analysis, manufacturing documentation, and client communication.

## 2D Visualization Standards

### View Types

| View | Description | Use Case |
|------|-------------|----------|
| **Front** | Primary view showing length and height | Primary dimension reference |
| **Top** | Plan view showing length and width | Feature layout, hole patterns |
| **Right Side** | Side view showing width and height | Depth features, profiles |
| **Isometric** | 3D view at 30° angles | Overall form understanding |
| **Section A-A** | Cut through specific plane | Internal features |
| **Detail A** | Magnified view of feature | Small feature clarity |

### Rendering Settings

```javascript
// Three.js orthographic camera setup for 2D views
const viewSettings = {
  front: {
    cameraPosition: [0, -100, 0],  // Looking along -Y
    up: [0, 0, 1],
    projection: 'orthographic'
  },
  top: {
    cameraPosition: [0, 0, 100],   // Looking along +Z
    up: [0, 1, 0],
    projection: 'orthographic'
  },
  side: {
    cameraPosition: [100, 0, 0],   // Looking along +X
    up: [0, 0, 1],
    projection: 'orthographic'
  },
  iso: {
    cameraPosition: [100, -100, 100],
    up: [0, 0, 1],
    projection: 'orthographic'
  }
};

// Rendering configuration
const renderConfig = {
  width: 1920,           // Output image width
  height: 1080,          // Output image height
  backgroundColor: 0xffffff,  // White background
  antialias: true,
  shadowMap: true,
  
  // Lighting
  lights: {
    ambient: { intensity: 0.6 },
    directional: [
      { position: [10, 10, 10], intensity: 0.8 },
      { position: [-10, -10, 5], intensity: 0.4 }  // Fill light
    ]
  },
  
  // Material
  material: {
    color: 0xcccccc,      // Light gray
    metalness: 0.3,
    roughness: 0.4,
    transparent: false
  },
  
  // Edges
  edges: {
    enabled: true,
    color: 0x333333,      // Dark gray
    linewidth: 1
  }
};
```

### Output Specifications

| Property | Value | Notes |
|----------|-------|-------|
| Resolution | 1920×1080 | Full HD |
| Format | PNG | Lossless compression |
| Color depth | 24-bit | RGB |
| Background | White (#FFFFFF) | Clean documentation |
| Viewport padding | 10% | Part doesn't touch edges |
| Scale | Fit to view | Maintain aspect ratio |

### Dimension Annotation (Optional)

```javascript
// Add dimension lines to 2D views
const dimensionStyle = {
  font: 'Arial',
  fontSize: 24,
  textColor: 0x000000,
  lineColor: 0x000000,
  extensionLineColor: 0x666666,
  arrowSize: 10,
  precision: 2  // Decimal places
};
```

## 3D Visualization Standards

### Interactive Viewer Specifications

```html
<!-- 3D Viewer HTML Template -->
<!DOCTYPE html>
<html>
<head>
  <title>CAD Viewer - {{part_name}}</title>
  <style>
    body { margin: 0; overflow: hidden; }
    #canvas-container { width: 100vw; height: 100vh; }
    #info-panel {
      position: absolute;
      top: 10px;
      left: 10px;
      background: rgba(255,255,255,0.9);
      padding: 15px;
      border-radius: 5px;
      font-family: Arial, sans-serif;
    }
  </style>
</head>
<body>
  <div id="canvas-container"></div>
  <div id="info-panel">
    <h3>{{part_name}}</h3>
    <p>Dimensions: {{dimensions}}</p>
    <p>Volume: {{volume}} cm³</p>
    <p>Features: {{feature_count}}</p>
  </div>
  
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
  <script>
    // Three.js setup
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0xf0f0f0);
    
    const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.set(50, 50, 50);
    
    const renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.shadowMap.enabled = true;
    document.getElementById('canvas-container').appendChild(renderer.domElement);
    
    // Controls
    const controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.05;
    
    // Lighting
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
    scene.add(ambientLight);
    
    const dirLight = new THREE.DirectionalLight(0xffffff, 0.8);
    dirLight.position.set(10, 10, 10);
    dirLight.castShadow = true;
    scene.add(dirLight);
    
    // Load geometry (placeholder - actual implementation would load from file)
    // const geometry = loadGeometryFromFile('{{geometry_file}}');
    
    // Animation loop
    function animate() {
      requestAnimationFrame(animate);
      controls.update();
      renderer.render(scene, camera);
    }
    animate();
    
    // Handle resize
    window.addEventListener('resize', () => {
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight);
    });
  </script>
</body>
</html>
```

### Viewer Controls

| Control | Action | Purpose |
|---------|--------|---------|
| **Left Click + Drag** | Rotate | View from different angles |
| **Right Click + Drag** | Pan | Move view without rotation |
| **Scroll** | Zoom | Magnify details |
| **Double Click** | Center on point | Focus on specific feature |
| **Hover** | Highlight feature | Identify geometry elements |

### Viewer Features

```javascript
// Feature highlighting
function highlightFeature(featureId) {
  const feature = findFeatureById(featureId);
  if (feature) {
    feature.material.emissive.setHex(0xff0000);
    feature.material.emissiveIntensity = 0.5;
  }
}

// Section view (clipping plane)
function createSectionPlane(normal, distance) {
  const plane = new THREE.Plane(normal, distance);
  renderer.clippingPlanes = [plane];
}

// Measurement tool
function measureDistance(point1, point2) {
  return point1.distanceTo(point2);
}

// Exploded view
function createExplodedView(explosionFactor) {
  // Move parts away from center based on explosionFactor
  parts.forEach(part => {
    const direction = part.position.clone().normalize();
    part.position.add(direction.multiplyScalar(explosionFactor));
  });
}
```

## Source Citation Format

When providing visualization guidance, cite sources as:
- Three.js Documentation — https://threejs.org/docs/
- OpenCASCADE Documentation — https://www.opencascade.com/doc/
- CAD Visualization Standards — `knowledge/cad/visualization-best-practices.md`

---
*CAD Visualization Best Practices for ProtoLabs Product Office*
