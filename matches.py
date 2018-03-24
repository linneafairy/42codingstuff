#!/usr/bin/env python
#by lleaver
import sys

try:
    n = int(sys.argv[1])
except ValueError:
    print "That's not an integer"
    n = 0
#minimum amount of matches to construct n squares
def findMatches (squares):
    return squares * (5 - squares)

print findMatches(n)
