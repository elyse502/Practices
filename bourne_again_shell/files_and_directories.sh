#!/bin/bash

# Create a file
touch file.txt

# Write to a file
echo "This is some content." > file.txt

# Append to a file
echo "Appending additional content." >> file.txt


# Read from a file
cat file.txt

# Copy the file
cp file.txt copied_file.txt

# Move/Rename the file
mv copied_file.txt renamed_file.txt

# Delete the file
rm renamed_file.txt

echo "File operations completed."
ls
echo ""


# Create a directory
mkdir example_directory

# Changing directory
cd example_directory

# Creating files inside the directory
echo "File inside the directory." > file_inside.txt
echo "Another file inside the directory." > another_file.txt
ls
cat file_inside.txt && cat another_file.txt
echo ""

# Going back to the parent directory
cd ..

# Copying the directory
cp -r example_directory copied_example_directory
echo "Listing contents of the parent directory:"
ls

# Moving/Renaming the copied directory
mv copied_example_directory renamed_example_directory

# Listing contents of the parent directory after renaming
echo -e "\nListing contents after renaming:"
ls

# Deleting the directory
rm -rf renamed_example_directory

echo -e "\nDirectory operations completed."

