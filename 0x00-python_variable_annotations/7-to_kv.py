#!/usr/bin/env python3
"""
This module provides a function for creating a
    tuple or a square of input and types it
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This function creates a
    tuple or a square of input and types it

    Parameters:
    k (str): The string to include in the tuple.
    v (Union[int, float]): The int or float to square.

    Returns:
    Tuple[str, float]: A tuple with the string k and the square of v as a
        float.
    """
    return (k, float(v ** 2))
