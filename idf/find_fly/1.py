#!/usr/bin/env python3.4

with open('1.rar','rb') as f:
	byte = f.read()
	data = bytearray(byte)
	with open('2.rar','wb') as f1:
		data[23] = 0x80
		f1.write(data)
