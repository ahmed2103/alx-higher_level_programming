#!/usr/bin/python3

"""rectangle class"""


class Rectangle:
    """This class represents a rectangle object"""

    def __init__(self, width=0, height=0):
        """initializes a rectangle object"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets width"""
        return self._width

    @property
    def height(self):
        """Gets height"""
        return self._height

    @height.setter
    def height(self, value):
        """Sets height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self._height = value

    @width.setter
    def width(self, value):
        """Sets width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self._width = value

    def area(self):
        """returns area of the object"""
        return self.width * self.height

    def perimeter(self):
        """returns area of the rectangle"""
        if self.height and self.width:
            return 2 * (self.width + self.height)
        return 0

    def __str__(self):
        """informal string representation of the rectangle"""
        if self.perimeter():
            return '\n'.join('#' * self.width for _ in range(self.height))
        else:
            return ''

    def __repr__(self):
        """formal representation of othe rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)
