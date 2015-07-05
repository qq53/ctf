#!/usr/bin/env python3.4

s = 'DVVFXK{Ig45tI(oNs|Hbjdlf}'
t = ''
j = 0

for i in s:
	t += chr(ord(i)-j)
	j = (j+1)%6
print(t)
