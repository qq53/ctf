#!/usr/bin/env python3.4

import requests, re

s = requests.session()
r = s.get('http://lab1.xseclab.com/xss2_0d557e6d2a4ac08b749b61473a075be1/index.php')
r.encoding = 'utf-8'
data = re.findall(r'<br/>(.+?)<', r.text, re.S)[0]
data = re.findall(r'(\d.+?)=', data)[0]
value = {'v':eval(data)}
r = s.post('http://lab1.xseclab.com/xss2_0d557e6d2a4ac08b749b61473a075be1/index.php', data=value)
r.encoding = 'utf-8'
print(r.text)
