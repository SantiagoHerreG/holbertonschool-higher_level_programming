#!/usr/bin/python3
"""This class will be the base of all other classes in this project.
"""
import json


class Base:
    """Base class with object id.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor of the class, id is optional
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        if type(list_dictionaries) is not list:
            raise TypeError("to_json_string takes a list of dictionaries")
        for elems in list_dictionaries:
            if type(elems) is not dict:
                raise TypeError("to_json_string takes a list of dictionaries")

        if len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation
        """
        if json_string is None or json_string == "":
            return []
        if type(json_string) is not str:
            raise TypeError("json_string must be a string")

        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file
        """
        if list_objs is None:
            list_objs = []

        if type(list_objs) is not list:
            raise TypeError("save_to_file takes a list of instances of Base")

        for elems in list_objs:
            if isinstance(elems, Base) is not True:
                raise TypeError("save_to_file takes a list of instances o\
f Base")
        new_list = []
        for objs in list_objs:
            new_list.append(objs.to_dictionary())

        json_str = Base.to_json_string(new_list)

        with open(cls.__name__ + ".json", encoding="UTF-8", mode="w") as f:
            f.write(json_str)
