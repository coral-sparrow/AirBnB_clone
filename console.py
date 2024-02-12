'''
    implementing the console class
'''


import cmd


class HBNBCommand(cmd.Cmd):
    """  Simple command processor.  """

    prompt = '(hbnb) '

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    def do_EOF(self, line):
        '''exit the cmd loop'''
        return True

    def help_EOF(self):
        '''help the EOF command'''
        print("exit the cmd loop")

    def help_quit(self):
        '''help the quit command'''
        print('Quit command to exit the program')

    def emptyline(self):
        '''override the emptyline behaviour'''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
