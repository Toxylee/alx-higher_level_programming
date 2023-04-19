#!/usr/bin/python3


def safe_print_list(my_list=[], a=0):
    leth = 0
    while leth < a:
        try:
            print("{}".format(my_list[leth]), end="")
        except IndexError:
            break
        leth += 1
    print("")
    return leth
