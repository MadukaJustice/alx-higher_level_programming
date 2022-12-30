#!/usr/bin/python3
"""
    Define matrix_mul which returns the product of two matrices
"""


def matrix_mul(m_a, m_b):
    """
        Returns result of m_a * m_b
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if len(m_a) == 0 or len(m_b) == 0 or m_a == [[]] or m_b == [[]]:
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for n in row:
            if not isinstance(n, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must should be of the same size")
        if len(row) != len(m_b):
            raise ValueError("m_a and m_b can't be multiplied")

    for row in m_b:
        for n in row:
            if not isinstance(n, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must should be of the same size")

    res = []
    new_matrix = []
    n = 0
    for row_A in range(len(m_a)):
        res = []
        for col_B in range(len(m_b[0])):
            for i in range(len(m_a[0])):
                n += m_a[row_A][i] * m_b[i][col_B]
            res.append(n)
            n = 0
        new_matrix.append(res)

    return new_matrix
