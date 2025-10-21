from pydantic import BaseModel, Field, field_validator, ConfigDict
from datetime import datetime
from typing import Optional
import re

class feedbackCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: Optional[str] = Field(None, max_length=254)
    message: str = Field(..., min_length=5, max_length=500)
    rating: int = Field(..., ge=1, le=5)

    @field_validator('name')
    def name_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('Name must not be empty')
        return v
    
    @field_validator('message')
    def message_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('Message must not be empty')
        return v
    
    @field_validator('email')
    def email_must_be_valid(cls, v):
        if v is None:
            return v
        v = v.strip()
        if not v:
            raise ValueError('Email must not be empty')
        if not re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', v):
            raise ValueError('Invalid email address')
        return v
    
class FeedbackResponse(BaseModel):
    """Schema for feedback response"""
    id: str
    name: str
    email: str
    rating: int
    comment: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
