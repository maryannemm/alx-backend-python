#!/usr/bin/env python3
'''Asynchronous Python example
'''
from typing import List
import asyncio

# Importing task_wait_random function from the 3-tasks module
time_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Returns a sorted list of results from task_wait_random function calls
    '''
    # Run multiple instances of task_wait_random concurrently using asyncio.gather
    res = await asyncio.gather(
        *tuple(map(lambda _: time_wait_random(max_delay), range(n)))
    )
    # Return the results sorted in ascending order
    return sorted(res)

