#!/usr/bin/python3

"""STARS"""
n = 10
for i in range(n):
	print(' ' * (n-i-1) + '*' * (2*i+1))
print()

m = 5
for i in range(m):
	print("* " * m if i in [0, m-1] else "* " + "  " * (m-2) + "*")

"""Dictionary Technique"""
def get_day(num):
	days = {1: "Mon", 2: "Tue", 3: "Wedn"}
	return days.get(num, "Invalid")

print()
print(get_day(1))
print(get_day(4))
