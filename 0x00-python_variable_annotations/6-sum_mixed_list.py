#!/usr/bin/env python3
""" Describes a type-annotated function sum_mixed_list """


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ return the sum as float """
    sum: float = 0
    for el in mxd_lst:
        sum += el
    return sum
