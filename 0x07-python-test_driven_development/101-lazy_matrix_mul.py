#!/usr/bin/python3
"""Module for matrix multiplication using NumPy"""

import numpy

def lazy_matrix_mul(m_a, m_b):
    """
    Performs matrix multiplication using NumPy's matmul function.

    Args:
    - m_a: First matrix
    - m_b: Second matrix

    Returns:
    - The result of matrix multiplication using NumPy's matmul function
    """
    return numpy.matmul(m_a, m_b)
