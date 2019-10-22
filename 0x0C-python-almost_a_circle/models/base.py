#!/usr/bin/python3
"""This class will be the base of all other classes in this project.
"""
import json
import csv


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
            raise TypeError("save_to_file takes a list of instances of cls")

        for elems in list_objs:
            if isinstance(elems, Base) is not True:
                raise TypeError("save_to_file takes a list of instances o\
f cls")
        new_list = []
        for objs in list_objs:
            new_list.append(objs.to_dictionary())

        json_str = Base.to_json_string(new_list)

        with open(cls.__name__ + ".json", encoding="UTF-8", mode="w") as f:
            f.write(json_str)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set
        """
        if (dictionary is None and cls.__name__ != "Base"):
            raise TypeError("create takes a key/value argument")

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
            if len(dictionary):
                dummy.update(**dictionary)
            return dummy
        elif cls.__name__ == "Square":
            dummy = cls(1)
            if len(dictionary):
                dummy.update(**dictionary)
            return dummy
        else:
            try:
                new_id = dictionary['id']
            except:
                new_id = None
            dummy = cls(new_id)
            return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances of the called class
        """
        try:
            with open(cls.__name__ + ".json", encoding="UTF-8") as f:
                read_json = f.read()
        except:
            return []

        list_python_dicts = Base.from_json_string(read_json)

        instances_list = []
        for dicts in list_python_dicts:
            instances_list.append(cls.create(**dicts))

        return instances_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes the instances to CSV format
        """
        if list_objs is None:
            list_objs = []

        if type(list_objs) is not list:
            raise TypeError("save_to_file_cvs takes a list of instances o\
f " + cls.__name__)

        for elems in list_objs:
            if isinstance(elems, Base) is not True:
                raise TypeError("save_to_file_csv takes a list of instances o\
f " + cls.__name__)
        string_to_save = ""
        if cls.__name__ == "Rectangle":
            for elems in list_objs:
                string_to_save += str(elems.id) + ","
                string_to_save += str(elems.width) + ","
                string_to_save += str(elems.height) + ","
                string_to_save += str(elems.x) + ","
                string_to_save += str(elems.y)
                string_to_save += '\n'

            with open("Rectangle.csv", encoding="UTF-8", mode="w") as f:
                f.write(string_to_save)
            return

        if cls.__name__ == "Square":
            for elems in list_objs:
                string_to_save += str(elems.id) + ","
                string_to_save += str(elems.size) + ","
                string_to_save += str(elems.x) + ","
                string_to_save += str(elems.y)
                string_to_save += '\n'

            with open("Square.csv", encoding="UTF-8", mode="w") as f:
                f.write(string_to_save)
            return
        if cls.__name__ == "Base":
            for elems in list_objs:
                string_to_save += str(elems.id)
                string_to_save += '\n'

            with open("Base.csv", encoding="UTF-8", mode="w") as f:
                f.write(string_to_save)
            return

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes the instances from CSV format
        """
        try:
            with open(cls.__name__ + ".csv", encoding="UTF-8") as f:
                read_csv = csv.reader(f, delimiter=",")

                list_python_dicts = []
                if cls.__name__ == "Rectangle":
                    for lines in read_csv:
                        new_dict = {}
                        new_dict['id'] = int(lines[0])
                        new_dict['width'] = int(lines[1])
                        new_dict['height'] = int(lines[2])
                        new_dict['x'] = int(lines[3])
                        new_dict['y'] = int(lines[4])
                        list_python_dicts.append(new_dict.copy())
                if cls.__name__ == "Square":
                    for lines in read_csv:
                        new_dict = {}
                        new_dict['id'] = int(lines[0])
                        new_dict['size'] = int(lines[1])
                        new_dict['x'] = int(lines[2])
                        new_dict['y'] = int(lines[3])
                        list_python_dicts.append(new_dict.copy())

                if cls.__name__ == "Base":
                    for lines in read_csv:
                        new_dict = {}
                        new_dict['id'] = int(lines[0])
                        list_python_dicts.append(new_dict.copy())

                instances_list = []
                for dicts in list_python_dicts:
                    instances_list.append(cls.create(**dicts))

                return instances_list
        except:
            return []
