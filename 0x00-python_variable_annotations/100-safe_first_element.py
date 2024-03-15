#!/usr/bin/env python3
"""
This module provides a function for returning the first element
    of a sequence, or None if the sequence is empty.
"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    This function returns the first element of a sequence, or None if the
        sequence holds no value

    Parameters:
    lst (Sequence): The sequence to process.


    Returns:
    Union[object, None]: The first element of the sequence, or None if the
        sequence holds no value
    """
    if lst:
        return lst[0]
    else:
        return None
