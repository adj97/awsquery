output_types={
    "o":" output",
    "e":"  error",
    "h":"   help"
}

def output(type, output):
    output = ["awsquery", output_types[type], str(output)]
    print(": ".join(output))
