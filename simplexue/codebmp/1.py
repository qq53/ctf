#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

import requests, os, sys, pytesseract
from PIL import Image

l = {}
def getcode(path):
	im = Image.open('bmp/'+path)
	w, h = im.size
	oim = im = im.resize((w*2, h*2))
	im = pytesseract.image_to_string(im,config="-psm 8")
	im = im.replace(' ','')
	l[path] = im
	if str.isnumeric(im) == False:
		print(path + ' - ' + im)
		oim.save(path)
	return im

for d in os.listdir('bmp'):
	getcode(d)
