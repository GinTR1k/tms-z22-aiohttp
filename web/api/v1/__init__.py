from aiohttp import web
from .always_ok import route as always_ok_route

app = web.Application()
app.router.add_routes(always_ok_route)
