# In Python, enumerate() is a built-in function that lets you loop through an iterable (like a list, tuple, or string) and automatically keep track of the index of each item.

# Instead of manually writing something like:

# python
i = 0
for value in my_list:
    print(i, value)
    i += 1
    
# You can do:
for i, value in enumerate(my_list):
    print(i, value)

# Syntax
enumerate(iterable, start=0)
# iterable → the sequence you want to loop through.

# start → the index at which enumeration should begin (default is 0).

# Example
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
# Output:

# 1 apple
# 2 banana
# 3 cherry


# Here:
# index comes from enumerate

# fruit is the actual item from the list

# ✅ When to use enumerate()?

# When you need both the index and the value in a loop.

# It makes your code shorter, cleaner, and avoids manual index tracking.