#!/usr/bin/env python3
from typing import List, Union
"""
type-anno take ints and floats -> float sum
"""


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Mixed into float sum"""
    return sum(mxd_list)
