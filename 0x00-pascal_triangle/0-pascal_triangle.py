#!/usr/bin/python3
"""This funcion
    return list of lists representing pascal triangle
"""


def pascal_triangle(n):
    """
    return pascal triangle
    """
    list = []
    if (n <= 0):
        return list
    list.append([1])
    for i in range(n - 1):
        list.append([1] + [list[i][j] + list[i][j + 1]
                    for j in range(len(list[i]) - 1)] + [1])
    return list