# Tutorial 17-Python Global Keywords

def funct1():
    x = 20

    def funct2():
        global x    # Global keyword is used to modify a global variable
        x = 25

    print("Before calling funct2: ", x)
    print("Calling funct2 now")
    funct2()
    print("After calling funct2: ", x)

funct1()
print("x in main : ", x)