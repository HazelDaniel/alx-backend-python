#!/usr/bin/env python3
"""Measures the total execution time for wait_n(n, max_delay)"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n, max_delay):
    """measures the total execution time for wait_n(n, max_delay)"""
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    return (end_time - start_time) / n
