# True False
print(5 == 5)
print(5 > 5)


# None
print(None == 0)
print(None == False)
print(None == [])
print(None == None)


def a_void_function():
    a = 1
    b = 2
    c = a + b
    # return (c)

x = a_void_function()
print(x)


# and, or, not
print(True and False)
print(True or False)
print(not False)

print(True and True)
print(True or True)
print(not True)


# as
import math as myMath
print(myMath.cos(myMath.pi))


# assert
# assert 5 > 5 # AssertionError
assert 5 > 4
assert 5 == 5


# break
for i in range(1, 11):
    if i == 5:
        break
    print(i)


# continue