from aiohttp import web
from aiohttp.web_request import Request

route = web.RouteTableDef()


@route.get('/always_ok')
async def always_ok(request: Request):
    return {'message': 'i\'m always not ok'}
