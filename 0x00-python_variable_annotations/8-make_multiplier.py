#!/usr/bin/env python3
"""
This module provides a function that creates a function that in turn
    multiplies a float by a factor.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This function takes a float as an argument and returns a function that
        multiplies a float by the factor.

    Parameters:
    factor (float): The factor to use in the returned function.

    Returns:
    Callable[[float], float]: A function that multiplies a float by the
        factor.
    """
    def multiply(n: float) -> float:
        """
        This function multiplies a float by the factor.

        Parameters:
        n (float): The float to multiply by the factor.

        Returns:
        float: The result of multiplying n by the factor.
        """
        return n * multiplier
    return multiply
