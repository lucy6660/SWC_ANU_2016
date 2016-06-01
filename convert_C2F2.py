#!/usr/bin/env python

from sys import argv

def celsius_to_fahr(temp_c):
	temp_f=temp_c* (9.0/5.0) + 32
	return temp_f

def main():
	try:
		cels=float(sys.argv[1])
		print(celcius_to_fahr(cels))

	except:
		print("First argument must be a number!")

if __name__ == "__main__":
	main()
