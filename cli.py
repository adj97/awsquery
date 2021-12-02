def help():
    print_message = [
        "Welcome to awsquery, a cli tool for querying aws resources with SQL",
        "Commands include: " + ", ".join(commands),
        "usage: awsquery <command> [parameters]"
    ]
    print("\n".join(print_message))

commands = [
    "help",
    "command1"
]
