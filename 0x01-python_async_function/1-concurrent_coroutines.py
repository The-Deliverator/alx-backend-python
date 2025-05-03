#!/usr/bin/env python3
"""uses async to make multiple routines"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times and returns
    a sorted list of delays in ascending order.
    """
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)

        # Insert delay in the correct position to keep list sorted
        index = 0
        while index < len(delays) and delays[index] < delay:
            index += 1
        delays.insert(index, delay)

    return delays
