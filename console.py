#!/usr/bin/python3
"""
Contains the entry point of the command intepreter
"""

import cmd
import models

class HBNBCommand(cmd.Cmd):
    """HBNB Console"""
    prompt = "(hbnb) "

    def quit(self, arg):
        """Exits console"""
        return True

    def empty_line(self):
        """Method for emptyline input"""
        return False

    def EOF(self, arg):
        """Exits console"""
        return True






    '''while True:
        try:
            user_input = input(prompt)
            if user_input == "quit":
                break
            print("You entered:", user_input)
        except EOFError:
            break
            print("Exiting the program...")'''



if __name__ == '__main__':
    HBNBCommand().cmdloop()