#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(number):
	string = str(number)
	return string == string[::-1]

def largest_palindrome(digits):
	start = int('1{0}'.format('0' * (digits - 1)))
	end = int('1{0}'.format('0' * digits))
	largest = 0
	for n in range(start, end):
		for m in range(n, end):
			x = n * m
			if is_palindrome(x) and x > largest:
				largest = x
	return largest


def main():
	print(largest_palindrome(3))

if __name__ == '__main__':
	main()