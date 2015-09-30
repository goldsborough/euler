#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the
digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

10! = 3,628,800 possibilities

The first entries in the sorted sequence of permutations would have the 0 in
front, leaving 9 digits with:

9! = 362,880 possibilities

So if we fix the first digit, we are left with that many possibilities.
Therefore, if sum all the possible permutations if we fix the first digit at
0, 1 and 2, we get 362,880 * 3 = 1,088,640 options. All values starting with
digit 3 would already be lexicographically greater. Furthermore, we can deduce
that the value must have a 3 at the start, because when 3 is at the start the
values lie between 725,760 and 1,088,640. And so on and so forth.

(9! * 2) + (8! * 6) + (7! * 6)
"""

def find_permutations(source, index=0, string=""):
	if index >= len(source):
		return []
	char = source[index]
	permutations = []
	for n in range(len(string) + 1):
		permuted = string[:n] + char + string[n:]
		if index == len(source) - 1:
			permutations.append(permuted)
		permutations += find_permutations(source, index + 1, permuted)

	return permutations

def find_millionth():
	prefix = '27'
	rest = ''.join(str(i) for i in range(10) if str(i) not in prefix)

	permutations = find_permutations(rest)
	permutations.sort()

	f = lambda x: x * f(x - 1) if x else 1
	offset = (f(9) * 2) + (f(8) * 6)

	return prefix + permutations[int(1e6) - offset - 1]

def main():
	print(find_millionth())

if __name__ == '__main__':
	main()
