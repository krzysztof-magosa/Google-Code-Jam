#! /usr/bin/env python


def solve():
    n, x = [int(x) for x in input().split()]
    s = sorted([int(y) for y in input().split()], reverse=True)
    disks = 0

    while s:
        current = s.pop(0)
        remaining = x - current

        for i in s:
            if i <= remaining:
                current += i
                s.remove(i)
                break

        disks += 1

    return disks


t = int(input())
for it in range(1, t+1):
    print("Case #{}: {}".format(it, solve()))
