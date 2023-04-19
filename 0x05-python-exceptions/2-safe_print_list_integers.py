#!/usr/bin/python3


def safe_print_list_integers(my_list=[], t=0):
    size = 0
    for idx in range(t):
        try:
            print("{:d}".format(my_list[idx]), end="")
        except (ValueError, TypeError):
            continue
        size = size + 1
    print("")
    return size
