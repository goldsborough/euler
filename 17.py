#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out
in words, how many letters would be used?
"""

def letters(n, m=1):
	single = {
		'0': '',
		'1': 'one',
		'2': 'two',
		'3': 'three',
		'4': 'four',
		'5': 'five',
		'6': 'six',
		'7': 'seven',
		'8': 'eight',
		'9': 'nine',
	}
	tens = {
		'1': 'teen',
		'2': 'twenty',
		'3': 'thirty',
		'4': 'forty',
		'5': 'fifty',
		'6': 'sixty',
		'7': 'seventy',
		'8': 'eighty',
		'9': 'ninety',	
	}
	orders = {
		3: 'thousand',
		6: 'million',
		9: 'billion',
		12: 'trillion'
	}
	special = {
		'10': 'ten',
		'11': 'eleven',
		'12': 'twelve',
		'13': 'thirteen',
		'15': 'fifteen',
		'18': 'eighteen'
	}
	length = 0
	for n in range(m, n + 1):
		string = str(n)[::-1]
		k = 0
		while k < len(string):
			digit = string[k]
			if digit != '0' and k % 3 == 1:
				length += len(tens[digit])
			if digit != '0' and k % 3 == 2:
				length += len(single[digit])
				length += len('hundred')
				if string[:-1] != '00':
					length += len('and')
			if k in orders:
				length += len(orders[k])
				if string != '{0}1'.format('0' * k):
					length += len('and')
			if k % 3 == 0:
				if string[k:k+2][::-1] in special:
					length += len(special[string[k:k+2][::-1]])
					k += 1
				else:
					length += len(single[digit])
			k += 1
	return length

def main():
	print(letters(1000))

if __name__ == '__main__':
	main()

