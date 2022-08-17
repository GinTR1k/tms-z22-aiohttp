from aiohttp import web
from aiohttp.web_request import Request

from web.models.message import Message

route = web.RouteTableDef()


@route.get('/always_ok')
async def always_ok(request: Request):
    return {"message": "i'm always ok"}


@route.post('/new_message')
async def new_message(request: Request):
    data = await request.json()
    message = Message(**data)

    async with request.app['db_session']() as session:
        session.add(message)
        await session.commit()

    return message.to_dict()
