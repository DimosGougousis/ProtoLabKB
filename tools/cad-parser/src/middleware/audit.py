"""
Audit middleware for compliance and governance.

Logs all requests/responses with compliance flags (regulated, ITAR, FDA, etc.)
for audit trails and governance reporting.
"""

import logging
import json
from datetime import datetime
from typing import Callable
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response


logger = logging.getLogger(__name__)


class AuditMiddleware(BaseHTTPMiddleware):
    """
    Middleware to log and audit all API requests/responses.

    Captures:
    - Request metadata (method, path, user, timestamp)
    - Compliance flags (ITAR, FDA, aerospace, etc.)
    - Response status and timing
    """

    REGULATED_KEYWORDS = {
        "itar": "ITAR",
        "defense": "ITAR",
        "military": "ITAR",
        "aerospace": "Aerospace",
        "faa": "FAA",
        "as9100": "Aerospace",
        "fda": "FDA",
        "medical": "FDA",
        "iso 13485": "Medical",
        "biocompatible": "Medical",
    }

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        """Process request and log audit entry."""
        start_time = datetime.utcnow()

        # Extract request info
        method = request.method
        path = request.url.path
        query_string = request.url.query

        # Detect compliance flags from query/path
        regulated_flag = self._detect_regulated(path + " " + query_string)

        # Call next middleware/route
        response = await call_next(request)

        # Calculate timing
        elapsed_ms = (datetime.utcnow() - start_time).total_seconds() * 1000

        # Log audit entry
        audit_entry = {
            "timestamp": start_time.isoformat(),
            "method": method,
            "path": path,
            "status_code": response.status_code,
            "elapsed_ms": elapsed_ms,
            "regulated": regulated_flag is not None,
            "regulated_category": regulated_flag,
        }

        if response.status_code >= 400:
            logger.warning(f"Audit: {json.dumps(audit_entry)}")
        else:
            logger.info(f"Audit: {json.dumps(audit_entry)}")

        return response

    def _detect_regulated(self, text: str) -> str | None:
        """Detect regulated keywords in text."""
        text_lower = text.lower()
        for keyword, category in self.REGULATED_KEYWORDS.items():
            if keyword in text_lower:
                return category
        return None
