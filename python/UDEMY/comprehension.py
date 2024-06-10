# Tutorial 40-Python List Comprehension

# Iterating a string through a for loop and adding the letters to a list
h_letters = []

for letter in 'human':
    h_letters.append(letter)
    print(h_letters)

print(h_letters)
print()


# Using comprehension
h_letters = [letter for letter in 'human']

print(h_letters)
print()


# List Comprehensions vs Lambda Function
h_letters = list(map(lambda x: x, 'human'))
print(h_letters)
print()


# If with list comprehension
number_list = [ x for x in range(20) if x % 2 == 0]
print(number_list)
print()


# Nested If with list comprehension
number_list = [ y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(number_list)
print()


# If..Else with list comprehension
obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
print(obj)
print()


# Tansposing a matrix using list comprehension
matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print(transpose)