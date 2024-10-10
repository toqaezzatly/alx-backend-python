#!/usr/bin/env python3
"""
Type-annotated callable function
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiplier_function(value: float) -> float:
        """value * multiplier"""
        return value * multiplier
    """callable function"""
    return multiplier_function
