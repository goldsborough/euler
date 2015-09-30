#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a
name score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

def char_sum(name):
	# More efficient than ord
	alphabet = {chr(65 + n - 1) : n for n in range(1, 27)}

	return sum(alphabet[char] for char in name)

def sum_of_scores(names):
	total = 0
	for n, name in enumerate(sorted(names)):
		total += char_sum(name) * (n + 1)

	return total


def main():
	with open('names.txt') as source:
		names = [i[1:-1] for i in source.read().split(',') if i]
		print(sum_of_scores(names))

if __name__ == '__main__':
	main()
