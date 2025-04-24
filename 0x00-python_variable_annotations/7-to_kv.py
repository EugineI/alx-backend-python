#!/usr/bin/env python3
"""takes a float and string as argument and returns a tuple"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns string and square of float/int as tuple"""
    return (k, float(v ** 2))
