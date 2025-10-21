# /D:/Programs/interview_task/miniFeadBackApp/backend/app/main.py
from fastapi import FastAPI

app = FastAPI(title="Feedback API", version="1.0.0")

@app.get("/", tags=["root"])
async def read_root():
    return {"message": "Feedback App"}
