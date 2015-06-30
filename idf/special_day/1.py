#!/usr/bin/env python3.4

import binascii

for y in range(1990, 2020):
	for m in range(1,13):
		for d in range(1,32):
			day = '%d%02d%02d' % (y,m,d)
			if binascii.crc32(day.encode('ascii')) == 0x4D1FAE0B:
				print(day)
				break
