import pytest
from datetime import datetime, timezone
from pydantic import ValidationError
from app.models.feedback import FeedbackCreate, FeedbackResponse

def test_feedback_model_creation():
    """Test creating a FeedbackModel instance with valid data"""
    feedback_data = FeedbackCreate(
        name="John Doe",
        email="john@example.com",
        message="Great service!",
        rating=5
    )
    assert feedback_data.name == "John Doe"
    assert feedback_data.email == "john@example.com"
    assert feedback_data.message == "Great service!"
    assert feedback_data.rating == 5
    # assert isinstance(feedback_data.created_at, datetime)

def test_feedback_missing_name():
    """Test that creating FeedbackModel without a name raises ValidationError"""
    with pytest.raises(ValidationError):
        FeedbackCreate(
            email="john@example.com",
            message="Great service!",
            rating=5
        )

def test_feedback_invalid_email():
    """Test that creating FeedbackModel with invalid email raises ValidationError"""
    with pytest.raises(ValidationError):
        FeedbackCreate(
            name="John Doe",
            email="invalid-email",
            message="Great service!",
            rating=5
        )

def test_feedback_invalid_rating_max_value():
    """Test that creating FeedbackModel with invalid rating raises ValidationError"""
    with pytest.raises(ValidationError):
        FeedbackCreate(
            name="John Doe",
            email="john@example.com",
            message="Great service!",
            rating=6  # Invalid rating, should be between 1 and 5
        )

def test_feedback_invalid_rating_min_value():
    """Test that creating FeedbackModel with invalid rating raises ValidationError"""
    with pytest.raises(ValidationError):
        FeedbackCreate(
            name="John Doe",
            email="john@example.com",
            message="Great service!",
            rating=0 # Invalid rating, should be between 1 and 5
        )

def test_feedback_response_includes_id_and_timestamp():
    """Test FeedbackResponse includes id and created_at"""
    feedback = FeedbackResponse(
        id="507f1f77bcf86cd799439011",
        name="John Doe",
        email="john@example.com",
        rating=5,
        message="Great!",
        created_at=datetime.now(timezone.utc)
    )
    assert feedback.id == "507f1f77bcf86cd799439011"
    assert isinstance(feedback.created_at, datetime)



