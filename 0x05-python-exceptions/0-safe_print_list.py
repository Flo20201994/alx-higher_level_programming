#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    k = 0
    list_len = 0
    for ele in my_list:
        list_len += 1
    if (x > list_len):
        x = list_len
    try:
        for k in range(0, x):
            print(my_list[k], end="")
        print()
    except:
        print("error occured")
    finally:
        return k + 1
