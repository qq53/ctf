#!/usr/bin/env python3.4

str = 'U8Y]:8KdJHTXRI>XU#?!K_ecJH]kJG*bRH7YJH7YSH]*=93dVZ3^S8*$:8"&:9U]RH;g=8Y!U92\'=j*$KH]ZSj&[S#!gU#*dK9\.'

for i in range(127):
	s = ''
	flag = True
	for j in range(len(str)):
		k = (ord(str[j]) + i)%127
		if k <= 32:
			flag = False
			break
		else:
			s += chr(k)
	if flag:
		print(s)
