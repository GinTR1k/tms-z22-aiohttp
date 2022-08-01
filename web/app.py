from aiohttp import web
from aiohttp.web_middlewares import middleware
from aiohttp.web_response import json_response

from web.api.index import route as index_route
from web.api.healthcheck import route as healthcheck_route
from web.api.v1 import app as v1_app
from web.api.v2 import app as v2_app
from web.startups import setup_database


def plugin_app(app, prefix, nested):
    async def set_db(a):
        a['db'] = app['db']
        a['db_session'] = app['db_session']

    nested.on_startup.append(set_db)
    app.add_subapp(prefix, nested)


@middleware
async def json_middleware(request, handler):
    resp = await handler(request)
    return json_response(resp)


app = web.Application(middlewares=[json_middleware])
app.on_startup.append(setup_database)

app.router.add_routes(index_route)
app.router.add_routes(healthcheck_route)

plugin_app(app, '/v1', v1_app)
plugin_app(app, '/v2', v2_app)


if __name__ == '__main__':
    web.run_app(app, host="127.0.0.1")
