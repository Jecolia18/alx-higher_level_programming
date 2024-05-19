#!/usr/bin/python3
def element_at(my_list, idx):
    """ retrieves an element from a list"""
    if idx == len(my_list) or idx > len(my_list):
        return None
    elif idx < 0:
        return None
    else:
        return my_list[idx]
