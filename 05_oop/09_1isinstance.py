class Car():

    def __init__(self,brand="null",model="null"): #self is like the this keyword
        self.brand = brand # __ is used to make private attributes
        self.model = model
       
class Electric_car(Car):
    def __init__(self, brand= "null", model="null", battery_power="null"):
        super().__init__(brand, model)
        self.battery_power = battery_power
    def details(self):
        return f"{self.brand} {self.model} {self.battery_power}"
my_car = Car("BMW", "M4")

print(isinstance(my_car,Car))#true
print(isinstance(my_car,Electric_car))#false

ev_car = Electric_car()
print(isinstance(ev_car,Electric_car))#true
print(isinstance(ev_car,Car))#true

# print(ev_car.details())# null null null