#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.
"""

def get_sum(values, row, column, sums={}):
    if (row, column) in sums:
        return sums[row, column]
    s = values[row][column]
    left = 0
    right = 0
    if column > 0:
        left = get_sum(values, row - 1, column - 1, sums)
    if column < row:
        right = get_sum(values, row - 1, column, sums)
    s += max([left, right])
    sums[row, column] = s

    return s


def largest_triangle_sum(values):
    largest = 0
    last_row = len(values) - 1
    for column in range(len(values[-1])):
        s = get_sum(values, last_row, column)
        if s > largest:
            largest = s

    return largest


def main():
    with open('triangle.txt') as source:
        triangle = source.read()
    values = [[int(j) for j in i.split()] for i in triangle.split('\n') if i]
    print(largest_triangle_sum(values))


if __name__ == '__main__':
    main()
