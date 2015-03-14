#! /usr/bin/env python3.5

# Copyright (c) 2015 Krzysztof Magosa
# Problem: A. Store Credit
# Link: https://code.google.com/codejam/contest/351101/dashboard#s=p0

import sys

def find_pair(c, i, p):
    for a in range(0, i):
        for b in range(a+1, i):
            if ((p[a] + p[b]) == c):
                return a+1, b+1

if __name__ == '__main__':
    n = int(sys.stdin.readline())

    for index in range(1, n+1):
        c = int(sys.stdin.readline())
        i = int(sys.stdin.readline())
        p = list(map(int, sys.stdin.readline().split(' ')))
        pair = find_pair(c, i, p)

        print('Case #' + str(index) + ': ' + str(pair[0]) + ' ' + str(pair[1]))
