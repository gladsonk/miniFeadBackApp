# /D:/Programs/interview_task/miniFeadBackApp/backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import feedback
from app.config.database import init_db, close_db


from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize and close database connections using lifespan."""
    await init_db()
    try:
        yield
    finally:
        await close_db()

app = FastAPI(title="Feedback API", version="1.0.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["root"])
async def read_root():
    return {"message": "Feedback App"}

app.include_router(feedback.router)
