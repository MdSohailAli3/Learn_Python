#Property-Decorator: it is used to denied the modification in varable
#used to access the method like an attribute to get clean code
# ex - callinng value is clean as calling get_value
#Decorators
class Car():
    total_car = 0
    def __init__(self,brand,model): #self is like the this keyword
        self.__brand = brand # __ is used to make private attributes
        self.__model = model
        Car.total_car += 1
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    def get_brand(self):
        return self.__brand
    @property
    def model(self):
        return self.__model
    def fuel_type(self):
        return "Petrol/Diesel"
    @staticmethod
    def general_description():#no need of self, because it cannot be called using object
        return "Cars are the means of transport"
class Electric_car(Car):
    def __init__(self, brand, model, battery_power):
        super().__init__(brand, model)
        self.battery_power = battery_power
    def fuel_type(self):
        return "Elcetric charge"

my_car = Car("BMW", "M4")
print(my_car.model)#M4 #we does not need to run using () because we using decorator
# my_car.model= "C3"
# print(my_car.model())#error because no setter
