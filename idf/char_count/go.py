#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

import re, requests

s = requests.session()
data = s.get('http://ctf.idf.cn/game/pro/37').text
hr = re.findall(r'<hr />\s*(.+?)\s*<hr />', data, re.S)[0]
l = {'w':0, 'o':0, 'l':0, 'd':0, 'y':0}
for i in hr:
	if i in l:
		l[i] = l[i] + 1
key = '%d%d%d%d%d' % (l['w'], l['o'], l['l'], l['d'], l['y'])
params = {'anwser': key}
result = s.post('http://ctf.idf.cn/game/pro/37', data=params);
print(result.text)
