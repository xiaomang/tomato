from litestar.datastructures import State
from motor.motor_asyncio import AsyncIOMotorDatabase


async def provide_mongo_db(state: State) -> AsyncIOMotorDatabase:
    """
    提供 MongoDB 数据库连接
    """
    return state.mongo_db
