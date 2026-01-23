#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = a_dictionary.key()
    sorted_keys = sorted(keys)
    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))
