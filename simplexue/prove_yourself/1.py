#!/usr/bin/env python3.4

s = [0x63,0x52,0x14,0x43,0x4B,0x69,0x53,0x73,0x4F,0x65,0x14,0x53,0x59,0x01]
t = ''

for i in s:
	t += chr(i ^ 0x20)
print(t)
