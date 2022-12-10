#!/usr/bin/python3


def best_score(a_dictionary):

    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    best_s = next(iter(a_dictionary.values()))
    best_k = next(iter(a_dictionary.keys()))
    for k in a_dictionary:
        if a_dictionary[k] > best_s:
            best_k = k
            best_s = a_dictionary[k]
            return best_k
