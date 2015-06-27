#!/usr/bin/env python3.4

import requests

s = requests.session()

with open('netbarcard.dump','rb') as f:
	fd = bytearray(f.read())

fd[0] = 0x8a
data = {'userfile': ('netbarcard.dump',fd,'application/octet-stream')}
r = s.post('http://lab1.xseclab.com/password2_454a7a7cb7213e14695c022cfb04141c/upload.php',files=data)
if '异常' not in r.text:
	print(r.text)
