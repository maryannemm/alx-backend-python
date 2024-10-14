#!/usr/bin/env python3
"""
This module contains a function to measure the execution time of wait_n.
"""

import time
import asyncio
from 1-concurrent_coroutines import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total runtime of wait_n(n, max_delay) and return average time per coroutine.

    Args:
        n (int): Number of coroutines to run.
        max_delay (int): Maximum delay for wait_random.

    Returns:
        float: Average time per coroutine.
    """
    start_time = time.time()  # Start the timer
    asyncio.run(wait_n(n, max_delay))  # Run wait_n with n and max_delay
    total_time = time.time() - start_time  # Calculate the total time taken

    return total_time / n  # Return the average time per coroutine

