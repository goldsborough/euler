#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of
28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum
of two abundant numbers.
"""

def is_abundant(n):
	sum_of_divisors = 1
	for k in range(2, n//2 + 1):
		if n % k == 0:
			sum_of_divisors += k
			if sum_of_divisors > n:
				return True

	return False

def sum_exists(n, integers):
	i = 0
	j = len(integers) - 1
	while i <= j:
		s = integers[i] + integers[j]
		if s < n:
			i += 1
		elif s > n:
			j -= 1
		else:
			return True

	return False
	

def sum_of_non_abundant_integers(limit):
	integers = sorted(i for i in range(1, limit + 1) if is_abundant(i))
	total = 0
	for n in range(1, limit + 1):
		if not sum_exists(n, integers):
			total += n

	return total

def main():
	limit = 28123
	print(sum_of_non_abundant_integers(limit))

if __name__ == '__main__':
	main()