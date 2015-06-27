#!/usr/bin/env python

import re

key = '02070D48030F1C294940041801181C0C140D0A0A20253A3B'

def decrypt( ep ):
	"""Cisco Type 7 password decryption.  Converted from perl code that was  
	written by jbash /|at|\ cisco.com"""

	xlat = ( 0x64, 0x73, 0x66, 0x64, 0x3b, 0x6b, 0x66, 0x6f, 0x41, 0x2c, 
		   0x2e, 0x69, 0x79, 0x65, 0x77, 0x72, 0x6b, 0x6c, 0x64, 0x4a, 
		   0x4b, 0x44, 0x48, 0x53, 0x55, 0x42 )

	dp = ""
	regex = re.compile( "^(..)(.+)" )
	if not ( len(ep) & 1 ):
		result = regex.search( ep )
	try:
		s, e = int( result.group(1) ), result.group(2)
	except ValueError:
	# typically get a ValueError for int( result.group(1))) because
	# the method was called with an unencrypted password.  For now
	# SILENTLY bypass the error
		s, e = (0, "")
	for ii in range( 0, len( e ), 2 ):
		# int( blah, 16) assumes blah is base16... cool
		magic  = int( re.search( ".{%s}(..)" % ii, e ).group(1), 16 )
		print "S = %s" % s
		if s <= 25:
		# Algorithm appears unpublished after s = 25
			newchar = "%c" % ( magic ^ int( xlat[ int( s  ) ] ) )
		else:
			newchar = "?"
		dp = dp + str( newchar )
		s = s + 1
	if s > 25:
		print "WARNING: password decryption failed."
	return dp

print(decrypt(key))
