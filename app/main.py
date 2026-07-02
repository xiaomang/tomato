from litestar import Litestar
from litestar.di import Provide
from app import lifespan, dependencies
from app.controllers.home import HomeController

app = Litestar(
    route_handlers=[HomeController],
    lifespan=[lifespan.connect_mongo_db],
    dependencies={
        'db': Provide(dependencies.provide_mongo_db),
    },
)
