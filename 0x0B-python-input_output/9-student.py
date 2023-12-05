#!/usr/bin/python3
"""module implement class student has a method to seralize itself"""
class student:
    """class represent a student"""
    def __init__(self, first_name, last_name, age):
        """student constructor to make instances"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self):
        """returns json dict of attributes in read only view"""
        return self.__dict__
