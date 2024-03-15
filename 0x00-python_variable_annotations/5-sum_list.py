#!/usr/bin/env python3
"""a typed function that takes a list input_list of floats as
    argument and returns their sum as a float."""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    This function adds two numbers and returns the result.

    Parameters:
    a (float): The first param.
    b (float): The second param.

    Returns:
    float: The sum of a and b.
    """
    return sum(input_list)
