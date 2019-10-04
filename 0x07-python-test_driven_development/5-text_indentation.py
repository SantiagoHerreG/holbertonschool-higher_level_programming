#!/usr/bin/python3
""" Module containing a function that prints a text
with 2 new lines after each of these characters: ., ? and :
5- task in python Test-driven development project


"""


def text_indentation(text):
    """ Function that prints a square of #'s
    Args:

        text (str): text to be printed
    """

    if isinstance(text, str) is False:
        raise TypeError("text must be a string")

    length = len(text)
    i = 0
    new_text = ""

    while i in range(length):
        if text[i] != ' ':
            break
        else:
            i += 1

    new_text += text[i:]
    i = 0
    length = len(new_text)

    while i in range(length):
        print(new_text[i], end="")

        if new_text[i] in ['.', '?', ':']:
            print('\n')

            while i + 1 < length:
                if new_text[i + 1] == " ":
                    i += 1
                else:
                    break
        i += 1
        if i < length:
            j = length - 1
            while j >= i:
                if new_text[j] == ' ':
                    if j == i:
                        return
                    j -= 1
                    continue
                else:
                    break
