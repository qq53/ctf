#!/usr/bin/env python3.4

import requests

s = requests.session()
header = {
'Host': 'lab1.xseclab.com',
'Connection': 'keep-alive',
'Cache-Control': 'max-age=0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36',
'DNT': '1',
'Referer': 'http://hackinglab.cn/index_2.php',
'Accept-Encoding': 'gzip, deflate, sdch',
'Accept-Language': 'en;q=0.6',
'Cookie': 'saeut=124.89.2.88.1434295791298139'
		}

s.headers.update(header)
print(s.headers)
r = s.get('http://lab1.xseclab.com/base1_0ef337f3afbe42d5619d7a36c19c20ab/index.php')
r.encoding = 'utf-8'
print(r.text)
