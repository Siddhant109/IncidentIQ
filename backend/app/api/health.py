from fastapi import APIRouter

from app.db import MongoManager
from app.kafka.producer import (
    KafkaProducerManager
)

router = APIRouter()


@router.get("/health")
async def health():

    mongo_status = "healthy"
    kafka_status = "healthy"

    try:
        await MongoManager.database.command(
            "ping"
        )
    except Exception:
        mongo_status = "unhealthy"

    try:
        if not KafkaProducerManager.producer:
            kafka_status = "unhealthy"
    except Exception:
        kafka_status = "unhealthy"

    return {
        "status": "healthy",
        "mongodb": mongo_status,
        "kafka": kafka_status,
    }