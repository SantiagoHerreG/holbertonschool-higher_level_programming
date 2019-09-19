#!/usr/bin/python3
def weight_average(my_list=[]):

    if not my_list:
        return(0)

    mul_count = 0
    div_count = 0

    for i in my_list:
        mul_count += i[0] * i[1]
        div_count += i[1]

    return (mul_count / div_count)
