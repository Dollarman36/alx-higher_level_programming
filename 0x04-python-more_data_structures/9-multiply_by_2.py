#!/usr/bin/python3


def multiply_by_2(a_dictionary):

    if a_dictionary is None:
        return

    new = dict(a_dictionary)
    for k in new:
        new[k] = new[k] * 2

        return new
