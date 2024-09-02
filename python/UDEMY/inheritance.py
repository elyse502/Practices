# Tutorial 20-Python Inheritance

# Creating Class and Object in Python
class myBird:

    def __init__(self):
        print("myBird class constructor is executing...")

    def whatType(self):
        print("I am a Bird...")

    def canSwim(self):
        print("I can swim...")


# myPenguin class inheriting the attributes from the myBird class
class myPenguin(myBird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("myPenguin class constructor is executing...")

    def whoIsThis(self):
        print("I am a Penguin...")

    def canRun(self):
        print("I can run faster...")


# Accesing the child class's attributes(Inheritance)
pg1 = myPenguin()
pg1.whatType()      # defined in myBird class
pg1.whoIsThis()     # defined in myPenguin class
pg1.canSwim()       # defined in myBird class
pg1.canRun()        # defined in myPenguin class


# polymorphism
class MyParrot:

    def canFly(self):
        print("Parrot can fly...")

    def canSwim(self):
        print("Parrot can't swim...")


class MyPenguin:

    def canFly(self):
        print("Penguin can't fly...")

    def canSwim(self):
        print("Penguin can swim...")


# common interface
def flying_bird_test(bird):
    bird.canFly()
    bird.canSwim()

# instantiate objects
bird_parrot = MyParrot()
bird_penguin = MyPenguin()

# passing the object
flying_bird_test(bird_parrot)
print()
flying_bird_test(bird_penguin)