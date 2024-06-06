#!/usr/bin/env python3
""" This module contains a function"""
from typing import Callable, Iterator, Union, Optional, List, Tuple


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function that multiplies,
    returns Callable[[float], float]: A function
    """
    def f(n: float) -> float:
        """ Multiplies a number by the given multiplier """
        return float(n * multiplier)

    return f
