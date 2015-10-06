#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""

def lower_bound(sequence, lower, upper, value):
	if lower == upper:
		return None
	middle = (lower + upper) // 2
	if value < sequence[middle]:
		result = lower_bound(sequence, lower, middle, value)
		return middle if result is None else result
	elif value > sequence[middle]:
		result = lower_bound(sequence, middle + 1, upper, value)
		return upper if result is None else result
	else:
		return middle

def combinations(value, cache):
	if value in cache:
		return cache[value]
	if value == 0:
		return [[]]
	possibilities = []
	for i in [1, 2, 5, 10, 20, 50, 100, 200]:
		if i <= value:
			for j in combinations(value - i, cache):
				if j:
					#print('!', value, i, j, possibilities)
					index = lower_bound(j, 0, len(j), i)
					permutation = j[:]
					permutation.insert(index, i)
					if permutation not in possibilities:
						possibilities.append(permutation)
					#print(permutation, index, possibilities)
				else:
					possibilities.append([i])
	cache[value] = possibilities

	return possibilities

def find_combinations(value):
	cache = {}
	result = len(combinations(value, cache))
	#print(cache)
	return result

def main():
	l = [2, 2]
	#print(lower_bound(l, 0, len(l), 1))
	print(find_combinations(200))

if __name__ == '__main__':
	main()
