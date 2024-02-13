#!/usr/bin/python3
'''
    implementing the console class
'''

from models import *

import cmd

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

    def do_EOF(self):
        '''exit the cmd loop'''
        return True

    def do_quit(self, arg):
        '''Quit command to exit the program'''
        return True

    def help_EOF(self):
        '''help the EOF command'''
        print("")
        print("exit the cmd loop")

    def help_quit(self):
        '''help the quit command'''
        print('Quit command to exit the program\n')

    def emptyline(self):
        '''override the emptyline behaviour'''
        pass

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
        print('Creates a new instance of BaseModel,'
              ' saves it (to the JSON file) and prints the id')

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
        print('Prints the string representation',
              ' of an instance based on the class name and id')

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
        print('Deletes an instance based on the class name and id')

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
        print('Prints all string representation',
              ' of all instances based or not on the class name')

    def do_update(self, args):
        '''update  instances based on the
        class name and id'''
        args_list = args.split()

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
        print('update  instances based on',
              ' the class name and id')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
