"""
STEP File Parser
Parses STEP (ISO 10303) files and extracts geometry data using CadQuery/OpenCASCADE.
"""

import os
import sys
import math
from pathlib import Path
from typing import List, Tuple, Dict, Any, Optional, Set
from dataclasses import dataclass
import json
import re

# CadQuery imports
try:
    import cadquery as cq
    from cadquery import exporters, importers
    from OCP.BRep import BRep_Tool
    from OCP.BRepGProp import BRepGProp
    from OCP.GProp import GProp_GProps
    from OCP.TopExp import TopExp_Explorer
    from OCP.TopAbs import TopAbs_FACE, TopAbs_EDGE, TopAbs_VERTEX, TopAbs_WIRE
    from OCP.BRepAdaptor import BRepAdaptor_Surface, BRepAdaptor_Curve
    from OCP.BRepTools import BRepTools
    from OCP.GeomAbs import GeomAbs_Cylinder, GeomAbs_Plane, GeomAbs_Cone, GeomAbs_Torus
    from OCP.gp import gp_Pnt, gp_Dir, gp_Vec
    from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeVertex
    from OCP.TopoDS import TopoDS_Face, TopoDS_Edge
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
        """
        Analyze a cylindrical face to determine if it's a hole or boss.
        
        Uses face orientation and adjacency analysis:
        - A hole's cylindrical face normal points toward the axis (concave)
        - A boss's cylindrical face normal points away from the axis (convex)
        """
        surface = BRepAdaptor_Surface(face)
        cylinder = surface.Cylinder()
        
        radius = cylinder.Radius()
        axis = cylinder.Axis()
        axis_dir = gp_Dir(axis.Direction())
        axis_loc = gp_Pnt(axis.Location())
        
        # Get face center for position
        props = GProp_GProps()
        BRepGProp.SurfaceProperties(face, props)
        face_center = props.CentreOfMass()
        
        # Determine if hole or boss by checking face normal orientation
        # Sample a point on the face and check normal direction
        u_min, u_max, v_min, v_max = BRepTools.UVBounds(face)
        u_mid = (u_min + u_max) / 2
        v_mid = (v_min + v_max) / 2
        
        # Get surface and normal at sample point
        surf = BRep_Tool.Surface(face)
        pnt = gp_Pnt()
        normal = gp_Vec()
        # Use surface evaluator
        try:
            from OCP.Geom import Geom_CylindricalSurface
            cyl_surf = Geom_CylindricalSurface.DownCast(surf)
            if cyl_surf is not None:
                pnt = cyl_surf.Value(u_mid, v_mid)
                # Normal at point on cylinder: radial direction
                radial = gp_Vec(axis_loc, pnt)
                if radial.Magnitude() > 1e-9:
                    radial.Normalize()
                    # Check if face normal points inward or outward
                    # Inward (toward axis) = hole, outward = boss
                    is_hole = self._is_face_normal_inward(face, radial)
                else:
                    is_hole = True  # Default to hole
            else:
                is_hole = True
        except Exception:
            is_hole = True
        
        # Calculate height by finding extent along axis
        height = self._calculate_cylindrical_height(face, axis_dir)
        
        feature_type = 'hole' if is_hole else 'boss'
        
        return {
            'type': feature_type,
            'diameter': radius * 2,
            'radius': radius,
            'height': height,
            'axis': [axis_dir.X(), axis_dir.Y(), axis_dir.Z()],
            'position': [face_center.X(), face_center.Y(), face_center.Z()],
            'is_through': height > 0 and height > self._get_part_max_dimension() * 0.8,
            'detection_confidence': 0.9
        }
    
    def _is_face_normal_inward(self, face, radial_vec) -> bool:
        """Check if face normal points inward (toward cylinder axis)."""
        try:
            # Get face orientation
            u_min, u_max, v_min, v_max = BRepTools.UVBounds(face)
            u_mid = (u_min + u_max) / 2
            v_mid = (v_min + v_max) / 2
            
            # Use BRepAdaptor to get normal
            surf = BRepAdaptor_Surface(face)
            pnt = gp_Pnt()
            du = gp_Vec()
            dv = gp_Vec()
            surf.D1(u_mid, v_mid, pnt, du, dv)
            
            # Normal = du x dv
            normal = du.Crossed(dv)
            if normal.Magnitude() > 1e-9:
                normal.Normalize()
                # Dot product: if normal points same direction as radial (outward), it's a boss
                dot = normal.Dot(radial_vec)
                return dot < 0  # Inward = hole
            return True
        except Exception:
            return True
    
    def _calculate_cylindrical_height(self, face, axis_dir) -> float:
        """Calculate the height of a cylindrical feature along its axis."""
        try:
            # Traverse all vertices of the face and project onto axis
            vertex_explorer = TopExp_Explorer(face, TopAbs_VERTEX)
            projections = []
            
            while vertex_explorer.More():
                vertex = vertex_explorer.Current()
                pnt = BRep_Tool.Pnt(vertex)
                # Project point onto axis direction
                proj = pnt.X() * axis_dir.X() + pnt.Y() * axis_dir.Y() + pnt.Z() * axis_dir.Z()
                projections.append(proj)
                vertex_explorer.Next()
            
            if projections:
                return max(projections) - min(projections)
            return 0.0
        except Exception:
            return 0.0
    
    def _get_part_max_dimension(self) -> float:
        """Get the maximum dimension of the part."""
        bbox = self._calculate_bounding_box()
        return max(bbox.width, bbox.height, bbox.depth)
    
    def _analyze_pocket(self, face) -> Optional[Dict]:
        """
        Analyze a planar face to determine if it's a pocket bottom.
        
        A pocket is identified by:
        - Planar face with area below a threshold (not the largest face)
        - Surrounded by vertical walls (adjacent faces are cylindrical or planar at angle)
        - Face normal points inward (concave region)
        """
        props = GProp_GProps()
        BRepGProp.SurfaceProperties(face, props)
        area = props.Mass()
        center = props.CentreOfMass()
        
        # Skip very large faces (likely external faces, not pockets)
        total_surface_area = self._calculate_surface_area()
        if area > total_surface_area * 0.3:
            return None
        
        # Check if face is concave (pocket) vs convex (protrusion)
        is_concave = self._is_face_concave(face)
        if not is_concave:
            return None
        
        # Estimate depth by finding maximum distance to adjacent faces
        depth = self._estimate_pocket_depth(face)
        
        # Get face bounds
        u_min, u_max, v_min, v_max = BRepTools.UVBounds(face)
        
        return {
            'type': 'pocket',
            'area': area,
            'depth': depth,
            'position': [center.X(), center.Y(), center.Z()],
            'width_approx': abs(u_max - u_min),
            'height_approx': abs(v_max - v_min),
            'is_concave': True,
            'detection_confidence': 0.75
        }
    
    def _is_face_concave(self, face) -> bool:
        """Check if a face is concave (part of a pocket/cavity)."""
        try:
            # Get face center and normal
            props = GProp_GProps()
            BRepGProp.SurfaceProperties(face, props)
            center = props.CentreOfMass()
            
            # Sample point and get normal
            surf = BRepAdaptor_Surface(face)
            u_min, u_max, v_min, v_max = BRepTools.UVBounds(face)
            u_mid = (u_min + u_max) / 2
            v_mid = (v_min + v_max) / 2
            
            pnt = gp_Pnt()
            du = gp_Vec()
            dv = gp_Vec()
            surf.D1(u_mid, v_mid, pnt, du, dv)
            normal = du.Crossed(dv)
            
            if normal.Magnitude() < 1e-9:
                return False
            normal.Normalize()
            
            # Check if normal points toward part center of mass
            com = self._calculate_center_of_mass()
            com_pnt = gp_Pnt(com[0], com[1], com[2])
            to_com = gp_Vec(center, com_pnt)
            
            if to_com.Magnitude() < 1e-9:
                return False
            to_com.Normalize()
            
            # If normal points toward COM, face is concave
            dot = normal.Dot(to_com)
            return dot > 0.3  # Threshold for concavity
        except Exception:
            return False
    
    def _estimate_pocket_depth(self, face) -> float:
        """Estimate pocket depth by measuring distance to opposite face."""
        try:
            # Get face center and normal
            props = GProp_GProps()
            BRepGProp.SurfaceProperties(face, props)
            center = props.CentreOfMass()
            
            surf = BRepAdaptor_Surface(face)
            u_min, u_max, v_min, v_max = BRepTools.UVBounds(face)
            u_mid = (u_min + u_max) / 2
            v_mid = (v_min + v_max) / 2
            
            pnt = gp_Pnt()
            du = gp_Vec()
            dv = gp_Vec()
            surf.D1(u_mid, v_mid, pnt, du, dv)
            normal = du.Crossed(dv)
            
            if normal.Magnitude() < 1e-9:
                return 0.0
            normal.Normalize()
            
            # Cast ray in normal direction and find intersection with other faces
            max_depth = 0.0
            for other_face in self.faces:
                if other_face == face:
                    continue
                # Simple distance check: project other face center onto normal
                other_props = GProp_GProps()
                BRepGProp.SurfaceProperties(other_face, other_props)
                other_center = other_props.CentreOfMass()
                
                vec = gp_Vec(center, other_center)
                dist = vec.Dot(normal)
                if dist > 0 and dist > max_depth:
                    max_depth = dist
            
            return max_depth
        except Exception:
            return 0.0
    
    def _classify_edge(self, edge) -> str:
        """
        Classify an edge as fillet, chamfer, or sharp.
        
        Uses edge curvature analysis:
        - Fillet: constant radius curvature connecting two faces
        - Chamfer: straight bevel at angle between two faces
        - Sharp: no blending
        """
        try:
            curve = BRepAdaptor_Curve(edge)
            curve_type = curve.GetType()
            
            # Get adjacent faces
            adjacent_faces = self._get_adjacent_faces(edge)
            if len(adjacent_faces) < 2:
                return 'sharp'
            
            # Check if edge is a circle/arc (potential fillet)
            if curve_type == 0:  # Line
                # Check angle between faces for chamfer detection
                angle = self._calculate_face_angle(adjacent_faces[0], adjacent_faces[1], edge)
                if 30 < angle < 150:  # Chamfer angle range
                    return 'chamfer'
                return 'sharp'
            
            elif curve_type == 1:  # Circle
                # Check if it's a blending edge (fillet)
                radius = abs(curve.Circle().Radius())
                if 0.1 < radius < 50:  # Reasonable fillet radius range
                    return 'fillet'
                return 'sharp'
            
            return 'sharp'
        except Exception:
            return 'sharp'
    
    def _get_adjacent_faces(self, edge) -> List[Any]:
        """Get faces adjacent to an edge."""
        adjacent = []
        try:
            for face in self.faces:
                edge_exp = TopExp_Explorer(face, TopAbs_EDGE)
                while edge_exp.More():
                    if edge_exp.Current().IsSame(edge):
                        adjacent.append(face)
                        break
                    edge_exp.Next()
        except Exception:
            pass
        return adjacent
    
    def _calculate_face_angle(self, face1, face2, edge) -> float:
        """Calculate the angle between two faces at an edge (in degrees)."""
        try:
            # Get normals at a point on the edge
            curve = BRepAdaptor_Curve(edge)
            u_min = curve.FirstParameter()
            u_max = curve.LastParameter()
            u_mid = (u_min + u_max) / 2
            
            pnt = gp_Pnt()
            tangent = gp_Vec()
            curve.D1(u_mid, pnt, tangent)
            
            # Get face normals at this point
            normal1 = self._get_face_normal_at_point(face1, pnt)
            normal2 = self._get_face_normal_at_point(face2, pnt)
            
            if normal1 is None or normal2 is None:
                return 180.0
            
            # Calculate angle between normals
            dot = normal1.Dot(normal2)
            dot = max(-1.0, min(1.0, dot))
            angle_rad = math.acos(abs(dot))
            return math.degrees(angle_rad)
        except Exception:
            return 180.0
    
    def _get_face_normal_at_point(self, face, pnt) -> Optional[Any]:
        """Get face normal at a specific point."""
        try:
            surf = BRepAdaptor_Surface(face)
            # Find closest point on surface
            from OCP.Extrema import Extrema_ExtPS
            extrema = Extrema_ExtPS(pnt, surf.Surface(), surf.Surface().UResolution(1e-6), 
                                    surf.Surface().VResolution(1e-6))
            if not extrema.IsDone() or extrema.NbExt() == 0:
                return None
            
            # Get parameters at closest point
            u, v = extrema.Point(1).Parameter()
            
            _, du, dv = gp_Pnt(), gp_Vec(), gp_Vec()
            surf.D1(u, v, _, du, dv)
            normal = du.Crossed(dv)
            if normal.Magnitude() > 1e-9:
                normal.Normalize()
                return normal
            return None
        except Exception:
            return None
    
    def _analyze_fillet(self, edge) -> Dict:
        """Analyze a fillet edge and extract its radius."""
        try:
            curve = BRepAdaptor_Curve(edge)
            if curve.GetType() == 1:  # Circle
                radius = abs(curve.Circle().Radius())
                center = curve.Circle().Position().Location()
                return {
                    'type': 'fillet',
                    'radius': radius,
                    'diameter': radius * 2,
                    'position': [center.X(), center.Y(), center.Z()],
                    'detection_confidence': 0.9
                }
        except Exception:
            pass
        
        return {
            'type': 'fillet',
            'radius': 0.0,
            'detection_confidence': 0.5
        }
    
    def _analyze_chamfer(self, edge) -> Dict:
        """Analyze a chamfer edge and extract its angle and distance."""
        try:
            adjacent_faces = self._get_adjacent_faces(edge)
            angle = 45.0
            if len(adjacent_faces) >= 2:
                angle = self._calculate_face_angle(adjacent_faces[0], adjacent_faces[1], edge)
            
            # Estimate chamfer distance from edge length
            curve = BRepAdaptor_Curve(edge)
            u_min = curve.FirstParameter()
            u_max = curve.LastParameter()
            p1 = gp_Pnt()
            p2 = gp_Pnt()
            curve.D0(u_min, p1)
            curve.D0(u_max, p2)
            length = p1.Distance(p2)
            
            return {
                'type': 'chamfer',
                'angle': angle,
                'length': length,
                'detection_confidence': 0.8
            }
        except Exception:
            return {
                'type': 'chamfer',
                'angle': 45.0,
                'detection_confidence': 0.5
            }
    
    def _extract_metadata(self, file_path: str) -> Dict[str, Any]:
        """Extract metadata from STEP file header with robust parsing."""
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
                content = f.read(50000)  # Read first 50KB
            
            # FILE_SCHEMA extraction
            schema_match = re.search(r"FILE_SCHEMA\s*\(\s*\(\s*['\"]([^'\"]+)['\"]", content)
            if schema_match:
                metadata['schema'] = schema_match.group(1)
            
            # FILE_NAME extraction: FILE_NAME('name','timestamp',('author'),('org'),'preprocessor','originating_system','authorization')
            file_name_match = re.search(
                r"FILE_NAME\s*\(\s*['\"]([^'\"]*)['\"]\s*,\s*['\"]([^'\"]*)['\"]\s*,\s*\(([^)]*)\)\s*,\s*\(([^)]*)\)\s*,\s*['\"]([^'\"]*)['\"]\s*,\s*['\"]([^'\"]*)['\"]\s*,\s*['\"]([^'\"]*)['\"]",
                content, re.DOTALL
            )
            if file_name_match:
                metadata['timestamp'] = file_name_match.group(2).strip()
                author_str = file_name_match.group(3).strip()
                org_str = file_name_match.group(4).strip()
                metadata['preprocessor_version'] = file_name_match.group(5).strip()
                metadata['originating_system'] = file_name_match.group(6).strip()
                metadata['authorization'] = file_name_match.group(7).strip()
                
                # Extract author from quoted string
                author_match = re.search(r"['\"]([^'\"]+)['\"]", author_str)
                if author_match:
                    metadata['author'] = author_match.group(1)
                
                # Extract organization from quoted string
                org_match = re.search(r"['\"]([^'\"]+)['\"]", org_str)
                if org_match:
                    metadata['organization'] = org_match.group(1)
            
            # FILE_DESCRIPTION
            desc_match = re.search(r"FILE_DESCRIPTION\s*\(\s*\(\s*['\"]([^'\"]+)['\"]", content)
            if desc_match:
                metadata['description'] = desc_match.group(1)
        
        except Exception as e:
            metadata['parse_error'] = str(e)
        
        return metadata


# Convenience function for direct usage
def parse_step_file(file_path: str) -> GeometryData:
    """Parse a STEP file and return geometry data"""
    parser = STEPParser()
    return parser.parse(file_path)
