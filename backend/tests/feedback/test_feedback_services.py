import pytest
from datetime import datetime, timezone
import asyncio
from app.models.feedback import FeedbackCreate, FeedbackResponse
from unittest.mock import AsyncMock, MagicMock, patch
from app.services.feedback_services import FeedbackService

@pytest.fixture
def mock_db():
    """Create mock database"""
    db = MagicMock()
    db.feedback = MagicMock()
    return db

@pytest.fixture
def feedback_service(mock_db):
    """Create feedback service with mock db"""
    return FeedbackService(mock_db)

@pytest.fixture
def sample_feedback_create():
    """Sample feedback data"""
    return FeedbackCreate(
        name="John Doe",
        email="john@example.com",
        message="Great service!",
        rating=5
    )
def test_create_feedback(feedback_service, mock_db, sample_feedback_create):
    """Test creating feedback"""
    mock_insert_result = MagicMock()
    mock_insert_result.inserted_id = "507f1f77bcf86cd799439011"
    mock_db.feedback.insert_one = AsyncMock(return_value=mock_insert_result)

    result = asyncio.run(feedback_service.create(sample_feedback_create))

    mock_db.feedback.insert_one.assert_awaited_once()
    assert result.id == "507f1f77bcf86cd799439011"
    assert result.name == sample_feedback_create.name
    assert result.email == sample_feedback_create.email
    assert result.rating == sample_feedback_create.rating
    assert result.message == sample_feedback_create.message
    assert isinstance(result.created_at, datetime)
    assert isinstance(result.created_at, datetime)

def test_get_all_feedback_retrun_all(feedback_service, mock_db):
    """Test retrieving all feedback"""
    sample_feedbacks = [
        {
            "_id": "507f1f77bcf86cd799439011",
            "name": "John Doe",
            "email": "John@example.com",
            "message": "Great service!",
            "rating": 5,
            "created_at": datetime.now(timezone.utc)
        }]

    mock_cursor = MagicMock()
    mock_cursor.to_list = AsyncMock(return_value=sample_feedbacks)
    mock_db.feedback.find = AsyncMock(return_value=mock_cursor)

    results = asyncio.run(feedback_service.get_all())

    assert len(results) == 1
    assert results[0].id == "507f1f77bcf86cd799439011"
    assert results[0].name == "John Doe"


def test_get_all_feedback_returns_empty_list_when_no_data(feedback_service, mock_db):
    """Test get_all_feedback returns empty list when no feedback exists"""

    mock_cursor = MagicMock()
    mock_cursor.to_list = AsyncMock(return_value=[])
    mock_db.feedback.find = AsyncMock(return_value=mock_cursor)

    result = asyncio.run(feedback_service.get_all())
    assert result == []
