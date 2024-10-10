#!/usr/bin/env python3
"""
key and float vlaue even if it is integer
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Tuples"""
    return (k, float(v ** 2))
