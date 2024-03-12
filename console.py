#!/usr/bin/python3
'''
module cmd - console.py that contains the entry point of the command interpreter
'''
import cmd


class HBNBCommand(cmd.Cmd):
	'''
	class definition 
	'''
	prompt = "(hbnb)"

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
