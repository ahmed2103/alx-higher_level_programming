#!/usr/bin/python3

class LockedClass:
    """LockedClass demonstrates the use of the __slots__ attribute to restrict
    dynamic attribute creation.

    Attributes:
        __slots__ (list): A list of strings specifying valid attribute names
            allowed for instances of this class, limiting attribute creation
            to only those listed in __slots__.
    """
    __slots__ = ['first_name']

