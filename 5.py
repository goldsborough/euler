#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
2520 is the smallest number that can be divided by each
of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20?
"""

def brute(n):
	x = 1
	while True:
		for m in range(1, n + 1):
			if x % m != 0:
				break
		else:
			return x
		x += 1

def get_range(r):
	r = [x for x in range(2, r + 1)]
	i = len(r) - 1
	while i >= 0:
		for j in r[:i]:
			if r[i] % j == 0:
				r.remove(j)
				i -= 1
		i -= 1
	return r

def better(n):
	x = n + 1
	r = get_range(n)
	while True:
		for m in r:
			if x % m != 0:
				break
		else:
			return x
		x += 1
	return x


def main():
	print(better(20))

if __name__ == '__main__':
	main()