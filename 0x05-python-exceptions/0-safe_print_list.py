#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        n = 0
        while (n < x):
            print(my_list[n], end="")
            n += 1
        print()
        return n
    except:
        print()
        return n
