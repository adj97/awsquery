def welcome():
    print_message = [
        "Welcome to awsql, a cli tool for querying aws resources with SQL",
        "Usage: ",
        "$ awsql (opens SQL cli)",
        "$ awsql help [help type]",
        "Help types include: " + ", ".join(help_types)
    ]
    print("\n".join(print_message))

commands = [
    "help"
]

help_types = [
    "resources",
    "awsdocs"
]
