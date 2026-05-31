from fastapi import APIRouter

from app.db import MongoManager

router = APIRouter()

@router.get("/health")
async def health():

    mongodb_status = "unknown"

    try:
        await MongoManager.database.command("ping")
        mongodb_status = "connected"
    except Exception:
        mongodb_status = "disconnected"

    return {
        "status": "healthy",
        "mongodb": mongodb_status,
    }