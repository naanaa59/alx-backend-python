#!/usr/bin/env python3
""" This script annotate a function named element_length """

from typing import Tuple, Iterable, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ return elements from a list """
    return [(i, len(i)) for i in lst]
