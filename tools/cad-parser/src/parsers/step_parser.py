"""
STEP File Parser
Parses STEP (ISO 10303) files and extracts geometry data using CadQuery/OpenCASCADE.
"""

import os
import sys
from pathlib import Path
from typing import List, Tuple, Dict, Any, Optional
from dataclasses import dataclass
import json

# CadQuery imports
try:
    import cadquery as cq
    from cadquery import exporters, importers
    from OCP.BRep import BRep_Tool
    from OCP.BRepGProp import BRepGProp
    from OCP.GProp import GProp_GProps
    from OCP.TopExp import TopExp_Explorer
    from OCP.TopAbs import TopAbs_FACE, TopAbs_EDGE, TopAbs_VERTEX
    from OCP.BRepAdaptor import BRepAdaptor_Surface, BRepAdaptor_Curve
    from OCP.GeomAbs import GeomAbs_Cylinder, GeomAbs_Plane, GeomAbs_Cone
    HAS_CADQUERY = True
except ImportError:
    HAS_CADQUERY = False
    print("Warning: CadQuery not available. STEP parsing will be limited.")

from .base_parser import BaseParser, GeometryData, BoundingBox


@dataclass
class STEPFeature:
    """Represents a manufacturing feature extracted from STEP"""
    feature_type: str  # 'hole', 'pocket', 'boss', 'fillet', etc.
    properties: Dict[str, Any]
    location: List[float]
    faces: List[Any]  # OCP face references
    edges: List[Any]  # OCP edge references


