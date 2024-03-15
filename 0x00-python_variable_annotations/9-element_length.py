#!/usr/bin/env python3
"""
This module provides a function for finding the length of each
    element in a list of strings and types it
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    This function takes a list of strings and returns a list of input tuples,
        where each tuple contains a string

    Parameters:
    lst (List[str]): The list of strings to parse

    Returns:
    List[Tuple[str, int]]: A list of input tuples, where each tuple contains
        a string and the length of that string.
    """
    return [(i, len(i)) for i in lst]
