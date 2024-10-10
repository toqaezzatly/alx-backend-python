#!/usr/bin/env python3
"""
type-annotated fn takes floats -> float sum
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """list of float to float sum"""
    return sum(input_list)
