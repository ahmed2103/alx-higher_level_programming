#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    if my_list:
        for i in range(x):
            try:
                value = my_list[i]
                if isinstance(value, int):
                    print("{:d}".format(value), end='')
                    printed += 1
            except (ValueError, TypeError):
                pass
    print()
    return printed
