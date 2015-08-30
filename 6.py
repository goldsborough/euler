#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The sum of the squares of the first ten natural numbers is:

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""

def square_sum(n):
	return sum([m*m for m in range(1, n + 1)])

def sum_square(n):
	s = sum([m for m in range(1, n + 1)])
	return s * s

def difference(n):
	return sum_square(n) - square_sum(n)

def main():
	print(difference(100))

if __name__ == '__main__':
	main()