#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """ returns a new dictionary with all values multiplied by 2"""
    dicky_dictionary = {x: a_dictionary[x] * 2 for x in a_dictionary.keys()}
    return (dicky_dictionary)
