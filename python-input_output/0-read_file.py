#!/usr/bin/python3
def read_file(filename=""):
    # Open the file using the correct keyword
    with open(filename, mode="r") as text:
        # Read the entire file content
        content = text.read()

        # Print the content to standard output
        print(content)
