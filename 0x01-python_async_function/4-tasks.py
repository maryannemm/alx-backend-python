#!/usr/bin/env python3
"""
This module contains a function that runs multiple asyncio Tasks concurrently.
"""

import asyncio
from typing import List
from 3-tasks import task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run task_wait_random n times concurrently and return the delays in ascending order.

    Args:
        n (int): Number of times to spawn task_wait_random.
        max_delay (int): Maximum delay for task_wait_random.

    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    
    # Collect completed results in the order they finish
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    
    return delays

