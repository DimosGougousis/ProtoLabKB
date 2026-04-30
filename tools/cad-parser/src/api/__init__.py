"""
CAD Parser API package.

REST API for B-Rep processing, DFM analysis, and generative design.
"""

from .app import create_app

__all__ = ["create_app"]
