# Tutorial 32-Python Statements And Comments

# This is a comment

# This is a long comment
# and multi-line comments
# can be written like this

"""
Multi-line comments
can also be written like this.
"""


# Statement - Assignment Statement
a = 1

# Multiline Statement
# Explicit line continuation - '\'
b = 1 + 2 + 3 + \
    4 + 5 + 6
print(b)

# Implicit line continuation within brackets
c = (1 + 2 + 3 +
     4 + 5 + 6)
print(c)

# Multiple statements in one line using - ';'
d = 1; e = 3; f = 0


# Code block (body of a function, loop etc.) starts with indentation
# and ends with the first unindented line.
for i in range(1, 10):
    print(i)
    if i == 5:
        break
print("End of the program...")