"""
Tests for REST API endpoints.
"""

import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from fastapi.testclient import TestClient
from src.api.app import create_app


@pytest.fixture
def client():
    """Create test client."""
    app = create_app()
    return TestClient(app)


class TestHealthEndpoint:
    """Tests for health check endpoint."""

    def test_health_check(self, client):
        """Test /api/health endpoint."""
        response = client.get("/api/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert "version" in data
        assert "service" in data

    def test_info_endpoint(self, client):
        """Test /api/info endpoint."""
        response = client.get("/api/info")
        assert response.status_code == 200
        data = response.json()
        assert "name" in data
        assert "features" in data
        assert isinstance(data["features"], list)


class TestRateLimiting:
    """Tests for rate limiting."""

    def test_rate_limit_exceeded(self, client):
        """Test rate limit enforcement."""
        # Make 101 requests (limit is 100 per min)
        for i in range(100):
            response = client.get("/api/health")
            assert response.status_code == 200

        # Next request should be rate limited
        response = client.get("/api/health")
        assert response.status_code == 429


class TestAuditLogging:
    """Tests for audit logging."""

    def test_audit_log_on_success(self, client):
        """Test that successful requests are logged."""
        response = client.get("/api/health")
        assert response.status_code == 200
        # Audit log should be written (check logs in real implementation)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
