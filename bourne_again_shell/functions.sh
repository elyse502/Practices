#!/bin/bash

# Function to add two numbers
add_numbers() {
	echo "Sum: $(($1 + $2))"
}
# Example: call the function with two numbers (e.g., 3 and 4)
add_numbers 3 4

# Function to subtract two numbers
subtract_numbers() {
	echo "Subtraction: $(($1 - $2))"
}
subtract_numbers 10 2

