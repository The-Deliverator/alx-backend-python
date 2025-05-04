#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns task_wait_random n times and returns
    a list of delays in ascending order."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    ordered_delays = []
    for delay in delays:
        index = 0
        while index < len(ordered_delays) and ordered_delays[index] < delay:
            index += 1
        ordered_delays.insert(index, delay)

    return ordered_delays
