"""
OBJ File Parser
Parses Wavefront OBJ files and extracts geometry data.
"""

import numpy as np
from pathlib import Path
from typing import List, Tuple, Dict, Any, Optional
import trimesh

from .base_parser import BaseParser, GeometryData, BoundingBox


class OBJParser(BaseParser):
    """Parser for Wavefront OBJ files"""
    
    def __init__(self):
        super().__init__()
        self.supported_extensions = ['.obj']
        self.format_name = "OBJ"
    
    def can_parse(self, file_path: str) -> bool:
        """Check if file is OBJ format"""
        return Path(file_path).suffix.lower() in self.supported_extensions
    
    def parse(self, file_path: str) -> GeometryData:
        """
        Parse OBJ file and extract geometry data.
        
        Args:
            file_path: Path to OBJ file
            
        Returns:
            GeometryData with extracted information
        """
        self.validate_file(file_path)
        
        try:
            # Load mesh using trimesh (handles OBJ with materials)
            mesh_data = trimesh.load(file_path, process=True)
            
            # Handle scene (multiple objects)
            if isinstance(mesh_data, trimesh.Scene):
                # Concatenate all meshes in scene
                mesh_data = trimesh.util.concatenate(mesh_data.dump())
            
            # Extract vertices
            vertices = mesh_data.vertices.tolist()
            
            # Calculate bounding box
            bounding_box = self.calculate_bounding_box(vertices)
            
            # Calculate volume (may be zero for non-watertight meshes)
            try:
                volume = float(mesh_data.volume) / 1000  # Convert to cm³
            except:
                volume = 0.0
            
            # Calculate surface area
            surface_area = float(mesh_data.area)
            
            # Calculate center of mass
            try:
                center_of_mass = mesh_data.center_mass.tolist()
            except:
                center_of_mass = bounding_box.center
            
            # Extract material information if available
            materials = self._extract_materials(file_path)
            
            # Check for mesh issues
            mesh_issues = self._check_mesh_issues(mesh_data)
            
            return GeometryData(
                bounding_box=bounding_box,
                volume=volume,
                surface_area=surface_area,
                center_of_mass=center_of_mass,
                format="OBJ",
                file_path=file_path,
                metadata={
                    'vertex_count': len(mesh_data.vertices),
                    'face_count': len(mesh_data.faces),
                    'has_texture': mesh_data.visual.uv is not None,
                    'has_vertex_colors': mesh_data.visual.vertex_colors is not None,
                    'materials': materials,
                    'mesh_issues': mesh_issues,
                    'is_watertight': mesh_data.is_watertight if hasattr(mesh_data, 'is_watertight') else False
                }
            )
            
        except Exception as e:
            raise RuntimeError(f"Failed to parse OBJ file: {str(e)}")
    
    def _extract_materials(self, file_path: str) -> List[Dict[str, Any]]:
        """Extract material definitions from MTL file"""
        materials = []
        
        mtl_path = Path(file_path).with_suffix('.mtl')
        if not mtl_path.exists():
            return materials
        
        try:
            with open(mtl_path, 'r') as f:
                current_material = None
                
                for line in f:
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue
                    
                    parts = line.split()
                    if not parts:
                        continue
                    
                    keyword = parts[0]
                    
                    if keyword == 'newmtl':
                        if current_material:
                            materials.append(current_material)
                        current_material = {
                            'name': parts[1] if len(parts) > 1 else 'unnamed',
                            'properties': {}
                        }
                    
                    elif current_material:
                        if keyword in ['Ka', 'Kd', 'Ks', 'Ke']:
                            # Color properties
                            current_material['properties'][keyword] = [
                                float(parts[1]),
                                float(parts[2]),
                                float(parts[3])
                            ] if len(parts) >= 4 else [0, 0, 0]
                        
                        elif keyword in ['Ns', 'Ni', 'd', 'Tr']:
                            # Scalar properties
                            current_material['properties'][keyword] = float(parts[1]) if len(parts) > 1 else 0
                        
                        elif keyword == 'illum':
                            current_material['properties']['illumination_model'] = int(parts[1]) if len(parts) > 1 else 0
                        
                        elif keyword == 'map_Kd':
                            current_material['properties']['diffuse_texture'] = ' '.join(parts[1:])
                
                if current_material:
                    materials.append(current_material)
        
        except Exception as e:
            print(f"Warning: Could not parse MTL file: {e}")
        
        return materials
    
    def _check_mesh_issues(self, mesh_data: trimesh.Trimesh) -> List[Dict[str, Any]]:
        """Check for common mesh issues"""
        issues = []
        
        # Check for degenerate faces
        if hasattr(mesh_data, 'face_angles'):
            degenerate = mesh_data.faces[
                mesh_data.face_angles.min(axis=1) < 0.001
            ]
            if len(degenerate) > 0:
                issues.append({
                    'type': 'degenerate_faces',
                    'count': len(degenerate),
                    'severity': 'warning',
                    'message': f"Found {len(degenerate)} degenerate faces"
                })
        
        # Check for non-manifold edges
        if hasattr(mesh_data, 'is_watertight'):
            if not mesh_data.is_watertight:
                issues.append({
                    'type': 'not_watertight',
                    'severity': 'warning',
                    'message': 'Mesh is not watertight (may have holes)'
                })
        
        return issues


# Convenience function
def parse_obj_file(file_path: str) -> GeometryData:
    """Parse an OBJ file and return geometry data"""
    parser = OBJParser()
    return parser.parse(file_path)
