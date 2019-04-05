import asyncio

import aiohttp
import pytest

@pytest.fixture
def loop():
    return asyncio.get_event_loop()


@pytest.yield_fixture
async def session():
    async with aiohttp.ClientSession() as client:
        yield client
