#!/usr/bin/python3
if __name__ == "__main__":
    form sys import argv
    numargs = len(argv)
    if numargs < 2:
        print("{} arguments.".format(numargs - 1))
    else:
        if numargs == 2:
            print("{} argument:".format(numargs - 1))
        elif numargs > 2:
            print("{} arguments:".format(numargs - 1))
        for i in range(1, numargs):
            print("{}: {}".format(i, argv[i])
