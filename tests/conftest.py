import pytest

from web.app import create_app


@pytest.fixture
def app(aiohttp_client, loop):
    web_app = create_app()
    web_app.on_startup.clear()
    return loop.run_until_complete(aiohttp_client(web_app))
