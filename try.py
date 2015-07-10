#!/usr/bin/env python
# -*- coding: utf-8 -*-

arr = []
for i in xrange(5):
    arr.append(i)
    for j in xrange(5):
        arr[i].append(j)

print arr
