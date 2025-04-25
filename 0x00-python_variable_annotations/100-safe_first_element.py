#!/usr/bin/env python3
"""duck-type"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return first element or none"""
    if lst:
        return lst[0]
    else:
        return None
