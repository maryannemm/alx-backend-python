#!/usr/bin/env python3
from typing import List, Any, Tuple

def zoom_array(lst: List[Any], factor: int = 2) -> List[Any]:
    """
    Zooms in on an array by a given factor.

    Parameters:
    ----------
    lst : List[Any]
        The list to be zoomed in on.
    
    factor : int
        The factor by which to zoom in (default is 2).

    Returns:
    -------
    List[Any]
        A new list that contains the elements of `lst` repeated `factor` times.
    """
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)  # Changed to an integer

