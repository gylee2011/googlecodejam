#! /usr/bin/env python

import sys

keymap = {}
keymap[' '] = '0'
num = 1
last_spell = ''
for letter in 'abcdefghijklmnopqrstuvwxyz':
	if letter in 'adgjmptw':
		num = num + 1
		last_spell = ''
	keymap[letter] = last_spell + str(num)
	last_spell = keymap[letter]

def find_spell(line):
	ret = []
	last_number = ''
	for letter in line:
		if letter not in keymap.keys():
			continue
		val = keymap[letter]
		if last_number == val[0]:
			ret.append(' ')
		ret.append(val)
		last_number = val[0]
	return ret

num_of_cases = int(sys.stdin.readline())

for i in range(num_of_cases):
	print "Case #%d: " % (i+1),
	last_number = 0
	for item in find_spell(sys.stdin.readline()):
		sys.stdout.write(item)
	print
