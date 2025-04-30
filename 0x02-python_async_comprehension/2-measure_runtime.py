#!/usr/bin/env python3
"""
This module provides an asynchronous function that measures the runtime
of running 4 instances of the async_comprehension function from the
'1-async_comprehension' module
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
     """
    Asynchronous function that measures and returns the runtime of
    running 4 instances of the async_comprehension function.

    Returns:
        float: The runtime of the async_comprehension function in seconds.
    """

    start_time = time.perf_counter()

    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
    )
    end_time = time.perf_counter()

    return time.perf_counter() - start_time
