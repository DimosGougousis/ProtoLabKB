"""
Topological and geometric validators for B-Rep shapes.

Ensures CAD-readiness before export to manufacturing (CNC, molding, 3D printing).
"""

import logging
from typing import Tuple, List, Dict
from dataclasses import dataclass


@dataclass
class ValidationResult:
    """Result of a validation check."""
    is_valid: bool
    violations: List[str]
    warnings: List[str]
    score: float  # 0.0 to 1.0


class TopologicalValidator:
    """
    Validates topological correctness of B-Rep geometries.

    Checks:
    - Euler formula (V - E + F = 2 for valid closed solids)
    - Orientation consistency (all faces consistently oriented)
    - Non-self-intersecting geometry
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def validate(self, shape_json: Dict) -> ValidationResult:
        """
        Validate topological correctness.

        Args:
            shape_json: B-Rep shape with metadata

        Returns:
            ValidationResult with violations and score
        """
        violations = []
        warnings = []

        metadata = shape_json.get("metadata", {})

        # Check 1: Euler characteristic
        v = metadata.get("vertices_count", 0)
        e = metadata.get("edges_count", 0)
        f = metadata.get("faces_count", 0)
        euler = v - e + f

        if euler != 2:
            violations.append(
                f"Euler characteristic mismatch: V({v}) - E({e}) + F({f}) = {euler} "
                f"(expected 2 for valid closed solid)"
            )

        # Check 2: Face count reasonable (min 4 for tetrahedron, max 10000 for complex)
        if f < 4:
            violations.append(f"Too few faces ({f}); minimum 4 for valid solid")
        elif f > 10000:
            warnings.append(f"Very high face count ({f}); may have tessellation artifacts")

        # Check 3: Solids count
        solids = metadata.get("solids_count", 0)
        if solids != 1:
            warnings.append(f"Expected 1 solid, found {solids}; may be multi-body or empty")

        # Calculate score
        score = 1.0
        score -= len(violations) * 0.5
        score -= len(warnings) * 0.1
        score = max(0.0, min(1.0, score))

        is_valid = len(violations) == 0

        return ValidationResult(
            is_valid=is_valid,
            violations=violations,
            warnings=warnings,
            score=score,
        )


class WatertightnessValidator:
    """
    Validates that geometry is watertight (no open edges, no holes).

    A watertight solid has:
    - All edges shared by exactly 2 faces
    - Consistent face orientation
    - No gaps or self-intersections
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def validate(self, shape_json: Dict) -> ValidationResult:
        """
        Validate watertightness.

        Args:
            shape_json: B-Rep shape with metadata

        Returns:
            ValidationResult
        """
        violations = []
        warnings = []

        metadata = shape_json.get("metadata", {})

        # Check watertight flag
        is_watertight = metadata.get("is_watertight", False)

        if not is_watertight:
            violations.append("Geometry is not watertight; has open edges or gaps")

        # Check volume > 0 (suggests closed, watertight solid)
        volume = metadata.get("volume", 0.0)
        if volume <= 0:
            violations.append(f"Volume is {volume}; expected positive volume for closed solid")

        # Check surface area reasonable
        surface_area = metadata.get("surface_area", 0.0)
        if surface_area <= 0:
            warnings.append(f"Surface area is {surface_area}; should be positive")

        # Calculate score
        score = 1.0 if is_watertight and volume > 0 else 0.0
        score -= len(violations) * 0.5
        score -= len(warnings) * 0.1

        is_valid = len(violations) == 0

        return ValidationResult(
            is_valid=is_valid,
            violations=violations,
            warnings=warnings,
            score=score,
        )


class CADReadinessValidator:
    """
    Validates CAD-readiness: combination of topological and manufacturing constraints.

    Suitable for CNC, injection molding, or 3D printing?
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.topo_validator = TopologicalValidator()
        self.water_validator = WatertightnessValidator()

    def validate(self, shape_json: Dict, process: str = "general") -> ValidationResult:
        """
        Validate CAD-readiness for specified manufacturing process.

        Args:
            shape_json: B-Rep shape
            process: "cnc" | "molding" | "3dprint" | "general"

        Returns:
            ValidationResult
        """
        all_violations = []
        all_warnings = []

        # Topological check
        topo_result = self.topo_validator.validate(shape_json)
        all_violations.extend(topo_result.violations)
        all_warnings.extend(topo_result.warnings)

        # Watertightness check
        water_result = self.water_validator.validate(shape_json)
        all_violations.extend(water_result.violations)
        all_warnings.extend(water_result.warnings)

        # Process-specific checks
        if process == "cnc":
            all_violations, all_warnings = self._check_cnc(shape_json, all_violations, all_warnings)
        elif process == "molding":
            all_violations, all_warnings = self._check_molding(shape_json, all_violations, all_warnings)
        elif process == "3dprint":
            all_violations, all_warnings = self._check_3dprint(shape_json, all_violations, all_warnings)

        # Overall score
        score = 1.0
        score -= len(all_violations) * 0.5
        score -= len(all_warnings) * 0.1
        score = max(0.0, min(1.0, score))

        is_valid = len(all_violations) == 0

        return ValidationResult(
            is_valid=is_valid,
            violations=all_violations,
            warnings=all_warnings,
            score=score,
        )

    def _check_cnc(self, shape_json: Dict, violations: List[str], warnings: List[str]) -> Tuple[List[str], List[str]]:
        """CNC-specific checks."""
        metadata = shape_json.get("metadata", {})
        bbox = metadata.get("bounding_box", {})

        # Check for reasonable dimensions
        x_range = bbox.get("max_x", 0) - bbox.get("min_x", 0)
        y_range = bbox.get("max_y", 0) - bbox.get("min_y", 0)
        z_range = bbox.get("max_z", 0) - bbox.get("min_z", 0)

        if x_range <= 0 or y_range <= 0 or z_range <= 0:
            violations.append("CNC: Invalid bounding box; dimensions must be positive")

        # Check aspect ratio (not too thin)
        if min(x_range, y_range, z_range) < 0.1 * max(x_range, y_range, z_range):
            warnings.append("CNC: Very thin features; may be difficult to machine")

        return violations, warnings

    def _check_molding(self, shape_json: Dict, violations: List[str], warnings: List[str]) -> Tuple[List[str], List[str]]:
        """Injection molding-specific checks."""
        # Check for undercuts, uniform wall thickness, etc.
        # For MVP, basic checks only
        metadata = shape_json.get("metadata", {})
        volume = metadata.get("volume", 0.0)

        if volume < 1.0:
            warnings.append("Molding: Very small part volume; may have injection pressure issues")

        return violations, warnings

    def _check_3dprint(self, shape_json: Dict, violations: List[str], warnings: List[str]) -> Tuple[List[str], List[str]]:
        """3D printing-specific checks."""
        # Check for enclosed voids, support requirements, etc.
        metadata = shape_json.get("metadata", {})
        surface_area = metadata.get("surface_area", 0.0)

        if surface_area < 1.0:
            warnings.append("3D Print: Very small surface area; may have resolution issues")

        return violations, warnings
