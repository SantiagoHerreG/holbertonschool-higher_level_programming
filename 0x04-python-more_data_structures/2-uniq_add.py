#!/usr/bin/python3
def uniq_add(my_list=[]):

    new_set = {elem for elem in my_list}

    count = 0
    for elem in new_set:
        count += elem
    return (count)
