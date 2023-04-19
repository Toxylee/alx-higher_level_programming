#!/usr/bin/python3


def magic_calculation(x, y):
    result = 0
    for i in range(1, 3):
        try:
            if (i > x):
                raise Exception("Too far")
            else:
                result += (x**y) / i
        except Exception:
            result = x + y
            break
    return (result)
