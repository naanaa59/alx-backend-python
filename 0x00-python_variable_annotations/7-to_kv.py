#!/usr/bin/env python3
""" Describes a type-annotated function to_kv """


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ returns a tuple with k and square of v as float """
    return (k, v ** 2)
