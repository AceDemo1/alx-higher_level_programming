#!/usr/bin/python3
if __name__ == "__main__":
    form sys import argv
    numargs = len(argv)
    if numargs == 1:
        print("0 arguments.")
    else:
        if numargs == 2:
            print("1 argument:")
        elif numargs > 2:
            print("{} arguments:".format(numargs - 1))
        for i in range(1, numargs):
            print("{}: {}".format(i, argv[i])
