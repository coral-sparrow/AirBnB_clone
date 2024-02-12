#!/usr/bin/python3
'''
    implementing the console class
'''


import cmd


class HBNBCommand(cmd.Cmd):
    """  Simple command processor.  """

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
