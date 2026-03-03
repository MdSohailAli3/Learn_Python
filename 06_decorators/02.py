# Problem: Create a decorator to print the function name and the values of its 
# arguments every time the function is called.
def debug(func):
    def wrapper(*args,**kwargs):
        args_value = ', '.join(str(arg) for arg in args) if args else "None" 
        kwargs_value = ', '.join(f"{key} : {value}" for key , value in kwargs.items()) if kwargs else "None"
        print(f"Calling {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        return func(*args,**kwargs)
    return wrapper    
@debug
def hello():
    print("Hello!")
@debug
def add(num1,num2):
    print(num1 + num2)
@debug
def greet(name, greeting = "Wassup!"):
    print(f"Hello {name}, {greeting}.")
@debug
def yo(sir,name="hello",yoyo="world"):
    print(f"name: {name}, yoyo: {yoyo}, sir:{sir}")
hello()
add(2,4)
greet("Johny")
yo("yes",name="honey",yoyo="singh")#Calling yo with args yes and kwargs name : honey, yoyo : singh
