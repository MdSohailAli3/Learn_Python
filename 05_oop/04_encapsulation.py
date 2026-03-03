class Car():
    def __init__(self,brand,model): #self is like the this keyword
        self.__brand = brand # __ is used to make private attributes
        self.__model = model
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    def get_brand(self):
        return self.__brand

class Electric_car(Car):
    def __init__(self, brand, model, battery_power):
        super().__init__(brand, model)
        self.battery_power = battery_power
    
my_ev = Electric_car("Tesla","Y", "90kWh")
print(my_ev.battery_power)
print(my_ev.full_name())
# print(my_ev.__brand) ->will not work, we used getter
print(my_ev.get_brand())