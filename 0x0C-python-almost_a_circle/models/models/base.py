#!/usr/bin/python3
"""moddule represents Base class"""
class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """method initialize class variables with id or its order in creation"""
        Base.__nb_objects += 1
        self.id = id if id else Base.__nb_objects
        

