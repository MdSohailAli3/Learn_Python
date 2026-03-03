#1
# def square(number):
#         return number ** 2
# print(square(6))
#---------------------------------------

# #2
# def add(number_one, number_two):
#         return number_one + number_two
# print(add(60,9))
#---------------------------------------

# #3
# def multiply(parmeter_one, parameter_two):
#         return parmeter_one * parameter_two
# print(multiply(5,"yo"))
#--------------------------------------

#4
# import math
# def circle(radius):
#         area = math.pi * radius ** 2
#         circumference = 2 * math.pi * radius
#         return area, circumference
# area , circumference = circle(3)
# print("Area: ",round(area,2),"Circumference: ",round(circumference,2))
#--------------------------------------

#5
# def greet(name = "User"):
#     print("Hello ",name,", How's your day going..")
# greet()
#--------------------------------------
#

# #6
# cube = lambda x: x ** 3
# print(cube(3))
# #------
# another = cube
# print(another(3))
#-------------------------------------------

#7
# def sum_all(*args):
#     return sum(args)
# print(sum_all())
# print(sum_all(2,3))
# print(sum_all(2,3,4))
# print(sum_all(2,3,4,5))
#-------------------------------------------

#8
# def print_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")
# print_kwargs(name="hell",power="fire")
# print_kwargs(name="Son",power="Off",enemy="Witch")
#------------------------------------------------

# #9
# def even_generator(limit):
#     for i in range(2, limit + 1, 2):
#         yield i
# for num in even_generator(10):
#     print(num, end=" ") #2 4 6 8 10
#-------------------------------------------------

#10
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)
print(factorial(5))