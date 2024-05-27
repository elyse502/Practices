# Tutorial 46-Python @property

# Demonstrating the use of the property
class Temp_Celsius:
    def __init__(self, temperature = 0):
        print("Assigning temperature value")
        self._temperature = temperature
        self.temp = 500

    def convert_to_fahrenheit(self):
        return (self._temperature * 1.8) + 32
    
    def get_temperature(self):
        print("Getting temperature value")
        return self._temperature
    
    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting temperature value")
        self._temperature = value
    # property() is a built-in function, creates and returns a property object 
    # property(fget=None, fset=None, fdel=None, doc=None)
    # property object has three methods, getter(), setter(), and deleter()
    temperature = property(get_temperature, set_temperature) # assign fget and fset using a single statement
    # make empty property
    #temperature = property()
    # assign fget
    #temperature = temperature.getter(get_temperature)
    # assign fset
    #temperature = temperature.setter(set_temperature)


c = Temp_Celsius(5)    
print(c.temperature)
c.temperature = 100
print(c.temperature)
print(c.__dict__)
print(c.__dict__["_temperature"])
print(c.__dict__["temp"])
print()


# Demonstrating the use of the property as a decorator
class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value


c = Celsius(5)
print(c.temperature)
c.temperature = 100
print(c.temperature)