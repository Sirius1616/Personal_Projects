#!/usr/bin/python3

import json
import os
from models.base_model import BaseModel
from models.user import User

"""The storage engine for the entire programme"""
class FileStorage:
    """The file for storage of objects
    Attributes:
        __file_path(str): the path to the file in the system
        __objects"""
    __file_path = 'file.json'
    __objects = {}


    def all(self):
        """Returns the already loaded objects that have been created"""
        return self.__objects

    def new(self, obj):
        """This methods creates a new object from alredy existing objects which would be loaded into the json file"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj


    def save(self):
        """This save method is what will serialize the dict object into a json file"""
        with open(self.__file_path, 'w', encoding='utf_8') as n_file:
            serial = {}
            for key, value in self.__objects.items():
                serial[key] = value.to_dict()
            json.dump(serial, n_file)


    def reload(self):
        """deserilizes the json file back to object string"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path) as a_file:
                objs = json.load(a_file)
                for value in objs.values():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))

        else:
            self.__objects = {}




