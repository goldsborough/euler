#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

cache = {}

def fibonacci_too_deep(n):
	if n in cache:
		return cache[n]
	elif n <= 2:
		return n
	value = fibonacci(n - 1) + fibonacci(n - 2)
	cache[n] = value

	return value

def fibonacci(n):
	x = 1
	y = 2
	for _ in range(2, n):
		y = x + y
		x = y - x

	return x

def binary_fib_search(lower, upper, target_length):
	if lower == upper:
		return None
	middle = (lower + upper)//2
	length = len(str(fibonacci(middle)))
	if target_length <= length:
		result = binary_fib_search(lower, middle, target_length)
		return result or middle

	return binary_fib_search(middle + 1, upper, target_length)

def main():
	print(binary_fib_search(0, 5000, 1000))

if __name__ == '__main__':
	main()