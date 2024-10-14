#!/usr/bin/env python3
"""
This module contains an async function to run multiple coroutines concurrently.
"""

import asyncio
from typing import List
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run wait_random n times concurrently and return the delays in ascending order.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay for wait_random.

    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []
    
    # Collect completed results in the order they finish
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    
    return delays

