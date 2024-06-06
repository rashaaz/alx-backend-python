#!/usr/bin/env python3
""" This module contains a function """
from typing import Any, Union, Sequence, Iterable, List, Tuple


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Safely returns the first element of a sequence """
    if lst:
        return lst[0]
    else:
        return None
