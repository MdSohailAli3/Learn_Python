# Q1
# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

# age = int(input("Enter your age: "))
# if age < 13:
#     print("You are an Child.")
# elif age < 20:
#     print("You are an Teenager.")
# elif age < 60:
#     print("You are an Adult.")
# else :
#     print("You are an Senior.")
#----------------------------------------------------

#Q2
# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), 
# $8 for children. Everyone gets a $2 discount on Wednesday.
# import random as rd
# age = int(input("Enter your age: "))
# weekdays = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
# current_day = rd.choice(weekdays)
# discount = 0
# price = 12 #or  price = 12 if age >= 18 else 8
# message =  "Your movie tickets price will be:\nPrice: {}\nDiscount: {}\nTotal: {}"
# if current_day == "Wednesday":
#     discount = 2
# if age < 18:
#     price = 8
# price_after_discount = price - discount
# print(message.format(price,discount,price_after_discount))
#-----------------------------------------------------------------------

# Q3
# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

# score = int(input("Enter your score(0-100): "))
# if score >= 90:
#     print("Your Grade is: A")
# elif score >= 80:
#     print("Your Grade is: B")
# elif score >= 70:
#     print("Your Grade is: C")
# elif score >= 60:
#     print("Your Grade is: D")
# else:
#     print("Your Grade is: f")
#--------------------------------------------

# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color.
#  (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

# colour = input("Enter you fruit colour (Green, Yellow, Brown): ")
# if colour == "Green":
#     print("Unrip")
# elif colour == "Yellow":
#     print("Ripe")
# elif colour == "Brown":
#     print("Overripe")
#------------------------------------

# Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

# Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).


# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.
# 

# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).


# Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

# Problem: Recommend a type of pet food based on the pet's species and age.
#  (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).
