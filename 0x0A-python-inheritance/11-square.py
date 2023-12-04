#!/usr/bin/python3
"""Module implementing the Square class"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Class representing a Square as a subclass of Rectangle"""
    def __init__(self, size):
        """Initialize a new Square object
        
        Args:
            size (int): Length of the square's side
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Compute the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Return string representation of the square"""
        return "[{}] {:d}/{:d}".format(self.__class__.__name__,
                                       self.__size, self.__size)
