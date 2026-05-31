from motor.motor_asyncio import AsyncIOMotorClient

from app.config import settings


class MongoManager:

    client = None
    database = None

    @classmethod
    async def connect(cls):

        cls.client = AsyncIOMotorClient(
            settings.MONGO_URI
        )

        cls.database = cls.client[
            settings.MONGO_DB_NAME
        ]

    @classmethod
    async def close(cls):

        if cls.client:
            cls.client.close()