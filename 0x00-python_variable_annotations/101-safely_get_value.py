#!/usr/bin/env python3
from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')  # Declare a generic type variable

"""
A module that contains a function to safely get a value from a dictionary.
"""

def safely_get_value(dct: Mapping[Any, T], key: Any, default: Union[T, None] = None) -> Union[T, Any]:
    """
    Safely retrieves a value from a dictionary.

    Parameters:
    ----------
    dct : Mapping[Any, T]
        The dictionary from which to retrieve the value.
    
    key : Any
        The key for which to retrieve the value.
    
    default : Union[T, None]
        The default value to return if the key does not exist in the dictionary (default is None).

    Returns:
    -------
    Union[T, Any]
        The value associated with the key if it exists, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default

