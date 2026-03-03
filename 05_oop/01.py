class Car():
    def __init__(self,brand,model): #self is like the this keyword
        self.brand = brand #init is like an constructor of that class
        self.model = model
car_1 = Car("Tata","Nano")
print(car_1.brand)
print(car_1.model)
car_2 = Car("Buggati","Chiron")
print(car_2.brand)
print(car_2.model)