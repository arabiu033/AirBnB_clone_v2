#!/usr/bin/python3
""" Concole Module """
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    contains the entry point of the command interpreter
    """
    prompt = "(hbnb) "

    def do_create(self, line):
        """
         Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        if line == "BaseModel":
            obj_instance = BaseModel()
            onj_instance.save()
        elif len(line) == 0:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        Prints the string representation of an instance based
        on the class name and id. Ex: $ show BaseModel 1234-1234-1234
        """
        if len(line) == 0:
            print("** class name missing **")
            return

        key = line.split(" ", maxsplit=1)
        if len(key) < 2:
            print("** instance id missing **")
        elif key[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            all_obj = strorage.all()
            try:
                obj = all_obj[".".join(key)]
                print(obj)
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234
        """
        if len(line) == 0:
            print("** class name missing **")
            return

        key = line.split(" ", maxsplit=1)
        if len(key) < 2:
            print("** instance id missing **")
        elif key[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            all_obj = strorage.all()
            try:
                del all_obj[".".join(key)]
                storage.save()
            except KeyError:
                print("** no instance found **")

    def do_quit(self, line):
        """
        exit the program
        """
        key = line.split(" ", maxsplit=1)
        print(".".join(key))
        return True

    def do_EOF(self, line):
        """
        exit the program
        """
        return True

    def help_quit(self):
        """
        Formated help output
        """
        print("Quit command to exit the program\n")

    def emptyline(self):
        """
        Do Nothing
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
