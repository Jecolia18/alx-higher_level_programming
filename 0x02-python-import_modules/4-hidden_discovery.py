#!/usr/bin/python3
from hidden_4 import *
if __name__ == "__main__":
    names = dir(hidden_4)
    for name in names:
        if name != '_':
            print(name)
