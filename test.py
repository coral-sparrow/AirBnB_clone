#!/usr/bin/python3

import cmd

class HelloWorld(cmd.Cmd):
    """  Simple command processor.  """

    def default(self, line: str) -> None:
        args = line.split('.')
        args[-1] = args[-1].replace('(', '')
        args[-1] = args[-1].replace(')', '')
        args.reverse()
        if hasattr(self, f'do_{args[0]}'):
            getattr(self, f'do_{args[0]}')(' '.join(args[1:]))

    
    def do_greet(self, line):
        print(f'hello {line}')
    
    def do_EOF(self, line):
        return True
    
    def do_quit(self, line):
        return True

    def help_EOF(self):
        print("exiting the cmd loop")

if __name__ == '__main__':
    HelloWorld().cmdloop()
