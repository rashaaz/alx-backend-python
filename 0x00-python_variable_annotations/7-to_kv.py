#!/usr/bin/env python3
""" This module contains a function"""
from typing import Callable, Iterator, Union, Optional, List, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Converts a string and a number to a tuple
    returns Tuple[str, float]: A tuple containing
    """

    return (k, v**2)
