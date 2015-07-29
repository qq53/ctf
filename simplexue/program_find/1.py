#!/usr/bin/env python3.4

s = 'xztiofwhf'
t = ''

for c in s:
	for i in range(26):
		if (i*5+11)%26 == ord(c)-ord('a'):
			t += chr(ord('a')+i)
print(t)
