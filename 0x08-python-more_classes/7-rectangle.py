#!/usr/bin/python3

"""rectangle class"""


class Rectangle:
    """This class represents a rectangle object"""
    print_symbol = '#'
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initializes a rectangle object"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            return '\n'.join("{}".format(self.print_symbol) * self.width
                             for _ in range(self.height))
        else:
            return ''

    def __repr__(self):
        """formal representation of the rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """ rectangle deletion"""
        Rectangle.number_of_instances -= 1
        print("{}".format("Bye rectangle..."))
