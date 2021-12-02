from sys import argv
from cli import welcome, commands, help_types
from helpers import output
from commands import awsqlhelp, runcli

if __name__ == "__main__":

    # first arg is main.py
    args = argv[1:]

    # empty args
    if len(args) == 0:
        welcome()
        runcli()
    else:
        try:
            if len(args) == 1:
                if args[0] == commands[0]:
                    welcome()
                else:
                    raise Exception
            elif len(args) == 2:
                if args[0] == commands[0] and args[1] in help_types:
                    welcome()
                    awsqlhelp(args[1])
                else:
                    raise Exception
            else:
                output("e", "Too many arguments: " + " ".join(args))
                welcome()
        except:
            output("e", "Unrecognised arguments: " + " ".join(args))
            welcome()
