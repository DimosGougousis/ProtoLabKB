"""
STL File Parser
Parses STL (Stereolithography) files and extracts geometry data.
"""

import numpy as np
from pathlib import Path
from typing import List, Tuple, Dict, Any
from stl import mesh
import trimesh

from .base_parser import BaseParser, GeometryData, BoundingBox


class STLParser(BaseParser):
    """Parser for STL (Stereolithography) files"""
    
    def __init__(self):
        super().__init__()
        self.supported_extensions = ['.stl']
        self.format_name = "STL"
    
    def can_parse(self, file_path: str) -> bool:
        """Check if file is STL format"""
        return Path(file_path).suffix.lower() in self.supported_extensions
    
    def parse(self, file_path: str) -> GeometryData:
        """
        Parse STL file and extract geometry data.
        
        Args:
            file_path: Path to STL file
            
        Returns:
            GeometryData with extracted information
        """
        self.validate_file(file_path)
        
        try:
            # Load mesh using trimesh
            mesh_data = trimesh.load(file_path)
            
            # Extract vertices
            vertices = mesh_data.vertices.tolist()
            
            # Calculate bounding box
            bounding_box = self.calculate_bounding_box(vertices)
            
            # Calculate volume
            volume = float(mesh_data.volume) / 1000  # Convert to cm³
            
            # Calculate surface area
            surface_area = float(mesh_data.area)
            
            # Calculate center of mass
            center_of_mass = mesh_data.center_mass.tolist()
            
            # Check if mesh is watertight
            is_watertight = mesh_data.is_watertight
            
            # Check for mesh issues
            mesh_issues = self._check_mesh_issues(mesh_data)
            
            return GeometryData(
                bounding_box=bounding_box,
                volume=volume,
                surface_area=surface_area,
                center_of_mass=center_of_mass,
                format="STL",
                file_path=file_path,
                metadata={
                    'is_watertight': is_watertight,
                    'triangle_count': len(mesh_data.faces),
                    'mesh_issues': mesh_issues
                }
            )
            
        except Exception as e:
            raise RuntimeError(f"Failed to parse STL file: {str(e)}")
    
    def _check_mesh_issues(self, mesh_data: trimesh.Trimesh) -> List[Dict[str, Any]]:
        """Check for common mesh issues"""
        issues = []
        
        # Check for degenerate faces
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
        
        # Check for duplicate vertices
        if not mesh_data.is_watertight:
            issues.append({
                'type': 'not_watertight',
                'severity': 'warning',
                'message': 'Mesh is not watertight (may have holes)'
            })
        
        # Check for inverted normals
        # (would need additional analysis)
        
        return issues
    
    def get_mesh_statistics(self, mesh_data: trimesh.Trimesh) -> Dict[str, Any]:
        """Get detailed mesh statistics"""
        return {
            'vertex_count': len(mesh_data.vertices),
            'face_count': len(mesh_data.faces),
            'edge_count': len(mesh_data.edges),
            'bounds': {
                'min': mesh_data.bounds[0].tolist(),
                'max': mesh_data.bounds[1].tolist()
            },
            'is_watertight': mesh_data.is_watertight,
            'is_winding_consistent': mesh_data.is_winding_consistent,
            'euler_number': mesh_data.euler_number,
            'volume': float(mesh_data.volume),
            'surface_area': float(mesh_data.area),
            'center_of_mass': mesh_data.center_mass.tolist(),
            'moment_of_inertia': mesh_data.moment_inertia.tolist() if hasattr(mesh_data, 'moment_inertia') else None
        }
