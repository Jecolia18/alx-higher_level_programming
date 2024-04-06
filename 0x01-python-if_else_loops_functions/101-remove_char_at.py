#!/usr/bin/python3
def remove_char_at(str, n):
    count = 0
    for c in str:
        if count == n:
            count += 1
            continue
        print(c, end="")
        count +=1
    print()
