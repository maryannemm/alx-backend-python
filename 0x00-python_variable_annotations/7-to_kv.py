#!/usr/bin/env python3
from typing import Union, Tuple

"""
A module that contains a function to return a tuple with a string and the square of a number (int or float).
"""

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with a string and the square of an int or float.

    Parameters:
    ----------
    k : str
        A string representing the key.
    v : Union[int, float]
        An integer or float whose square is to be calculated.

    Returns:
    -------
    Tuple[str, float]
        A tuple where the first element is the string k, and the second element is the square of v as a float.
    """
    return (k, float(v ** 2))

