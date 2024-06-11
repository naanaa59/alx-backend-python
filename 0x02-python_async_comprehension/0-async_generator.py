#!/usr/bin/env python3
""" a python module to loop 10 times """
import random
import time
import asyncio
from typing import Generator


def async_generator() -> Generator[float, None, None]:
    """
    async_generator - function to loop 10 times
    Arguments:
        no arguments
    Returns:
        nothing
    """
    for i in range(10):
        time.sleep(1)
        yield random.uniform(0, 10)