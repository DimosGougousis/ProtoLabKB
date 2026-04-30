"""
CAD geometry processing module.

Provides B-Rep (Boundary Representation) operations, topological validation,
and mesh-to-B-Rep conversion using OpenCASCADE.
"""

from .brep_engine import BRepEngine
from .validators import TopologicalValidator, WatertightnessValidator
from .mesh_to_brep import MeshToBRepConverter

__all__ = [
    "BRepEngine",
    "TopologicalValidator",
    "WatertightnessValidator",
    "MeshToBRepConverter",
]
