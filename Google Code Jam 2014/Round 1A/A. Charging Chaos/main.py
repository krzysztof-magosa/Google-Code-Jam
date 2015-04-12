#! /usr/bin/env python

from collections import Counter
from sys import maxsize

t = int(input())
for it in range(1, t+1):
    n, l = [int(x) for x in input().rstrip('\n').split()]
    outlets = [int(x, 2) for x in input().rstrip('\n').split()]
    devices = [int(x, 2) for x in input().rstrip('\n').split()]
    devicesCounter = Counter(devices)

    best = maxsize
    """
    By XORing each outlet with first device we are getting
    just bits (buttons) which are in incorrect position.

    e.g.
    outlet = 010010
    device = 110010
           ^ 100000
    """

    for flips in set((x ^ devices[0]) for x in outlets):
        flipped = ((y ^ flips) for y in outlets)

        if Counter(flipped) == devicesCounter:
            best = min(best, bin(flips).count("1"))

    print("Case #{}: {}".format(it, "NOT POSSIBLE" if best == maxsize else best))
