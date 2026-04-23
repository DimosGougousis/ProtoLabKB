"""
Feature Detector
Detects manufacturing features (holes, pockets, bosses, etc.) from geometry.
"""

import numpy as np
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)


@dataclass
class DetectedFeature:
    """Represents a detected manufacturing feature"""
    feature_type: str
    properties: Dict[str, Any]
    confidence: float
    supporting_geometry: List[Any]


class FeatureDetector:
    """Detects manufacturing features from CAD geometry"""
    
    def __init__(self):
        self.min_hole_diameter = 0.5  # mm
        self.max_hole_diameter = 100.0  # mm
        self.min_pocket_depth = 0.5  # mm
        self.min_boss_height = 1.0  # mm
        self.min_fillet_radius = 0.1  # mm
    
    def detect_all(self, geometry) -> Dict[str, List[Dict]]:
        """
        Detect all manufacturing features from geometry.
        
        Args:
            geometry: Geometry data (trimesh, CadQuery shape, etc.)
            
        Returns:
            Dictionary of feature types with lists of detected features
        """
        features = {
            'holes': [],
            'pockets': [],
            'bosses': [],
            'fillets': [],
            'chamfers': [],
            'threads': [],
            'thin_walls': []
        }
        
        try:
            # Detect holes
            features['holes'] = self.detect_holes(geometry)
            logger.info(f"Detected {len(features['holes'])} holes")
            
            # Detect pockets
            features['pockets'] = self.detect_pockets(geometry)
            logger.info(f"Detected {len(features['pockets'])} pockets")
            
            # Detect bosses
            features['bosses'] = self.detect_bosses(geometry)
            logger.info(f"Detected {len(features['bosses'])} bosses")
            
            # Detect fillets
            features['fillets'] = self.detect_fillets(geometry)
            logger.info(f"Detected {len(features['fillets'])} fillets")
            
            # Detect chamfers
            features['chamfers'] = self.detect_chamfers(geometry)
            logger.info(f"Detected {len(features['chamfers'])} chamfers")
            
            # Detect thin walls
            features['thin_walls'] = self.detect_thin_walls(geometry)
            logger.info(f"Detected {len(features['thin_walls'])} thin wall regions")
            
        except Exception as e:
            logger.error(f"Error during feature detection: {e}")
        
        return features
    
    def detect_holes(self, geometry) -> List[Dict]:
        """Detect holes in geometry"""
        holes = []
        
        # For mesh-based geometry (STL/OBJ)
        if hasattr(geometry, 'vertices') and hasattr(geometry, 'faces'):
            holes = self._detect_holes_mesh(geometry)
        
        # For B-rep geometry (STEP)
        elif hasattr(geometry, 'faces'):
            holes = self._detect_holes_brep(geometry)
        
        return holes
    
    def _detect_holes_mesh(self, mesh) -> List[Dict]:
        """Detect holes in mesh geometry using curvature analysis"""
        holes = []
        
        try:
            # Find circular boundaries (potential holes)
            # This is a simplified approach - full implementation would use
            # more sophisticated feature recognition
            
            # Get boundary edges
            boundary_edges = mesh.edges_unique[mesh.edges_boundary]
            
            # Group edges into loops
            loops = self._group_edges_into_loops(boundary_edges, mesh)
            
            for loop in loops:
                # Check if loop is approximately circular
                circle_fit = self._fit_circle_to_loop(loop, mesh)
                
                if circle_fit and circle_fit['circularity'] > 0.8:
                    diameter = circle_fit['diameter']
                    
                    if self.min_hole_diameter <= diameter <= self.max_hole_diameter:
                        holes.append({
                            'id': f'hole_{len(holes)}',
                            'type': 'through_hole',  # Would need depth analysis
                            'diameter': diameter,
                            'position': circle_fit['center'],
                            'axis': [0, 0, 1],  # Would need to calculate from face normal
                            'confidence': circle_fit['circularity'],
                            'detection_method': 'mesh_boundary_loop'
                        })
        
        except Exception as e:
            logger.error(f"Error detecting holes in mesh: {e}")
        
        return holes
    
    def _detect_holes_brep(self, geometry) -> List[Dict]:
        """Detect holes in B-rep geometry using face analysis"""
        holes = []
        
        try:
            from OCP.BRepAdaptor import BRepAdaptor_Surface
            from OCP.GeomAbs import GeomAbs_Cylinder
            from OCP.TopExp import TopExp_Explorer
            from OCP.TopAbs import TopAbs_FACE
            
            # Find all cylindrical faces
            face_explorer = TopExp_Explorer(geometry.wrapped, TopAbs_FACE)
            
            while face_explorer.More():
                face = face_explorer.Current()
                surface = BRepAdaptor_Surface(face)
                
                if surface.GetType() == GeomAbs_Cylinder:
                    cylinder = surface.Cylinder()
                    diameter = cylinder.Radius() * 2
                    
                    if self.min_hole_diameter <= diameter <= self.max_hole_diameter:
                        axis = cylinder.Axis()
                        holes.append({
                            'id': f'hole_{len(holes)}',
                            'type': 'cylindrical_feature',
                            'diameter': diameter,
                            'position': [
                                axis.Location().X(),
                                axis.Location().Y(),
                                axis.Location().Z()
                            ],
                            'axis': [
                                axis.Direction().X(),
                                axis.Direction().Y(),
                                axis.Direction().Z()
                            ],
                            'confidence': 0.95,
                            'detection_method': 'brep_cylindrical_face'
                        })
                
                face_explorer.Next()
        
        except Exception as e:
            logger.error(f"Error detecting holes in B-rep: {e}")
        
        return holes
    
    def _group_edges_into_loops(self, edges, mesh) -> List[List[int]]:
        """Group edges into closed loops"""
        # Simplified implementation
        # Full implementation would build edge connectivity graph
        return [edges.tolist()] if len(edges) > 0 else []
    
    def _fit_circle_to_loop(self, loop, mesh) -> Optional[Dict]:
        """Fit a circle to a loop of edges"""
        try:
            # Get vertices in loop
            vertices = mesh.vertices[loop]
            
            if len(vertices) < 3:
                return None
            
            # Fit circle using least squares
            # This is a simplified 2D circle fit
            center = np.mean(vertices, axis=0)
            distances = np.linalg.norm(vertices - center, axis=1)
            radius = np.mean(distances)
            
            # Calculate circularity (how well points fit circle)
            std_dev = np.std(distances)
            circularity = 1.0 - (std_dev / radius) if radius > 0 else 0
            
            return {
                'center': center.tolist(),
                'radius': radius,
                'diameter': radius * 2,
                'circularity': max(0, circularity)
            }
        
        except Exception as e:
            logger.error(f"Error fitting circle: {e}")
            return None
    
    def detect_pockets(self, geometry) -> List[Dict]:
        """Detect pockets in geometry"""
        # Placeholder - full implementation would analyze concave regions
        return []
    
    def detect_bosses(self, geometry) -> List[Dict]:
        """Detect bosses in geometry"""
        # Placeholder - full implementation would analyze convex protrusions
        return []
    
    def detect_fillets(self, geometry) -> List[Dict]:
        """Detect fillets in geometry"""
        # Placeholder - full implementation would analyze rounded edges
        return []
    
    def detect_chamfers(self, geometry) -> List[Dict]:
        """Detect chamfers in geometry"""
        # Placeholder - full implementation would analyze beveled edges
        return []
    
    def detect_threads(self, geometry) -> List[Dict]:
        """Detect threads in geometry"""
        # Placeholder - full implementation would analyze helical surfaces
        return []
    
    def detect_thin_walls(self, geometry) -> List[Dict]:
        """Detect thin walls in geometry"""
        # Placeholder - full implementation would analyze wall thickness
        return []


# Convenience function
def detect_features(geometry) -> Dict[str, List[Dict]]:
    """Detect all features in geometry"""
    detector = FeatureDetector()
    return detector.detect_all(geometry)
