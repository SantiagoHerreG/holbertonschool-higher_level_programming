#!/usr/bin/python3
def search_replace(my_list, search, replace):

    new_list = []

    if not my_list:
        return (None)

    for value in my_list:
        if value == search:
            new_list.append(replace)
        else:
            new_list.append(value)

    return (new_list)
