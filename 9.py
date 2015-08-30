#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

I. a^2 + b^2 = c^2
II. a + b + c = 1000
III. a * b * c = x

c = sqrt(a^2 + b^2)
"""

import math

def is_pythagorean(a, b, c):
	return a*a + b*b == c*c

def brute(n):
	for c in range(1, n):
		for a in range(1, c):
			for b in range(a, c):
				if is_pythagorean(a, b, c) and a + b + c == n:
					return a * b * c

def better(n):
	for a in range(1, n//2):
		for b in range(a, n//2):
			c = math.sqrt(a*a + b*b)
			if a + b + c == n:
				return a * b * c

def main():
	print(better(1000))

if __name__ == '__main__':
	main()