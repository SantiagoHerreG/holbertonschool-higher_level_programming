#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    print("Last digit of {} is {}".format(number, number % (-10)), end="")
    print(" and is less than 6 and not 0")
else:
    if number % 10 > 5:
        print("Last digit of {} is {}".format(number, number % 10), end="")
        print(" and is greater than 5")
    elif number % 10 == 0:
        print("Last digit of {} is 0 and is 0".format(number))
