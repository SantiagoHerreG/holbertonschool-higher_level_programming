#!/usr/bin/python3
def roman_to_int(roman_string):

    my_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    new_list = []

    if not roman_string:
        return (0)

    for idx in range(len(roman_string)):
        for elem in my_dict:
            if roman_string[idx] == elem:
                new_list.append(my_dict[elem])
    if len(new_list) != len(roman_string):
        return (0)

    count = 0

    for i in range(len(new_list)):
        if ((i + 1) == len(new_list) or new_list[i] >= new_list[i + 1]):
            count += new_list[i]
        else:
            count -= new_list[i]

    return (count)
