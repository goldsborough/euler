#!/usr/bin/env python
# -*- coding: utf-8 -8-

"""
Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

def boxes(n):
	lattice = {(n - 1, n) : 1}
	for column in range(n - 1, -1, -1):
		for row in range(column, -1, -1):
			r = 0
			if column < n - 1:
				r += lattice[row, column + 1]
			if row < column:
				r += lattice[row + 1, column]
			else:
				r += lattice[row, column + 1]
			lattice[row, column] = r
	return lattice[0,0]

def edges(n):
	lattice = {(n - 1, n) : 1}
	for column in range(n - 1, -1, -1):
		for row in range(column, -1, -1):
			r = 0
			if column == n - 1:
				r += 1
			else:
				r += lattice[row, column + 1]
			if row < column:
				r += lattice[row + 1, column]
			else:
				r += lattice[row, column + 1]
			lattice[row, column] = r
	return lattice[0,0]

def main():
	print(edges(20))

if __name__ == '__main__':
	main()