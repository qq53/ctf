#!/usr/bin/env python3.4

import requests, re

s = requests.session()
r = s.get('http://ctf8.simplexue.com/jia/index.php')
r.encoding = 'gbk'
data = re.findall(r"<div name='my_expr'>(.+)</div>", r.text)[0]
data = data.replace('x','*')
value = {'pass_key':eval(data)}
r = s.post('http://ctf8.simplexue.com/jia/index.php?action=check_pass', data=value)
r.encoding = 'gbk'
print(r.text)
