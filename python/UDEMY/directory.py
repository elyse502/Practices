# Tutorial 10-Directory And File Management
import os
print(os.getcwd())  # Returns the present working directory
print(os.getcwdb()) # Returns the present working directory as a byte object


os.chdir('/home/elysee_niyibizi/Practices/')  # used to change directory
print(os.listdir()) # All files and sub directories inside a directory
                    # can be known using the listdir() method.
print(os.getcwd())  # Returns the present working directory


# used to make a new directory
os.mkdir('Test')


# used to rename a directory
os.rename('Test', 'New_One')


# Removing a file and a directory
os.remove('Test.txt')   # used to remove a file
os.rmdir('New_One') # used to remove a directory


os.chdir('/home/elysee_niyibizi/Practices/python/UDEMY')