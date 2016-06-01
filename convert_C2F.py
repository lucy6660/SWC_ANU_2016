#!/usr/bin/env python


import sys

try:
	temp_f = (float(sys.argv[1]) * 1.8 + 32)

	print('The temperature in fahrenhit is: ', temp_f) 

except:
	print('The input is not a number')
