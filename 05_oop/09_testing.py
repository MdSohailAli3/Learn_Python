class Car():

    def __init__(self,brand,model): #self is like the this keyword
        self.__brand = brand # __ is used to make private attributes
        self.__model = model
    
my_car = Car("BMW", "M4")
# print(my_car.brand)#error in both brand or __brand
#how to access 
print(my_car._Car__brand)#BMW
#so it is still possible to access private atributes, python just make it harder by changing its name internally


#and we can use just self._brand = brand ,as an naming convention
#it is still accessible ,but it is used to tell the devs that this is not recommend to use outside
#it is just an naming convention used in python


