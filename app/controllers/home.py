from typing import Annotated

from litestar import Controller, get
from msgspec import Struct, Meta
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.settings import settings



class HomeFindResponse(Struct):
    message: Annotated[str, Meta(description="首页消息")] = "Hello, World!"


class HomeController(Controller):
    @get(summary="首页")
    async def find(self, db: AsyncIOMotorDatabase) -> HomeFindResponse:
        tests = await db.list_collection_names()
        print(tests)
        return HomeFindResponse(
            message=f"Hello, {settings.app_name}!, version {settings.app_version}, {settings.app_description}"
        )
