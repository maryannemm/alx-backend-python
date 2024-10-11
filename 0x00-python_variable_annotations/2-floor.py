#!/usr/bin/env python3
"""
A module that contains a function to return the floor of a float with type annotations.
"""

import math

def floor(n: float) -> int:
    """
    Returns the floor of a float.

    Parameters:
    ----------
    n : float
        The float number whose floor value is to be returned.

    Returns:
    -------
    int
        The floor value of the given float.
    """
    return math.floor(n)

