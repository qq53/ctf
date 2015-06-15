#!/usr/bin/env python3.4

import requests

s = requests.session()
header = {
'Host': 'lab1.xseclab.com',
'Connection': 'keep-alive',
'Cache-Control': 'max-age=0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'User-Agent': 'HAHA',
'DNT': '1',
'X-Forwarded-For':'127.0.0.1',
'Referer': 'http://hackinglab.cn/index_2.php',
'Accept-Encoding': 'gzip, deflate, sdch',
'Accept-Language': 'en;q=0.6',
'Cookie': 'saeut=124.89.2.88.1434295791298139'
		}

s.headers.update(header)
print(s.headers)
r = s.get('http://lab1.xseclab.com/base11_0f8e35973f552d69a02047694c27a8c9/index.php')
r.encoding = 'utf-8'
print(r.text)
