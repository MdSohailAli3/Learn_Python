class Engine():
    def engine(self):
        return "This is engine"
class Battery():
    def battery(self):
        return "This is battery"
class Electric_car(Engine,Battery):
    pass
ev_car = Electric_car()
print(ev_car.battery())
print(ev_car.engine())