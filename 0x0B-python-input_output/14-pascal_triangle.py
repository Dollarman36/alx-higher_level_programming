#!/usr/bin/python3

""" pascal_triangle module """


def pascal_triangle(n):
    """
    pascal_triangle function

    returns a list of lists of integers representing the
    Pascals triangle of n
    """

    if n <= 0:
        return []

    pascal = [[1]]
    for i in range(n - 1):
        row = pascal[-1]
        n_row = []
        if type(row) is int:
            row = [row, row]
            pascal.append(row)
            continue
        for idx, j in enumerate(row):
            if idx == 0:
                n_row.append(row[idx])
                continue
            n_row.insert(idx, row[idx] + row[idx - 1])
        n_row.append(row[idx])
        pascal.append(n_row)

    return pascal
