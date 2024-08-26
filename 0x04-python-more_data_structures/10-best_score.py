#!/usr/bin/python3
def best_score(a_dictionary):
    keyc = next(iter(a_dictionary))
    maxi = a_dictionary[keyc]
    for x in a_dictionary.values():
        if maxi < x:
            maxi = x
    return (maxi)
w 
