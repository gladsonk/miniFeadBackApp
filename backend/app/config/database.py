from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os
from app.config.settings import settings

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")

client: AsyncIOMotorClient = None
db = None

async def init_db():
    """Initialize database connection"""
    global client, db
    client = AsyncIOMotorClient(settings.MONGO_URL)
    db = client[settings.DB_NAME]
    print(f"Connected to MongoDB: {settings.DB_NAME}")


async def get_database():
    """Get the database instance"""
    global db
    if db is None:
        await init_db()
    return db

async def close_db():
    """Close the database connection"""
    global client
    if client:
        client.close()
        print("MongoDB connection closed")