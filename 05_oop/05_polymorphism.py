class Car():
    def __init__(self,brand,model): #self is like the this keyword
        self.__brand = brand # __ is used to make private attributes
        self.__model = model
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    def get_brand(self):
        return self.__brand
    def fuel_type(self):
        return "Petrol/Diesel"

class Electric_car(Car):
    def __init__(self, brand, model, battery_power):
        super().__init__(brand, model)
        self.battery_power = battery_power
    def fuel_type(self):
        return "Elcetric charge"

my_ev = Electric_car("Tesla","Y", "90kWh")
car = Car("BMW", "M4")
print(my_ev.full_name(),my_ev.fuel_type())
print(car.full_name(),car.fuel_type())
