#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_set = set()
    for wrd_1 in set_1:
        for wrd_2 in set_2:
            if wrd_1 == wrd_2:
                new_set.add(wrd_1)
    return (new_set)
