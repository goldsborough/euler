#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
A unit fraction contains 1 in the numerator. The decimal representation
of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring
cycle in its decimal fraction part.
"""

from __future__ import division

import re


def longest_cycle(limit):
    longest = 1
    champion = None
    cycle = re.compile(r'((\d+)(?=\2)){4,}')
    base = int('1' + '0' * int(1e4))
    for d in range(1, limit):
        floating = str(base//d)
        match = cycle.search(floating)
        if match:
            digits = match.group(1)
            if len(digits) < 2 or digits[0] == digits[1]:
                continue
            # print(d, floating, len(digits), digits)
            if len(digits) > longest:
                longest = len(digits)
                champion = d

    return longest, champion


def main():
    print(longest_cycle(1000))

if __name__ == '__main__':
    main()
