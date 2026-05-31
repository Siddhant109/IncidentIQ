from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api import health_router
from app.config import settings
from app.core import configure_logging
from app.db import MongoManager


@asynccontextmanager
async def lifespan(app: FastAPI):

    configure_logging()

    await MongoManager.connect()

    yield

    await MongoManager.close()


app = FastAPI(
    title=settings.PROJECT_NAME,
    lifespan=lifespan,
)

app.include_router(
    health_router,
    tags=["Health"]
)