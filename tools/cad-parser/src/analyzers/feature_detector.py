"""
Feature Detector
Detects manufacturing features (holes, pockets, bosses, etc.) from geometry.
"""

import numpy as np
from typing import List, Dict, Any, Optional, Tuple, Set
from dataclasses import dataclass
import logging
from collections import defaultdict

try:
    import trimesh
    HAS_TRIMESH = True
except ImportError:
    HAS_TRIMESH = False

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
        """
        Group boundary edges into closed loops using edge connectivity graph.
        
        Returns list of vertex index loops.
        """
        if len(edges) == 0:
            return []
        
        try:
            # Build vertex connectivity graph
            # edges is array of [v1, v2] pairs
            graph = defaultdict(list)
            for edge in edges:
                v1, v2 = int(edge[0]), int(edge[1])
                graph[v1].append(v2)
                graph[v2].append(v1)
            
            # Find closed loops by traversing the graph
            visited = set()
            loops = []
            
            for start_vertex in graph:
                if start_vertex in visited:
                    continue
                
                loop = []
                current = start_vertex
                prev = None
                
                while current not in visited:
                    visited.add(current)
                    loop.append(current)
                    
                    # Find next vertex in loop
                    neighbors = [n for n in graph[current] if n != prev]
                    if not neighbors:
                        break
                    
                    prev = current
                    current = neighbors[0]
                    
                    # Check if loop closed
                    if current == start_vertex:
                        break
                
                if len(loop) >= 3:
                    loops.append(loop)
            
            return loops
        
        except Exception as e:
            logger.error(f"Error grouping edges into loops: {e}")
            return []
    
    def _fit_circle_to_loop(self, loop_vertices, mesh) -> Optional[Dict]:
        """
        Fit a circle to a loop of vertex indices using least-squares circle fitting.
        
        Uses algebraic least squares for robustness.
        """
        try:
            # Get 3D vertices from loop
            vertices = mesh.vertices[loop_vertices]
            
            if len(vertices) < 3:
                return None
            
            # Project to best-fit plane for 2D circle fitting
            center_3d = np.mean(vertices, axis=0)
            
            # Compute PCA to find plane normal
            centered = vertices - center_3d
            cov = np.dot(centered.T, centered) / len(vertices)
            eigenvalues, eigenvectors = np.linalg.eigh(cov)
            
            # Normal is eigenvector with smallest eigenvalue
            normal = eigenvectors[:, 0]
            
            # Create local coordinate system
            # u, v are orthonormal basis for the plane
            if abs(normal[2]) < 0.9:
                u = np.cross(normal, [0, 0, 1])
            else:
                u = np.cross(normal, [0, 1, 0])
            u = u / np.linalg.norm(u)
            v = np.cross(normal, u)
            v = v / np.linalg.norm(v)
            
            # Project vertices to 2D plane coordinates
            x = np.dot(centered, u)
            y = np.dot(centered, v)
            
            # Algebraic least squares circle fit
            # Circle equation: (x-a)^2 + (y-b)^2 = r^2
            # Linearized: x^2 + y^2 = 2ax + 2by + (r^2 - a^2 - b^2)
            # Let c = r^2 - a^2 - b^2, then: x^2 + y^2 = 2ax + 2by + c
            
            A = np.column_stack([2 * x, 2 * y, np.ones(len(x))])
            b_vec = x**2 + y**2
            
            # Solve least squares
            coeffs, residuals, rank, s = np.linalg.lstsq(A, b_vec, rcond=None)
            
            a, b, c = coeffs
            radius = np.sqrt(a**2 + b**2 + c)
            
            # Convert 2D center back to 3D
            center_2d = np.array([a, b])
            center_3d_fit = center_3d + center_2d[0] * u + center_2d[1] * v
            
            # Calculate circularity: how well points fit the circle
            distances = np.sqrt((x - a)**2 + (y - b)**2)
            std_dev = np.std(distances)
            circularity = 1.0 - (std_dev / radius) if radius > 0 else 0
            circularity = max(0, min(1, circularity))
            
            return {
                'center': center_3d_fit.tolist(),
                'radius': float(radius),
                'diameter': float(radius * 2),
                'circularity': float(circularity),
                'normal': normal.tolist(),
                'vertex_count': len(vertices)
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
