#!/usr/bin/python3

import os
import json

class Base:
    """Base model which will serve as the model for other classes
    Attributes:
        __nb_objects(int): The counter for the number of objects that would be created"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization for the Base class
        Args:
            id(int): Id of each of the objects that would be created"""

        self.id = id

        if self.id == None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries == None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                obj_list = []
                for obj in list_objs:
                    obj_list.append(obj.to_dictionary())
                jsonfile.write(cls.to_json_string(obj_list))


    @staticmethod
    def from_json_string(json_string):
        if json_string == None:
            return []
        else:
            return json.loads(json_string)


    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1, 0, 0, None)
        elif cls.__name__ == 'Square':
            dummy = cls(1, 0, 0, None)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        file_name = cls.__name__ + ".json"
        list_of_instances = []
        list_dictionaries = []

        if os.path.exists(file_name):
            with open(file_name, 'r') as my_file:
                my_str = my_file.read()
                list_dictionaries = cls.from_json_string(my_str)
                for dictionary in list_dictionaries:
                    list_of_instances.append(cls.create(**dictionary))
        return list_of_instances



