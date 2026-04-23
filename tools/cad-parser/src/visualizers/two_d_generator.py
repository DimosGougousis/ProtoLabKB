"""
2D View Generator
Generates orthographic 2D views (front, top, side, isometric) from 3D geometry.
"""

import numpy as np
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import logging

logger = logging.getLogger(__name__)

# Try to import rendering libraries
try:
    import matplotlib
    matplotlib.use('Agg')  # Use non-interactive backend
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    logger.warning("Matplotlib not available. 2D view generation will be limited.")

try:
    import pyrender
    import trimesh
    HAS_PYRENDER = True
except ImportError:
    HAS_PYRENDER = False


class TwoDGenerator:
    """Generator for 2D orthographic views from 3D geometry"""
    
    def __init__(self, width: int = 1920, height: int = 1080):
        self.width = width
        self.height = height
        self.output_dir = Path("./output")
        
        if not HAS_MATPLOTLIB and not HAS_PYRENDER:
            raise RuntimeError(
                "No rendering library available. Install matplotlib or pyrender."
            )
    
    def generate_view(
        self,
        geometry,
        view_type: str,
        output_path: Path,
        show_dimensions: bool = False
    ) -> Path:
        """
        Generate a 2D view from 3D geometry.
        
        Args:
            geometry: Geometry data (trimesh, CadQuery shape, etc.)
            view_type: Type of view ('front', 'top', 'side', 'iso')
            output_path: Path to save the image
            show_dimensions: Whether to overlay dimension annotations
            
        Returns:
            Path to generated image
        """
        if HAS_PYRENDER and hasattr(geometry, 'vertices'):
            # Use pyrender for high-quality rendering
            return self._render_with_pyrender(geometry, view_type, output_path)
        elif HAS_MATPLOTLIB:
            # Use matplotlib as fallback
            return self._render_with_matplotlib(geometry, view_type, output_path)
        else:
            raise RuntimeError("No rendering method available")
    
    def _render_with_pyrender(
        self,
        geometry,
        view_type: str,
        output_path: Path
    ) -> Path:
        """Render using PyRender for high-quality output"""
        # Convert to trimesh if needed
        if hasattr(geometry, 'wrapped'):
            # CadQuery shape - convert to trimesh
            mesh = self._cadquery_to_trimesh(geometry)
        elif isinstance(geometry, trimesh.Trimesh):
            mesh = geometry
        else:
            raise ValueError(f"Unsupported geometry type: {type(geometry)}")
        
        # Create scene
        scene = pyrender.Scene()
        
        # Add mesh
        pyrender_mesh = pyrender.Mesh.from_trimesh(mesh)
        scene.add(pyrender_mesh)
        
        # Set up camera based on view type
        camera, pose = self._get_camera_setup(view_type, mesh.bounds)
        scene.add(camera, pose=pose)
        
        # Add lighting
        light = pyrender.DirectionalLight(color=[1.0, 1.0, 1.0], intensity=2.0)
        scene.add(light, pose=pose)
        
        # Render
        renderer = pyrender.OffscreenRenderer(self.width, self.height)
        color, depth = renderer.render(scene)
        
        # Save image
        import imageio
        imageio.imwrite(str(output_path), color)
        
        return output_path
    
    def _render_with_matplotlib(
        self,
        geometry,
        view_type: str,
        output_path: Path
    ) -> Path:
        """Render using Matplotlib as fallback"""
        fig = plt.figure(figsize=(self.width / 100, self.height / 100), dpi=100)
        ax = fig.add_subplot(111, projection='3d')
        
        # Get vertices and faces
        if hasattr(geometry, 'vertices'):
            # Trimesh or similar
            vertices = geometry.vertices
            faces = geometry.faces
        elif hasattr(geometry, 'wrapped'):
            # CadQuery - convert to mesh
            mesh = self._cadquery_to_mesh(geometry)
            vertices = mesh.vertices
            faces = mesh.faces
        else:
            raise ValueError(f"Cannot extract geometry from {type(geometry)}")
        
        # Plot mesh
        ax.plot_trisurf(
            vertices[:, 0],
            vertices[:, 1],
            vertices[:, 2],
            triangles=faces,
            cmap='gray',
            alpha=0.8,
            edgecolor='none'
        )
        
        # Set view angle
        self._set_matplotlib_view(ax, view_type)
        
        # Remove axes for clean output
        ax.set_axis_off()
        
        # Save
        plt.savefig(output_path, dpi=100, bbox_inches='tight', pad_inches=0.1)
        plt.close()
        
        return output_path
    
    def _cadquery_to_trimesh(self, shape) -> trimesh.Trimesh:
        """Convert CadQuery shape to trimesh"""
        # Export to STL temporarily
        import tempfile
        with tempfile.NamedTemporaryFile(suffix='.stl', delete=False) as tmp:
            tmp_path = tmp.name
        
        try:
            exporters.export(shape, tmp_path, exporters.ExportTypes.STL)
            mesh = trimesh.load(tmp_path)
            return mesh
        finally:
            Path(tmp_path).unlink(missing_ok=True)
    
    def _get_camera_setup(self, view_type: str, bounds: np.ndarray) -> Tuple[Any, np.ndarray]:
        """Get camera and pose for view type"""
        # Calculate scene center and size
        center = (bounds[0] + bounds[1]) / 2
        size = np.linalg.norm(bounds[1] - bounds[0])
        
        # Camera parameters
        fov = 45.0
        distance = size / np.tan(np.radians(fov / 2))
        
        # View configurations
        views = {
            'front': {
                'eye': center + [0, -distance, 0],
                'up': [0, 0, 1]
            },
            'top': {
                'eye': center + [0, 0, distance],
                'up': [0, 1, 0]
            },
            'side': {
                'eye': center + [distance, 0, 0],
                'up': [0, 0, 1]
            },
            'iso': {
                'eye': center + [distance, -distance, distance],
                'up': [0, 0, 1]
            }
        }
        
        view = views.get(view_type, views['iso'])
        
        # Create camera
        camera = pyrender.PerspectiveCamera(yfov=np.radians(fov))
        
        # Create pose matrix
        pose = self._look_at(view['eye'], center, view['up'])
        
        return camera, pose
    
    def _look_at(self, eye: List[float], target: List[float], up: List[float]) -> np.ndarray:
        """Create look-at matrix"""
        eye = np.array(eye)
        target = np.array(target)
        up = np.array(up)
        
        forward = target - eye
        forward = forward / np.linalg.norm(forward)
        
        right = np.cross(forward, up)
        right = right / np.linalg.norm(right)
        
        up = np.cross(right, forward)
        
        pose = np.eye(4)
        pose[0, :3] = right
        pose[1, :3] = up
        pose[2, :3] = -forward
        pose[:3, 3] = eye
        
        return pose
    
    def _set_matplotlib_view(self, ax, view_type: str):
        """Set matplotlib view angle"""
        views = {
            'front': {'elev': 0, 'azim': -90},
            'top': {'elev': 90, 'azim': -90},
            'side': {'elev': 0, 'azim': 0},
            'iso': {'elev': 30, 'azim': -45}
        }
        
        view = views.get(view_type, views['iso'])
        ax.view_init(elev=view['elev'], azim=view['azim'])


# Convenience function for direct usage
def parse_stl_file(file_path: str) -> GeometryData:
    """Parse an STL file and return geometry data"""
    parser = STLParser()
    return parser.parse(file_path)
