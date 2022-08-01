from aiohttp import web
from aiohttp.web_request import Request

route = web.RouteTableDef()


@route.get('/')
@route.post('/')
async def index(request: Request):
    return ['Hello World!']
