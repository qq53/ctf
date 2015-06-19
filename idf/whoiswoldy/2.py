#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('sort','r') as f:
	d = []
	i = f.readline().strip()
	k = 1
	while True:
		j = f.readline().strip()
		if not j:
			break
		if int(j) - int(i) < 100:
			k = k + 1
		else:
			if k > 1:
				d.append(i + ' %d' % k)
			i = j
			k = 1
	with open('sort_count','w') as f1:
		f1.write(str(d))
