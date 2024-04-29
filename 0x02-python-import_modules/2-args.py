#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":

    num_argv = len(argv)
    if num_argv == 1:
        print("0 arguments.")
    elif num_argv == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_argv-1))
    for i in range(1, num_argv):
        print("{}: {}".format(i, argv[i]))
