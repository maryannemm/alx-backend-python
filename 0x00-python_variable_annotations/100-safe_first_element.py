#!/usr/bin/env python3
from typing import Sequence, Any, Union

"""
A module that contains a function to safely retrieve the first element of a sequence.
"""

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a sequence or None if the sequence is empty.

    Parameters:
    ----------
    lst : Sequence[Any]
        A sequence (e.g., list, tuple) from which to retrieve the first element.

    Returns:
    -------
    Union[Any, None]
        The first element of the sequence or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None

