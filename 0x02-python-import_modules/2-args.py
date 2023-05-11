#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    len = len(argv) - 1
    if len == 0:
        print("0 arguments.")
    elif len == 1:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{:d} arguments:".format(len))
        i = 1
        while i <= len:
            print("{:d}: {}".format(i, argv[i]))
            i += 1
