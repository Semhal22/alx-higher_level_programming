#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    length = len(argv) - 1
    i = 1
    sum = 0
    while i <= length:
        sum += int(argv[i])
        i += 1
    print(sum)
