#!/usr/bin/python3
if __name__ == "__main__"
    import sys
    sum = 0
    num = len(sys.argv)
    if num < 2:
        print("0")
    else: 
        for i in range(1, num):
            sum += int(argv[i])
            print("{}".format(sum))
