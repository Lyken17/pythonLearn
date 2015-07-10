#!/usr/bin/env python
age = int(raw_input('Please enter your age\n'))
while age > 0:
	if age >= 18:
		print 'Adult,allowed'
	else:
		print 'Children,refused'
	age = int(raw_input('Please enter your age\n'))
