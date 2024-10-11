#!/usr/bin/env python3
from typing import Callable

"""
A module that contains a function to create a multiplier function.
"""

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Parameters:
    ----------
    multiplier : float
        The multiplier to be used in the multiplication function.

    Returns:
    -------
    Callable[[float], float]
        A function that takes a float as input and returns the product of that float and the multiplier.
    """
    def multiply(value: float) -> float:
        """Multiplies a float by the multiplier."""
        return value * multiplier
    
    return multiply

