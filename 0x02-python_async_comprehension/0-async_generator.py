#!/usr/bin/env python3

""" Asynchronous generator module """

from asyncio import sleep
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ This coroutine will loop 10 times, each time asynchronously """
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
