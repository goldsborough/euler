#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import math

def is_prime(n):
	if n <= 1:
		return False
	if n <= 3:
		return True
	if n % 2 == 0 or n % 3 == 0:
		return False
	for m in range(5, int(math.sqrt(n)) + 1, 6):
		if n % m == 0 or n % (m + 2) == 0:
			return False
	return True

def brute(n):
	s = 0
	for k in range(2, n + 1):
		if is_prime(k):
			s += k
	return s

def better(n):
	r = [True for _ in range(n + 1)]
	for i in range(2, int(math.sqrt(n)) + 1):
		if r[i]:
			for j in range(i*i, len(r), i):
				r[j] = False
	s = 0
	for i in range(2, len(r)):
		if r[i]:
			s += i
	return s

def main():
	print(better(10))

if __name__ == '__main__':
	main()