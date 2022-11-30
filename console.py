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
            obj_instance.save()
            print(obj_instance.id)
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
            all_obj = storage.all()
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
            all_obj = storage.all()
            try:
                del all_obj[".".join(key)]
                storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name. Ex: $ all BaseModel or $ all
        """
        if len(line) != 0 and  line != "BaseModel":
            print("** class doesn't exist **")
        else:
            lis = []
            all_objs = storage.all()
            for key in all_objs.keys():
                lis.append(all_objs[key].__str__())
            print(lis)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        if len(line) == 0:
            print("** class name missing **")
            return
        key = line.split(" ")
        if key[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(key) == 1:
            print("** instance id missing **")
        else:
            all_obj = storage.all()
            try:
                obj = all_obj[".".join([key[0], key[1]])]
                if len(key) == 2:
                    print("** attribute name missing **")
                elif len(key) == 3:
                    print("** value missing **")
                else:
                    if key[3][:1] == '"':
                        value = key[3][1:-1]
                    else:
                        value = key[3]
                    obj.__dict__[key[2]] = value
                    storage.new(obj)
                    obj.save()
            except KeyError:
                print("** no instance found **")

    def do_quit(self, line):
        """
        exit the program
        """
        return True

    def do_EOF(self, line):
        """
        exit the program
        """
        print()
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
