#!/usr/bin/env python3
"""
CAD Parser Service - FastAPI Application
ProtoLabs Product Office

This service provides CAD file parsing, feature extraction, and visualization generation.
Supports STEP, STL, OBJ, and 3MF formats.
"""

import os
import sys
import json
import logging
from pathlib import Path
from typing import Optional, List, Dict, Any
from datetime import datetime
from fastapi import FastAPI, File, UploadFile, HTTPException, BackgroundTasks
from fastapi.responses import JSONResponse, FileResponse
from pydantic import BaseModel, Field
import uvicorn

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from parsers.step_parser import STEPParser
from parsers.stl_parser import STLParser
from parsers.obj_parser import OBJParser
from visualizers.two_d_generator import TwoDGenerator
from visualizers.three_d_generator import ThreeDGenerator
from analyzers.feature_detector import FeatureDetector
from analyzers.dfm_pre_checker import DFMPreChecker

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="CAD Parser Service",
    description="Parse CAD files and generate visualizations for DFM analysis",
    version="1.0.0"
)

# Configuration
OUTPUT_DIR = Path(os.getenv('CAD_OUTPUT_DIR', './output'))
OUTPUT_DIR.mkdir(exist_ok=True)

ALLOWED_EXTENSIONS = {'.step', '.stp', '.stl', '.obj', '.3mf'}
MAX_FILE_SIZE = 100 * 1024 * 1024  # 100MB

# Pydantic Models
class GeometryData(BaseModel):
    bounding_box: Dict[str, float]
    volume: float
    surface_area: float
    center_of_mass: List[float]

class FeatureSummary(BaseModel):
    hole_count: int
    pocket_count: int
    boss_count: int
    fillet_count: int
    chamfer_count: int
    thread_count: int

class VisualizationPaths(BaseModel):
    front: str
    top: str
    side: str
    iso: str
    viewer_3d: str

class DFMPreAnalysis(BaseModel):
    process_hints: List[str]
    critical_issues: List[Dict]
    warnings: List[Dict]
    notes: List[Dict]

class CADParseResponse(BaseModel):
    success: bool
    file_info: Dict[str, Any]
    geometry: GeometryData
    features: FeatureSummary
    feature_details: Dict[str, List[Dict]]
    visualizations: VisualizationPaths
    dfm_pre_analysis: DFMPreAnalysis
    output_directory: str
    processing_time_ms: int

class HealthResponse(BaseModel):
    status: str
    version: str
    supported_formats: List[str]

# Helper Functions
def get_file_extension(filename: str) -> str:
    return Path(filename).suffix.lower()

def validate_file(file: UploadFile) -> None:
    """Validate uploaded file"""
    ext = get_file_extension(file.filename)
    
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file format: {ext}. Allowed: {', '.join(ALLOWED_EXTENSIONS)}"
        )
    
    # Check file size (read first chunk)
    file.file.seek(0, 2)  # Seek to end
    size = file.file.tell()
    file.file.seek(0)  # Reset to beginning
    
    if size > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail=f"File too large: {size / 1024 / 1024:.1f}MB. Max: {MAX_FILE_SIZE / 1024 / 1024:.0f}MB"
        )

def get_parser(file_extension: str):
    """Get appropriate parser for file type"""
    parsers = {
        '.step': STEPParser,
        '.stp': STEPParser,
        '.stl': STLParser,
        '.obj': OBJParser,
        '.3mf': STLParser  # 3MF uses similar mesh structure
    }
    
    return parsers.get(file_extension)

# API Endpoints
@app.get("/", response_model=HealthResponse)
async def root():
    """Service health check"""
    return HealthResponse(
        status="healthy",
        version="1.0.0",
        supported_formats=list(ALLOWED_EXTENSIONS)
    )

