#!/usr/bin/env python3
"""
type-anno take ints and floats -> float sum
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Mixed into float sum"""
    return sum(mxd_list)
