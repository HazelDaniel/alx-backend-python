#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait_random process get spawned n times with the specified max_delay
        and returns the list of all the delays (float values)."""
    futures = [wait_random(max_delay) for _ in range(n)]
    futures = asyncio.as_completed(futures)
    delays = [await future for future in futures]
    return delays
