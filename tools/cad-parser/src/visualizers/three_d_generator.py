"""
3D Viewer Generator
Generates interactive HTML/Three.js viewers from 3D geometry.
"""

import json
import base64
from pathlib import Path
from typing import Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)

# HTML template for Three.js viewer
VIEWER_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>3D CAD Viewer - {{part_name}}</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #1a1a1a;
            color: #fff;
            overflow: hidden;
        }
        
        #container {
            width: 100vw;
            height: 100vh;
            position: relative;
        }
        
        #info-panel {
            position: absolute;
            top: 20px;
            left: 20px;
            background: rgba(0, 0, 0, 0.8);
            padding: 20px;
            border-radius: 8px;
            min-width: 250px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        #info-panel h2 {
            font-size: 18px;
            margin-bottom: 15px;
            color: #4fc3f7;
        }
        
        #info-panel .metric {
            display: flex;
            justify-content: space-between;
            margin: 8px 0;
            font-size: 14px;
        }
        
        #info-panel .metric .label {
            color: #aaa;
        }
        
        #info-panel .metric .value {
            color: #fff;
            font-weight: 500;
        }
        
        #controls {
            position: absolute;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            gap: 10px;
            background: rgba(0, 0, 0, 0.8);
            padding: 10px;
            border-radius: 8px;
            backdrop-filter: blur(10px);
        }
        
        #controls button {
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: #fff;
            padding: 8px 16px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 13px;
            transition: all 0.2s;
        }
        
        #controls button:hover {
            background: rgba(255, 255, 255, 0.2);
        }
        
        #controls button.active {
            background: #4fc3f7;
            color: #000;
        }
        
        #loading {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 18px;
            color: #4fc3f7;
        }
        
        .spinner {
            width: 40px;
            height: 40px;
            border: 4px solid rgba(79, 195, 247, 0.3);
            border-top-color: #4fc3f7;
            border-radius: 50%;
            animation: spin 1s linear infinite;
            margin: 0 auto 15px;
        }
        
        @keyframes spin {
            to { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <div id="container">
        <div id="loading">
            <div class="spinner"></div>
            Loading 3D Model...
        </div>
        
        <div id="info-panel" style="display: none;">
            <h2>{{part_name}}</h2>
            <div class="metric">
                <span class="label">Dimensions</span>
                <span class="value">{{dimensions}}</span>
            </div>
            <div class="metric">
                <span class="label">Volume</span>
                <span class="value">{{volume}} cm³</span>
            </div>
            <div class="metric">
                <span class="label">Surface Area</span>
                <span class="value">{{surface_area}} mm²</span>
            </div>
            <div class="metric">
                <span class="label">Faces</span>
                <span class="value">{{face_count}}</span>
            </div>
        </div>
        
        <div id="controls" style="display: none;">
            <button id="btn-wireframe">Wireframe</button>
            <button id="btn-solid" class="active">Solid</button>
            <button id="btn-section">Section</button>
            <button id="btn-reset">Reset View</button>
        </div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
    <script>
        // Model data injected by generator
        const modelData = {{model_data_json}};
        
        let scene, camera, renderer, controls;
        let mesh, wireframeMesh, sectionMesh;
        let isWireframe = false;
        let isSection = false;
        
        function init() {
            // Scene
            scene = new THREE.Scene();
            scene.background = new THREE.Color(0x1a1a1a);
            
            // Camera
            const aspect = window.innerWidth / window.innerHeight;
            camera = new THREE.PerspectiveCamera(45, aspect, 0.1, 1000);
            
            // Position camera based on bounding box
            const bbox = modelData.bounding_box;
            const center = bbox.center;
            const size = Math.max(
                bbox.dimensions[0],
                bbox.dimensions[1],
                bbox.dimensions[2]
            );
            camera.position.set(
                center[0] + size,
                center[1] - size,
                center[2] + size
            );
            camera.lookAt(center[0], center[1], center[2]);
            
            // Renderer
            renderer = new THREE.WebGLRenderer({ antialias: true });
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.shadowMap.enabled = true;
            document.getElementById('container').appendChild(renderer.domElement);
            
            // Controls
            controls = new THREE.OrbitControls(camera, renderer.domElement);
            controls.enableDamping = true;
            controls.dampingFactor = 0.05;
            controls.target.set(center[0], center[1], center[2]);
            
            // Lighting
            const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
            scene.add(ambientLight);
            
            const dirLight = new THREE.DirectionalLight(0xffffff, 0.8);
            dirLight.position.set(10, 10, 10);
            dirLight.castShadow = true;
            scene.add(dirLight);
            
            // Load geometry
            loadGeometry();
            
            // Hide loading, show UI
            document.getElementById('loading').style.display = 'none';
            document.getElementById('info-panel').style.display = 'block';
            document.getElementById('controls').style.display = 'flex';
            
            // Event listeners
            window.addEventListener('resize', onWindowResize);
            document.getElementById('btn-wireframe').addEventListener('click', toggleWireframe);
            document.getElementById('btn-solid').addEventListener('click', toggleSolid);
            document.getElementById('btn-section').addEventListener('click', toggleSection);
            document.getElementById('btn-reset').addEventListener('click', resetView);
        }
        
        function loadGeometry() {
            // Load from model data
            // This is a placeholder - actual implementation would load the mesh data
            
            const geometry = new THREE.BoxGeometry(1, 1, 1);  // Placeholder
            const material = new THREE.MeshStandardMaterial({
                color: 0xcccccc,
                metalness: 0.3,
                roughness: 0.4
            });
            
            mesh = new THREE.Mesh(geometry, material);
            scene.add(mesh);
            
            // Wireframe version
            const wireframeGeometry = new THREE.WireframeGeometry(geometry);
            const wireframeMaterial = new THREE.LineBasicMaterial({ color: 0x000000 });
            wireframeMesh = new THREE.LineSegments(wireframeGeometry, wireframeMaterial);
            wireframeMesh.visible = false;
            scene.add(wireframeMesh);
        }
        
        function onWindowResize() {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        }
        
        function toggleWireframe() {
            isWireframe = true;
            isSection = false;
            mesh.visible = false;
            wireframeMesh.visible = true;
            updateButtonStates();
        }
        
        function toggleSolid() {
            isWireframe = false;
            isSection = false;
            mesh.visible = true;
            wireframeMesh.visible = false;
            updateButtonStates();
        }
        
        function toggleSection() {
            isSection = !isSection;
            // Section plane logic would go here
            updateButtonStates();
        }
        
        function resetView() {
            const bbox = modelData.bounding_box;
            const center = bbox.center;
            const size = Math.max(
                bbox.dimensions[0],
                bbox.dimensions[1],
                bbox.dimensions[2]
            );
            
            camera.position.set(
                center[0] + size,
                center[1] - size,
                center[2] + size
            );
            camera.lookAt(center[0], center[1], center[2]);
            controls.target.set(center[0], center[1], center[2]);
            controls.update();
        }
        
        function updateButtonStates() {
            document.getElementById('btn-wireframe').classList.toggle('active', isWireframe);
            document.getElementById('btn-solid').classList.toggle('active', !isWireframe && !isSection);
            document.getElementById('btn-section').classList.toggle('active', isSection);
        }
        
        function animate() {
            requestAnimationFrame(animate);
            controls.update();
            renderer.render(scene, camera);
        }
        
        // Initialize when DOM is ready
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', init);
        } else {
            init();
        }
        
        // Start animation loop
        animate();
    </script>
</body>
</html>
'''

    def _get_model_data_json(self, geometry) -> str:
        """Generate model data JSON for viewer"""
        if hasattr(geometry, 'to_dict'):
            data = geometry.to_dict()
        else:
            # Fallback for other geometry types
            data = {
                'bounding_box': {
                    'center': [0, 0, 0],
                    'dimensions': [100, 100, 100]
                }
            }
        
        return json.dumps(data)


# Convenience function
def generate_3d_viewer(geometry, output_path: Path, part_name: str = "Part") -> Path:
    """Generate a 3D viewer HTML file"""
    generator = ThreeDGenerator()
    return generator.generate_viewer(geometry, output_path, part_name)
