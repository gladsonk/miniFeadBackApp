from app.models.feedback import FeedbackCreate, FeedbackResponse
from datetime import datetime
from datetime import timezone

class FeedbackService:
    """Service for managing feedback operations"""

    def __init__(self, db):
        self.db = db
        self.collection = db.feedback

    async def create(self, feedback: FeedbackCreate) -> FeedbackResponse:
        """Create a new feedback entry in the database"""
        feedback_dict = feedback.model_dump()

        feedback_dict["created_at"] = datetime.now(timezone.utc)
        result = await self.collection.insert_one(feedback_dict)
        return FeedbackResponse(
            id=str(result.inserted_id),
            name=feedback_dict["name"],
            email=feedback_dict["email"],
            rating=feedback_dict["rating"],
            message=feedback_dict["message"],
            created_at=feedback_dict["created_at"]
        )
    
    async def get_all(self) -> list[FeedbackResponse]:
        """Retrieve all feedback entries from the database"""
        # await the find coroutine to obtain the cursor, then apply sort
        cursor = await self.collection.find()
        feedback_list = await cursor.to_list(length=None)
        return [
            FeedbackResponse(
                id=str(fb["_id"]),
                name=fb["name"],
                email=fb["email"],
                rating=fb["rating"],
                message=fb["message"],
                created_at=fb["created_at"]
            ) for fb in feedback_list
        ]
    
    