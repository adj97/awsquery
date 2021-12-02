from helpers import *
from cli import *

from json import load

def runcli():
    print("Opening awsql ...")
    print("You must end commands with a semi-colon (;)")
    sc = ";"

    history = []

    # run cli loop
    while True:
        # single command loop
        cmd = input("awsql> ")
        if cmd.replace(";","") in ["exit;","exit"]:
            break
        elif cmd.replace(";","") in ["hist", "h", "history"]:
            for i, v in enumerate(history): print(str(i+1) + " : " + v)
        else:
            if sc in cmd:
                cmd = cmd.split(";")[0]
            else:
                while True:
                    cmd += input("...... ")
                    if sc in cmd: break
            print("Executing \"" + cmd + "\"")
            history.append(cmd)


    print("Closed awsql cli")
    return

def awsqlhelp(help_type):
    print()
    index = help_types.index(help_type)
    with open('help.json') as file:
        data = load(file)
    print(data["help"][index][0])
    for line in data["help"][index][1:]:
        print("  " + line)