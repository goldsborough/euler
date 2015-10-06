#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n² + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
"""

import math

def is_prime(n):
	if n <= 1:
		return False
	if n <= 3:
		return True
	if n % 2 == 0 or n % 3 == 0:
		return False
	for m in range(5, int(math.ceil(math.sqrt(n))), 6):
		if n % m == 0 or n % (m + 2) == 0:
			return False
	return True

def number_of_primes(expression):
	n = 0
	while is_prime(expression(n)):
		n += 1
	return n - 1

def find_coefficients(limit):
	largest = 0
	best_a = None
	best_b = None
	for a in range(-limit, limit):
		for b in range(-limit, limit):
			number = number_of_primes(lambda n: n*n + a*n + b)
			if number > largest:
				largest = number
				best_a, best_b = a, b

	return best_a, best_b, largest

def main():
	print(find_coefficients(1000))

if __name__ == '__main__':
	main()
