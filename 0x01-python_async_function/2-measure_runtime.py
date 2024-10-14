#!/usr/bin/env python3
'''Asynchronous Python example
'''
import time
import asyncio

# Importing the wait_n function from 1-concurrent_coroutines
wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    '''Calculates the average execution time for wait_n function
    '''
    start = time.time()  # Record the start time
    asyncio.run(wait_n(n, max_delay))  # Run wait_n with asyncio
    # Calculate total execution time and return average time per function call
    return (time.time() - start) / n

