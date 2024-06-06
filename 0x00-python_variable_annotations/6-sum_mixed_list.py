#!/usr/bin/env python3

""" This module contains a function """
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """  Sums a list of integers and floats """
    return float(sum(mxd_lst))
