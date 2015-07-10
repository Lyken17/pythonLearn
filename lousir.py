#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools
import string

ReVarHash = {   "00000" : "$zero" ,
                "00001" : "$at"   ,
                "00010" : "$v0"   ,
                "00011" : "$v1"   ,
                "00100" : "$a0"   ,
                "00101" : "$a1"   ,
                "00110" : "$a2"   ,
                "00111" : "$a3"   ,
                "01000" : "$t0"   ,
                "01001" : "$t1"   ,
                "01010" : "$t2"   ,
                "01011" : "$t3"   ,
                "01100" : "$t4"   ,
                "01101" : "$t5"   ,
                "01110" : "$t6"   ,
                "01111" : "$t7"   ,
                "10000" : "$s0"   ,
                "10001" : "$s1"   ,
                "10010" : "$s2"   ,
                "10011" : "$s3"   ,
                "10100" : "$s4"   ,
                "10101" : "$s5"   ,
                "10110" : "$s6"   ,
                "10111" : "$s7"   ,
                "11000" : "$t8"   ,
                "11001" : "$t9"
            }

int2 = functools.partial(int, base=2)
int16 = functools.partial(int, base=16)


R_type = {"000000"}
I_type = {"100011","101011","000100"}
J_type = {"000010"}

fp = open("input")
cin = fp.read()

stdin = cin.split("\n")[:-1]
stdout = []
for lines in stdin:
	#print lines
	insert = ""
	if lines[0:6] in R_type:#R type
		if lines[-6:] == "100000": #add
			insert += "add    "
		elif lines[-6:] == "100010": #sub
			insert += "sub    "
		elif insert[-6:] == "101010": #slt
			insert += "slt    "
		insert += ReVarHash[lines[6:11]] + ','
		insert += ReVarHash[lines[11:16]] + ','
		insert += ReVarHash[lines[16:21]]
	elif lines[0:6] in I_type:
		if lines[0:6] == "100011":
			insert += "lw     "
		elif lines[0:6] == "101011":
			insert += "sw     "
		elif lines[0:6] == "000100":
			insert += "beq    "
		insert += ReVarHash[lines[6:11]] + ','
		insert += str(int2(lines[16:])) + '(' + ReVarHash[lines[11:16]] + ')'
	elif lines[0:6] in J_type:
		shift = 0
		if lines[0:6] == "000010":
			insert += "j      "
		if lines[6] == '1':
			address = ['0' if i == '1' else '0' for i in lines[6:]]
			shift = int16(address) - 1
		else:
			address = lines[6:]
			shift = int16(address)
		insert += "0x" + str(shift)

	#print insert
	stdout.append(insert)

for lines in stdout:
	print lines
