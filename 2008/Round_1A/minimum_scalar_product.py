#!  /usr/bin/env python

import sys

T = int(sys.stdin.readline())

for i in range(T):
	n = int(sys.stdin.readline())
	v1 = map(int, sys.stdin.readline().split())
	v2 = map(int, sys.stdin.readline().split())
	v1.sort()
	v2.sort()
	v2.reverse()
	print "Case #%d: %d" % (i+1, reduce( (lambda x, y: x+y), map( (lambda x, y: x*y), v1, v2 ) ) )
