#!/usr/bin/env python3
"""
This module provides an asynchronous function that measures the runtime
of running 4 instances of the async_comprehension function from the
'1-async_comprehension' module
"""
import asyncio
import time
from importlib import import_module as using

async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:

    start_time = time.perf_counter()

    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
    )
    end_time = time.perf_counter()

    return end_time - start_time
