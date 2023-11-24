#!/usr/bin/python3
"""
This module defines a function to divide elements in a matrix.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements in a matrix by a specified divisor.
    
    Args:
    - matrix (list of lists): Represents the matrix to be divided.
    - div (int/float): The divisor used for division.
    
    Returns:
    - list of lists: Resultant matrix after division.
    
    Raises:
    - TypeError: If the matrix is not a list of lists containing only integers or floats,
      or if the rows of the matrix are of different sizes.
    - ZeroDivisionError: If the divisor is zero.
    """
    if (not isinstance(matrix, list) or not len(matrix) or
            0 in [len(listx) if type(listx) is list else 0 for listx in matrix] or
            any(False in x for x in [[isinstance(ele, (int, float)) for ele in row] for row in matrix])):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    if len(set([len(listx) for listx in matrix])) > 1:
        raise TypeError('Each row of the matrix must have the same size')

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    return [[round(ele / div, 2) for ele in row] for row in matrix]
