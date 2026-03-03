class Car():
    def __init__(self,brand,model): #self is like the this keyword
        self.brand = brand #init is like an constructor of that class
        self.model = model
    def full_name(self):
        return f"{self.brand} {self.model}"
# car_1 = Car("Tata","Nano")
# print(car_1.brand)
# print(car_1.model)
# print(car_1.full_name())
# car_2 = Car("Buggati","Chiron")
# print(car_2.brand)
# print(car_2.model)
# print(car_2.full_name())
class Electric_car(Car):
    def __init__(self, brand, model, battery_power):
        super().__init__(brand, model)
        self.battery_power = battery_power
    def full_name(self):
        return super().full_name() + f" {self.battery_power}"  #just tried myself without learning and it actually works
my_ev = Electric_car("Tesla","Y", "90kWh")
print(my_ev.battery_power)
print(my_ev.full_name())