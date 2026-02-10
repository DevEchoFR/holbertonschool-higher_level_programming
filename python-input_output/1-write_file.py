#!/usr/bin/python3
def write_file(filename="", text=""):
    # Open the file using the correct mode
    with open(filename, mode="w") as numbers:
        # Write the text to the file
        text = numbers.write(numbers)

    # Return the number of characters written
    return text
