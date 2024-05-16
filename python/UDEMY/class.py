class MyComplexNumber:
    # Constructor methods
    def __init__(self, real = 0, imag = 0):
        print("MyComplexNumber constructor executing...")
        self.real_part = real
        self.imaginary_part = imag

    def displayComplex(self):
        print("{0} + {1}j".format(self.real_part, self.imaginary_part))


# Create a new object against MyComplexNumber class
cmplx1 = MyComplexNumber(40, 50)

# Calling displayComplex() function
# Output: 40 + 50j
cmplx1.displayComplex()

# Create another object against MyComplexNumber class
# and create a new attribute 'new_attribute'
cmplx2 = MyComplexNumber(60, 70)
cmplx2.new_attribute = 80
cmplx2.displayComplex()

# Output: (60, 70, 80)
print((cmplx2.real_part, cmplx2.imaginary_part, cmplx2.new_attribute))

# but cmplx1 object doesn't have attribute 'new_attribute
# AttributeError: 'MyComplexNumber' object has no attribute 'new_attribute'
# cmplx1.new_attribute

# Deleting object attributes and the object itself
print(cmplx1)
del cmplx1.real_part
del cmplx1

# print(cmplx1) # NameError: name 'cmplx1' is not defined