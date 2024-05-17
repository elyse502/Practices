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