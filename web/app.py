import logging

from aiohttp import web
from aiohttp.web_middlewares import middleware
from aiohttp.web_response import json_response

from web.api.index import route as index_route
from web.api.healthcheck import route as healthcheck_route
from web.api.v1 import app as v1_app
from web.api.v2 import app as v2_app
from web.startups import run_background_tasks, setup_database

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s - %(message)s', level=logging.INFO)


def plugin_app(app, prefix, nested):
    async def set_db(a):
        a['db'] = app['db']
        a['db_session'] = app['db_session']

    nested.on_startup.append(set_db)
    app.add_subapp(prefix, nested)


@middleware
async def json_middleware(request, handler):
    resp = await handler(request)
    return json_response({
        'status': 'ok',
        'data': resp,
    })


def create_app(app=None):
    logger.info('Configuring app...')
    app = app or web.Application(middlewares=[json_middleware])
    app.on_startup.append(setup_database)

    app.router.add_routes(index_route)
    app.router.add_routes(healthcheck_route)

    plugin_app(app, '/v1', v1_app)
    plugin_app(app, '/v2', v2_app)

    app.on_startup.append(run_background_tasks)
    return app


if __name__ == '__main__':
    logger.debug('Starting web server...')
    web.run_app(create_app(), host="127.0.0.1")
    logger.debug('Stopped web server')
