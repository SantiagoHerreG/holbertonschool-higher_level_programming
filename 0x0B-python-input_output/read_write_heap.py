#!/usr/bin/python3
"""script that finds a string in the heap of a running process,
and replaces it.

"""
import sys

if len(sys.argv) != 4:
    print("Usage: read_write_heap.py pid search_string replace_string")
    exit(1)

with open("/proc/" + sys.argv[1] + "/maps", encoding="UTF-8") as f:

    for lines in f:

        if "heap" in lines:
            words_in_line = lines.split()
            address = words_in_line[0].split('-')

address_start = int(address[0], 16)
address_end = int(address[1], 16)

with open("/proc/" + sys.argv[1] + "/mem", mode="rb+") as f:

    f.seek(address_start)
    read_heap = f.read(address_end - address_start)
    try:
        position_of_string = read_heap.index(bytes(sys.argv[2], "ASCII"))
    except:
        exit(0)
    f.seek(address_start + position_of_string)
    if sys.argv[3] == "":
        f.write("\0")
        exit(0)
    new_str = bytes(sys.argv[3], "ASCII")
    f.write(new_str)
