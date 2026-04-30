"""
FastAPI application factory and configuration.

Creates the core API application with middleware, routes, and error handling.
"""

import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from src.middleware.audit import AuditMiddleware
from src.middleware.security import SecurityMiddleware


logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan context manager."""
    logger.info("Starting CAD Parser API")
    yield
    logger.info("Shutting down CAD Parser API")


def create_app() -> FastAPI:
    """
    Create and configure FastAPI application.

    Returns:
        Configured FastAPI app instance
    """
    app = FastAPI(
        title="ProtoLab CAD Parser API",
        description="AI-powered CAD parsing, analysis, and generative design API",
        version="0.1.0",
        lifespan=lifespan,
    )

    # ===== CORS Configuration =====
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000", "http://localhost:5173"],  # Dev origins
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # ===== Custom Middleware (Order: innermost last) =====
    # Security middleware validates auth tokens, rate limiting
    app.add_middleware(SecurityMiddleware)

    # Audit middleware logs all requests/responses for compliance
    app.add_middleware(AuditMiddleware)

    # ===== Health Check Endpoint =====
    @app.get("/api/health")
    async def health_check():
        """Health check endpoint."""
        return {
            "status": "ok",
            "version": "0.1.0",
            "service": "cad-parser-api",
        }

    # ===== Route Registration (Phase 1-4) =====
    # Phase 1: Placeholder routes
    @app.get("/api/info")
    async def info():
        """API information endpoint."""
        return {
            "name": "ProtoLab CAD Parser",
            "version": "0.1.0",
            "features": [
                "B-Rep parsing",
                "DFM analysis",
                "Generative design (planned)",
                "Drawing automation (planned)",
            ],
        }

    logger.info("FastAPI application created successfully")
    return app


# Instantiate the app for deployment
app = create_app()
