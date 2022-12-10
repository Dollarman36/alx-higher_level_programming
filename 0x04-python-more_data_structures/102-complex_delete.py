#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    if a_dictionary is None or len(a_dictionary) == 0:
        return a_dictionary
    keys = []
    for k in a_dictionary:
        if a_dictionary[k] == value:
            keys.append(k)
            for k in keys:
                del a_dictionary[k]
                return a_dictionary
