#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg_count = len(sys.argv) - 1
    if arg_count == 0:
        print("0 arguments.")
    elif arg_count != 0:
        print("{} argument{}:".format(
            arg_count,
            "" if arg_count == 1 else "s"
		))
    for i in range(1, arg_count + 1):
        print("{}: {}".format(i, sys.argv[i]))
