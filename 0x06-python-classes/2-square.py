#!/usr/bin/python3
"""class Square that represents a square"""

class Square:
    """class Square that represents a square"""
    __size = None

    def __init__(self, size=0):
        """the size of the square"""
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
