# Tutorial 9-Python Different Modules

# Importing module as well as renaming it
import math as m

print ("The value of pi is", m.pi)


# Usage of from
from math import pi
print("The value of pi is", pi)


# import all names from the standard module math
from math import *
print("The value of e is", e)
print("The value of pi is", pi)