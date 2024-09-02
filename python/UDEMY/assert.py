# Tutorial 45-Python Assert

def avg(marks):
    assert len(marks) != 0
    return sum(marks)/len(marks)

mark1 = [11, 22, 33]
print("Average of mark1:", avg(mark1))

mark1 = []
# print("Average of mark1:", avg(mark1))  # This will throw an error
print()


# Using assert with error message
def avg(marks):
    assert len(marks) != 0, "List is empty"
    return sum(marks)/len(marks)

mark2 = [55, 88, 78, 90, 79]
print("Average of mark2:", avg(mark2))

mark1 = []
print("Average of mark1:", avg(mark1))  # This will throw an error with the error message "List is empty" we provided