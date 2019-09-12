#!/usr/bin/python3

import hidden_4

name_list = dir(hidden_4)

for i in range(0, len(name_list)):
    if (name_list[i][0] == "_" and name_list[i][1] == "_"):
        continue
    print(name_list[i])
