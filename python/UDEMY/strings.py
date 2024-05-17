# Tutorial 12- Python Strings

# differrent ways to define a string in python
mystr1 = 'Welcome'
print(mystr1)

mystr2 = "Welcome"
print(mystr2)

mystr3 = '''Welcome'''
print(mystr3)


# triple quotes string can extend multiple lines
mystr3 = """Welcome 
to the world of 
Python Programming"""
print(mystr3)


# accessing characters in a string
mystr = 'language'
print('mystr = ', mystr)

print('mystr[0] = ', mystr[0])
print('mystr[-1] = ', mystr[-1])
print('mystr[1:5] = ', mystr[1:5])
print('mystr[5:-2] = ', mystr[5:-2])
# print('mystr[10] = ', mystr[10]) # IndexError: string index out of range


# strings are immutable
# but different strings can be assigned

mystr = 'language'
print(mystr)

mystr = 'programming'
print(mystr)

# mystr[3] = 'x'  # TypeError: 'str' object does not support item assignment


# concatenation of strings

mystr1 = 'Welcome'
mystr2 = ' to all'

# using +
print('mystr1 + mystr2 = ', mystr1 + mystr2)

# using *
print('mystr1 * 3 = ', mystr1 * 3)


# iterating though a string
letter_count = 0
for letters in 'Hello World':
    if letters == 'l':
        letter_count += 1
print(letter_count, 'times l letters has been found')


# string membership
print('l' in 'hello')
print('l' not in 'hello')
print('b' in 'hello')
print('b' not in 'hello')


# built-in functions with string
mystr = 'university'

# using enumarate()
my_list_enumerate = list(enumerate(mystr))
print('list(enumerate(mystr)) = ', my_list_enumerate)

# using character count
print('len(mystr) = ', len(mystr))


# string formatting using escape sequence
# print("tell me "what's your name?"")

# using triple quotes
print('''tell me "what's your name?"''')

# escaping single quotes
print('tell me "what\'s your name?"')

# escaping double quotes
print("tell me \"what's your name?\"")

print("c:\\User\\user\\mydata.txt")
print("this line is having a new line \ncharacter")
print("this line is having a tab \t character")
print("ABC written in \x41\x42\x43 (HEX) representation")


# format() method for string formatting
# default(implicit) order
default_order = "{} {} and {}".format('Today', 'is', 'Sunday')
print(default_order)

# order using positional argument
positional_order = "{1} {0} and {2}".format('is', 'Today', 'Sunday')
print(positional_order)

# order using keyword argument
keyword_order = "{t} {i} and {s}".format(i='is', t='Today', s='Sunday')
print(keyword_order)


# formatting numbers
print("Required binary representation of {0} is {0:b}".format(20))

# formatting floats
print("Exponential representation of {0} is {0:e}".format(1566.345))

# round off
print("One third is: {0:.3f}".format(1/3))


# string methods
print("gOOD moRNing tO alL".lower())
print("gOOD moRNing tO alL".upper())
print("gOOD moRNing tO alL".title())
print("gOOD moRNing tO alL".capitalize())
print("gOOD moRNing tO alL".find('tO'))
print("gOOD moRNing tO alL".find('to'))
print("gOOD moRNing tO alL".replace('alL', 'everybody'))
print("gOOD moRNing tO alL".replace('all', 'everybody'))
print("gOOD moRNing tO alL".split())
