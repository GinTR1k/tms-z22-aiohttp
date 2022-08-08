import logging

import aiohttp
from aiohttp import web
from faker import Faker

logger = logging.getLogger(__name__)

faker = Faker()


def get_random_name():
    return faker.name()


async def ws(request):
    ws_current = web.WebSocketResponse()
    ws_ready = ws_current.can_prepare(request)

    if not ws_ready.ok:
        return

    await ws_current.prepare(request)

    name = get_random_name()
    logger.info(f'{name} joined.')

    await ws_current.send_json({'action': 'connect', 'name': name})

    for ws in request.app['websockets'].values():
        await ws.send_json({'action': 'join', 'name': name})

    request.app['websockets'][name] = ws_current

    while True:
        msg = await ws_current.receive()

        if msg.type != aiohttp.WSMsgType.text:
            break

        for ws in request.app['websockets'].values():
            if ws is not ws_current:
                await ws.send_json(
                    {'action': 'sent', 'name': name, 'text': msg.data}
                )

    del request.app['websockets'][name]
    logger.info('%s disconnected.', name)
    for ws in request.app['websockets'].values():
        await ws.send_json({'action': 'disconnect', 'name': name})

    return ws_current
