#!/usr/bin/env python3.4

import re

with open('data','rt') as f:
	data = f.read().strip().split('\n')
count = {}
for d in data:
	count[d] = d.count('a')
count_s = sorted(count.items(), key=lambda x:x[1])

key = [0]*47
i = 0
equ=list(map(lambda x:x[0],count_s))
for a in range(len(equ)):
	for c in range(33,127):
		p = re.sub('a\[\d+\]',str(c),equ[a])
		if eval(p):
			key[i] = c
			equ = list(map(lambda x:x.replace('a[%d]'%i,str(key[i])),equ))
			i += 1
			break
fkey = ''
for c in key:
	fkey += chr(c)
print(fkey)
