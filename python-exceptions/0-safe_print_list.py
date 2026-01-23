def safe_print_list(my_list=[], x=0):
    count = 0

    for items in range(x):
        try:
            print(items, end="")
            count += 1
        except IndexError:
            break

    print()
    return count
