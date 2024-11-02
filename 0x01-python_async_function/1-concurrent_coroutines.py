#!/usr/bin/env python3
'''Asynchronous Python example
'''
import asyncio
from typing import List

# Importing the wait_random function from 0-basic_async_syntax
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Returns a sorted list of results from wait_random function calls
    '''
    # Using asyncio.gather to run multiple instances of wait_random concurrently
    res = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    # Returning the sorted list of results
    return sorted(res)

