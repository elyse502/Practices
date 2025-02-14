#!/usr/bin/python3
"""MAP Function"""
names = ["Elysee", "Clement", "Yves", "Placide", "Bruno", "Calvin"]
print(list(map(len, names)))

def stringAppend(name):
	return name + "'s"

print(list(map(stringAppend, names)))
print()

"""FILTER Function"""
def fiveCharLong(name):
	if len(name) > 5:
		return name;
	
Filtered = filter(fiveCharLong, names)
print(list(Filtered))
print()

"""ENUMERATE Function"""
print(list(enumerate(names)))
for index, name in enumerate(names):
	print(f"\t{index}: {name}")
print()

"""ZIP Function"""
age = [24, 22, 21, 20, 25, 23, 30, 19]
newList = list(zip(names, age))
print(newList)

for name, age in newList:
	print(f"\t{name} => {age}")
print()

"""ARGS and KWARGS"""
def summation(*args):
	sum = 0
	for i in args:
		sum += i
	return sum

print(f"\tTHE SUM = {summation(10, 20, 30, 40)}")

def person(**kwargs):
	print(kwargs)
	for key, value in kwargs.items():
		print(f"\t{key}: {value}")
	return 1

person(name="Elysée", age=24, gender="M", status="single")










