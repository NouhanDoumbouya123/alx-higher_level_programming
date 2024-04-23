#!/usr/bin/python3
"""This module contains the base class that
will be the base of all other classes
in order to manage id attribute"""
import json
import csv


class Base:
    """This is actually the base class of all classes
    Private class attribue:
    __nb_objects = 0
    Class constructor:
    def __init__(self, id=None)
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """This the class constructor
        Args:
        id: which is the id
        """

        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1

            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """A static method that returns the JSON
        representation of a list of list_dictionaries"""

        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saving to a file"""

        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            json_string = cls.to_json_string(
                    [obj.to_dictionary() for obj in list_objs]
            )
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """A static method that returns the list of
        dictionaries represented by json_string"""

        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """A class method that returns an instance
        with all attributes already set"""

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1, 0, 0)  # Create a dummy Rectangle instance
        elif cls.__name__ == "Square":
            dummy = cls(1, 1, 0, 0)     # Create a dummy Square instance

        dummy.update(**dictionary)  # Apply real values using update method
        return dummy

    @classmethod
    def load_from_file(cls):
        """A class method that returns a list of instances"""

        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()  # Read the JSON string from file
        except FileNotFoundError:
            return []  # Return an empty list if the file doesn't exist

        # Convert the JSON string to a list of dictionaries
        list_dicts = cls.from_json_string(json_string)
        # Create instances from the dictionaries using the create method
        instances = [cls.create(**dict_) for dict_ in list_dicts]
        return instances
