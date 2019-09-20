#!/usr/bin/python3
def complex_delete(a_dictionary, value):

    del_list = []

    for elem in a_dictionary:
        if a_dictionary[elem] == value:
            del_list.append(elem)

    for keys in del_list:
        del a_dictionary[keys]

    return (a_dictionary)
