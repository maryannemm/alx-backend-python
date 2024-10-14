#!/usr/bin/env python3
'''Example of asynchronous Python code
'''
import time
import asyncio

# Loading the wait_n function from 1-concurrent_coroutines module
wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    '''Measures the average time taken for wait_n to complete
    '''
    start = time.time()  # Capture the initial time
    asyncio.run(wait_n(n, max_delay))  # Execute the wait_n function asynchronously
    # Compute the total runtime and return the average time per execution
    return (time.time() - start) / n

