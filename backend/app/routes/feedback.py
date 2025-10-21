from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from app.models.feedback import FeedbackCreate, FeedbackResponse
from app.services.feedback_services import FeedbackService
from app.config.database import get_database


router = APIRouter(prefix="/api/feedback", tags=["Feedback"])

feedback_service = None

async def get_feedback_service():
    """Dependency to get feedback service"""
    global feedback_service
    if feedback_service is None:
        db = await get_database()
        feedback_service = FeedbackService(db)
    return feedback_service

    
@router.post("", response_model=FeedbackResponse, status_code=status.HTTP_201_CREATED)
async def create_feedback(
    feedback: FeedbackCreate,
    service: FeedbackService = Depends(get_feedback_service)
):
    """Create new feedback entry"""
    try:
        return await service.create(feedback)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to create feedback: {str(e)}"
        )


@router.get("", response_model=List[FeedbackResponse])
async def get_all_feedback(
    service: FeedbackService = Depends(get_feedback_service)
):
    """Get all feedback entries"""
    try:
        return await service.get_all()
    except Exception as e:  
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to retrieve feedback: {str(e)}"
        )
