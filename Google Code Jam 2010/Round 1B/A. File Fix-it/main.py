#! /usr/bin/env python3.5

# Copyright (c) 2015 Krzysztof Magosa
# Problem: A. File Fix-it
# Link: https://code.google.com/codejam/contest/635101/dashboard#s=p0

import sys

def expand_nests(path):
    parts = path.rstrip('/').split('/')
    return ['/'.join(parts[:x]) for x in range(2, len(parts)+1)]

if __name__ == '__main__':
    t = int(sys.stdin.readline())

    for ti in range(1, t+1):
        n, m = [int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
        
        existing = []
        for ni in range(1, n+1):
            existing.extend(expand_nests(sys.stdin.readline().rstrip('\n')))

        created = 0
        requested = []
        for mi in range(1, m+1):
            nests = expand_nests(sys.stdin.readline().rstrip('\n'))

            for nest in nests:
                if nest not in existing:
                    created += 1
                    existing.append(nest)

        print('Case #%d: %d' % (ti, created))
