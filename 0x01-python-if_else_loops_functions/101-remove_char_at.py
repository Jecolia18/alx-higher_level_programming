#!/usr/bin/python3
def remove_char_at(str, n):
    """
    creates a copy of the string
    remove the character at the position n
    """
    if n < 0:
        return str
    return str[:n] + str[n + 1:]
