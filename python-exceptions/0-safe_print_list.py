def safe_print_list(my_list=[], x=0):
    count = 0

    for number in range(x):
        try:
            print(my_list[number], end="")
            count += 1
        except IndexError:
            break

    print()
    return count
