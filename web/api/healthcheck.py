from aiohttp import web
from aiohttp.web_request import Request

route = web.RouteTableDef()


@route.get('/health')
@route.get('/new_health')
async def health(request: Request):
    return {'message': 'ok'}
