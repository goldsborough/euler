#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

def is_prime(n):
	if n <= 1:
		return False
	if n <= 3:
		return True
	if n % 2 == 0 or n % 3 == 0:
		return False
	# Only need to check up to sqrt(N)
	# after, the terms of the products
	# making up the number flip, e.g.
	# 2 * 10, ...., 10 * 20 for 20
	limit = math.sqrt(n)
	# Next prime after 3
	m = 5 
	while m <= limit:
		# All primes are of the form
		# 6k +- 1, so we start at 5
		# (6 * 1 - 1) and then check
		# 5 + 2 = 6 + 1 = 7, etc.
		if n % m == 0 or n % m + 2 == 0:
			return False
		m += 6
	return True

def largest_prime(n):
	p = -1
	m = 5
	while n > 1:
		if n % 2 == 0:
			n /= 2
			p = m
		if n % 3 == 0:
			n /= 3
			p = m
		if n % m == 0:
			n /= m
			p = m
		if n % (m + 2) == 0:
			n /= (m + 2)
			p = m + 2
		m += 6
	return p

def main():
	print(largest_prime(600851475143))

if __name__ == '__main__':
	main()