@app.post("/parse", response_model=CADParseResponse)
async def parse_cad(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    process_hint: Optional[str] = None,
    vertical: Optional[str] = None,
    material: Optional[str] = None
):
    """
    Parse a CAD file and extract geometry, features, and generate visualizations.
    
    - **file**: CAD file (STEP, STL, OBJ, 3MF)
    - **process_hint**: Optional process hint (cnc, injection, 3d-printing, sheet-metal)
    - **vertical**: Optional industry vertical (aerospace, medical, automotive)
    - **material**: Optional material specification
    """
    start_time = datetime.now()
    
    # Validate file
    validate_file(file)
    
    # Save uploaded file
    file_ext = get_file_extension(file.filename)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_subdir = OUTPUT_DIR / f"{Path(file.filename).stem}_{timestamp}"
    output_subdir.mkdir(exist_ok=True)
    
    file_path = output_subdir / f"input{file_ext}"
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
    
    logger.info(f"Saved uploaded file to {file_path}")
    
    try:
        # Get appropriate parser
        parser_class = get_parser(file_ext)
        if not parser_class:
            raise HTTPException(status_code=400, detail=f"No parser available for {file_ext}")
        
        parser = parser_class()
        
        # Parse geometry
        logger.info("Parsing geometry...")
        geometry = parser.parse(str(file_path))
        
        # Extract features
        logger.info("Detecting features...")
        feature_detector = FeatureDetector()
        features = feature_detector.detect_all(geometry)
        
        # Generate visualizations
        logger.info("Generating visualizations...")
        viz_2d = TwoDGenerator()
        viz_3d = ThreeDGenerator()
        
        visualizations = {
            'front': viz_2d.generate_view(geometry, 'front', output_subdir / 'front.png'),
            'top': viz_2d.generate_view(geometry, 'top', output_subdir / 'top.png'),
            'side': viz_2d.generate_view(geometry, 'side', output_subdir / 'side.png'),
            'iso': viz_2d.generate_view(geometry, 'iso', output_subdir / 'iso.png'),
            'viewer_3d': viz_3d.generate_viewer(geometry, output_subdir / 'viewer.html')
        }
        
        # Pre-DFM analysis
        logger.info("Running DFM pre-analysis...")
        dfm_checker = DFMPreChecker()
        dfm_analysis = dfm_checker.analyze(geometry, features, process_hint)
        
        # Calculate processing time
        processing_time = int((datetime.now() - start_time).total_seconds() * 1000)
        
        # Build response
        response = CADParseResponse(
            success=True,
            file_info={
                "filename": file.filename,
                "format": file_ext.replace('.', '').upper(),
                "size_bytes": file_path.stat().st_size,
                "saved_path": str(file_path)
            },
            geometry=GeometryData(
                bounding_box=geometry.bounding_box,
                volume=geometry.volume,
                surface_area=geometry.surface_area,
                center_of_mass=geometry.center_of_mass
            ),
            features=FeatureSummary(
                hole_count=len(features.get('holes', [])),
                pocket_count=len(features.get('pockets', [])),
                boss_count=len(features.get('bosses', [])),
                fillet_count=len(features.get('fillets', [])),
                chamfer_count=len(features.get('chamfers', [])),
                thread_count=len(features.get('threads', []))
            ),
            feature_details=features,
            visualizations=VisualizationPaths(
                front=str(visualizations['front']),
                top=str(visualizations['top']),
                side=str(visualizations['side']),
                iso=str(visualizations['iso']),
                viewer_3d=str(visualizations['viewer_3d'])
            ),
            dfm_pre_analysis=DFMPreAnalysis(
                process_hints=dfm_analysis.get('process_hints', []),
                critical_issues=dfm_analysis.get('critical_issues', []),
                warnings=dfm_analysis.get('warnings', []),
                notes=dfm_analysis.get('notes', [])
            ),
            output_directory=str(output_subdir),
            processing_time_ms=processing_time
        )
        
        logger.info(f"Successfully processed {file.filename} in {processing_time}ms")
        return response
        
    except Exception as e:
        logger.error(f"Error processing CAD file: {str(e)}")
        raise HTTPException(status_code=500, detail=f"CAD processing error: {str(e)}")

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "output_directory": str(OUTPUT_DIR),
        "supported_formats": list(ALLOWED_EXTENSIONS)
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
