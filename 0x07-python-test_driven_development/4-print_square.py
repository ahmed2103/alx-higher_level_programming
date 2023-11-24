#!/usr/bin/python3
'''Defines a function to print a square made of '#' characters'''

def print_square(size):
    """
    Prints a square of '#' characters of a specified size.

    Args:
    - size (int): The size of the square to be printed.
    
    Raises:
    - TypeError: If size is not an integer.
    - ValueError: If size is less than zero.
    """
    if size is 0:
        return
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    print('\n'.join('#' * size for x in range(size)))
