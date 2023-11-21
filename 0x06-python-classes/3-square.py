#!/usr/bin/python3
class Square:
    """class Square that defines a square"""
    __size = None

    def __init__(self, size=0):
        """Initialization with optional size"""
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("Size must be >= 0")
        else:
            raise TypeError("Size must be an integer")

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
