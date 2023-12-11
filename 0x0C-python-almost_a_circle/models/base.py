#!/usr/bin/python3

from json import dumps, load, loads
import csv

class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize class variables"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.
        :param list_dictionaries: List of dictionaries.
        :return: JSON string.
        """
        return dumps(list_dictionaries) if list_dictionaries else "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves the list of objects to a JSON file.
        :param cls: Class (as it is a class method).
        :param list_objs: List of objects.
        :returns: None.
        """
        if not list_objs:
            list_objs = []
        with open("{:s}.json".format(cls.__name__), "w") as file:
            file.write(cls.to_json_string([obj.to_dictionary() for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """
        Deserializes a JSON string into a list of objects.
        :param json_string: JSON string to deserialize.
        :returns: List of objects.
        """
        return loads(json_string) if json_string else "[]"

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance of the class with attributes from a dictionary.
        :param cls: Class to create an instance of.
        :param dictionary: Dictionary with necessary attributes.
        :return: Instance with specified attributes.
        """
        if cls.__name__ == "Rectangle":
            c = cls(dictionary.get('width', 1), dictionary.get('height', 1))
        elif cls.__name__ == "Square":
            c = cls(dictionary.get('size', 1))
        else:
            c = cls()
        c.update(**dictionary)
        return c

    @classmethod
    def load_from_file(cls):
        """
        Loads serialized JSON from a file and creates objects.
        :param cls: Class of the object.
        :return: List of objects created by create function.
        :raise: FileNotFoundError if the file does not exist.
        """
        try:
            with open("{}.json".format(cls.__name__), "r") as file:
                list_dicts = cls.from_json_string(file.read())
                return [cls.create(**kwarg) for kwarg in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def load_from_file_csv(cls):
        """
        Loads a file containing CSV representation of objects.
        Attempts to open a file named '<class name>.csv' and convert it back to the original list of objects.
        If the file does not exist, returns an empty list.
        """
        try:
            with open("{}.csv".format(cls.__name__), 'r') as csvf:
                if cls.__name__ == "Rectangle":
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == "Square":
                    fieldnames = ['id', 'size', 'x', 'y']
                else:
                    fieldnames = ['id']
                reader = csv.DictReader(csvf, fieldnames=fieldnames)
                list_objs = []
                for row in reader:
                    for key in row:
                        row[key] = int(row[key])
                    list_objs.append(cls.create(**row))
                return list_objs
        except FileNotFoundError:
            return []
