#!/usr/bin/python3
"""Module implementing function to verify class membership"""


def is_kind_of_class(obj, a_class):
    """Checks if obj is an instance of or inherits from a_class"""
    return isinstance(obj, a_class)
