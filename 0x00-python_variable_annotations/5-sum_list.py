#!/usr/bin/env python3
""" Describes a type-annotated function sum_list """


from typing import List


def sum_list(input_list: List[float]) -> float:
    """ returns the sum of the list """
    sum = 0
    for el in input_list:
        sum += el
    return sum
