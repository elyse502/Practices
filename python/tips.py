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
def print_day_of_week(day_number):
    days_of_week = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
    }
    
    return days_of_week.get(day_number, 'Invalid number')

print()
print(print_day_of_week(1))
print(print_day_of_week(7))
print(print_day_of_week(8))
