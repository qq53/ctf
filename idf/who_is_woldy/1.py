#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def findSubStr(s,d):
	indexes = []
	subLen = len(s)
	fullLen = len(d)
	for i in range(fullLen - subLen + 1):
		if d[i:i+subLen] == s:
			indexes.append(i)
			i = i + subLen
	return indexes

with open('whoiswoldy.txt','r') as f:
	d = f.read();
	places = []
	with open('2000words.txt','r') as f1:
		while True:
			s = f1.readline().strip();
			if not s:
				break
			places += findSubStr(s,d)
	with open('data','w') as f2:
		f2.write(str(places))
