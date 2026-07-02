import logging
from contextlib import asynccontextmanager

from litestar import Litestar
from motor.motor_asyncio import AsyncIOMotorClient

from app.settings import settings

@asynccontextmanager
async def connect_mongo_db(app: Litestar):
    """
    连接 MongoDB 数据库
    """
    logging.info("Connecting to MongoDB...")
    client = AsyncIOMotorClient(settings.mongo_uri)
    db = client.get_database(settings.mongo_db_name)
    app.state.mongo_db = db
    yield
    client.close()
    logging.info("MongoDB connection closed")
