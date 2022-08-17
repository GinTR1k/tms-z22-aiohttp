import pytest


@pytest.mark.asyncio
async def test_always_ok(app):
    resp = await app.get('/v1/always_ok')
    assert resp.status == 200

    result = await resp.json()
    assert result == {
        'status': 'ok',
        'data': {
            'message': 'i\'m always ok',
        },
    }


@pytest.mark.asyncio
async def test_always_ok2(app):
    resp = await app.get('/v1/always_ok')
    assert resp.status == 200

    result = await resp.json()
    assert result == {
        'status': 'ok',
        'data': {
            'message': 'i\'m always ok',
        },
    }
