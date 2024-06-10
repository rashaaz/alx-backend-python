#!/usr/bin/env python3
""" This module contains a function to measure """

from asyncio import run
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measures the total execution time """
    start = time()

    run(wait_n(n, max_delay))

    end = time()

    return (end - start) / n
