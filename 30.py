#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Surprisingly there are only three numbers that can be written as the sum
of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of
fifth powers of their digits.
"""

def equals_sum_of_powers(n, p):
	return n == sum(i*i*i*i*i for i in map(int, str(n)) if i)

def sum_of_power(p, limit = 2e5):
	total = 0
	for n in range(2, int(limit)):
		if equals_sum_of_powers(n, p):
			total += n

	return total

def main():
	print(sum_of_power(5))

if __name__ == '__main__':
	main()
