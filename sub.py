#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

fp = open("Eng.srt")
cnt = 0
label = False

for each in fp:
	if re.match(r'\d\d\:\d\d\:\d\d\,\d\d\d\s\-\-\>\s\d\d\:\d\d\:\d\d\,\d\d\d',each):
		label = True
	if not label:
		continue
	else:
		pass
	
	cnt += 1
	print each