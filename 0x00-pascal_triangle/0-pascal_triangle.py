#!/usr/bin/python3
"""
This program defines a function to generate Pascal's
triangle up to the nth row,
and then prints the triangle using another function.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for _ in range(1, n):
        prev_row = triangle[-1]
        new_row = [1] + [prev_row[i] + prev_row[i + 1] for i\
                         in range(len(prev_row) - 1)] + [1]
        triangle.append(new_row)

    return triangle
