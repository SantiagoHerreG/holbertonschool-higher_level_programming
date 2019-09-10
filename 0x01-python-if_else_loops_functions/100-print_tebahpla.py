#!/usr/bin/python3
i = 122
j = 1
while i >= 65:
    print("{:s}".format(chr(i)), end='')
    j *= -1
    i += j * 32
    i -= 1
