#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """ replaces an element in a list at a specific position"""
    if idx < 0:
        return my_list
    elif idx > len(my_list) or idx == len(my_list):
        return my_list
    else:
        new_list = my_list[:]
        new_list[idx] = element
        return new_list
