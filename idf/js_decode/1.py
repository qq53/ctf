#!/usr/bin/env python3.4

s = '1d1b1d1c1e4d4747191a1a4819464d194d1d191e4619484f4e4d484d48484b4f'
t = ''
print(len(s))
for i in range(0,len(s),2):
	h = int(s[i:i+2],16)
	r = 127-h
	print(r)
	t += chr(r)
print(t)
