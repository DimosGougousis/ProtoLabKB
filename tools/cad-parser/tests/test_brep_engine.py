"""
Unit tests for B-Rep engine.

Test suite for topological validation and B-Rep operations.
"""

import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.geometry import BRepEngine, TopologicalValidator, WatertightnessValidator


class TestBRepEngine:
    """Tests for BRepEngine."""

    def setup_method(self):
        """Set up test fixtures."""
        self.engine = BRepEngine()

    def test_create_box(self):
        """Test box creation."""
        box = self.engine.create_box(10, 20, 30)
        assert box is not None
        assert box["type"] == "BRepShape"
        metadata = box.get("metadata", {})
        assert metadata.get("is_valid")
        assert metadata.get("is_watertight")

    def test_create_cylinder(self):
        """Test cylinder creation."""
        cyl = self.engine.create_cylinder(radius=5, height=20)
        assert cyl is not None
        assert cyl["type"] == "BRepShape"

    def test_create_sphere(self):
        """Test sphere creation."""
        sphere = self.engine.create_sphere(radius=10)
        assert sphere is not None
        assert sphere["type"] == "BRepShape"

    def test_validate_topology(self):
        """Test Euler characteristic validation."""
        box = self.engine.create_box(10, 10, 10)
        is_valid, msg = self.engine.validate_topology(box)
        assert is_valid, msg

    def test_validate_watertightness(self):
        """Test watertightness validation."""
        box = self.engine.create_box(10, 10, 10)
        is_valid, msg = self.engine.validate_watertightness(box)
        assert is_valid, msg

    def test_compute_properties(self):
        """Test property computation."""
        box = self.engine.create_box(10, 20, 30)
        props = self.engine.compute_properties(box)
        assert props is not None
        assert "volume" in props
        assert "surface_area" in props
        assert "bounding_box" in props


class TestTopologicalValidator:
    """Tests for TopologicalValidator."""

    def setup_method(self):
        """Set up test fixtures."""
        self.validator = TopologicalValidator()
        self.engine = BRepEngine()

    def test_validate_valid_box(self):
        """Test validation of valid box."""
        box = self.engine.create_box(10, 10, 10)
        result = self.validator.validate(box)
        assert result.is_valid
        assert result.score > 0.8

    def test_validate_invalid_shape(self):
        """Test validation of invalid shape."""
        invalid_shape = {
            "type": "BRepShape",
            "metadata": {
                "vertices_count": 2,
                "edges_count": 1,
                "faces_count": 0,
                "solids_count": 0,
                "euler_characteristic": 1,
            }
        }
        result = self.validator.validate(invalid_shape)
        assert not result.is_valid
        assert len(result.violations) > 0


class TestWatertightnessValidator:
    """Tests for WatertightnessValidator."""

    def setup_method(self):
        """Set up test fixtures."""
        self.validator = WatertightnessValidator()
        self.engine = BRepEngine()

    def test_validate_watertight_box(self):
        """Test validation of watertight box."""
        box = self.engine.create_box(10, 10, 10)
        result = self.validator.validate(box)
        assert result.is_valid
        assert result.score == 1.0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
