#!/usr/bin/python3
'''
    implementing the console class
'''


import cmd
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.review import Review
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.user import User


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

    # def emptyline(self
    #     '''override the emptyline behaviour'''
    #     pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
    # def hasan():
    #     """asas"""
    
    # print(hasan.__doc__)
