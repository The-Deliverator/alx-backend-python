#!/usr/bin/env python3
"""
Asychronously waits for a random delay between
0 and max_delay seconds, then returns the actual delay time.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds, then returns it.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
