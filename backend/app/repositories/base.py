from app.db import MongoManager


class BaseRepository:

    collection_name: str

    @property
    def collection(self):
        return MongoManager.database[
            self.collection_name
        ]

    async def create(self, document: dict):

        return await self.collection.insert_one(
            document
        )

    async def get(self, query: dict):

        return await self.collection.find_one(
            query
        )

    async def find_many(self, query: dict):

        cursor = self.collection.find(query)

        return await cursor.to_list(length=100)

    async def update(
        self,
        query: dict,
        update: dict
    ):
        return await self.collection.update_one(
            query,
            {"$set": update}
        )