class STEPParser(BaseParser):
    """Parser for STEP (ISO 10303) files using CadQuery/OpenCASCADE"""
    
    def __init__(self):
        super().__init__()
        self.supported_extensions = ['.step', '.stp']
        self.format_name = "STEP"
        self.shape = None
        self.faces = []
        self.edges = []
        
        if not HAS_CADQUERY:
            raise RuntimeError("CadQuery is required for STEP parsing. Install with: pip install cadquery")
    
    def can_parse(self, file_path: str) -> bool:
        """Check if file is STEP format"""
        return Path(file_path).suffix.lower() in self.supported_extensions
    
    def parse(self, file_path: str) -> GeometryData:
        """
        Parse STEP file and extract comprehensive geometry data.
        
        Args:
            file_path: Path to STEP file
            
        Returns:
            GeometryData with extracted information including B-rep topology
        """
        self.validate_file(file_path)
        
        try:
            # Import STEP file using CadQuery
            self.shape = importers.importStep(file_path)
            
            # Extract topology
            self._extract_topology()
            
            # Calculate geometric properties
            bounding_box = self._calculate_bounding_box()
            volume = self._calculate_volume()
            surface_area = self._calculate_surface_area()
            center_of_mass = self._calculate_center_of_mass()
            
            # Extract manufacturing features
            features = self._extract_features()
            
            # Get STEP metadata if available
            metadata = self._extract_metadata(file_path)
            
            return GeometryData(
                bounding_box=bounding_box,
                volume=volume,
                surface_area=surface_area,
                center_of_mass=center_of_mass,
                format="STEP",
                file_path=file_path,
                metadata={
                    'face_count': len(self.faces),
                    'edge_count': len(self.edges),
                    'features': features,
                    'step_metadata': metadata,
                    'cadquery_version': cq.__version__ if hasattr(cq, '__version__') else 'unknown'
                }
            )
            
        except Exception as e:
            raise RuntimeError(f"Failed to parse STEP file: {str(e)}")
    
    def _extract_topology(self):
        """Extract faces and edges from B-rep"""
        # Use OCP (OpenCASCADE) to traverse topology
        face_explorer = TopExp_Explorer(self.shape.wrapped, TopAbs_FACE)
        while face_explorer.More():
            face = face_explorer.Current()
            self.faces.append(face)
            face_explorer.Next()
        
        edge_explorer = TopExp_Explorer(self.shape.wrapped, TopAbs_EDGE)
        while edge_explorer.More():
            edge = edge_explorer.Current()
            self.edges.append(edge)
            edge_explorer.Next()
    
    def _calculate_bounding_box(self) -> BoundingBox:
        """Calculate 3D bounding box"""
        # Use CadQuery's built-in bounding box
        bbox = self.shape.val().BoundingBox()
        return BoundingBox(
            min_x=bbox.xmin,
            min_y=bbox.ymin,
            min_z=bbox.zmin,
            max_x=bbox.xmax,
            max_y=bbox.ymax,
            max_z=bbox.zmax
        )
    
    def _calculate_volume(self) -> float:
        """Calculate part volume in cm³"""
        # Use OCP GProp for accurate volume
        props = GProp_GProps()
        BRepGProp.VolumeProperties(self.shape.wrapped, props)
        volume_mm3 = props.Mass()
        return volume_mm3 / 1000  # Convert to cm³
    
    def _calculate_surface_area(self) -> float:
        """Calculate total surface area in mm²"""
        props = GProp_GProps()
        BRepGProp.SurfaceProperties(self.shape.wrapped, props)
        return props.Mass()
    
    def _calculate_center_of_mass(self) -> List[float]:
        """Calculate center of mass"""
        props = GProp_GProps()
        BRepGProp.VolumeProperties(self.shape.wrapped, props)
        cog = props.CentreOfMass()
        return [cog.X(), cog.Y(), cog.Z()]
    
    def _extract_features(self) -> Dict[str, List[Dict]]:
        """Extract manufacturing features from B-rep"""
        features = {
            'holes': [],
            'pockets': [],
            'bosses': [],
            'fillets': [],
            'chamfers': [],
            'threads': [],
            'thin_walls': []
        }
        
        # Analyze each face for features
        for face in self.faces:
            # Detect cylindrical faces (potential holes/bosses)
            if self._is_cylindrical_face(face):
                feature = self._analyze_cylindrical_feature(face)
                if feature:
                    if feature['type'] == 'hole':
                        features['holes'].append(feature)
                    elif feature['type'] == 'boss':
                        features['bosses'].append(feature)
            
            # Detect planar faces (potential pockets)
            elif self._is_planar_face(face):
                pocket = self._analyze_pocket(face)
                if pocket:
                    features['pockets'].append(pocket)
        
        # Analyze edges for fillets and chamfers
        for edge in self.edges:
            edge_type = self._classify_edge(edge)
            if edge_type == 'fillet':
                features['fillets'].append(self._analyze_fillet(edge))
            elif edge_type == 'chamfer':
                features['chamfers'].append(self._analyze_chamfer(edge))
        
        return features
    
    def _is_cylindrical_face(self, face) -> bool:
        """Check if face is cylindrical"""
        surface = BRepAdaptor_Surface(face)
        return surface.GetType() == GeomAbs_Cylinder
    
    def _is_planar_face(self, face) -> bool:
        """Check if face is planar"""
        surface = BRepAdaptor_Surface(face)
        return surface.GetType() == GeomAbs_Plane
    
    def _analyze_cylindrical_feature(self, face) -> Optional[Dict]:
        """Analyze a cylindrical face to determine if it's a hole or boss"""
        # This is a simplified implementation
        # Full implementation would analyze face orientation and adjacency
        
        surface = BRepAdaptor_Surface(face)
        cylinder = surface.Cylinder()
        
        radius = cylinder.Radius()
        axis = cylinder.Axis()
        
        return {
            'type': 'hole',  # Simplified - would need adjacency analysis
            'diameter': radius * 2,
            'axis': [axis.Direction().X(), axis.Direction().Y(), axis.Direction().Z()],
            'position': [axis.Location().X(), axis.Location().Y(), axis.Location().Z()]
        }
    
    def _analyze_pocket(self, face) -> Optional[Dict]:
        """Analyze a planar face to determine if it's a pocket bottom"""
        # Simplified implementation
        # Full implementation would check for surrounding walls
        
        props = GProp_GProps()
        BRepGProp.SurfaceProperties(face, props)
        area = props.Mass()
        
        return {
            'type': 'pocket',
            'area': area,
            'depth': 0  # Would need to measure from adjacent faces
        }
    
    def _classify_edge(self, edge) -> str:
        """Classify an edge as fillet, chamfer, or sharp"""
        # Simplified - would analyze edge geometry
        return 'sharp'
    
    def _analyze_fillet(self, edge) -> Dict:
        """Analyze a fillet edge"""
        return {'type': 'fillet'}
    
    def _analyze_chamfer(self, edge) -> Dict:
        """Analyze a chamfer edge"""
        return {'type': 'chamfer'}
    
    def _extract_metadata(self, file_path: str) -> Dict[str, Any]:
        """Extract metadata from STEP file header"""
        metadata = {
            'schema': None,
            'author': None,
            'organization': None,
            'timestamp': None,
            'preprocessor_version': None,
            'originating_system': None,
            'authorization': None
        }
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                # Read first 1000 lines looking for header
                for i, line in enumerate(f):
                    if i > 1000:
                        break
                    
                    line = line.strip()
                    
                    # FILE_SCHEMA
                    if 'FILE_SCHEMA' in line:
                        if '(' in line and ')' in line:
                            schema = line.split('(')[1].split(')')[0].strip("'\"")
                            metadata['schema'] = schema
                    
                    # FILE_NAME metadata
                    if 'FILE_NAME' in line:
                        # Next lines contain metadata
                        pass
                    
                    # Author
                    if line.startswith("'") and metadata['author'] is None:
                        if 'author' not in line.lower() and 'step' not in line.lower():
                            metadata['author'] = line.strip("'\"")
                    
                    # Timestamp
                    if ':' in line and '-' in line and metadata['timestamp'] is None:
                        # Simple heuristic for timestamp
                        if line.count('-') >= 2 and line.count(':') >= 2:
                            metadata['timestamp'] = line.strip("'\"")
        
        except Exception as e:
            metadata['parse_error'] = str(e)
        
        return metadata


# Convenience function for direct usage
def parse_step_file(file_path: str) -> GeometryData:
    """Parse a STEP file and return geometry data"""
    parser = STEPParser()
    return parser.parse(file_path)
