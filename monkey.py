#!/usr/bin/env python
# -*- coding: utf-8 -*-
monkey = [0] * 50
monkey[0] = 1
monkey[1] = 2
for i in xrange(48):
    monkey[i+2] = monkey[i] + monkey[i+1]

print monkey[2]
print monkey[49]
