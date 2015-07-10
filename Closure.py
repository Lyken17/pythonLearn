#!/usr/bin/env python
def count():
	fs = []
	for i in range(1,4):
		def f(j):
			def g():
				return j * j
			return g
		fs.append(f(i))
	return fs

f1 ,f2, f3 = count()
print f1()
print f2()
print f3()
