#!/usr/bin/python3

"""Module representing the Base class"""

from json import dumps, load


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize class variables"""
        Base.__nb_objects += 1
        self.id = id if id is not None else Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        :param list_dictionaries: list of dictionaries
        :return: JSON
        """
        return dumps(list_dictionaries) if list_dictionaries else "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """saves above json to file
        :param cls: class as it is class method
        :param list_objs: list of dictionaries
        :returns: none
        """
        if not list_objs:
            list_objs = []
        with open("{:s}.json".format(cls.__name__), "w") as file:
            file.write(cls.to_json_string([obj.to_dictionary() for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """
        deseralizes json
        :param json_string: json string to deseralize
        :returns: objects in dictionary
        """
        return load(json_string) if json_string else []

    @classmethod
    def create(cls, **dictionary):
        """
        Create a Rectangle or Square instance with “dummy” mandatory attributes.
        :param cls: class to create instance
        :param dictionary: that have necessary attributes.
        :return:instance with dummy attributes.
        """
        if cls.__name__ == "Rectangle":
            c = cls(1, 1)
        elif cls.__name__ == "Square":
            c = cls(1)
        else:
            c = cls()
        c.update(**dictionary)
        return c

    @classmethod
    def load_from_file(cls):
        """
        class method that loads seralized json and deseraize it then crate the object
        :param cls: class of the object.
        :return: the object created by create function
        :raise: FileNotFoundError if the file does not exist
        """
        try:
            with open("{}.json".format(cls.__name__), "r") as file:
                list_dicts = cls.from_json_string(file.read())
                return [cls.create(**kwag) for kwag in list_dicts]
        except FileNotFoundError:
            return []
    @classmethod
    def load_from_file_csv(cls):
        """Class method to load file containing csv representation of objects.
        Attempts to open file named '<class name>.csv' and convert back to
        original list of objects. If it does not exist, returns empty list.
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
