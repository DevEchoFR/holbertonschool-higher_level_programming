def print_sorted_dictionary(a_dictionary):
    keys = a_dictionary.keys()
    sorted_keys = sorted(keys)
    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))
