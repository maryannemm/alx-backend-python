#!/usr/bin/env python3
"""
This module contains an asynchronous function that waits for a random delay.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous function that waits for a random delay between 0 and max_delay seconds.

    Args:
        max_delay (int): Maximum delay in seconds (default is 10).

    Returns:
        float: The random delay time.
    """
    delay = random.uniform(0, max_delay)  # Get a random float between 0 and max_delay
    await asyncio.sleep(delay)  # Wait asynchronously for the delay
    return delay

