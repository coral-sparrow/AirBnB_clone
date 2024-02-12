'''
    implementing the console class 
'''


import cmd

class HBNBCommand(cmd.Cmd):
    """  Simple command processor.  """

    prompt = '(hbnb) '
     
    def do_EOF(self, line):
        return True
    
    def do_quit(self, line):
        return True

    def help_EOF(self):
        print("exit the cmd loop")
    
    def help_quit(self):
        print("exit the cmd loop")

if __name__ == '__main__':
    HBNBCommand().cmdloop()