#!/usr/bin/python3

"""STARS"""
n = 10
for i in range(n):
	print(' ' * (n-i-1) + '*' * (2*i+1))
print()

m = 5
for i in range(m):
	print("* " * m if i in [0, m-1] else "* " + "  " * (m-2) + "*")
