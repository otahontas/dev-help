import pytest
from httpx import AsyncClient
from dev_help.server import app

@pytest.mark.asyncio()
async def test_app():
    """Check app starts and returns 200 from homepage"""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"hello": "world"}