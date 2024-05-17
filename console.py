#!/usr/bin/python3
'''
    implementing the console class
'''

from models import *

import cmd
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.review import Review
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.user import User

classes = {
    'BaseModel': base_model.BaseModel,
    "User": user.User,
    'City': city.City,
    'Amenity': amenity.Amenity,
    'Place': place.Place,
    'Review': review.Review,
    'State': state.State
}


class HBNBCommand(cmd.Cmd):
    """Simple command processor.  """

    prompt = '(hbnb) '
    
    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
    }

    def do_EOF(self, arg):
        '''exit the cmd iteration'''
        return True
    
    def do_help(self, arg):
        """hasasasasasasa"""
        return super().do_help(arg)
    


    def do_quit(self, arg):
        '''Quit command to exit the program'''
        return True

    def do_show(self, arg):
        '''prints the string representation of an instance based on the class name and id'''    
        return True

    def help_EOF(self):
        '''help the EOF command'''
        print("EOF signal to exit the program.")

    def help_quit(self):
        '''help the quit command'''
        print("Quit command to exit the program.")


    # def emptyline(self
    #     '''override the emptyline behaviour'''
    #     pass

    def do_create(self, args):
        '''create new instance of BaseModel'''
        args_list = args.split()
        classes = {
            'BaseModel': base_model.BaseModel,
            "User": user.User,
            'City': city.City,
            'Amenity': amenity.Amenity,
            'Place': place.Place,
            'Review': review.Review,
            'State': state.State
            }

        if len(args_list) > 1:
            print(f"unknown number of args {args}")
            print(f"Usage: create <class-name>")
        elif len(args_list) == 0:
            print('** class name missing **')
        elif args_list[0] not in classes.keys():
            print('** class doesn\'t exist **')
        else:
            instance = classes[args_list[0]]()
            print(instance.id)
            instance.save()

    def help_create(self):
        '''create new instance of BaseModel'''
        print("Usage: create <class>\n        "
              "Create a new class instance and print its id.")

    def do_show(self, args):
        '''show instance of database'''
        args_list = args.split()

        if len(args_list) == 0:
            print("** class name missing **")
        elif args_list[0] not in classes.keys():
            print('** class doesn\'t exist **')
        elif len(args_list) == 1:
            print('** instance id missing **')
        else:
            try:
                print(storage.all()['.'.join(args_list)])
            except KeyError:
                print('** no instance found **')

    def help_show(self):
        '''show instance of database'''
        print("Usage: show <class> <id> or <class>.show(<id>)\n        "
              "Display the string representation of a class instance of"
              " a given id.")

    def do_destroy(self, args):
        '''destroy instance of database'''
        args_list = args.split()

        if len(args_list) == 0:
            print("** class name missing **")
        elif args_list[0] not in classes.keys():
            print('** class doesn\'t exist **')
        elif len(args_list) == 1:
            print('** instance id missing **')
        else:
            try:
                storage._FileStorage__objects.pop('.'.join(args_list))
                storage.save()
            except KeyError:
                print('** no instance found **')

    def help_destroy(self):
        '''destroy instance of database'''
        print("Usage: destroy <class> <id> or <class>.destroy(<id>)\n        "
              "Delete a class instance of a given id.")

    def do_all(self, args):
        '''
            Prints all string representation of
            all instances based or not on the class name
        '''
        if not args:
            for _, obj in storage.all().items():
                print(obj)
        elif args not in classes.keys():
            print('** class doesn\'t exist **')
        else:
            for _, obj in storage.all().items():
                if obj.to_dict()['__class__'] == args:
                    print(obj)

    def help_all(self):
        '''print all string rep.
        of instances in database'''
        print("Usage: all or all <class> or <class>.all()\n        "
              "Display string representations of all"
              " instances of a given class"
              ".\n        If no class is specified, displays all instantiated "
              "objects.")

    def do_update(self, args):
        '''update  instances based on the
        class name and id'''
        args_list = args.split()
        print(args_list)
        if len(args_list) == 0:
            print("** class name missing **")
        elif args_list[0] not in classes.keys():
            print('** class doesn\'t exist **')
        elif len(args_list) == 1:
            print('** instance id missing **')
        elif len(args_list) == 2:
            print('** attribute name missing **')
        elif len(args_list) == 3:
            print('** value missing **')
        else:
            try:
                instance = storage.all()['.'.join(args_list[:2])]
                setattr(instance, args_list[2], args_list[3].replace('"', ''))
                storage.save()
            except KeyError:
                print('** no instance found **')

    def help_update(self):
        '''update instances in database'''
        print("Usage: update <class> <id> <attribute_name> "
              "<attribute_value> or"
              "\n       <class>.update(<id>, "
              "<attribute_name>, <attribute_value"
              ">) or\n       <class>.update(<id>, <dictionary>)\n        "
              "Update a class instance of "
              "a given id by adding or updating\n   "
              "     a given attribute key/value pair or dictionary.")

    def default(self, line: str):
        args = line.split('.')
        command = args.pop()
        tmp = command.split('(')
        args.extend(tmp[1:])
        args[-1] = args[-1].replace(')', '')
        args[-1] = args[-1].replace(',', '')
        command = tmp[0]
        if hasattr(self, f'do_{command}'):
            getattr(self, f'do_{command}')(' '.join(args).strip())

    def do_count(self, args):
        '''count by class name'''
        count = 0
        objs = list(storage.all().keys())
        for i in objs:
            if i.split('.')[0] == args:
                count += 1
        print(count)

    def help_count(self):
        '''count instances of model in database'''
        print("Usage: count <class> or <class>.count() ")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
    # def hasan():
    #     """asas"""
    
    # print(hasan.__doc__)
