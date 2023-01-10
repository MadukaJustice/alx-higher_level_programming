#!/usr/bin/python3
"""
    Initialize Module to print Pascal's tringle
"""


def pascal_triangle(n):
    """
        Defines function to print pascals triangle
        using recursion
    """
    if n <= 0:
        return []

    if n == 1:
        return [[1]]

    else:
        result = pascal_triangle(n-1)

        curr_row = [1]
        prev_row = result[-1]

        for i in range(len(prev_row)-1):
            curr_row.append(prev_row[i] + prev_row[i+1])

        curr_row += [1]
        result.append(curr_row)

        return result
