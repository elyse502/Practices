# Tutorial 13- Python Data Type Conversion

# Implicit Type Conversion
num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("datatype of num_int:", type(num_int))
print("datatype of num_flo:", type(num_flo))

print("Value of num_new:", num_new)
print("datatype of num_new:", type(num_new))


# Addition of string(higher) data type and integer(lower) datatype
num_int = 123
num_str = "456"

print("Data type of num_int:", type(num_int))
print("Data type of num_str:", type(num_str))
# Error: Implicit conversion will not work here
# print(num_int + num_str)


# Explicit Type Conversion
num_int = 123
num_str = "456"

print("Data type of num_int:", type(num_int))
print("Data type of num_str before Type Casting:", type(num_str))

num_str = int(num_str)  # Converting string to integer
print("Data type of num_str after Type Casting:", type(num_str))

num_sum = num_int + num_str

print("Sum of num_int and num_str:", num_sum)
print("Data type of the sum:", type(num_sum))