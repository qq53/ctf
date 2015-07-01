#!/usr/bin/env python3.4

str = 'ABAAAABABBABAAAABABAAABAAAAAABAAAAAAAABAABBBAABBAB'

str = str.replace('A','0')
str = str.replace('B','1')

d = ''
for i in range(len(str)//5):
	v = int(str[i*5:i*5+5],2)
	d += chr(v+ord('a'))
print(d)
