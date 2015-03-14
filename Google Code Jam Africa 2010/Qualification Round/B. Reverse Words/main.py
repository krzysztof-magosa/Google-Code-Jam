#! /usr/bin/env python3.5

# Copyright (c) 2015 Krzysztof Magosa
# Problem: B. Reverse Words
# Link: https://code.google.com/codejam/contest/351101/dashboard#s=p1

import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())

    for index in range(1, n+1):
        words = sys.stdin.readline().rstrip('\n').split(' ')
        print('Case #%d: %s' % (index, ' '.join(reversed(words))))
