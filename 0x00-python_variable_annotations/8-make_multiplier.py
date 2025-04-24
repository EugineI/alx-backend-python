#!/usr/bin/env python3
"""
function that takes a float multiplier
returns function to multiply float by multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """takes a float multiplier and return a function"""
    def multiply(n: float) -> float:
        """multiplies float by multiplier"""
        return n * multiplier
    return multiply
