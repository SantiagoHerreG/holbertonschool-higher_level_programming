#!/usr/bin/python3
def best_score(a_dictionary):

    if not a_dictionary:
        return (None)

    new_dict = list(sorted(a_dictionary.values()))

    for elem in a_dictionary:
        if new_dict[-1] == a_dictionary[elem]:
            return (elem)
