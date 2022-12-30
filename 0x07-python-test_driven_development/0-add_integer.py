#!/usr/bin/python3

"""0-add_integer

This module has a single function named "add_integer" that adds two integers.

Example:

This module can be called from a main caller function like:

     add_integer = __import__('0-add_integer').add_integer

     print(add_integer(1, 2))
"""


def add_integer(a, b=98):
    """adds two integers"""

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
