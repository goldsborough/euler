#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

def sm(n, p):
	if p == 0:
		return 1
	if p == 1:
		return n
	if n == 2:
		return 1 << p
	if p % 2 == 0:
		return sm(n * n, p//2)
	return n * sm(n * n, p//2)

def easy(n):
	print(sum(int(i) for i in str(2**n)))

def main():
	print(sm(2, 1000))

if __name__ == '__main__':
	main()

