#!/usr/bin/python3
"""Defines pascal-triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of ints representing.
    """
    if n <= 0:
        return []

    triang = [[1]]
    while len(triang) != n:
        one = triang[-1]
        two = [1]
        for ind in range(len(one) - 1):
            two.append(one[ind] + one[ind + 1])
        two.append(1)
        triang.append(two)
    return triang

