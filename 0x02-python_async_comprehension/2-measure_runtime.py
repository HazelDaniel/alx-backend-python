#!/usr/bin/env python3
"""this measures running time for 4 async comprehensions ran in parallel"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """this function executes async_comprehension four times in parallel
        measures the total runtime and return it"""
    start_time = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    return time.perf_counter() - start_time
