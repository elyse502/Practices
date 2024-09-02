# Generate a Random Array
from numpy import random

x = random.randint(100, size=(5))
print(x)

x = random.randint(100, size=(3, 5))
print(x)

x = random.rand(5)
print(x)

x = random.rand(3, 5)
print(x)
