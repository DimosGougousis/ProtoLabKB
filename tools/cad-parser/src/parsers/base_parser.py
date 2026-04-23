"""
Base parser class for CAD file formats.
Defines the interface that all parsers must implement.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Dict, Any, Optional
from pathlib import Path


@dataclass
class BoundingBox:
    """3D bounding box"""
    min_x: float
    min_y: float
    min_z: float
    max_x: float
    max_y: float
    max_z: float
    
    @property
    def width(self) -> float:
        return self.max_x - self.min_x
    
    @property
    def height(self) -> float:
        return self.max_y - self.min_y
    
    @property
    def depth(self) -> float:
        return self.max_z - self.min_z
    
    @property
    def center(self) -> List[float]:
        return [
            (self.min_x + self.max_x) / 2,
            (self.min_y + self.max_y) / 2,
            (self.min_z + self.max_z) / 2
        ]
    
    def to_dict(self) -> Dict[str, float]:
        return {
            'min': [self.min_x, self.min_y, self.min_z],
            'max': [self.max_x, self.max_y, self.max_z],
            'dimensions': [self.width, self.height, self.depth],
            'center': self.center
        }


@dataclass
class GeometryData:
    """Extracted geometry data from CAD file"""
    bounding_box: BoundingBox
    volume: float
    surface_area: float
    center_of_mass: List[float]
    format: str
    file_path: str
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'bounding_box': self.bounding_box.to_dict(),
            'volume': self.volume,
            'surface_area': self.surface_area,
            'center_of_mass': self.center_of_mass,
            'format': self.format,
            'file_path': self.file_path
        }


class BaseParser(ABC):
    """Abstract base class for CAD parsers"""
    
    def __init__(self):
        self.supported_extensions: List[str] = []
        self.format_name: str = ""
    
    @abstractmethod
    def parse(self, file_path: str) -> GeometryData:
        """
        Parse a CAD file and extract geometry data.
        
        Args:
            file_path: Path to the CAD file
            
        Returns:
            GeometryData object with extracted information
            
        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If file format is invalid
            RuntimeError: If parsing fails
        """
        pass
    
    @abstractmethod
    def can_parse(self, file_path: str) -> bool:
        """
        Check if this parser can handle the given file.
        
        Args:
            file_path: Path to the file
            
        Returns:
            True if this parser can parse the file
        """
        pass
    
    def validate_file(self, file_path: str) -> None:
        """Validate that file exists and is readable"""
        path = Path(file_path)
        
        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        if not path.is_file():
            raise ValueError(f"Path is not a file: {file_path}")
        
        if path.stat().st_size == 0:
            raise ValueError(f"File is empty: {file_path}")
    
    def calculate_bounding_box(self, vertices: List[List[float]]) -> BoundingBox:
        """Calculate bounding box from list of vertices"""
        if not vertices:
            return BoundingBox(0, 0, 0, 0, 0, 0)
        
        xs = [v[0] for v in vertices]
        ys = [v[1] for v in vertices]
        zs = [v[2] for v in vertices]
        
        return BoundingBox(
            min_x=min(xs),
            min_y=min(ys),
            min_z=min(zs),
            max_x=max(xs),
            max_y=max(ys),
            max_z=max(zs)
        )
