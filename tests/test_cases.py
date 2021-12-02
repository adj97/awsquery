from helpers import *

def output():
    expected_output = [
        "awsql:  output: qwertyuiop12345",
        "awsql:   error: qwertyuiop12345",
        "awsql:    help: qwertyuiop12345"
    ]
    input = [
        ["o", "qwertyuiop12345"],
        ["e", "qwertyuiop12345"],
        ["h", "qwertyuiop12345"]
    ]

    for i,e in zip(input, expected_output):
        assert output(i[0], i[1]) == e
