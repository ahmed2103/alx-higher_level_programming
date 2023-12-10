#!/usr/bin/python3
"""
module that implements square inherited from Rectangle +
dimensional and diagonal equality
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class that represents a square inherited from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """square initializer
        :param size: size of the square
        :type size: int
        :param x: x position of the square
        :type x: int
        :param y: y position of the square
        :type y: int
        :param id: id of the square
        :type id: int
        :raise
        TypeError: if size, x, or y are not integers
        ValueError: if size, x, or y are not positive integers
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """property that represents the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """property that sets the size of the square
        :param value: size of the square
        :type value: int
        :raises TypeError: if size is not int
        :raises ValueError: if size not positive """
        self.width = value
        self.height = value

    def __str__(self):
        """method that returns a string representation of the square"""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """method that update the attributes of the square from
        the given arguments"""
        attrs = ("id", "size", "x", "y")
        for attr, arg in zip(attrs, args):
            setattr(self, attr, arg)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """method to return a dictionary representation of the square"""
        return {'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y}
