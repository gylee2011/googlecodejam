#!  /usr/bin/env python

import sys


def find_pair(credit, price_list):
	for i in range(len(price_list)):
		for j in range(len(price_list)):
			if i==j:
				continue
			if price_list[i] + price_list[j] == credit:
				return (i+1, j+1)

num_of_cases = int(sys.stdin.readline())

for i in range(num_of_cases):
	credit = int(sys.stdin.readline())
	num_of_items = sys.stdin.readline()
	price_list = map(int, sys.stdin.readline().split())
	result = find_pair(credit, price_list)
	print "Case #%d: %d %d" % (i+1, result[0], result[1])
