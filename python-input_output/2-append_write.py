#!/usr/bin/python3
def append_write(filename="", text=""):
    # Open the file using append mode
    with open(filename, mode="a") as something:
        # Write the text to the file
        result = something.write(text)

    # Return the number of characters added
    return result
