#!/usr/bin/python3
def uppercase(string):
    i = 0
    while i < len(string):
        if (ord(string[i]) >= 97 and ord(string[i]) <= 122):
            char = chr(ord(string[i]) - (97 - 65))
            i += 1
        else:
            char = string[i]
            i += 1
        print("{:s}".format(char), end="")
    print()
