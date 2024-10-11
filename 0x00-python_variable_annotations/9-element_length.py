#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple

"""
A module that contains a function to compute the lengths of elements in an iterable.
"""

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, each containing an element from the iterable and its length.

    Parameters:
    ----------
    lst : Iterable[Sequence]
        An iterable containing sequences (e.g., strings, lists).

    Returns:
    -------
    List[Tuple[Sequence, int]]
        A list of tuples where each tuple contains an element from lst and its length.
    """
    return [(i, len(i)) for i in lst]

