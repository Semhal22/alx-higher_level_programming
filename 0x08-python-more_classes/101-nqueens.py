#!/usr/bin/python3
import sys
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
N = int(sys.argv[1])
if type(N) is not int:
    print("N must be a number")
    sys.exit(1)
if N < 4:
    print("N must be at least 4")
    sys.exit(1)
