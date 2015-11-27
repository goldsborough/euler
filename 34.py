#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def get_factorials(n):
	f = lambda x: x * f(x - 1) if x else 1
	return [f(i) for i in range(n)]


def sum_factorial_digits(limit):
	factorial = get_factorials(10)
	total = 0
	digit_sum = 0
	order = int(math.log10(limit))
	for n in range(3, int(limit)):
		digit = n % 10
		if digit == 0:
			digit_sum = 0
			value = n
			for i in range(order):
				digit_sum += factorial[value % 10]
				value //= 10
				if value == 0:
					break
		else:
			digit_sum += factorial[digit]
		if digit_sum == n:
			total += n
		digit_sum -= factorial[digit]

	return total

def main():
	print(sum_factorial_digits(1e4))

if __name__ == '__main__':
	main()
