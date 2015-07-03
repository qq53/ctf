#!/usr/bin/env python3.4

import re, itertools

with open('data','r') as f:
	data = f.read().strip()
w = re.split('[^a-zA-Z]+',data)
count = {}
for i in w:
	count.setdefault(i,0)
	count[i] += 1
s = sorted(count.items(), key=lambda x: x[1], reverse=True)
w3 = [i for i in s if len(i[0])==3][:3]
w1 = [i for i in s if len(i[0])==1][:4]
print(w3)
print(w1)
offset = {}
the = 'THE'
for i in w3:
	c = 0
	for j in i[0]:
		key = (ord(the[c])-ord(j)) % 26
		offset.setdefault(key,0)
		offset[key] += 1
		c += 1
for i in w1:
	for j in i[0]:
		key = (ord('A')-ord(j)) % 26
		offset.setdefault(key,0)
		offset[key] += 1
		key = (ord('I')-ord(j)) % 26
		offset.setdefault(key,0)
		offset[key] += 1
offset = list(filter(lambda x:x[1]>1,offset.items()))
offset = [i[0] for i in offset]
test = 'EB BMQF KYJRD'
A = list(itertools.permutations(offset))
for i in A:
	t = ''
	for j in range(len(test)):
		if 'A' <= test[j] <= 'Z':
			t += chr((ord(test[j])+i[j%len(i)]-ord('A'))%26+ord('a'))
		else:
			t += test[j]
	#print(t+' offset: '+str(i))
offset_final = [4,12,15,23,2]
t = ''
i = 0
for j in data:
	if 'A' <= j <= 'Z':
		t += chr((ord(j)+offset_final[i%len(offset_final)]-ord('A'))%26+ord('a'))
	else:
		t += j
	i += 1
print(t)
