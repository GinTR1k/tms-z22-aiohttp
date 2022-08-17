import logging
from datetime import datetime

from aiohttp import web
from aiohttp.web_request import Request

route = web.RouteTableDef()

logger = logging.getLogger(__name__)


@route.get('/health')
@route.get('/new_health')
async def health(request: Request):
    try:
        async with request.app['db_session']() as session:
            await session.execute('SELECT 1')
        is_db_ok = True
    except Exception as e:
        is_db_ok = False
        logger.exception(e)

    return {
        'time': datetime.utcnow().isoformat(),
        'status': all([is_db_ok]),
        'services': {
            'db': is_db_ok,
        },
    }
