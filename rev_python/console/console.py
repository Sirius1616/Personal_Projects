#!/usr/bin/python3
"""The entry point for the programme which would be run in the console"""
import cmd
import sys
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """The command line class that inherits from the cmd module"""

    classes = ["BaseModel", "User", "State", "City", "Amenity",
                 "Place", "Review"]

    prompt = "(hbnb)"
    def do_quit(self, arg):
        """This overides the command that quites the programme"""
        return True

    def do_EOF(self, arg):
        """Returns True when and empty line + Enter is executed"""
        return True

    def emptyline(self):
        """Overrides the emptyline method by doing nothing"""

        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it to JSON, and print its id"""
        arg_list = arg.split()
        if len(arg_list) == 0:
            print("** class name missing **")
        else:
            class_name = arg_list[0]
            if class_name not in self.classes:
                print("** class doesn't exist **")
            else:
                new_instance = globals()[class_name]()
                new_instance.save()
                print(new_instance.id)

    def do_show(self, arg):
        """Displays the details of a particular attribute"""
        arg_list = arg.split()
        if len(arg_list) == 0:
            print("** class name missing **")
        else:
            class_name = arg_list[0]
            if class_name not in self.classes:
                print("** class doesn't exist **")
            elif len(arg_list) == 1:
                    print('** instance id missing **')
            else:
                key = "{}.{}".format(arg_list[0], arg_list[1])
                if key not in storage.all():
                    print('** no instance found **')
                else:
                    print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234
        """
        arg_list = arg.split()
        if len(arg_list) == 0:
            print("** class name missing **")
        else:
            class_name = arg_list[0]
            if class_name not in self.classes:
                print("** class doesn't exist **")
            elif len(arg_list) == 1:
                    print('** instance id missing **')
            else:
                key = "{}.{}".format(arg_list[0], arg_list[1])
                if key not in storage.all():
                    print('** no instance found **')
                else:
                    ob_store = storage.all()
                    del ob_store[key]
                    storage.save

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name. 
        Ex: $ all BaseModel or $ all
        """
        arg_list = arg.split()
        list_all = []
        dict_all = {}
        if arg:
            class_name = arg_list[0]
            if class_name not in self.classes:
                print("** class doesn't exist **")
            else:
                for key, value in storage.all().items():
                    new_key = key.split(".")[0]
                    dict_all[new_key] = str(value)
                for key, value in dict_all.items():
                    list_all.append(value)
                print(list_all)

        else:
            for key, value in storage.all().items():
                list_all.append(str(value))
            print(list_all)

    def update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute. 
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        



if __name__ == "__main__":
    HBNBCommand().cmdloop()
