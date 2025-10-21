import pytest 
from httpx import AsyncClient, ASGITransport
from datetime import datetime, timezone
from unittest.mock import AsyncMock, patch, MagicMock
from app.models.feedback import FeedbackResponse
from app.main import app
import asyncio

@pytest.fixture
def sample_feedback_response():
    """Fixture for a sample feedback response."""

    return FeedbackResponse(
        id="507f1f77bcf86cd799439011",
        name="John Doe",
        email="john@example.com",
        message="Great service!",
        rating=5,
        created_at=datetime.now(timezone.utc)
    )
        

def test_create_feedback_endpoint_success(sample_feedback_response):
    """Test POST /api/feedback creates feedback successfully"""
    with patch('app.routes.feedback.feedback_service') as mock_service:
        mock_service.create = AsyncMock(return_value=sample_feedback_response)
        async def run_test():
            async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
                response = await client.post(
                    "/api/feedback",
                    json={
                        "name": "John Doe",
                        "email": "john@example.com",
                        "rating": 5,
                        "message": "Excellent!"
                    }
                )
                return response
        response = asyncio.run(run_test())
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "John Doe"
    assert data["email"] == "john@example.com"
    assert data["rating"] == 5


def test_create_feedback_endpoint_validation_error():
    """Test POST /api/feedback returns 422 for invalid data"""
    async def run_test():
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
            response = await client.post(
                "/api/feedback",
                json={
                    "name": "John Doe",
                    "rating": 6 # Invalid: > 5
                }
            )
            return response
    response = asyncio.run(run_test())
    assert response.status_code == 422


def test_get_all_feedback_endpoint_success(sample_feedback_response):
    """Test GET /api/feedback returns all feedback"""
    with patch('app.routes.feedback.feedback_service') as mock_service:
        mock_service.get_all = AsyncMock(return_value=[sample_feedback_response.model_dump()])
        async def run_test():
            async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
                response = await client.get("/api/feedback")
            return response
        response = asyncio.run(run_test())

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["name"] == "John Doe"


def test_get_all_feedback_endpoint_empty_list():
    """Test GET /api/feedback returns empty list when no feedback"""
    with patch('app.routes.feedback.feedback_service') as mock_service:
        mock_service.get_all = AsyncMock(return_value=[])
        async def run_test():
            async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
                response = await client.get("/api/feedback")
            return response
        response = asyncio.run(run_test())
        assert response.status_code == 200
        assert response.json() == []
