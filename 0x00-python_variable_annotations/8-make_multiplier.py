#!/usr/bin/env python3
""" Describes a type-annotated function make_multiplier """


from typing import Callable


multiply = Callable[[float], float]


def make_multiplier(multiplier: float) -> multiply:
    """ returns a function that multiply a float by multiplier"""
    def multiply(x: float) -> float:
        """ return mulitiplication result """
        return x * multiplier
    return multiply
