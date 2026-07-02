from litestar import Litestar

from app.controllers.home import HomeController

app = Litestar(route_handlers=[HomeController])