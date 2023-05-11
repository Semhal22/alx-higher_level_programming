#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    length = len(argv) - 1
    if length == 0:
        print("0 arguments.")
    elif length == 1:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{:d} arguments:".format(length))
        i = 1
        while i <= length:
            print("{:d}: {}".format(i, argv[i]))
            i += 1
