#!/usr/bin/python3
if __name__ == "__main__":
    form sys import argv
    argc = len(argv)
    if argc == 0:
        print("{} arguments.".format(argc))
    if argc == 1:
        print("{} arguments:".format(argc - 1))
    elif argc == 2:
        print("{} argument.".format(argc - 1))
    else:
        print("{} arguments:".format(argc - 1))
    for i in range(1, argc):
        print("{}: {}".format(i, argv[i])
