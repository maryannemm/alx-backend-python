#!/usr/bin/env python3
from typing import List, Union

"""
A module that contains a function to sum a list of integers and floats with type annotations.
"""

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list containing both integers and floats.

    Parameters:
    ----------
    mxd_lst : List[Union[int, float]]
        A list of integers and floats to be summed.

    Returns:
    -------
    float
        The sum of the list of integers and floats.
    """
    return sum(mxd_lst)

