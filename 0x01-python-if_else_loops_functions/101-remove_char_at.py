#!/usr/bin/python3
def remove_char_at(words, n):

    string = ''
    for i in range(0, len(words)):
        if (i != n):
            string = string + words[i]
    words = string
    return (words)
