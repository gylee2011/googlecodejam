#! /usr/bin/env python

import sys

sys.stdin.readline()

case_number = 1
for line in sys.stdin.readlines():
	print "Case #%d:" % (case_number),
	for word in reversed(line.split()):
		print word,
	case_number = case_number + 1
	print ''
