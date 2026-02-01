def add_integer(a, b=98):
    # Check first parameter
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")

    # Check second parameter
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    # Convert floats to integers
    a = int(a)
    b = int(b)

    # Return the result
    return a + b
