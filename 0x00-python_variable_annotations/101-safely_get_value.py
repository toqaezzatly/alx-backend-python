#!/usr/bin/env python3
""" more involved type annotations """

from typing import Mapping, Any, Union, TypeVar


# Define the TypeVar 'T' at the top
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None]) -> Union[Any, T]:
    """ return value of key or default """
    if key in dct:
        return dct[key]
    else:
        return default
