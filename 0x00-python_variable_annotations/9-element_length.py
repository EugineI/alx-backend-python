#!/usr/bin/env python3
"""Function annotation"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """annotates an iterable list"""
    return [(i, len(i)) for i in lst]
