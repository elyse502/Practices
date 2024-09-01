#!/bin/bash

# Create a sample text file
echo -e "John 25\nAlice 30\nBob 22\nJane 28" > data.txt

# Displaying the original content
echo "Original content of data.txt:"
cat data.txt

# Use awk to print names and ages
echo -e "\nUsing awk to process the file:"
awk '{print "Name: " $1, "\tAge: " $2}' data.txt
echo ""



# Sample file
FILE="example.txt"

# Display the original content
echo "Original content of $FILE:"
cat $FILE

# Use sed to replace "sample" with "modified" in the file
sed 's/sample/modified/' $FILE > modified_file.txt

# Display the modified content
echo -e "\nModified content:"
cat modified_file.txt

