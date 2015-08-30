#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10001-st prime number?

104743
"""

import math

def is_prime(n):
	if n <= 1:
		return False
	if n <= 3:
		return False
	if n % 2 == 0 or n % 3 == 0:
		return False
	limit = math.sqrt(n)
	m = 5
	while m <= limit:
		if n % m == 0 or n % (m + 2) == 0:
			return False
		m += 6
	return True

def brute(n):
	count = 0
	x = 0
	while count <= n:
		if is_prime(x):
			count += 1
		x += 1
	return x - 1

def main():
	print(brute(10001))

if __name__ == '__main__':
	main()