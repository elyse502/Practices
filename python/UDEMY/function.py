# Tutorial 22-Python Function Arguments

def findMax(a, b):  # Function taking arguments and returning a value
    if a > b:
        return a
    else:
        return b
    
print("Max number between 100 and 20 is ", findMax(100, 20))


def hello(name, msg = ", how are you?"):    # Function with default parameter
    print("Hello", name, msg)


hello("Agnibha", ", have a nice day.")
hello("Agnibha")


def sumAll(*args):  # Function with arbitray arguments
    sum = 0
    for i in args:
        sum += i
    return sum

print("Sum of all the integers between 1-5 is ", sumAll(1, 2, 3, 4, 5))


def defaultArg(a = 100, b = 200, c = 300):
    print("a = {}, b = {}, c = {}...".format(a, b, c))

defaultArg(10, 20, 30)
defaultArg(10, 20)
defaultArg(10)
defaultArg()
defaultArg(b=222, c=333, a=111)
defaultArg(b=222, a=111)