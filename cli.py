def help():
    print_message = [
        "Welcome to <tool name>, a cli tool for <description>",
        "Commands include: " + ", ".join(commands),
        "usage: <tool name> <command> [parameters]"
    ]
    print("\n".join(print_message))

commands = [
    "help",
    "command1"
]
