#! /usr/bin/env python3.5

# Copyright (c) 2015 Krzysztof Magosa
# Problem: C. T9 Spelling
# Link: https://code.google.com/codejam/contest/351101/dashboard#s=p2

import sys

if __name__ == '__main__':
    keypad = {
        0: [' '],
        2: ['a', 'b', 'c'],
        3: ['d', 'e', 'f'],
        4: ['g', 'h', 'i'],
        5: ['j', 'k', 'l'],
        6: ['m', 'n', 'o'],
        7: ['p', 'q', 'r', 's'],
        8: ['t', 'u', 'v'],
        9: ['w', 'x', 'y', 'z']
    }

    keypresses = {}
    for digit, letters in keypad.items():
        for index, letter in enumerate(letters):
            keypresses[letter] = (str(digit), (index+1))

    n = int(sys.stdin.readline())

    for index in range(1, n+1):
        last = None
        line = sys.stdin.readline().rstrip('\n')

        print('Case #%d: ' % index, end='')
    
        for letter in line:
            current = keypresses[letter]

            # Delimit letters using the same key on keypad
            if last is not None and last[0] == current[0]:
                print(' ', end='')
                
            print(current[0] * current[1], end='')
            last = current

        print('')

