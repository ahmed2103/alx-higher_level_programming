#!/usr/bin/python3

import math

class MagicClass:
    """Replicates bytecode for ALX"""
    def __init__(self, radius=0):
        """Instantiate a MagicClass object to represent a circle"""
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')
        self.__radius = float(radius)

    def area(self):
        """Compute the area of a circle"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Compute the circumference of a circle"""
        return 2 * math.pi * self.__radius
