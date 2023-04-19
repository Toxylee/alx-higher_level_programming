#!/usr/bin/python3
from sys import stderr


def safe_function(a, *args):
    try:
        return a(*args)
    except (ZeroDivisionError, IndexError, TypeError, ValueError) as err:
        stderr.write("Exception: {}\n".format(err))
        return None
