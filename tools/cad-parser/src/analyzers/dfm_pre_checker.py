"""
DFM Pre-Checker
Performs preliminary Design for Manufacturing analysis on extracted geometry.
"""

import numpy as np
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)


@dataclass
class DFMCheck:
    """Represents a DFM check result"""
    check_type: str  # 'critical', 'warning', 'note'
    category: str    # 'geometry', 'tolerance', 'material', 'process'
    message: str
    feature_id: Optional[str]
    recommendation: str
    source: str


class DFMPreChecker:
    """Performs preliminary DFM analysis on CAD geometry"""
    
    def __init__(self):
        # Process capability thresholds
        self.thresholds = {
            'cnc-machining': {
                'min_hole_diameter': 0.5,
                'max_hole_depth_ratio': 10.0,
                'min_internal_radius': 0.5,
                'min_wall_thickness': 0.5,
                'max_aspect_ratio': 5.0
            },
            'injection-molding': {
                'min_wall_thickness': 0.5,
                'max_wall_thickness': 6.0,
                'min_draft_angle': 0.5,
                'max_aspect_ratio': 3.0,
                'min_corner_radius': 0.5
            },
            '3d-printing-sla': {
                'min_wall_thickness': 0.3,
                'min_feature_size': 0.1,
                'max_overhang_angle': 30.0,
                'min_hole_diameter': 0.5
            },
            '3d-printing-sls': {
                'min_wall_thickness': 0.8,
                'min_feature_size': 0.5,
                'max_overhang_angle': 45.0
            }
        }
    
    def analyze(
        self,
        geometry,
        features: Dict[str, List[Dict]],
        process_hint: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Perform DFM pre-analysis on geometry and features.
        
        Args:
            geometry: Geometry data
            features: Dictionary of detected features
            process_hint: Optional process hint
            
        Returns:
            Dictionary with analysis results
        """
        results = {
            'process_hints': [],
            'critical_issues': [],
            'warnings': [],
            'notes': [],
            'recommendations': []
        }
        
        # Determine likely processes
        results['process_hints'] = self._suggest_processes(geometry, features)
        
        # Check holes
        if 'holes' in features:
            for hole in features['holes']:
                self._check_hole(hole, results, process_hint)
        
        # Check pockets
        if 'pockets' in features:
            for pocket in features['pockets']:
                self._check_pocket(pocket, results, process_hint)
        
        # Check bosses
        if 'bosses' in features:
            for boss in features['bosses']:
                self._check_boss(boss, results, process_hint)
        
        # Check thin walls
        if 'thin_walls' in features:
            for wall in features['thin_walls']:
                self._check_thin_wall(wall, results, process_hint)
        
        # Check overall geometry
        self._check_overall_geometry(geometry, results, process_hint)
        
        return results
    
    def _suggest_processes(
        self,
        geometry,
        features: Dict[str, List[Dict]]
    ) -> List[str]:
        """Suggest manufacturing processes based on geometry"""
        suggestions = []
        
        # Check geometry properties
        has_complex_features = (
            len(features.get('holes', [])) > 0 or
            len(features.get('pockets', [])) > 0 or
            len(features.get('threads', [])) > 0
        )
        
        is_watertight = getattr(geometry, 'is_watertight', False)
        volume = getattr(geometry, 'volume', 0)
        
        # Suggest CNC machining for solid parts with features
        if is_watertight and has_complex_features:
            suggestions.append('cnc-machining')
        
        # Suggest 3D printing for complex geometries
        if not is_watertight or len(features.get('pockets', [])) > 2:
            suggestions.append('3d-printing-sla')
            suggestions.append('3d-printing-sls')
        
        # Suggest injection molding for plastic-like volumes
        if 1 < volume < 1000 and is_watertight:
            suggestions.append('injection-molding')
        
        return suggestions[:3]  # Return top 3 suggestions
    
    def _check_hole(self, hole: Dict, results: Dict, process_hint: Optional[str]):
        """Check hole for DFM issues"""
        diameter = hole.get('diameter', 0)
        depth = hole.get('depth', 0)
        
        # Check minimum diameter
        if diameter < 0.5:
            results['critical_issues'].append({
                'type': 'critical',
                'category': 'geometry',
                'feature': 'hole',
                'feature_id': hole.get('id'),
                'message': f"Hole diameter {diameter:.2f}mm is below minimum 0.5mm",
                'recommendation': 'Increase hole diameter to at least 0.5mm or use drilling',
                'source': 'knowledge/cad/extraction-rules.md'
            })
        elif diameter < 1.0:
            results['warnings'].append({
                'type': 'warning',
                'category': 'geometry',
                'feature': 'hole',
                'feature_id': hole.get('id'),
                'message': f"Hole diameter {diameter:.2f}mm is small",
                'recommendation': 'Verify process capability for small holes',
                'source': 'knowledge/cad/extraction-rules.md'
            })
        
        # Check aspect ratio
        if depth > 0 and diameter > 0:
            aspect_ratio = depth / diameter
            if aspect_ratio > 10:
                results['critical_issues'].append({
                    'type': 'critical',
                    'category': 'geometry',
                    'feature': 'hole',
                    'feature_id': hole.get('id'),
                    'message': f"Hole aspect ratio {aspect_ratio:.1f}:1 exceeds 10:1 limit",
                    'recommendation': 'Use gun drilling or redesign with shorter hole',
                    'source': 'knowledge/cad/extraction-rules.md'
                })
            elif aspect_ratio > 3:
                results['warnings'].append({
                    'type': 'warning',
                    'category': 'geometry',
                    'feature': 'hole',
                    'feature_id': hole.get('id'),
                    'message': f"Hole aspect ratio {aspect_ratio:.1f}:1 requires peck drilling",
                    'recommendation': 'Specify peck drilling cycle in manufacturing instructions',
                    'source': 'knowledge/cad/extraction-rules.md'
                })
    
    def _check_pocket(self, pocket: Dict, results: Dict, process_hint: Optional[str]):
        """Check pocket for DFM issues"""
        depth = pocket.get('depth', 0)
        area = pocket.get('area', 0)
        min_corner_radius = pocket.get('min_corner_radius', 0)
        
        if area > 0:
            width = np.sqrt(area)
            aspect_ratio = depth / width if width > 0 else 0
            
            if aspect_ratio > 3:
                results['critical_issues'].append({
                    'type': 'critical',
                    'category': 'geometry',
                    'feature': 'pocket',
                    'feature_id': pocket.get('id'),
                    'message': f"Pocket aspect ratio {aspect_ratio:.1f}:1 exceeds 3:1 limit",
                    'recommendation': 'Consider through-pocket or multiple pockets',
                    'source': 'knowledge/cad/extraction-rules.md'
                })
            elif aspect_ratio > 2:
                results['warnings'].append({
                    'type': 'warning',
                    'category': 'geometry',
                    'feature': 'pocket',
                    'feature_id': pocket.get('id'),
                    'message': f"Pocket aspect ratio {aspect_ratio:.1f}:1 requires extended reach",
                    'recommendation': 'Verify tool reach and rigidity',
                    'source': 'knowledge/cad/extraction-rules.md'
                })
        
        if min_corner_radius < 0.5:
            results['warnings'].append({
                'type': 'warning',
                'category': 'geometry',
                'feature': 'pocket',
                'feature_id': pocket.get('id'),
                'message': f"Pocket corner radius {min_corner_radius:.2f}mm is small",
                'recommendation': 'Increase to 0.5mm minimum or specify EDM',
                'source': 'knowledge/cad/extraction-rules.md'
            })
    
    def _check_boss(self, boss: Dict, results: Dict, process_hint: Optional[str]):
        """Check boss for DFM issues"""
        height = boss.get('height', 0)
        base_diameter = boss.get('base_diameter', 0)
        
        if base_diameter > 0:
            aspect_ratio = height / base_diameter
            
            if aspect_ratio > 3:
                results['warnings'].append({
                    'type': 'warning',
                    'category': 'geometry',
                    'feature': 'boss',
                    'feature_id': boss.get('id'),
                    'message': f"Boss aspect ratio {aspect_ratio:.1f}:1 may cause vibration",
                    'recommendation': 'Add ribs or reduce height',
                    'source': 'knowledge/cad/extraction-rules.md'
                })
    
    def _check_thin_wall(self, wall: Dict, results: Dict, process_hint: Optional[str]):
        """Check thin wall for DFM issues"""
        thickness = wall.get('thickness', 0)
        area = wall.get('area', 0)
        
        # Process-specific minimums
        min_thickness = 0.5  # Default for CNC
        if process_hint == 'injection-molding':
            min_thickness = 0.5
        elif process_hint == '3d-printing-sla':
            min_thickness = 0.3
        elif process_hint == '3d-printing-sls':
            min_thickness = 0.8
        
        if thickness < min_thickness * 0.5:
            results['critical_issues'].append({
                'type': 'critical',
                'category': 'geometry',
                'feature': 'thin_wall',
                'message': f"Wall thickness {thickness:.2f}mm is critically thin",
                'recommendation': f"Increase to at least {min_thickness}mm",
                'source': 'knowledge/cad/extraction-rules.md'
            })
        elif thickness < min_thickness:
            results['warnings'].append({
                'type': 'warning',
                'category': 'geometry',
                'feature': 'thin_wall',
                'message': f"Wall thickness {thickness:.2f}mm below recommended {min_thickness}mm",
                'recommendation': 'Consider thickening or verify process capability',
                'source': 'knowledge/cad/extraction-rules.md'
            })
    
    def _check_overall_geometry(self, geometry, results: Dict, process_hint: Optional[str]):
        """Check overall geometry characteristics"""
        # Get bounding box
        if hasattr(geometry, 'bounding_box'):
            bbox = geometry.bounding_box
            dimensions = [
                bbox.max_x - bbox.min_x,
                bbox.max_y - bbox.min_y,
                bbox.max_z - bbox.min_z
            ]
            max_dim = max(dimensions)
            
            # Check for very large parts
            if max_dim > 500:  # 500mm
                results['warnings'].append({
                    'type': 'warning',
                    'category': 'geometry',
                    'message': f"Large part dimension ({max_dim:.1f}mm) may limit process options",
                    'recommendation': 'Verify machine capacity or consider segmentation',
                    'source': 'knowledge/cad/extraction-rules.md'
                })
            
            # Check for very small parts
            if max_dim < 5:  # 5mm
                results['notes'].append({
                    'type': 'note',
                    'category': 'geometry',
                    'message': f"Small part ({max_dim:.1f}mm) requires precision handling",
                    'recommendation': 'Consider fixturing and handling requirements',
                    'source': 'knowledge/cad/extraction-rules.md'
                })
        
        # Check volume
        if hasattr(geometry, 'volume'):
            volume = geometry.volume
            if volume > 1000:  # 1000 cm³
                results['notes'].append({
                    'type': 'note',
                    'category': 'cost',
                    'message': f"Large volume ({volume:.1f}cm³) will impact material cost",
                    'recommendation': 'Consider hollow sections or lightweighting',
                    'source': 'knowledge/cad/extraction-rules.md'
                })


# Convenience function
def check_dfm(geometry, features, process_hint=None) -> Dict[str, Any]:
    """Run DFM pre-check on geometry and features"""
    checker = DFMPreChecker()
    return checker.analyze(geometry, features, process_hint)
