#!/usr/bin/python3
''' Contains a function to check inheritance'''


def inherits_from(obj, a_class):
    ''' Checks if obj is an instance of a class that inherited (directly or indirectly)'''
    return type(obj) != a_class and isinstance(obj, a_class)
