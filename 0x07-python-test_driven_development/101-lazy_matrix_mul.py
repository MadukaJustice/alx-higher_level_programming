#!/usr/bin/python3
"""
    Define lazy_matrix_mul function
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
        Computes and returns the product of two matrices
    """
    return numpy.matmul(m_a, m_b)
