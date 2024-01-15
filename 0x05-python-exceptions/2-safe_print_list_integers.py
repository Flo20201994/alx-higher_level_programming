#!/usr/bin/python3

"""
Write a function that prints the first x elements of a list and only integers.
"""


def safe_print_list_integers(my_list=[], x=0):
    w = 0
    for k in range(0, x):
        try:
            print("{:d}".format(my_list[k]), end="")
            w += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (k)
