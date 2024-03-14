#!/usr/bin/python3
'''
module cmd - console.py that contains the entry point of the command interpreter
'''
import cmd
import cmd
import json
import re
import models
# from models import storage
from models.base_model import BaseModel
from models.user import User

class HBNBCommand(cmd.Cmd):
	'''
	class definition 
	'''
	prompt = "(hbnb)"

    def my_errors(self, line, num_of_args):
        """Displays error messages to user

        Args:
            line(any): gets user input using command line
            num_of_args(int): number of input arguments

        Description:
            Displays output to the use based on
            the input commands.

        """
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]

        msg = ["** class name missing **",
               "** class doesn't exist **",
               "** instance id missing **",
               "** no instance found **",
               "** attribute name missing **",
               "** value missing **"]
        if not line:
            print(msg[0])
            return 1
        args = line.split()
        if num_of_args >= 1 and args[0] not in classes:
            print(msg[1])
            return 1
        elif num_of_args == 1:
            return 0
        if num_of_args >= 2 and len(args) < 2:
            print(msg[2])
            return 1
        d = storage.all()

        for i in range(len(args)):
            if args[i][0] == '"':
                args[i] = args[i].replace('"', "")
        key = args[0] + '.' + args[1]
        if num_of_args >= 2 and key not in d:
            print(msg[3])
            return 1
        elif num_of_args == 2:
            return 0
        if num_of_args >= 4 and len(args) < 3:
            print(msg[4])
            return 1
        if num_of_args >= 4 and len(args) < 4:
            print(msg[5])
            return 1
        return 0

	def do_quit(self, args):
		'''
		exit the program
		'''
		return True

	def help_quit(self, args):
		'''
		this action is provided by default by cmd but should be kept updated and documented
		'''
		print("Quit the program")

	def do_EOF(self, args):
		'''
		EOF (Ctrl+D) signal to exit the program
		'''
		print()
		return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
