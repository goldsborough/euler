#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
"""

seen = {}

def collatz(n):
	length = 1
	m = n
	while n > 1:
		if n % 2 == 0:
			n //= 2
		else:
			n = 3 * n + 1
		if n in seen:
			return length + seen[n]
		length += 1
	seen[m] = length
	return length

def longest_chain(n):
	longest = 0
	longest_k = 0
	for k in range(1, n):
		length = collatz(k)
		if length > longest:
			longest = length
			longest_k = k
	return longest_k


def main():
	print(longest_chain(1000000))

if __name__ == '__main__':
	main()