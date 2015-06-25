#/usr/bin/env python3.4
# -*- coding: ascii -*-

import base64

s = 'AGV5IULSB3ZLVSE='
f = open('data','w')

def dfs(d, t):
	if d == len(s):
		if r'\x' not in str(base64.b64decode(t.encode('ascii'))):
			f.write(base64.b64decode(t.encode('ascii')).decode('ascii') + '\n')
	else:
		dfs(d + 1, t + s[d])
		if 'A' <= s[d] <= 'Z':
			dfs(d + 1, t + chr(ord(s[d]) - ord('A') + ord('a')))
			
dfs(0, '')
f.close()