#!/usr/bin/env python3
""" This module contains a function"""
from typing import Mapping, MutableMapping, Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Computes the length of elements """
    return [(i, len(i)) for i in lst]
