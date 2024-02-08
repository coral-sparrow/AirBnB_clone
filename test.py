import cmd

class HelloWorld(cmd.Cmd):
    """Simple command processor example."""
    
    def do_greet(self, line):
        print("hello")
    
    def do_EOF(self, line):
        return True
    
    def do_quit(self, line):
        return True

    def help_EOF(self):
        print("exiting the cmd loop")

if __name__ == '__main__':
    HelloWorld().cmdloop()
