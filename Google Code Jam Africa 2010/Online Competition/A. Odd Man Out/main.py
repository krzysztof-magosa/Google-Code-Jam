#! /usr/bin/env python3.5

# Copyright (c) 2015 Krzysztof Magosa
# Problem: A. Odd Man Out
# Link: https://code.google.com/codejam/contest/438101/dashboard#s=p0

if __name__ == '__main__':
    n = int(input())

    for ni in range(1, n+1):
        g = int(input())
        guests = [int(x) for x in input().split(' ')]
        counter = {}
        
        for guest in guests:
            if guest in counter:
                counter[guest] += 1
            else:
                counter[guest] = 1
        
        alones = [key for key, value in counter.items() if value == 1]
        print('Case #%d: %d' % (ni, alones[0]))
