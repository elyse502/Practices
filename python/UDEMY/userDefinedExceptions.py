# Tutorial 28-Python User Defined Exception

class VotersElligibility(Exception):
    def __int__(self):
        super()


try:
    age = int(input("Enter your age: "))
    print("Age is " + str(age))
    if age < 18:
        raise VotersElligibility
except VotersElligibility:
    print("Age is less than 18")
except ValueError:
    print("Age is not numeric")
else:
    print("Age is greater than or equal to 18")
finally:
    print("End of the program")