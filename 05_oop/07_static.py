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
print(Car.general_description())