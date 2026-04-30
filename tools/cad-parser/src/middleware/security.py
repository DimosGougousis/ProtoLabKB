"""
Security middleware for authentication and rate limiting.

For MVP: Mocked authentication (local testing only).
Production deployment requires WP01-WP04 completion for real auth/encryption.
"""

import logging
from datetime import datetime, timedelta
from typing import Dict, Callable
from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response


logger = logging.getLogger(__name__)


class SecurityMiddleware(BaseHTTPMiddleware):
    """
    Security middleware for auth and rate limiting.

    MVP Features (local testing):
    - Bearer token validation (stub)
    - Rate limiting (100 req/min per IP)

    Production (WP01-WP04):
    - Real OAuth2/mTLS auth
    - Encryption at rest/transit
    - Adversarial defense
    """

    def __init__(self, app):
        super().__init__(app)
        self.request_log: Dict[str, list] = {}  # IP -> list of timestamps
        self.rate_limit_req_per_min = 100

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        """Process request with security checks."""
        # Get client IP
        client_ip = request.client.host if request.client else "unknown"

        # Check rate limit
        if not self._check_rate_limit(client_ip):
            logger.warning(f"Rate limit exceeded for {client_ip}")
            raise HTTPException(status_code=429, detail="Rate limit exceeded")

        # Check auth token (for MVP, optional)
        auth_header = request.headers.get("authorization", "")
        if auth_header and not self._validate_token(auth_header):
            logger.warning(f"Invalid auth token from {client_ip}")
            raise HTTPException(status_code=401, detail="Invalid authentication")

        response = await call_next(request)
        return response

    def _check_rate_limit(self, client_ip: str) -> bool:
        """Check if client has exceeded rate limit."""
        now = datetime.utcnow()
        cutoff = now - timedelta(minutes=1)

        # Initialize or clean up old entries
        if client_ip not in self.request_log:
            self.request_log[client_ip] = []

        # Remove old entries
        self.request_log[client_ip] = [ts for ts in self.request_log[client_ip] if ts > cutoff]

        # Check limit
        if len(self.request_log[client_ip]) >= self.rate_limit_req_per_min:
            return False

        # Record this request
        self.request_log[client_ip].append(now)
        return True

    def _validate_token(self, auth_header: str) -> bool:
        """
        Validate Bearer token.

        MVP: Accept any token starting with 'Bearer '.
        Production: Verify JWT signature, expiry, etc.
        """
        try:
            parts = auth_header.split()
            if len(parts) != 2 or parts[0].lower() != "bearer":
                return False

            token = parts[1]
            # For MVP, just check it's not empty
            return len(token) > 0
        except Exception:
            return False
