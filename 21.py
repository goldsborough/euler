#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Let d(n) be defined as the sum of proper divisors of n (numbers
less than n which divide evenly into n).

If d(a) = b and d(b) = a, where a ≠ b, then a and b are an
amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71
and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10,000.
"""

def d(n):
	sum_of_divisors = 0
	for k in range(1, n//2 + 1):
		if n % k == 0:
			sum_of_divisors += k

	return sum_of_divisors

def brute(N):
	amicable_sum = 0
	amicable_numbers = set()
	for n in range(1, N):
		if n in amicable_numbers:
			continue
		m = d(n)
		if n != m and d(m) == n:
			amicable_sum += m + n
			amicable_numbers.add(m)
			amicable_numbers.add(n)
	return amicable_sum

def get_amicable_sum(N):
	return brute(N)

def main():
	print(get_amicable_sum(10000))

if __name__ == '__main__':
	main()